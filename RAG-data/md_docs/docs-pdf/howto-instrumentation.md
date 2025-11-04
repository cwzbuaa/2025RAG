### 第1页

Instrumenting CPython with DTrace
and SystemTap
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Enablingthestaticmarkers 2
2 StaticDTraceprobes 3
3 StaticSystemTapmarkers 4
4 Availablestaticmarkers 5
5 SystemTapTapsets 6
6 Examples 7
author
DavidMalcolm
author
ŁukaszLanga
DTrace and SystemTap are monitoring tools, each providing a way to inspect what the processes on a computer
systemaredoing. Theybothusedomain-specificlanguagesallowingausertowritescriptswhich:
• filterwhichprocessesaretobeobserved
• gatherdatafromtheprocessesofinterest
• generatereportsonthedata
AsofPython3.6,CPythoncanbebuiltwithembedded“markers”,alsoknownas“probes”,thatcanbeobservedby
aDTraceorSystemTapscript,makingiteasiertomonitorwhattheCPythonprocessesonasystemaredoing.
CPython implementation detail: DTrace markers are implementation details of the CPython interpreter. No
guaranteesaremadeaboutprobecompatibilitybetweenversionsofCPython. DTracescriptscanstopworkingor
workincorrectlywithoutwarningwhenchangingCPythonversions.
1

### 第2页

1 Enabling the static markers
macOScomeswithbuilt-insupportforDTrace. OnLinux,inordertobuildCPythonwiththeembeddedmarkers
forSystemTap,theSystemTapdevelopmenttoolsmustbeinstalled.
OnaLinuxmachine,thiscanbedonevia:
$ yum install systemtap-sdt-devel
or:
$ sudo apt-get install systemtap-sdt-dev
CPythonmustthenbeconfigured with the --with-dtrace option:
checking for --with-dtrace... yes
OnmacOS,youcanlistavailableDTraceprobesbyrunningaPythonprocessinthebackgroundandlistingallprobes
madeavailablebythePythonprovider:
$ python3.6 -q &
$ sudo dtrace -l -P python$! # or: dtrace -l -m python3.6
ID PROVIDER MODULE FUNCTION NAME
29564 python18035 python3.6 _PyEval_EvalFrameDefault function-entry
29565 python18035 python3.6 dtrace_function_entry function-entry
29566 python18035 python3.6 _PyEval_EvalFrameDefault function-
,→return
29567 python18035 python3.6 dtrace_function_return function-
,→return
29568 python18035 python3.6 collect gc-done
29569 python18035 python3.6 collect gc-start
29570 python18035 python3.6 _PyEval_EvalFrameDefault line
29571 python18035 python3.6 maybe_dtrace_line line
On Linux, you can verify if the SystemTap static markers are present in the built binary by seeing if it contains a
“.note.stapsdt”section.
$ readelf -S ./python | grep .note.stapsdt
[30] .note.stapsdt NOTE 0000000000000000 00308d78
Ifyou’vebuiltPythonasasharedlibrary(withthe--enable-sharedconfigureoption),youneedtolookinstead
withinthesharedlibrary. Forexample:
$ readelf -S libpython3.3dm.so.1.0 | grep .note.stapsdt
[29] .note.stapsdt NOTE 0000000000000000 00365b68
Sufficientlymodernreadelfcanprintthemetadata:
$ readelf -n ./python
Displaying notes found at file offset 0x00000254 with length 0x00000020:
Owner Data size Description
GNU 0x00000010 NT_GNU_ABI_TAG (ABI version tag)
OS: Linux, ABI: 2.6.32
Displaying notes found at file offset 0x00000274 with length 0x00000024:
Owner Data size Description
GNU 0x00000014 NT_GNU_BUILD_ID (unique build ID␣
(continuesonnextpage)
2

### 第3页

(continuedfrompreviouspage)
,→bitstring)
Build ID: df924a2b08a7e89f6e11251d4602022977af2670
Displaying notes found at file offset 0x002d6c30 with length 0x00000144:
Owner Data size Description
stapsdt 0x00000031 NT_STAPSDT (SystemTap probe␣
,→descriptors)
Provider: python
Name: gc__start
Location: 0x00000000004371c3, Base: 0x0000000000630ce2, Semaphore:␣
,→0x00000000008d6bf6
Arguments: -4@%ebx
stapsdt 0x00000030 NT_STAPSDT (SystemTap probe␣
,→descriptors)
Provider: python
Name: gc__done
Location: 0x00000000004374e1, Base: 0x0000000000630ce2, Semaphore:␣
,→0x00000000008d6bf8
Arguments: -8@%rax
stapsdt 0x00000045 NT_STAPSDT (SystemTap probe␣
,→descriptors)
Provider: python
Name: function__entry
Location: 0x000000000053db6c, Base: 0x0000000000630ce2, Semaphore:␣
,→0x00000000008d6be8
Arguments: 8@%rbp 8@%r12 -4@%eax
stapsdt 0x00000046 NT_STAPSDT (SystemTap probe␣
,→descriptors)
Provider: python
Name: function__return
Location: 0x000000000053dba8, Base: 0x0000000000630ce2, Semaphore:␣
,→0x00000000008d6bea
Arguments: 8@%rbp 8@%r12 -4@%eax
The above metadata contains information for SystemTap describing how it can patch strategically placed machine
codeinstructionstoenablethetracinghooksusedbyaSystemTapscript.
2 Static DTrace probes
ThefollowingexampleDTracescriptcanbeusedtoshowthecall/returnhierarchyofaPythonscript,onlytracing
withintheinvocationofafunctioncalled“start”. Inotherwords,import-timefunctioninvocationsarenotgoingto
belisted:
self int indent;
python$target:::function-entry
/copyinstr(arg1) == "start"/
{
self->trace = 1;
}
python$target:::function-entry
/self->trace/
{
printf("%d\t%*s:", timestamp, 15, probename);
printf("%*s", self->indent, "");
(continuesonnextpage)
3

### 第4页

(continuedfrompreviouspage)
printf("%s:%s:%d\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
self->indent++;
}
python$target:::function-return
/self->trace/
{
self->indent--;
printf("%d\t%*s:", timestamp, 15, probename);
printf("%*s", self->indent, "");
printf("%s:%s:%d\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
}
python$target:::function-return
/copyinstr(arg1) == "start"/
{
self->trace = 0;
}
Itcanbeinvokedlikethis:
$ sudo dtrace -q -s call_stack.d -c "python3.6 script.py"
Theoutputlookslikethis:
156641360502280 function-entry:call_stack.py:start:23
156641360518804 function-entry: call_stack.py:function_1:1
156641360532797 function-entry: call_stack.py:function_3:9
156641360546807 function-return: call_stack.py:function_3:10
156641360563367 function-return: call_stack.py:function_1:2
156641360578365 function-entry: call_stack.py:function_2:5
156641360591757 function-entry: call_stack.py:function_1:1
156641360605556 function-entry: call_stack.py:function_3:9
156641360617482 function-return: call_stack.py:function_3:10
156641360629814 function-return: call_stack.py:function_1:2
156641360642285 function-return: call_stack.py:function_2:6
156641360656770 function-entry: call_stack.py:function_3:9
156641360669707 function-return: call_stack.py:function_3:10
156641360687853 function-entry: call_stack.py:function_4:13
156641360700719 function-return: call_stack.py:function_4:14
156641360719640 function-entry: call_stack.py:function_5:18
156641360732567 function-return: call_stack.py:function_5:21
156641360747370 function-return:call_stack.py:start:28
3 Static SystemTap markers
Thelow-levelwaytousetheSystemTapintegrationistousethestaticmarkersdirectly. Thisrequiresyoutoexplicitly
statethebinaryfilecontainingthem.
Forexample,thisSystemTapscriptcanbeusedtoshowthecall/returnhierarchyofaPythonscript:
probe process("python").mark("function__entry") {
filename = user_string($arg1);
funcname = user_string($arg2);
lineno = $arg3;
(continuesonnextpage)
4

### 第5页

(continuedfrompreviouspage)
printf("%s => %s in %s:%d\\n",
thread_indent(1), funcname, filename, lineno);
}
probe process("python").mark("function__return") {
filename = user_string($arg1);
funcname = user_string($arg2);
lineno = $arg3;
printf("%s <= %s in %s:%d\\n",
thread_indent(-1), funcname, filename, lineno);
}
Itcanbeinvokedlikethis:
$ stap \
show-call-hierarchy.stp \
-c "./python test.py"
Theoutputlookslikethis:
11408 python(8274): => __contains__ in Lib/_abcoll.py:362
11414 python(8274): => __getitem__ in Lib/os.py:425
11418 python(8274): => encode in Lib/os.py:490
11424 python(8274): <= encode in Lib/os.py:493
11428 python(8274): <= __getitem__ in Lib/os.py:426
11433 python(8274): <= __contains__ in Lib/_abcoll.py:366
wherethecolumnsare:
• timeinmicrosecondssincestartofscript
• nameofexecutable
• PIDofprocess
andtheremainderindicatesthecall/returnhierarchyasthescriptexecutes.
Fora--enable-sharedbuildofCPython,themarkersarecontainedwithinthelibpythonsharedlibrary,andthe
probe’sdottedpathneedstoreflectthis. Forexample,thislinefromtheaboveexample:
probe process("python").mark("function__entry") {
shouldinsteadread:
probe process("python").library("libpython3.6dm.so.1.0").mark("function__entry") {
(assumingadebugbuildofCPython3.6)
4 Available static markers
function__entry(str filename, str funcname, int lineno)
This marker indicates that execution of a Python function has begun. It is only triggered for pure-Python
(bytecode)functions.
Thefilename,functionname,andlinenumberareprovidedbacktothetracingscriptaspositionalarguments,
whichmustbeaccessedusing$arg1,$arg2,$arg3:
• $arg1: (const char *)filename,accessibleusinguser_string($arg1)
• $arg2: (const char *)functionname,accessibleusinguser_string($arg2)
5

### 第6页

• $arg3: intlinenumber
function__return(str filename, str funcname, int lineno)
Thismarkeristheconverseoffunction__entry(),andindicatesthatexecutionofaPythonfunctionhas
ended(eitherviareturn,orviaanexception). Itisonlytriggeredforpure-Python(bytecode)functions.
Theargumentsarethesameasforfunction__entry()
line(str filename, str funcname, int lineno)
ThismarkerindicatesaPythonlineisabouttobeexecuted. Itistheequivalentofline-by-linetracingwitha
Pythonprofiler. ItisnottriggeredwithinCfunctions.
Theargumentsarethesameasforfunction__entry().
gc__start(int generation)
FireswhenthePythoninterpreterstartsagarbagecollectioncycle. arg0isthegenerationtoscan,likegc.
collect().
gc__done(long collected)
FireswhenthePythoninterpreterfinishesagarbagecollectioncycle. arg0isthenumberofcollectedobjects.
import__find__load__start(str modulename)
Firesbeforeimportlibattemptstofindandloadthemodule. arg0isthemodulename.
Addedinversion3.7.
import__find__load__done(str modulename, int found)
Firesafterimportlib’sfind_and_loadfunctioniscalled. arg0isthemodulename,arg1indicatesifmodule
wassuccessfullyloaded.
Addedinversion3.7.
audit(str event, void *tuple)
Fires when sys.audit() or PySys_Audit() is called. arg0 is the event name as C string, arg1 is a
PyObjectpointertoatupleobject.
Addedinversion3.8.
5 SystemTap Tapsets
Thehigher-levelwaytousetheSystemTapintegrationistousea“tapset”: SystemTap’sequivalentofalibrary,which
hidessomeofthelower-leveldetailsofthestaticmarkers.
Hereisatapsetfile,basedonanon-sharedbuildofCPython:
/*
Provide a higher-level wrapping around the function__entry and
function__return markers:
\*/
probe python.function.entry = process("python").mark("function__entry")
{
filename = user_string($arg1);
funcname = user_string($arg2);
lineno = $arg3;
frameptr = $arg4
}
probe python.function.return = process("python").mark("function__return")
{
filename = user_string($arg1);
funcname = user_string($arg2);
lineno = $arg3;
(continuesonnextpage)
6

### 第7页

(continuedfrompreviouspage)
frameptr = $arg4
}
IfthisfileisinstalledinSystemTap’stapsetdirectory(e.g. /usr/share/systemtap/tapset),thentheseaddi-
tionalprobepointsbecomeavailable:
python.function.entry(str filename, str funcname, int lineno, frameptr)
ThisprobepointindicatesthatexecutionofaPythonfunctionhasbegun. Itisonlytriggeredforpure-Python
(bytecode)functions.
python.function.return(str filename, str funcname, int lineno, frameptr)
This probe point is the converse of python.function.return, and indicates that execution of a Python
functionhasended(eitherviareturn,orviaanexception). Itisonlytriggeredforpure-Python(bytecode)
functions.
6 Examples
ThisSystemTapscriptusesthetapsetabovetomorecleanlyimplementtheexamplegivenaboveoftracingthePython
function-callhierarchy,withoutneedingtodirectlynamethestaticmarkers:
probe python.function.entry
{
printf("%s => %s in %s:%d\n",
thread_indent(1), funcname, filename, lineno);
}
probe python.function.return
{
printf("%s <= %s in %s:%d\n",
thread_indent(-1), funcname, filename, lineno);
}
Thefollowingscriptusesthetapsetabovetoprovideatop-likeviewofallrunningCPythoncode,showingthetop
20mostfrequentlyenteredbytecodeframes,eachsecond,acrossthewholesystem:
global fn_calls;
probe python.function.entry
{
fn_calls[pid(), filename, funcname, lineno] += 1;
}
probe timer.ms(1000) {
printf("\033[2J\033[1;1H") /* clear screen \*/
printf("%6s %80s %6s %30s %6s\n",
"PID", "FILENAME", "LINE", "FUNCTION", "CALLS")
foreach ([pid, filename, funcname, lineno] in fn_calls- limit 20) {
printf("%6d %80s %6d %30s %6d\n",
pid, filename, lineno, funcname,
fn_calls[pid, filename, funcname, lineno]);
}
delete fn_calls;
}
7

