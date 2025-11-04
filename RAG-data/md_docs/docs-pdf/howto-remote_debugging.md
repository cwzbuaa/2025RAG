### 第1页

Remote debugging attachment
protocol
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Permissionrequirements 1
2 LocatingthePyRuntimestructure 3
3 Reading_Py_DebugOffsets 5
4 Locatingtheinterpreterandthreadstate 7
5 Writingcontrolinformation 8
6 Summary 9
ThisprotocolenablesexternaltoolstoattachtoarunningCPythonprocessandexecutePythoncoderemotely.
MostplatformsrequireelevatedprivilegestoattachtoanotherPythonprocess.
1 Permission requirements
Attaching to a running Python process for remote debugging requires elevated privileges on most platforms. The
specificrequirementsandtroubleshootingstepsdependonyouroperatingsystem:
Linux
ThetracerprocessmusthavetheCAP_SYS_PTRACEcapabilityorequivalentprivileges. Youcanonlytraceprocesses
youownandcansignal. Tracingmayfailiftheprocessisalreadybeingtraced,orifitisrunningwithset-user-IDor
set-group-ID.SecuritymoduleslikeYamamayfurtherrestricttracing.
Totemporarilyrelaxptracerestrictions(untilreboot),run:
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
(cid:174) Note
Disablingptrace_scopereducessystemhardeningandshouldonlybedoneintrustedenvironments.
1

### 第2页

Ifrunninginsideacontainer,use--cap-add=SYS_PTRACEor--privileged,andrunasrootifneeded.
Tryre-runningthecommandwithelevatedprivileges:
sudo -E !!
macOS
Toattachtoanotherprocess,youtypicallyneedtorunyourdebuggingtoolwithelevatedprivileges. Thiscanbedone
byusingsudoorrunningasroot.
Evenwhenattachingtoprocessesyouown,macOSmayblockdebuggingunlessthedebuggerisrunwithrootprivi-
legesduetosystemsecurityrestrictions.
Windows
Toattachtoanotherprocess, youusuallyneedtorunyourdebuggingtoolwithadministrativeprivileges. Startthe
commandpromptorterminalasAdministrator.
SomeprocessesmaystillbeinaccessibleevenwithAdministratorrights,unlessyouhavetheSeDebugPrivilege
privilegeenabled.
Toresolvefileorfolderaccessissues,adjustthesecuritypermissions:
1. Right-clickthefileorfolderandselectProperties.
2. GototheSecuritytabtoviewusersandgroupswithaccess.
3. ClickEdittomodifypermissions.
4. Selectyouruseraccount.
5. InPermissions,checkReadorFullcontrolasneeded.
6. ClickApply,thenOKtoconfirm.
(cid:174) Note
Ensureyou’vesatisfiedallPermissionrequirementsbeforeproceeding.
Thissectiondescribesthelow-levelprotocolthatenablesexternaltoolstoinjectandexecuteaPythonscriptwithin
arunningCPythonprocess.
This mechanism forms the basis of the sys.remote_exec() function, which instructs a remote Python process
to execute a .py file. However, this section does not document the usage of that function. Instead, it provides a
detailedexplanationoftheunderlyingprotocol,whichtakesasinputthepidofatargetPythonprocessandthepath
to a Python source file to be executed. This information supports independent reimplementation of the protocol,
regardlessofprogramminglanguage.
(cid:193) Warning
The execution of the injected script depends on the interpreter reaching a safe evaluation point. As a result,
executionmaybedelayeddependingontheruntimestateofthetargetprocess.
Onceinjected,thescriptisexecutedbytheinterpreterwithinthetargetprocessthenexttimeasafeevaluationpoint
isreached. Thisapproachenablesremoteexecutioncapabilitieswithoutmodifyingthebehaviororstructureofthe
runningPythonapplication.
Subsequentsectionsprovideastep-by-stepdescriptionoftheprotocol,includingtechniquesforlocatinginterpreter
structuresinmemory,safelyaccessinginternalfields,andtriggeringcodeexecution. Platform-specificvariationsare
notedwhereapplicable,andexampleimplementationsareincludedtoclarifyeachoperation.
2

| (cid:193) Warning |
| --- |
| The execution of the injected script depends on the interpreter reaching a safe evaluation point. As a result,
executionmaybedelayeddependingontheruntimestateofthetargetprocess. |

### 第3页

2 Locating the PyRuntime structure
CPython places the PyRuntime structure in a dedicated binary section to help external tools find it at runtime.
The name and format of this section vary by platform. For example, .PyRuntime is used on ELF systems, and
__DATA,__PyRuntime is used onmacOS.Toolscanfindtheoffsetofthisstructurebyexaminingthebinaryon
disk.
The PyRuntime structure contains CPython’s global interpreter state and provides access to other internal data,
includingthelistofinterpreters,threadstates,anddebuggersupportfields.
ToworkwitharemotePythonprocess,adebuggermustfirstfindthememoryaddressofthePyRuntimestructurein
thetargetprocess. Thisaddresscan’tbehardcodedorcalculatedfromasymbolname,becauseitdependsonwhere
theoperatingsystemloadedthebinary.
ThemethodforfindingPyRuntimedependsontheplatform,butthestepsarethesameingeneral:
1. FindthebaseaddresswherethePythonbinaryorsharedlibrarywasloadedinthetargetprocess.
2. Usetheon-diskbinarytolocatetheoffsetofthe.PyRuntimesection.
3. Addthesectionoffsettothebaseaddresstocomputetheaddressinmemory.
Thesectionsbelowexplainhowtodothisoneachsupportedplatformandincludeexamplecode.
Linux(ELF)
TofindthePyRuntimestructureonLinux:
1. Read the process’s memory map (for example, /proc/<pid>/maps) to find the address where the Python
executableorlibpythonwasloaded.
2. ParsetheELFsectionheadersinthebinarytogettheoffsetofthe.PyRuntimesection.
3. Addthatoffsettothebaseaddressfromstep1togetthememoryaddressofPyRuntime.
Thefollowingisanexampleimplementation:
def find_py_runtime_linux(pid: int) -> int:
# Step 1: Try to find the Python executable in memory
binary_path, base_address = find_mapped_binary(
pid, name_contains="python"
)
# Step 2: Fallback to shared library if executable is not found
if binary_path is None:
binary_path, base_address = find_mapped_binary(
pid, name_contains="libpython"
)
# Step 3: Parse ELF headers to get .PyRuntime section offset
section_offset = parse_elf_section_offset(
binary_path, ".PyRuntime"
)
# Step 4: Compute PyRuntime address in memory
return base_address + section_offset
On Linux systems, there are two main approaches to read memory from another process. The first is through the
/proc filesystem, specifically by reading from /proc/[pid]/mem which provides direct access to the process’s
memory. This requires appropriate permissions - either being the same user as the target process or having root
access. Thesecondapproachisusingtheprocess_vm_readv()systemcallwhichprovidesamoreefficientway
tocopymemorybetweenprocesses. Whileptrace’sPTRACE_PEEKTEXToperationcanalsobeusedtoreadmemory,
itissignificantlyslowerasitonlyreadsonewordatatimeandrequiresmultiplecontextswitchesbetweenthetracer
andtraceeprocesses.
3

### 第4页

ForparsingELFsections,theprocessinvolvesreadingandinterpretingtheELFfileformatstructuresfromthebinary
fileondisk. TheELFheadercontainsapointertothesectionheadertable. Eachsectionheadercontainsmetadata
aboutasectionincludingitsname(storedinaseparatestringtable),offset,andsize. Tofindaspecificsectionlike
.PyRuntime,youneedtowalkthroughtheseheadersandmatchthesectionname. Thesectionheaderthenprovides
theoffsetwherethatsectionexistsinthefile,whichcanbeusedtocalculateitsruntimeaddresswhenthebinaryis
loadedintomemory.
YoucanreadmoreabouttheELFfileformatintheELFspecification.
macOS(Mach-O)
TofindthePyRuntimestructureonmacOS:
1. Call task_for_pid() to get the mach_port_t task port for the target process. This handle is needed to
readmemoryusingAPIslikemach_vm_read_overwriteandmach_vm_region.
2. ScanthememoryregionstofindtheonecontainingthePythonexecutableorlibpython.
3. Load the binary file from disk and parse the Mach-O headers to find the section named PyRuntime in the
__DATAsegment. OnmacOS,symbolnamesareautomaticallyprefixedwithanunderscore,sothePyRuntime
symbolappearsas_PyRuntimeinthesymboltable,butthesectionnameisnotaffected.
Thefollowingisanexampleimplementation:
def find_py_runtime_macos(pid: int) -> int:
# Step 1: Get access to the process's memory
handle = get_memory_access_handle(pid)
# Step 2: Try to find the Python executable in memory
binary_path, base_address = find_mapped_binary(
handle, name_contains="python"
)
# Step 3: Fallback to libpython if the executable is not found
if binary_path is None:
binary_path, base_address = find_mapped_binary(
handle, name_contains="libpython"
)
# Step 4: Parse Mach-O headers to get __DATA,__PyRuntime section offset
section_offset = parse_macho_section_offset(
binary_path, "__DATA", "__PyRuntime"
)
# Step 5: Compute the PyRuntime address in memory
return base_address + section_offset
On macOS, accessing another process’s memory requires using Mach-O specific APIs and file formats. The first
stepisobtainingatask_porthandleviatask_for_pid(),whichprovidesaccesstothetargetprocess’smemory
space. ThishandleenablesmemoryoperationsthroughAPIslikemach_vm_read_overwrite().
Theprocessmemorycanbeexaminedusingmach_vm_region()toscanthroughthevirtualmemoryspace,while
proc_regionfilename()helpsidentifywhichbinaryfilesareloadedateachmemoryregion. WhenthePython
binaryorlibraryisfound,itsMach-OheadersneedtobeparsedtolocatethePyRuntimestructure.
TheMach-Oformatorganizescodeanddataintosegmentsandsections. ThePyRuntimestructurelivesinasection
named __PyRuntime within the __DATA segment. The actual runtime address calculation involves finding the
__TEXTsegmentwhichservesasthebinary’sbaseaddress,thenlocatingthe__DATAsegmentcontainingourtarget
section. Thefinaladdressiscomputedbycombiningthebaseaddresswiththeappropriatesectionoffsetsfromthe
Mach-Oheaders.
Notethataccessinganotherprocess’smemoryonmacOStypicallyrequireselevatedprivileges-eitherrootaccessor
specialsecurityentitlementsgrantedtothedebuggingprocess.
4

### 第5页

Windows(PE)
TofindthePyRuntimestructureonWindows:
1. UsetheToolHelpAPItoenumerateallmodulesloadedinthetargetprocess. Thisisdoneusingfunctionssuch
asCreateToolhelp32Snapshot,Module32First,andModule32Next.
2. Identify the module corresponding to python.exe or pythonXY.dll, where X and Y are the major and
minorversionnumbersofthePythonversion,andrecorditsbaseaddress.
3. Locate the PyRuntim section. Due to the PE format’s 8-character limit on section names (defined as
IMAGE_SIZEOF_SHORT_NAME), the original name PyRuntime is truncated. This section contains the
PyRuntimestructure.
4. Retrievethesection’srelativevirtualaddress(RVA)andaddittothebaseaddressofthemodule.
Thefollowingisanexampleimplementation:
def find_py_runtime_windows(pid: int) -> int:
# Step 1: Try to find the Python executable in memory
binary_path, base_address = find_loaded_module(
pid, name_contains="python"
)
# Step 2: Fallback to shared pythonXY.dll if the executable is not
# found
if binary_path is None:
binary_path, base_address = find_loaded_module(
pid, name_contains="python3"
)
# Step 3: Parse PE section headers to get the RVA of the PyRuntime
# section. The section name appears as "PyRuntim" due to the
# 8-character limit defined by the PE format (IMAGE_SIZEOF_SHORT_NAME).
section_rva = parse_pe_section_offset(binary_path, "PyRuntim")
# Step 4: Compute PyRuntime address in memory
return base_address + section_rva
On Windows, accessing another process’s memory requires using the Windows API functions like
CreateToolhelp32Snapshot() and Module32First()/Module32Next() to enumerate loaded mod-
ules. The OpenProcess() function provides a handle to access the target process’s memory space, enabling
memoryoperationsthroughReadProcessMemory().
The process memory can be examined by enumerating loaded modules to find the Python binary or DLL. When
found,itsPEheadersneedtobeparsedtolocatethePyRuntimestructure.
ThePEformatorganizescodeanddataintosections. ThePyRuntimestructurelivesinasectionnamed“PyRuntim”
(truncatedfrom“PyRuntime”duetoPE’s8-characternamelimit). Theactualruntimeaddresscalculationinvolves
findingthemodule’sbaseaddressfromthemoduleentry,thenlocatingourtargetsectioninthePEheaders. Thefinal
addressiscomputedbycombiningthebaseaddresswiththesection’svirtualaddressfromthePEsectionheaders.
Notethataccessinganotherprocess’smemoryonWindowstypicallyrequiresappropriateprivileges-eitheradmin-
istrativeaccessortheSeDebugPrivilegeprivilegegrantedtothedebuggingprocess.
3 Reading _Py_DebugOffsets
OncetheaddressofthePyRuntimestructurehasbeendetermined,thenextstepistoreadthe_Py_DebugOffsets
structurelocatedatthebeginningofthePyRuntimeblock.
Thisstructureprovidesversion-specificfieldoffsetsthatareneededtosafelyreadinterpreterandthreadstatememory.
TheseoffsetsvarybetweenCPythonversionsandmustbecheckedbeforeusetoensuretheyarecompatible.
5

### 第6页

Toreadandcheckthedebugoffsets,followthesesteps:
1. ReadmemoryfromthetargetprocessstartingatthePyRuntimeaddress,coveringthesamenumberofbytes
asthe_Py_DebugOffsetsstructure. ThisstructureislocatedattheverystartofthePyRuntimememory
block. ItslayoutisdefinedinCPython’sinternalheadersandstaysthesamewithinagivenminorversion,but
maychangeinmajorversions.
2. Checkthatthestructurecontainsvaliddata:
• Thecookiefieldmustmatchtheexpecteddebugmarker.
• TheversionfieldmustmatchtheversionofthePythoninterpreterusedbythedebugger.
• Ifeitherthedebuggerorthetargetprocessisusingapre-releaseversion(forexample,analpha,beta,or
releasecandidate),theversionsmustmatchexactly.
• Thefree_threadedfieldmusthavethesamevalueinboththedebuggerandthetargetprocess.
3. Ifthestructureisvalid,theoffsetsitcontainscanbeusedtolocatefieldsinmemory. Ifanycheckfails,the
debuggershouldstoptheoperationtoavoidreadingmemoryinthewrongformat.
Thefollowingisanexampleimplementationthatreadsandchecks_Py_DebugOffsets:
def read_debug_offsets(pid: int, py_runtime_addr: int) -> DebugOffsets:
# Step 1: Read memory from the target process at the PyRuntime address
data = read_process_memory(
pid, address=py_runtime_addr, size=DEBUG_OFFSETS_SIZE
)
# Step 2: Deserialize the raw bytes into a _Py_DebugOffsets structure
debug_offsets = parse_debug_offsets(data)
# Step 3: Validate the contents of the structure
if debug_offsets.cookie != EXPECTED_COOKIE:
raise RuntimeError("Invalid or missing debug cookie")
if debug_offsets.version != LOCAL_PYTHON_VERSION:
raise RuntimeError(
"Mismatch between caller and target Python versions"
)
if debug_offsets.free_threaded != LOCAL_FREE_THREADED:
raise RuntimeError("Mismatch in free-threaded configuration")
return debug_offsets
(cid:193) Warning
Processsuspensionrecommended
Toavoidraceconditionsandensurememoryconsistency,itisstronglyrecommendedthatthetargetprocessbe
suspended before performing any operations that read or write internal interpreter state. The Python runtime
mayconcurrentlymutateinterpreterdatastructures—suchascreatingordestroyingthreads—duringnormalex-
ecution. Thiscanresultininvalidmemoryreadsorwrites.
AdebuggermaysuspendexecutionbyattachingtotheprocesswithptraceorbysendingaSIGSTOPsignal.
Executionshouldonlyberesumedafterdebugger-sidememoryoperationsarecomplete.
(cid:174) Note
Sometools, suchasprofilersorsampling-baseddebuggers, mayoperateonarunningprocesswithoutsus-
pension. Insuchcases,toolsmustbeexplicitlydesignedtohandlepartiallyupdatedorinconsistentmemory.
Formostdebuggerimplementations,suspendingtheprocessremainsthesafestandmostrobustapproach.
6

| (cid:193) Warning |
| --- |
| Processsuspensionrecommended
Toavoidraceconditionsandensurememoryconsistency,itisstronglyrecommendedthatthetargetprocessbe
suspended before performing any operations that read or write internal interpreter state. The Python runtime
mayconcurrentlymutateinterpreterdatastructures—suchascreatingordestroyingthreads—duringnormalex-
ecution. Thiscanresultininvalidmemoryreadsorwrites.
AdebuggermaysuspendexecutionbyattachingtotheprocesswithptraceorbysendingaSIGSTOPsignal.
Executionshouldonlyberesumedafterdebugger-sidememoryoperationsarecomplete.
(cid:174) Note
Sometools, suchasprofilersorsampling-baseddebuggers, mayoperateonarunningprocesswithoutsus-
pension. Insuchcases,toolsmustbeexplicitlydesignedtohandlepartiallyupdatedorinconsistentmemory.
Formostdebuggerimplementations,suspendingtheprocessremainsthesafestandmostrobustapproach. |

### 第7页

4 Locating the interpreter and thread state
BeforecodecanbeinjectedandexecutedinaremotePythonprocess,thedebuggermustchooseathreadinwhich
toscheduleexecution. Thisisnecessarybecausethecontrolfieldsusedtoperformremotecodeinjectionarelocated
inthe_PyRemoteDebuggerSupportstructure,whichisembeddedinaPyThreadStateobject. Thesefieldsare
modifiedbythedebuggertorequestexecutionofinjectedscripts.
The PyThreadState structure represents a thread running inside a Python interpreter. It maintains the thread’s
evaluationcontextandcontainsthefieldsrequiredfordebuggercoordination. LocatingavalidPyThreadStateis
thereforeakeyprerequisitefortriggeringexecutionremotely.
A thread is typically selected based on its role or ID. In most cases, the main thread is used, but some tools may
targetaspecificthreadbyitsnativethreadID.Oncethetargetthreadischosen,thedebuggermustlocateboththe
interpreterandtheassociatedthreadstatestructuresinmemory.
Therelevantinternalstructuresaredefinedasfollows:
• PyInterpreterStaterepresentsanisolatedPythoninterpreterinstance. Eachinterpretermaintainsitsown
setofimportedmodules,built-instate,andthreadstatelist. AlthoughmostPythonapplicationsuseasingle
interpreter,CPythonsupportsmultipleinterpretersinthesameprocess.
• PyThreadStaterepresentsathreadrunningwithinaninterpreter. Itcontainsexecutionstateandthecontrol
fieldsusedbythedebugger.
Tolocateathread:
1. Use the offset runtime_state.interpreters_head to obtain the address of the first interpreter in the
PyRuntimestructure. Thisistheentrypointtothelinkedlistofactiveinterpreters.
2. Use the offset interpreter_state.threads_main to access the main thread state associated with the
selectedinterpreter. Thisistypicallythemostreliablethreadtotarget.
3. Optionally, use the offset interpreter_state.threads_head to iterate through the linked list of all
thread states. Each PyThreadState structure contains a native_thread_id field, which may be com-
paredtoatargetthreadIDtofindaspecificthread.
4. OnceavalidPyThreadStatehasbeenfound,itsaddresscanbeusedinlaterstepsoftheprotocol,suchas
writingdebuggercontrolfieldsandschedulingexecution.
Thefollowingisanexampleimplementationthatlocatesthemainthreadstate:
def find_main_thread_state(
pid: int, py_runtime_addr: int, debug_offsets: DebugOffsets,
) -> int:
# Step 1: Read interpreters_head from PyRuntime
interp_head_ptr = (
py_runtime_addr + debug_offsets.runtime_state.interpreters_head
)
interp_addr = read_pointer(pid, interp_head_ptr)
if interp_addr == 0:
raise RuntimeError("No interpreter found in the target process")
# Step 2: Read the threads_main pointer from the interpreter
threads_main_ptr = (
interp_addr + debug_offsets.interpreter_state.threads_main
)
thread_state_addr = read_pointer(pid, threads_main_ptr)
if thread_state_addr == 0:
raise RuntimeError("Main thread state is not available")
return thread_state_addr
ThefollowingexampledemonstrateshowtolocateathreadbyitsnativethreadID:
7

### 第8页

def find_thread_by_id(
pid: int,
interp_addr: int,
debug_offsets: DebugOffsets,
target_tid: int,
) -> int:
# Start at threads_head and walk the linked list
thread_ptr = read_pointer(
pid,
interp_addr + debug_offsets.interpreter_state.threads_head
)
while thread_ptr:
native_tid_ptr = (
thread_ptr + debug_offsets.thread_state.native_thread_id
)
native_tid = read_int(pid, native_tid_ptr)
if native_tid == target_tid:
return thread_ptr
thread_ptr = read_pointer(
pid,
thread_ptr + debug_offsets.thread_state.next
)
raise RuntimeError("Thread with the given ID was not found")
Onceavalidthreadstatehasbeenlocated,thedebuggercanproceedwithmodifyingitscontrolfieldsandscheduling
execution,asdescribedinthenextsection.
5 Writing control information
Once a valid PyThreadState structure has been identified, the debugger may modify control fields within it to
scheduletheexecutionofaspecifiedPythonscript. Thesecontrolfieldsarecheckedperiodicallybytheinterpreter,
andwhensetcorrectly,theytriggertheexecutionofremotecodeatasafepointintheevaluationloop.
EachPyThreadStatecontainsa_PyRemoteDebuggerSupportstructureusedforcommunicationbetweenthe
debuggerandtheinterpreter. Thelocationsofitsfieldsaredefinedbythe_Py_DebugOffsetsstructureandinclude
thefollowing:
• debugger_script_path: Afixed-sizebufferthatholdsthefullpathtoaPythonsourcefile(.py). Thisfile
mustbeaccessibleandreadablebythetargetprocesswhenexecutionistriggered.
• debugger_pending_call: Anintegerflag. Settingthisto1tellstheinterpreterthatascriptisreadytobe
executed.
• eval_breaker: A field checked by the interpreter during execution. Setting bit 5
(_PY_EVAL_PLEASE_STOP_BIT, value 1U << 5) in this field causes the interpreter to pause and
checkfordebuggeractivity.
Tocompletetheinjection,thedebuggermustperformthefollowingsteps:
1. Writethefullscriptpathintothedebugger_script_pathbuffer.
2. Setdebugger_pending_callto1.
3. Readthecurrentvalueofeval_breaker,setbit5(_PY_EVAL_PLEASE_STOP_BIT),andwritetheupdated
valueback. Thissignalstheinterpretertocheckfordebuggeractivity.
Thefollowingisanexampleimplementation:
8

### 第9页

def inject_script(
pid: int,
thread_state_addr: int,
debug_offsets: DebugOffsets,
script_path: str
) -> None:
# Compute the base offset of _PyRemoteDebuggerSupport
support_base = (
thread_state_addr +
debug_offsets.debugger_support.remote_debugger_support
)
# Step 1: Write the script path into debugger_script_path
script_path_ptr = (
support_base +
debug_offsets.debugger_support.debugger_script_path
)
write_string(pid, script_path_ptr, script_path)
# Step 2: Set debugger_pending_call to 1
pending_ptr = (
support_base +
debug_offsets.debugger_support.debugger_pending_call
)
write_int(pid, pending_ptr, 1)
# Step 3: Set _PY_EVAL_PLEASE_STOP_BIT (bit 5, value 1 << 5) in
# eval_breaker
eval_breaker_ptr = (
thread_state_addr +
debug_offsets.debugger_support.eval_breaker
)
breaker = read_int(pid, eval_breaker_ptr)
breaker |= (1 << 5)
write_int(pid, eval_breaker_ptr, breaker)
Oncethesefieldsareset, thedebuggermayresumetheprocess(ifitwassuspended). Theinterpreterwillprocess
therequestatthenextsafeevaluationpoint,loadthescriptfromdisk,andexecuteit.
Itistheresponsibilityofthedebuggertoensurethatthescriptfileremainspresentandaccessibletothetargetprocess
duringexecution.
(cid:174) Note
Script execution is asynchronous. The script file cannot be deleted immediately after injection. The debugger
shouldwaituntiltheinjectedscripthasproducedanobservableeffectbeforeremovingthefile. Thiseffectdepends
onwhatthescriptisdesignedtodo. Forexample,adebuggermightwaituntiltheremoteprocessconnectsback
toasocketbeforeremovingthescript. Oncesuchaneffectisobserved,itissafetoassumethefileisnolonger
needed.
6 Summary
ToinjectandexecuteaPythonscriptinaremoteprocess:
1. LocatethePyRuntimestructureinthetargetprocess’smemory.
2. Readandvalidatethe_Py_DebugOffsetsstructureatthebeginningofPyRuntime.
9

### 第10页

3. UsetheoffsetstolocateavalidPyThreadState.
4. WritethepathtoaPythonscriptintodebugger_script_path.
5. Setthedebugger_pending_callflagto1.
6. Set_PY_EVAL_PLEASE_STOP_BITintheeval_breakerfield.
7. Resumetheprocess(ifsuspended). Thescriptwillexecuteatthenextsafeevaluationpoint.
10

