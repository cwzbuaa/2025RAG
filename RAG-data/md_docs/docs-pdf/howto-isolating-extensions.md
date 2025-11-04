### 第1页

Isolating Extension Modules
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Whoshouldreadthis 2
2 Background 2
2.1 EnterPer-ModuleState . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 IsolatedModuleObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.3 SurprisingEdgeCases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3 MakingModulesSafewithMultipleInterpreters 3
3.1 ManagingGlobalState . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3.2 ManagingPer-ModuleState . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3.3 Opt-Out: LimitingtoOneModuleObjectperProcess . . . . . . . . . . . . . . . . . . . . . . . . 4
3.4 ModuleStateAccessfromFunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
4 HeapTypes 5
4.1 ChangingStaticTypestoHeapTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4.2 DefiningHeapTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4.3 Garbage-CollectionProtocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.4 ModuleStateAccessfromClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.5 ModuleStateAccessfromRegularMethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.6 ModuleStateAccessfromSlotMethods,GettersandSetters . . . . . . . . . . . . . . . . . . . . . 9
4.7 LifetimeoftheModuleState . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5 OpenIssues 9
5.1 Per-ClassScope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
5.2 LosslessConversiontoHeapTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
Abstract
Traditionally,statebelongingtoPythonextensionmoduleswaskeptinCstaticvariables,whichhaveprocess-
wide scope. This document describes problems of such per-process state and shows a safer way: per-module
state.
Thedocumentalsodescribeshowtoswitchtoper-modulestatewherepossible. Thistransitioninvolvesallocating
space for that state, potentially switching from static types to heap types, and—perhaps most importantly—
accessingper-modulestatefromcode.
1

### 第2页

1 Who should read this
This guide is written for maintainers of C-API extensions who would like to make that extension safer to use in
applicationswherePythonitselfisusedasalibrary.
2 Background
AninterpreteristhecontextinwhichPythoncoderuns. Itcontainsconfiguration(e.g. theimportpath)andruntime
state(e.g. thesetofimportedmodules).
Python supports running multiple interpreters in one process. There are two cases to think about—users may run
interpreters:
• insequence,withseveralPy_InitializeEx()/Py_FinalizeEx()cycles,and
• inparallel,managing“sub-interpreters”usingPy_NewInterpreter()/Py_EndInterpreter().
Both cases (and combinations of them) would be most useful when embedding Python within a library. Libraries
generallyshouldn’tmakeassumptionsabouttheapplicationthatusesthem,whichincludeassumingaprocess-wide
“mainPythoninterpreter”.
Historically,Pythonextensionmodulesdon’thandlethisusecasewell. Manyextensionmodules(andevensomestdlib
modules)useper-processglobalstate,becauseCstaticvariablesareextremelyeasytouse. Thus,datathatshould
bespecifictoaninterpreterendsupbeingsharedbetweeninterpreters. Unlesstheextensiondeveloperiscareful,it
isveryeasytointroduceedgecasesthatleadtocrasheswhenamoduleisloadedinmorethanoneinterpreterinthe
sameprocess.
Unfortunately,per-interpreterstateisnoteasytoachieve. Extensionauthorstendtonotkeepmultipleinterpretersin
mindwhendeveloping,anditiscurrentlycumbersometotestthebehavior.
2.1 Enter Per-Module State
Instead of focusing on per-interpreter state, Python’s C API is evolving to better support the more granular per-
modulestate. ThismeansthatC-leveldatashouldbeattachedtoamoduleobject. Eachinterpretercreatesitsown
moduleobject,keepingthedataseparate. Fortestingtheisolation,multiplemoduleobjectscorrespondingtoasingle
extensioncanevenbeloadedinasingleinterpreter.
Per-module state provides an easy way to think about lifetime and resource ownership: the extension module will
initializewhenamoduleobjectiscreated,andcleanupwhenit’sfreed. Inthisregard,amoduleisjustlikeanyother
PyObject*;thereareno“oninterpretershutdown”hookstothink—orforget—about.
Notethatthereareusecasesfordifferentkindsof“globals”: per-process,per-interpreter,per-threadorper-taskstate.
Withper-modulestateasthedefault,thesearestillpossible,butyoushouldtreatthemasexceptionalcases: ifyou
needthem,youshouldgivethemadditionalcareandtesting. (Notethatthisguidedoesnotcoverthem.)
2.2 Isolated Module Objects
Thekeypointtokeepinmindwhendevelopinganextensionmoduleisthatseveralmoduleobjectscanbecreated
fromasinglesharedlibrary. Forexample:
>>> import sys
>>> import binascii
>>> old_binascii = binascii
>>> del sys.modules['binascii']
>>> import binascii # create a new module object
>>> old_binascii == binascii
False
Asaruleofthumb,thetwomodulesshouldbecompletelyindependent. Allobjectsandstatespecifictothemodule
should be encapsulated within the module object, not shared with other module objects, and cleaned up when the
moduleobjectisdeallocated. Sincethisjustisaruleofthumb,exceptionsarepossible(seeManagingGlobalState),
buttheywillneedmorethoughtandattentiontoedgecases.
2

### 第3页

Whilesomemodulescoulddowithlessstringentrestrictions,isolatedmodulesmakeiteasiertosetclearexpectations
andguidelinesthatworkacrossavarietyofusecases.
2.3 Surprising Edge Cases
Note that isolated modules do create some surprising edge cases. Most notably, each module object will typically
not share its classes and exceptions with other similar modules. Continuing from the example above, note that
old_binascii.Error and binascii.Error are separate objects. In the following code, the exception is not
caught:
>>> old_binascii.Error == binascii.Error
False
>>> try:
... old_binascii.unhexlify(b'qwertyuiop')
... except binascii.Error:
... print('boo')
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
binascii.Error: Non-hexadecimal digit found
Thisisexpected. Noticethatpure-Pythonmodulesbehavethesameway: itisapartofhowPythonworks.
The goal is to make extension modules safe at the C level, not to make hacks behave intuitively. Mutating sys.
modules“manually”countsasahack.
3 Making Modules Safe with Multiple Interpreters
3.1 Managing Global State
Sometimes, the state associated with a Python module is not specific to that module, but to the entire process (or
somethingelse“moreglobal”thanamodule). Forexample:
• Thereadlinemodulemanagestheterminal.
• Amodulerunningonacircuitboardwantstocontroltheon-boardLED.
Inthesecases,thePythonmoduleshouldprovideaccesstotheglobalstate,ratherthanownit. Ifpossible,writethe
modulesothatmultiplecopiesofitcanaccessthestateindependently(alongwithotherlibraries,whetherforPython
orotherlanguages). Ifthatisnotpossible,considerexplicitlocking.
Ifitisnecessarytouseprocess-globalstate,thesimplestwaytoavoidissueswithmultipleinterpretersistoexplicitly
preventamodulefrombeingloadedmorethanonceperprocess—seeOpt-Out: LimitingtoOneModuleObjectper
Process.
3.2 Managing Per-Module State
To use per-module state, use multi-phase extension module initialization. This signals that your module supports
multipleinterpreterscorrectly.
SetPyModuleDef.m_sizetoapositivenumbertorequestthatmanybytesofstoragelocaltothemodule. Usually,
this will be set to the size of some module-specific struct, which can store all of the module’s C-level state. In
particular,itiswhereyoushouldputpointerstoclasses(includingexceptions,butexcludingstatictypes)andsettings
(e.g. csv’sfield_size_limit)whichtheCcodeneedstofunction.
(cid:174) Note
Another option is to store state in the module’s __dict__, but you must avoid crashing when users modify
__dict__fromPythoncode. Thisusuallymeanserror-andtype-checkingattheClevel,whichiseasytoget
wrongandhardtotestsufficiently.
3

### 第4页

However,ifmodulestateisnotneededinCcode,storingitin__dict__onlyisagoodidea.
IfthemodulestateincludesPyObject pointers, themoduleobjectmustholdreferencesto thoseobjectsandim-
plementthemodule-levelhooksm_traverse,m_clearandm_free. Theseworkliketp_traverse,tp_clear
andtp_freeofaclass. Addingthemwillrequiresomeworkandmakethecodelonger;thisisthepriceformodules
whichcanbeunloadedcleanly.
An example of a module with per-module state is currently available as xxlimited; example module initialization
shownatthebottomofthefile.
3.3 Opt-Out: Limiting to One Module Object per Process
Anon-negativePyModuleDef.m_sizesignalsthatamodulesupportsmultipleinterpreterscorrectly. Ifthisisnot
yetthecaseforyourmodule,youcanexplicitlymakeyourmoduleloadableonlyonceperprocess. Forexample:
// A process-wide flag
static int loaded = 0;
// Mutex to provide thread safety (only needed for free-threaded Python)
static PyMutex modinit_mutex = {0};
static int
exec_module(PyObject* module)
{
PyMutex_Lock(&modinit_mutex);
if (loaded) {
PyMutex_Unlock(&modinit_mutex);
PyErr_SetString(PyExc_ImportError,
"cannot load module more than once per process");
return -1;
}
loaded = 1;
PyMutex_Unlock(&modinit_mutex);
// ... rest of initialization
}
If your module’s PyModuleDef.m_clear function is able to prepare for future re-initialization, it should clear
the loaded flag. In this case, your module won’t support multiple instances existing concurrently, but it will,
for example, support being loaded after Python runtime shutdown (Py_FinalizeEx()) and re-initialization
(Py_Initialize()).
3.4 Module State Access from Functions
Accessing the state from module-level functions is straightforward. Functions get the module object as their first
argument;forextractingthestate,youcanusePyModule_GetState:
static PyObject *
func(PyObject *module, PyObject *args)
{
my_struct *state = (my_struct*)PyModule_GetState(module);
if (state == NULL) {
return NULL;
}
// ... rest of logic
}
4

### 第5页

(cid:174) Note
PyModule_GetState may return NULL without setting an exception if there is no module state, i.e.
PyModuleDef.m_size was zero. In your own module, you’re in control of m_size, so this is easy to pre-
vent.
4 Heap Types
Traditionally,typesdefinedinCcodearestatic;thatis,static PyTypeObjectstructuresdefineddirectlyincode
andinitializedusingPyType_Ready().
Suchtypesarenecessarilysharedacrosstheprocess. Sharingthembetweenmoduleobjectsrequirespayingattention
to any state they own or access. To limit the possible issues, static types are immutable at the Python level: for
example,youcan’tsetstr.myattribute = 123.
CPythonimplementationdetail: Sharingtrulyimmutableobjectsbetweeninterpretersisfine,aslongastheydon’t
provideaccesstomutableobjects. However,inCPython,everyPythonobjecthasamutableimplementationdetail:
the reference count. Changes to the refcount are guarded by the GIL. Thus, code that shares any Python objects
acrossinterpretersimplicitlydependsonCPython’scurrent,process-wideGIL.
Becausetheyareimmutableandprocess-global, statictypescannotaccess“their” modulestate. If anymethodof
such a type requires access to module state, the type must be converted to a heap-allocated type, or heap type for
short. ThesecorrespondmorecloselytoclassescreatedbyPython’sclassstatement.
Fornewmodules,usingheaptypesbydefaultisagoodruleofthumb.
4.1 Changing Static Types to Heap Types
Statictypescanbeconvertedtoheaptypes,butnotethattheheaptypeAPIwasnotdesignedfor“lossless”conversion
from static types—that is, creating a type that works exactly like a given static type. So, when rewriting the class
definitioninanewAPI,youarelikelytounintentionallychangeafewdetails(e.g. pickleabilityorinheritedslots).
Alwaystestthedetailsthatareimportanttoyou.
Watchoutforthefollowingtwopointsinparticular(butnotethatthisisnotacomprehensivelist):
• Unlikestatictypes,heaptypeobjectsaremutablebydefault. UsethePy_TPFLAGS_IMMUTABLETYPEflagto
preventmutability.
• Heaptypesinherittp_newbydefault,soitmaybecomepossibletoinstantiatethemfromPythoncode. You
canpreventthiswiththePy_TPFLAGS_DISALLOW_INSTANTIATIONflag.
4.2 Defining Heap Types
HeaptypescanbecreatedbyfillingaPyType_Specstructure, adescriptionor“blueprint”ofaclass, andcalling
PyType_FromModuleAndSpec()toconstructanewclassobject.
(cid:174) Note
Otherfunctions,likePyType_FromSpec(),canalsocreateheaptypes,butPyType_FromModuleAndSpec()
associatesthemodulewiththeclass,allowingaccesstothemodulestatefrommethods.
Theclassshouldgenerallybestoredinboththemodulestate(forsafeaccessfromC)andthemodule’s__dict__
(foraccessfromPythoncode).
5

### 第6页

4.3 Garbage-Collection Protocol
Instancesofheaptypesholdareferencetotheirtype. Thisensuresthatthetypeisn’tdestroyedbeforeallitsinstances
are,butmayresultinreferencecyclesthatneedtobebrokenbythegarbagecollector.
Toavoidmemoryleaks,instancesofheaptypesmustimplementthegarbagecollectionprotocol. Thatis,heaptypes
should:
• HavethePy_TPFLAGS_HAVE_GCflag.
• Define a traverse function using Py_tp_traverse, which visits the type (e.g. using
Py_VISIT(Py_TYPE(self))).
PleaserefertothedocumentationofPy_TPFLAGS_HAVE_GCandtp_traverseforadditionalconsiderations.
The API for defining heap types grew organically, leaving it somewhat awkward to use in its current state. The
followingsectionswillguideyouthroughcommonissues.
tp_traverseinPython3.8andlower
Therequirementtovisitthetypefromtp_traversewasaddedinPython3.9. IfyousupportPython3.8andlower,
thetraversefunctionmustnotvisitthetype,soitmustbemorecomplicated:
static int my_traverse(PyObject *self, visitproc visit, void *arg)
{
if (Py_Version >= 0x03090000) {
Py_VISIT(Py_TYPE(self));
}
return 0;
}
Unfortunately,Py_VersionwasonlyaddedinPython3.11. Asareplacement,use:
• PY_VERSION_HEX,ifnotusingthestableABI,or
• sys.version_info(viaPySys_GetObject()andPyArg_ParseTuple()).
Delegatingtp_traverse
If your traverse function delegates to the tp_traverse of its base class (or another type), ensure that
Py_TYPE(self)isvisitedonlyonce. Notethatonlyheaptypeareexpectedtovisitthetypeintp_traverse.
Forexample,ifyourtraversefunctionincludes:
base->tp_traverse(self, visit, arg)
…andbasemaybeastatictype,thenitshouldalsoinclude:
if (base->tp_flags & Py_TPFLAGS_HEAPTYPE) {
// a heap type's tp_traverse already visited Py_TYPE(self)
} else {
if (Py_Version >= 0x03090000) {
Py_VISIT(Py_TYPE(self));
}
}
Itisnotnecessarytohandlethetype’sreferencecountintp_newandtp_clear.
Definingtp_dealloc
Ifyourtypehasacustomtp_deallocfunction,itneedsto:
• callPyObject_GC_UnTrack()beforeanyfieldsareinvalidated,and
• decrementthereferencecountofthetype.
6

### 第7页

To keep the type valid while tp_free is called, the type’s refcount needs to be decremented after the instance is
deallocated. Forexample:
static void my_dealloc(PyObject *self)
{
PyObject_GC_UnTrack(self);
...
PyTypeObject *type = Py_TYPE(self);
type->tp_free(self);
Py_DECREF(type);
}
Thedefaulttp_deallocfunctiondoesthis,soifyourtypedoesnot overridetp_deallocyoudon’tneedtoadd
it.
Notoverridingtp_free
Thetp_freeslotofaheaptypemustbesettoPyObject_GC_Del(). Thisisthedefault;donotoverrideit.
AvoidingPyObject_New
GC-trackedobjectsneedtobeallocatedusingGC-awarefunctions.
IfyouusePyObject_New()orPyObject_NewVar():
• Get and call type’s tp_alloc slot, if possible. That is, replace TYPE *o = PyObject_New(TYPE,
typeobj)with:
TYPE *o = typeobj->tp_alloc(typeobj, 0);
Replaceo = PyObject_NewVar(TYPE, typeobj, size)withthesame,butusesizeinsteadofthe0.
• If the above is not possible (e.g. inside a custom tp_alloc), call PyObject_GC_New() or
PyObject_GC_NewVar():
TYPE *o = PyObject_GC_New(TYPE, typeobj);
TYPE *o = PyObject_GC_NewVar(TYPE, typeobj, size);
4.4 Module State Access from Classes
IfyouhaveatypeobjectdefinedwithPyType_FromModuleAndSpec(),youcancallPyType_GetModule()to
gettheassociatedmodule,andthenPyModule_GetState()togetthemodule’sstate.
To save a some tedious error-handling boilerplate code, you can combine these two steps with
PyType_GetModuleState(),resultingin:
my_struct *state = (my_struct*)PyType_GetModuleState(type);
if (state == NULL) {
return NULL;
}
4.5 Module State Access from Regular Methods
Accessingthemodule-levelstatefrommethodsofaclassissomewhatmorecomplicated,butispossiblethanksto
APIintroducedinPython3.9. Togetthestate,youneedtofirstgetthedefiningclass,andthengetthemodulestate
fromit.
Thelargestroadblockisgettingtheclassamethodwasdefinedin, orthatmethod’s“definingclass”forshort. The
definingclasscanhaveareferencetothemoduleitispartof.
7

### 第8页

Do not confuse the defining class with Py_TYPE(self). If the method is called on a subclass of your type,
Py_TYPE(self)willrefertothatsubclass,whichmaybedefinedindifferentmodulethanyours.
(cid:174) Note
The following Python code can illustrate the concept. Base.get_defining_class returns Base even if
type(self) == Sub:
class Base:
def get_type_of_self(self):
return type(self)
def get_defining_class(self):
return __class__
class Sub(Base):
pass
For a method to get its “defining class”, it must use the METH_METHOD | METH_FASTCALL |
METH_KEYWORDScalling conventionandthecorrespondingPyCMethodsignature:
PyObject *PyCMethod(
PyObject *self, // object the method was called on
PyTypeObject *defining_class, // defining class
PyObject *const *args, // C array of arguments
Py_ssize_t nargs, // length of "args"
PyObject *kwnames) // NULL, or dict of keyword arguments
Onceyouhavethedefiningclass,callPyType_GetModuleState()togetthestateofitsassociatedmodule.
Forexample:
static PyObject *
example_method(PyObject *self,
PyTypeObject *defining_class,
PyObject *const *args,
Py_ssize_t nargs,
PyObject *kwnames)
{
my_struct *state = (my_struct*)PyType_GetModuleState(defining_class);
if (state == NULL) {
return NULL;
}
... // rest of logic
}
PyDoc_STRVAR(example_method_doc, "...");
static PyMethodDef my_methods[] = {
{"example_method",
(PyCFunction)(void(*)(void))example_method,
METH_METHOD|METH_FASTCALL|METH_KEYWORDS,
example_method_doc}
{NULL},
}
8

### 第9页

4.6 Module State Access from Slot Methods, Getters and Setters
(cid:174) Note
ThisisnewinPython3.11.
Slot methods—the fast C equivalents for special methods, such as nb_add for __add__ or tp_new for
initialization—have a very simple API that doesn’t allow passing in the defining class, unlike with PyCMethod.
ThesamegoesforgettersandsettersdefinedwithPyGetSetDef.
Toaccessthemodulestateinthesecases,usethePyType_GetModuleByDef()function,andpassinthemodule
definition. Onceyouhavethemodule,callPyModule_GetState()togetthestate:
PyObject *module = PyType_GetModuleByDef(Py_TYPE(self), &module_def);
my_struct *state = (my_struct*)PyModule_GetState(module);
if (state == NULL) {
return NULL;
}
PyType_GetModuleByDef() works by searching the method resolution order (i.e. all superclasses) for the first
superclassthathasacorrespondingmodule.
(cid:174) Note
In very exotic cases (inheritance chains spanning multiple modules created from the same definition),
PyType_GetModuleByDef()mightnotreturnthemoduleofthetruedefiningclass. However,itwillalways
returnamodulewiththesamedefinition,ensuringacompatibleCmemorylayout.
4.7 Lifetime of the Module State
Whenamoduleobjectisgarbage-collected,itsmodulestateisfreed. Foreachpointerto(apartof)themodulestate,
youmustholdareferencetothemoduleobject.
Usuallythisisnotanissue,becausetypescreatedwithPyType_FromModuleAndSpec(),andtheirinstances,hold
areferencetothemodule. However,youmustbecarefulinreferencecountingwhenyoureferencemodulestatefrom
otherplaces,suchascallbacksforexternallibraries.
5 Open Issues
Severalissuesaroundper-modulestateandheaptypesarestillopen.
Discussionsaboutimprovingthesituationarebestheldonthediscussforumunderc-apitag.
5.1 Per-Class Scope
It is currently (as of Python 3.11) not possible to attach state to individual types without relying on CPython im-
plementationdetails(whichmaychangeinthefuture—perhaps, ironically, toallowapropersolutionforper-class
scope).
5.2 Lossless Conversion to Heap Types
TheheaptypeAPIwasnotdesignedfor“lossless”conversionfromstatictypes; thatis, creatingatypethatworks
exactlylikeagivenstatictype.
9

