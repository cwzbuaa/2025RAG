### 第1页

Extending and Embedding Python
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 Recommendedthirdpartytools 3
2 Creatingextensionswithoutthirdpartytools 5
2.1 ExtendingPythonwithCorC++ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.1 ASimpleExample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.2 Intermezzo: ErrorsandExceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.3 BacktotheExample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.1.4 TheModule’sMethodTableandInitializationFunction . . . . . . . . . . . . . . . . . . 9
2.1.5 CompilationandLinkage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1.6 CallingPythonFunctionsfromC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.1.7 ExtractingParametersinExtensionFunctions . . . . . . . . . . . . . . . . . . . . . . . 14
2.1.8 KeywordParametersforExtensionFunctions . . . . . . . . . . . . . . . . . . . . . . . . 15
2.1.9 BuildingArbitraryValues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.1.10 ReferenceCounts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.1.11 WritingExtensionsinC++ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.1.12 ProvidingaCAPIforanExtensionModule . . . . . . . . . . . . . . . . . . . . . . . . 20
2.2 DefiningExtensionTypes: Tutorial. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.2.1 TheBasics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.2.2 AddingdataandmethodstotheBasicexample . . . . . . . . . . . . . . . . . . . . . . . 27
2.2.3 Providingfinercontroloverdataattributes . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.2.4 Supportingcyclicgarbagecollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
2.2.5 Subclassingothertypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
2.3 DefiningExtensionTypes: AssortedTopics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
2.3.1 FinalizationandDe-allocation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
2.3.2 ObjectPresentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
2.3.3 AttributeManagement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
2.3.4 ObjectComparison . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
2.3.5 AbstractProtocolSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
2.3.6 WeakReferenceSupport . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
2.3.7 MoreSuggestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.4 BuildingCandC++Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.4.1 BuildingCandC++Extensionswithsetuptools. . . . . . . . . . . . . . . . . . . . . . . 58
2.5 BuildingCandC++ExtensionsonWindows. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.5.1 ACookbookApproach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.5.2 DifferencesBetweenUnixandWindows . . . . . . . . . . . . . . . . . . . . . . . . . . 59
2.5.3 UsingDLLsinPractice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3 EmbeddingtheCPythonruntimeinalargerapplication 61
3.1 EmbeddingPythoninAnotherApplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.1.1 VeryHighLevelEmbedding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.1.2 BeyondVeryHighLevelEmbedding: Anoverview . . . . . . . . . . . . . . . . . . . . . 62
3.1.3 PureEmbedding. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.1.4 ExtendingEmbeddedPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.1.5 EmbeddingPythoninC++ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
i

### 第4页

3.1.6 CompilingandLinkingunderUnix-likesystems . . . . . . . . . . . . . . . . . . . . . . 66
A Glossary 69
B Aboutthisdocumentation 87
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
C HistoryandLicense 89
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 90
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 90
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 91
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 91
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 92
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 93
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 93
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
D Copyright 109
Index 111
ii

### 第5页

This document describes how to write modules in C or C++ to extend the Python interpreter with new modules.
Thosemodulescannotonlydefinenewfunctionsbutalsonewobjecttypesandtheirmethods. Thedocumentalso
describes how to embed the Python interpreter in another application, for use as an extension language. Finally,
itshowshowtocompileandlinkextensionmodulessothattheycanbeloadeddynamically(atruntime)intothe
interpreter,iftheunderlyingoperatingsystemsupportsthisfeature.
ThisdocumentassumesbasicknowledgeaboutPython. Foraninformalintroductiontothelanguage,seetutorial-
index. reference-indexgivesamoreformaldefinitionofthelanguage. library-indexdocumentstheexistingobject
types,functionsandmodules(bothbuilt-inandwritteninPython)thatgivethelanguageitswideapplicationrange.
ForadetaileddescriptionofthewholePython/CAPI,seetheseparatec-api-index.
CONTENTS 1

### 第6页

2 CONTENTS

### 第7页

CHAPTER
ONE
RECOMMENDED THIRD PARTY TOOLS
ThisguideonlycoversthebasictoolsforcreatingextensionsprovidedaspartofthisversionofCPython. Somethird
partytoolsofferbothsimplerandmoresophisticatedapproachestocreatingCandC++extensionsforPython.
3

### 第8页

4 Chapter1. Recommendedthirdpartytools

### 第9页

CHAPTER
TWO
CREATING EXTENSIONS WITHOUT THIRD PARTY TOOLS
ThissectionoftheguidecoverscreatingCandC++extensionswithoutassistancefromthirdpartytools. Itisintended
primarilyforcreatorsofthosetools,ratherthanbeingarecommendedwaytocreateyourownCextensions.
(cid:181) Seealso
PEP489–Multi-phaseextensionmoduleinitialization
2.1 Extending Python with C or C++
Itisquiteeasytoaddnewbuilt-inmodulestoPython,ifyouknowhowtoprograminC.Suchextensionmodulescan
dotwothingsthatcan’tbedonedirectlyinPython: theycanimplementnewbuilt-inobjecttypes,andtheycancall
Clibraryfunctionsandsystemcalls.
Tosupportextensions,thePythonAPI(ApplicationProgrammersInterface)definesasetoffunctions,macrosand
variablesthatprovideaccesstomostaspectsofthePythonrun-timesystem. ThePythonAPIisincorporatedinaC
sourcefilebyincludingtheheader"Python.h".
Thecompilationofanextensionmoduledependsonitsintendeduseaswellasonyoursystemsetup;detailsaregiven
inlaterchapters.
(cid:174) Note
TheCextensioninterfaceisspecifictoCPython,andextensionmodulesdonotworkonotherPythonimplemen-
tations. Inmanycases,itispossibletoavoidwritingCextensionsandpreserveportabilitytootherimplementa-
tions. Forexample,ifyourusecaseiscallingClibraryfunctionsorsystemcalls,youshouldconsiderusingthe
ctypesmoduleorthecffilibraryratherthanwritingcustomCcode. ThesemodulesletyouwritePythoncode
tointerfacewithCcodeandaremoreportablebetweenimplementationsofPythonthanwritingandcompiling
aCextensionmodule.
2.1.1 A Simple Example
Let’screateanextensionmodulecalledspam(thefavoritefoodofMontyPythonfans…)andlet’ssaywewantto
createaPythoninterfacetotheClibraryfunctionsystem()1. Thisfunctiontakesanull-terminatedcharacterstring
asargumentandreturnsaninteger. WewantthisfunctiontobecallablefromPythonasfollows:
>>> import spam
>>> status = spam.system("ls -l")
Beginbycreatingafilespammodule.c. (Historically,ifamoduleiscalledspam,theCfilecontainingitsimple-
mentationiscalledspammodule.c;ifthemodulenameisverylong,likespammify,themodulenamecanbejust
spammify.c.)
Thefirsttwolinesofourfilecanbe:
1Aninterfaceforthisfunctionalreadyexistsinthestandardmoduleos—itwaschosenasasimpleandstraightforwardexample.
5

| (cid:181) Seealso |
| --- |
| PEP489–Multi-phaseextensionmoduleinitialization |

### 第10页

#define PY_SSIZE_T_CLEAN
#include <Python.h>
whichpullsinthePythonAPI(youcanaddacommentdescribingthepurposeofthemoduleandacopyrightnotice
ifyoulike).
(cid:174) Note
SincePythonmaydefinesomepre-processordefinitionswhichaffectthestandardheadersonsomesystems,you
mustincludePython.hbeforeanystandardheadersareincluded.
#define PY_SSIZE_T_CLEAN was used to indicatethat Py_ssize_t shouldbe used insomeAPIs instead
ofint. ItisnotnecessarysincePython3.13,butwekeepithereforbackwardcompatibility. Seearg-parsing-
string-and-buffersforadescriptionofthismacro.
Alluser-visiblesymbolsdefinedby Python.h havea prefixof Py or PY,exceptthosedefinedinstandardheader
files. Forconvenience, andsincetheyareusedextensivelybythePythoninterpreter, "Python.h"includesafew
standardheaderfiles: <stdio.h>,<string.h>,<errno.h>,and<stdlib.h>. Ifthelatterheaderfiledoesnot
existonyoursystem,itdeclaresthefunctionsmalloc(),free()andrealloc()directly.
The next thing we add to our module file is the C function that will be called when the Python expression spam.
system(string)isevaluated(we’llseeshortlyhowitendsupbeingcalled):
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
const char *command;
int sts;
if (!PyArg_ParseTuple(args, "s", &command))
return NULL;
sts = system(command);
return PyLong_FromLong(sts);
}
ThereisastraightforwardtranslationfromtheargumentlistinPython(forexample,thesingleexpression"ls -l")
totheargumentspassedtotheCfunction. TheCfunctionalwayshastwoarguments,conventionallynamedselfand
args.
Theself argumentpointstothemoduleobjectformodule-levelfunctions;foramethoditwouldpointtotheobject
instance.
The args argument will be a pointer to a Python tuple object containing the arguments. Each item of the tuple
correspondstoanargumentinthecall’sargumentlist. TheargumentsarePythonobjects—inordertodoanything
withtheminourCfunctionwehavetoconvertthemtoCvalues. ThefunctionPyArg_ParseTuple()inthePython
APIcheckstheargumenttypesandconvertsthemtoCvalues. Itusesatemplatestringtodeterminetherequired
typesoftheargumentsaswellasthetypesoftheCvariablesintowhichtostoretheconvertedvalues. Moreabout
thislater.
PyArg_ParseTuple() returnstrue (nonzero)if allargumentshave therighttype anditscomponents havebeen
storedinthevariableswhoseaddressesarepassed. Itreturnsfalse(zero)ifaninvalidargumentlistwaspassed. In
thelattercaseitalsoraisesanappropriateexceptionsothecallingfunctioncanreturnNULLimmediately(aswesaw
intheexample).
6 Chapter2. Creatingextensionswithoutthirdpartytools

### 第11页

2.1.2 Intermezzo: Errors and Exceptions
AnimportantconventionthroughoutthePythoninterpreteristhefollowing: whenafunctionfails,itshouldsetan
exception condition and return an error value (usually -1 or a NULL pointer). Exception information is stored in
three members of the interpreter’s thread state. These are NULL if there is no exception. Otherwise they are the
C equivalents of the members of the Python tuple returned by sys.exc_info(). These are the exception type,
exceptioninstance,andatracebackobject. Itisimportanttoknowaboutthemtounderstandhowerrorsarepassed
around.
ThePythonAPIdefinesanumberoffunctionstosetvarioustypesofexceptions.
ThemostcommononeisPyErr_SetString(). ItsargumentsareanexceptionobjectandaCstring. Theexception
objectisusuallyapredefinedobjectlikePyExc_ZeroDivisionError. TheCstringindicatesthecauseoftheerror
andisconvertedtoaPythonstringobjectandstoredasthe“associatedvalue”oftheexception.
AnotherusefulfunctionisPyErr_SetFromErrno(),whichonlytakesanexceptionargumentandconstructsthe
associatedvaluebyinspectionoftheglobalvariableerrno. ThemostgeneralfunctionisPyErr_SetObject(),
which takes two object arguments, the exception and its associated value. You don’t need to Py_INCREF() the
objectspassedtoanyofthesefunctions.
Youcantestnon-destructivelywhetheranexceptionhasbeensetwithPyErr_Occurred(). Thisreturnsthecurrent
exceptionobject,orNULLifnoexceptionhasoccurred. Younormallydon’tneedtocallPyErr_Occurred()tosee
whetheranerroroccurredinafunctioncall,sinceyoushouldbeabletotellfromthereturnvalue.
When a function f that calls another function g detects that the latter fails, f should itself return an error value
(usuallyNULLor-1). ItshouldnotcalloneofthePyErr_*functions—onehasalreadybeencalledbyg. f’scaller
isthensupposedtoalsoreturnanerrorindicationtoitscaller,againwithoutcallingPyErr_*,andsoon—themost
detailed cause of the error was already reported by the function that first detected it. Once the error reaches the
Pythoninterpreter’smainloop,thisabortsthecurrentlyexecutingPythoncodeandtriestofindanexceptionhandler
specifiedbythePythonprogrammer.
(TherearesituationswhereamodulecanactuallygiveamoredetailederrormessagebycallinganotherPyErr_*
function, and in such cases it is fine to do so. As a general rule, however, this is not necessary, and can cause
informationaboutthecauseoftheerrortobelost: mostoperationscanfailforavarietyofreasons.)
Toignoreanexceptionsetbyafunctioncallthatfailed,theexceptionconditionmustbeclearedexplicitlybycalling
PyErr_Clear(). TheonlytimeCcodeshouldcallPyErr_Clear()isifitdoesn’twanttopasstheerrorontothe
interpreterbutwantstohandleitcompletelybyitself(possiblybytryingsomethingelse,orpretendingnothingwent
wrong).
Everyfailingmalloc()callmustbeturnedintoanexception—thedirectcallerofmalloc()(orrealloc())
mustcallPyErr_NoMemory()andreturnafailureindicatoritself. Alltheobject-creatingfunctions(forexample,
PyLong_FromLong())alreadydothis,sothisnoteisonlyrelevanttothosewhocallmalloc()directly.
Alsonotethat,withtheimportantexceptionofPyArg_ParseTuple()andfriends,functionsthatreturnaninteger
statususuallyreturnapositivevalueorzeroforsuccessand-1forfailure,likeUnixsystemcalls.
Finally, be careful to clean up garbage (by making Py_XDECREF() or Py_DECREF() calls for objects you have
alreadycreated)whenyoureturnanerrorindicator!
Thechoiceofwhichexceptiontoraiseisentirelyyours. TherearepredeclaredCobjectscorrespondingtoallbuilt-in
Pythonexceptions,suchasPyExc_ZeroDivisionError,whichyoucanusedirectly. Ofcourse,youshouldchoose
exceptionswisely—don’tusePyExc_TypeErrortomeanthatafilecouldn’tbeopened(thatshouldprobablybe
PyExc_OSError). Ifsomething’swrongwiththeargumentlist,thePyArg_ParseTuple()functionusuallyraises
PyExc_TypeError. If you have an argument whose value must be in a particular range or must satisfy other
conditions,PyExc_ValueErrorisappropriate.
Youcanalsodefineanewexceptionthatisuniquetoyourmodule. Thesimplestwaytodothisistodeclareastatic
globalobjectvariableatthebeginningofthefile:
static PyObject *SpamError = NULL;
and initialize it by calling PyErr_NewException() in the module’s Py_mod_exec function
(spam_module_exec()):
2.1. ExtendingPythonwithCorC++ 7

### 第12页

SpamError = PyErr_NewException("spam.error", NULL, NULL);
Since SpamError is a global variable, it will be overwritten every time the module is reinitialized, when the
Py_mod_execfunctioniscalled.
Fornow,let’savoidtheissue: wewillblockrepeatedinitializationbyraisinganImportError:
static PyObject *SpamError = NULL;
static int
spam_module_exec(PyObject *m)
{
if (SpamError != NULL) {
PyErr_SetString(PyExc_ImportError,
"cannot initialize spam module more than once");
return -1;
}
SpamError = PyErr_NewException("spam.error", NULL, NULL);
if (PyModule_AddObjectRef(m, "SpamError", SpamError) < 0) {
return -1;
}
return 0;
}
static PyModuleDef_Slot spam_module_slots[] = {
{Py_mod_exec, spam_module_exec},
{0, NULL}
};
static struct PyModuleDef spam_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "spam",
.m_size = 0, // non-negative
.m_slots = spam_module_slots,
};
PyMODINIT_FUNC
PyInit_spam(void)
{
return PyModuleDef_Init(&spam_module);
}
NotethatthePythonnamefortheexceptionobjectisspam.error. ThePyErr_NewException()functionmay
createaclasswiththebaseclassbeingException(unlessanotherclassispassedininsteadofNULL),describedin
bltin-exceptions.
NotealsothattheSpamErrorvariableretainsareferencetothenewlycreatedexceptionclass; thisisintentional!
Sincetheexceptioncouldberemovedfromthemodulebyexternalcode,anownedreferencetotheclassisneededto
ensurethatitwillnotbediscarded,causingSpamErrortobecomeadanglingpointer. Shoulditbecomeadangling
pointer,Ccodewhichraisestheexceptioncouldcauseacoredumporotherunintendedsideeffects.
Fornow,thePy_DECREF()calltoremovethisreferenceismissing. EvenwhenthePythoninterpretershutsdown,
theglobalSpamErrorvariablewillnotbegarbage-collected. Itwill“leak”. Wedid,however,ensurethatthiswill
happenatmostonceperprocess.
WediscusstheuseofPyMODINIT_FUNCasafunctionreturntypelaterinthissample.
Thespam.errorexceptioncanberaisedinyourextensionmoduleusingacalltoPyErr_SetString()asshown
below:
8 Chapter2. Creatingextensionswithoutthirdpartytools

### 第13页

static PyObject *
spam_system(PyObject *self, PyObject *args)
{
const char *command;
int sts;
if (!PyArg_ParseTuple(args, "s", &command))
return NULL;
sts = system(command);
if (sts < 0) {
PyErr_SetString(SpamError, "System command failed");
return NULL;
}
return PyLong_FromLong(sts);
}
2.1.3 Back to the Example
Goingbacktoourexamplefunction,youshouldnowbeabletounderstandthisstatement:
if (!PyArg_ParseTuple(args, "s", &command))
return NULL;
It returns NULL (the error indicator for functions returning object pointers) if an error is detected in the argument
list,relyingontheexceptionsetbyPyArg_ParseTuple(). Otherwisethestringvalueoftheargumenthasbeen
copiedtothelocalvariablecommand. Thisisapointerassignmentandyouarenotsupposedtomodifythestringto
whichitpoints(soinStandardC,thevariablecommandshouldproperlybedeclaredasconst char *command).
The next statement is a call to the Unix function system(), passing it the string we just got from
PyArg_ParseTuple():
sts = system(command);
Our spam.system() function must return the value of sts as a Python object. This is done using the function
PyLong_FromLong().
return PyLong_FromLong(sts);
Inthiscase,itwillreturnanintegerobject. (Yes,evenintegersareobjectsontheheapinPython!)
If you have a C function that returns no useful argument (a function returning void), the corresponding Python
functionmustreturnNone. Youneedthisidiomtodoso(whichisimplementedbythePy_RETURN_NONEmacro):
Py_INCREF(Py_None);
return Py_None;
Py_NoneistheCnameforthespecialPythonobjectNone. ItisagenuinePythonobjectratherthanaNULLpointer,
whichmeans“error”inmostcontexts,aswehaveseen.
2.1.4 The Module’s Method Table and Initialization Function
Ipromisedtoshowhowspam_system()iscalledfromPythonprograms. First,weneedtolistitsnameandaddress
ina“methodtable”:
static PyMethodDef spam_methods[] = {
...
{"system", spam_system, METH_VARARGS,
"Execute a shell command."},
(continuesonnextpage)
2.1. ExtendingPythonwithCorC++ 9

### 第14页

(continuedfrompreviouspage)
...
{NULL, NULL, 0, NULL} /* Sentinel */
};
Notethethirdentry(METH_VARARGS).Thisisaflagtellingtheinterpreterthecallingconventiontobeusedforthe
C function. It should normally always be METH_VARARGS or METH_VARARGS | METH_KEYWORDS; a value of 0
meansthatanobsoletevariantofPyArg_ParseTuple()isused.
WhenusingonlyMETH_VARARGS,thefunctionshouldexpectthePython-levelparameterstobepassedinasatuple
acceptableforparsingviaPyArg_ParseTuple();moreinformationonthisfunctionisprovidedbelow.
The METH_KEYWORDS bit may be set in the third field if keyword arguments should be passed to the function. In
thiscase,theCfunctionshouldacceptathirdPyObject *parameterwhichwillbeadictionaryofkeywords. Use
PyArg_ParseTupleAndKeywords()toparsetheargumentstosuchafunction.
Themethodtablemustbereferencedinthemoduledefinitionstructure:
static struct PyModuleDef spam_module = {
...
.m_methods = spam_methods,
...
};
This structure, in turn, must be passed to the interpreter in the module’s initialization function. The initialization
function must be named PyInit_name(), where name is the name of the module, and should be the only non-
staticitemdefinedinthemodulefile:
PyMODINIT_FUNC
PyInit_spam(void)
{
return PyModuleDef_Init(&spam_module);
}
NotethatPyMODINIT_FUNCdeclaresthefunctionasPyObject *returntype,declaresanyspeciallinkagedecla-
rationsrequiredbytheplatform,andforC++declaresthefunctionasextern "C".
PyInit_spam()iscalledwheneachinterpreterimportsitsmodulespamforthefirsttime. (Seebelowforcomments
aboutembeddingPython.) ApointertothemoduledefinitionmustbereturnedviaPyModuleDef_Init(),sothat
theimportmachinerycancreatethemoduleandstoreitinsys.modules.
When embedding Python, the PyInit_spam() function is not called automatically unless there’s an entry in the
PyImport_Inittab table. To add the module to the initialization table, use PyImport_AppendInittab(),
optionallyfollowedbyanimportofthemodule:
#define PY_SSIZE_T_CLEAN
#include <Python.h>
int
main(int argc, char *argv[])
{
PyStatus status;
PyConfig config;
PyConfig_InitPythonConfig(&config);
/* Add a built-in module, before Py_Initialize */
if (PyImport_AppendInittab("spam", PyInit_spam) == -1) {
fprintf(stderr, "Error: could not extend in-built modules table\n");
exit(1);
}
(continuesonnextpage)
10 Chapter2. Creatingextensionswithoutthirdpartytools

### 第15页

(continuedfrompreviouspage)
/* Pass argv[0] to the Python interpreter */
status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
if (PyStatus_Exception(status)) {
goto exception;
}
/* Initialize the Python interpreter. Required.
If this step fails, it will be a fatal error. */
status = Py_InitializeFromConfig(&config);
if (PyStatus_Exception(status)) {
goto exception;
}
PyConfig_Clear(&config);
/* Optionally import the module; alternatively,
import can be deferred until the embedded script
imports it. */
PyObject *pmodule = PyImport_ImportModule("spam");
if (!pmodule) {
PyErr_Print();
fprintf(stderr, "Error: could not import module 'spam'\n");
}
// ... use Python C API here ...
return 0;
exception:
PyConfig_Clear(&config);
Py_ExitStatusException(status);
}
(cid:174) Note
If you declare a global variable or a local static one, the module may experience unintended side-effects on
re-initialisation, for example when removing entries from sys.modules or importing compiled modules into
multipleinterpreterswithinaprocess(orfollowingafork()withoutaninterveningexec()). Ifmodulestate
isnotyetfullyisolated,authorsshouldconsidermarkingthemoduleashavingnosupportforsubinterpreters(via
Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED).
AmoresubstantialexamplemoduleisincludedinthePythonsourcedistributionasModules/xxlimited.c. This
filemaybeusedasatemplateorsimplyreadasanexample.
2.1.5 Compilation and Linkage
Therearetwomorethingstodobeforeyoucanuseyournewextension: compilingandlinkingitwiththePython
system. Ifyouusedynamicloading,thedetailsmaydependonthestyleofdynamicloadingyoursystemuses;seethe
chaptersaboutbuildingextensionmodules(chapterBuildingCandC++Extensions)andadditionalinformationthat
pertainsonlytobuildingonWindows(chapterBuildingCandC++ExtensionsonWindows)formoreinformation
aboutthis.
Ifyoucan’tusedynamicloading,orifyouwanttomakeyourmoduleapermanentpartofthePythoninterpreter,
youwillhavetochangetheconfigurationsetupandrebuildtheinterpreter. Luckily,thisisverysimpleonUnix: just
placeyourfile(spammodule.cforexample)intheModules/directoryofanunpackedsourcedistribution,adda
linetothefileModules/Setup.localdescribingyourfile:
2.1. ExtendingPythonwithCorC++ 11

### 第16页

spam spammodule.o
and rebuild the interpreter by running make in the toplevel directory. You can also run make in the Modules/
subdirectory,butthenyoumustfirstrebuildMakefiletherebyrunning‘makeMakefile’. (Thisisnecessaryeach
timeyouchangetheSetupfile.)
If your module requires additional libraries to link with, these can be listed on the line in the configuration file as
well,forinstance:
spam spammodule.o -lX11
2.1.6 Calling Python Functions from C
SofarwehaveconcentratedonmakingCfunctionscallablefromPython. Thereverseisalsouseful: callingPython
functionsfromC.Thisisespeciallythecaseforlibrariesthatsupportso-called“callback”functions. IfaCinterface
makesuseofcallbacks,theequivalentPythonoftenneedstoprovideacallbackmechanismtothePythonprogram-
mer; theimplementationwillrequirecallingthePythoncallbackfunctionsfromaCcallback. Otherusesarealso
imaginable.
Fortunately, the Python interpreter is easily called recursively, and there is a standard interface to call a Python
function. (Iwon’tdwellonhowtocallthePythonparserwithaparticularstringasinput—ifyou’reinterested,have
alookattheimplementationofthe-ccommandlineoptioninModules/main.cfromthePythonsourcecode.)
Calling a Python function is easy. First, the Python program must somehow pass you the Python function object.
Youshouldprovideafunction(orsomeotherinterface)todothis. Whenthisfunctioniscalled,saveapointertothe
Pythonfunctionobject(becarefultoPy_INCREF()it!) inaglobalvariable—orwhereveryouseefit. Forexample,
thefollowingfunctionmightbepartofamoduledefinition:
static PyObject *my_callback = NULL;
static PyObject *
my_set_callback(PyObject *dummy, PyObject *args)
{
PyObject *result = NULL;
PyObject *temp;
if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
if (!PyCallable_Check(temp)) {
PyErr_SetString(PyExc_TypeError, "parameter must be callable");
return NULL;
}
Py_XINCREF(temp); /* Add a reference to new callback */
Py_XDECREF(my_callback); /* Dispose of previous callback */
my_callback = temp; /* Remember new callback */
/* Boilerplate to return "None" */
Py_INCREF(Py_None);
result = Py_None;
}
return result;
}
This function must be registered with the interpreter using the METH_VARARGS flag; this is described in section
TheModule’sMethodTableandInitializationFunction. ThePyArg_ParseTuple()functionanditsargumentsare
documentedinsectionExtractingParametersinExtensionFunctions.
ThemacrosPy_XINCREF()andPy_XDECREF()increment/decrementthereferencecountofanobjectandaresafe
inthepresenceofNULLpointers(butnotethattempwillnotbeNULLinthiscontext). Moreinfoontheminsection
ReferenceCounts.
Later, whenitistimetocallthefunction, youcalltheCfunctionPyObject_CallObject(). Thisfunctionhas
12 Chapter2. Creatingextensionswithoutthirdpartytools

### 第17页

twoarguments,bothpointerstoarbitraryPythonobjects: thePythonfunction,andtheargumentlist. Theargument
list must always be a tuple object, whose length is the number of arguments. To call the Python function with no
arguments,passinNULL,oranemptytuple;tocallitwithoneargument,passasingletontuple. Py_BuildValue()
returnsatuplewhenitsformatstringconsistsofzeroormoreformatcodesbetweenparentheses. Forexample:
int arg;
PyObject *arglist;
PyObject *result;
...
arg = 123;
...
/* Time to call the callback */
arglist = Py_BuildValue("(i)", arg);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);
PyObject_CallObject() returns a Python object pointer: this is the return value of the Python func-
tion. PyObject_CallObject() is “reference-count-neutral” with respect to its arguments. In the exam-
ple a new tuple was created to serve as the argument list, which is Py_DECREF()-ed immediately after the
PyObject_CallObject()call.
ThereturnvalueofPyObject_CallObject()is“new”: eitheritisabrandnewobject,oritisanexistingobject
whosereferencecounthasbeenincremented. So,unlessyouwanttosaveitinaglobalvariable,youshouldsomehow
Py_DECREF()theresult,even(especially!) ifyouarenotinterestedinitsvalue.
Before you do this, however, it is important to check that the return value isn’t NULL. If it is, the Python function
terminatedbyraisinganexception. IftheCcodethatcalledPyObject_CallObject()iscalledfromPython,it
should now return an error indication to its Python caller, so the interpreter can print a stack trace, or the calling
Pythoncodecanhandletheexception. Ifthisisnotpossibleordesirable,theexceptionshouldbeclearedbycalling
PyErr_Clear(). Forexample:
if (result == NULL)
return NULL; /* Pass error back */
...use result...
Py_DECREF(result);
DependingonthedesiredinterfacetothePythoncallbackfunction,youmayalsohavetoprovideanargumentlistto
PyObject_CallObject(). InsomecasestheargumentlistisalsoprovidedbythePythonprogram,throughthe
sameinterfacethatspecifiedthecallbackfunction. Itcanthenbesavedandusedinthesamemannerasthefunction
object. Inothercases,youmayhavetoconstructanewtupletopassastheargumentlist. Thesimplestwaytodothis
istocallPy_BuildValue(). Forexample,ifyouwanttopassanintegraleventcode,youmightusethefollowing
code:
PyObject *arglist;
...
arglist = Py_BuildValue("(l)", eventcode);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);
if (result == NULL)
return NULL; /* Pass error back */
/* Here maybe use the result */
Py_DECREF(result);
NotetheplacementofPy_DECREF(arglist)immediatelyafterthecall, beforetheerrorcheck! Alsonotethat
strictlyspeakingthiscodeisnotcomplete: Py_BuildValue()mayrunoutofmemory,andthisshouldbechecked.
YoumayalsocallafunctionwithkeywordargumentsbyusingPyObject_Call(),whichsupportsargumentsand
keywordarguments. Asintheaboveexample,weusePy_BuildValue()toconstructthedictionary.
2.1. ExtendingPythonwithCorC++ 13

### 第18页

PyObject *dict;
...
dict = Py_BuildValue("{s:i}", "name", val);
result = PyObject_Call(my_callback, NULL, dict);
Py_DECREF(dict);
if (result == NULL)
return NULL; /* Pass error back */
/* Here maybe use the result */
Py_DECREF(result);
2.1.7 Extracting Parameters in Extension Functions
ThePyArg_ParseTuple()functionisdeclaredasfollows:
int PyArg_ParseTuple(PyObject *arg, const char *format, ...);
TheargargumentmustbeatupleobjectcontaininganargumentlistpassedfromPythontoaCfunction. Theformat
argumentmustbeaformatstring,whosesyntaxisexplainedinarg-parsinginthePython/CAPIReferenceManual.
Theremainingargumentsmustbeaddressesofvariableswhosetypeisdeterminedbytheformatstring.
NotethatwhilePyArg_ParseTuple()checksthatthePythonargumentshavetherequiredtypes,itcannotcheck
thevalidityoftheaddressesofCvariablespassedtothecall: ifyoumakemistakesthere,yourcodewillprobably
crashoratleastoverwriterandombitsinmemory. Sobecareful!
NotethatanyPythonobjectreferenceswhichareprovidedtothecallerareborrowedreferences;donotdecrement
theirreferencecount!
Someexamplecalls:
#define PY_SSIZE_T_CLEAN
#include <Python.h>
int ok;
int i, j;
long k, l;
const char *s;
Py_ssize_t size;
ok = PyArg_ParseTuple(args, ""); /* No arguments */
/* Python call: f() */
ok = PyArg_ParseTuple(args, "s", &s); /* A string */
/* Possible Python call: f('whoops!') */
ok = PyArg_ParseTuple(args, "lls", &k, &l, &s); /* Two longs and a string */
/* Possible Python call: f(1, 2, 'three') */
ok = PyArg_ParseTuple(args, "(ii)s#", &i, &j, &s, &size);
/* A pair of ints and a string, whose size is also returned */
/* Possible Python call: f((1, 2), 'three') */
{
const char *file;
const char *mode = "r";
int bufsize = 0;
ok = PyArg_ParseTuple(args, "s|si", &file, &mode, &bufsize);
/* A string, and optionally another string and an integer */
(continuesonnextpage)
14 Chapter2. Creatingextensionswithoutthirdpartytools

### 第19页

(continuedfrompreviouspage)
/* Possible Python calls:
f('spam')
f('spam', 'w')
f('spam', 'wb', 100000) */
}
{
int left, top, right, bottom, h, v;
ok = PyArg_ParseTuple(args, "((ii)(ii))(ii)",
&left, &top, &right, &bottom, &h, &v);
/* A rectangle and a point */
/* Possible Python call:
f(((0, 0), (400, 300)), (10, 10)) */
}
{
Py_complex c;
ok = PyArg_ParseTuple(args, "D:myfunction", &c);
/* a complex, also providing a function name for errors */
/* Possible Python call: myfunction(1+2j) */
}
2.1.8 Keyword Parameters for Extension Functions
ThePyArg_ParseTupleAndKeywords()functionisdeclaredasfollows:
int PyArg_ParseTupleAndKeywords(PyObject *arg, PyObject *kwdict,
const char *format, char * const *kwlist, ...);
TheargandformatparametersareidenticaltothoseofthePyArg_ParseTuple()function. Thekwdictparameter
is the dictionary of keywords received as the third parameter from the Python runtime. The kwlist parameter is a
NULL-terminatedlistofstringswhichidentifytheparameters;thenamesarematchedwiththetypeinformationfrom
formatfromlefttoright. Onsuccess,PyArg_ParseTupleAndKeywords()returnstrue,otherwiseitreturnsfalse
andraisesanappropriateexception.
(cid:174) Note
Nestedtuplescannotbeparsedwhenusingkeywordarguments! Keywordparameterspassedinwhicharenot
presentinthekwlistwillcauseTypeErrortoberaised.
Hereisanexamplemodulewhichuseskeywords,basedonanexamplebyGeoffPhilbrick(philbrick@hks.com):
#define PY_SSIZE_T_CLEAN
#include <Python.h>
static PyObject *
keywdarg_parrot(PyObject *self, PyObject *args, PyObject *keywds)
{
int voltage;
const char *state = "a stiff";
const char *action = "voom";
const char *type = "Norwegian Blue";
static char *kwlist[] = {"voltage", "state", "action", "type", NULL};
(continuesonnextpage)
2.1. ExtendingPythonwithCorC++ 15

### 第20页

(continuedfrompreviouspage)
if (!PyArg_ParseTupleAndKeywords(args, keywds, "i|sss", kwlist,
&voltage, &state, &action, &type))
return NULL;
printf("-- This parrot wouldn't %s if you put %i Volts through it.\n",
action, voltage);
printf("-- Lovely plumage, the %s -- It's %s!\n", type, state);
Py_RETURN_NONE;
}
static PyMethodDef keywdarg_methods[] = {
/* The cast of the function is necessary since PyCFunction values
* only take two PyObject* parameters, and keywdarg_parrot() takes
* three.
*/
{"parrot", (PyCFunction)(void(*)(void))keywdarg_parrot, METH_VARARGS | METH_
,→KEYWORDS,
"Print a lovely skit to standard output."},
{NULL, NULL, 0, NULL} /* sentinel */
};
static struct PyModuleDef keywdarg_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "keywdarg",
.m_size = 0,
.m_methods = keywdarg_methods,
};
PyMODINIT_FUNC
PyInit_keywdarg(void)
{
return PyModuleDef_Init(&keywdarg_module);
}
2.1.9 Building Arbitrary Values
ThisfunctionisthecounterparttoPyArg_ParseTuple(). Itisdeclaredasfollows:
PyObject *Py_BuildValue(const char *format, ...);
It recognizes a set of format units similar to the ones recognized by PyArg_ParseTuple(), but the arguments
(whichareinputtothefunction,notoutput)mustnotbepointers,justvalues. ItreturnsanewPythonobject,suitable
forreturningfromaCfunctioncalledfromPython.
OnedifferencewithPyArg_ParseTuple(): whilethelatterrequiresitsfirstargumenttobeatuple(sincePython
argument lists are always represented as tuples internally), Py_BuildValue() does not always build a tuple. It
builds a tuple only if its format string contains two or more format units. If the format string is empty, it returns
None;ifitcontainsexactlyoneformatunit,itreturnswhateverobjectisdescribedbythatformatunit. Toforceitto
returnatupleofsize0orone,parenthesizetheformatstring.
Examples(totheleftthecall,totherighttheresultingPythonvalue):
Py_BuildValue("") None
Py_BuildValue("i", 123) 123
Py_BuildValue("iii", 123, 456, 789) (123, 456, 789)
Py_BuildValue("s", "hello") 'hello'
(continuesonnextpage)
16 Chapter2. Creatingextensionswithoutthirdpartytools

### 第21页

(continuedfrompreviouspage)
Py_BuildValue("y", "hello") b'hello'
Py_BuildValue("ss", "hello", "world") ('hello', 'world')
Py_BuildValue("s#", "hello", 4) 'hell'
Py_BuildValue("y#", "hello", 4) b'hell'
Py_BuildValue("()") ()
Py_BuildValue("(i)", 123) (123,)
Py_BuildValue("(ii)", 123, 456) (123, 456)
Py_BuildValue("(i,i)", 123, 456) (123, 456)
Py_BuildValue("[i,i]", 123, 456) [123, 456]
Py_BuildValue("{s:i,s:i}",
"abc", 123, "def", 456) {'abc': 123, 'def': 456}
Py_BuildValue("((ii)(ii)) (ii)",
1, 2, 3, 4, 5, 6) (((1, 2), (3, 4)), (5, 6))
2.1.10 Reference Counts
InlanguageslikeCorC++,theprogrammerisresponsiblefordynamicallocationanddeallocationofmemoryon
theheap. InC,thisisdoneusingthefunctionsmalloc()andfree(). InC++,theoperatorsnewanddeleteare
usedwithessentiallythesamemeaningandwe’llrestrictthefollowingdiscussiontotheCcase.
Every block of memory allocated with malloc() should eventually be returned to the pool of available memory
byexactlyonecalltofree(). Itisimportanttocallfree()attherighttime. Ifablock’saddressisforgottenbut
free()isnotcalledforit,thememoryitoccupiescannotbereuseduntiltheprogramterminates. Thisiscalleda
memoryleak. Ontheotherhand,ifaprogramcallsfree()forablockandthencontinuestousetheblock,itcreates
aconflictwithreuseoftheblockthroughanothermalloc()call. Thisiscalledusingfreedmemory. Ithasthesame
badconsequencesasreferencinguninitializeddata—coredumps,wrongresults,mysteriouscrashes.
Commoncausesofmemoryleaksareunusualpathsthroughthecode. Forinstance,afunctionmayallocateablock
ofmemory,dosomecalculation,andthenfreetheblockagain. Nowachangeintherequirementsforthefunction
mayaddatesttothecalculationthatdetectsanerrorconditionandcanreturnprematurelyfromthefunction. It’s
easytoforgettofreetheallocatedmemoryblockwhentakingthisprematureexit,especiallywhenitisaddedlater
tothecode. Suchleaks,onceintroduced,oftengoundetectedforalongtime: theerrorexitistakenonlyinasmall
fractionofallcalls,andmostmodernmachineshaveplentyofvirtualmemory,sotheleakonlybecomesapparent
inalong-runningprocessthatusestheleakingfunctionfrequently. Therefore,it’simportanttopreventleaksfrom
happeningbyhavingacodingconventionorstrategythatminimizesthiskindoferrors.
SincePythonmakesheavyuseofmalloc()andfree(),itneedsastrategytoavoidmemoryleaksaswellasthe
useoffreedmemory. Thechosenmethodiscalledreferencecounting. Theprincipleissimple: everyobjectcontains
acounter,whichisincrementedwhenareferencetotheobjectisstoredsomewhere,andwhichisdecrementedwhen
areferencetoitisdeleted. Whenthecounterreacheszero,thelastreferencetotheobjecthasbeendeletedandthe
objectisfreed.
Analternativestrategyiscalledautomaticgarbagecollection. (Sometimes,referencecountingisalsoreferredtoas
agarbagecollectionstrategy,hencemyuseof“automatic”todistinguishthetwo.) Thebigadvantageofautomatic
garbagecollectionisthattheuserdoesn’tneedtocallfree()explicitly. (Anotherclaimedadvantageisanimprove-
mentinspeedormemoryusage—thisisnohardfacthowever.) ThedisadvantageisthatforC,thereisnotruly
portableautomaticgarbagecollector,whilereferencecountingcanbeimplementedportably(aslongasthefunctions
malloc()andfree()areavailable—whichtheCStandardguarantees). Maybesomedayasufficientlyportable
automaticgarbagecollectorwillbeavailableforC.Untilthen,we’llhavetolivewithreferencecounts.
While Python uses the traditional reference counting implementation, it also offers a cycle detector that works to
detect reference cycles. This allows applications to not worry about creating direct or indirect circular references;
thesearetheweaknessofgarbagecollectionimplementedusingonlyreferencecounting. Referencecyclesconsist
ofobjectswhichcontain(possiblyindirect)referencestothemselves,sothateachobjectinthecyclehasareference
countwhichisnon-zero. Typicalreferencecountingimplementationsarenotabletoreclaimthememorybelonging
to any objects in a reference cycle, or referenced from the objects in the cycle, even though there are no further
referencestothecycleitself.
The cycle detector is able to detect garbage cycles and can reclaim them. The gc module exposes a way to run
2.1. ExtendingPythonwithCorC++ 17

### 第22页

thedetector(thecollect()function),aswellasconfigurationinterfacesandtheabilitytodisablethedetectorat
runtime.
ReferenceCountinginPython
Therearetwomacros,Py_INCREF(x)andPy_DECREF(x),whichhandletheincrementinganddecrementingof
thereferencecount. Py_DECREF()alsofreestheobjectwhenthecountreacheszero. Forflexibility,itdoesn’tcall
free()directly—rather,itmakesacallthroughafunctionpointerintheobject’stypeobject. Forthispurpose(and
others),everyobjectalsocontainsapointertoitstypeobject.
Thebigquestionnowremains: whentousePy_INCREF(x)andPy_DECREF(x)? Let’sfirstintroducesometerms.
Nobody“owns”anobject;however,youcanownareferencetoanobject. Anobject’sreferencecountisnowdefined
asthenumberofownedreferencestoit. TheownerofareferenceisresponsibleforcallingPy_DECREF()whenthe
referenceisnolongerneeded. Ownershipofareferencecanbetransferred. Therearethreewaystodisposeofan
ownedreference: passiton,storeit,orcallPy_DECREF(). Forgettingtodisposeofanownedreferencecreatesa
memoryleak.
Itisalsopossibletoborrow2 areferencetoanobject. TheborrowerofareferenceshouldnotcallPy_DECREF().
Theborrowermustnotholdontotheobjectlongerthantheownerfromwhichitwasborrowed. Usingaborrowed
referenceaftertheownerhasdisposedofitrisksusingfreedmemoryandshouldbeavoidedcompletely3.
Theadvantageofborrowingoverowningareferenceisthatyoudon’tneedtotakecareofdisposingofthereference
onallpossiblepathsthroughthecode—inotherwords,withaborrowedreferenceyoudon’truntheriskofleaking
whenaprematureexitistaken. Thedisadvantageofborrowingoverowningisthattherearesomesubtlesituations
whereinseeminglycorrectcodeaborrowedreferencecanbeusedaftertheownerfromwhichitwasborrowedhas
infactdisposedofit.
AborrowedreferencecanbechangedintoanownedreferencebycallingPy_INCREF(). Thisdoesnotaffectthe
statusoftheownerfromwhichthereferencewasborrowed—itcreatesanewownedreference,andgivesfullowner
responsibilities(thenewownermustdisposeofthereferenceproperly,aswellasthepreviousowner).
OwnershipRules
Whenever an object reference is passed into or out of a function, it is part of the function’s interface specification
whetherownershipistransferredwiththereferenceornot.
Mostfunctionsthatreturnareferencetoanobjectpassonownershipwiththereference. Inparticular,allfunctions
whosefunctionitistocreateanewobject,suchasPyLong_FromLong()andPy_BuildValue(),passownership
tothereceiver. Eveniftheobjectisnotactuallynew,youstillreceiveownershipofanewreferencetothatobject.
Forinstance,PyLong_FromLong()maintainsacacheofpopularvaluesandcanreturnareferencetoacacheditem.
Many functions that extract objects from other objects also transfer ownership with the reference, for instance
PyObject_GetAttrString(). The picture is less clear, here, however, since a few common routines are ex-
ceptions: PyTuple_GetItem(),PyList_GetItem(),PyDict_GetItem(),andPyDict_GetItemString()
allreturnreferencesthatyouborrowfromthetuple,listordictionary.
ThefunctionPyImport_AddModule()alsoreturnsaborrowedreference,eventhoughitmayactuallycreatethe
objectitreturns: thisispossiblebecauseanownedreferencetotheobjectisstoredinsys.modules.
Whenyoupassanobjectreferenceintoanotherfunction,ingeneral,thefunctionborrowsthereferencefromyou—
ifitneedstostoreit,itwillusePy_INCREF()tobecomeanindependentowner. Thereareexactlytwoimportant
exceptionstothisrule: PyTuple_SetItem()andPyList_SetItem(). Thesefunctionstakeoverownershipof
theitempassedtothem—eveniftheyfail! (NotethatPyDict_SetItem()andfriendsdon’ttakeoverownership
—theyare“normal.”)
WhenaCfunctioniscalledfromPython,itborrowsreferencestoitsargumentsfromthecaller. Thecallerownsa
referencetotheobject,sotheborrowedreference’slifetimeisguaranteeduntilthefunctionreturns. Onlywhensucha
borrowedreferencemustbestoredorpassedon,itmustbeturnedintoanownedreferencebycallingPy_INCREF().
TheobjectreferencereturnedfromaCfunctionthatiscalledfromPythonmustbeanownedreference—ownership
istransferredfromthefunctiontoitscaller.
2Themetaphorof“borrowing”areferenceisnotcompletelycorrect:theownerstillhasacopyofthereference.
3Checkingthatthereferencecountisatleast1doesnotwork—thereferencecountitselfcouldbeinfreedmemoryandmaythusbereused
foranotherobject!
18 Chapter2. Creatingextensionswithoutthirdpartytools

### 第23页

ThinIce
Thereareafewsituationswhereseeminglyharmlessuseofaborrowedreferencecanleadtoproblems. Theseall
havetodowithimplicitinvocationsoftheinterpreter,whichcancausetheownerofareferencetodisposeofit.
ThefirstandmostimportantcasetoknowaboutisusingPy_DECREF()onanunrelatedobjectwhileborrowinga
referencetoalistitem. Forinstance:
void
bug(PyObject *list)
{
PyObject *item = PyList_GetItem(list, 0);
PyList_SetItem(list, 1, PyLong_FromLong(0L));
PyObject_Print(item, stdout, 0); /* BUG! */
}
Thisfunctionfirstborrowsareferencetolist[0],thenreplaceslist[1]withthevalue0,andfinallyprintsthe
borrowedreference. Looksharmless,right? Butit’snot!
Let’s follow the control flow into PyList_SetItem(). The list owns references to all its items, so when item
1 is replaced, it has to dispose of the original item 1. Now let’s suppose the original item 1 was an instance of
a user-defined class, and let’s further suppose that the class defined a __del__() method. If this class instance
hasareferencecountof1, disposingofitwillcallits__del__()method. Internally, PyList_SetItem()calls
Py_DECREF()onthereplaceditem,whichinvokesreplaceditem’scorrespondingtp_deallocfunction. During
deallocation,tp_dealloccallstp_finalize,whichismappedtothe__del__()methodforclassinstances(see
PEP442). ThisentiresequencehappenssynchronouslywithinthePyList_SetItem()call.
Since it is written in Python, the __del__() method can execute arbitrary Python code. Could it perhaps do
something to invalidate the reference to item in bug()? You bet! Assuming that the list passed into bug() is
accessibletothe__del__()method,itcouldexecuteastatementtotheeffectofdel list[0],andassumingthis
wasthelastreferencetothatobject,itwouldfreethememoryassociatedwithit,therebyinvalidatingitem.
The solution, once you know the source of the problem, is easy: temporarily increment the reference count. The
correctversionofthefunctionreads:
void
no_bug(PyObject *list)
{
PyObject *item = PyList_GetItem(list, 0);
Py_INCREF(item);
PyList_SetItem(list, 1, PyLong_FromLong(0L));
PyObject_Print(item, stdout, 0);
Py_DECREF(item);
}
This is a true story. An older version of Python contained variants of this bug and someone spent a considerable
amountoftimeinaCdebuggertofigureoutwhyhis__del__()methodswouldfail…
Thesecondcaseofproblemswithaborrowedreferenceisavariantinvolvingthreads. Normally,multiplethreadsin
thePythoninterpretercan’tgetineachother’sway,becausethereisagloballockprotectingPython’sentireobject
space. However,itispossibletotemporarilyreleasethislockusingthemacroPy_BEGIN_ALLOW_THREADS,andto
re-acquireitusingPy_END_ALLOW_THREADS.ThisiscommonaroundblockingI/Ocalls, toletotherthreadsuse
theprocessorwhilewaitingfortheI/Otocomplete. Obviously,thefollowingfunctionhasthesameproblemasthe
previousone:
void
bug(PyObject *list)
{
PyObject *item = PyList_GetItem(list, 0);
(continuesonnextpage)
2.1. ExtendingPythonwithCorC++ 19

### 第24页

(continuedfrompreviouspage)
Py_BEGIN_ALLOW_THREADS
...some blocking I/O call...
Py_END_ALLOW_THREADS
PyObject_Print(item, stdout, 0); /* BUG! */
}
NULLPointers
Ingeneral,functionsthattakeobjectreferencesasargumentsdonotexpectyoutopassthemNULLpointers,andwill
dumpcore(orcauselatercoredumps)ifyoudoso. FunctionsthatreturnobjectreferencesgenerallyreturnNULL
only to indicate that an exception occurred. The reason for not testing for NULL arguments is that functions often
passtheobjectstheyreceiveontootherfunction—ifeachfunctionweretotestforNULL,therewouldbealotof
redundanttestsandthecodewouldrunmoreslowly.
It is better to test for NULL only at the “source:” when a pointer that may be NULL is received, for example, from
malloc()orfromafunctionthatmayraiseanexception.
The macros Py_INCREF() and Py_DECREF() do not check for NULL pointers — however, their variants
Py_XINCREF()andPy_XDECREF()do.
Themacrosforcheckingforaparticularobjecttype(Pytype_Check())don’tcheckforNULLpointers—again,
thereismuchcodethatcallsseveraloftheseinarowtotestanobjectagainstvariousdifferentexpectedtypes,and
thiswouldgenerateredundanttests. TherearenovariantswithNULLchecking.
TheCfunctioncallingmechanismguaranteesthattheargumentlistpassedtoCfunctions(argsintheexamples)is
neverNULL—infactitguaranteesthatitisalwaysatuple4.
ItisasevereerrortoeverletaNULLpointer“escape”tothePythonuser.
2.1.11 Writing Extensions in C++
ItispossibletowriteextensionmodulesinC++. Somerestrictionsapply. Ifthemainprogram(thePythoninterpreter)
is compiled and linked by the C compiler, global or static objects with constructors cannot be used. This is not a
problemifthemainprogramislinkedbytheC++compiler. FunctionsthatwillbecalledbythePythoninterpreter
(inparticular,moduleinitializationfunctions)havetobedeclaredusingextern "C". Itisunnecessarytoenclose
thePythonheaderfilesinextern "C" {...}—theyusethisformalreadyifthesymbol__cplusplusisdefined
(allrecentC++compilersdefinethissymbol).
2.1.12 Providing a C API for an Extension Module
ManyextensionmodulesjustprovidenewfunctionsandtypestobeusedfromPython,butsometimesthecodein
anextensionmodulecanbeusefulforotherextensionmodules. Forexample,anextensionmodulecouldimplement
atype“collection”whichworkslikelistswithoutorder. JustlikethestandardPythonlisttypehasaCAPIwhich
permitsextensionmodulestocreateandmanipulatelists,thisnewcollectiontypeshouldhaveasetofCfunctions
fordirectmanipulationfromotherextensionmodules.
At first sight this seems easy: just write the functions (without declaring them static, of course), provide an
appropriateheaderfile,anddocumenttheCAPI.Andinfactthiswouldworkifallextensionmoduleswerealways
linkedstaticallywiththePythoninterpreter. Whenmodulesareusedassharedlibraries,however,thesymbolsdefined
inonemodulemaynotbevisibletoanothermodule. Thedetailsofvisibilitydependontheoperatingsystem;some
systems use one global namespace for the Python interpreter and all extension modules (Windows, for example),
whereas others require an explicit list of imported symbols at module link time (AIX is one example), or offer a
choiceofdifferentstrategies(mostUnices). Andevenifsymbolsaregloballyvisible,themodulewhosefunctions
onewishestocallmightnothavebeenloadedyet!
Portabilitythereforerequiresnottomakeanyassumptionsaboutsymbolvisibility. Thismeansthatallsymbolsin
extensionmodulesshouldbedeclaredstatic,exceptforthemodule’sinitializationfunction,inordertoavoidname
clasheswithotherextensionmodules(asdiscussedinsectionTheModule’sMethodTableandInitializationFunction).
4Theseguaranteesdon’tholdwhenyouusethe“old”stylecallingconvention—thisisstillfoundinmuchexistingcode.
20 Chapter2. Creatingextensionswithoutthirdpartytools

### 第25页

Anditmeansthatsymbolsthatshould beaccessiblefromotherextensionmodulesmustbeexportedinadifferent
way.
PythonprovidesaspecialmechanismtopassC-levelinformation(pointers)fromoneextensionmoduletoanother
one: Capsules. ACapsuleisaPythondatatypewhichstoresapointer(void*). Capsulescanonlybecreatedand
accessed via their C API, but they can be passed around like any other Python object. In particular, they can be
assigned to a name in an extension module’s namespace. Other extension modules can then import this module,
retrievethevalueofthisname,andthenretrievethepointerfromtheCapsule.
There are many ways in which Capsules can be used to export the C API of an extension module. Each function
couldgetitsownCapsule,orallCAPIpointerscouldbestoredinanarraywhoseaddressispublishedinaCapsule.
Andthevarioustasksofstoringandretrievingthepointerscanbedistributedindifferentwaysbetweenthemodule
providingthecodeandtheclientmodules.
Whichever method you choose, it’s important to name your Capsules properly. The function PyCapsule_New()
takesanameparameter(const char*);you’repermittedtopassinaNULLname,butwestronglyencourageyou
tospecifyaname. ProperlynamedCapsulesprovideadegreeofruntimetype-safety;thereisnofeasiblewaytotell
oneunnamedCapsulefromanother.
Inparticular,CapsulesusedtoexposeCAPIsshouldbegivenanamefollowingthisconvention:
modulename.attributename
TheconveniencefunctionPyCapsule_Import()makesiteasytoloadaCAPIprovidedviaaCapsule,butonly
iftheCapsule’snamematchesthisconvention. ThisbehaviorgivesCAPIusersahighdegreeofcertaintythatthe
CapsuletheyloadcontainsthecorrectCAPI.
Thefollowingexampledemonstratesanapproachthatputsmostoftheburdenonthewriteroftheexportingmodule,
whichisappropriateforcommonlyusedlibrarymodules. ItstoresallCAPIpointers(justoneintheexample!) inan
arrayofvoidpointerswhichbecomesthevalueofaCapsule. Theheaderfilecorrespondingtothemoduleprovides
amacrothattakescareofimportingthemoduleandretrievingitsCAPIpointers;clientmodulesonlyhavetocall
thismacrobeforeaccessingtheCAPI.
TheexportingmoduleisamodificationofthespammodulefromsectionASimpleExample. Thefunctionspam.
system()doesnotcalltheClibraryfunctionsystem()directly,butafunctionPySpam_System(),whichwould
of course do something more complicated in reality (such as adding “spam” to every command). This function
PySpam_System()isalsoexportedtootherextensionmodules.
ThefunctionPySpam_System()isaplainCfunction,declaredstaticlikeeverythingelse:
static int
PySpam_System(const char *command)
{
return system(command);
}
Thefunctionspam_system()ismodifiedinatrivialway:
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
const char *command;
int sts;
if (!PyArg_ParseTuple(args, "s", &command))
return NULL;
sts = PySpam_System(command);
return PyLong_FromLong(sts);
}
Inthebeginningofthemodule,rightaftertheline
2.1. ExtendingPythonwithCorC++ 21

### 第26页

#include <Python.h>
twomorelinesmustbeadded:
#define SPAM_MODULE
#include "spammodule.h"
The #define is used to tell the header file that it is being included in the exporting module, not a client module.
Finally,themodule’smod_execfunctionmusttakecareofinitializingtheCAPIpointerarray:
static int
spam_module_exec(PyObject *m)
{
static void *PySpam_API[PySpam_API_pointers];
PyObject *c_api_object;
/* Initialize the C API pointer array */
PySpam_API[PySpam_System_NUM] = (void *)PySpam_System;
/* Create a Capsule containing the API pointer array's address */
c_api_object = PyCapsule_New((void *)PySpam_API, "spam._C_API", NULL);
if (PyModule_Add(m, "_C_API", c_api_object) < 0) {
return -1;
}
return 0;
}
NotethatPySpam_APIisdeclaredstatic; otherwisethepointerarraywoulddisappearwhenPyInit_spam()
terminates!
Thebulkoftheworkisintheheaderfilespammodule.h,whichlookslikethis:
#ifndef Py_SPAMMODULE_H
#define Py_SPAMMODULE_H
#ifdef __cplusplus
extern "C" {
#endif
/* Header file for spammodule */
/* C API functions */
#define PySpam_System_NUM 0
#define PySpam_System_RETURN int
#define PySpam_System_PROTO (const char *command)
/* Total number of C API pointers */
#define PySpam_API_pointers 1
#ifdef SPAM_MODULE
/* This section is used when compiling spammodule.c */
static PySpam_System_RETURN PySpam_System PySpam_System_PROTO;
#else
/* This section is used in modules that use spammodule's API */
(continuesonnextpage)
22 Chapter2. Creatingextensionswithoutthirdpartytools

### 第27页

(continuedfrompreviouspage)
static void **PySpam_API;
#define PySpam_System \
(*(PySpam_System_RETURN (*)PySpam_System_PROTO) PySpam_API[PySpam_System_NUM])
/* Return -1 on error, 0 on success.
* PyCapsule_Import will set an exception if there's an error.
*/
static int
import_spam(void)
{
PySpam_API = (void **)PyCapsule_Import("spam._C_API", 0);
return (PySpam_API != NULL) ? 0 : -1;
}
#endif
#ifdef __cplusplus
}
#endif
#endif /* !defined(Py_SPAMMODULE_H) */
AllthataclientmodulemustdoinordertohaveaccesstothefunctionPySpam_System()istocallthefunction
(orrathermacro)import_spam()initsmod_execfunction:
static int
client_module_exec(PyObject *m)
{
if (import_spam() < 0) {
return -1;
}
/* additional initialization can happen here */
return 0;
}
Themaindisadvantageofthisapproachisthatthefilespammodule.hisrathercomplicated. However, thebasic
structureisthesameforeachfunctionthatisexported,soithastobelearnedonlyonce.
Finally it should be mentioned that Capsules offer additional functionality, which is especially useful for memory
allocationanddeallocationofthepointerstoredinaCapsule. ThedetailsaredescribedinthePython/CAPIReference
ManualinthesectioncapsulesandintheimplementationofCapsules(filesInclude/pycapsule.handObjects/
pycapsule.cinthePythonsourcecodedistribution).
2.2 Defining Extension Types: Tutorial
PythonallowsthewriterofaCextensionmoduletodefinenewtypesthatcanbemanipulatedfromPythoncode,
muchlikethebuilt-instrandlisttypes. Thecodeforallextensiontypesfollowsapattern, buttherearesome
detailsthatyouneedtounderstandbeforeyoucangetstarted. Thisdocumentisagentleintroductiontothetopic.
2.2.1 The Basics
TheCPythonruntimeseesallPythonobjectsasvariablesoftypePyObject*,whichservesasa“basetype”forall
Pythonobjects. ThePyObjectstructureitselfonlycontainstheobject’sreferencecountandapointertotheobject’s
“typeobject”. Thisiswheretheactionis;thetypeobjectdetermineswhich(C)functionsgetcalledbytheinterpreter
2.2. DefiningExtensionTypes: Tutorial 23

### 第28页

when, forinstance, anattributegetslookeduponanobject, amethodcalled, oritismultipliedbyanotherobject.
TheseCfunctionsarecalled“typemethods”.
So,ifyouwanttodefineanewextensiontype,youneedtocreateanewtypeobject.
Thissortofthingcanonlybeexplainedbyexample,sohere’saminimal,butcomplete,modulethatdefinesanew
typenamedCustominsideaCextensionmodulecustom:
(cid:174) Note
Whatwe’reshowinghereisthetraditionalwayofdefiningstaticextensiontypes. Itshouldbeadequateformost
uses. TheCAPIalsoallowsdefiningheap-allocatedextensiontypesusingthePyType_FromSpec()function,
whichisn’tcoveredinthistutorial.
#define PY_SSIZE_T_CLEAN
#include <Python.h>
typedef struct {
PyObject_HEAD
/* Type-specific fields go here. */
} CustomObject;
static PyTypeObject CustomType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "custom.Custom",
.tp_doc = PyDoc_STR("Custom objects"),
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
.tp_flags = Py_TPFLAGS_DEFAULT,
.tp_new = PyType_GenericNew,
};
static int
custom_module_exec(PyObject *m)
{
if (PyType_Ready(&CustomType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
return -1;
}
return 0;
}
static PyModuleDef_Slot custom_module_slots[] = {
{Py_mod_exec, custom_module_exec},
// Just use this while using static types
{Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
{0, NULL}
};
static PyModuleDef custom_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "custom",
.m_doc = "Example module that creates an extension type.",
(continuesonnextpage)
24 Chapter2. Creatingextensionswithoutthirdpartytools

### 第29页

(continuedfrompreviouspage)
.m_size = 0,
.m_slots = custom_module_slots,
};
PyMODINIT_FUNC
PyInit_custom(void)
{
return PyModuleDef_Init(&custom_module);
}
Nowthat’squiteabittotakeinatonce, buthopefullybitswillseemfamiliarfromthepreviouschapter. Thisfile
definesthreethings:
1. WhataCustomobjectcontains: thisistheCustomObjectstruct,whichisallocatedonceforeachCustom
instance.
2. How the Custom type behaves: this is the CustomType struct, which defines a set of flags and function
pointersthattheinterpreterinspectswhenspecificoperationsarerequested.
3. How to define and execute the custom module: this is the PyInit_custom function and the associated
custom_modulestructfordefiningthemodule, andthecustom_module_execfunctiontosetupafresh
moduleobject.
Thefirstbitis:
typedef struct {
PyObject_HEAD
} CustomObject;
This is what a Custom object will contain. PyObject_HEAD is mandatory at the start of each object struct and
definesafieldcalledob_baseoftypePyObject,containingapointertoatypeobjectandareferencecount(these
canbeaccessedusingthemacrosPy_TYPEandPy_REFCNTrespectively). Thereasonforthemacroistoabstract
awaythelayoutandtoenableadditionalfieldsindebugbuilds.
(cid:174) Note
There is no semicolon above after the PyObject_HEAD macro. Be wary of adding one by accident: some
compilerswillcomplain.
Of course, objects generally store additional data besides the standard PyObject_HEAD boilerplate; for example,
hereisthedefinitionforstandardPythonfloats:
typedef struct {
PyObject_HEAD
double ob_fval;
} PyFloatObject;
Thesecondbitisthedefinitionofthetypeobject.
static PyTypeObject CustomType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "custom.Custom",
.tp_doc = PyDoc_STR("Custom objects"),
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
.tp_flags = Py_TPFLAGS_DEFAULT,
.tp_new = PyType_GenericNew,
};
2.2. DefiningExtensionTypes: Tutorial 25

### 第30页

(cid:174) Note
We recommend using C99-style designated initializers as above, to avoid listing all the PyTypeObject fields
thatyoudon’tcareaboutandalsotoavoidcaringaboutthefields’declarationorder.
TheactualdefinitionofPyTypeObjectinobject.hhasmanymorefieldsthanthedefinitionabove. Theremaining
fieldswillbefilledwithzerosbytheCcompiler,andit’scommonpracticetonotspecifythemexplicitlyunlessyou
needthem.
We’regoingtopickitapart,onefieldatatime:
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
Thislineismandatoryboilerplatetoinitializetheob_basefieldmentionedabove.
.tp_name = "custom.Custom",
Thenameofourtype. Thiswillappearinthedefaulttextualrepresentationofourobjectsandinsomeerrormessages,
forexample:
>>> "" + custom.Custom()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "custom.Custom") to str
Notethatthenameisadottednamethatincludesboththemodulenameandthenameofthetypewithinthemodule.
ThemoduleinthiscaseiscustomandthetypeisCustom,sowesetthetypenametocustom.Custom. Usingthe
realdottedimportpathisimportanttomakeyourtypecompatiblewiththepydocandpicklemodules.
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
ThisissothatPythonknowshowmuchmemorytoallocatewhencreatingnewCustominstances. tp_itemsize
isonlyusedforvariable-sizedobjectsandshouldotherwisebezero.
(cid:174) Note
IfyouwantyourtypetobesubclassablefromPython,andyourtypehasthesametp_basicsizeasitsbase
type, you may have problems with multiple inheritance. A Python subclass of your type will have to list your
typefirstinits__bases__,orelseitwillnotbeabletocallyourtype’s__new__()methodwithoutgettingan
error. Youcanavoidthisproblembyensuringthatyourtypehasalargervaluefortp_basicsizethanitsbase
typedoes. Mostofthetime,thiswillbetrueanyway,becauseeitheryourbasetypewillbeobject,orelseyou
willbeaddingdatamemberstoyourbasetype,andthereforeincreasingitssize.
WesettheclassflagstoPy_TPFLAGS_DEFAULT.
.tp_flags = Py_TPFLAGS_DEFAULT,
Alltypesshouldincludethisconstantintheirflags. ItenablesallofthemembersdefineduntilatleastPython3.3. If
youneedfurthermembers,youwillneedtoORthecorrespondingflags.
Weprovideadocstringforthetypeintp_doc.
.tp_doc = PyDoc_STR("Custom objects"),
To enable object creation, we have to provide a tp_new handler. This is the equivalent of the Python method
__new__(),buthastobespecifiedexplicitly. Inthiscase,wecanjustusethedefaultimplementationprovidedby
theAPIfunctionPyType_GenericNew().
26 Chapter2. Creatingextensionswithoutthirdpartytools

### 第31页

.tp_new = PyType_GenericNew,
Everythingelseinthefileshouldbefamiliar,exceptforsomecodeincustom_module_exec():
if (PyType_Ready(&CustomType) < 0) {
return -1;
}
ThisinitializestheCustomtype,fillinginanumberofmemberstotheappropriatedefaultvalues,includingob_type
thatweinitiallysettoNULL.
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
return -1;
}
Thisaddsthetypetothemoduledictionary. ThisallowsustocreateCustominstancesbycallingtheCustomclass:
>>> import custom
>>> mycustom = custom.Custom()
That’sit! Allthatremainsistobuildit;puttheabovecodeinafilecalledcustom.c,
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
[project]
name = "custom"
version = "1"
inafilecalledpyproject.toml,and
from setuptools import Extension, setup
setup(ext_modules=[Extension("custom", ["custom.c"])])
inafilecalledsetup.py;thentyping
$ python -m pip install .
inashellshouldproduceafilecustom.soinasubdirectoryandinstallit;nowfireupPython—youshouldbeable
toimport customandplayaroundwithCustomobjects.
Thatwasn’tsohard,wasit?
Ofcourse,thecurrentCustomtypeisprettyuninteresting. Ithasnodataanddoesn’tdoanything. Itcan’tevenbe
subclassed.
2.2.2 Adding data and methods to the Basic example
Let’sextendthebasicexampletoaddsomedataandmethods. Let’salsomakethetypeusableasabaseclass. We’ll
createanewmodule,custom2thataddsthesecapabilities:
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stddef.h> /* for offsetof() */
typedef struct {
PyObject_HEAD
PyObject *first; /* first name */
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 27

### 第32页

(continuedfrompreviouspage)
PyObject *last; /* last name */
int number;
} CustomObject;
static void
Custom_dealloc(PyObject *op)
{
CustomObject *self = (CustomObject *) op;
Py_XDECREF(self->first);
Py_XDECREF(self->last);
Py_TYPE(self)->tp_free(self);
}
static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
CustomObject *self;
self = (CustomObject *) type->tp_alloc(type, 0);
if (self != NULL) {
self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->first == NULL) {
Py_DECREF(self);
return NULL;
}
self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->last == NULL) {
Py_DECREF(self);
return NULL;
}
self->number = 0;
}
return (PyObject *) self;
}
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
CustomObject *self = (CustomObject *) op;
static char *kwlist[] = {"first", "last", "number", NULL};
PyObject *first = NULL, *last = NULL;
if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
&first, &last,
&self->number))
return -1;
if (first) {
Py_XSETREF(self->first, Py_NewRef(first));
}
if (last) {
Py_XSETREF(self->last, Py_NewRef(last));
}
return 0;
}
static PyMemberDef Custom_members[] = {
(continuesonnextpage)
28 Chapter2. Creatingextensionswithoutthirdpartytools

### 第33页

(continuedfrompreviouspage)
{"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
"first name"},
{"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
"last name"},
{"number", Py_T_INT, offsetof(CustomObject, number), 0,
"custom number"},
{NULL} /* Sentinel */
};
static PyObject *
Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
{
CustomObject *self = (CustomObject *) op;
if (self->first == NULL) {
PyErr_SetString(PyExc_AttributeError, "first");
return NULL;
}
if (self->last == NULL) {
PyErr_SetString(PyExc_AttributeError, "last");
return NULL;
}
return PyUnicode_FromFormat("%S %S", self->first, self->last);
}
static PyMethodDef Custom_methods[] = {
{"name", Custom_name, METH_NOARGS,
"Return the name, combining the first and last name"
},
{NULL} /* Sentinel */
};
static PyTypeObject CustomType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "custom2.Custom",
.tp_doc = PyDoc_STR("Custom objects"),
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
.tp_new = Custom_new,
.tp_init = Custom_init,
.tp_dealloc = Custom_dealloc,
.tp_members = Custom_members,
.tp_methods = Custom_methods,
};
static int
custom_module_exec(PyObject *m)
{
if (PyType_Ready(&CustomType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
return -1;
}
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 29

### 第34页

(continuedfrompreviouspage)
return 0;
}
static PyModuleDef_Slot custom_module_slots[] = {
{Py_mod_exec, custom_module_exec},
{Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
{0, NULL}
};
static PyModuleDef custom_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "custom2",
.m_doc = "Example module that creates an extension type.",
.m_size = 0,
.m_slots = custom_module_slots,
};
PyMODINIT_FUNC
PyInit_custom2(void)
{
return PyModuleDef_Init(&custom_module);
}
Thisversionofthemodulehasanumberofchanges.
TheCustomtypenowhasthreedataattributesinitsCstruct,first,last,andnumber. Thefirstandlastvariablesare
Pythonstringscontainingfirstandlastnames. ThenumberattributeisaCinteger.
Theobjectstructureisupdatedaccordingly:
typedef struct {
PyObject_HEAD
PyObject *first; /* first name */
PyObject *last; /* last name */
int number;
} CustomObject;
Because we now have data to manage, we have to be more careful about object allocation and deallocation. At a
minimum,weneedadeallocationmethod:
static void
Custom_dealloc(PyObject *op)
{
CustomObject *self = (CustomObject *) op;
Py_XDECREF(self->first);
Py_XDECREF(self->last);
Py_TYPE(self)->tp_free(self);
}
whichisassignedtothetp_deallocmember:
.tp_dealloc = Custom_dealloc,
ThismethodfirstclearsthereferencecountsofthetwoPythonattributes. Py_XDECREF()correctlyhandlesthecase
whereitsargumentisNULL(whichmighthappenhereiftp_newfailedmidway). Itthencallsthetp_freemember
oftheobject’stype(computedbyPy_TYPE(self))tofreetheobject’smemory. Notethattheobject’stypemight
notbeCustomType,becausetheobjectmaybeaninstanceofasubclass.
30 Chapter2. Creatingextensionswithoutthirdpartytools

### 第35页

(cid:174) Note
The explicit cast to CustomObject * above is needed because we defined Custom_dealloc to take a
PyObject * argument, as the tp_dealloc function pointer expects to receive a PyObject * argument.
By assigning to the tp_dealloc slot of a type, we declare that it can only be called with instances of our
CustomObjectclass,sothecastto(CustomObject *)issafe. Thisisobject-orientedpolymorphism,inC!
In existing code, or in previous versions of this tutorial, you might see similar functions take a pointer to the
subtypeobjectstructure(CustomObject*)directly,likethis:
Custom_dealloc(CustomObject *self)
{
Py_XDECREF(self->first);
Py_XDECREF(self->last);
Py_TYPE(self)->tp_free((PyObject *) self);
}
...
.tp_dealloc = (destructor) Custom_dealloc,
ThisdoesthesamethingonallarchitecturesthatCPythonsupports,butaccordingtotheCstandard,itinvokes
undefinedbehavior.
Wewanttomakesurethatthefirstandlastnamesareinitializedtoemptystrings,soweprovideatp_newimple-
mentation:
static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
CustomObject *self;
self = (CustomObject *) type->tp_alloc(type, 0);
if (self != NULL) {
self->first = PyUnicode_FromString("");
if (self->first == NULL) {
Py_DECREF(self);
return NULL;
}
self->last = PyUnicode_FromString("");
if (self->last == NULL) {
Py_DECREF(self);
return NULL;
}
self->number = 0;
}
return (PyObject *) self;
}
andinstallitinthetp_newmember:
.tp_new = Custom_new,
Thetp_newhandlerisresponsibleforcreating(asopposedtoinitializing)objectsofthetype. ItisexposedinPython
as the __new__() method. It is not required to define a tp_new member, and indeed many extension types will
simplyreusePyType_GenericNew()asdoneinthefirstversionoftheCustomtypeabove. Inthiscase,weuse
thetp_newhandlertoinitializethefirstandlastattributestonon-NULLdefaultvalues.
tp_new is passed the type being instantiated (not necessarily CustomType, if a subclass is instantiated) and any
argumentspassedwhenthetypewascalled,andisexpectedtoreturntheinstancecreated. tp_newhandlersalways
accept positional and keyword arguments, but they often ignore the arguments, leaving the argument handling to
initializer(a.k.a. tp_initinCor__init__inPython)methods.
2.2. DefiningExtensionTypes: Tutorial 31

### 第36页

(cid:174) Note
tp_newshouldn’tcalltp_initexplicitly,astheinterpreterwilldoititself.
Thetp_newimplementationcallsthetp_allocslottoallocatememory:
self = (CustomObject *) type->tp_alloc(type, 0);
Sincememoryallocationmayfail,wemustcheckthetp_allocresultagainstNULLbeforeproceeding.
(cid:174) Note
Wedidn’tfillthetp_allocslotourselves. RatherPyType_Ready()fillsitforusbyinheritingitfromourbase
class,whichisobjectbydefault. Mosttypesusethedefaultallocationstrategy.
(cid:174) Note
Ifyouarecreatingaco-operativetp_new(onethatcallsabasetype’stp_newor__new__()), youmustnot
trytodeterminewhatmethodtocallusingmethodresolutionorderatruntime. Alwaysstaticallydeterminewhat
type you are going to call, and call its tp_new directly, or via type->tp_base->tp_new. If you do not do
this,PythonsubclassesofyourtypethatalsoinheritfromotherPython-definedclassesmaynotworkcorrectly.
(Specifically,youmaynotbeabletocreateinstancesofsuchsubclasseswithoutgettingaTypeError.)
Wealsodefineaninitializationfunctionwhichacceptsargumentstoprovideinitialvaluesforourinstance:
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
CustomObject *self = (CustomObject *) op;
static char *kwlist[] = {"first", "last", "number", NULL};
PyObject *first = NULL, *last = NULL, *tmp;
if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
&first, &last,
&self->number))
return -1;
if (first) {
tmp = self->first;
Py_INCREF(first);
self->first = first;
Py_XDECREF(tmp);
}
if (last) {
tmp = self->last;
Py_INCREF(last);
self->last = last;
Py_XDECREF(tmp);
}
return 0;
}
byfillingthetp_initslot.
32 Chapter2. Creatingextensionswithoutthirdpartytools

### 第37页

.tp_init = Custom_init,
Thetp_initslotisexposedinPythonasthe__init__()method. Itisusedtoinitializeanobjectafterit’screated.
Initializersalwaysacceptpositionalandkeywordarguments,andtheyshouldreturneither0onsuccessor-1onerror.
Unlikethetp_newhandler,thereisnoguaranteethattp_initiscalledatall(forexample,thepicklemoduleby
defaultdoesn’tcall__init__()onunpickledinstances). Itcanalsobecalledmultipletimes. Anyonecancallthe
__init__()methodonourobjects. Forthisreason,wehavetobeextracarefulwhenassigningthenewattribute
values. Wemightbetempted,forexampletoassignthefirstmemberlikethis:
if (first) {
Py_XDECREF(self->first);
Py_INCREF(first);
self->first = first;
}
Butthiswouldberisky. Ourtypedoesn’trestrictthetypeofthefirstmember,soitcouldbeanykindofobject.
Itcouldhaveadestructorthatcausescodetobeexecutedthattriestoaccessthefirstmember;orthatdestructor
coulddetachthethreadstateandletarbitrarycoderuninotherthreadsthataccessesandmodifiesourobject.
Tobeparanoidandprotectourselvesagainstthispossibility,wealmostalwaysreassignmembersbeforedecrementing
theirreferencecounts. Whendon’twehavetodothis?
• whenweabsolutelyknowthatthereferencecountisgreaterthan1;
• whenweknowthatdeallocationoftheobject1willneitherdetachthethreadstatenorcauseanycallsbackinto
ourtype’scode;
• whendecrementingareferencecountinatp_deallochandleronatypewhichdoesn’tsupportcyclicgarbage
collection2.
Wewanttoexposeourinstancevariablesasattributes. Thereareanumberofwaystodothat. Thesimplestwayis
todefinememberdefinitions:
static PyMemberDef Custom_members[] = {
{"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
"first name"},
{"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
"last name"},
{"number", Py_T_INT, offsetof(CustomObject, number), 0,
"custom number"},
{NULL} /* Sentinel */
};
andputthedefinitionsinthetp_membersslot:
.tp_members = Custom_members,
Each member definition has a member name, type, offset, access flags and documentation string. See the Generic
AttributeManagementsectionbelowfordetails.
Adisadvantageofthisapproachisthatitdoesn’tprovideawaytorestrictthetypesofobjectsthatcanbeassigned
tothePythonattributes. Weexpectthefirstandlastnamestobestrings, butanyPythonobjectscanbeassigned.
Further,theattributescanbedeleted,settingtheCpointerstoNULL.Eventhoughwecanmakesurethemembers
areinitializedtonon-NULLvalues,thememberscanbesettoNULLiftheattributesaredeleted.
Wedefineasinglemethod,Custom.name(),thatoutputstheobjectsnameastheconcatenationofthefirstandlast
names.
1Thisistruewhenweknowthattheobjectisabasictype,likeastringorafloat.
2Wereliedonthisinthetp_deallochandlerinthisexample,becauseourtypedoesn’tsupportgarbagecollection.
2.2. DefiningExtensionTypes: Tutorial 33

### 第38页

static PyObject *
Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
{
CustomObject *self = (CustomObject *) op;
if (self->first == NULL) {
PyErr_SetString(PyExc_AttributeError, "first");
return NULL;
}
if (self->last == NULL) {
PyErr_SetString(PyExc_AttributeError, "last");
return NULL;
}
return PyUnicode_FromFormat("%S %S", self->first, self->last);
}
ThemethodisimplementedasaCfunctionthattakesaCustom(orCustomsubclass)instanceasthefirstargument.
Methods always take an instance as the first argument. Methods often take positional and keyword arguments as
well, butinthiscasewedon’ttakeanyanddon’tneedtoacceptapositionalargumenttupleorkeywordargument
dictionary. ThismethodisequivalenttothePythonmethod:
def name(self):
return "%s %s" % (self.first, self.last)
NotethatwehavetocheckforthepossibilitythatourfirstandlastmembersareNULL.Thisisbecausetheycan
bedeleted,inwhichcasetheyaresettoNULL.Itwouldbebettertopreventdeletionoftheseattributesandtorestrict
theattributevaluestobestrings. We’llseehowtodothatinthenextsection.
Nowthatwe’vedefinedthemethod,weneedtocreateanarrayofmethoddefinitions:
static PyMethodDef Custom_methods[] = {
{"name", Custom_name, METH_NOARGS,
"Return the name, combining the first and last name"
},
{NULL} /* Sentinel */
};
(notethatweusedtheMETH_NOARGSflagtoindicatethatthemethodisexpectingnoargumentsotherthanself)
andassignittothetp_methodsslot:
.tp_methods = Custom_methods,
Finally,we’llmakeourtypeusableasabaseclassforsubclassing. We’vewrittenourmethodscarefullysofarsothat
theydon’tmakeanyassumptionsaboutthetypeoftheobjectbeingcreatedorused,soallweneedtodoistoadd
thePy_TPFLAGS_BASETYPEtoourclassflagdefinition:
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
WerenamePyInit_custom()toPyInit_custom2(),updatethemodulenameinthePyModuleDefstruct,and
updatethefullclassnameinthePyTypeObjectstruct.
Finally,weupdateoursetup.pyfiletoincludethenewmodule,
from setuptools import Extension, setup
setup(ext_modules=[
Extension("custom", ["custom.c"]),
Extension("custom2", ["custom2.c"]),
])
andthenwere-installsothatwecanimport custom2:
34 Chapter2. Creatingextensionswithoutthirdpartytools

### 第39页

$ python -m pip install .
2.2.3 Providing finer control over data attributes
Inthissection,we’llprovidefinercontroloverhowthefirstandlastattributesaresetintheCustomexample.
Inthepreviousversionofourmodule,theinstancevariablesfirstandlastcouldbesettonon-stringvaluesor
evendeleted. Wewanttomakesurethattheseattributesalwayscontainstrings.
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stddef.h> /* for offsetof() */
typedef struct {
PyObject_HEAD
PyObject *first; /* first name */
PyObject *last; /* last name */
int number;
} CustomObject;
static void
Custom_dealloc(PyObject *op)
{
CustomObject *self = (CustomObject *) op;
Py_XDECREF(self->first);
Py_XDECREF(self->last);
Py_TYPE(self)->tp_free(self);
}
static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
CustomObject *self;
self = (CustomObject *) type->tp_alloc(type, 0);
if (self != NULL) {
self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->first == NULL) {
Py_DECREF(self);
return NULL;
}
self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->last == NULL) {
Py_DECREF(self);
return NULL;
}
self->number = 0;
}
return (PyObject *) self;
}
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
CustomObject *self = (CustomObject *) op;
static char *kwlist[] = {"first", "last", "number", NULL};
PyObject *first = NULL, *last = NULL;
if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 35

### 第40页

(continuedfrompreviouspage)
&first, &last,
&self->number))
return -1;
if (first) {
Py_SETREF(self->first, Py_NewRef(first));
}
if (last) {
Py_SETREF(self->last, Py_NewRef(last));
}
return 0;
}
static PyMemberDef Custom_members[] = {
{"number", Py_T_INT, offsetof(CustomObject, number), 0,
"custom number"},
{NULL} /* Sentinel */
};
static PyObject *
Custom_getfirst(PyObject *op, void *closure)
{
CustomObject *self = (CustomObject *) op;
return Py_NewRef(self->first);
}
static int
Custom_setfirst(PyObject *op, PyObject *value, void *closure)
{
CustomObject *self = (CustomObject *) op;
if (value == NULL) {
PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
return -1;
}
if (!PyUnicode_Check(value)) {
PyErr_SetString(PyExc_TypeError,
"The first attribute value must be a string");
return -1;
}
Py_SETREF(self->first, Py_NewRef(value));
return 0;
}
static PyObject *
Custom_getlast(PyObject *op, void *closure)
{
CustomObject *self = (CustomObject *) op;
return Py_NewRef(self->last);
}
static int
Custom_setlast(PyObject *op, PyObject *value, void *closure)
{
CustomObject *self = (CustomObject *) op;
if (value == NULL) {
PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
(continuesonnextpage)
36 Chapter2. Creatingextensionswithoutthirdpartytools

### 第41页

(continuedfrompreviouspage)
return -1;
}
if (!PyUnicode_Check(value)) {
PyErr_SetString(PyExc_TypeError,
"The last attribute value must be a string");
return -1;
}
Py_SETREF(self->last, Py_NewRef(value));
return 0;
}
static PyGetSetDef Custom_getsetters[] = {
{"first", Custom_getfirst, Custom_setfirst,
"first name", NULL},
{"last", Custom_getlast, Custom_setlast,
"last name", NULL},
{NULL} /* Sentinel */
};
static PyObject *
Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
{
CustomObject *self = (CustomObject *) op;
return PyUnicode_FromFormat("%S %S", self->first, self->last);
}
static PyMethodDef Custom_methods[] = {
{"name", Custom_name, METH_NOARGS,
"Return the name, combining the first and last name"
},
{NULL} /* Sentinel */
};
static PyTypeObject CustomType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "custom3.Custom",
.tp_doc = PyDoc_STR("Custom objects"),
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
.tp_new = Custom_new,
.tp_init = Custom_init,
.tp_dealloc = Custom_dealloc,
.tp_members = Custom_members,
.tp_methods = Custom_methods,
.tp_getset = Custom_getsetters,
};
static int
custom_module_exec(PyObject *m)
{
if (PyType_Ready(&CustomType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 37

### 第42页

(continuedfrompreviouspage)
return -1;
}
return 0;
}
static PyModuleDef_Slot custom_module_slots[] = {
{Py_mod_exec, custom_module_exec},
{Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
{0, NULL}
};
static PyModuleDef custom_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "custom3",
.m_doc = "Example module that creates an extension type.",
.m_size = 0,
.m_slots = custom_module_slots,
};
PyMODINIT_FUNC
PyInit_custom3(void)
{
return PyModuleDef_Init(&custom_module);
}
Toprovidegreatercontrol,overthefirstandlastattributes,we’llusecustomgetterandsetterfunctions. Here
arethefunctionsforgettingandsettingthefirstattribute:
static PyObject *
Custom_getfirst(PyObject *op, void *closure)
{
CustomObject *self = (CustomObject *) op;
Py_INCREF(self->first);
return self->first;
}
static int
Custom_setfirst(PyObject *op, PyObject *value, void *closure)
{
CustomObject *self = (CustomObject *) op;
PyObject *tmp;
if (value == NULL) {
PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
return -1;
}
if (!PyUnicode_Check(value)) {
PyErr_SetString(PyExc_TypeError,
"The first attribute value must be a string");
return -1;
}
tmp = self->first;
Py_INCREF(value);
self->first = value;
Py_DECREF(tmp);
return 0;
}
38 Chapter2. Creatingextensionswithoutthirdpartytools

### 第43页

ThegetterfunctionispassedaCustomobjectanda“closure”, whichisavoidpointer. Inthiscase, theclosureis
ignored. (The closure supports an advanced usage in which definition data is passed to the getter and setter. This
could,forexample,beusedtoallowasinglesetofgetterandsetterfunctionsthatdecidetheattributetogetorset
basedondataintheclosure.)
The setter function is passed the Custom object, the new value, and the closure. The new value may be NULL, in
whichcasetheattributeisbeingdeleted. Inoursetter,weraiseanerroriftheattributeisdeletedorifitsnewvalue
isnotastring.
WecreateanarrayofPyGetSetDefstructures:
static PyGetSetDef Custom_getsetters[] = {
{"first", Custom_getfirst, Custom_setfirst,
"first name", NULL},
{"last", Custom_getlast, Custom_setlast,
"last name", NULL},
{NULL} /* Sentinel */
};
andregisteritinthetp_getsetslot:
.tp_getset = Custom_getsetters,
ThelastiteminaPyGetSetDefstructureisthe“closure”mentionedabove. Inthiscase,wearen’tusingaclosure,
sowejustpassNULL.
Wealsoremovethememberdefinitionsfortheseattributes:
static PyMemberDef Custom_members[] = {
{"number", Py_T_INT, offsetof(CustomObject, number), 0,
"custom number"},
{NULL} /* Sentinel */
};
Wealsoneedtoupdatethetp_inithandlertoonlyallowstrings3tobepassed:
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
CustomObject *self = (CustomObject *) op;
static char *kwlist[] = {"first", "last", "number", NULL};
PyObject *first = NULL, *last = NULL, *tmp;
if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
&first, &last,
&self->number))
return -1;
if (first) {
tmp = self->first;
Py_INCREF(first);
self->first = first;
Py_DECREF(tmp);
}
if (last) {
tmp = self->last;
Py_INCREF(last);
(continuesonnextpage)
3Wenowknowthatthefirstandlastmembersarestrings,soperhapswecouldbelesscarefulaboutdecrementingtheirreferencecounts,
however,weacceptinstancesofstringsubclasses. Eventhoughdeallocatingnormalstringswon’tcallbackintoourobjects,wecan’tguarantee
thatdeallocatinganinstanceofastringsubclasswon’tcallbackintoourobjects.
2.2. DefiningExtensionTypes: Tutorial 39

### 第44页

(continuedfrompreviouspage)
self->last = last;
Py_DECREF(tmp);
}
return 0;
}
Withthesechanges,wecanassurethatthefirstandlastmembersareneverNULLsowecanremovechecksfor
NULLvaluesinalmostallcases. ThismeansthatmostofthePy_XDECREF()callscanbeconvertedtoPy_DECREF()
calls. Theonlyplacewecan’tchangethesecallsisinthetp_deallocimplementation,wherethereisthepossibility
thattheinitializationofthesemembersfailedintp_new.
Wealsorenamethemoduleinitializationfunctionandmodulenameintheinitializationfunction,aswedidbefore,
andweaddanextradefinitiontothesetup.pyfile.
2.2.4 Supporting cyclic garbage collection
Pythonhasacyclicgarbagecollector(GC)thatcanidentifyunneededobjectsevenwhentheirreferencecountsare
notzero. Thiscanhappenwhenobjectsareinvolvedincycles. Forexample,consider:
>>> l = []
>>> l.append(l)
>>> del l
Inthisexample,wecreatealistthatcontainsitself. Whenwedeleteit,itstillhasareferencefromitself. Itsreference
count doesn’t drop to zero. Fortunately, Python’s cyclic garbage collector will eventually figure out that the list is
garbageandfreeit.
In the second version of the Custom example, we allowed any kind of object to be stored in the first or last
attributes4. Besides, in the second and third versions, we allowed subclassing Custom, and subclasses may add
arbitraryattributes. Foranyofthosetworeasons,Customobjectscanparticipateincycles:
>>> import custom3
>>> class Derived(custom3.Custom): pass
...
>>> n = Derived()
>>> n.some_attribute = n
ToallowaCustominstanceparticipatinginareferencecycletobeproperlydetectedandcollectedbythecyclicGC,
ourCustomtypeneedstofilltwoadditionalslotsandtoenableaflagthatenablestheseslots:
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stddef.h> /* for offsetof() */
typedef struct {
PyObject_HEAD
PyObject *first; /* first name */
PyObject *last; /* last name */
int number;
} CustomObject;
static int
Custom_traverse(PyObject *op, visitproc visit, void *arg)
{
CustomObject *self = (CustomObject *) op;
(continuesonnextpage)
4Also,evenwithourattributesrestrictedtostringsinstances,theusercouldpassarbitrarystrsubclassesandthereforestillcreatereference
cycles.
40 Chapter2. Creatingextensionswithoutthirdpartytools

### 第45页

(continuedfrompreviouspage)
Py_VISIT(self->first);
Py_VISIT(self->last);
return 0;
}
static int
Custom_clear(PyObject *op)
{
CustomObject *self = (CustomObject *) op;
Py_CLEAR(self->first);
Py_CLEAR(self->last);
return 0;
}
static void
Custom_dealloc(PyObject *op)
{
PyObject_GC_UnTrack(op);
(void)Custom_clear(op);
Py_TYPE(op)->tp_free(op);
}
static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
CustomObject *self;
self = (CustomObject *) type->tp_alloc(type, 0);
if (self != NULL) {
self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->first == NULL) {
Py_DECREF(self);
return NULL;
}
self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
if (self->last == NULL) {
Py_DECREF(self);
return NULL;
}
self->number = 0;
}
return (PyObject *) self;
}
static int
Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
{
CustomObject *self = (CustomObject *) op;
static char *kwlist[] = {"first", "last", "number", NULL};
PyObject *first = NULL, *last = NULL;
if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
&first, &last,
&self->number))
return -1;
if (first) {
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 41

### 第46页

(continuedfrompreviouspage)
Py_SETREF(self->first, Py_NewRef(first));
}
if (last) {
Py_SETREF(self->last, Py_NewRef(last));
}
return 0;
}
static PyMemberDef Custom_members[] = {
{"number", Py_T_INT, offsetof(CustomObject, number), 0,
"custom number"},
{NULL} /* Sentinel */
};
static PyObject *
Custom_getfirst(PyObject *op, void *closure)
{
CustomObject *self = (CustomObject *) op;
return Py_NewRef(self->first);
}
static int
Custom_setfirst(PyObject *op, PyObject *value, void *closure)
{
CustomObject *self = (CustomObject *) op;
if (value == NULL) {
PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
return -1;
}
if (!PyUnicode_Check(value)) {
PyErr_SetString(PyExc_TypeError,
"The first attribute value must be a string");
return -1;
}
Py_XSETREF(self->first, Py_NewRef(value));
return 0;
}
static PyObject *
Custom_getlast(PyObject *op, void *closure)
{
CustomObject *self = (CustomObject *) op;
return Py_NewRef(self->last);
}
static int
Custom_setlast(PyObject *op, PyObject *value, void *closure)
{
CustomObject *self = (CustomObject *) op;
if (value == NULL) {
PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
return -1;
}
if (!PyUnicode_Check(value)) {
PyErr_SetString(PyExc_TypeError,
"The last attribute value must be a string");
(continuesonnextpage)
42 Chapter2. Creatingextensionswithoutthirdpartytools

### 第47页

(continuedfrompreviouspage)
return -1;
}
Py_XSETREF(self->last, Py_NewRef(value));
return 0;
}
static PyGetSetDef Custom_getsetters[] = {
{"first", Custom_getfirst, Custom_setfirst,
"first name", NULL},
{"last", Custom_getlast, Custom_setlast,
"last name", NULL},
{NULL} /* Sentinel */
};
static PyObject *
Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
{
CustomObject *self = (CustomObject *) op;
return PyUnicode_FromFormat("%S %S", self->first, self->last);
}
static PyMethodDef Custom_methods[] = {
{"name", Custom_name, METH_NOARGS,
"Return the name, combining the first and last name"
},
{NULL} /* Sentinel */
};
static PyTypeObject CustomType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "custom4.Custom",
.tp_doc = PyDoc_STR("Custom objects"),
.tp_basicsize = sizeof(CustomObject),
.tp_itemsize = 0,
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
.tp_new = Custom_new,
.tp_init = Custom_init,
.tp_dealloc = Custom_dealloc,
.tp_traverse = Custom_traverse,
.tp_clear = Custom_clear,
.tp_members = Custom_members,
.tp_methods = Custom_methods,
.tp_getset = Custom_getsetters,
};
static int
custom_module_exec(PyObject *m)
{
if (PyType_Ready(&CustomType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
return -1;
}
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 43

### 第48页

(continuedfrompreviouspage)
return 0;
}
static PyModuleDef_Slot custom_module_slots[] = {
{Py_mod_exec, custom_module_exec},
{Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
{0, NULL}
};
static PyModuleDef custom_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "custom4",
.m_doc = "Example module that creates an extension type.",
.m_size = 0,
.m_slots = custom_module_slots,
};
PyMODINIT_FUNC
PyInit_custom4(void)
{
return PyModuleDef_Init(&custom_module);
}
First,thetraversalmethodletsthecyclicGCknowaboutsubobjectsthatcouldparticipateincycles:
static int
Custom_traverse(PyObject *op, visitproc visit, void *arg)
{
CustomObject *self = (CustomObject *) op;
int vret;
if (self->first) {
vret = visit(self->first, arg);
if (vret != 0)
return vret;
}
if (self->last) {
vret = visit(self->last, arg);
if (vret != 0)
return vret;
}
return 0;
}
For each subobject that can participate in cycles, we need to call the visit() function, which is passed to the
traversalmethod. Thevisit()functiontakesasargumentsthesubobjectandtheextraargumentargpassedtothe
traversalmethod. Itreturnsanintegervaluethatmustbereturnedifitisnon-zero.
PythonprovidesaPy_VISIT()macrothatautomatescallingvisitfunctions. WithPy_VISIT(),wecanminimize
theamountofboilerplateinCustom_traverse:
static int
Custom_traverse(PyObject *op, visitproc visit, void *arg)
{
CustomObject *self = (CustomObject *) op;
Py_VISIT(self->first);
Py_VISIT(self->last);
return 0;
(continuesonnextpage)
44 Chapter2. Creatingextensionswithoutthirdpartytools

### 第49页

(continuedfrompreviouspage)
}
(cid:174) Note
Thetp_traverseimplementationmustnameitsargumentsexactlyvisitandarginordertousePy_VISIT().
Second,weneedtoprovideamethodforclearinganysubobjectsthatcanparticipateincycles:
static int
Custom_clear(PyObject *op)
{
CustomObject *self = (CustomObject *) op;
Py_CLEAR(self->first);
Py_CLEAR(self->last);
return 0;
}
NoticetheuseofthePy_CLEAR()macro. Itistherecommendedandsafewaytocleardataattributesofarbitrary
typeswhiledecrementingtheirreferencecounts. IfyouweretocallPy_XDECREF()insteadontheattributebefore
settingittoNULL,thereisapossibilitythattheattribute’sdestructorwouldcallbackintocodethatreadstheattribute
again(especiallyifthereisareferencecycle).
(cid:174) Note
YoucouldemulatePy_CLEAR()bywriting:
PyObject *tmp;
tmp = self->first;
self->first = NULL;
Py_XDECREF(tmp);
Nevertheless,itismucheasierandlesserror-pronetoalwaysusePy_CLEAR()whendeletinganattribute. Don’t
trytomicro-optimizeattheexpenseofrobustness!
ThedeallocatorCustom_deallocmaycallarbitrarycodewhenclearingattributes. ItmeansthecircularGCcanbe
triggeredinsidethefunction. SincetheGCassumesreferencecountisnotzero,weneedtountracktheobjectfrom
the GC by calling PyObject_GC_UnTrack() before clearing members. Here is our reimplemented deallocator
usingPyObject_GC_UnTrack()andCustom_clear:
static void
Custom_dealloc(PyObject *op)
{
PyObject_GC_UnTrack(op);
(void)Custom_clear(op);
Py_TYPE(op)->tp_free(op);
}
Finally,weaddthePy_TPFLAGS_HAVE_GCflagtotheclassflags:
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
That’s pretty much it. If we had written custom tp_alloc or tp_free handlers, we’d need to modify them for
cyclicgarbagecollection. Mostextensionswillusetheversionsautomaticallyprovided.
2.2. DefiningExtensionTypes: Tutorial 45

### 第50页

2.2.5 Subclassing other types
Itispossibletocreatenewextensiontypesthatarederivedfromexistingtypes. Itiseasiesttoinheritfromthebuiltin
types,sinceanextensioncaneasilyusethePyTypeObjectitneeds. ItcanbedifficulttosharethesePyTypeObject
structuresbetweenextensionmodules.
In this example we will create a SubList type that inherits from the built-in list type. The new type will be
completelycompatiblewithregularlists,butwillhaveanadditionalincrement()methodthatincreasesaninternal
counter:
>>> import sublist
>>> s = sublist.SubList(range(3))
>>> s.extend(s)
>>> print(len(s))
6
>>> print(s.increment())
1
>>> print(s.increment())
2
#define PY_SSIZE_T_CLEAN
#include <Python.h>
typedef struct {
PyListObject list;
int state;
} SubListObject;
static PyObject *
SubList_increment(PyObject *op, PyObject *Py_UNUSED(dummy))
{
SubListObject *self = (SubListObject *) op;
self->state++;
return PyLong_FromLong(self->state);
}
static PyMethodDef SubList_methods[] = {
{"increment", SubList_increment, METH_NOARGS,
PyDoc_STR("increment state counter")},
{NULL},
};
static int
SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
{
SubListObject *self = (SubListObject *) op;
if (PyList_Type.tp_init(op, args, kwds) < 0)
return -1;
self->state = 0;
return 0;
}
static PyTypeObject SubListType = {
.ob_base = PyVarObject_HEAD_INIT(NULL, 0)
.tp_name = "sublist.SubList",
.tp_doc = PyDoc_STR("SubList objects"),
.tp_basicsize = sizeof(SubListObject),
.tp_itemsize = 0,
(continuesonnextpage)
46 Chapter2. Creatingextensionswithoutthirdpartytools

### 第51页

(continuedfrompreviouspage)
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
.tp_init = SubList_init,
.tp_methods = SubList_methods,
};
static int
sublist_module_exec(PyObject *m)
{
SubListType.tp_base = &PyList_Type;
if (PyType_Ready(&SubListType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
return -1;
}
return 0;
}
static PyModuleDef_Slot sublist_module_slots[] = {
{Py_mod_exec, sublist_module_exec},
{Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
{0, NULL}
};
static PyModuleDef sublist_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "sublist",
.m_doc = "Example module that creates an extension type.",
.m_size = 0,
.m_slots = sublist_module_slots,
};
PyMODINIT_FUNC
PyInit_sublist(void)
{
return PyModuleDef_Init(&sublist_module);
}
Asyoucansee,thesourcecodecloselyresemblestheCustomexamplesinprevioussections. Wewillbreakdown
themaindifferencesbetweenthem.
typedef struct {
PyListObject list;
int state;
} SubListObject;
Theprimarydifferenceforderivedtypeobjectsisthatthebasetype’sobjectstructuremustbethefirstvalue. The
basetypewillalreadyincludethePyObject_HEAD()atthebeginningofitsstructure.
WhenaPythonobjectisaSubListinstance,itsPyObject *pointercanbesafelycasttobothPyListObject
*andSubListObject *:
static int
SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
{
(continuesonnextpage)
2.2. DefiningExtensionTypes: Tutorial 47

### 第52页

(continuedfrompreviouspage)
SubListObject *self = (SubListObject *) op;
if (PyList_Type.tp_init(op, args, kwds) < 0)
return -1;
self->state = 0;
return 0;
}
Weseeabovehowtocallthroughtothe__init__()methodofthebasetype.
Thispatternisimportantwhenwritingatypewithcustomtp_newandtp_deallocmembers. Thetp_newhandler
shouldnotactuallycreatethememoryfortheobjectwithitstp_alloc,butletthebaseclasshandleitbycallingits
owntp_new.
ThePyTypeObjectstructsupportsatp_basespecifyingthetype’sconcretebaseclass. Duetocross-platformcom-
pilerissues,youcan’tfillthatfielddirectlywithareferencetoPyList_Type;itshouldbedoneinthePy_mod_exec
function:
static int
sublist_module_exec(PyObject *m)
{
SubListType.tp_base = &PyList_Type;
if (PyType_Ready(&SubListType) < 0) {
return -1;
}
if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
return -1;
}
return 0;
}
BeforecallingPyType_Ready(),thetypestructuremusthavethetp_baseslotfilledin. Whenwearederivingan
existingtype,itisnotnecessarytofilloutthetp_allocslotwithPyType_GenericNew()–theallocationfunction
fromthebasetypewillbeinherited.
Afterthat,callingPyType_Ready()andaddingthetypeobjecttothemoduleisthesameaswiththebasicCustom
examples.
2.3 Defining Extension Types: Assorted Topics
Thissectionaimstogiveaquickfly-byonthevarioustypemethodsyoucanimplementandwhattheydo.
HereisthedefinitionofPyTypeObject,withsomefieldsonlyusedindebugbuildsomitted:
typedef struct _typeobject {
PyObject_VAR_HEAD
const char *tp_name; /* For printing, in format "<module>.<name>" */
Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
/* Methods to implement standard operations */
destructor tp_dealloc;
Py_ssize_t tp_vectorcall_offset;
getattrfunc tp_getattr;
setattrfunc tp_setattr;
PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
or tp_reserved (Python 3) */
(continuesonnextpage)
48 Chapter2. Creatingextensionswithoutthirdpartytools

### 第53页

(continuedfrompreviouspage)
reprfunc tp_repr;
/* Method suites for standard classes */
PyNumberMethods *tp_as_number;
PySequenceMethods *tp_as_sequence;
PyMappingMethods *tp_as_mapping;
/* More standard operations (here for binary compatibility) */
hashfunc tp_hash;
ternaryfunc tp_call;
reprfunc tp_str;
getattrofunc tp_getattro;
setattrofunc tp_setattro;
/* Functions to access object as input/output buffer */
PyBufferProcs *tp_as_buffer;
/* Flags to define presence of optional/expanded features */
unsigned long tp_flags;
const char *tp_doc; /* Documentation string */
/* Assigned meaning in release 2.0 */
/* call function for all accessible objects */
traverseproc tp_traverse;
/* delete references to contained objects */
inquiry tp_clear;
/* Assigned meaning in release 2.1 */
/* rich comparisons */
richcmpfunc tp_richcompare;
/* weak reference enabler */
Py_ssize_t tp_weaklistoffset;
/* Iterators */
getiterfunc tp_iter;
iternextfunc tp_iternext;
/* Attribute descriptor and subclassing stuff */
PyMethodDef *tp_methods;
PyMemberDef *tp_members;
PyGetSetDef *tp_getset;
// Strong reference on a heap type, borrowed reference on a static type
PyTypeObject *tp_base;
PyObject *tp_dict;
descrgetfunc tp_descr_get;
descrsetfunc tp_descr_set;
Py_ssize_t tp_dictoffset;
initproc tp_init;
allocfunc tp_alloc;
newfunc tp_new;
freefunc tp_free; /* Low-level free-memory routine */
(continuesonnextpage)
2.3. DefiningExtensionTypes: AssortedTopics 49

### 第54页

(continuedfrompreviouspage)
inquiry tp_is_gc; /* For PyObject_IS_GC */
PyObject *tp_bases;
PyObject *tp_mro; /* method resolution order */
PyObject *tp_cache; /* no longer used */
void *tp_subclasses; /* for static builtin types this is an index */
PyObject *tp_weaklist; /* not used for static builtin types */
destructor tp_del;
/* Type attribute cache version tag. Added in version 2.6.
* If zero, the cache is invalid and must be initialized.
*/
unsigned int tp_version_tag;
destructor tp_finalize;
vectorcallfunc tp_vectorcall;
/* bitset of which type-watchers care about this type */
unsigned char tp_watched;
/* Number of tp_version_tag values used.
* Set to _Py_ATTR_CACHE_UNUSED if the attribute cache is
* disabled for this type (e.g. due to custom MRO entries).
* Otherwise, limited to MAX_VERSIONS_PER_CLASS (defined elsewhere).
*/
uint16_t tp_versions_used;
} PyTypeObject;
Nowthat’salot ofmethods. Don’tworrytoomuchthough–ifyouhaveatypeyouwanttodefine,thechancesare
verygoodthatyouwillonlyimplementahandfulofthese.
Asyouprobablyexpectbynow,we’regoingtogooverthisandgivemoreinformationaboutthevarioushandlers.
Wewon’tgointheordertheyaredefinedinthestructure,becausethereisalotofhistoricalbaggagethatimpacts
theorderingofthefields. It’softeneasiesttofindanexamplethatincludesthefieldsyouneedandthenchangethe
valuestosuityournewtype.
const char *tp_name; /* For printing */
Thenameofthetype–asmentionedinthepreviouschapter,thiswillappearinvariousplaces,almostentirelyfor
diagnosticpurposes. Trytochoosesomethingthatwillbehelpfulinsuchasituation!
Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
Thesefieldstelltheruntimehowmuchmemorytoallocatewhennewobjectsofthistypearecreated. Pythonhas
somebuilt-insupportforvariablelengthstructures(think: strings, tuples)whichiswherethetp_itemsizefield
comesin. Thiswillbedealtwithlater.
const char *tp_doc;
Hereyoucanputastring(oritsaddress)thatyouwantreturnedwhenthePythonscriptreferencesobj.__doc__
toretrievethedocstring.
Nowwecometothebasictypemethods–theonesmostextensiontypeswillimplement.
2.3.1 Finalization and De-allocation
50 Chapter2. Creatingextensionswithoutthirdpartytools

### 第55页

destructor tp_dealloc;
This function is called when the reference count of the instance of your type is reduced to zero and the Python
interpreterwantstoreclaimit. Ifyourtypehasmemorytofreeorotherclean-uptoperform, youcanputithere.
Theobjectitselfneedstobefreedhereaswell. Hereisanexampleofthisfunction:
static void
newdatatype_dealloc(PyObject *op)
{
newdatatypeobject *self = (newdatatypeobject *) op;
free(self->obj_UnderlyingDatatypePtr);
Py_TYPE(self)->tp_free(self);
}
Ifyourtypesupportsgarbagecollection,thedestructorshouldcallPyObject_GC_UnTrack()beforeclearingany
memberfields:
static void
newdatatype_dealloc(PyObject *op)
{
newdatatypeobject *self = (newdatatypeobject *) op;
PyObject_GC_UnTrack(op);
Py_CLEAR(self->other_obj);
...
Py_TYPE(self)->tp_free(self);
}
Oneimportantrequirementofthedeallocatorfunctionisthatitleavesanypendingexceptionsalone. Thisisimportant
sincedeallocatorsarefrequentlycalledastheinterpreterunwindsthePythonstack;whenthestackisunwounddueto
anexception(ratherthannormalreturns),nothingisdonetoprotectthedeallocatorsfromseeingthatanexceptionhas
alreadybeenset. AnyactionswhichadeallocatorperformswhichmaycauseadditionalPythoncodetobeexecuted
maydetectthatanexceptionhasbeenset. Thiscanleadtomisleadingerrorsfromtheinterpreter. Theproperway
toprotectagainstthisistosaveapendingexceptionbeforeperformingtheunsafeaction,andrestoringitwhendone.
ThiscanbedoneusingthePyErr_Fetch()andPyErr_Restore()functions:
static void
my_dealloc(PyObject *obj)
{
MyObject *self = (MyObject *) obj;
PyObject *cbresult;
if (self->my_callback != NULL) {
PyObject *err_type, *err_value, *err_traceback;
/* This saves the current exception state */
PyErr_Fetch(&err_type, &err_value, &err_traceback);
cbresult = PyObject_CallNoArgs(self->my_callback);
if (cbresult == NULL) {
PyErr_WriteUnraisable(self->my_callback);
}
else {
Py_DECREF(cbresult);
}
/* This restores the saved exception state */
PyErr_Restore(err_type, err_value, err_traceback);
(continuesonnextpage)
2.3. DefiningExtensionTypes: AssortedTopics 51

### 第56页

(continuedfrompreviouspage)
Py_DECREF(self->my_callback);
}
Py_TYPE(self)->tp_free(self);
}
(cid:174) Note
There are limitations to what you can safely do in a deallocator function. First, if your type supports garbage
collection (using tp_traverse and/or tp_clear), some of the object’s members can have been cleared or
finalized by the time tp_dealloc is called. Second, in tp_dealloc, your object is in an unstable state: its
referencecountisequaltozero. Anycalltoanon-trivialobjectorAPI(asintheexampleabove)mightendup
callingtp_deallocagain,causingadoublefreeandacrash.
StartingwithPython3.4,itisrecommendednottoputanycomplexfinalizationcodeintp_dealloc,andinstead
usethenewtp_finalizetypemethod.
(cid:181) Seealso
PEP442explainsthenewfinalizationscheme.
2.3.2 Object Presentation
InPython,therearetwowaystogenerateatextualrepresentationofanobject: therepr()function,andthestr()
function. (Theprint()functionjustcallsstr().) Thesehandlersarebothoptional.
reprfunc tp_repr;
reprfunc tp_str;
Thetp_reprhandlershouldreturnastringobjectcontainingarepresentationoftheinstanceforwhichitiscalled.
Hereisasimpleexample:
static PyObject *
newdatatype_repr(PyObject *op)
{
newdatatypeobject *self = (newdatatypeobject *) op;
return PyUnicode_FromFormat("Repr-ified_newdatatype{{size:%d}}",
self->obj_UnderlyingDatatypePtr->size);
}
Ifnotp_reprhandlerisspecified,theinterpreterwillsupplyarepresentationthatusesthetype’stp_nameanda
uniquelyidentifyingvaluefortheobject.
Thetp_strhandleristostr()whatthetp_reprhandlerdescribedaboveistorepr();thatis,itiscalledwhen
Pythoncodecallsstr()onaninstanceofyourobject. Itsimplementationisverysimilartothetp_reprfunction,
buttheresultingstringisintendedforhumanconsumption. Iftp_strisnotspecified,thetp_reprhandlerisused
instead.
Hereisasimpleexample:
static PyObject *
newdatatype_str(PyObject *op)
{
newdatatypeobject *self = (newdatatypeobject *) op;
return PyUnicode_FromFormat("Stringified_newdatatype{{size:%d}}",
(continuesonnextpage)
52 Chapter2. Creatingextensionswithoutthirdpartytools

| (cid:181) Seealso |
| --- |
| PEP442explainsthenewfinalizationscheme. |

### 第57页

(continuedfrompreviouspage)
self->obj_UnderlyingDatatypePtr->size);
}
2.3.3 Attribute Management
Foreveryobjectwhichcansupportattributes,thecorrespondingtypemustprovidethefunctionsthatcontrolhowthe
attributesareresolved. Thereneedstobeafunctionwhichcanretrieveattributes(ifanyaredefined),andanotherto
setattributes(ifsettingattributesisallowed). Removinganattributeisaspecialcase,forwhichthenewvaluepassed
tothehandlerisNULL.
Pythonsupportstwopairsofattributehandlers;atypethatsupportsattributesonlyneedstoimplementthefunctions
foronepair. Thedifferenceisthatonepairtakesthenameoftheattributeas a char*, whiletheotheracceptsa
PyObject*. Eachtypecanusewhicheverpairmakesmoresensefortheimplementation’sconvenience.
getattrfunc tp_getattr; /* char * version */
setattrfunc tp_setattr;
/* ... */
getattrofunc tp_getattro; /* PyObject * version */
setattrofunc tp_setattro;
If accessing attributes of an object is always a simple operation (this will be explained shortly), there are generic
implementationswhichcanbeusedtoprovidethePyObject*versionoftheattributemanagementfunctions. The
actualneedfortype-specificattributehandlersalmostcompletelydisappearedstartingwithPython2.2,thoughthere
aremanyexampleswhichhavenotbeenupdatedtousesomeofthenewgenericmechanismthatisavailable.
GenericAttributeManagement
Mostextensiontypesonlyusesimpleattributes. So,whatmakestheattributessimple? Thereareonlyacoupleof
conditionsthatmustbemet:
1. ThenameoftheattributesmustbeknownwhenPyType_Ready()iscalled.
2. Nospecialprocessingisneededtorecordthatanattributewaslookeduporset,nordoactionsneedtobetaken
basedonthevalue.
Notethatthislistdoesnotplaceanyrestrictionsonthevaluesoftheattributes, whenthevaluesarecomputed, or
howrelevantdataisstored.
WhenPyType_Ready()iscalled,itusesthreetablesreferencedbythetypeobjecttocreatedescriptorswhichare
placedinthedictionaryofthetypeobject. Eachdescriptorcontrolsaccesstooneattributeoftheinstanceobject.
Eachofthetablesisoptional;ifallthreeareNULL,instancesofthetypewillonlyhaveattributesthatareinherited
fromtheirbasetype,andshouldleavethetp_getattroandtp_setattrofieldsNULLaswell,allowingthebase
typetohandleattributes.
Thetablesaredeclaredasthreefieldsofthetypeobject:
struct PyMethodDef *tp_methods;
struct PyMemberDef *tp_members;
struct PyGetSetDef *tp_getset;
If tp_methods is not NULL, it must refer to an array of PyMethodDef structures. Each entry in the table is an
instanceofthisstructure:
typedef struct PyMethodDef {
const char *ml_name; /* method name */
PyCFunction ml_meth; /* implementation function */
int ml_flags; /* flags */
const char *ml_doc; /* docstring */
} PyMethodDef;
2.3. DefiningExtensionTypes: AssortedTopics 53

### 第58页

Oneentryshouldbedefinedforeachmethodprovidedbythetype;noentriesareneededformethodsinheritedfrom
abasetype. Oneadditionalentryisneededattheend;itisasentinelthatmarkstheendofthearray. Theml_name
fieldofthesentinelmustbeNULL.
Thesecondtableisusedtodefineattributeswhichmapdirectlytodatastoredintheinstance. Avarietyofprimitive
Ctypesaresupported,andaccessmayberead-onlyorread-write. Thestructuresinthetablearedefinedas:
typedef struct PyMemberDef {
const char *name;
int type;
int offset;
int flags;
const char *doc;
} PyMemberDef;
Foreachentryinthetable,adescriptorwillbeconstructedandaddedtothetypewhichwillbeabletoextractavalue
fromtheinstancestructure. ThetypefieldshouldcontainatypecodelikePy_T_INTorPy_T_DOUBLE;thevalue
willbeusedtodeterminehowtoconvertPythonvaluestoandfromCvalues. Theflagsfieldisusedtostoreflags
whichcontrolhowtheattributecanbeaccessed: youcansetittoPy_READONLYtopreventPythoncodefromsetting
it.
An interesting advantage of using the tp_members table to build descriptors that are used at runtime is that any
attributedefinedthiswaycanhaveanassociateddocstringsimplybyprovidingthetextinthetable. Anapplication
canusetheintrospectionAPItoretrievethedescriptorfromtheclassobject,andgetthedocstringusingits__doc__
attribute.
Aswiththetp_methodstable,asentinelentrywithaml_namevalueofNULLisrequired.
Type-specificAttributeManagement
Forsimplicity, onlythechar*versionwillbedemonstratedhere; thetypeofthenameparameteristheonlydif-
ferencebetweenthechar*andPyObject*flavorsoftheinterface. Thisexampleeffectivelydoesthesamething
asthegenericexampleabove,butdoesnotusethegenericsupportaddedinPython2.2. Itexplainshowthehandler
functionsarecalled,sothatifyoudoneedtoextendtheirfunctionality,you’llunderstandwhatneedstobedone.
Thetp_getattrhandleriscalledwhentheobjectrequiresanattributelook-up. Itiscalledinthesamesituations
wherethe__getattr__()methodofaclasswouldbecalled.
Hereisanexample:
static PyObject *
newdatatype_getattr(PyObject *op, char *name)
{
newdatatypeobject *self = (newdatatypeobject *) op;
if (strcmp(name, "data") == 0) {
return PyLong_FromLong(self->data);
}
PyErr_Format(PyExc_AttributeError,
"'%.100s' object has no attribute '%.400s'",
Py_TYPE(self)->tp_name, name);
return NULL;
}
The tp_setattr handler is called when the __setattr__() or __delattr__() method of a class instance
would be called. When an attribute should be deleted, the third parameter will be NULL. Here is an example that
simplyraisesanexception;ifthiswerereallyallyouwanted,thetp_setattrhandlershouldbesettoNULL.
static int
newdatatype_setattr(PyObject *op, char *name, PyObject *v)
{
(continuesonnextpage)
54 Chapter2. Creatingextensionswithoutthirdpartytools

### 第59页

(continuedfrompreviouspage)
PyErr_Format(PyExc_RuntimeError, "Read-only attribute: %s", name);
return -1;
}
2.3.4 Object Comparison
richcmpfunc tp_richcompare;
The tp_richcompare handler is called when comparisons are needed. It is analogous to the rich comparison
methods,like__lt__(),andalsocalledbyPyObject_RichCompare()andPyObject_RichCompareBool().
ThisfunctioniscalledwithtwoPythonobjectsandtheoperatorasarguments,wheretheoperatorisoneofPy_EQ,
Py_NE,Py_LE,Py_GE,Py_LTorPy_GT.Itshouldcomparethetwoobjectswithrespecttothespecifiedoperatorand
returnPy_TrueorPy_Falseifthecomparisonissuccessful,Py_NotImplementedtoindicatethatcomparison
isnotimplementedandtheotherobject’scomparisonmethodshouldbetried,orNULLifanexceptionwasset.
Hereisasampleimplementation,foradatatypethatisconsideredequalifthesizeofaninternalpointerisequal:
static PyObject *
newdatatype_richcmp(PyObject *lhs, PyObject *rhs, int op)
{
newdatatypeobject *obj1 = (newdatatypeobject *) lhs;
newdatatypeobject *obj2 = (newdatatypeobject *) rhs;
PyObject *result;
int c, size1, size2;
/* code to make sure that both arguments are of type
newdatatype omitted */
size1 = obj1->obj_UnderlyingDatatypePtr->size;
size2 = obj2->obj_UnderlyingDatatypePtr->size;
switch (op) {
case Py_LT: c = size1 < size2; break;
case Py_LE: c = size1 <= size2; break;
case Py_EQ: c = size1 == size2; break;
case Py_NE: c = size1 != size2; break;
case Py_GT: c = size1 > size2; break;
case Py_GE: c = size1 >= size2; break;
}
result = c ? Py_True : Py_False;
return Py_NewRef(result);
}
2.3.5 Abstract Protocol Support
Python supports a variety of abstract ‘protocols;’ the specific interfaces provided to use these interfaces are docu-
mentedinabstract.
AnumberoftheseabstractinterfacesweredefinedearlyinthedevelopmentofthePythonimplementation. Inpar-
ticular,thenumber,mapping,andsequenceprotocolshavebeenpartofPythonsincethebeginning. Otherprotocols
havebeenaddedovertime. Forprotocolswhichdependonseveralhandlerroutinesfromthetypeimplementation,
theolderprotocolshavebeendefinedasoptionalblocksofhandlersreferencedbythetypeobject. Fornewerpro-
tocolsthereareadditionalslotsinthemaintypeobject,withaflagbitbeingsettoindicatethattheslotsarepresent
andshouldbecheckedbytheinterpreter. (Theflagbitdoesnotindicatethattheslotvaluesarenon-NULL.Theflag
maybesettoindicatethepresenceofaslot,butaslotmaystillbeunfilled.)
2.3. DefiningExtensionTypes: AssortedTopics 55

### 第60页

PyNumberMethods *tp_as_number;
PySequenceMethods *tp_as_sequence;
PyMappingMethods *tp_as_mapping;
Ifyouwishyourobjecttobeabletoactlikeanumber,asequence,oramappingobject,thenyouplacetheaddress
of a structure that implements the C type PyNumberMethods, PySequenceMethods, or PyMappingMethods,
respectively. Itisuptoyoutofillinthisstructurewithappropriatevalues. Youcanfindexamplesoftheuseofeach
oftheseintheObjectsdirectoryofthePythonsourcedistribution.
hashfunc tp_hash;
Thisfunction,ifyouchoosetoprovideit,shouldreturnahashnumberforaninstanceofyourdatatype. Hereisa
simpleexample:
static Py_hash_t
newdatatype_hash(PyObject *op)
{
newdatatypeobject *self = (newdatatypeobject *) op;
Py_hash_t result;
result = self->some_size + 32767 * self->some_number;
if (result == -1) {
result = -2;
}
return result;
}
Py_hash_tisasignedintegertypewithaplatform-varyingwidth. Returning-1fromtp_hashindicatesanerror,
whichiswhyyoushouldbecarefultoavoidreturningitwhenhashcomputationissuccessful,asseenabove.
ternaryfunc tp_call;
Thisfunctioniscalledwhenaninstanceofyourdatatypeis“called”,forexample,ifobj1isaninstanceofyourdata
typeandthePythonscriptcontainsobj1('hello'),thetp_callhandlerisinvoked.
Thisfunctiontakesthreearguments:
1. self istheinstanceofthedatatypewhichisthesubjectofthecall. Ifthecallisobj1('hello'),thenself is
obj1.
2. argsisatuplecontainingtheargumentstothecall. YoucanusePyArg_ParseTuple()toextracttheargu-
ments.
3. kwds is a dictionary of keyword arguments that were passed. If this is non-NULL and you support keyword
arguments,usePyArg_ParseTupleAndKeywords()toextractthearguments. Ifyoudonotwanttosupport
keywordargumentsandthisisnon-NULL,raiseaTypeErrorwithamessagesayingthatkeywordarguments
arenotsupported.
Hereisatoytp_callimplementation:
static PyObject *
newdatatype_call(PyObject *op, PyObject *args, PyObject *kwds)
{
newdatatypeobject *self = (newdatatypeobject *) op;
PyObject *result;
const char *arg1;
const char *arg2;
const char *arg3;
if (!PyArg_ParseTuple(args, "sss:call", &arg1, &arg2, &arg3)) {
return NULL;
(continuesonnextpage)
56 Chapter2. Creatingextensionswithoutthirdpartytools

### 第61页

(continuedfrompreviouspage)
}
result = PyUnicode_FromFormat(
"Returning -- value: [%d] arg1: [%s] arg2: [%s] arg3: [%s]\n",
self->obj_UnderlyingDatatypePtr->size,
arg1, arg2, arg3);
return result;
}
/* Iterators */
getiterfunc tp_iter;
iternextfunc tp_iternext;
Thesefunctionsprovidesupportfortheiteratorprotocol. Bothhandlerstakeexactlyoneparameter,theinstancefor
whichthey arebeing called, andreturn a new reference. In the case ofan error, they should setan exceptionand
returnNULL.tp_itercorrespondstothePython__iter__()method, whiletp_iternextcorrespondstothe
Python__next__()method.
Any iterable object must implement the tp_iter handler, which must return an iterator object. Here the same
guidelinesapplyasforPythonclasses:
• Forcollections(suchaslistsandtuples)whichcansupportmultipleindependentiterators,anewiteratorshould
becreatedandreturnedbyeachcalltotp_iter.
• Objectswhichcanonlybeiteratedoveronce(usuallyduetosideeffectsofiteration,suchasfileobjects)can
implement tp_iter by returning a new reference to themselves – and should also therefore implement the
tp_iternexthandler.
Any iterator object should implement both tp_iter and tp_iternext. An iterator’s tp_iter handler should
returnanewreferencetotheiterator. Itstp_iternexthandlershouldreturnanewreferencetothenextobjectin
theiteration, ifthereisone. Iftheiterationhasreachedtheend, tp_iternextmayreturnNULLwithoutsetting
anexception,oritmaysetStopIterationinadditiontoreturningNULL;avoidingtheexceptioncanyieldslightly
betterperformance. Ifanactualerroroccurs,tp_iternextshouldalwayssetanexceptionandreturnNULL.
2.3.6 Weak Reference Support
OneofthegoalsofPython’sweakreferenceimplementationistoallowanytypetoparticipateintheweakreference
mechanismwithoutincurringtheoverheadonperformance-criticalobjects(suchasnumbers).
(cid:181) Seealso
Documentationfortheweakrefmodule.
Foranobjecttobeweaklyreferenceable,theextensiontypemustsetthePy_TPFLAGS_MANAGED_WEAKREFbitof
thetp_flagsfield. Thelegacytp_weaklistoffsetfieldshouldbeleftaszero.
Concretely,hereishowthestaticallydeclaredtypeobjectwouldlook:
static PyTypeObject TrivialType = {
PyVarObject_HEAD_INIT(NULL, 0)
/* ... other members omitted for brevity ... */
.tp_flags = Py_TPFLAGS_MANAGED_WEAKREF | ...,
};
The only further addition is that tp_dealloc needs to clear any weak references (by calling
PyObject_ClearWeakRefs()):
static void
Trivial_dealloc(PyObject *op)
(continuesonnextpage)
2.3. DefiningExtensionTypes: AssortedTopics 57

### 第62页

(continuedfrompreviouspage)
{
/* Clear weakrefs first before calling any destructors */
PyObject_ClearWeakRefs(op);
/* ... remainder of destruction code omitted for brevity ... */
Py_TYPE(op)->tp_free(op);
}
2.3.7 More Suggestions
In order to learn how to implement any specific method for your new data type, get the CPython source code.
Go to the Objects directory, then search the C source files for tp_ plus the function you want (for example,
tp_richcompare). Youwillfindexamplesofthefunctionyouwanttoimplement.
When you need to verify that an object is a concrete instance of the type you are implementing, use the
PyObject_TypeCheck()function. Asampleofitsusemightbesomethinglikethefollowing:
if (!PyObject_TypeCheck(some_object, &MyType)) {
PyErr_SetString(PyExc_TypeError, "arg #1 not a mything");
return NULL;
}
(cid:181) Seealso
DownloadCPythonsourcereleases.
https://www.python.org/downloads/source/
TheCPythonprojectonGitHub,wheretheCPythonsourcecodeisdeveloped.
https://github.com/python/cpython
2.4 Building C and C++ Extensions
ACextensionforCPythonisasharedlibrary(forexample,a.sofileonLinux,.pydonWindows),whichexports
aninitializationfunction.
Seeextension-modulesfordetails.
2.4.1 Building C and C++ Extensions with setuptools
Building,packaginganddistributingextensionmodulesisbestdonewiththird-partytools,andisoutofscopeofthis
document. OnesuitabletoolisSetuptools,whosedocumentationcanbefoundathttps://setuptools.pypa.io/en/latest/
setuptools.html.
Thedistutilsmodule,whichwasincludedinthestandardlibraryuntilPython3.12,isnowmaintainedaspartof
Setuptools.
2.5 Building C and C++ Extensions on Windows
This chapter briefly explains how to create a Windows extension module for Python using Microsoft Visual C++,
andfollowswithmoredetailedbackgroundinformationonhowitworks. Theexplanatorymaterialisusefulforboth
the Windows programmer learning to build Python extensions and the Unix programmer interested in producing
softwarewhichcanbesuccessfullybuiltonbothUnixandWindows.
Module authors are encouraged to use the distutils approach for building extension modules, instead of the one
describedinthissection. YouwillstillneedtheCcompilerthatwasusedtobuildPython;typicallyMicrosoftVisual
C++.
58 Chapter2. Creatingextensionswithoutthirdpartytools

| (cid:181) Seealso |
| --- |
| DownloadCPythonsourcereleases.
https://www.python.org/downloads/source/
TheCPythonprojectonGitHub,wheretheCPythonsourcecodeisdeveloped.
https://github.com/python/cpython |

### 第63页

(cid:174) Note
ThischaptermentionsanumberoffilenamesthatincludeanencodedPythonversionnumber. Thesefilenames
are represented with the version number shown as XY; in practice, 'X' will be the major version number and
'Y'willbetheminorversionnumberofthePythonreleaseyou’reworkingwith. Forexample,ifyouareusing
Python2.2.1,XYwillactuallybe22.
2.5.1 A Cookbook Approach
TherearetwoapproachestobuildingextensionmodulesonWindows,justasthereareonUnix:usethesetuptools
packagetocontrolthebuildprocess,ordothingsmanually. Thesetuptoolsapproachworkswellformostextensions;
documentationonusingsetuptoolstobuildandpackageextensionmodulesisavailableinBuildingCandC++
Extensionswithsetuptools. Ifyoufindyoureallyneedtodothingsmanually,itmaybeinstructivetostudytheproject
fileforthewinsoundstandardlibrarymodule.
2.5.2 Differences Between Unix and Windows
UnixandWindowsusecompletelydifferentparadigmsforrun-timeloadingofcode. Beforeyoutrytobuildamodule
thatcanbedynamicallyloaded,beawareofhowyoursystemworks.
InUnix,asharedobject(.so)filecontainscodetobeusedbytheprogram,andalsothenamesoffunctionsanddata
thatitexpectstofindintheprogram. Whenthefileisjoinedtotheprogram,allreferencestothosefunctionsand
datainthefile’scodearechangedtopointtotheactuallocationsintheprogramwherethefunctionsanddataare
placedinmemory. Thisisbasicallyalinkoperation.
InWindows,adynamic-linklibrary(.dll)filehasnodanglingreferences. Instead,anaccesstofunctionsordata
goes through a lookup table. So the DLL code does not have to be fixed up at runtime to refer to the program’s
memory;instead,thecodealreadyusestheDLL’slookuptable,andthelookuptableismodifiedatruntimetopoint
tothefunctionsanddata.
InUnix,thereisonlyonetypeoflibraryfile(.a)whichcontainscodefromseveralobjectfiles(.o). Duringthelink
steptocreateasharedobjectfile(.so),thelinkermayfindthatitdoesn’tknowwhereanidentifierisdefined. The
linkerwilllookforitintheobjectfilesinthelibraries;ifitfindsit,itwillincludeallthecodefromthatobjectfile.
InWindows,therearetwotypesoflibrary,astaticlibraryandanimportlibrary(bothcalled.lib). Astaticlibrary
islikeaUnix.afile;itcontainscodetobeincludedasnecessary. Animportlibraryisbasicallyusedonlytoreassure
thelinkerthatacertainidentifierislegal,andwillbepresentintheprogramwhentheDLLisloaded. Sothelinker
usestheinformationfromtheimportlibrarytobuildthelookuptableforusingidentifiersthatarenotincludedinthe
DLL.WhenanapplicationoraDLLislinked,animportlibrarymaybegenerated,whichwillneedtobeusedfor
allfutureDLLsthatdependonthesymbolsintheapplicationorDLL.
Suppose you are building two dynamic-load modules, B and C, which should share another block of code A. On
Unix,youwouldnot passA.atothelinkerforB.soandC.so;thatwouldcauseittobeincludedtwice,sothatB
andCwouldeachhavetheirowncopy. InWindows,buildingA.dllwillalsobuildA.lib. YoudopassA.libto
thelinkerforBandC.A.libdoesnotcontaincode;itjustcontainsinformationwhichwillbeusedatruntimeto
accessA’scode.
In Windows, using an import library is sort of like using import spam; it gives you access to spam’s names, but
doesnotcreateaseparatecopy. OnUnix,linkingwithalibraryismorelikefrom spam import *;itdoescreate
aseparatecopy.
Py_NO_LINK_LIB
Turnofftheimplicit,#pragma-basedlinkagewiththePythonlibrary,performedinsideCPythonheaderfiles.
Addedinversion3.14.
2.5. BuildingCandC++ExtensionsonWindows 59

### 第64页

2.5.3 Using DLLs in Practice
Windows Python is built in Microsoft Visual C++; using other compilers may or may not work. The rest of this
sectionisMSVC++specific.
WhencreatingDLLsinWindows,youcanusetheCPythonlibraryintwoways:
1. Bydefault,inclusionofPC/pyconfig.hdirectlyorviaPython.htriggersanimplicit,configure-awarelink
with the library. The header file chooses pythonXY_d.lib for Debug, pythonXY.lib for Release, and
pythonX.libforReleasewiththeLimitedAPIenabled.
TobuildtwoDLLs,spamandni(whichusesCfunctionsfoundinspam),youcouldusethesecommands:
cl /LD /I/python/include spam.c
cl /LD /I/python/include ni.c spam.lib
Thefirstcommandcreatedthreefiles: spam.obj,spam.dllandspam.lib. Spam.dlldoesnotcontain
anyPythonfunctions(suchasPyArg_ParseTuple()),butitdoesknowhowtofindthePythoncodethanks
totheimplicitlylinkedpythonXY.lib.
Thesecondcommandcreatedni.dll(and.objand.lib),whichknowshowtofindthenecessaryfunctions
fromspam,andalsofromthePythonexecutable.
2. ManuallybydefiningPy_NO_LINK_LIBmacrobeforeincludingPython.h. YoumustpasspythonXY.lib
tothelinker.
TobuildtwoDLLs,spamandni(whichusesCfunctionsfoundinspam),youcouldusethesecommands:
cl /LD /DPy_NO_LINK_LIB /I/python/include spam.c ../libs/pythonXY.lib
cl /LD /DPy_NO_LINK_LIB /I/python/include ni.c spam.lib ../libs/pythonXY.lib
Thefirstcommandcreatedthreefiles: spam.obj,spam.dllandspam.lib. Spam.dlldoesnotcontain
anyPythonfunctions(suchasPyArg_ParseTuple()),butitdoesknowhowtofindthePythoncodethanks
topythonXY.lib.
Thesecondcommandcreatedni.dll(and.objand.lib),whichknowshowtofindthenecessaryfunctions
fromspam,andalsofromthePythonexecutable.
Not every identifier is exported to the lookup table. If you want any other modules (including Python) to be
able to see your identifiers, you have to say _declspec(dllexport), as in void _declspec(dllexport)
initspam(void)orPyObject _declspec(dllexport) *NiGetSpamData(void).
Developer Studio will throw in a lot of import libraries that you do not really need, adding about 100K to your
executable. Togetridofthem,usetheProjectSettingsdialog,Linktab,tospecifyignoredefaultlibraries. Addthe
correctmsvcrtxx.libtothelistoflibraries.
60 Chapter2. Creatingextensionswithoutthirdpartytools

### 第65页

CHAPTER
THREE
EMBEDDING THE CPYTHON RUNTIME IN A LARGER
APPLICATION
Sometimes, rather than creating an extension that runs inside the Python interpreter as the main application, it is
desirabletoinsteadembedtheCPythonruntimeinsidealargerapplication. Thissectioncoverssomeofthedetails
involvedindoingthatsuccessfully.
3.1 Embedding Python in Another Application
ThepreviouschaptersdiscussedhowtoextendPython,thatis,howtoextendthefunctionalityofPythonbyattaching
a library of C functions to it. It is also possible to do it the other way around: enrich your C/C++ application by
embeddingPythoninit. Embeddingprovidesyourapplicationwiththeabilitytoimplementsomeofthefunctionality
ofyourapplicationinPythonratherthanCorC++. Thiscanbeusedformanypurposes;oneexamplewouldbeto
allowuserstotailortheapplicationtotheirneedsbywritingsomescriptsinPython. Youcanalsouseityourselfif
someofthefunctionalitycanbewritteninPythonmoreeasily.
EmbeddingPythonissimilartoextendingit,butnotquite. ThedifferenceisthatwhenyouextendPython,themain
programoftheapplicationisstillthePythoninterpreter,whileifyouembedPython,themainprogrammayhave
nothingtodowithPython—instead,somepartsoftheapplicationoccasionallycallthePythoninterpretertorun
somePythoncode.
SoifyouareembeddingPython,youareprovidingyourownmainprogram. Oneofthethingsthismainprogram
has to do is initialize the Python interpreter. At the very least, you have to call the function Py_Initialize().
ThereareoptionalcallstopasscommandlineargumentstoPython. Thenlateryoucancalltheinterpreterfromany
partoftheapplication.
There are several different ways to call the interpreter: you can pass a string containing Python statements to
PyRun_SimpleString(),oryoucanpassastdiofilepointerandafilename(foridentificationinerrormessages
only)toPyRun_SimpleFile(). Youcanalsocallthelower-leveloperationsdescribedinthepreviouschaptersto
constructandusePythonobjects.
(cid:181) Seealso
c-api-index
ThedetailsofPython’sCinterfacearegiveninthismanual. Agreatdealofnecessaryinformationcanbe
foundhere.
3.1.1 Very High Level Embedding
The simplest form of embedding Python is the use of the very high level interface. This interface is intended to
executeaPythonscriptwithoutneedingtointeractwiththeapplicationdirectly. Thiscanforexamplebe usedto
performsomeoperationonafile.
#define PY_SSIZE_T_CLEAN
#include <Python.h>
(continuesonnextpage)
61

| (cid:181) Seealso |
| --- |
| c-api-index
ThedetailsofPython’sCinterfacearegiveninthismanual. Agreatdealofnecessaryinformationcanbe
foundhere. |

### 第66页

(continuedfrompreviouspage)
int
main(int argc, char *argv[])
{
PyStatus status;
PyConfig config;
PyConfig_InitPythonConfig(&config);
/* optional but recommended */
status = PyConfig_SetBytesString(&config, &config.program_name, argv[0]);
if (PyStatus_Exception(status)) {
goto exception;
}
status = Py_InitializeFromConfig(&config);
if (PyStatus_Exception(status)) {
goto exception;
}
PyConfig_Clear(&config);
PyRun_SimpleString("from time import time,ctime\n"
"print('Today is', ctime(time()))\n");
if (Py_FinalizeEx() < 0) {
exit(120);
}
return 0;
exception:
PyConfig_Clear(&config);
Py_ExitStatusException(status);
}
(cid:174) Note
#define PY_SSIZE_T_CLEAN was used to indicatethat Py_ssize_t shouldbe used insomeAPIs instead
ofint. ItisnotnecessarysincePython3.13,butwekeepithereforbackwardcompatibility. Seearg-parsing-
string-and-buffersforadescriptionofthismacro.
SettingPyConfig.program_nameshouldbecalledbeforePy_InitializeFromConfig()toinformtheinter-
preteraboutpathstoPythonrun-timelibraries. Next,thePythoninterpreterisinitializedwithPy_Initialize(),
followed by the execution of a hard-coded Python script that prints the date and time. Afterwards, the
Py_FinalizeEx() call shuts the interpreter down, followed by the end of the program. In a real program, you
maywanttogetthePythonscriptfromanothersource,perhapsatext-editorroutine,afile,oradatabase. Getting
thePythoncodefromafilecanbetterbedonebyusingthePyRun_SimpleFile()function,whichsavesyouthe
troubleofallocatingmemoryspaceandloadingthefilecontents.
3.1.2 Beyond Very High Level Embedding: An overview
ThehighlevelinterfacegivesyoutheabilitytoexecutearbitrarypiecesofPythoncodefromyourapplication,but
exchangingdatavaluesisquitecumbersometosaytheleast. Ifyouwantthat,youshoulduselowerlevelcalls. At
thecostofhavingtowritemoreCcode,youcanachievealmostanything.
ItshouldbenotedthatextendingPythonandembeddingPythonisquitethesameactivity,despitethedifferentintent.
Mosttopicsdiscussedinthepreviouschaptersarestillvalid. Toshowthis,considerwhattheextensioncodefrom
PythontoCreallydoes:
1. ConvertdatavaluesfromPythontoC,
62 Chapter3. EmbeddingtheCPythonruntimeinalargerapplication

### 第67页

2. PerformafunctioncalltoaCroutineusingtheconvertedvalues,and
3. ConvertthedatavaluesfromthecallfromCtoPython.
WhenembeddingPython,theinterfacecodedoes:
1. ConvertdatavaluesfromCtoPython,
2. PerformafunctioncalltoaPythoninterfaceroutineusingtheconvertedvalues,and
3. ConvertthedatavaluesfromthecallfromPythontoC.
Asyoucansee,thedataconversionstepsaresimplyswappedtoaccommodatethedifferentdirectionofthecross-
languagetransfer. Theonlydifferenceistheroutinethatyoucallbetweenbothdataconversions. Whenextending,
youcallaCroutine,whenembedding,youcallaPythonroutine.
ThischapterwillnotdiscusshowtoconvertdatafromPythontoCandviceversa. Also,properuseofreferences
anddealingwitherrorsisassumedtobeunderstood. Sincetheseaspectsdonotdifferfromextendingtheinterpreter,
youcanrefertoearlierchaptersfortherequiredinformation.
3.1.3 Pure Embedding
ThefirstprogramaimstoexecuteafunctioninaPythonscript. Likeinthesectionabouttheveryhighlevelinterface,
thePythoninterpreterdoesnotdirectlyinteractwiththeapplication(butthatwillchangeinthenextsection).
ThecodetorunafunctiondefinedinaPythonscriptis:
#define PY_SSIZE_T_CLEAN
#include <Python.h>
int
main(int argc, char *argv[])
{
PyObject *pName, *pModule, *pFunc;
PyObject *pArgs, *pValue;
int i;
if (argc < 3) {
fprintf(stderr,"Usage: call pythonfile funcname [args]\n");
return 1;
}
Py_Initialize();
pName = PyUnicode_DecodeFSDefault(argv[1]);
/* Error checking of pName left out */
pModule = PyImport_Import(pName);
Py_DECREF(pName);
if (pModule != NULL) {
pFunc = PyObject_GetAttrString(pModule, argv[2]);
/* pFunc is a new reference */
if (pFunc && PyCallable_Check(pFunc)) {
pArgs = PyTuple_New(argc - 3);
for (i = 0; i < argc - 3; ++i) {
pValue = PyLong_FromLong(atoi(argv[i + 3]));
if (!pValue) {
Py_DECREF(pArgs);
Py_DECREF(pModule);
fprintf(stderr, "Cannot convert argument\n");
return 1;
(continuesonnextpage)
3.1. EmbeddingPythoninAnotherApplication 63

### 第68页

(continuedfrompreviouspage)
}
/* pValue reference stolen here: */
PyTuple_SetItem(pArgs, i, pValue);
}
pValue = PyObject_CallObject(pFunc, pArgs);
Py_DECREF(pArgs);
if (pValue != NULL) {
printf("Result of call: %ld\n", PyLong_AsLong(pValue));
Py_DECREF(pValue);
}
else {
Py_DECREF(pFunc);
Py_DECREF(pModule);
PyErr_Print();
fprintf(stderr,"Call failed\n");
return 1;
}
}
else {
if (PyErr_Occurred())
PyErr_Print();
fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
}
Py_XDECREF(pFunc);
Py_DECREF(pModule);
}
else {
PyErr_Print();
fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
return 1;
}
if (Py_FinalizeEx() < 0) {
return 120;
}
return 0;
}
ThiscodeloadsaPythonscriptusingargv[1],andcallsthefunctionnamedinargv[2]. Itsintegerargumentsare
theothervaluesoftheargvarray. Ifyoucompileandlinkthisprogram(let’scallthefinishedexecutablecall),and
useittoexecuteaPythonscript,suchas:
def multiply(a,b):
print("Will compute", a, "times", b)
c = 0
for i in range(0, a):
c = c + b
return c
thentheresultshouldbe:
$ call multiply multiply 3 2
Will compute 3 times 2
Result of call: 6
Althoughtheprogramisquitelargeforitsfunctionality,mostofthecodeisfordataconversionbetweenPythonand
C,andforerrorreporting. TheinterestingpartwithrespecttoembeddingPythonstartswith
64 Chapter3. EmbeddingtheCPythonruntimeinalargerapplication

### 第69页

Py_Initialize();
pName = PyUnicode_DecodeFSDefault(argv[1]);
/* Error checking of pName left out */
pModule = PyImport_Import(pName);
Afterinitializingtheinterpreter,thescriptisloadedusingPyImport_Import(). ThisroutineneedsaPythonstring
asitsargument,whichisconstructedusingthePyUnicode_DecodeFSDefault()dataconversionroutine.
pFunc = PyObject_GetAttrString(pModule, argv[2]);
/* pFunc is a new reference */
if (pFunc && PyCallable_Check(pFunc)) {
...
}
Py_XDECREF(pFunc);
Oncethescriptisloaded,thenamewe’relookingforisretrievedusingPyObject_GetAttrString(). Ifthename
exists,andtheobjectreturnediscallable,youcansafelyassumethatitisafunction. Theprogramthenproceedsby
constructingatupleofargumentsasnormal. ThecalltothePythonfunctionisthenmadewith:
pValue = PyObject_CallObject(pFunc, pArgs);
Uponreturnofthefunction,pValueiseitherNULLoritcontainsareferencetothereturnvalueofthefunction. Be
suretoreleasethereferenceafterexaminingthevalue.
3.1.4 Extending Embedded Python
Untilnow,theembeddedPythoninterpreterhadnoaccesstofunctionalityfromtheapplicationitself. ThePython
APIallowsthisbyextendingtheembeddedinterpreter. Thatis,theembeddedinterpretergetsextendedwithroutines
providedbytheapplication. Whileitsoundscomplex,itisnotsobad. Simplyforgetforawhilethattheapplication
startsthePythoninterpreter. Instead,considertheapplicationtobeasetofsubroutines,andwritesomegluecode
thatgivesPythonaccesstothoseroutines,justlikeyouwouldwriteanormalPythonextension. Forexample:
static int numargs=0;
/* Return the number of arguments of the application command line */
static PyObject*
emb_numargs(PyObject *self, PyObject *args)
{
if(!PyArg_ParseTuple(args, ":numargs"))
return NULL;
return PyLong_FromLong(numargs);
}
static PyMethodDef emb_module_methods[] = {
{"numargs", emb_numargs, METH_VARARGS,
"Return the number of arguments received by the process."},
{NULL, NULL, 0, NULL}
};
static struct PyModuleDef emb_module = {
.m_base = PyModuleDef_HEAD_INIT,
.m_name = "emb",
.m_size = 0,
.m_methods = emb_module_methods,
};
(continuesonnextpage)
3.1. EmbeddingPythoninAnotherApplication 65

### 第70页

(continuedfrompreviouspage)
static PyObject*
PyInit_emb(void)
{
return PyModuleDef_Init(&emb_module);
}
Inserttheabovecodejustabovethemain()function. Also, insertthefollowingtwostatementsbeforethecallto
Py_Initialize():
numargs = argc;
PyImport_AppendInittab("emb", &PyInit_emb);
Thesetwolinesinitializethenumargsvariable,andmaketheemb.numargs()functionaccessibletotheembedded
Pythoninterpreter. Withtheseextensions,thePythonscriptcandothingslike
import emb
print("Number of arguments", emb.numargs())
Inarealapplication,themethodswillexposeanAPIoftheapplicationtoPython.
3.1.5 Embedding Python in C++
ItisalsopossibletoembedPythoninaC++program; preciselyhowthisisdonewilldependonthedetailsofthe
C++systemused;ingeneralyouwillneedtowritethemainprograminC++,andusetheC++compilertocompile
andlinkyourprogram. ThereisnoneedtorecompilePythonitselfusingC++.
3.1.6 Compiling and Linking under Unix-like systems
Itisnotnecessarilytrivialtofindtherightflagstopasstoyourcompiler(andlinker)inordertoembedthePythonin-
terpreterintoyourapplication,particularlybecausePythonneedstoloadlibrarymodulesimplementedasCdynamic
extensions(.sofiles)linkedagainstit.
Tofindouttherequiredcompilerandlinkerflags,youcanexecutethepythonX.Y-configscriptwhichisgenerated
aspartoftheinstallationprocess(apython3-configscriptmayalsobeavailable). Thisscripthasseveraloptions,
ofwhichthefollowingwillbedirectlyusefultoyou:
• pythonX.Y-config --cflagswillgiveyoutherecommendedflagswhencompiling:
$ /opt/bin/python3.11-config --cflags
-I/opt/include/python3.11 -I/opt/include/python3.11 -Wsign-compare -DNDEBUG -
,→g -fwrapv -O3 -Wall
• pythonX.Y-config --ldflags --embedwillgiveyoutherecommendedflagswhenlinking:
$ /opt/bin/python3.11-config --ldflags --embed
-L/opt/lib/python3.11/config-3.11-x86_64-linux-gnu -L/opt/lib -lpython3.11 -
,→lpthread -ldl -lutil -lm
(cid:174) Note
ToavoidconfusionbetweenseveralPythoninstallations(andespeciallybetweenthesystemPythonandyourown
compiledPython), itisrecommendedthatyouusetheabsolutepathtopythonX.Y-config, asintheabove
example.
Ifthisproceduredoesn’tworkforyou(itisnotguaranteedtoworkforallUnix-likeplatforms;however,wewelcome
bug reports) you will have to read your system’s documentation about dynamic linking and/or examine Python’s
Makefile(usesysconfig.get_makefile_filename()tofinditslocation)andcompilationoptions. Inthis
66 Chapter3. EmbeddingtheCPythonruntimeinalargerapplication

### 第71页

case,thesysconfigmoduleisausefultooltoprogrammaticallyextracttheconfigurationvaluesthatyouwillwant
tocombinetogether. Forexample:
>>> import sysconfig
>>> sysconfig.get_config_var('LIBS')
'-lpthread -ldl -lutil'
>>> sysconfig.get_config_var('LINKFORSHARED')
'-Xlinker -export-dynamic'
3.1. EmbeddingPythoninAnotherApplication 67

### 第72页

68 Chapter3. EmbeddingtheCPythonruntimeinalargerapplication

### 第73页

APPENDIX
A
GLOSSARY
>>>
The default Python prompt of the interactive shell. Often seen for code examples which can be executed
interactivelyintheinterpreter.
...
Canreferto:
• ThedefaultPythonpromptoftheinteractiveshellwhenenteringthecodeforanindentedcodeblock,
when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or
triplequotes),orafterspecifyingadecorator.
• ThethreedotsformoftheEllipsisobject.
abstractbaseclass
Abstractbaseclassescomplementduck-typingbyprovidingawaytodefineinterfaceswhenothertechniques
likehasattr()wouldbeclumsyorsubtlywrong(forexamplewithmagicmethods). ABCsintroducevirtual
subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and
issubclass();seetheabcmoduledocumentation. Pythoncomeswithmanybuilt-inABCsfordatastruc-
tures(inthecollections.abcmodule),numbers(inthenumbersmodule),streams(intheiomodule),
importfindersandloaders(intheimportlib.abcmodule). YoucancreateyourownABCswiththeabc
module.
annotatefunction
A function that can be called to retrieve the annotations of an object. This function is accessible as the
__annotate__ attribute of functions, classes, and modules. Annotate functions are a subset of evaluate
functions.
annotation
Alabelassociatedwithavariable,aclassattributeorafunctionparameterorreturnvalue,usedbyconvention
asatypehint.
Annotations of local variables cannot be accessed at runtime, but annotations of global variables, class at-
tributes, and functions can be retrieved by calling annotationlib.get_annotations() on modules,
classes,andfunctions,respectively.
Seevariableannotation, functionannotation, PEP484, PEP526, andPEP649, whichdescribethisfunc-
tionality. Alsoseeannotations-howtoforbestpracticesonworkingwithannotations.
argument
Avaluepassedtoafunction(ormethod)whencallingthefunction. Therearetwokindsofargument:
• keywordargument: anargumentprecededbyanidentifier(e.g. name=)inafunctioncallorpassedasa
valueinadictionaryprecededby**. Forexample,3and5arebothkeywordargumentsinthefollowing
callstocomplex():
complex(real=3, imag=5)
complex(**{'real': 3, 'imag': 5})
• positionalargument: anargumentthatisnotakeywordargument. Positionalargumentscanappearatthe
beginningofanargumentlistand/orbepassedaselementsofaniterableprecededby*. Forexample,3
69

### 第74页

and5arebothpositionalargumentsinthefollowingcalls:
complex(3, 5)
complex(*(3, 5))
Arguments are assigned to the named local variables in a function body. See the calls section for the rules
governingthisassignment. Syntactically,anyexpressioncanbeusedtorepresentanargument;theevaluated
valueisassignedtothelocalvariable.
Seealsotheparameterglossaryentry,theFAQquestiononthedifferencebetweenargumentsandparameters,
andPEP362.
asynchronouscontextmanager
Anobjectwhichcontrolstheenvironmentseeninanasync withstatementbydefining__aenter__()and
__aexit__()methods. IntroducedbyPEP492.
asynchronousgenerator
Afunctionwhichreturnsanasynchronousgeneratoriterator. Itlookslikeacoroutinefunctiondefinedwith
async def except that it contains yield expressions for producing a series of values usable in an async
forloop.
Usuallyreferstoanasynchronousgeneratorfunction, butmayrefertoanasynchronousgeneratoriterator in
somecontexts. Incaseswheretheintendedmeaningisn’tclear,usingthefulltermsavoidsambiguity.
Anasynchronousgeneratorfunctionmaycontainawaitexpressionsaswellasasync for,andasync with
statements.
asynchronousgeneratoriterator
Anobjectcreatedbyanasynchronousgeneratorfunction.
Thisisanasynchronousiteratorwhichwhencalledusingthe__anext__()methodreturnsanawaitableobject
whichwillexecutethebodyoftheasynchronousgeneratorfunctionuntilthenextyieldexpression.
Eachyieldtemporarilysuspendsprocessing,rememberingtheexecutionstate(includinglocalvariablesand
pendingtry-statements). Whentheasynchronousgeneratoriteratoreffectivelyresumeswithanotherawaitable
returnedby__anext__(),itpicksupwhereitleftoff. SeePEP492andPEP525.
asynchronousiterable
An object, that can be used in an async for statement. Must return an asynchronous iterator from its
__aiter__()method. IntroducedbyPEP492.
asynchronousiterator
An object that implements the __aiter__() and __anext__() methods. __anext__() must return an
awaitableobject. async forresolvestheawaitablesreturnedbyanasynchronousiterator’s__anext__()
methoduntilitraisesaStopAsyncIterationexception. IntroducedbyPEP492.
attachedthreadstate
AthreadstatethatisactiveforthecurrentOSthread.
Whenathreadstateisattached,theOSthreadhasaccesstothefullPythonCAPIandcansafelyinvokethe
bytecodeinterpreter.
Unlessafunctionexplicitlynotesotherwise,attemptingtocalltheCAPIwithoutanattachedthreadstatewill
result in a fatal error or undefined behavior. A thread state can be attached and detached explicitly by the
userthroughtheCAPI,orimplicitlybytheruntime,includingduringblockingCcallsandbythebytecode
interpreterinbetweencalls.
OnmostbuildsofPython,havinganattachedthreadstateimpliesthatthecallerholdstheGILforthecurrent
interpreter,soonlyoneOSthreadcanhaveanattachedthreadstateatagivenmoment. Infree-threadedbuilds
ofPython,threadscanconcurrentlyholdanattachedthreadstate,allowingfortrueparallelismofthebytecode
interpreter.
attribute
Avalueassociatedwithanobjectwhichisusuallyreferencedbynameusingdottedexpressions. Forexample,
ifanobjectohasanattributeaitwouldbereferencedaso.a.
70 AppendixA. Glossary

### 第75页

Itispossibletogiveanobjectanattributewhosenameisnotanidentifierasdefinedbyidentifiers,forexample
usingsetattr(),iftheobjectallowsit. Suchanattributewillnotbeaccessibleusingadottedexpression,
andwouldinsteadneedtoberetrievedwithgetattr().
awaitable
Anobjectthatcanbeusedinanawaitexpression. Canbeacoroutineoranobjectwithan__await__()
method. SeealsoPEP492.
BDFL
BenevolentDictatorForLife,a.k.a. GuidovanRossum,Python’screator.
binaryfile
Afileobjectabletoreadandwritebytes-likeobjects. Examplesofbinaryfilesarefilesopenedinbinarymode
('rb','wb'or'rb+'),sys.stdin.buffer,sys.stdout.buffer,andinstancesofio.BytesIOand
gzip.GzipFile.
Seealsotextfileforafileobjectabletoreadandwritestrobjects.
borrowedreference
InPython’sCAPI,aborrowedreferenceisareferencetoanobject,wherethecodeusingtheobjectdoesnot
ownthereference. Itbecomesadanglingpointeriftheobjectisdestroyed. Forexample,agarbagecollection
canremovethelaststrongreferencetotheobjectandsodestroyit.
CallingPy_INCREF()ontheborrowedreferenceisrecommendedtoconvertittoastrongreferencein-place,
exceptwhentheobjectcannotbedestroyedbeforethelastusageoftheborrowedreference. ThePy_NewRef()
functioncanbeusedtocreateanewstrongreference.
bytes-likeobject
An object that supports the bufferobjects and can export a C-contiguous buffer. This includes all bytes,
bytearray,andarray.arrayobjects,aswellasmanycommonmemoryviewobjects. Bytes-likeobjects
canbeusedforvariousoperationsthatworkwithbinarydata;theseincludecompression,savingtoabinary
file,andsendingoverasocket.
Someoperationsneedthebinarydatatobemutable. Thedocumentationoftenreferstotheseas“read-write
bytes-likeobjects”. Examplemutablebufferobjectsincludebytearrayandamemoryviewofabytearray.
Other operations require the binary data to be stored in immutable objects (“read-only bytes-like objects”);
examplesoftheseincludebytesandamemoryviewofabytesobject.
bytecode
Pythonsourcecodeiscompiledintobytecode,theinternalrepresentationofaPythonprogramintheCPython
interpreter. Thebytecodeisalsocachedin.pycfilessothatexecutingthesamefileisfasterthesecondtime
(recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a
virtualmachinethatexecutesthemachinecodecorrespondingtoeachbytecode. Donotethatbytecodesare
notexpectedtoworkbetweendifferentPythonvirtualmachines,nortobestablebetweenPythonreleases.
Alistofbytecodeinstructionscanbefoundinthedocumentationforthedismodule.
callable
Acallableisanobjectthatcanbecalled,possiblywithasetofarguments(seeargument),withthefollowing
syntax:
callable(argument1, argument2, argumentN)
Afunction,andbyextensionamethod,isacallable. Aninstanceofaclassthatimplementsthe__call__()
methodisalsoacallable.
callback
Asubroutinefunctionwhichispassedasanargumenttobeexecutedatsomepointinthefuture.
class
A template for creating user-defined objects. Class definitions normally contain method definitions which
operateoninstancesoftheclass.
classvariable
Avariabledefinedinaclassandintendedtobemodifiedonlyatclasslevel(i.e.,notinaninstanceoftheclass).
71

### 第76页

closurevariable
Afreevariablereferencedfromanestedscopethatisdefinedinanouterscoperatherthanbeingresolvedat
runtime from the globals or builtin namespaces. May be explicitly defined with the nonlocal keyword to
allowwriteaccess,orimplicitlydefinedifthevariableisonlybeingread.
Forexample,intheinnerfunctioninthefollowingcode,bothxandprintarefreevariables,butonlyxis
aclosurevariable:
def outer():
x = 0
def inner():
nonlocal x
x += 1
print(x)
return inner
Duetothecodeobject.co_freevarsattribute(which,despiteitsname,onlyincludesthenamesofclosure
variablesratherthanlistingallreferencedfreevariables),themoregeneralfreevariabletermissometimesused
evenwhentheintendedmeaningistoreferspecificallytoclosurevariables.
complexnumber
Anextensionofthefamiliarrealnumbersysteminwhichallnumbersareexpressedasasumofarealpartand
animaginarypart. Imaginarynumbersarerealmultiplesoftheimaginaryunit(thesquarerootof-1),often
written i in mathematics or j in engineering. Python has built-in support for complex numbers, which are
writtenwiththislatternotation;theimaginarypartiswrittenwithajsuffix,e.g.,3+1j. Togetaccesstocom-
plexequivalentsofthemathmodule,usecmath. Useofcomplexnumbersisafairlyadvancedmathematical
feature. Ifyou’renotawareofaneedforthem,it’salmostcertainyoucansafelyignorethem.
context
Thistermhasdifferentmeaningsdependingonwhereandhowitisused. Somecommonmeanings:
• Thetemporarystateorenvironmentestablishedbyacontextmanagerviaawithstatement.
• The collection of keyvalue bindings associated with a particular contextvars.Context object and
accessedviaContextVarobjects. Alsoseecontextvariable.
• Acontextvars.Contextobject. Alsoseecurrentcontext.
contextmanagementprotocol
The__enter__()and__exit__()methodscalledbythewithstatement. SeePEP343.
contextmanager
Anobjectwhichimplementsthecontextmanagementprotocol andcontrolstheenvironmentseenina with
statement. SeePEP343.
contextvariable
A variable whose value depends on which context is the current context. Values are accessed via
contextvars.ContextVarobjects. Contextvariablesareprimarilyusedtoisolatestatebetweenconcur-
rentasynchronoustasks.
contiguous
AbufferisconsideredcontiguousexactlyifitiseitherC-contiguousorFortrancontiguous. Zero-dimensional
buffersareCandFortrancontiguous. Inone-dimensionalarrays,theitemsmustbelaidoutinmemorynext
toeachother,inorderofincreasingindexesstartingfromzero. InmultidimensionalC-contiguousarrays,the
lastindexvariesthefastestwhenvisitingitemsinorderofmemoryaddress. However,inFortrancontiguous
arrays,thefirstindexvariesthefastest.
coroutine
Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at
anotherpoint. Coroutinescanbeentered,exited,andresumedatmanydifferentpoints. Theycanbeimple-
mentedwiththeasync defstatement. SeealsoPEP492.
coroutinefunction
Afunctionwhichreturnsacoroutineobject. Acoroutinefunctionmaybedefinedwiththeasync defstate-
72 AppendixA. Glossary

### 第77页

ment, and may contain await, async for, and async with keywords. These were introduced by PEP
492.
CPython
ThecanonicalimplementationofthePythonprogramminglanguage,asdistributedonpython.org. Theterm
“CPython”isusedwhennecessarytodistinguishthisimplementationfromotherssuchasJythonorIronPython.
currentcontext
Thecontext (contextvars.Contextobject)thatiscurrentlyusedbyContextVarobjectstoaccess(get
or set) the values of context variables. Each thread has its own current context. Frameworks for executing
asynchronous tasks (see asyncio) associate each task with a context which becomes the current context
wheneverthetaskstartsorresumesexecution.
cyclicisolate
A subgroup of one or more objects that reference each other in a reference cycle, but are not referenced by
objects outside the group. The goal of the cyclic garbage collector is to identify these groups and break the
referencecyclessothatthememorycanbereclaimed.
decorator
Afunctionreturninganotherfunction,usuallyappliedasafunctiontransformationusingthe@wrappersyntax.
Commonexamplesfordecoratorsareclassmethod()andstaticmethod().
Thedecoratorsyntaxismerelysyntacticsugar,thefollowingtwofunctiondefinitionsaresemanticallyequiv-
alent:
def f(arg):
...
f = staticmethod(f)
@staticmethod
def f(arg):
...
The same concept exists for classes, but is less commonly used there. See the documentation for function
definitionsandclassdefinitionsformoreaboutdecorators.
descriptor
Anyobjectwhichdefinesthemethods__get__(),__set__(),or__delete__(). Whenaclassattribute
is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get,
set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor,
therespectivedescriptormethodgetscalled. Understandingdescriptorsisakeytoadeepunderstandingof
Pythonbecausetheyarethebasisformanyfeaturesincludingfunctions,methods,properties,classmethods,
staticmethods,andreferencetosuperclasses.
Formoreinformationaboutdescriptors’methods,seedescriptorsortheDescriptorHowToGuide.
dictionary
Anassociativearray,wherearbitrarykeysaremappedtovalues. Thekeyscanbeanyobjectwith__hash__()
and__eq__()methods. CalledahashinPerl.
dictionarycomprehension
A compact way to process all or part of the elements in an iterable and return a dictionary with the re-
sults. results = {n: n ** 2 for n in range(10)}generatesadictionarycontainingkeynmapped
tovaluen ** 2. Seecomprehensions.
dictionaryview
Theobjectsreturnedfromdict.keys(),dict.values(),anddict.items()arecalleddictionaryviews.
Theyprovideadynamicviewonthedictionary’sentries,whichmeansthatwhenthedictionarychanges,the
view reflects these changes. To force the dictionary view to become a full list use list(dictview). See
dict-views.
docstring
Astringliteralwhichappearsasthefirstexpressioninaclass,functionormodule. Whileignoredwhenthe
suiteisexecuted,itisrecognizedbythecompilerandputintothe__doc__attributeoftheenclosingclass,
73

### 第78页

functionormodule. Sinceitisavailableviaintrospection,itisthecanonicalplacefordocumentationofthe
object.
duck-typing
Aprogrammingstylewhichdoesnotlookatanobject’stypetodetermineifithastherightinterface;instead,
the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be
a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility
by allowing polymorphic substitution. Duck-typing avoids tests using type() or isinstance(). (Note,
however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs
hasattr()testsorEAFPprogramming.
dunder
An informal short-hand for “double underscore”, used when talking about a special method. For example,
__init__isoftenpronounced“dunderinit”.
EAFP
Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of
valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is
characterizedbythepresenceofmanytryandexceptstatements. ThetechniquecontrastswiththeLBYL
stylecommontomanyotherlanguagessuchasC.
evaluatefunction
A function that can be called to evaluate a lazily evaluated attribute of an object, such as the value of type
aliasescreatedwiththetypestatement.
expression
Apieceofsyntaxwhichcanbeevaluatedtosomevalue. Inotherwords,anexpressionisanaccumulationof
expressionelementslikeliterals,names,attributeaccess,operatorsorfunctioncallswhichallreturnavalue. In
contrasttomanyotherlanguages,notalllanguageconstructsareexpressions. Therearealsostatementswhich
cannotbeusedasexpressions,suchaswhile. Assignmentsarealsostatements,notexpressions.
extensionmodule
AmodulewritteninCorC++,usingPython’sCAPItointeractwiththecoreandwithusercode.
f-string
f-strings
StringliteralsprefixedwithforFarecommonlycalled“f-strings”whichisshortforformattedstringliterals.
SeealsoPEP498.
fileobject
Anobjectexposingafile-orientedAPI(withmethodssuchasread()orwrite())toanunderlyingresource.
Dependingonthewayitwascreated,afileobjectcanmediateaccesstoarealon-diskfileortoanothertypeof
storageorcommunicationdevice(forexamplestandardinput/output,in-memorybuffers,sockets,pipes,etc.).
Fileobjectsarealsocalledfile-likeobjectsorstreams.
Thereareactuallythreecategoriesoffileobjects: rawbinaryfiles, bufferedbinaryfilesandtextfiles. Their
interfaces are defined in the io module. The canonical way to create a file object is by using the open()
function.
file-likeobject
Asynonymforfileobject.
filesystemencodinganderrorhandler
EncodinganderrorhandlerusedbyPythontodecodebytesfromtheoperatingsystemandencodeUnicodeto
theoperatingsystem.
Thefilesystemencodingmustguaranteetosuccessfullydecodeallbytesbelow128. Ifthefilesystemencoding
failstoprovidethisguarantee,APIfunctionscanraiseUnicodeError.
The sys.getfilesystemencoding() and sys.getfilesystemencodeerrors() functions can be
usedtogetthefilesystemencodinganderrorhandler.
ThefilesystemencodinganderrorhandlerareconfiguredatPythonstartupbythePyConfig_Read()func-
tion: seefilesystem_encodingandfilesystem_errorsmembersofPyConfig.
Seealsothelocaleencoding.
74 AppendixA. Glossary

### 第79页

finder
Anobjectthattriestofindtheloaderforamodulethatisbeingimported.
Therearetwotypesoffinder: metapathfindersforusewithsys.meta_path,andpathentryfindersforuse
withsys.path_hooks.
Seefinders-and-loadersandimportlibformuchmoredetail.
floordivision
Mathematicaldivisionthatroundsdowntonearestinteger. Thefloordivisionoperatoris//. Forexample,the
expression11 // 4evaluatesto2incontrasttothe2.75returnedbyfloattruedivision. Notethat(-11)
// 4is-3becausethatis-2.75roundeddownward. SeePEP238.
freethreading
AthreadingmodelwheremultiplethreadscanrunPythonbytecodesimultaneouslywithinthesameinterpreter.
ThisisincontrasttotheglobalinterpreterlockwhichallowsonlyonethreadtoexecutePythonbytecodeata
time. SeePEP703.
freevariable
Formally, as defined in the language execution model, a free variable is any variable used in a namespace
whichisnotalocalvariableinthatnamespace. Seeclosurevariableforanexample. Pragmatically,duetothe
nameofthecodeobject.co_freevarsattribute,thetermisalsosometimesusedasasynonymforclosure
variable.
function
Aseriesofstatementswhichreturnssomevaluetoacaller. Itcanalsobepassedzeroormoreargumentswhich
maybeusedintheexecutionofthebody. Seealsoparameter,method,andthefunctionsection.
functionannotation
Anannotationofafunctionparameterorreturnvalue.
Function annotations are usually used for type hints: for example, this function is expected to take two int
argumentsandisalsoexpectedtohaveanintreturnvalue:
def sum_two_numbers(a: int, b: int) -> int:
return a + b
Functionannotationsyntaxisexplainedinsectionfunction.
SeevariableannotationandPEP484,whichdescribethisfunctionality. Alsoseeannotations-howtoforbest
practicesonworkingwithannotations.
__future__
Afuturestatement,from __future__ import <feature>,directsthecompilertocompilethecurrent
moduleusingsyntaxorsemanticsthatwillbecomestandardinafuturereleaseofPython. The__future__
moduledocumentsthepossiblevaluesoffeature. Byimportingthismoduleandevaluatingitsvariables,you
canseewhenanewfeaturewasfirstaddedtothelanguageandwhenitwill(ordid)becomethedefault:
>>> import __future__
>>> __future__.division
_Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)
garbagecollection
Theprocessoffreeingmemorywhenitisnotusedanymore. Pythonperformsgarbagecollectionviareference
countingandacyclicgarbagecollectorthatisabletodetectandbreakreferencecycles. Thegarbagecollector
canbecontrolledusingthegcmodule.
generator
A function which returns a generator iterator. It looks like a normal function except that it contains yield
expressionsforproducingaseriesofvaluesusableinafor-looporthatcanberetrievedoneatatimewiththe
next()function.
Usuallyreferstoageneratorfunction,butmayrefertoageneratoriterator insomecontexts. Incaseswhere
theintendedmeaningisn’tclear,usingthefulltermsavoidsambiguity.
75

### 第80页

generatoriterator
Anobjectcreatedbyageneratorfunction.
Eachyieldtemporarilysuspendsprocessing,rememberingtheexecutionstate(includinglocalvariablesand
pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to
functionswhichstartfreshoneveryinvocation).
generatorexpression
Anexpressionthatreturnsaniterator. Itlookslikeanormalexpressionfollowedbyaforclausedefininga
loop variable, range, andan optional if clause. The combinedexpressiongeneratesvaluesfor an enclosing
function:
>>> sum(i*i for i in range(10)) # sum of squares 0, 1, 4, ... 81
285
genericfunction
Afunctioncomposedofmultiplefunctionsimplementingthesameoperationfordifferenttypes. Whichim-
plementationshouldbeusedduringacallisdeterminedbythedispatchalgorithm.
Seealsothesingledispatchglossaryentry,thefunctools.singledispatch()decorator,andPEP443.
generictype
Atypethatcanbeparameterized; typicallyacontainerclasssuchaslistordict. Usedfortypehintsand
annotations.
Formoredetails,seegenericaliastypes,PEP483,PEP484,PEP585,andthetypingmodule.
GIL
Seeglobalinterpreterlock.
globalinterpreterlock
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at
a time. This simplifies the CPython implementation by making the object model (including critical built-in
typessuchasdict)implicitlysafeagainstconcurrentaccess. Lockingtheentireinterpretermakesiteasier
fortheinterpretertobemulti-threaded,attheexpenseofmuchoftheparallelismaffordedbymulti-processor
machines.
However,someextensionmodules,eitherstandardorthird-party,aredesignedsoastoreleasetheGILwhen
doingcomputationallyintensivetaskssuchascompressionorhashing. Also,theGILisalwaysreleasedwhen
doingI/O.
AsofPython3.13, theGILcanbedisabledusingthe--disable-gilbuildconfiguration. Afterbuilding
Pythonwiththisoption,codemustberunwith-X gil=0oraftersettingthePYTHON_GIL=0environment
variable. This feature enables improved performance for multi-threaded applications and makes it easier to
usemulti-coreCPUsefficiently. Formoredetails,seePEP703.
InpriorversionsofPython’sCAPI,afunctionmightdeclarethatitrequirestheGILtobeheldinordertouse
it. Thisreferstohavinganattachedthreadstate.
hash-basedpyc
Abytecodecachefilethatusesthehashratherthanthelast-modifiedtimeofthecorrespondingsourcefileto
determineitsvalidity. Seepyc-invalidation.
hashable
Anobjectishashableifithasahashvaluewhichneverchangesduringitslifetime(itneedsa__hash__()
method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which
compareequalmusthavethesamehashvalue.
Hashabilitymakesanobjectusableasadictionarykeyandasetmember,becausethesedatastructuresusethe
hashvalueinternally.
Most of Python’s immutable built-in objects are hashable; mutable containers (such as lists or dictionaries)
arenot;immutablecontainers(suchastuplesandfrozensets)areonlyhashableiftheirelementsarehashable.
Objectswhichareinstancesofuser-definedclassesarehashablebydefault. Theyallcompareunequal(except
withthemselves),andtheirhashvalueisderivedfromtheirid().
76 AppendixA. Glossary

### 第81页

IDLE
AnIntegratedDevelopmentandLearningEnvironmentforPython. idleisabasiceditorandinterpreterenvi-
ronmentwhichshipswiththestandarddistributionofPython.
immortal
ImmortalobjectsareaCPythonimplementationdetailintroducedinPEP683.
Ifanobjectisimmortal,itsreferencecount isnevermodified,andthereforeitisneverdeallocatedwhilethe
interpreterisrunning. Forexample,TrueandNoneareimmortalinCPython.
Immortalobjectscanbeidentifiedviasys._is_immortal(),orviaPyUnstable_IsImmortal()inthe
CAPI.
immutable
Anobjectwithafixedvalue. Immutableobjectsincludenumbers,stringsandtuples. Suchanobjectcannot
bealtered. Anewobjecthastobecreatedifadifferentvaluehastobestored. Theyplayanimportantrolein
placeswhereaconstanthashvalueisneeded,forexampleasakeyinadictionary.
importpath
Alistoflocations(orpathentries)thataresearchedbythepathbasedfinderformodulestoimport. During
import,thislistoflocationsusuallycomesfromsys.path,butforsubpackagesitmayalsocomefromthe
parentpackage’s__path__attribute.
importing
TheprocessbywhichPythoncodeinonemoduleismadeavailabletoPythoncodeinanothermodule.
importer
Anobjectthatbothfindsandloadsamodule;bothafinderandloaderobject.
interactive
Pythonhasaninteractiveinterpreterwhichmeansyoucanenterstatementsandexpressionsattheinterpreter
prompt, immediately execute them and see their results. Just launch python with no arguments (possibly
by selecting it fromyour computer’s mainmenu). It isa very powerfulway to testout new ideas orinspect
modulesandpackages(rememberhelp(x)). Formoreoninteractivemode,seetut-interac.
interpreted
Pythonisaninterpretedlanguage,asopposedtoacompiledone,thoughthedistinctioncanbeblurrybecause
ofthepresenceofthebytecodecompiler. Thismeansthatsourcefilescanberundirectlywithoutexplicitly
creating an executable which is then run. Interpreted languages typically have a shorter development/debug
cyclethancompiledones,thoughtheirprogramsgenerallyalsorunmoreslowly. Seealsointeractive.
interpretershutdown
Whenaskedtoshutdown,thePythoninterpreterentersaspecialphasewhereitgraduallyreleasesallallocated
resources, suchasmodulesandvariouscriticalinternalstructures. Italsomakesseveralcallstothegarbage
collector. Thiscantriggertheexecutionofcodeinuser-defineddestructorsorweakrefcallbacks. Codeexe-
cutedduringtheshutdownphasecanencountervariousexceptionsastheresourcesitreliesonmaynotfunction
anymore(commonexamplesarelibrarymodulesorthewarningsmachinery).
Themainreasonforinterpretershutdownisthatthe__main__moduleorthescriptbeingrunhasfinished
executing.
iterable
Anobjectcapableofreturningitsmembersoneatatime. Examplesofiterablesincludeallsequencetypes
(such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any
classesyoudefinewithan__iter__()methodorwitha__getitem__()methodthatimplementssequence
semantics.
Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(),
…). Whenaniterableobjectispassedasanargumenttothebuilt-infunctioniter(),itreturnsaniterator
fortheobject. Thisiteratorisgoodforonepassoverthesetofvalues. Whenusingiterables,itisusuallynot
necessarytocalliter()ordealwithiteratorobjectsyourself. Theforstatementdoesthatautomaticallyfor
you,creatingatemporaryunnamedvariabletoholdtheiteratorforthedurationoftheloop. Seealsoiterator,
sequence,andgenerator.
77

### 第82页

iterator
An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing
ittothebuilt-infunctionnext())returnsuccessiveitemsinthestream. Whennomoredataareavailablea
StopIterationexceptionisraisedinstead. Atthispoint,theiteratorobjectisexhaustedandanyfurthercalls
toits__next__()methodjustraiseStopIterationagain. Iteratorsarerequiredtohavean__iter__()
methodthatreturnstheiteratorobjectitselfsoeveryiteratorisalsoiterableandmaybeusedinmostplaces
whereotheriterablesareaccepted. Onenotableexceptioniscodewhichattemptsmultipleiterationpasses. A
containerobject(suchasalist)producesafreshnewiteratoreachtimeyoupassittotheiter()function
oruseitinaforloop. Attemptingthiswithaniteratorwilljustreturnthesameexhaustediteratorobjectused
inthepreviousiterationpass,makingitappearlikeanemptycontainer.
Moreinformationcanbefoundintypeiter.
CPythonimplementationdetail: CPythondoesnotconsistentlyapplytherequirementthataniteratordefine
__iter__(). Andalsopleasenotethatthefree-threadingCPythondoesnotguaranteethethread-safetyof
iteratoroperations.
keyfunction
Akeyfunctionorcollationfunctionisacallablethatreturnsavalueusedforsortingorordering. Forexample,
locale.strxfrm()isusedtoproduceasortkeythatisawareoflocalespecificsortconventions.
A number of tools in Python accept key functions to control how elements are ordered or grouped. They
include min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.
nlargest(),anditertools.groupby().
There are several ways to create a key function. For example. the str.lower() method can serve as a
key function for case insensitive sorts. Alternatively, a key function can be built from a lambda expression
suchaslambda r: (r[0], r[2]). Also,operator.attrgetter(),operator.itemgetter(),and
operator.methodcaller()arethreekeyfunctionconstructors. SeetheSortingHOWTOforexamples
ofhowtocreateandusekeyfunctions.
keywordargument
Seeargument.
lambda
Ananonymousinlinefunctionconsistingofasingleexpressionwhichisevaluatedwhenthefunctioniscalled.
Thesyntaxtocreatealambdafunctionislambda [parameters]: expression
LBYL
Lookbeforeyouleap. Thiscodingstyleexplicitlytestsforpre-conditionsbeforemakingcallsorlookups. This
stylecontrastswiththeEAFPapproachandischaracterizedbythepresenceofmanyifstatements.
In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the
looking”and“theleaping”. Forexample, thecode, if key in mapping: return mapping[key] can
failifanotherthreadremoveskeyfrommappingafterthetest,butbeforethelookup. Thisissuecanbesolved
withlocksorbyusingtheEAFPapproach.
lexicalanalyzer
Formalnameforthetokenizer;seetoken.
list
Abuilt-inPythonsequence. Despiteitsnameitismoreakintoanarrayinotherlanguagesthantoalinkedlist
sinceaccesstoelementsisO(1).
listcomprehension
Acompactwaytoprocessallorpartoftheelementsinasequenceandreturnalistwiththeresults. result
= ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]generatesalistofstringscon-
tainingevenhexnumbers(0x..) intherangefrom0to255. Theifclauseisoptional. Ifomitted,allelements
inrange(256)areprocessed.
loader
An object that loads a module. It must define the exec_module() and create_module() methods to
implementtheLoaderinterface. Aloaderistypicallyreturnedbyafinder. Seealso:
• finders-and-loaders
78 AppendixA. Glossary

### 第83页

• importlib.abc.Loader
• PEP302
localeencoding
On Unix, it is the encoding of the LC_CTYPE locale. It can be set with locale.setlocale(locale.
LC_CTYPE, new_locale).
OnWindows,itistheANSIcodepage(ex: "cp1252").
OnAndroidandVxWorks,Pythonuses"utf-8"asthelocaleencoding.
locale.getencoding()canbeusedtogetthelocaleencoding.
Seealsothefilesystemencodinganderrorhandler.
magicmethod
Aninformalsynonymforspecialmethod.
mapping
A container object that supports arbitrary key lookups and implements the methods specified in the
collections.abc.Mapping or collections.abc.MutableMapping abstract base classes. Exam-
ples include dict, collections.defaultdict, collections.OrderedDict and collections.
Counter.
metapathfinder
Afinderreturnedbyasearchofsys.meta_path. Metapathfindersarerelatedto,butdifferentfrompath
entryfinders.
Seeimportlib.abc.MetaPathFinderforthemethodsthatmetapathfindersimplement.
metaclass
Theclassofaclass. Classdefinitionscreateaclassname, aclassdictionary, andalistofbaseclasses. The
metaclass is responsible for taking those three arguments and creating the class. Most object oriented pro-
gramming languages provide a default implementation. What makes Python special is that it is possible to
createcustommetaclasses. Mostusersneverneedthistool,butwhentheneedarises,metaclassescanprovide
powerful,elegantsolutions. Theyhavebeenusedforloggingattributeaccess,addingthread-safety,tracking
objectcreation,implementingsingletons,andmanyothertasks.
Moreinformationcanbefoundinmetaclasses.
method
Afunctionwhichisdefinedinsideaclassbody. Ifcalledasanattributeofaninstanceofthatclass,themethod
willgettheinstanceobjectasitsfirstargument(whichisusuallycalledself). Seefunctionandnestedscope.
methodresolutionorder
Method Resolution Order is the order in which base classes are searched for a member during lookup. See
python_2.3_mrofordetailsofthealgorithmusedbythePythoninterpretersincethe2.3release.
module
AnobjectthatservesasanorganizationalunitofPythoncode. Moduleshaveanamespacecontainingarbitrary
Pythonobjects. ModulesareloadedintoPythonbytheprocessofimporting.
Seealsopackage.
modulespec
Anamespacecontainingtheimport-relatedinformationusedtoloadamodule. Aninstanceofimportlib.
machinery.ModuleSpec.
Seealsomodule-specs.
MRO
Seemethodresolutionorder.
mutable
Mutableobjectscanchangetheirvaluebutkeeptheirid(). Seealsoimmutable.
79

### 第84页

namedtuple
Theterm“namedtuple”appliestoanytypeorclassthatinheritsfromtupleandwhoseindexableelementsare
alsoaccessibleusingnamedattributes. Thetypeorclassmayhaveotherfeaturesaswell.
Several built-in types are named tuples, including the values returned by time.localtime() and os.
stat(). Anotherexampleissys.float_info:
>>> sys.float_info[1] # indexed access
1024
>>> sys.float_info.max_exp # named field access
1024
>>> isinstance(sys.float_info, tuple) # kind of tuple
True
Some named tuples are built-in types (such as the above examples). Alternatively, a named tuple can be
created from a regular class definition that inherits from tuple and that defines named fields. Such a class
canbewrittenbyhand,oritcanbecreatedbyinheritingtyping.NamedTuple,orwiththefactoryfunction
collections.namedtuple(). Thelattertechniquesalsoaddsomeextramethodsthatmaynotbefound
inhand-writtenorbuilt-innamedtuples.
namespace
The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local,
global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support
modularitybypreventingnamingconflicts. Forinstance,thefunctionsbuiltins.openandos.open()are
distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear
which module implements a function. For instance, writing random.seed() or itertools.islice()
makesitclearthatthosefunctionsareimplementedbytherandomanditertoolsmodules,respectively.
namespacepackage
A package which serves only as a container for subpackages. Namespace packages may have no physical
representation,andspecificallyarenotlikearegularpackagebecausetheyhaveno__init__.pyfile.
Namespacepackagesallowseveralindividuallyinstallablepackagestohaveacommonparentpackage. Oth-
erwise,itisrecommendedtousearegularpackage.
Formoreinformation,seePEP420andreference-namespace-package.
Seealsomodule.
nestedscope
The ability to refer to a variable in an enclosing definition. For instance, a function defined inside another
functioncanrefertovariablesintheouterfunction. Notethatnestedscopesbydefaultworkonlyforreference
andnotforassignment. Localvariablesbothreadandwriteintheinnermostscope. Likewise,globalvariables
readandwritetotheglobalnamespace. Thenonlocalallowswritingtoouterscopes.
new-styleclass
Old name for the flavor of classes now used for all class objects. In earlier Python versions, only
new-style classes could use Python’s newer, versatile features like __slots__, descriptors, properties,
__getattribute__(),classmethods,andstaticmethods.
object
Anydatawithstate(attributesorvalue)anddefinedbehavior(methods). Alsotheultimatebaseclassofany
new-styleclass.
optimizedscope
A scope where target local variable names are reliably known to the compiler when the code is compiled,
allowingoptimizationofreadandwriteaccesstothesenames. Thelocalnamespacesforfunctions,generators,
coroutines,comprehensions,andgeneratorexpressionsareoptimizedinthisfashion. Note: mostinterpreter
optimizationsareappliedtoallscopes,onlythoserelyingonaknownsetoflocalandnonlocalvariablenames
arerestrictedtooptimizedscopes.
package
A Python module which can contain submodules or recursively, subpackages. Technically, a package is a
Pythonmodulewitha__path__attribute.
80 AppendixA. Glossary

### 第85页

Seealsoregularpackageandnamespacepackage.
parameter
Anamedentityinafunction(ormethod)definitionthatspecifiesanargument (orinsomecases,arguments)
thatthefunctioncanaccept. Therearefivekindsofparameter:
• positional-or-keyword: specifiesanargumentthatcanbepassedeitherpositionallyorasakeywordargu-
ment. Thisisthedefaultkindofparameter,forexamplefooandbarinthefollowing:
def func(foo, bar=None): ...
• positional-only: specifiesanargumentthatcanbesuppliedonlybyposition. Positional-onlyparameters
canbedefinedbyincludinga/characterintheparameterlistofthefunctiondefinitionafterthem,for
exampleposonly1andposonly2inthefollowing:
def func(posonly1, posonly2, /, positional_or_keyword): ...
• keyword-only: specifiesanargumentthatcanbesuppliedonlybykeyword. Keyword-onlyparameters
canbedefinedbyincludingasinglevar-positionalparameterorbare*intheparameterlistofthefunction
definitionbeforethem,forexamplekw_only1andkw_only2inthefollowing:
def func(arg, *, kw_only1, kw_only2): ...
• var-positional: specifiesthatanarbitrarysequenceofpositionalargumentscanbeprovided(inaddition
toanypositionalargumentsalreadyacceptedbyotherparameters). Suchaparametercanbedefinedby
prependingtheparameternamewith*,forexampleargsinthefollowing:
def func(*args, **kwargs): ...
• var-keyword: specifiesthatarbitrarilymanykeywordargumentscanbeprovided(inadditiontoanykey-
wordargumentsalreadyacceptedbyotherparameters). Suchaparametercanbedefinedbyprepending
theparameternamewith**,forexamplekwargsintheexampleabove.
Parameters can specify both optional and required arguments, as well as default values for some optional
arguments.
Seealsotheargumentglossaryentry,theFAQquestiononthedifferencebetweenargumentsandparameters,
theinspect.Parameterclass,thefunctionsection,andPEP362.
pathentry
Asinglelocationontheimportpathwhichthepathbasedfinderconsultstofindmodulesforimporting.
pathentryfinder
A finder returned by a callable on sys.path_hooks (i.e. a path entry hook) which knows how to locate
modulesgivenapathentry.
Seeimportlib.abc.PathEntryFinderforthemethodsthatpathentryfindersimplement.
pathentryhook
Acallableonthesys.path_hookslistwhichreturnsapathentryfinderifitknowshowtofindmoduleson
aspecificpathentry.
pathbasedfinder
Oneofthedefaultmetapathfinderswhichsearchesanimportpathformodules.
path-likeobject
An object representing a file system path. A path-like object is either a str or bytes object representing
a path, or an object implementing the os.PathLike protocol. An object that supports the os.PathLike
protocol can be converted to a str or bytes file system path by calling the os.fspath() function; os.
fsdecode() and os.fsencode() can be used to guarantee a str or bytes result instead, respectively.
IntroducedbyPEP519.
PEP
PythonEnhancementProposal. APEPisadesigndocumentprovidinginformationtothePythoncommunity,
81

### 第86页

ordescribinganewfeatureforPythonoritsprocessesorenvironment. PEPsshouldprovideaconcisetechnical
specificationandarationaleforproposedfeatures.
PEPsareintendedtobetheprimarymechanismsforproposingmajornewfeatures,forcollectingcommunity
inputonanissue, andfordocumentingthedesigndecisionsthathavegoneintoPython. ThePEPauthoris
responsibleforbuildingconsensuswithinthecommunityanddocumentingdissentingopinions.
SeePEP1.
portion
A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package, as
definedinPEP420.
positionalargument
Seeargument.
provisionalAPI
A provisional API is one which has been deliberately excluded from the standard library’s backwards com-
patibility guarantees. While major changes to such interfaces are not expected, as long as they are marked
provisional, backwards incompatible changes (up to and including removal of the interface) may occur if
deemednecessarybycoredevelopers. Suchchangeswillnotbemadegratuitously–theywilloccuronlyif
seriousfundamentalflawsareuncoveredthatweremissedpriortotheinclusionoftheAPI.
Even for provisional APIs, backwards incompatible changes are seen as a “solution of last resort” - every
attemptwillstillbemadetofindabackwardscompatibleresolutiontoanyidentifiedproblems.
Thisprocessallowsthestandardlibrarytocontinuetoevolveovertime,withoutlockinginproblematicdesign
errorsforextendedperiodsoftime. SeePEP411formoredetails.
provisionalpackage
SeeprovisionalAPI.
Python3000
NicknameforthePython3.xreleaseline(coinedlongagowhenthereleaseofversion3wassomethinginthe
distantfuture.) Thisisalsoabbreviated“Py3k”.
Pythonic
AnideaorpieceofcodewhichcloselyfollowsthemostcommonidiomsofthePythonlanguage,ratherthan
implementingcodeusingconceptscommontootherlanguages. Forexample,acommonidiominPythonis
toloopoverallelementsofaniterableusingaforstatement. Manyotherlanguagesdon’thavethistypeof
construct,sopeopleunfamiliarwithPythonsometimesuseanumericalcounterinstead:
for i in range(len(food)):
print(food[i])
Asopposedtothecleaner,Pythonicmethod:
for piece in food:
print(piece)
qualifiedname
Adottednameshowingthe“path”fromamodule’sglobalscopetoaclass,functionormethoddefinedinthat
module, as defined in PEP 3155. For top-level functions and classes, the qualified name is the same as the
object’sname:
>>> class C:
... class D:
... def meth(self):
... pass
...
>>> C.__qualname__
'C'
>>> C.D.__qualname__
(continuesonnextpage)
82 AppendixA. Glossary

### 第87页

(continuedfrompreviouspage)
'C.D'
>>> C.D.meth.__qualname__
'C.D.meth'
Whenusedtorefertomodules,thefullyqualifiednamemeanstheentiredottedpathtothemodule,including
anyparentpackages,e.g. email.mime.text:
>>> import email.mime.text
>>> email.mime.text.__name__
'email.mime.text'
referencecount
Thenumberofreferencestoanobject. Whenthereferencecountofanobjectdropstozero,itisdeallocated.
Some objects are immortal and have reference counts that are never modified, and therefore the objects are
neverdeallocated. ReferencecountingisgenerallynotvisibletoPythoncode, butitisakeyelementofthe
CPythonimplementation. Programmerscancallthesys.getrefcount()functiontoreturnthereference
countforaparticularobject.
InCPython,referencecountsarenotconsideredtobestableorwell-definedvalues;thenumberofreferences
toanobject,andhowthatnumberisaffectedbyPythoncode,maybedifferentbetweenversions.
regularpackage
Atraditionalpackage,suchasadirectorycontainingan__init__.pyfile.
Seealsonamespacepackage.
REPL
Anacronymforthe“read–eval–printloop”,anothernamefortheinteractiveinterpretershell.
__slots__
Adeclarationinsideaclassthatsavesmemorybypre-declaringspaceforinstanceattributesandeliminating
instancedictionaries. Thoughpopular,thetechniqueissomewhattrickytogetrightandisbestreservedfor
rarecaseswheretherearelargenumbersofinstancesinamemory-criticalapplication.
sequence
An iterable which supports efficient element access using integer indices via the __getitem__() special
method and defines a __len__() method that returns the length of the sequence. Some built-in sequence
typesarelist,str,tuple,andbytes. Notethatdictalsosupports__getitem__()and__len__(),
but is considered a mapping rather than a sequence because the lookups use arbitrary hashable keys rather
thanintegers.
Thecollections.abc.Sequenceabstractbaseclassdefinesamuchricherinterfacethatgoesbeyondjust
__getitem__()and__len__(),addingcount(),index(),__contains__(),and__reversed__().
Types that implement this expanded interface can be registered explicitly using register(). For more
documentationonsequencemethodsgenerally,seeCommonSequenceOperations.
setcomprehension
Acompactwaytoprocessallorpartoftheelementsinaniterableandreturnasetwiththeresults. results
= {c for c in 'abracadabra' if c not in 'abc'}generatesthesetofstrings{'r', 'd'}. See
comprehensions.
singledispatch
Aformofgenericfunctiondispatchwheretheimplementationischosenbasedonthetypeofasingleargument.
slice
Anobjectusuallycontainingaportionofasequence. Asliceiscreatedusingthesubscriptnotation,[]with
colons between numbers when several are given, such as in variable_name[1:3:5]. The bracket (sub-
script)notationusessliceobjectsinternally.
softdeprecated
AsoftdeprecatedAPIshouldnotbeusedinnewcode,butitissafeforalreadyexistingcodetouseit. The
APIremainsdocumentedandtested,butwillnotbeenhancedfurther.
83

### 第88页

Softdeprecation,unlikenormaldeprecation,doesnotplanonremovingtheAPIandwillnotemitwarnings.
SeePEP387: SoftDeprecation.
specialmethod
AmethodthatiscalledimplicitlybyPythontoexecuteacertainoperationonatype,suchasaddition. Such
methodshavenamesstartingandendingwithdoubleunderscores. Specialmethodsaredocumentedinspe-
cialnames.
standardlibrary
Thecollectionofpackages,modulesandextensionmodulesdistributedasapartoftheofficialPythoninterpreter
package. Theexactmembershipofthecollectionmayvarybasedonplatform,availablesystemlibraries,or
othercriteria. Documentationcanbefoundatlibrary-index.
Seealsosys.stdlib_module_namesforalistofallpossiblestandardlibrarymodulenames.
statement
Astatementispartofasuite(a“block”ofcode). Astatementiseitheranexpressionoroneofseveralconstructs
withakeyword,suchasif,whileorfor.
statictypechecker
AnexternaltoolthatreadsPythoncodeandanalyzesit, lookingforissuessuchasincorrecttypes. Seealso
typehintsandthetypingmodule.
stdlib
Anabbreviationofstandardlibrary.
strongreference
In Python’s C API, a strong reference is a reference to an object which is owned by the code holding the
reference. ThestrongreferenceistakenbycallingPy_INCREF()whenthereferenceiscreatedandreleased
withPy_DECREF()whenthereferenceisdeleted.
ThePy_NewRef()functioncanbeusedtocreateastrongreferencetoanobject. Usually,thePy_DECREF()
functionmustbecalledonthestrongreferencebeforeexitingthescopeofthestrongreference,toavoidleaking
onereference.
Seealsoborrowedreference.
t-string
t-strings
StringliteralsprefixedwithtorTarecommonlycalled“t-strings”whichisshortfortemplatestringliterals.
textencoding
AstringinPythonisasequenceofUnicodecodepoints(inrangeU+0000–U+10FFFF).Tostoreortransfer
astring,itneedstobeserializedasasequenceofbytes.
Serializingastringintoasequenceofbytesisknownas“encoding”,andrecreatingthestringfromthesequence
ofbytesisknownas“decoding”.
Thereareavarietyofdifferenttextserializationcodecs,whicharecollectivelyreferredtoas“textencodings”.
textfile
Afileobjectabletoreadandwritestrobjects. Often,atextfileactuallyaccessesabyte-orienteddatastream
andhandlesthetextencodingautomatically. Examplesoftextfilesarefilesopenedintextmode('r'or'w'),
sys.stdin,sys.stdout,andinstancesofio.StringIO.
Seealsobinaryfileforafileobjectabletoreadandwritebytes-likeobjects.
threadstate
TheinformationusedbytheCPythonruntimetoruninanOSthread. Forexample,thisincludesthecurrent
exception,ifany,andthestateofthebytecodeinterpreter.
EachthreadstateisboundtoasingleOSthread,butthreadsmayhavemanythreadstatesavailable. Atmost,
oneofthemmaybeattachedatonce.
An attached thread state is required to call most of Python’s C API, unless a function explicitly documents
otherwise. Thebytecodeinterpreteronlyrunsunderanattachedthreadstate.
84 AppendixA. Glossary

### 第89页

Eachthreadstatebelongstoasingleinterpreter,buteachinterpretermayhavemanythreadstates,including
multipleforthesameOSthread. Threadstatesfrommultipleinterpretersmaybeboundtothesamethread,
butonlyonecanbeattachedinthatthreadatanygivenmoment.
SeeThreadStateandtheGlobalInterpreterLockformoreinformation.
token
A small unit of source code, generated by the lexical analyzer (also called the tokenizer). Names, numbers,
strings,operators,newlinesandsimilararerepresentedbytokens.
The tokenize module exposes Python’s lexical analyzer. The token module contains information on the
varioustypesoftokens.
triple-quotedstring
Astringwhichisboundbythreeinstancesofeitheraquotationmark(”)oranapostrophe(‘). Whiletheydon’t
provide any functionality not available with single-quoted strings, they are useful for a number of reasons.
Theyallowyoutoincludeunescapedsingleanddoublequoteswithinastringandtheycanspanmultiplelines
withouttheuseofthecontinuationcharacter,makingthemespeciallyusefulwhenwritingdocstrings.
type
ThetypeofaPythonobjectdetermineswhatkindofobjectitis;everyobjecthasatype. Anobject’stypeis
accessibleasits__class__attributeorcanberetrievedwithtype(obj).
typealias
Asynonymforatype,createdbyassigningthetypetoanidentifier.
Typealiasesareusefulforsimplifyingtypehints. Forexample:
def remove_gray_shades(
colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
pass
couldbemademorereadablelikethis:
Color = tuple[int, int, int]
def remove_gray_shades(colors: list[Color]) -> list[Color]:
pass
SeetypingandPEP484,whichdescribethisfunctionality.
typehint
Anannotationthatspecifiestheexpectedtypeforavariable,aclassattribute,orafunctionparameterorreturn
value.
TypehintsareoptionalandarenotenforcedbyPythonbuttheyareusefultostatictypecheckers. Theycan
alsoaidIDEswithcodecompletionandrefactoring.
Type hints of global variables, class attributes, and functions, but not local variables, can be accessed using
typing.get_type_hints().
SeetypingandPEP484,whichdescribethisfunctionality.
universalnewlines
Amannerofinterpretingtextstreamsinwhichallofthefollowingarerecognizedasendingaline: theUnix
end-of-lineconvention'\n',theWindowsconvention'\r\n',andtheoldMacintoshconvention'\r'. See
PEP278andPEP3116,aswellasbytes.splitlines()foranadditionaluse.
variableannotation
Anannotationofavariableoraclassattribute.
Whenannotatingavariableoraclassattribute,assignmentisoptional:
class C:
field: 'annotation'
85

### 第90页

Variableannotationsareusuallyusedfortypehints: forexamplethisvariableisexpectedtotakeintvalues:
count: int = 0
Variableannotationsyntaxisexplainedinsectionannassign.
Seefunctionannotation,PEP484andPEP526,whichdescribethisfunctionality. Alsoseeannotations-howto
forbestpracticesonworkingwithannotations.
virtualenvironment
AcooperativelyisolatedruntimeenvironmentthatallowsPythonusersandapplicationstoinstallandupgrade
PythondistributionpackageswithoutinterferingwiththebehaviourofotherPythonapplicationsrunningon
thesamesystem.
Seealsovenv.
virtualmachine
Acomputerdefinedentirelyinsoftware. Python’svirtualmachineexecutesthebytecodeemittedbythebyte-
codecompiler.
walrusoperator
Alight-heartedwaytorefertotheassignmentexpressionoperator:=becauseitlooksabitlikeawalrusifyou
turnyourhead.
ZenofPython
ListingofPythondesignprinciplesandphilosophiesthatarehelpfulinunderstandingandusingthelanguage.
Thelistingcanbefoundbytyping“import this”attheinteractiveprompt.
86 AppendixA. Glossary

### 第91页

APPENDIX
B
ABOUT THIS DOCUMENTATION
Python’sdocumentationisgeneratedfromreStructuredTextsourcesusingSphinx,adocumentationgeneratororigi-
nallycreatedforPythonandnowmaintainedasanindependentproject.
Development of the documentation and its toolchain is an entirely volunteer effort, just like Python itself. If you
wanttocontribute,pleasetakealookatthereporting-bugspageforinformationonhowtodoso. Newvolunteers
arealwayswelcome!
Manythanksgoto:
• FredL.Drake,Jr.,thecreatoroftheoriginalPythondocumentationtoolsetandauthorofmuchofthecontent;
• theDocutilsprojectforcreatingreStructuredTextandtheDocutilssuite;
• FredrikLundhforhisAlternativePythonReferenceprojectfromwhichSphinxgotmanygoodideas.
B.1 Contributors to the Python documentation
ManypeoplehavecontributedtothePythonlanguage,thePythonstandardlibrary,andthePythondocumentation.
SeeMisc/ACKSinthePythonsourcedistributionforapartiallistofcontributors.
ItisonlywiththeinputandcontributionsofthePythoncommunitythatPythonhassuchwonderfuldocumentation
–ThankYou!
87

### 第92页

88 AppendixB. Aboutthisdocumentation

### 第93页

APPENDIX
C
HISTORY AND LICENSE
C.1 History of the software
Pythonwascreatedintheearly1990sbyGuidovanRossumatStichtingMathematischCentrum(CWI,seehttps:
//www.cwi.nl)intheNetherlandsasasuccessorofalanguagecalledABC.GuidoremainsPython’sprincipalauthor,
althoughitincludesmanycontributionsfromothers.
In1995,GuidocontinuedhisworkonPythonattheCorporationforNationalResearchInitiatives(CNRI,seehttps:
//www.cnri.reston.va.us)inReston,Virginiawherehereleasedseveralversionsofthesoftware.
InMay2000,GuidoandthePythoncoredevelopmentteammovedtoBeOpen.comtoformtheBeOpenPythonLabs
team. InOctoberofthesameyear,thePythonLabsteammovedtoDigitalCreations,whichbecameZopeCorpo-
ration. In2001,thePythonSoftwareFoundation(PSF,seehttps://www.python.org/psf/)wasformed,anon-profit
organization created specifically to own Python-related Intellectual Property. Zope Corporation was a sponsoring
memberofthePSF.
AllPythonreleasesareOpenSource(seehttps://opensource.orgfortheOpenSourceDefinition). Historically,most,
butnotall,PythonreleaseshavealsobeenGPL-compatible;thetablebelowsummarizesthevariousreleases.
Release Derivedfrom Year Owner GPL-compatible? (1)
0.9.0thru1.2 n/a 1991-1995 CWI yes
1.3thru1.5.2 1.2 1995-1999 CNRI yes
1.6 1.5.2 2000 CNRI no
2.0 1.6 2000 BeOpen.com no
1.6.1 1.6 2001 CNRI yes(2)
2.1 2.0+1.6.1 2001 PSF no
2.0.1 2.0+1.6.1 2001 PSF yes
2.1.1 2.1+2.0.1 2001 PSF yes
2.1.2 2.1.1 2002 PSF yes
2.1.3 2.1.2 2002 PSF yes
2.2andabove 2.1.1 2001-now PSF yes
(cid:174) Note
(1) GPL-compatibledoesn’tmeanthatwe’redistributingPythonundertheGPL.AllPythonlicenses,unlike
the GPL, let you distribute a modified version without making your changes open source. The GPL-
compatible licenses make it possible to combine Python with other software that is released under the
GPL;theothersdon’t.
(2) AccordingtoRichardStallman,1.6.1isnotGPL-compatible,becauseitslicensehasachoiceoflawclause.
AccordingtoCNRI,however, Stallman’slawyerhastoldCNRI’slawyerthat1.6.1is“notincompatible”
withtheGPL.
ThankstothemanyoutsidevolunteerswhohaveworkedunderGuido’sdirectiontomakethesereleasespossible.
89

| Release | Derivedfrom | Year | Owner | GPL-compatible? (1) |
| --- | --- | --- | --- | --- |
| 0.9.0thru1.2 | n/a | 1991-1995 | CWI | yes |
| 1.3thru1.5.2 | 1.2 | 1995-1999 | CNRI | yes |
| 1.6 | 1.5.2 | 2000 | CNRI | no |
| 2.0 | 1.6 | 2000 | BeOpen.com | no |
| 1.6.1 | 1.6 | 2001 | CNRI | yes(2) |
| 2.1 | 2.0+1.6.1 | 2001 | PSF | no |
| 2.0.1 | 2.0+1.6.1 | 2001 | PSF | yes |
| 2.1.1 | 2.1+2.0.1 | 2001 | PSF | yes |
| 2.1.2 | 2.1.1 | 2002 | PSF | yes |
| 2.1.3 | 2.1.2 | 2002 | PSF | yes |
| 2.2andabove | 2.1.1 | 2001-now | PSF | yes |

### 第94页

C.2 Terms and conditions for accessing or otherwise using Python
PythonsoftwareanddocumentationarelicensedunderthePythonSoftwareFoundationLicenseVersion2.
StartingwithPython3.8.6,examples,recipes,andothercodeinthedocumentationareduallicensedunderthePSF
LicenseVersion2andtheZero-ClauseBSDlicense.
SomesoftwareincorporatedintoPythonisunderdifferentlicenses. Thelicensesarelistedwithcodefallingunder
thatlicense. SeeLicensesandAcknowledgementsforIncorporatedSoftwareforanincompletelistoftheselicenses.
C.2.1 PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
the Individual or Organization ("Licensee") accessing and otherwise using this
software ("Python") in source or binary form and its associated documentation.
2. Subject to the terms and conditions of this License Agreement, PSF hereby
grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
analyze, test, perform and/or display publicly, prepare derivative works,
distribute, and otherwise use Python alone or in any derivative
version, provided, however, that PSF's License Agreement and PSF's notice of
copyright, i.e., "Copyright © 2001 Python Software Foundation; All Rights
Reserved" are retained in Python alone or in any derivative version
prepared by Licensee.
3. In the event Licensee prepares a derivative work that is based on or
incorporates Python or any part thereof, and wants to make the
derivative work available to others as provided herein, then Licensee hereby
agrees to include in any such work a brief summary of the changes made to␣
,→Python.
4. PSF is making Python available to Licensee on an "AS IS" basis.
PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF
EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
USE OF PYTHON WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON, OR ANY DERIVATIVE
THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
6. This License Agreement will automatically terminate upon a material breach of
its terms and conditions.
7. Nothing in this License Agreement shall be deemed to create any relationship
of agency, partnership, or joint venture between PSF and Licensee. This License
Agreement does not grant permission to use PSF trademarks or trade name in a
trademark sense to endorse or promote products or services of Licensee, or any
third party.
8. By copying, installing or otherwise using Python, Licensee agrees
to be bound by the terms and conditions of this License Agreement.
90 AppendixC. HistoryandLicense

### 第95页

C.2.2 BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0
BEOPENPYTHONOPENSOURCELICENSEAGREEMENTVERSION1
1. This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an office at
160 Saratoga Avenue, Santa Clara, CA 95051, and the Individual or Organization
("Licensee") accessing and otherwise using this software in source or binary
form and its associated documentation ("the Software").
2. Subject to the terms and conditions of this BeOpen Python License Agreement,
BeOpen hereby grants Licensee a non-exclusive, royalty-free, world-wide license
to reproduce, analyze, test, perform and/or display publicly, prepare derivative
works, distribute, and otherwise use the Software alone or in any derivative
version, provided, however, that the BeOpen Python License is retained in the
Software, alone or in any derivative version prepared by Licensee.
3. BeOpen is making the Software available to Licensee on an "AS IS" basis.
BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF
EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
USE OF THE SOFTWARE WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
4. BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE SOFTWARE FOR
ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF USING,
MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY DERIVATIVE THEREOF, EVEN IF
ADVISED OF THE POSSIBILITY THEREOF.
5. This License Agreement will automatically terminate upon a material breach of
its terms and conditions.
6. This License Agreement shall be governed by and interpreted in all respects
by the law of the State of California, excluding conflict of law provisions.
Nothing in this License Agreement shall be deemed to create any relationship of
agency, partnership, or joint venture between BeOpen and Licensee. This License
Agreement does not grant permission to use BeOpen trademarks or trade names in a
trademark sense to endorse or promote products or services of Licensee, or any
third party. As an exception, the "BeOpen Python" logos available at
http://www.pythonlabs.com/logos.html may be used according to the permissions
granted on that web page.
7. By copying, installing or otherwise using the software, Licensee agrees to be
bound by the terms and conditions of this License Agreement.
C.2.3 CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1
1. This LICENSE AGREEMENT is between the Corporation for National Research
Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191
("CNRI"), and the Individual or Organization ("Licensee") accessing and
otherwise using Python 1.6.1 software in source or binary form and its
associated documentation.
2. Subject to the terms and conditions of this License Agreement, CNRI hereby
grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
analyze, test, perform and/or display publicly, prepare derivative works,
distribute, and otherwise use Python 1.6.1 alone or in any derivative version,
provided, however, that CNRI's License Agreement and CNRI's notice of copyright,
i.e., "Copyright © 1995-2001 Corporation for National Research Initiatives; All
(continuesonnextpage)
C.2. TermsandconditionsforaccessingorotherwiseusingPython 91

### 第96页

(continuedfrompreviouspage)
Rights Reserved" are retained in Python 1.6.1 alone or in any derivative version
prepared by Licensee. Alternately, in lieu of CNRI's License Agreement,
Licensee may substitute the following text (omitting the quotes): "Python 1.6.1
is made available subject to the terms and conditions in CNRI's License
Agreement. This Agreement together with Python 1.6.1 may be located on the
internet using the following unique, persistent identifier (known as a handle):
1895.22/1013. This Agreement may also be obtained from a proxy server on the
internet using the following URL: http://hdl.handle.net/1895.22/1013".
3. In the event Licensee prepares a derivative work that is based on or
incorporates Python 1.6.1 or any part thereof, and wants to make the derivative
work available to others as provided herein, then Licensee hereby agrees to
include in any such work a brief summary of the changes made to Python 1.6.1.
4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS" basis. CNRI
MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED. BY WAY OF EXAMPLE,
BUT NOT LIMITATION, CNRI MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY
OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF
PYTHON 1.6.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.
5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 1.6.1 FOR
ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1, OR ANY DERIVATIVE
THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.
6. This License Agreement will automatically terminate upon a material breach of
its terms and conditions.
7. This License Agreement shall be governed by the federal intellectual property
law of the United States, including without limitation the federal copyright
law, and, to the extent such U.S. federal law does not apply, by the law of the
Commonwealth of Virginia, excluding Virginia's conflict of law provisions.
Notwithstanding the foregoing, with regard to derivative works based on Python
1.6.1 that incorporate non-separable material that was previously distributed
under the GNU General Public License (GPL), the law of the Commonwealth of
Virginia shall govern this License Agreement only as to issues arising under or
with respect to Paragraphs 4, 5, and 7 of this License Agreement. Nothing in
this License Agreement shall be deemed to create any relationship of agency,
partnership, or joint venture between CNRI and Licensee. This License Agreement
does not grant permission to use CNRI trademarks or trade name in a trademark
sense to endorse or promote products or services of Licensee, or any third
party.
8. By clicking on the "ACCEPT" button where indicated, or by copying, installing
or otherwise using Python 1.6.1, Licensee agrees to be bound by the terms and
conditions of this License Agreement.
C.2.4 CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2
Copyright © 1991 - 1995, Stichting Mathematisch Centrum Amsterdam, The
Netherlands. All rights reserved.
Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted, provided that
the above copyright notice appear in all copies and that both that copyright
(continuesonnextpage)
92 AppendixC. HistoryandLicense

### 第97页

(continuedfrompreviouspage)
notice and this permission notice appear in supporting documentation, and that
the name of Stichting Mathematisch Centrum or CWI not be used in advertising or
publicity pertaining to distribution of the software without specific, written
prior permission.
STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT
OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
SOFTWARE.
C.2.5 ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTA-
TION
Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
C.3 Licenses and Acknowledgements for Incorporated Software
Thissectionisanincomplete,butgrowinglistoflicensesandacknowledgementsforthird-partysoftwareincorporated
inthePythondistribution.
C.3.1 Mersenne Twister
The_randomCextensionunderlyingtherandommoduleincludescodebasedonadownloadfromhttp://www.math.
sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/emt19937ar.html. Thefollowingaretheverbatimcommentsfromthe
originalcode:
A C-program for MT19937, with initialization improved 2002/1/26.
Coded by Takuji Nishimura and Makoto Matsumoto.
Before using, initialize the state by using init_genrand(seed)
or init_by_array(init_key, key_length).
Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
(continuesonnextpage)
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 93

### 第98页

(continuedfrompreviouspage)
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. The names of its contributors may not be used to endorse or promote
products derived from this software without specific prior written
permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
Any feedback is very welcome.
http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)
C.3.2 Sockets
Thesocketmoduleusesthefunctions,getaddrinfo(),andgetnameinfo(),whicharecodedinseparatesource
filesfromtheWIDEProject,https://www.wide.ad.jp/.
Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. Neither the name of the project nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
94 AppendixC. HistoryandLicense

### 第99页

C.3.3 Asynchronous socket services
Thetest.support.asynchatandtest.support.asyncoremodulescontainthefollowingnotice:
Copyright 1996 by Sam Rushing
All Rights Reserved
Permission to use, copy, modify, and distribute this software and
its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that copyright notice and this permission
notice appear in supporting documentation, and that the name of Sam
Rushing not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior
permission.
SAM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
C.3.4 Cookie management
Thehttp.cookiesmodulecontainsthefollowingnotice:
Copyright 2000 by Timothy O'Malley <timo@alum.mit.edu>
All Rights Reserved
Permission to use, copy, modify, and distribute this software
and its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that copyright notice and this permission
notice appear in supporting documentation, and that the name of
Timothy O'Malley not be used in advertising or publicity
pertaining to distribution of the software without specific, written
prior permission.
Timothy O'Malley DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS, IN NO EVENT SHALL Timothy O'Malley BE LIABLE FOR
ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
C.3.5 Execution tracing
Thetracemodulecontainsthefollowingnotice:
portions copyright 2001, Autonomous Zones Industries, Inc., all rights...
err... reserved and offered to the public under the terms of the
Python 2.2 license.
(continuesonnextpage)
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 95

### 第100页

(continuedfrompreviouspage)
Author: Zooko O'Whielacronx
http://zooko.com/
mailto:zooko@zooko.com
Copyright 2000, Mojam Media, Inc., all rights reserved.
Author: Skip Montanaro
Copyright 1999, Bioreason, Inc., all rights reserved.
Author: Andrew Dalke
Copyright 1995-1997, Automatrix, Inc., all rights reserved.
Author: Skip Montanaro
Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.
Permission to use, copy, modify, and distribute this Python software and
its associated documentation for any purpose without fee is hereby
granted, provided that the above copyright notice appears in all copies,
and that both that copyright notice and this permission notice appear in
supporting documentation, and that the name of neither Automatrix,
Bioreason or Mojam Media be used in advertising or publicity pertaining to
distribution of the software without specific, written prior permission.
C.3.6 UUencode and UUdecode functions
Theuucodeccontainsthefollowingnotice:
Copyright 1994 by Lance Ellinghouse
Cathedral City, California Republic, United States of America.
All Rights Reserved
Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Lance Ellinghouse
not be used in advertising or publicity pertaining to distribution
of the software without specific, written prior permission.
LANCE ELLINGHOUSE DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL LANCE ELLINGHOUSE CENTRUM BE LIABLE
FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
Modified by Jack Jansen, CWI, July 1995:
- Use binascii module to do the actual line-by-line conversion
between ascii and binary. This results in a 1000-fold speedup. The C
version is still 5 times faster, though.
- Arguments more compliant with Python standard
96 AppendixC. HistoryandLicense

### 第101页

C.3.7 XML Remote Procedure Calls
Thexmlrpc.clientmodulecontainsthefollowingnotice:
The XML-RPC client interface is
Copyright (c) 1999-2002 by Secret Labs AB
Copyright (c) 1999-2002 by Fredrik Lundh
By obtaining, using, and/or copying this software and/or its
associated documentation, you agree that you have read, understood,
and will comply with the following terms and conditions:
Permission to use, copy, modify, and distribute this software and
its associated documentation for any purpose and without fee is
hereby granted, provided that the above copyright notice appears in
all copies, and that both that copyright notice and this permission
notice appear in supporting documentation, and that the name of
Secret Labs AB or the author not be used in advertising or publicity
pertaining to distribution of the software without specific, written
prior permission.
SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-
ABILITY AND FITNESS. IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR
BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
OF THIS SOFTWARE.
C.3.8 test_epoll
Thetest.test_epollmodulecontainsthefollowingnotice:
Copyright (c) 2001-2006 Twisted Matrix Laboratories.
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 97

### 第102页

C.3.9 Select kqueue
Theselectmodulecontainsthefollowingnoticeforthekqueueinterface:
Copyright (c) 2000 Doug White, 2006 James Knight, 2007 Christian Heimes
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
C.3.10 SipHash24
ThefilePython/pyhash.ccontainsMarekMajkowski’implementationofDanBernstein’sSipHash24algorithm.
Itcontainsthefollowingnote:
<MIT License>
Copyright (c) 2013 Marek Majkowski <marek@popcount.org>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
</MIT License>
Original location:
https://github.com/majek/csiphash/
Solution inspired by code from:
Samuel Neves (supercop/crypto_auth/siphash24/little)
djb (supercop/crypto_auth/siphash24/little2)
Jean-Philippe Aumasson (https://131002.net/siphash/siphash24.c)
98 AppendixC. HistoryandLicense

### 第103页

C.3.11 strtod and dtoa
ThefilePython/dtoa.c,whichsuppliesCfunctionsdtoaandstrtodforconversionofCdoublestoandfromstrings,
isderivedfromthefileofthesamenamebyDavidM.Gay, currentlyavailablefromhttps://web.archive.org/web/
20220517033456/http://www.netlib.org/fp/dtoa.c. The original file, as retrieved on March 16, 2009, contains the
followingcopyrightandlicensingnotice:
/****************************************************************
*
* The author of this software is David M. Gay.
*
* Copyright (c) 1991, 2000, 2001 by Lucent Technologies.
*
* Permission to use, copy, modify, and distribute this software for any
* purpose without fee is hereby granted, provided that this entire notice
* is included in all copies of any software which is or includes a copy
* or modification of this software and in all copies of the supporting
* documentation for such software.
*
* THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
* WARRANTY. IN PARTICULAR, NEITHER THE AUTHOR NOR LUCENT MAKES ANY
* REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
* OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
*
***************************************************************/
C.3.12 OpenSSL
Themoduleshashlib,posixandsslusetheOpenSSLlibraryforaddedperformanceifmadeavailablebythe
operatingsystem. Additionally,theWindowsandmacOSinstallersforPythonmayincludeacopyoftheOpenSSL
libraries,soweincludeacopyoftheOpenSSLlicensehere. FortheOpenSSL3.0release,andlaterreleasesderived
fromthat,theApacheLicensev2applies:
Apache License
Version 2.0, January 2004
https://www.apache.org/licenses/
TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
1. Definitions.
"License" shall mean the terms and conditions for use, reproduction,
and distribution as defined by Sections 1 through 9 of this document.
"Licensor" shall mean the copyright owner or entity authorized by
the copyright owner that is granting the License.
"Legal Entity" shall mean the union of the acting entity and all
other entities that control, are controlled by, or are under common
control with that entity. For the purposes of this definition,
"control" means (i) the power, direct or indirect, to cause the
direction or management of such entity, whether by contract or
otherwise, or (ii) ownership of fifty percent (50%) or more of the
outstanding shares, or (iii) beneficial ownership of such entity.
"You" (or "Your") shall mean an individual or Legal Entity
exercising permissions granted by this License.
(continuesonnextpage)
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 99

### 第104页

(continuedfrompreviouspage)
"Source" form shall mean the preferred form for making modifications,
including but not limited to software source code, documentation
source, and configuration files.
"Object" form shall mean any form resulting from mechanical
transformation or translation of a Source form, including but
not limited to compiled object code, generated documentation,
and conversions to other media types.
"Work" shall mean the work of authorship, whether in Source or
Object form, made available under the License, as indicated by a
copyright notice that is included in or attached to the work
(an example is provided in the Appendix below).
"Derivative Works" shall mean any work, whether in Source or Object
form, that is based on (or derived from) the Work and for which the
editorial revisions, annotations, elaborations, or other modifications
represent, as a whole, an original work of authorship. For the purposes
of this License, Derivative Works shall not include works that remain
separable from, or merely link (or bind by name) to the interfaces of,
the Work and Derivative Works thereof.
"Contribution" shall mean any work of authorship, including
the original version of the Work and any modifications or additions
to that Work or Derivative Works thereof, that is intentionally
submitted to Licensor for inclusion in the Work by the copyright owner
or by an individual or Legal Entity authorized to submit on behalf of
the copyright owner. For the purposes of this definition, "submitted"
means any form of electronic, verbal, or written communication sent
to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems,
and issue tracking systems that are managed by, or on behalf of, the
Licensor for the purpose of discussing and improving the Work, but
excluding communication that is conspicuously marked or otherwise
designated in writing by the copyright owner as "Not a Contribution."
"Contributor" shall mean Licensor and any individual or Legal Entity
on behalf of whom a Contribution has been received by Licensor and
subsequently incorporated within the Work.
2. Grant of Copyright License. Subject to the terms and conditions of
this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
copyright license to reproduce, prepare Derivative Works of,
publicly display, publicly perform, sublicense, and distribute the
Work and such Derivative Works in Source or Object form.
3. Grant of Patent License. Subject to the terms and conditions of
this License, each Contributor hereby grants to You a perpetual,
worldwide, non-exclusive, no-charge, royalty-free, irrevocable
(except as stated in this section) patent license to make, have made,
use, offer to sell, sell, import, and otherwise transfer the Work,
where such license applies only to those patent claims licensable
by such Contributor that are necessarily infringed by their
Contribution(s) alone or by combination of their Contribution(s)
with the Work to which such Contribution(s) was submitted. If You
(continuesonnextpage)
100 AppendixC. HistoryandLicense

### 第105页

(continuedfrompreviouspage)
institute patent litigation against any entity (including a
cross-claim or counterclaim in a lawsuit) alleging that the Work
or a Contribution incorporated within the Work constitutes direct
or contributory patent infringement, then any patent licenses
granted to You under this License for that Work shall terminate
as of the date such litigation is filed.
4. Redistribution. You may reproduce and distribute copies of the
Work or Derivative Works thereof in any medium, with or without
modifications, and in Source or Object form, provided that You
meet the following conditions:
(a) You must give any other recipients of the Work or
Derivative Works a copy of this License; and
(b) You must cause any modified files to carry prominent notices
stating that You changed the files; and
(c) You must retain, in the Source form of any Derivative Works
that You distribute, all copyright, patent, trademark, and
attribution notices from the Source form of the Work,
excluding those notices that do not pertain to any part of
the Derivative Works; and
(d) If the Work includes a "NOTICE" text file as part of its
distribution, then any Derivative Works that You distribute must
include a readable copy of the attribution notices contained
within such NOTICE file, excluding those notices that do not
pertain to any part of the Derivative Works, in at least one
of the following places: within a NOTICE text file distributed
as part of the Derivative Works; within the Source form or
documentation, if provided along with the Derivative Works; or,
within a display generated by the Derivative Works, if and
wherever such third-party notices normally appear. The contents
of the NOTICE file are for informational purposes only and
do not modify the License. You may add Your own attribution
notices within Derivative Works that You distribute, alongside
or as an addendum to the NOTICE text from the Work, provided
that such additional attribution notices cannot be construed
as modifying the License.
You may add Your own copyright statement to Your modifications and
may provide additional or different license terms and conditions
for use, reproduction, or distribution of Your modifications, or
for any such Derivative Works as a whole, provided Your use,
reproduction, and distribution of the Work otherwise complies with
the conditions stated in this License.
5. Submission of Contributions. Unless You explicitly state otherwise,
any Contribution intentionally submitted for inclusion in the Work
by You to the Licensor shall be under the terms and conditions of
this License, without any additional terms or conditions.
Notwithstanding the above, nothing herein shall supersede or modify
the terms of any separate license agreement you may have executed
with Licensor regarding such Contributions.
(continuesonnextpage)
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 101

### 第106页

(continuedfrompreviouspage)
6. Trademarks. This License does not grant permission to use the trade
names, trademarks, service marks, or product names of the Licensor,
except as required for reasonable and customary use in describing the
origin of the Work and reproducing the content of the NOTICE file.
7. Disclaimer of Warranty. Unless required by applicable law or
agreed to in writing, Licensor provides the Work (and each
Contributor provides its Contributions) on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied, including, without limitation, any warranties or conditions
of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
PARTICULAR PURPOSE. You are solely responsible for determining the
appropriateness of using or redistributing the Work and assume any
risks associated with Your exercise of permissions under this License.
8. Limitation of Liability. In no event and under no legal theory,
whether in tort (including negligence), contract, or otherwise,
unless required by applicable law (such as deliberate and grossly
negligent acts) or agreed to in writing, shall any Contributor be
liable to You for damages, including any direct, indirect, special,
incidental, or consequential damages of any character arising as a
result of this License or out of the use or inability to use the
Work (including but not limited to damages for loss of goodwill,
work stoppage, computer failure or malfunction, or any and all
other commercial damages or losses), even if such Contributor
has been advised of the possibility of such damages.
9. Accepting Warranty or Additional Liability. While redistributing
the Work or Derivative Works thereof, You may choose to offer,
and charge a fee for, acceptance of support, warranty, indemnity,
or other liability obligations and/or rights consistent with this
License. However, in accepting such obligations, You may act only
on Your own behalf and on Your sole responsibility, not on behalf
of any other Contributor, and only if You agree to indemnify,
defend, and hold each Contributor harmless for any liability
incurred by, or claims asserted against, such Contributor by reason
of your accepting any such warranty or additional liability.
END OF TERMS AND CONDITIONS
C.3.13 expat
The pyexpat extension is built using an included copy of the expat sources unless the build is configured
--with-system-expat:
Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
and Clark Cooper
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
(continuesonnextpage)
102 AppendixC. HistoryandLicense

### 第107页

(continuedfrompreviouspage)
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
C.3.14 libffi
The_ctypesCextensionunderlyingthectypesmoduleisbuiltusinganincludedcopyofthelibffisourcesunless
thebuildisconfigured--with-system-libffi:
Copyright (c) 1996-2008 Red Hat, Inc and others.
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
C.3.15 zlib
Thezlibextensionisbuiltusinganincludedcopyofthezlibsourcesifthezlibversionfoundonthesystemistoo
oldtobeusedforthebuild:
Copyright (C) 1995-2011 Jean-loup Gailly and Mark Adler
This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.
Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:
1. The origin of this software must not be misrepresented; you must not
claim that you wrote the original software. If you use this software
in a product, an acknowledgment in the product documentation would be
(continuesonnextpage)
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 103

### 第108页

(continuedfrompreviouspage)
appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.
Jean-loup Gailly Mark Adler
jloup@gzip.org madler@alumni.caltech.edu
C.3.16 cfuhash
Theimplementationofthehashtableusedbythetracemallocisbasedonthecfuhashproject:
Copyright (c) 2005 Don Owens
All rights reserved.
This code is released under the BSD license:
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided
with the distribution.
* Neither the name of the author nor the names of its
contributors may be used to endorse or promote products derived
from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
C.3.17 libmpdec
The_decimalCextensionunderlyingthedecimalmoduleisbuiltusinganincludedcopyofthelibmpdeclibrary
unlessthebuildisconfigured--with-system-libmpdec:
Copyright (c) 2008-2020 Stefan Krah. All rights reserved.
Redistribution and use in source and binary forms, with or without
(continuesonnextpage)
104 AppendixC. HistoryandLicense

### 第109页

(continuedfrompreviouspage)
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.
C.3.18 W3C C14N test suite
TheC14N2.0testsuiteinthetestpackage(Lib/test/xmltestdata/c14n-20/)wasretrievedfromtheW3C
websiteathttps://www.w3.org/TR/xml-c14n2-testcases/andisdistributedunderthe3-clauseBSDlicense:
Copyright (c) 2013 W3C(R) (MIT, ERCIM, Keio, Beihang),
All Rights Reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
* Redistributions of works must retain the original copyright notice,
this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
* Neither the name of the W3C nor the names of its contributors may be
used to endorse or promote products derived from this work without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 105

### 第110页

C.3.19 mimalloc
MITLicense:
Copyright (c) 2018-2021 Microsoft Corporation, Daan Leijen
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
C.3.20 asyncio
Partsoftheasynciomoduleareincorporatedfromuvloop0.16,whichisdistributedundertheMITlicense:
Copyright (c) 2015-2021 MagicStack Inc. http://magic.io
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
C.3.21 Global Unbounded Sequences (GUS)
The file Python/qsbr.c is adapted from FreeBSD’s “Global Unbounded Sequences” safe memory reclamation
schemeinsubr_smr.c. Thefileisdistributedunderthe2-ClauseBSDLicense:
Copyright (c) 2019,2020 Jeffrey Roberson <jeff@FreeBSD.org>
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
(continuesonnextpage)
106 AppendixC. HistoryandLicense

### 第111页

(continuedfrompreviouspage)
are met:
1. Redistributions of source code must retain the above copyright
notice unmodified, this list of conditions, and the following
disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
C.3.22 Zstandard bindings
ZstandardbindingsinModules/_zstdandLib/compression/zstdarebasedoncodefromthepyzstdlibrary,
copyrightMaLinandcontributors. Thepyzstdcodeisdistributedunderthe3-ClauseBSDLicense:
Copyright (c) 2020-present, Ma Lin and contributors.
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 107

### 第112页

108 AppendixC. HistoryandLicense

### 第113页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
109

### 第114页

110 AppendixD. Copyright

### 第115页

INDEX
Non-alphabetical
current context,73
...,69 cyclic isolate,73
ellipsis literal,69
D
>>>,69
__future__,75 deallocation, object,50
__slots__,83 decorator,73
descriptor,73
A
dictionary,73
abstract base class,69 dictionary comprehension,73
annotate function,69 dictionary view,73
annotation,69 docstring,73
argument,69 duck-typing,74
asynchronous context manager,70 dunder,74
asynchronous generator,70
E
asynchronous generator iterator,70
asynchronous iterable,70 EAFP,74
asynchronous iterator,70 environment variable
attached thread state,70 PYTHON_GIL,76
attribute,70 evaluate function,74
awaitable,71 expression,74
extension module,74
B
F
BDFL,71
binary file,71 f-string,74
borrowed reference,71 f-strings,74
built-in function file object,74
repr,52 file-like object,74
bytecode,71 filesystem encoding and error handler,74
bytes-like object,71 finalization, of objects,50
finder,75
C floor division,75
callable,71 Fortran contiguous,72
callback,71 free threading,75
C-contiguous,72 free variable,75
class,71
function,75
class variable,71 function annotation,75
closure variable,72
G
complex number,72
context,72 garbage collection,75
context management protocol,72 generator,75
context manager,72 generator expression,76
context variable,72 generator iterator,76
contiguous,72 generic function,76
coroutine,72 generic type,76
coroutine function,72 GIL,76
CPython,73 global interpreter lock,76
111

### 第116页

H
optimized scope,80
hash-based pyc,76
P
hashable,76
package,80
I
parameter,81
IDLE,77 path based finder,81
immortal,77 path entry,81
immutable,77 path entry finder,81
import path,77 path entry hook,81
importer,77 path-like object,81
importing,77 PEP,81
interactive,77 Philbrick, Geoff,15
interpreted,77 portion,82
interpreter shutdown,77 positional argument,82
iterable,77 provisional API,82
iterator,78 provisional package,82
Py_NO_LINK_LIB(Cmacro),59
K
PyArg_ParseTuple(Cfunction),14
key function,78
PyArg_ParseTupleAndKeywords(Cfunction),15
keyword argument,78
PyErr_Fetch(Cfunction),51
PyErr_Restore(Cfunction),51
L PyObject_CallObject(Cfunction),12
Python 3000,82
lambda,78
Python Enhancement Proposals
LBYL,78
PEP 1,82
lexical analyzer,78
PEP 238,75
list,78
PEP 278,85
list comprehension,78
PEP 302,79
loader,78
PEP 343,72
locale encoding,79
PEP 362,70,81
M PEP 411,82
PEP 420,80,82
magic
PEP 442,19,52
method,79
PEP 443,76
magic method,79
PEP 483,76
mapping,79
PEP 484,69,75,76,85,86
meta path finder,79
PEP 489,5
metaclass,79
PEP 492,7073
method,79
PEP 498,74
magic,79
PEP 519,81
special,84
PEP 525,70
method resolution order,79
PEP 526,69,86
module,79
PEP 585,76
module spec,79
PEP 649,69
MRO,79
PEP 683,77
mutable,79
PEP 703,75,76
N PEP 3116,85
PEP 3155,82
named tuple,80
PYTHON_GIL,76
namespace,80
Pythonic,82
namespace package,80
nested scope,80 Q
new-style class,80
qualified name,82
O
R
object,80
reference count,83
deallocation,50
regular package,83
finalization,50
REPL,83
112 Index

### 第117页

repr
built-in function,52
S
sequence,83
set comprehension,83
single dispatch,83
slice,83
soft deprecated,83
special
method,84
special method,84
standard library,84
statement,84
static type checker,84
stdlib,84
string
object representation,52
strong reference,84
T
t-string,84
t-strings,84
text encoding,84
text file,84
thread state,84
token,85
triple-quoted string,85
type,85
type alias,85
type hint,85
U
universal newlines,85
V
variable annotation,85
virtual environment,86
virtual machine,86
W
walrus operator,86
Z
Zen of Python,86
Index 113

