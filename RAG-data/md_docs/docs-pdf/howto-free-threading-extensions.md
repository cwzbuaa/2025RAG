### 第1页

C API Extension Support for Free
Threading
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 IdentifyingtheFree-ThreadedBuildinC 2
2 ModuleInitialization 2
2.1 Multi-PhaseInitialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Single-PhaseInitialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
3 GeneralAPIGuidelines 3
3.1 ContainerThreadSafety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
4 BorrowedReferences 3
5 MemoryAllocationAPIs 4
6 ThreadStateandGILAPIs 4
7 ProtectingInternalExtensionState 4
8 CriticalSections 5
8.1 WhatAreCriticalSections? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
8.2 UsingCriticalSections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
8.3 HowCriticalSectionsWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
8.4 DeadlockAvoidance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
8.5 ImportantConsiderations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
9 BuildingExtensionsfortheFree-ThreadedBuild 6
9.1 LimitedCAPIandStableABI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
9.2 Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Startingwiththe3.13release,CPythonhassupportforrunningwiththeglobalinterpreterlock(GIL)disabledina
configurationcalledfreethreading. ThisdocumentdescribeshowtoadaptCAPIextensionstosupportfreethreading.
1

### 第2页

1 Identifying the Free-Threaded Build in C
TheCPythonCAPIexposesthePy_GIL_DISABLEDmacro: inthefree-threadedbuildit’sdefinedto1,andinthe
regularbuildit’snotdefined. Youcanuseittoenablecodethatonlyrunsunderthefree-threadedbuild:
#ifdef Py_GIL_DISABLED
/* code that only runs in the free-threaded build */
#endif
(cid:174) Note
OnWindows,thismacroisnotdefinedautomatically,butmustbespecifiedtothecompilerwhenbuilding. The
sysconfig.get_config_var() functioncanbe usedto determinewhetherthecurrentrunninginterpreter
hadthemacrodefined.
2 Module Initialization
ExtensionmodulesneedtoexplicitlyindicatethattheysupportrunningwiththeGILdisabled;otherwiseimporting
theextensionwillraiseawarningandenabletheGILatruntime.
TherearetwowaystoindicatethatanextensionmodulesupportsrunningwiththeGILdisableddependingonwhether
theextensionusesmulti-phaseorsingle-phaseinitialization.
2.1 Multi-Phase Initialization
Extensions that use multi-phase initialization (i.e., PyModuleDef_Init()) should add a Py_mod_gil slot in
the module definition. If your extension supports older versions of CPython, you should guard the slot with a
PY_VERSION_HEXcheck.
static struct PyModuleDef_Slot module_slots[] = {
...
#if PY_VERSION_HEX >= 0x030D0000
{Py_mod_gil, Py_MOD_GIL_NOT_USED},
#endif
{0, NULL}
};
static struct PyModuleDef moduledef = {
PyModuleDef_HEAD_INIT,
.m_slots = module_slots,
...
};
2.2 Single-Phase Initialization
Extensions that use single-phase initialization (i.e., PyModule_Create()) should call
PyUnstable_Module_SetGIL() to indicate that they support running with the GIL disabled. The func-
tion is only defined in the free-threaded build, so you should guard the call with #ifdef Py_GIL_DISABLED to
avoidcompilationerrorsintheregularbuild.
static struct PyModuleDef moduledef = {
PyModuleDef_HEAD_INIT,
...
};
PyMODINIT_FUNC
(continuesonnextpage)
2

### 第3页

(continuedfrompreviouspage)
PyInit_mymodule(void)
{
PyObject *m = PyModule_Create(&moduledef);
if (m == NULL) {
return NULL;
}
#ifdef Py_GIL_DISABLED
PyUnstable_Module_SetGIL(m, Py_MOD_GIL_NOT_USED);
#endif
return m;
}
3 General API Guidelines
MostoftheCAPIisthread-safe,buttherearesomeexceptions.
• StructFields: AccessingfieldsinPythonCAPIobjectsorstructsdirectlyisnotthread-safeifthefieldmay
beconcurrentlymodified.
• Macros: Accessor macros like PyList_GET_ITEM, PyList_SET_ITEM, and macros like
PySequence_Fast_GET_SIZE that use the object returned by PySequence_Fast() do not per-
formanyerrorcheckingorlocking. Thesemacrosarenotthread-safeifthecontainerobjectmaybemodified
concurrently.
• BorrowedReferences: CAPIfunctionsthatreturnborrowedreferencesmaynotbethread-safeifthecon-
tainingobjectismodifiedconcurrently. Seethesectiononborrowedreferencesformoreinformation.
3.1 Container Thread Safety
ContainerslikePyListObject,PyDictObject,andPySetObjectperforminternallockinginthefree-threaded
build. Forexample,thePyList_Append()willlockthelistbeforeappendinganitem.
PyDict_Next
A notable exception is PyDict_Next(), which does not lock the dictionary. You should use
Py_BEGIN_CRITICAL_SECTION to protect the dictionary while iterating over it if the dictionary may be
concurrentlymodified:
Py_BEGIN_CRITICAL_SECTION(dict);
PyObject *key, *value;
Py_ssize_t pos = 0;
while (PyDict_Next(dict, &pos, &key, &value)) {
...
}
Py_END_CRITICAL_SECTION();
4 Borrowed References
SomeCAPIfunctionsreturnborrowedreferences. TheseAPIsarenotthread-safeifthecontainingobjectismodified
concurrently. Forexample,it’snotsafetousePyList_GetItem()ifthelistmaybemodifiedconcurrently.
ThefollowingtablelistssomeborrowedreferenceAPIsandtheirreplacementsthatreturnstrongreferences.
3

### 第4页

BorrowedreferenceAPI StrongreferenceAPI
PyList_GetItem() PyList_GetItemRef()
PyList_GET_ITEM() PyList_GetItemRef()
PyDict_GetItem() PyDict_GetItemRef()
PyDict_GetItemWithError() PyDict_GetItemRef()
PyDict_GetItemString() PyDict_GetItemStringRef()
PyDict_SetDefault() PyDict_SetDefaultRef()
PyDict_Next() none(seePyDict_Next)
PyWeakref_GetObject() PyWeakref_GetRef()
PyWeakref_GET_OBJECT() PyWeakref_GetRef()
PyImport_AddModule() PyImport_AddModuleRef()
PyCell_GET() PyCell_Get()
NotallAPIsthatreturnborrowedreferencesareproblematic. Forexample,PyTuple_GetItem()issafebecause
tuplesareimmutable. Similarly,notallusesoftheaboveAPIsareproblematic. Forexample,PyDict_GetItem()
isoftenusedforparsingkeywordargumentdictionariesinfunctioncalls; thosekeywordargumentdictionariesare
effectivelyprivate(notaccessiblebyotherthreads),sousingborrowedreferencesinthatcontextissafe.
SomeofthesefunctionswereaddedinPython3.13. Youcanusethepythoncapi-compatpackagetoprovideimple-
mentationsofthesefunctionsforolderPythonversions.
5 Memory Allocation APIs
Python’smemorymanagementCAPIprovidesfunctionsinthreedifferentallocationdomains: “raw”,“mem”,and
“object”. Forthread-safety,thefree-threadedbuildrequiresthatonlyPythonobjectsareallocatedusingtheobject
domain,andthatallPythonobjectareallocatedusingthatdomain. ThisdiffersfromthepriorPythonversions,where
thiswasonlyabestpracticeandnotahardrequirement.
(cid:174) Note
Search for uses of PyObject_Malloc() in your extension and check that the allocated memory is used for
Pythonobjects. UsePyMem_Malloc()toallocatebuffersinsteadofPyObject_Malloc().
6 Thread State and GIL APIs
PythonprovidesasetoffunctionsandmacrostomanagethreadstateandtheGIL,suchas:
• PyGILState_Ensure()andPyGILState_Release()
• PyEval_SaveThread()andPyEval_RestoreThread()
• Py_BEGIN_ALLOW_THREADSandPy_END_ALLOW_THREADS
Thesefunctionsshouldstillbeusedinthefree-threadedbuildtomanagethreadstateevenwhentheGILisdisabled.
Forexample, ifyoucreateathreadoutsideofPython, youmustcallPyGILState_Ensure()beforecallinginto
thePythonAPItoensurethatthethreadhasavalidPythonthreadstate.
YoushouldcontinuetocallPyEval_SaveThread()orPy_BEGIN_ALLOW_THREADSaroundblockingoperations,
suchasI/Oorlockacquisitions,toallowotherthreadstorunthecyclicgarbagecollector.
7 Protecting Internal Extension State
YourextensionmayhaveinternalstatethatwaspreviouslyprotectedbytheGIL.Youmayneedtoaddlockingto
protectthisstate. Theapproachwilldependonyourextension,butsomecommonpatternsinclude:
4

| BorrowedreferenceAPI | StrongreferenceAPI |
| --- | --- |
| PyList_GetItem() | PyList_GetItemRef() |
| PyList_GET_ITEM() | PyList_GetItemRef() |
| PyDict_GetItem() | PyDict_GetItemRef() |
| PyDict_GetItemWithError() | PyDict_GetItemRef() |
| PyDict_GetItemString() | PyDict_GetItemStringRef() |
| PyDict_SetDefault() | PyDict_SetDefaultRef() |
| PyDict_Next() | none(seePyDict_Next) |
| PyWeakref_GetObject() | PyWeakref_GetRef() |
| PyWeakref_GET_OBJECT() | PyWeakref_GetRef() |
| PyImport_AddModule() | PyImport_AddModuleRef() |
| PyCell_GET() | PyCell_Get() |

### 第5页

• Caches: global caches are a common source of shared state. Consider using a lock to protect the cache or
disablingitinthefree-threadedbuildifthecacheisnotcriticalforperformance.
• Global State: global state may need to be protected by a lock or moved to thread local storage. C11 and
C++11providethethread_localor_Thread_localforthread-localstorage.
8 Critical Sections
Inthefree-threadedbuild,CPythonprovidesamechanismcalled“criticalsections”toprotectdatathatwouldother-
wisebeprotectedbytheGIL.Whileextensionauthorsmaynotinteractwiththeinternalcriticalsectionimplemen-
tationdirectly,understandingtheirbehavioriscrucialwhenusingcertainCAPIfunctionsormanagingsharedstate
inthefree-threadedbuild.
8.1 What Are Critical Sections?
Conceptually,criticalsectionsactasadeadlockavoidancelayerbuiltontopofsimplemutexes. Eachthreadmain-
tains a stack of active critical sections. When a thread needs to acquire a lock associated with a critical section
(e.g.,implicitlywhencallingathread-safeCAPIfunctionlikePyDict_SetItem(),orexplicitlyusingmacros),it
attemptstoacquiretheunderlyingmutex.
8.2 Using Critical Sections
TheprimaryAPIsforusingcriticalsectionsare:
• Py_BEGIN_CRITICAL_SECTIONandPy_END_CRITICAL_SECTION-Forlockingasingleobject
• Py_BEGIN_CRITICAL_SECTION2andPy_END_CRITICAL_SECTION2-Forlockingtwoobjectssimulta-
neously
ThesemacrosmustbeusedinmatchingpairsandmustappearinthesameCscope,sincetheyestablishanewlocal
scope. Thesemacrosareno-opsinnon-free-threadedbuilds,sotheycanbesafelyaddedtocodethatneedstosupport
bothbuildtypes.
Acommonuseofacriticalsectionwouldbetolockanobjectwhileaccessinganinternalattributeofit. Forexample,
ifanextensiontypehasaninternalcountfield,youcoulduseacriticalsectionwhilereadingorwritingthatfield:
// read the count, returns new reference to internal count value
PyObject *result;
Py_BEGIN_CRITICAL_SECTION(obj);
result = Py_NewRef(obj->count);
Py_END_CRITICAL_SECTION();
return result;
// write the count, consumes reference from new_count
Py_BEGIN_CRITICAL_SECTION(obj);
obj->count = new_count;
Py_END_CRITICAL_SECTION();
8.3 How Critical Sections Work
Unlike traditional locks, critical sections do not guarantee exclusive access throughout their entire duration. If a
threadwouldblockwhileholdingacriticalsection(e.g.,byacquiringanotherlockorperformingI/O),thecritical
sectionistemporarilysuspended—alllocksarereleased—andthenresumedwhentheblockingoperationcompletes.
ThisbehaviorissimilartowhathappenswiththeGILwhenathreadmakesablockingcall. Thekeydifferencesare:
• Criticalsectionsoperateonaper-objectbasisratherthanglobally
• Criticalsectionsfollowastackdisciplinewithineachthread(the“begin”and“end”macrosenforcethissince
theymustbepairedandwithinthesamescope)
• Criticalsectionsautomaticallyreleaseandreacquirelocksaroundpotentialblockingoperations
5

### 第6页

8.4 Deadlock Avoidance
Criticalsectionshelpavoiddeadlocksintwoways:
1. Ifathreadtriestoacquirealockthat’salreadyheldbyanotherthread,itfirstsuspendsallofitsactivecritical
sections,temporarilyreleasingtheirlocks
2. Whentheblockingoperationcompletes,onlythetop-mostcriticalsectionisreacquiredfirst
Thismeansyoucannotrelyonnestedcriticalsectionstolockmultipleobjectsatonce,astheinnercriticalsection
maysuspendtheouterones. Instead,usePy_BEGIN_CRITICAL_SECTION2tolocktwoobjectssimultaneously.
Note that the locks described above are only PyMutex based locks. The critical section implementation does not
know about or affect other locking mechanisms that might be in use, like POSIX mutexes. Also note that while
blockingonanyPyMutexcausesthecriticalsectionstobesuspended,onlythemutexesthatarepartofthecritical
sectionsarereleased. IfPyMutexisusedwithoutacriticalsection,itwillnotbereleasedandthereforedoesnotget
thesamedeadlockavoidance.
8.5 Important Considerations
• Criticalsectionsmaytemporarilyreleasetheirlocks,allowingotherthreadstomodifytheprotecteddata. Be
carefulaboutmakingassumptionsaboutthestateofthedataafteroperationsthatmightblock.
• Becauselockscanbetemporarilyreleased(suspended),enteringacriticalsectiondoesnotguaranteeexclusive
accesstotheprotectedresourcethroughoutthesection’sduration. Ifcodewithinacriticalsectioncallsanother
functionthatblocks(e.g.,acquiresanotherlock,performsblockingI/O),alllocksheldbythethreadviacritical
sectionswillbereleased. ThisissimilartohowtheGILcanbereleasedduringblockingcalls.
• Onlythelock(s)associatedwiththemostrecentlyentered(top-most)criticalsectionareguaranteedtobeheld
atanygiventime. Locksforouter,nestedcriticalsectionsmighthavebeensuspended.
• You can lock at most two objects simultaneously with these APIs. If you need to lock more objects, you’ll
needtorestructureyourcode.
• Whilecriticalsectionswillnotdeadlockifyouattempttolockthesameobjecttwice, theyarelessefficient
thanpurpose-builtreentrantlocksforthisusecase.
• When using Py_BEGIN_CRITICAL_SECTION2, the order of the objects doesn’t affect correctness (the im-
plementationhandlesdeadlockavoidance),butit’sgoodpracticetoalwayslockobjectsinaconsistentorder.
• Remember that the critical section macros are primarily for protecting access to Python objects that might
be involved in internal CPython operations susceptible to the deadlock scenarios described above. For pro-
tecting purely internal extension state, standard mutexes or other synchronization primitives might be more
appropriate.
9 Building Extensions for the Free-Threaded Build
CAPIextensionsneedtobebuiltspecificallyforthefree-threadedbuild. Thewheels,sharedlibraries,andbinaries
areindicatedbyatsuffix.
• pypa/manylinuxsupportsthefree-threadedbuild,withthetsuffix,suchaspython3.13t.
• pypa/cibuildwheelsupportsthefree-threadedbuildifyousetCIBW_ENABLEtocpython-freethreading.
9.1 Limited C API and Stable ABI
The free-threaded build does not currently support the Limited C API or the stable ABI. If you use setuptools to
buildyourextensionandcurrentlysetpy_limited_api=Trueyoucanusepy_limited_api=not sysconfig.
get_config_var("Py_GIL_DISABLED") to opt out of the limited API when building with the free-threaded
build.
6

### 第7页

(cid:174) Note
You will need to build separate wheels specifically for the free-threaded build. If you currently use the stable
ABI,youcancontinuetobuildasinglewheelformultiplenon-free-threadedPythonversions.
9.2 Windows
DuetoalimitationoftheofficialWindowsinstaller,youwillneedtomanuallydefinePy_GIL_DISABLED=1when
buildingextensionsfromsource.
(cid:181) Seealso
Porting Extension Modules to Support Free-Threading: A community-maintained porting guide for extension
authors.
7

| (cid:181) Seealso |
| --- |
| Porting Extension Modules to Support Free-Threading: A community-maintained porting guide for extension
authors. |

