### 第1页

Python support for free threading
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Installation 2
2 Identifyingfree-threadedPython 2
3 Theglobalinterpreterlockinfree-threadedPython 2
4 Threadsafety 2
5 Knownlimitations 2
5.1 Immortalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
5.2 Frameobjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
5.3 Iterators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
5.4 Single-threadedperformance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
6 Behavioralchanges 3
6.1 Contextvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
6.2 Warningfilters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Index 4
Starting with the 3.13 release, CPython has support for a build of Python called free threading where the global
interpreterlock(GIL)isdisabled. Free-threadedexecutionallowsforfullutilizationoftheavailableprocessingpower
byrunningthreadsinparallelonavailableCPUcores. Whilenotallsoftwarewillbenefitfromthisautomatically,
programsdesignedwiththreadinginmindwillrunfasteronmulti-corehardware.
Thefree-threadedmodeisworkingandcontinuestobeimproved,butthereissomeadditionaloverheadinsingle-
threaded workloads compared to the regular build. Additionally, third-party packages, in particular ones with an
extensionmodule,maynotbereadyforuseinafree-threadedbuild,andwillre-enabletheGIL.
ThisdocumentdescribestheimplicationsoffreethreadingforPythoncode. Seefreethreading-extensions-howtofor
informationonhowtowriteCextensionsthatsupportthefree-threadedbuild.
(cid:181) Seealso
PEP703–MakingtheGlobalInterpreterLockOptionalinCPythonforanoveralldescriptionoffree-threaded
Python.
1

| (cid:181) Seealso |
| --- |
| PEP703–MakingtheGlobalInterpreterLockOptionalinCPythonforanoveralldescriptionoffree-threaded
Python. |

### 第2页

1 Installation
Starting with Python 3.13, the official macOS and Windows installers optionally support installing free-threaded
Pythonbinaries. Theinstallersareavailableathttps://www.python.org/downloads/.
Forinformationonotherplatforms,seetheInstallingaFree-ThreadedPython,acommunity-maintainedinstallation
guideforinstallingfree-threadedPython.
WhenbuildingCPythonfromsource,the--disable-gilconfigureoptionshouldbeusedtobuildafree-threaded
Pythoninterpreter.
2 Identifying free-threaded Python
Tocheckifthecurrentinterpretersupportsfree-threading,python -VVandsys.versioncontain“free-threading
build”. Thenewsys._is_gil_enabled()functioncanbeusedtocheckwhethertheGILisactuallydisabledin
therunningprocess.
The sysconfig.get_config_var("Py_GIL_DISABLED") configuration variable can be used to determine
whetherthebuildsupportsfreethreading. Ifthevariableissetto1,thenthebuildsupportsfreethreading. Thisis
therecommendedmechanismfordecisionsrelatedtothebuildconfiguration.
3 The global interpreter lock in free-threaded Python
Free-threadedbuildsofCPythonsupportoptionallyrunningwiththeGILenabledatruntimeusingtheenvironment
variablePYTHON_GILorthecommand-lineoption-X gil.
TheGILmayalsoautomaticallybeenabledwhenimportingaC-APIextensionmodulethatisnotexplicitlymarked
assupportingfreethreading. Awarningwillbeprintedinthiscase.
Inadditiontoindividualpackagedocumentation,thefollowingwebsitestrackthestatusofpopularpackagessupport
forfreethreading:
• https://py-free-threading.github.io/tracking/
• https://hugovk.github.io/free-threaded-wheels/
4 Thread safety
The free-threaded build of CPython aims to provide similar thread-safety behavior at the Python level to the de-
fault GIL-enabled build. Built-in types like dict, list, and set use internal locks to protect against concurrent
modifications in ways that behave similarly to the GIL. However, Python has not historically guaranteed specific
behaviorforconcurrentmodificationstothesebuilt-intypes,sothisshouldbetreatedasadescriptionofthecurrent
implementation,notaguaranteeofcurrentorfuturebehavior.
(cid:174) Note
It’s recommended to use the threading.Lock or other synchronization primitives instead of relying on the
internallocksofbuilt-intypes,whenpossible.
5 Known limitations
Thissectiondescribesknownlimitationsofthefree-threadedCPythonbuild.
2

### 第3页

5.1 Immortalization
Thefree-threadedbuildofthe3.13releasemakessomeobjectsimmortal. Immortalobjectsarenotdeallocatedand
havereferencecountsthatarenevermodified. Thisisdonetoavoidreferencecountcontentionthatwouldprevent
efficientmulti-threadedscaling.
Anobjectwillbemadeimmortalwhenanewthreadisstartedforthefirsttimeafterthemainthreadisrunning. The
followingobjectsareimmortalized:
• functionobjectsdeclaredatthemodulelevel
• methoddescriptors
• codeobjects
• moduleobjectsandtheirdictionaries
• classes(typeobjects)
Because immortal objects are never deallocated, applications that create many objects of these types may see in-
creasedmemoryusage. Thisisexpectedtobeaddressedinthe3.14release.
Additionally,numericandstringliteralsinthecodeaswellasstringsreturnedbysys.intern()arealsoimmor-
talized. Thisbehaviorisexpectedtoremaininthe3.14free-threadedbuild.
5.2 Frame objects
Itisnotsafetoaccessframeobjectsfromotherthreadsanddoingsomaycauseyourprogramtocrash. Thismeans
that sys._current_frames() is generally not safe to use in a free-threaded build. Functions like inspect.
currentframe()andsys._getframe()aregenerallysafeaslongastheresultingframeobjectisnotpassedto
anotherthread.
5.3 Iterators
Sharing the same iterator object between multiple threads is generally not safe and threads may see duplicate or
missingelementswheniteratingorcrashtheinterpreter.
5.4 Single-threaded performance
Thefree-threadedbuildhasadditionaloverheadwhenexecutingPythoncodecomparedtothedefaultGIL-enabled
build. In3.13,thisoverheadisabout40%onthepyperformancesuite. ProgramsthatspendmostoftheirtimeinC
extensionsorI/Owillseelessofanimpact. Thelargestimpactisbecausethespecializingadaptiveinterpreter(PEP
659)isdisabledinthefree-threadedbuild. Weexpecttore-enableitinathread-safewayinthe3.14release. This
overheadisexpectedtobereducedinupcomingPythonrelease. Weareaimingforanoverheadof10%orlesson
thepyperformancesuitecomparedtothedefaultGIL-enabledbuild.
6 Behavioral changes
ThissectiondescribesCPythonbehaviouralchangeswiththefree-threadedbuild.
6.1 Context variables
Inthefree-threadedbuild,theflagthread_inherit_contextissettotruebydefaultwhichcausesthreadscreated
with threading.Thread to start with a copy of the Context() of the caller of start(). In the default GIL-
enabledbuild,theflagdefaultstofalsesothreadsstartwithanemptyContext().
6.2 Warning filters
Inthefree-threadedbuild,theflagcontext_aware_warningsissettotruebydefault. InthedefaultGIL-enabled
build, the flag defaults to false. If the flag is true then the warnings.catch_warnings context manager uses a
contextvariableforwarningfilters. Iftheflagisfalsethencatch_warningsmodifiestheglobalfilterslist,which
isnotthread-safe. Seethewarningsmoduleformoredetails.
3

### 第4页

Index
E
environment variable
PYTHON_GIL,2
P
Python Enhancement Proposals
PEP 659,3
PEP 703,1
PYTHON_GIL,2
4

