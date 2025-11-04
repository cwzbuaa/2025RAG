### 第1页

Installing Python Modules
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 Keyterms 3
2 Basicusage 5
3 HowdoI…? 7
3.1 …installpipinversionsofPythonpriortoPython3.4? . . . . . . . . . . . . . . . . . . . . . . 7
3.2 …installpackagesjustforthecurrentuser? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.3 …installscientificPythonpackages?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.4 …workwithmultipleversionsofPythoninstalledinparallel? . . . . . . . . . . . . . . . . . . . 7
4 Commoninstallationissues 9
4.1 InstallingintothesystemPythononLinux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.2 Pipnotinstalled. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.3 Installingbinaryextensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
A Glossary 11
B Aboutthisdocumentation 29
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
C HistoryandLicense 31
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 32
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 32
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 33
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 33
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 34
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 35
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 35
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
i

### 第4页

C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
D Copyright 51
Index 53
ii

### 第5页

Email
distutils-sig@python.org
Asapopularopensourcedevelopmentproject,Pythonhasanactivesupportingcommunityofcontributorsandusers
thatalsomaketheirsoftwareavailableforotherPythondeveloperstouseunderopensourcelicenseterms.
ThisallowsPythonuserstoshareandcollaborateeffectively,benefitingfromthesolutionsothershavealreadycreated
to common (and sometimes even rare!) problems, as well as potentially contributing their own solutions to the
commonpool.
Thisguidecoverstheinstallationpartoftheprocess. ForaguidetocreatingandsharingyourownPythonprojects,
refertothePythonpackaginguserguide.
(cid:174) Note
For corporate and other institutional users, be aware that many organisations have their own policies around
usingandcontributingtoopensourcesoftware. Pleasetakesuchpoliciesintoaccountwhenmakinguseofthe
distributionandinstallationtoolsprovidedwithPython.
CONTENTS 1

### 第6页

2 CONTENTS

### 第7页

CHAPTER
ONE
KEY TERMS
• pip is the preferred installer program. Starting with Python 3.4, it is included by default with the Python
binaryinstallers.
• Avirtualenvironmentisasemi-isolatedPythonenvironmentthatallowspackagestobeinstalledforusebya
particularapplication,ratherthanbeinginstalledsystemwide.
• venv is the standard tool for creating virtual environments, and has been part of Python since Python 3.3.
StartingwithPython3.4,itdefaultstoinstallingpipintoallcreatedvirtualenvironments.
• virtualenvisathirdpartyalternative(andpredecessor)tovenv. Itallowsvirtualenvironmentstobeused
onversionsofPythonpriorto3.4,whicheitherdon’tprovidevenvatall,oraren’tabletoautomaticallyinstall
pipintocreatedenvironments.
• ThePythonPackageIndexisapublicrepositoryofopensourcelicensedpackagesmadeavailableforuseby
otherPythonusers.
• the Python Packaging Authority is the group of developers and documentation authors responsible for the
maintenanceandevolutionofthestandardpackagingtoolsandtheassociatedmetadataandfileformatstan-
dards. Theymaintainavarietyoftools,documentation,andissuetrackersonGitHub.
• distutils is the original build and distribution system first added to the Python standard library in 1998.
Whiledirectuseofdistutilsisbeingphasedout,itstilllaidthefoundationforthecurrentpackagingand
distributioninfrastructure,anditnotonlyremainspartofthestandardlibrary,butitsnamelivesoninother
ways(suchasthenameofthemailinglistusedtocoordinatePythonpackagingstandardsdevelopment).
Changedinversion3.5: Theuseofvenvisnowrecommendedforcreatingvirtualenvironments.
(cid:181) Seealso
PythonPackagingUserGuide: Creatingandusingvirtualenvironments
3

| (cid:181) Seealso |
| --- |
| PythonPackagingUserGuide: Creatingandusingvirtualenvironments |

### 第8页

4 Chapter1. Keyterms

### 第9页

CHAPTER
TWO
BASIC USAGE
Thestandardpackagingtoolsarealldesignedtobeusedfromthecommandline.
The following command will install the latest version of a module and its dependencies from the Python Package
Index:
python -m pip install SomePackage
(cid:174) Note
For POSIX users (including macOS and Linux users), the examples in this guide assume the use of a virtual
environment.
ForWindowsusers,theexamplesinthisguideassumethattheoptiontoadjustthesystemPATHenvironment
variablewasselectedwheninstallingPython.
It’s also possible to specify an exact or minimum version directly on the command line. When using comparator
operators such as >, < or some other special character which get interpreted by shell, the package name and the
versionshouldbeenclosedwithindoublequotes:
python -m pip install SomePackage==1.0.4 # specific version
python -m pip install "SomePackage>=1.0.4" # minimum version
Normally,ifasuitablemoduleisalreadyinstalled,attemptingtoinstallitagainwillhavenoeffect. Upgradingexisting
modulesmustberequestedexplicitly:
python -m pip install --upgrade SomePackage
MoreinformationandresourcesregardingpipanditscapabilitiescanbefoundinthePythonPackagingUserGuide.
Creationofvirtualenvironmentsisdonethroughthevenvmodule. Installingpackagesintoanactivevirtualenvi-
ronmentusesthecommandsshownabove.
(cid:181) Seealso
PythonPackagingUserGuide: InstallingPythonDistributionPackages
5

| (cid:181) Seealso |
| --- |
| PythonPackagingUserGuide: InstallingPythonDistributionPackages |

### 第10页

6 Chapter2. Basicusage

### 第11页

CHAPTER
THREE
HOW DO I …?
Thesearequickanswersorlinksforsomecommontasks.
3.1 … install pip in versions of Python prior to Python 3.4?
PythononlystartedbundlingpipwithPython3.4. Forearlierversions,pipneedstobe“bootstrapped”asdescribed
inthePythonPackagingUserGuide.
(cid:181) Seealso
PythonPackagingUserGuide: RequirementsforInstallingPackages
3.2 … install packages just for the current user?
Passingthe--useroptiontopython -m pip installwillinstallapackagejustforthecurrentuser,ratherthan
forallusersofthesystem.
3.3 … install scientific Python packages?
AnumberofscientificPythonpackageshavecomplexbinarydependencies,andaren’tcurrentlyeasytoinstallusing
pipdirectly. Atthispointintime, itwilloftenbeeasierforuserstoinstallthesepackagesbyothermeansrather
thanattemptingtoinstallthemwithpip.
(cid:181) Seealso
PythonPackagingUserGuide: InstallingScientificPackages
3.4 … work with multiple versions of Python installed in parallel?
OnLinux,macOS,andotherPOSIXsystems,usetheversionedPythoncommandsincombinationwiththe-mswitch
toruntheappropriatecopyofpip:
python2 -m pip install SomePackage # default Python 2
python2.7 -m pip install SomePackage # specifically Python 2.7
python3 -m pip install SomePackage # default Python 3
python3.4 -m pip install SomePackage # specifically Python 3.4
Appropriatelyversionedpipcommandsmayalsobeavailable.
OnWindows,usethepyPythonlauncherincombinationwiththe-mswitch:
7

| (cid:181) Seealso |
| --- |
| PythonPackagingUserGuide: RequirementsforInstallingPackages |


| (cid:181) Seealso |
| --- |
| PythonPackagingUserGuide: InstallingScientificPackages |

### 第12页

py -2 -m pip install SomePackage # default Python 2
py -2.7 -m pip install SomePackage # specifically Python 2.7
py -3 -m pip install SomePackage # default Python 3
py -3.4 -m pip install SomePackage # specifically Python 3.4
8 Chapter3. HowdoI…?

### 第13页

CHAPTER
FOUR
COMMON INSTALLATION ISSUES
4.1 Installing into the system Python on Linux
On Linux systems, a Python installation will typically be included as part of the distribution. Installing into this
Pythoninstallationrequiresrootaccesstothesystem, andmayinterferewiththeoperationofthesystempackage
managerandothercomponentsofthesystemifacomponentisunexpectedlyupgradedusingpip.
On such systems, it is often better to use a virtual environment or a per-user installation when installing packages
withpip.
4.2 Pip not installed
Itispossiblethatpipdoesnotgetinstalledbydefault. Onepotentialfixis:
python -m ensurepip --default-pip
Therearealsoadditionalresourcesforinstallingpip.
4.3 Installing binary extensions
Pythonhastypicallyreliedheavilyonsourcebaseddistribution,withendusersbeingexpectedtocompileextension
modulesfromsourceaspartoftheinstallationprocess.
Withtheintroductionofsupportforthebinarywheelformat,andtheabilitytopublishwheelsforatleastWindows
andmacOSthroughthePythonPackageIndex, thisproblemisexpectedtodiminishovertime, asusersaremore
regularlyabletoinstallpre-builtextensionsratherthanneedingtobuildthemthemselves.
Someofthesolutionsforinstallingscientificsoftwarethatarenotyetavailableaspre-builtwheelfilesmayalsohelp
withobtainingotherbinaryextensionswithoutneedingtobuildthemlocally.
(cid:181) Seealso
PythonPackagingUserGuide: BinaryExtensions
9

| (cid:181) Seealso |
| --- |
| PythonPackagingUserGuide: BinaryExtensions |

### 第14页

10 Chapter4. Commoninstallationissues

### 第15页

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
11

### 第16页

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
12 AppendixA. Glossary

### 第17页

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
13

### 第18页

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
14 AppendixA. Glossary

### 第19页

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
15

### 第20页

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
16 AppendixA. Glossary

### 第21页

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
17

### 第22页

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
18 AppendixA. Glossary

### 第23页

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
19

### 第24页

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
20 AppendixA. Glossary

### 第25页

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
21

### 第26页

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
22 AppendixA. Glossary

### 第27页

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
23

### 第28页

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
24 AppendixA. Glossary

### 第29页

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
25

### 第30页

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
26 AppendixA. Glossary

### 第31页

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
27

### 第32页

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
28 AppendixA. Glossary

### 第33页

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
29

### 第34页

30 AppendixB. Aboutthisdocumentation

### 第35页

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
31

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

### 第36页

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
32 AppendixC. HistoryandLicense

### 第37页

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
C.2. TermsandconditionsforaccessingorotherwiseusingPython 33

### 第38页

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
34 AppendixC. HistoryandLicense

### 第39页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 35

### 第40页

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
36 AppendixC. HistoryandLicense

### 第41页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 37

### 第42页

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
38 AppendixC. HistoryandLicense

### 第43页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 39

### 第44页

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
40 AppendixC. HistoryandLicense

### 第45页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 41

### 第46页

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
42 AppendixC. HistoryandLicense

### 第47页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 43

### 第48页

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
44 AppendixC. HistoryandLicense

### 第49页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 45

### 第50页

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
46 AppendixC. HistoryandLicense

### 第51页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 47

### 第52页

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
48 AppendixC. HistoryandLicense

### 第53页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 49

### 第54页

50 AppendixC. HistoryandLicense

### 第55页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
51

### 第56页

52 AppendixD. Copyright

### 第57页

INDEX
Non-alphabetical D
...,11 decorator,15
ellipsis literal,11 descriptor,15
>>>,11 dictionary,15
__future__,17 dictionary comprehension,15
__slots__,25 dictionary view,15
docstring,15
A
duck-typing,16
abstract base class,11 dunder,16
annotate function,11
E
annotation,11
argument,11 EAFP,16
asynchronous context manager,12 environment variable
asynchronous generator,12 PYTHON_GIL,18
asynchronous generator iterator,12 evaluate function,16
asynchronous iterable,12 expression,16
asynchronous iterator,12 extension module,16
attached thread state,12
F
attribute,12
awaitable,13 f-string,16
f-strings,16
B
file object,16
BDFL,13 file-like object,16
binary file,13 filesystem encoding and error handler,16
borrowed reference,13 finder,17
bytecode,13 floor division,17
bytes-like object,13 Fortran contiguous,14
free threading,17
C
free variable,17
callable,13 function,17
callback,13 function annotation,17
C-contiguous,14
G
class,13
class variable,13 garbage collection,17
closure variable,14 generator,17
complex number,14 generator expression,18
context,14 generator iterator,18
context management protocol,14 generic function,18
context manager,14 generic type,18
context variable,14 GIL,18
contiguous,14 global interpreter lock,18
coroutine,14
H
coroutine function,14
CPython,15 hash-based pyc,18
current context,15 hashable,18
cyclic isolate,15
53

### 第58页

I
path entry,23
IDLE,19 path entry finder,23
immortal,19 path entry hook,23
immutable,19 path-like object,23
import path,19
PEP,23
importer,19
portion,24
importing,19 positional argument,24
interactive,19 provisional API,24
interpreted,19 provisional package,24
interpreter shutdown,19 Python 3000,24
iterable,19 Python Enhancement Proposals
iterator,20 PEP 1,24
PEP 238,17
K PEP 278,27
PEP 302,21
key function,20
PEP 343,14
keyword argument,20
PEP 362,12,23
L PEP 411,24
PEP 420,22,24
lambda,20
PEP 443,18
LBYL,20
PEP 483,18
lexical analyzer,20
PEP 484,11,17,18,27,28
list,20
PEP 492,1215
list comprehension,20
PEP 498,16
loader,20
PEP 519,23
locale encoding,21
PEP 525,12
M PEP 526,11,28
PEP 585,18
magic PEP 649,11
method,21
PEP 683,19
magic method,21 PEP 703,17,18
mapping,21
PEP 3116,27
meta path finder,21 PEP 3155,24
metaclass,21
PYTHON_GIL,18
method,21
Pythonic,24
magic,21
special,26 Q
method resolution order,21
qualified name,24
module,21
module spec,21 R
MRO,21
reference count,25
mutable,21
regular package,25
N REPL,25
named tuple,22 S
namespace,22
namespace package,22 sequence,25
nested scope,22 set comprehension,25
new-style class,22 single dispatch,25
slice,25
O soft deprecated,25
special
object,22
method,26
optimized scope,22
special method,26
P standard library,26
statement,26
package,22
static type checker,26
parameter,23
stdlib,26
path based finder,23
strong reference,26
54 Index

### 第59页

T
t-string,26
t-strings,26
text encoding,26
text file,26
thread state,26
token,27
triple-quoted string,27
type,27
type alias,27
type hint,27
U
universal newlines,27
V
variable annotation,27
virtual environment,28
virtual machine,28
W
walrus operator,28
Z
Zen of Python,28
Index 55

