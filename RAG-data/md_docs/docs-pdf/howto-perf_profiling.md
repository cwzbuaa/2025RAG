### 第1页

Python support for the Linux perf
profiler
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Howtoenableperfprofilingsupport 4
2 Howtoobtainthebestresults 4
3 Howtoworkwithoutframepointers 5
Index 7
author
PabloGalindo
TheLinuxperfprofilerisaverypowerfultoolthatallowsyoutoprofileandobtaininformationabouttheperformance
of your application. perf also has a very vibrant ecosystem of tools that aid with the analysis of the data that it
produces.
ThemainproblemwithusingtheperfprofilerwithPythonapplicationsisthatperfonlygetsinformationabout
nativesymbols,thatis,thenamesoffunctionsandprocedureswritteninC.Thismeansthatthenamesandfilenames
ofPythonfunctionsinyourcodewillnotappearintheoutputofperf.
SincePython3.12,theinterpretercanruninaspecialmodethatallowsPythonfunctionstoappearintheoutputof
theperfprofiler. Whenthismodeisenabled,theinterpreterwillinterposeasmallpieceofcodecompiledonthe
flybeforetheexecutionofeveryPythonfunctionanditwillteachperftherelationshipbetweenthispieceofcode
andtheassociatedPythonfunctionusingperfmapfiles.
(cid:174) Note
SupportfortheperfprofileriscurrentlyonlyavailableforLinuxonselectarchitectures. Checktheoutputofthe
configurebuildsteporchecktheoutputofpython -m sysconfig | grep HAVE_PERF_TRAMPOLINE
toseeifyoursystemissupported.
Forexample,considerthefollowingscript:
def foo(n):
result = 0
(continuesonnextpage)
1

### 第2页

(continuedfrompreviouspage)
for _ in range(n):
result += 1
return result
def bar(n):
foo(n)
def baz(n):
bar(n)
if __name__ == "__main__":
baz(1000000)
WecanrunperftosampleCPUstacktracesat9999hertz:
$ perf record -F 9999 -g -o perf.data python my_script.py
Thenwecanuseperf reporttoanalyzethedata:
$ perf report --stdio -n -g
# Children Self Samples Command Shared Object Symbol
# ........ ........ ............ .......... .................. ...............
,→...........................
#
91.08% 0.00% 0 python.exe python.exe [.] _start
|
---_start
|
--90.71%--__libc_start_main
Py_BytesMain
|
|--56.88%--pymain_run_python.constprop.0
| |
| |--56.13%--_PyRun_AnyFileObject
| | _PyRun_SimpleFileObject
| | |
| | |--55.02%--run_mod
| | | |
| | | --54.65%--PyEval_EvalCode
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
,→Vectorcall
| | | _PyEval_Vector
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
,→Vectorcall
| | | _PyEval_Vector
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
,→Vectorcall
| | | _PyEval_Vector
| | | |
| | | |--51.67%--_
(continuesonnextpage)
2

### 第3页

(continuedfrompreviouspage)
,→PyEval_EvalFrameDefault
| | | | |
| | | | |--
,→11.52%--_PyLong_Add
| | | | | ␣
,→ |
| | | | | ␣
,→ |--2.97%--_PyObject_Malloc
...
Asyoucansee,thePythonfunctionsarenotshownintheoutput,only_PyEval_EvalFrameDefault(thefunction
thatevaluatesthePythonbytecode)showsup. Unfortunatelythat’snotveryusefulbecauseallPythonfunctionsuse
thesameCfunctiontoevaluatebytecodesowecannotknowwhichPythonfunctioncorrespondstowhichbytecode-
evaluatingfunction.
Instead,ifwerunthesameexperimentwithperfsupportenabledweget:
$ perf report --stdio -n -g
# Children Self Samples Command Shared Object Symbol
# ........ ........ ............ .......... .................. ...............
,→......................................................
#
90.58% 0.36% 1 python.exe python.exe [.] _start
|
---_start
|
--89.86%--__libc_start_main
Py_BytesMain
|
|--55.43%--pymain_run_python.constprop.0
| |
| |--54.71%--_PyRun_AnyFileObject
| | _PyRun_SimpleFileObject
| | |
| | |--53.62%--run_mod
| | | |
| | | --53.26%--PyEval_EvalCode
| | | py::<module>:/
,→src/script.py
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
,→Vectorcall
| | | _PyEval_Vector
| | | py::baz:/src/
,→script.py
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
,→Vectorcall
| | | _PyEval_Vector
| | | py::bar:/src/
,→script.py
| | | _PyEval_
,→EvalFrameDefault
| | | PyObject_
(continuesonnextpage)
3

### 第4页

(continuedfrompreviouspage)
,→Vectorcall
| | | _PyEval_Vector
| | | py::foo:/src/
,→script.py
| | | |
| | | |--51.81%--_
,→PyEval_EvalFrameDefault
| | | | |
| | | | |--
,→13.77%--_PyLong_Add
| | | | | ␣
,→ |
| | | | | ␣
,→ |--3.26%--_PyObject_Malloc
1 How to enable perf profiling support
perfprofilingsupportcanbeenabledeitherfromthestartusingtheenvironmentvariablePYTHONPERFSUPPORT
or the -X perf option, or dynamically using sys.activate_stack_trampoline() and sys.
deactivate_stack_trampoline().
Thesysfunctionstakeprecedenceoverthe-Xoption,the-Xoptiontakesprecedenceovertheenvironmentvariable.
Example,usingtheenvironmentvariable:
$ PYTHONPERFSUPPORT=1 perf record -F 9999 -g -o perf.data python my_script.py
$ perf report -g -i perf.data
Example,usingthe-Xoption:
$ perf record -F 9999 -g -o perf.data python -X perf my_script.py
$ perf report -g -i perf.data
Example,usingthesysAPIsinfileexample.py:
import sys
sys.activate_stack_trampoline("perf")
do_profiled_stuff()
sys.deactivate_stack_trampoline()
non_profiled_stuff()
…then:
$ perf record -F 9999 -g -o perf.data python ./example.py
$ perf report -g -i perf.data
2 How to obtain the best results
For best results, Python should be compiled with CFLAGS="-fno-omit-frame-pointer
-mno-omit-leaf-frame-pointer" as this allows profilers to unwind using only the frame pointer and
not on DWARF debug information. This is because as the code that is interposed to allow perf support is
dynamicallygenerateditdoesn’thaveanyDWARFdebugginginformationavailable.
Youcancheckifyoursystemhasbeencompiledwiththisflagbyrunning:
4

### 第5页

$ python -m sysconfig | grep 'no-omit-frame-pointer'
Ifyoudon’tseeanyoutputitmeansthatyourinterpreterhasnotbeencompiledwithframepointersandthereforeit
maynotbeabletoshowPythonfunctionsintheoutputofperf.
3 How to work without frame pointers
If you are working with a Python interpreter that has been compiled without frame pointers, you can still use the
perf profiler, but the overhead will be a bit higher because Python needs to generate unwinding information for
everyPythonfunctioncallonthefly. Additionally,perfwilltakemoretimetoprocessthedatabecauseitwillneed
tousetheDWARFdebugginginformationtounwindthestackandthisisaslowprocess.
To enable this mode, you can use the environment variable PYTHON_PERF_JIT_SUPPORT or the -X perf_jit
option,whichwillenabletheJITmodefortheperfprofiler.
(cid:174) Note
Duetoabugintheperftool,onlyperfversionshigherthanv6.8willworkwiththeJITmode. Thefixwas
alsobackportedtothev6.7.2versionofthetool.
Notethatwhencheckingtheversionoftheperftool(whichcanbedonebyrunningperf version)youmust
takeintoaccountthatsomedistrosaddsomecustomversionnumbersincludinga-character. Thismeansthat
perf 6.7-3isnotnecessarilyperf 6.7.3.
WhenusingtheperfJITmode,youneedanextrastepbeforeyoucanrunperf report. Youneedtocalltheperf
injectcommandtoinjecttheJITinformationintotheperf.datafile.:
$ perf record -F 9999 -g -k 1 --call-graph dwarf -o perf.data python -Xperf_jit my_
,→script.py
$ perf inject -i perf.data --jit --output perf.jit.data
$ perf report -g -i perf.jit.data
orusingtheenvironmentvariable:
$ PYTHON_PERF_JIT_SUPPORT=1 perf record -F 9999 -g --call-graph dwarf -o perf.data␣
,→python my_script.py
$ perf inject -i perf.data --jit --output perf.jit.data
$ perf report -g -i perf.jit.data
perf inject --jitcommandwillreadperf.data,automaticallypickuptheperfdumpfilethatPythoncreates
(in/tmp/perf-$PID.dump),andthencreateperf.jit.datawhichmergesalltheJITinformationtogether. It
shouldalsocreatealotofjitted-XXXX-N.sofilesinthecurrentdirectorywhichareELFimagesforalltheJIT
trampolinesthatwerecreatedbyPython.
(cid:193) Warning
Whenusing--call-graph dwarf,theperftoolwilltakesnapshotsofthestackoftheprocessbeingprofiled
andsavetheinformationintheperf.datafile. Bydefault,thesizeofthestackdumpis8192bytes,butyou
canchangethesizebypassingitafteracommalike--call-graph dwarf,16384.
Thesizeofthestackdumpisimportantbecauseifthesizeistoosmallperfwillnotbeabletounwindthestack
andtheoutputwillbeincomplete. Ontheotherhand,ifthesizeistoobig,thenperfwon’tbeabletosample
theprocessasfrequentlyasitwouldlikeastheoverheadwillbehigher.
ThestacksizeisparticularlyimportantwhenprofilingPythoncodecompiledwithlowoptimizationlevels(like
-O0), as these builds tend to have larger stack frames. If you are compiling Python with -O0 and not seeing
Pythonfunctionsinyourprofilingoutput,tryincreasingthestackdumpsizeto65528bytes(themaximum):
5

| (cid:193) Warning |
| --- |
| Whenusing--call-graph dwarf,theperftoolwilltakesnapshotsofthestackoftheprocessbeingprofiled
andsavetheinformationintheperf.datafile. Bydefault,thesizeofthestackdumpis8192bytes,butyou
canchangethesizebypassingitafteracommalike--call-graph dwarf,16384.
Thesizeofthestackdumpisimportantbecauseifthesizeistoosmallperfwillnotbeabletounwindthestack
andtheoutputwillbeincomplete. Ontheotherhand,ifthesizeistoobig,thenperfwon’tbeabletosample
theprocessasfrequentlyasitwouldlikeastheoverheadwillbehigher.
ThestacksizeisparticularlyimportantwhenprofilingPythoncodecompiledwithlowoptimizationlevels(like
-O0), as these builds tend to have larger stack frames. If you are compiling Python with -O0 and not seeing
Pythonfunctionsinyourprofilingoutput,tryincreasingthestackdumpsizeto65528bytes(themaximum): |

### 第6页

$ perf record -F 9999 -g -k 1 --call-graph dwarf,65528 -o perf.data python -
,→Xperf_jit my_script.py
Differentcompilationflagscansignificantlyimpactstacksizes:
• Buildswith-O0typicallyhavemuchlargerstackframesthanthosewith-O1orhigher
• Addingoptimizations(-O1,-O2,etc.) typicallyreducesstacksize
• Framepointers(-fno-omit-frame-pointer)generallyprovidemorereliablestackunwinding
6

### 第7页

Index
E
environment variable
PYTHON_PERF_JIT_SUPPORT,5
PYTHONPERFSUPPORT,4
P
PYTHON_PERF_JIT_SUPPORT,5
PYTHONPERFSUPPORT,4
7

