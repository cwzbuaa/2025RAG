### 第1页

What’s New in Python
Release 3.14.0rc3
A. M. Kuchling
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Summary–releasehighlights 4
2 Incompatiblechanges 4
3 Newfeatures 4
3.1 PEP779: Free-threadedPythonisofficiallysupported . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 PEP734: Multipleinterpretersinthestdlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3 PEP750: Templatestrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.4 PEP768: SafeexternaldebuggerinterfaceforCPython . . . . . . . . . . . . . . . . . . . . . . . 7
3.5 PEP784: AddingZstandardtothestandardlibrary . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.6 RemoteattachingtoarunningPythonprocesswithPDB . . . . . . . . . . . . . . . . . . . . . . . 8
3.7 PEP758–Allowexceptandexcept*expressionswithoutparentheses . . . . . . . . . . . . . . . . 9
3.8 PEP649and749: deferredevaluationofannotations . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.9 Improvederrormessages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.10 PEP741: PythonconfigurationCAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.11 Asynciointrospectioncapabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.12 Anewtypeofinterpreter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.13 Free-threadedmode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.14 SyntaxhighlightinginPyREPL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.15 Binaryreleasesfortheexperimentaljust-in-timecompiler . . . . . . . . . . . . . . . . . . . . . . 17
3.16 Concurrentsafewarningscontrol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.17 Incrementalgarbagecollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 Platformsupport 17
5 Otherlanguagechanges 18
5.1 PEP765: Disallowreturn/break/continuethatexitafinallyblock . . . . . . . . . . . . . 19
6 Newmodules 19
7 Improvedmodules 19
7.1 argparse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.2 ast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.3 asyncio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.4 calendar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.5 concurrent.futures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.6 configparser . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.7 contextvars . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.8 ctypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
1

### 第2页

7.9 curses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.10 datetime . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.11 decimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.12 difflib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.13 dis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
7.14 errno . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.15 faulthandler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.16 fnmatch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.17 fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.18 functools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.19 getopt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.20 getpass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.21 graphlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
7.22 heapq . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.23 hmac. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.24 http . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.25 imaplib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.26 inspect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.27 io . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.28 json . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
7.29 linecache. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
7.30 logging.handlers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
7.31 math . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
7.32 mimetypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
7.33 multiprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
7.34 operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.35 os . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.36 os.path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.37 pathlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.38 pdb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
7.39 pickle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.40 platform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.41 pydoc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.42 socket . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.43 ssl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7.44 struct. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.45 symtable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.46 sys . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.47 sys.monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.48 sysconfig . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.49 tarfile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.50 threading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
7.51 tkinter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.52 turtle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.53 types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.54 typing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.55 unicodedata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
7.56 unittest . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
7.57 urllib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
7.58 uuid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
7.59 webbrowser . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
7.60 zipfile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8 Optimizations 31
8.1 asyncio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.2 base64 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.3 bdb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.4 difflib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
2

### 第3页

8.5 gc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
8.6 io . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
8.7 pathlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
8.8 pdb . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
8.9 uuid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
8.10 zlib. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
9 Removed 32
9.1 argparse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
9.2 ast . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
9.3 asyncio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
9.4 email. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.5 importlib.abc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.6 itertools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.7 pathlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.8 pkgutil . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.9 pty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.10 sqlite3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
9.11 urllib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
10 Deprecated 36
10.1 Newdeprecations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
10.2 PendingremovalinPython3.15. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
10.3 PendingremovalinPython3.16. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
10.4 PendingremovalinPython3.17. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
10.5 PendingremovalinPython3.19. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
10.6 Pendingremovalinfutureversions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
11 CPythonbytecodechanges 43
11.1 Pseudo-instructions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
12 CAPIchanges 44
12.1 NewfeaturesintheCAPI. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
12.2 LimitedCAPIchanges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
12.3 RemovedCAPIs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
12.4 DeprecatedCAPIs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
13 BuildChanges 50
13.1 build-details.json . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
13.2 DiscontinuationofPGPsignatures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
14 PortingtoPython3.14 50
14.1 ChangesinthePythonAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
14.2 ChangesintheCAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
Index 53
Editor
HugovanKemenade
ThisarticleexplainsthenewfeaturesinPython3.14,comparedto3.13.
Forfulldetails,seethechangelog.
(cid:181) Seealso
PEP745–Python3.14releaseschedule
3

| (cid:181) Seealso |
| --- |
| PEP745–Python3.14releaseschedule |

### 第4页

(cid:174) Note
Prereleaseusersshouldbeawarethatthisdocumentiscurrentlyindraftform. Itwillbeupdatedsubstantiallyas
Python3.14movestowardsrelease,soit’sworthcheckingbackevenafterreadingearlierversions.
1 Summary – release highlights
Python 3.14 will be the latest stable release of the Python programming language, with a mix of changes to the
language,theimplementationandthestandardlibrary.
Thebiggestchangestotheimplementationincludetemplatestrings(PEP750),deferredevaluationofannotations
(PEP649),andanewtypeofinterpreterthatusestailcalls.
Thelibrarychangesincludetheadditionofanewannotationlibmoduleforintrospectingandwrappingannota-
tions(PEP749),anewcompression.zstdmoduleforZstandardsupport(PEP784),plussyntaxhighlightingin
theREPL,aswellastheusualdeprecationsandremovals,andimprovementsinuser-friendlinessandcorrectness.
• PEP779: Free-threadedPythonisofficiallysupported
• PEP649and749: deferredevaluationofannotations
• PEP734: Multipleinterpretersinthestdlib
• PEP741: PythonconfigurationCAPI
• PEP750: Templatestrings
• PEP758: Allowexceptandexcept*expressionswithoutparentheses
• PEP761: DiscontinuationofPGPsignatures
• PEP765: Disallowreturn/break/continuethatexitafinallyblock
• Free-threadedmodeimprovements
• PEP768: SafeexternaldebuggerinterfaceforCPython
• PEP784: AddingZstandardtothestandardlibrary
• Anewtypeofinterpreter
• SyntaxhighlightinginPyREPL,andcoloroutputinunittest,argparse,jsonandcalendarCLIs
• Binaryreleasesfortheexperimentaljust-in-timecompiler
2 Incompatible changes
On platforms other than macOS and Windows, the default start method for multiprocessing and
ProcessPoolExecutorswitchesfromforktoforkserver.
See(1)and(2)fordetails.
If you encounter NameErrors or pickling errors coming out of multiprocessing or concurrent.futures,
seetheforkserverrestrictions.
Theinterpreteravoidssomereferencecountmodificationsinternallywhenit’ssafetodoso. Thiscanleadtodifferent
values returned from sys.getrefcount() and Py_REFCNT() compared to previous versions of Python. See
belowfordetails.
3 New features
3.1 PEP 779: Free-threaded Python is officially supported
Thefree-threadedbuildofPythonisnowsupportedandnolongerexperimental. ThisisthestartofphaseIIwhere
free-threadedPythonisofficiallysupportedbutstilloptional.
4

### 第5页

We are confident that the project is on the right path, and we appreciate the continued dedication from everyone
workingtomakefree-threadingreadyforbroaderadoptionacrossthePythoncommunity.
WiththeserecommendationsandtheacceptanceofthisPEP,weasthePythondevelopercommunityshouldbroadly
advertisethatfree-threadingisasupportedPythonbuildoptionnowandintothefuture,andthatitwillnotberemoved
withoutaproperdeprecationschedule.
AnydecisiontotransitiontophaseIII,withfree-threadingasthedefaultorsolebuildofPythonisstillundecided,
anddependentonmanyfactorsbothwithinCPythonitselfandthecommunity. Thisdecisionisforthefuture.
(cid:181) Seealso
PEP779anditsacceptance.
3.2 PEP 734: Multiple interpreters in the stdlib
TheCPythonruntimesupportsrunningmultiplecopiesofPythoninthesameprocesssimultaneouslyandhasdone
soforover20years. Eachoftheseseparatecopiesiscalledan“interpreter”. However,thefeaturehadbeenavailable
onlythroughtheC-API.
Thatlimitationisremovedinthe3.14release,withthenewconcurrent.interpretersmodule.
Thereareatleasttwonotablereasonswhyusingmultipleinterpretersisworthconsidering:
• theysupportanew(toPython),human-friendlyconcurrencymodel
• truemulti-coreparallelism
Forsomeusecases,concurrencyinsoftwareenablesefficiencyandcansimplifysoftware,atahighlevel. Atthesame
time,implementingandmaintainingallbutthesimplestconcurrencyisoftenastruggleforthehumanbrain. That
especiallyappliestoplainthreads(forexample,threading),whereallmemoryissharedbetweenallthreads.
Withmultipleisolatedinterpreters,youcantakeadvantageofaclassofconcurrencymodels,likeCSPortheactor
model,thathavefoundsuccessinotherprogramminglanguages,likeSmalltalk,Erlang,Haskell,andGo. Thinkof
multipleinterpreterslikethreadsbutwithopt-insharing.
Regardingmulti-coreparallelism: asofthe3.12release,interpretersarenowsufficientlyisolatedfromoneanotherto
beusedinparallel. (SeePEP684.) ThisunlocksavarietyofCPU-intensiveusecasesforPythonthatwerelimited
bytheGIL.
Usingmultipleinterpretersissimilarinmanywaystomultiprocessing, inthattheybothprovideisolatedlog-
ical“processes”thatcanruninparallel,withnosharingbydefault. However,whenusingmultipleinterpreters,an
applicationwillusefewersystemresourcesandwilloperatemoreefficiently(sinceitstayswithinthesameprocess).
Thinkofmultipleinterpretersashavingtheisolationofprocesseswiththeefficiencyofthreads.
Whilethefeaturehasbeenaroundfordecades,multipleinterpretershavenotbeenusedwidely,duetolowawareness
andthelackofastdlibmodule. Consequently,theycurrentlyhaveseveralnotablelimitations,whichwillimprove
significantlynowthatthefeatureisfinallygoingmainstream.
Currentlimitations:
• startingeachinterpreterhasnotbeenoptimizedyet
• each interpreter uses more memory than necessary (we will be working next on extensive internal sharing
betweeninterpreters)
• there aren’t many options yet for truly sharing objects or other data between interpreters (other than
memoryview)
• manyextensionmodulesonPyPIarenotcompatiblewithmultipleinterpretersyet(stdlibextensionmodules
arecompatible)
• theapproachtowritingapplicationsthatusemultipleisolatedinterpretersismostlyunfamiliartoPythonusers,
fornow
5

| (cid:181) Seealso |
| --- |
| PEP779anditsacceptance. |

### 第6页

TheimpactoftheselimitationswilldependonfutureCPythonimprovements,howinterpretersareused,andwhat
thecommunitysolvesthroughPyPIpackages. Dependingontheusecase,thelimitationsmaynothavemuchimpact,
sotryitout!
Furthermore,futureCPythonreleaseswillreduceoreliminateoverheadandprovideutilitiesthatarelessappropriate
onPyPI.Inthemeantime,mostofthelimitationscanalsobeaddressedthroughextensionmodules,meaningPyPI
packagescanfillanygapfor3.14,andevenbackto3.12whereinterpreterswerefinallyproperlyisolatedandstopped
sharingtheGIL.Likewise,weexpecttoslowlyseelibrariesonPyPIforhigh-levelabstractionsontopofinterpreters.
Regarding extension modules, work is in progress to update some PyPI projects, as well as tools like Cython, py-
bind11,nanobind,andPyO3. Thestepsforisolatinganextensionmodulearefoundatisolating-extensions-howto.
Isolatingamodulehasalotofoverlapwithwhatisrequiredtosupportfree-threading, sotheongoingworkinthe
communityinthatareawillhelpacceleratesupportformultipleinterpreters.
Alsoaddedin3.14: concurrent.futures.InterpreterPoolExecutor.
(cid:181) Seealso
PEP734.
3.3 PEP 750: Template strings
Template string literals (t-strings) are a generalization of f-strings, using a t in place of the f prefix. Instead of
evaluatingtostr,t-stringsevaluatetoanewstring.templatelib.Templatetype:
from string.templatelib import Template
name = "World"
template: Template = t"Hello {name}"
The template can then be combined with functions that operate on the template’s structure to produce a str or a
string-likeresult. Forexample,sanitizinginput:
evil = "<script>alert('evil')</script>"
template = t"<p>{evil}</p>"
assert html(template) == "<p>&lt;script&gt;alert('evil')&lt;/script&gt;</p>"
Asanotherexample,generatingHTMLattributesfromdata:
attributes = {"src": "shrubbery.jpg", "alt": "looks nice"}
template = t"<img {attributes}>"
assert html(template) == '<img src="shrubbery.jpg" alt="looks nice" />'
Comparedtousinganf-string,thehtmlfunctionhasaccesstotemplateattributescontainingtheoriginalinformation:
staticstrings,interpolations,andvaluesfromtheoriginalscope. Unlikeexistingtemplatingapproaches,t-stringsbuild
fromthewell-knownf-stringsyntaxandrules. TemplatesystemsthusbenefitfromPythontoolingastheyaremuch
closertothePythonlanguage,syntax,scoping,andmore.
Writingtemplatehandlersisstraightforward:
from string.templatelib import Template, Interpolation
def lower_upper(template: Template) -> str:
"""Render static parts lowercased and interpolations uppercased."""
parts: list[str] = []
for item in template:
if isinstance(item, Interpolation):
parts.append(str(item.value).upper())
else:
(continuesonnextpage)
6

### 第7页

(continuedfrompreviouspage)
parts.append(item.lower())
return "".join(parts)
name = "world"
assert lower_upper(t"HELLO {name}") == "hello WORLD"
With this in place, developers can write template systems to sanitize SQL, make safe shell operations, improve
logging, tackle modern ideas in web development (HTML, CSS, and so on), and implement lightweight, custom
businessDSLs.
(ContributedbyJimBaker,GuidovanRossum,PaulEveritt,KoudaiAono,LysandrosNikolaou,DavePeck,Adam
Turner,JelleZijlstra,BénédiktTran,andPabloGalindoSalgadoingh-132661.)
(cid:181) Seealso
PEP750.
3.4 PEP 768: Safe external debugger interface for CPython
PEP 768 introduces a zero-overhead debugging interface that allows debuggers and profilers to safely attach to
runningPythonprocesses. ThisisasignificantenhancementtoPython’sdebuggingcapabilitiesallowingdebuggers
toforegounsafealternatives. Seebelowforhowthisfeatureisleveragedtoimplementthenewpdbmodule’sremote
attachingcapabilities.
The new interface provides safe execution points for attaching debugger code without modifying the interpreter’s
normalexecutionpathoraddingruntimeoverhead. ThisenablestoolstoinspectandinteractwithPythonapplications
inreal-timewithoutstoppingorrestartingthem—acrucialcapabilityforhigh-availabilitysystemsandproduction
environments.
Forconvenience,CPythonimplementsthisinterfacethroughthesysmodulewithasys.remote_exec()function:
sys.remote_exec(pid, script_path)
ThisfunctionallowssendingPythoncodetobeexecutedinatargetprocessatthenextsafeexecutionpoint. How-
ever, tool authors can also implement the protocol directly as described in the PEP, which details the underlying
mechanismsusedtosafelyattachtorunningprocesses.
Here’sasimpleexamplethatinspectsobjecttypesinarunningPythonprocess:
import os
import sys
import tempfile
# Create a temporary script
with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as␣
,→f:
script_path = f.name
f.write(f"import my_debugger; my_debugger.connect({os.getpid()})")
try:
# Execute in process with PID 1234
print("Behold! An offering:")
sys.remote_exec(1234, script_path)
finally:
os.unlink(script_path)
Thedebugginginterfacehasbeencarefullydesignedwithsecurityinmindandincludesseveralmechanismstocontrol
access:
• APYTHON_DISABLE_REMOTE_DEBUGenvironmentvariable.
7

| (cid:181) Seealso |
| --- |
| PEP750. |

### 第8页

• A-X disable-remote-debugcommand-lineoption.
• A--without-remote-debugconfigureflagtocompletelydisablethefeatureatbuildtime.
A key implementation detail is that the interface piggybacks on the interpreter’s existing evaluation loop and safe
points, ensuring zero overhead during normal execution while providing a reliable way for external processes to
coordinatedebuggingoperations.
(ContributedbyPabloGalindoSalgado,MattWozniski,andIvonaStojanovicingh-131591.)
(cid:181) Seealso
PEP768.
3.5 PEP 784: Adding Zstandard to the standard library
The new compression package contains modules compression.lzma, compression.bz2, compression.
gzip and compression.zlib which re-export the lzma, bz2, gzip and zlib modules respectively. The new
import names under compression are the canonical names for importing these compression modules going for-
ward. However,theexistingmodulesnameshavenotbeendeprecated. Anydeprecationorremovaloftheexisting
compressionmoduleswilloccurnosoonerthanfiveyearsafterthereleaseof3.14.
Thenewcompression.zstdmoduleprovidescompressionanddecompressionAPIsfortheZstandardformatvia
bindings to Meta’s zstd library. Zstandard is a widely adopted, highly efficient, and fast compression format. In
addition to the APIs introduced in compression.zstd, support for reading and writing Zstandard compressed
archiveshasbeenaddedtothetarfile,zipfile,andshutilmodules.
Here’sanexampleofusingthenewmoduletocompresssomedata:
from compression import zstd
import math
data = str(math.pi).encode() * 20
compressed = zstd.compress(data)
ratio = len(compressed) / len(data)
print(f"Achieved compression ratio of {ratio}")
Ascanbeseen,theAPIissimilartotheAPIsofthelzmaandbz2modules.
(ContributedbyEmmaHarperSmith,AdamTurner,GregoryP.Smith,TomasRoun,VictorStinner,andRogdham
ingh-132983.)
(cid:181) Seealso
PEP784.
3.6 Remote attaching to a running Python process with PDB
The pdb module now supports remote attaching to a running Python process using a new -p PID command-line
option:
python -m pdb -p 1234
ThiswillconnecttothePythonprocesswiththegivenPIDandallowyoutodebugitinteractively. Noticethatdue
tohowthePythoninterpreterworksattachingtoaremoteprocessthatisblockedinasystemcallorwaitingforI/O
willonlyworkoncethenextbytecodeinstructionisexecutedorwhentheprocessreceivesasignal.
8

| (cid:181) Seealso |
| --- |
| PEP768. |


| (cid:181) Seealso |
| --- |
| PEP784. |

### 第9页

This feature uses PEP 768 and the sys.remote_exec() function to attach to the remote process and send the
PDBcommandstoit.
(ContributedbyMattWozniskiandPabloGalindoingh-131591.)
(cid:181) Seealso
PEP768.
3.7 PEP 758 – Allow except and except* expressions without parentheses
Theexceptandexcept*expressionsnowallowparenthesestobeomittedwhentherearemultipleexceptiontypes
andtheasclauseisnotused. Forexamplethefollowingexpressionsarenowvalid:
try:
connect_to_server()
except TimeoutError, ConnectionRefusedError:
print("Network issue encountered.")
# The same applies to except* (for exception groups):
try:
connect_to_server()
except* TimeoutError, ConnectionRefusedError:
print("Network issue encountered.")
CheckPEP758formoredetails.
(ContributedbyPabloGalindoandBrettCannoningh-131831.)
(cid:181) Seealso
PEP758.
3.8 PEP 649 and 749: deferred evaluation of annotations
Theannotationsonfunctions,classes,andmodulesarenolongerevaluatedeagerly. Instead,annotationsarestored
in special-purpose annotate functions and evaluated only when necessary (except if from __future__ import
annotationsisused). ThisisspecifiedinPEP649andPEP749.
This change is designed to make annotations in Python more performant and more usable in most circumstances.
Theruntimecostfordefiningannotationsisminimized,butitremainspossibletointrospectannotationsatruntime.
Itisnolongernecessarytoencloseannotationsinstringsiftheycontainforwardreferences.
The new annotationlib module provides tools for inspecting deferred annotations. Annotations may be evalu-
atedintheVALUEformat(whichevaluatesannotationstoruntimevalues,similartothebehaviorinearlierPython
versions),theFORWARDREFformat(whichreplacesundefinednameswithspecialmarkers),andtheSTRINGformat
(whichreturnsannotationsasstrings).
Thisexampleshowshowtheseformatsbehave:
>>> from annotationlib import get_annotations, Format
>>> def func(arg: Undefined):
... pass
>>> get_annotations(func, format=Format.VALUE)
Traceback (most recent call last):
...
NameError: name 'Undefined' is not defined
>>> get_annotations(func, format=Format.FORWARDREF)
(continuesonnextpage)
9

| (cid:181) Seealso |
| --- |
| PEP768. |


| (cid:181) Seealso |
| --- |
| PEP758. |

### 第10页

(continuedfrompreviouspage)
{'arg': ForwardRef('Undefined', owner=<function func at 0x...>)}
>>> get_annotations(func, format=Format.STRING)
{'arg': 'Undefined'}
Implicationsforannotatedcode
Ifyoudefineannotationsinyourcode(forexample, forusewithastatictypechecker), thenthischangeprobably
doesnotaffectyou: youcankeepwritingannotationsthesamewayyoudidwithpreviousversionsofPython.
You will likely be able to remove quoted strings in annotations, which are frequently used for forward references.
Similarly,ifyouusefrom __future__ import annotationstoavoidhavingtowritestringsinannotations,
youmaywellbeabletoremovethatimportonceyousupportonlyPython3.14andnewer. However,ifyourelyon
third-partylibrariesthatreadannotations,thoselibrariesmayneedchangestosupportunquotedannotationsbefore
theyworkasexpected.
Implicationsforreadersof__annotations__
If your code reads the __annotations__ attribute on objects, you may want to make changes in order to sup-
portcodethatreliesondeferredevaluationofannotations. Forexample, youmaywanttouseannotationlib.
get_annotations()withtheFORWARDREFformat,asthedataclassesmodulenowdoes.
The external typing_extensions package provides partial backports of some of the functionality of the
annotationlibmodule,suchastheFormatenumandtheget_annotations()function. Thesecanbeused
towritecross-versioncodethattakesadvantageofthenewbehaviorinPython3.14.
Relatedchanges
The changes in Python 3.14 are designed to rework how __annotations__ works at runtime while minimizing
breakagetocodethatcontainsannotationsinsourcecodeandtocodethatreads__annotations__. However,if
yourelyonundocumenteddetailsoftheannotationbehaviororonprivatefunctionsinthestandardlibrary,thereare
manywaysinwhichyourcodemaynotworkinPython3.14. Tosafeguardyourcodeagainstfuturechanges, use
onlythedocumentedfunctionalityoftheannotationlibmodule.
In particular, do not read annotations directly from the namespace dictionary attribute of type ob-
jects. Use annotationlib.get_annotate_from_class_namespace() during class construction and
annotationlib.get_annotations()afterwards.
In previous releases, it was sometimes possible to access class annotations from an instance of an annotated class.
Thisbehaviorwasundocumentedandaccidental,andwillnolongerworkinPython3.14.
from __future__ import annotations
In Python 3.7, PEP 563 introduced the from __future__ import annotations directive, which turns all
annotations into strings. This directive is now considered deprecated and it is expected to be removed in a future
versionofPython. However,thisremovalwillnothappenuntilafterPython3.13,thelastversionofPythonwithout
deferredevaluationofannotations,reachesitsendoflifein2029. InPython3.14,thebehaviorofcodeusingfrom
__future__ import annotationsisunchanged.
(ContributedbyJelleZijlstraingh-119180;PEP649waswrittenbyLarryHastings.)
(cid:181) Seealso
PEP649andPEP749.
10

| (cid:181) Seealso |
| --- |
| PEP649andPEP749. |

### 第11页

3.9 Improved error messages
• TheinterpreternowprovideshelpfulsuggestionswhenitdetectstyposinPythonkeywords. Whenawordthat
closelyresemblesaPythonkeywordisencountered,theinterpreterwillsuggestthecorrectkeywordintheerror
message. Thisfeaturehelpsprogrammersquicklyidentifyandfixcommontypingmistakes. Forexample:
>>> whille True:
... pass
Traceback (most recent call last):
File "<stdin>", line 1
whille True:
^^^^^^
SyntaxError: invalid syntax. Did you mean 'while'?
>>> asynch def fetch_data():
... pass
Traceback (most recent call last):
File "<stdin>", line 1
asynch def fetch_data():
^^^^^^
SyntaxError: invalid syntax. Did you mean 'async'?
>>> async def foo():
... awaid fetch_data()
Traceback (most recent call last):
File "<stdin>", line 2
awaid fetch_data()
^^^^^
SyntaxError: invalid syntax. Did you mean 'await'?
>>> raisee ValueError("Error")
Traceback (most recent call last):
File "<stdin>", line 1
raisee ValueError("Error")
^^^^^^
SyntaxError: invalid syntax. Did you mean 'raise'?
Whilethefeaturefocusesonthemostcommoncases,somevariationsofmisspellingsmaystillresultinregular
syntaxerrors. (ContributedbyPabloGalindoingh-132449.)
• When an unpacking assignment fails due to an incorrect number of variables, the error message prints the
receivednumberofvaluesinmorecasesthanbefore. (ContributedbyTusharSadhwaniingh-122239.)
>>> x, y, z = 1, 2, 3, 4
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
x, y, z = 1, 2, 3, 4
^^^^^^^
ValueError: too many values to unpack (expected 3, got 4)
• elif statements that follow an else block now have a specific error message. (Contributed by Steele
Farnsworthingh-129902.)
>>> if who == "me":
... print("It's me!")
... else:
... print("It's not me!")
... elif who is None:
... print("Who is it?")
(continuesonnextpage)
11

### 第12页

(continuedfrompreviouspage)
File "<stdin>", line 5
elif who is None:
^^^^
SyntaxError: 'elif' block follows an 'else' block
• Ifastatement(pass,del,return,yield,raise,break,continue,assert,import,from)ispassed
totheif_exprafterelse,oroneofpass,break,orcontinueispassedbeforeif,thentheerrormessage
highlightswheretheexpressionisrequired. (ContributedbySergeyMiryanovingh-129515.)
>>> x = 1 if True else pass
Traceback (most recent call last):
File "<string>", line 1
x = 1 if True else pass
^^^^
SyntaxError: expected expression after 'else', but statement is given
>>> x = continue if True else break
Traceback (most recent call last):
File "<string>", line 1
x = continue if True else break
^^^^^^^^
SyntaxError: expected expression before 'if', but statement is given
• Whenincorrectlyclosedstringsaredetected,theerrormessagesuggeststhatthestringmaybeintendedtobe
partofthestring. (ContributedbyPabloGalindoingh-88535.)
>>> "The interesting object "The important object" is very important"
Traceback (most recent call last):
SyntaxError: invalid syntax. Is this intended to be part of the string?
• Whenstringshaveincompatibleprefixes,theerrornowshowswhichprefixesareincompatible. (Contributed
byNikitaSobolevingh-133197.)
>>> ub'abc'
File "<python-input-0>", line 1
ub'abc'
^^
SyntaxError: 'u' and 'b' prefixes are incompatible
• Improvederrormessageswhenusingaswithincompatibletargetsin:
– Imports: import ... as ...
– Fromimports: from ... import ... as ...
– Excepthandlers: except ... as ...
– Pattern-matchcases: case ... as ...
(ContributedbyNikitaSobolevingh-123539,gh-123562,andgh-123440.)
>>> import ast as arr[0]
File "<python-input-1>", line 1
import ast as arr[0]
^^^^^^
SyntaxError: cannot use subscript as import target
• Improvederrormessagewhentryingtoaddaninstanceofanunhashabletypetoadictorset. (Contributed
byCFBolz-TereickandVictorStinneringh-132828.)
12

### 第13页

>>> s = set()
>>> s.add({'pages': 12, 'grade': 'A'})
Traceback (most recent call last):
File "<python-input-1>", line 1, in <module>
s.add({'pages': 12, 'grade': 'A'})
~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
>>> d = {}
>>> l = [1, 2, 3]
>>> d[l] = 12
Traceback (most recent call last):
File "<python-input-4>", line 1, in <module>
d[l] = 12
~^^^
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
3.10 PEP 741: Python configuration C API
Add a PyInitConfig C API to configure the Python initialization without relying on C structures and the ability to
makeABI-compatiblechangesinthefuture.
Complete the PEP 587 PyConfig C API by adding PyInitConfig_AddModule() which can be used to add a
built-inextensionmodule;afeaturepreviouslyreferredtoasthe“inittab”.
AddPyConfig_Get()andPyConfig_Set()functionstogetandsetthecurrentruntimeconfiguration.
PEP587“PythonInitializationConfiguration”unifiedallthewaystoconfigurethePythoninitialization. ThisPEP
unifiesalsotheconfigurationofthePythonpreinitializationandthePythoninitializationinasingleAPI.Moreover,
thisPEPonlyprovidesasinglechoicetoembedPython,insteadofhavingtwo“Python”and“Isolated”choices(PEP
587),tosimplifytheAPIfurther.
ThelowerlevelPEP587PyConfigAPIremainsavailableforusecaseswithanintentionallyhigherlevelofcouplingto
CPythonimplementationdetails(suchasemulatingthefullfunctionalityofCPython’sCLI,includingitsconfiguration
mechanisms).
(ContributedbyVictorStinneringh-107954.)
(cid:181) Seealso
PEP741.
3.11 Asyncio introspection capabilities
Addedanewcommand-lineinterfacetoinspectrunningPythonprocessesusingasynchronoustasks,availablevia:
python -m asyncio ps PID
This tool inspects the given process ID (PID) and displays information about currently running asyncio tasks. It
outputsatasktable: aflatlistingofalltasks,theirnames,theircoroutinestacks,andwhichtasksareawaitingthem.
python -m asyncio pstree PID
This tool fetches the same information, but renders a visual async call tree, showing coroutine relationships in a
hierarchicalformat. Thiscommandisparticularlyusefulfordebugginglong-runningorstuckasynchronousprograms.
Itcanhelpdevelopersquicklyidentifywhereaprogramisblocked,whattasksarepending,andhowcoroutinesare
chainedtogether.
Forexamplegiventhiscode:
13

| (cid:181) Seealso |
| --- |
| PEP741. |

### 第14页

import asyncio
async def play(track):
await asyncio.sleep(5)
print(f"(cid:0) Finished: {track}")
async def album(name, tracks):
async with asyncio.TaskGroup() as tg:
for track in tracks:
tg.create_task(play(track), name=track)
async def main():
async with asyncio.TaskGroup() as tg:
tg.create_task(
album("Sundowning", ["TNDNBTG", "Levitate"]), name="Sundowning")
tg.create_task(
album("TMBTE", ["DYWTYLM", "Aqua Regia"]), name="TMBTE")
if __name__ == "__main__":
asyncio.run(main())
Executingthenewtoolontherunningprocesswillyieldatablelikethis:
python -m asyncio ps 12345
tid task id task name coroutine stack ␣
,→ awaiter chain awaiter␣
,→name awaiter id
-----------------------------------------------------------------------------------
,→---------------------------------------------------------------------------------
,→----------------
1935500 0x7fc930c18050 Task-1 TaskGroup._aexit -> TaskGroup.
,→__aexit__ -> main ␣
,→ 0x0
1935500 0x7fc930c18230 Sundowning TaskGroup._aexit -> TaskGroup.
,→__aexit__ -> album TaskGroup._aexit -> TaskGroup.__aexit__ -> main Task-1 ␣
,→ 0x7fc930c18050
1935500 0x7fc93173fa50 TMBTE TaskGroup._aexit -> TaskGroup.
,→__aexit__ -> album TaskGroup._aexit -> TaskGroup.__aexit__ -> main Task-1 ␣
,→ 0x7fc930c18050
1935500 0x7fc93173fdf0 TNDNBTG sleep -> play ␣
,→ TaskGroup._aexit -> TaskGroup.__aexit__ -> album ␣
,→Sundowning 0x7fc930c18230
1935500 0x7fc930d32510 Levitate sleep -> play ␣
,→ TaskGroup._aexit -> TaskGroup.__aexit__ -> album ␣
,→Sundowning 0x7fc930c18230
1935500 0x7fc930d32890 DYWTYLM sleep -> play ␣
,→ TaskGroup._aexit -> TaskGroup.__aexit__ -> album TMBTE ␣
,→ 0x7fc93173fa50
1935500 0x7fc93161ec30 Aqua Regia sleep -> play ␣
,→ TaskGroup._aexit -> TaskGroup.__aexit__ -> album TMBTE ␣
,→ 0x7fc93173fa50
oratreelikethis:
python -m asyncio pstree 12345
(continuesonnextpage)
14

### 第15页

(continuedfrompreviouspage)
└── (T) Task-1
└── main example.py:13
└── TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
└── TaskGroup._aexit Lib/asyncio/taskgroups.py:121
├── (T) Sundowning
│ └── album example.py:8
│ └── TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
│ └── TaskGroup._aexit Lib/asyncio/taskgroups.py:121
│ ├── (T) TNDNBTG
│ │ └── play example.py:4
│ │ └── sleep Lib/asyncio/tasks.py:702
│ └── (T) Levitate
│ └── play example.py:4
│ └── sleep Lib/asyncio/tasks.py:702
└── (T) TMBTE
└── album example.py:8
└── TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
└── TaskGroup._aexit Lib/asyncio/taskgroups.py:121
├── (T) DYWTYLM
│ └── play example.py:4
│ └── sleep Lib/asyncio/tasks.py:702
└── (T) Aqua Regia
└── play example.py:4
└── sleep Lib/asyncio/tasks.py:702
Ifacycleisdetectedintheasyncawaitgraph(whichcouldindicateaprogrammingissue),thetoolraisesanerror
andliststhecyclepathsthatpreventtreeconstruction:
python -m asyncio pstree 12345
ERROR: await-graph contains cycles - cannot print a tree!
cycle: Task-2 → Task-3 → Task-2
(ContributedbyPabloGalindo,ŁukaszLanga,YurySelivanov,andMartaGomezMaciasingh-91048.)
3.12 A new type of interpreter
AnewtypeofinterpreterhasbeenaddedtoCPython. ItusestailcallsbetweensmallCfunctionsthatimplement
individual Python opcodes, rather than one large C case statement. For certain newer compilers, this interpreter
providessignificantlybetterperformance. Preliminarynumbersonourmachinessuggestanywhereupto30%faster
Python code, and a geometric mean of 3-5% faster on pyperformance depending on platform and architecture.
ThebaselineisPython3.14builtwithClang19withoutthisnewinterpreter.
ThisinterpretercurrentlyonlyworkswithClang19andneweronx86-64andAArch64architectures. However,we
expectthatafuturereleaseofGCCwillsupportthisaswell.
Thisfeatureisopt-infornow. Wehighlyrecommendenablingprofile-guidedoptimizationwiththenewinterpreter
asitistheonlyconfigurationwehavetestedandcanvalidateitsimprovedperformance. Forfurtherinformationon
howtobuildPython,see--with-tail-call-interp.
(cid:174) Note
ThisisnottobeconfusedwithtailcalloptimizationofPythonfunctions,whichiscurrentlynotimplementedin
CPython.
ThisnewinterpretertypeisaninternalimplementationdetailoftheCPythoninterpreter. Itdoesn’tchangethe
visiblebehaviorofPythonprogramsatall. Itcanimprovetheirperformance,butdoesn’tchangeanythingelse.
15

### 第16页

(cid:193) Attention
Thissectionpreviouslyreporteda9-15%geometricmeanspeedup. Thisnumberhassincebeencautiouslyrevised
downto3-5%. Whileweexpectperformanceresultstobebetterthanwhatwereport, ourestimatesaremore
conservativeduetoacompilerbugfoundinClang/LLVM19,whichcausesthenormalinterpretertobeslower.
Wewereunawareofthisbug,resultingininaccurateresults. Wesincerelyapologizeforcommunicatingresults
thatwereonlyaccurateforLLVMv19.1.xandv20.1.0. Inthemeantime,thebughasbeenfixedinLLVMv20.1.1
andfortheupcomingv21.1, butitwillremainunfixedforLLVMv19.1.xandv20.1.0. Thusanybenchmarks
withthoseversionsofLLVMmayproduceinaccuratenumbers. (ThankstoNelsonElhageforbringingthisto
light.)
(ContributedbyKenJiningh-128563,withideasonhowtoimplementthisinCPythonbyMarkShannon,Garrett
Gu,HaoranXu,andJoshHaberman.)
3.13 Free-threaded mode
Free-threadedmode(PEP703), initiallyaddedin3.13, hasbeensignificantlyimproved. Theimplementationde-
scribed in PEP 703 was finished, including C API changes, and temporary workarounds in the interpreter were
replacedwithmorepermanentsolutions. Thespecializingadaptiveinterpreter(PEP659)isnowenabledinfree-
threaded mode, which along with many other optimizations greatly improves its performance. The performance
penaltyonsingle-threadedcodeinfree-threadedmodeisnowroughly5-10%, dependingonplatformandCcom-
pilerused.
Thisworkwasdonebymanycontributors: SamGross,MattPage,NeilSchemenauer,ThomasWouters,Donghee
Na, KirillPodoprigora, KenJin, ItamarOren, BrettSimmers, DinoViehland, NathanGoldbaum, RalfGommers,
LysandrosNikolaou,KumarAditya,EdgarMargffoy,andmanyothers.
SomeofthesecontributorsareemployedbyMeta,whichhascontinuedtoprovidesignificantengineeringresources
tosupportthisproject.
From3.14,whencompilingextensionmodulesforthefree-threadedbuildofCPythononWindows,thepreprocessor
variable Py_GIL_DISABLED now needs to be specified by the build backend, as it will no longer be determined
automaticallybytheCcompiler. Forarunninginterpreter,thesettingthatwasusedatcompiletimecanbefound
usingsysconfig.get_config_var().
Anewflaghasbeenadded,context_aware_warnings. Thisflagdefaultstotrueforthefree-threadedbuildand
falsefortheGIL-enabledbuild. Iftheflagistruethenthewarnings.catch_warningscontextmanagerusesa
context variable for warning filters. This makes the context manager behave predictably when used with multiple
threadsorasynchronoustasks.
Anewflaghasbeenadded,thread_inherit_context. Thisflagdefaultstotrueforthefree-threadedbuildand
falsefortheGIL-enabledbuild. Iftheflagistruethenthreadscreatedwiththreading.Threadstartwithacopy
oftheContext()ofthecallerofstart(). Mostsignificantly,thismakesthewarningfilteringcontextestablished
bycatch_warningsbe“inherited”bythreads(orasynciotasks)startedwithinthatcontext. Italsoaffectsother
modulesthatusecontextvariables,suchasthedecimalcontextmanager.
3.14 Syntax highlighting in PyREPL
The default interactive shell now highlights Python syntax as you type. The feature is enabled by default unless
thePYTHON_BASIC_REPLenvironmentissetoranycolor-disablingenvironmentvariablesareused. Seeusing-on-
controlling-colorfordetails.
The default color theme for syntax highlighting strives for good contrast and uses exclusively the 4-bit VGA stan-
dard ANSI color codes for maximum compatibility. The theme can be customized using an experimental API
_colorize.set_theme(). Thiscanbecalledinteractively,aswellasinthePYTHONSTARTUPscript.
(ContributedbyŁukaszLangaingh-131507.)
16

| (cid:193) Attention |
| --- |
| Thissectionpreviouslyreporteda9-15%geometricmeanspeedup. Thisnumberhassincebeencautiouslyrevised
downto3-5%. Whileweexpectperformanceresultstobebetterthanwhatwereport, ourestimatesaremore
conservativeduetoacompilerbugfoundinClang/LLVM19,whichcausesthenormalinterpretertobeslower.
Wewereunawareofthisbug,resultingininaccurateresults. Wesincerelyapologizeforcommunicatingresults
thatwereonlyaccurateforLLVMv19.1.xandv20.1.0. Inthemeantime,thebughasbeenfixedinLLVMv20.1.1
andfortheupcomingv21.1, butitwillremainunfixedforLLVMv19.1.xandv20.1.0. Thusanybenchmarks
withthoseversionsofLLVMmayproduceinaccuratenumbers. (ThankstoNelsonElhageforbringingthisto
light.) |

### 第17页

3.15 Binary releases for the experimental just-in-time compiler
TheofficialmacOSandWindowsreleasebinariesnowincludeanexperimentaljust-in-time(JIT)compiler. Although
itisnotrecommendedforproductionuse, itcanbetestedbysettingPYTHON_JIT=1asanenvironmentvariable.
Downstreamsourcebuildsandredistributorscanusethe--enable-experimental-jit=yes-offconfiguration
optionforsimilarbehavior.
The JIT is at an early stage and still in active development. As such, the typical performance impact of enabling
it can range from 10% slower to 20% faster, depending on workload. To aid in testing and evaluation, a set of
introspectionfunctionshasbeenprovidedinthesys._jitnamespace. sys._jit.is_available()canbeused
todetermineifthecurrentexecutablesupportsJITcompilation,whilesys._jit.is_enabled()canbeusedto
tellifJITcompilationhasbeenenabledforthecurrentprocess.
Currently, the most significant missing functionality is that native debuggers and profilers like gdb and perf are
unable to unwind through JIT frames (Python debuggers and profilers, like pdb or profile, continue to work
withoutmodification). Free-threadedbuildsdonotsupportJITcompilation.
Pleasereportanybugsormajorperformanceregressionsthatyouencounter!
(cid:181) Seealso
PEP744
3.16 Concurrent safe warnings control
Thewarnings.catch_warningscontextmanagerwillnowoptionallyuseacontextvariableforwarningfilters.
Thisisenabledbysettingthecontext_aware_warningsflag,eitherwiththe-Xcommand-lineoptionoranen-
vironmentvariable. Thisgivespredictablewarningscontrolwhenusingcatch_warningscombinedwithmultiple
threads or asynchronous tasks. The flag defaults to true for the free-threaded build and false for the GIL-enabled
build.
(ContributedbyNeilSchemenauerandKumarAdityaingh-130010.)
3.17 Incremental garbage collection
Thecyclegarbagecollectorisnowincremental. Thismeansthatmaximumpausetimesarereducedbyanorderof
magnitudeormoreforlargerheaps.
Therearenowonlytwogenerations: youngandold. Whengc.collect()isnotcalleddirectly,theGCisinvoked
alittlelessfrequently. Wheninvoked,itcollectstheyounggenerationandanincrementoftheoldgeneration,instead
ofcollectingoneormoregenerations.
Thebehaviorofgc.collect()changesslightly:
• gc.collect(1): Performsanincrementofgarbagecollection,ratherthancollectinggeneration1.
• Othercallstogc.collect()areunchanged.
(ContributedbyMarkShannoningh-108362.)
4 Platform support
• PEP776: Emscriptenisnowanofficiallysupportedplatformattier3. Asapartofthiseffort,morethan25
bugsinEmscriptenlibcwerefixed. Emscriptennowincludessupportforctypes,termios,andfcntl,as
wellasexperimentalsupportforPyREPL.
(ContributedbyR.HoodChathamingh-127146,gh-127683,andgh-136931.)
17

| (cid:181) Seealso |
| --- |
| PEP744 |

### 第18页

5 Other language changes
• Thedefaultinteractiveshellnowsupportsimportautocompletion. Thismeansthattypingimport fooand
pressing<tab>willsuggestmodulesstartingwithfoo. Similarly,typingfrom foo import bwillsuggest
submodulesoffoostartingwithb. Notethatautocompletionofmoduleattributesisnotcurrentlysupported.
(ContributedbyTomasRouningh-69605.)
• Themap()built-innowhasanoptionalkeyword-onlystrictflaglikezip()tocheckthatalltheiterablesare
ofequallength. (ContributedbyWannesBoeykensingh-119793.)
• Incorrect usage of await and asynchronous comprehensions is now detected even if the code is optimized
awaybythe-Ocommand-lineoption. Forexample,python -O -c 'assert await 1'nowproducesa
SyntaxError. (ContributedbyJelleZijlstraingh-121637.)
• Writesto__debug__arenowdetectedevenifthecodeisoptimizedawaybythe-Ocommand-lineoption. For
example,python -O -c 'assert (__debug__ := 1)'nowproducesaSyntaxError. (Contributed
byIritKatrielingh-122245.)
• Addclassmethodsfloat.from_number()andcomplex.from_number()toconvertanumbertofloat
or complex type correspondingly. They raise an error if the argument is a string. (Contributed by Serhiy
Storchakaingh-84978.)
• Implement mixed-mode arithmetic rules combining real and complex numbers as specified by C standards
sinceC99. (ContributedbySergeyBKirpichevingh-69639.)
• AllWindowscodepagesarenowsupportedas“cpXXX”codecsonWindows. (ContributedbySerhiyStor-
chakaingh-123803.)
• superobjectsarenowpickleableandcopyable. (ContributedbySerhiyStorchakaingh-125767.)
• Thememoryviewtypenowsupportssubscription,makingitagenerictype. (ContributedbyBrianSchubert
ingh-126012.)
• Supportunderscoreandcommaas thousandsseparatorsinthefractionalpart forfloating-pointpresentation
typesofthenew-stylestringformatting(withformat()orf-strings). (ContributedbySergeyBKirpichevin
gh-87790.)
• The bytes.fromhex() and bytearray.fromhex() methods now accept ASCII bytes and bytes-like
objects. (ContributedbyDanielPopeingh-129349.)
• Support\zasasynonymfor\Zinregular expressions. Itisinterpretedunambiguouslyinmanyother
regularexpressionengines,unlike\Z,whichhassubtlydifferentbehavior. (ContributedbySerhiyStorchaka
ingh-133306.)
• \B in regular expression now matches the empty input string. Now it is always the opposite of \b.
(ContributedbySerhiyStorchakaingh-124130.)
• iOS and macOS apps can now be configured to redirect stdout and stderr content to the system log.
(ContributedbyRussellKeith-Mageeingh-127592.)
• TheiOStestbedisnowabletostreamtestoutputwhilethetestisrunning. Thetestbedcanalsobeusedtorun
thetestsuiteofprojectsotherthanCPythonitself. (ContributedbyRussellKeith-Mageeingh-127592.)
• Three-argument pow() now tries calling __rpow__() if necessary. Previously it was only called in two-
argumentpow()andthebinarypoweroperator. (ContributedbySerhiyStorchakaingh-130104.)
• Addabuilt-inimplementationforHMAC(RFC2104)usingformallyverifiedcodefromtheHACL*project.
This implementation is used as a fallback when the OpenSSL implementation of HMAC is not available.
(ContributedbyBénédiktTraningh-99108.)
• The import time flag can now track modules that are already loaded (‘cached’), via the new -X
importtime=2. When such a module is imported, the self and cumulative times are replaced by the
stringcached. Valuesabove2for-X importtimearenowreservedforfutureuse. (ContributedbyNoah
KimandAdamTurneringh-118655.)
18

### 第19页

• When subclassing from a pure C type, the C slots for the new type are no longer replaced with a wrapped
versiononclasscreationiftheyarenotexplicitlyoverriddeninthesubclass. (ContributedbyTomaszPytelin
gh-132329.)
• The command-line option -c now automatically dedents its code argument before execution. The auto-
dedentation behavior mirrors textwrap.dedent(). (Contributed by Jon Crall and Steven Sun in gh-
103998.)
• Improveerrormessagewhenanobjectsupportingthesynchronouscontextmanagerprotocolisenteredusing
async withinsteadofwith. Andviceversawiththeasynchronouscontextmanagerprotocol. (Contributed
byBénédiktTraningh-128398.)
• -JisnolongerareservedflagforJython,andnowhasnospecialmeaning. (ContributedbyAdamTurnerin
gh-133336.)
• Theint()built-innolongerdelegatesto__trunc__(). Classesthatwanttosupportconversiontoint()
mustimplementeither__int__()or__index__(). (ContributedbyMarkDickinsoningh-119743.)
• Using NotImplemented in a boolean context will now raise a TypeError. This has raised a
DeprecationWarningsincePython3.9. (ContributedbyJelleZijlstraingh-118767.)
5.1 PEP 765: Disallow return/break/continue that exit a finally block
Thecompiler emits a SyntaxWarning whena return, break or continue statementappears where itexits a
finallyblock. ThischangeisspecifiedinPEP765.
6 New modules
• annotationlib: Forintrospectingannotations. SeePEP749formoredetails. (ContributedbyJelleZijlstra
ingh-119180.)
7 Improved modules
7.1 argparse
• Thedefaultvalueoftheprogramnamefor argparse.ArgumentParser nowreflectsthewaythePython
interpreterwasinstructedtofindthe__main__modulecode. (ContributedbySerhiyStorchakaandAlyssa
Coghlaningh-66436.)
• Introducedtheoptionalsuggest_on_error parametertoargparse.ArgumentParser,enablingsuggestions
forargumentchoicesandsubparsernamesifmistypedbytheuser. (ContributedbySavannahOstrowskiin
gh-124456.)
• Enable color for help text, which can be disabled with the optional color parameter to argparse.
ArgumentParser. This can also be controlled by environment variables. (Contributed by Hugo van Ke-
menadeingh-130645.)
7.2 ast
• Add ast.compare() for comparing two ASTs. (Contributed by Batuhan Taskaya and Jeremy Hylton in
gh-60191.)
• Addsupportforcopy.replace()forASTnodes. (ContributedbyBénédiktTraningh-121141.)
• DocstringsarenowremovedfromanoptimizedASTinoptimizationlevel2. (ContributedbyIritKatrielin
gh-123958.)
• The repr() output for AST nodes now includes more information. (Contributed by Tomas Roun in gh-
116022.)
• ast.parse(),whencalledwithanASTasinput,nowalwaysverifiesthattherootnodetypeisappropriate.
(ContributedbyIritKatrielingh-130139.)
19

### 第20页

• Add new --feature-version, --optimize, --show-empty options to the command-line interface.
(ContributedbySemyonMorozingh-133367.)
7.3 asyncio
• Thefunctionandmethodsnamedcreate_task()nowtakeanarbitrarylistofkeywordarguments. Allkey-
wordargumentsarepassedtotheTaskconstructororthecustomtaskfactory. (Seeset_task_factory()
fordetails.) Thenameandcontextkeywordargumentsarenolongerspecial; thenameshouldnowbeset
usingthenamekeywordargumentofthefactory,andcontextmaybeNone.
This affects the following function and methods: asyncio.create_task(), asyncio.loop.
create_task(), asyncio.TaskGroup.create_task(). (Contributed by Thomas Grainger in gh-
128307.)
• There are two new utility functions for introspecting and printing a program’s call graph:
capture_call_graph() and print_call_graph(). (Contributed by Yury Selivanov, Pablo Galindo
Salgado,andŁukaszLangaingh-91048.)
7.4 calendar
• Bydefault,today’sdateishighlightedincolorincalendar’scommand-linetextoutput. Thiscanbecontrolled
byenvironmentvariables. (ContributedbyHugovanKemenadeingh-128317.)
7.5 concurrent.futures
• Add InterpreterPoolExecutor, which exposes “subinterpreters” (multiple Python interpreters in the
same process) to Python code. This is separate from the proposed API in PEP 734. (Contributed by Eric
Snowingh-124548.)
• ThedefaultProcessPoolExecutorstartmethodchangedfromforktoforkserveronplatformsotherthan
macOSandWindowswhereitwasalreadyspawn.
Ifthethreadingincompatibleforkmethodisrequired,youmustexplicitlyrequestitbysupplyingamultipro-
cessingcontextmp_contexttoProcessPoolExecutor.
See forkserver restrictions for information and differences with the fork method and how this change may
affectexistingcodewithmutableglobalsharedvariablesand/orsharedobjectsthatcannotbeautomatically
pickled.
(ContributedbyGregoryP.Smithingh-84559.)
• Add concurrent.futures.ProcessPoolExecutor.terminate_workers() and concurrent.
futures.ProcessPoolExecutor.kill_workers() as ways to terminate or kill all living worker
processesinthegivenpool. (ContributedbyCharlesMachalowingh-130849.)
• Addtheoptionalbuffersizeparametertoconcurrent.futures.Executor.map()tolimitthenumber
ofsubmittedtaskswhoseresultshavenotyetbeenyielded. Ifthebufferisfull,iterationovertheiterablespauses
untilaresultisyieldedfromthebuffer. (ContributedbyEnzoBonnalandJoshRosenbergingh-74028.)
7.6 configparser
• Securityfix: willnolongerwriteconfigfilesitcannotread. Attemptingtoconfigparser.ConfigParser.
write()keyscontainingdelimitersorbeginningwiththesectionheaderpatternwillraiseaconfigparser.
InvalidWriteError. (ContributedbyJacobLincolningh-129270.)
7.7 contextvars
• Supportcontextmanagerprotocolbycontextvars.Token. (ContributedbyAndrewSvetlovingh-129889.)
20

### 第21页

7.8 ctypes
• The layout of bit fields in Structure and Union now matches platform defaults (GCC/Clang or MSVC)
moreclosely. Inparticular,fieldsnolongeroverlap. (ContributedbyMatthiasGörgensingh-97702.)
• TheStructure._layout_classattributecannowbesettohelpmatchanon-defaultABI.(Contributedby
PetrViktoriningh-97702.)
• TheclassofStructure/UnionfielddescriptorsisnowavailableasCField, andhasnewattributestoaid
debuggingandintrospection. (ContributedbyPetrViktoriningh-128715.)
• OnWindows,theCOMErrorexceptionisnowpublic. (ContributedbyJunKomodaingh-126686.)
• OnWindows,theCopyComPointer()functionisnowpublic. (ContributedbyJunKomodaingh-127275.)
• ctypes.memoryview_at() now exists to create a memoryview object that refers to the supplied pointer
andlength. Thisworkslikectypes.string_at()exceptitavoidsabuffercopy,andistypicallyusefulwhen
implementingpurePythoncallbackfunctionsthatarepasseddynamically-sizedbuffers. (ContributedbyRian
Hunteringh-112018.)
• Complex types, c_float_complex, c_double_complex and c_longdouble_complex, arenowavail-
ableifboththecompilerandthelibffilibrarysupportcomplexCtypes. (ContributedbySergeyBKirpichev
ingh-61103.)
• Addctypes.util.dllist()forlistingthesharedlibrariesloadedbythecurrentprocess. (Contributedby
BrianWardingh-119349.)
• Move ctypes.POINTER() types cache from a global internal cache (_pointer_type_cache) to the
ctypes._CData.__pointer_type__ attribute of the corresponding ctypes types. This will stop the
cachefromgrowingwithoutlimitsinsomesituations. (ContributedbySergeyMiryanovingh-100926.)
• Thectypes.py_objecttypenowsupportssubscription, makingitagenerictype. (ContributedbyBrian
Schubertingh-132168.)
• ctypesnowsupportsfree-threadingbuilds. (ContributedbyKumarAdityaandPeterBiermaingh-127945.)
7.9 curses
• Add the assume_default_colors() function, a refinement of the use_default_colors() function
whichallowstochangethecolorpair0. (ContributedbySerhiyStorchakaingh-133139.)
7.10 datetime
• Add datetime.time.strptime() and datetime.date.strptime(). (Contributed by Wannes
Boeykensingh-41431.)
7.11 decimal
• AddalternativeDecimalconstructorDecimal.from_number(). (ContributedbySerhiyStorchakaingh-
121798.)
• Expose decimal.IEEEContext() to support creation of contexts corresponding to the IEEE 754 (2008)
decimalinterchangeformats. (ContributedbySergeyBKirpichevingh-53032.)
7.12 difflib
• Comparison pages with highlighted changes generated by the difflib.HtmlDiff class now support dark
mode. (ContributedbyJiahaoLiingh-129939.)
7.13 dis
• Addsupportforrenderingfullsourcelocationinformationofinstructions,ratherthanonlythelinenum-
ber. Thisfeatureisaddedtothefollowinginterfacesviatheshow_positionskeywordargument:
– dis.Bytecode
21

### 第22页

– dis.dis()
– dis.distb()
– dis.disassemble()
Thisfeatureisalsoexposedviadis --show-positions. (ContributedbyBénédiktTraningh-123165.)
• Addthedis --specializedcommand-lineoptiontoshowspecializedbytecode. (ContributedbyBénédikt
Traningh-127413.)
7.14 errno
• Adderrno.EHWPOISONerrorcode. (ContributedbyJamesRoyingh-126585.)
7.15 faulthandler
• AddsupportforprintingtheCstacktraceonsystemsthatsupportitviafaulthandler.dump_c_stack()
orviathec_stackargumentinfaulthandler.enable(). (ContributedbyPeterBiermaingh-127604.)
7.16 fnmatch
• Addedfnmatch.filterfalse()forexcludingnamesmatchingapattern. (ContributedbyBénédiktTran
ingh-74598.)
7.17 fractions
• Addsupportforconvertinganyobjectsthathavetheas_integer_ratio()methodtoaFraction. (Con-
tributedbySerhiyStorchakaingh-82017.)
• Add alternative Fraction constructor Fraction.from_number(). (Contributed by Serhiy Storchaka in
gh-121797.)
7.18 functools
• Add support to functools.partial() and functools.partialmethod() for functools.
Placeholdersentinelstoreserveaplaceforpositionalarguments. (ContributedbyDominykasGrigonisin
gh-119127.)
• Allowtheinitialparameteroffunctools.reduce()tobepassedasakeywordargument. (Contributedby
SayandipDuttaingh-125916.)
7.19 getopt
• Addsupportforoptionswithoptionalarguments. (ContributedbySerhiyStorchakaingh-126374.)
• Add support for returning intermixed options and non-option arguments in order. (Contributed by Serhiy
Storchakaingh-126390.)
7.20 getpass
• Supportkeyboardfeedbackbygetpass.getpass()viathekeyword-onlyoptionalargumentecho_char.
Placeholdercharactersarerenderedwheneveracharacterisentered,andremovedwhenacharacterisdeleted.
(ContributedbySemyonMorozingh-77065.)
7.21 graphlib
• Allowgraphlib.TopologicalSorter.prepare()tobecalledmorethanonceaslongassortinghasnot
started. (ContributedbyDanielPopeingh-130914.)
22

### 第23页

7.22 heapq
• Addfunctionsforworkingwithmax-heaps:
– heapq.heapify_max(),
– heapq.heappush_max(),
– heapq.heappop_max(),
– heapq.heapreplace_max()
– heapq.heappushpop_max()
7.23 hmac
• Addabuilt-inimplementationforHMAC(RFC2104)usingformallyverifiedcodefromtheHACL*project.
(ContributedbyBénédiktTraningh-99108.)
7.24 http
• Directorylistsanderrorpagesgeneratedbythehttp.servermoduleallowthebrowsertoapplyitsdefault
darkmode. (ContributedbyYorikHanseningh-123430.)
• Thehttp.servermodulenowsupportsservingoverHTTPSusingthehttp.server.HTTPSServerclass.
This functionality is exposed by the command-line interface (python -m http.server) through the fol-
lowingoptions:
– --tls-cert <path>: PathtotheTLScertificatefile.
– --tls-key <path>: Optionalpathtotheprivatekeyfile.
– --tls-password-file <path>: Optionalpathtothepasswordfilefortheprivatekey.
(ContributedbySemyonMorozingh-85162.)
7.25 imaplib
• AddIMAP4.idle(),implementingtheIMAP4IDLEcommandasdefinedinRFC2177. (Contributedby
Forestingh-55454.)
7.26 inspect
• inspect.signature()takesanewargumentannotation_formattocontroltheannotationlib.Format
usedforrepresentingannotations. (ContributedbyJelleZijlstraingh-101552.)
• inspect.Signature.format()takesanewargumentunquote_annotations. Iftrue,stringannotationsare
displayedwithoutsurroundingquotes. (ContributedbyJelleZijlstraingh-101552.)
• Addfunctioninspect.ispackage()todeterminewhetheranobjectisapackageornot. (Contributedby
ZhikangYaningh-125634.)
7.27 io
• Reading text from a non-blocking stream with read may now raise a BlockingIOError if the operation
cannotimmediatelyreturnbytes. (ContributedbyGiovanniSiragusaingh-109523.)
• Add protocols io.Reader and io.Writer as simpler alternatives to the pseudo-protocols typing.IO,
typing.TextIO,andtyping.BinaryIO.(ContributedbySebastianRittauingh-127648.)
7.28 json
• AddnotesforJSONserializationerrorsthatallowtoidentifythesourceoftheerror. (ContributedbySerhiy
Storchakaingh-122163.)
23

### 第24页

• Enablethejsonmoduletoworkasascriptusingthe-mswitch:python -m json. SeetheJSONcommand-
lineinterfacedocumentation. (ContributedbyTreyHunneringh-122873.)
• Bydefault,theoutputoftheJSONcommand-lineinterfaceishighlightedincolor. Thiscanbecontrolledby
environmentvariables. (ContributedbyTomasRouningh-131952.)
7.29 linecache
• linecache.getline() can retrieve source code for frozen modules. (Contributed by Tian Gao in gh-
131638.)
7.30 logging.handlers
• logging.handlers.QueueListenernowimplementsthecontextmanagerprotocol,allowingittobeused
inawithstatement. (ContributedbyCharlesMachalowingh-132106.)
• QueueListener.start now raises a RuntimeError if the listener is already started. (Contributed by
CharlesMachalowingh-132106.)
7.31 math
• Added more detailed error messages for domain errors in the module. (Contributed by Charlie Zhao and
SergeyBKirpichevingh-101410.)
7.32 mimetypes
• Documentthecommand-lineformimetypes. Itnowexitswith1onfailureinsteadof0and2onincorrect
command-line parameters instead of 1. Also, errors are printed to stderr instead of stdout and their text is
madetighter. (ContributedbyOlegIaryginandHugovanKemenadeingh-93096.)
• AddMSandRFC8081MIMEtypesforfonts:
– EmbeddedOpenType: application/vnd.ms-fontobject
– OpenTypeLayout(OTF)font/otf
– TrueType: font/ttf
– WOFF1.0font/woff
– WOFF2.0font/woff2
(ContributedbySahilPrajapatiandHugovanKemenadeingh-84852.)
• AddRFC9559MIMEtypesforMatroskaaudiovisualdatacontainerstructures,containing:
– audiowithnovideo: audio/matroska(.mka)
– video: video/matroska(.mkv)
– stereoscopicvideo: video/matroska-3d(.mk3d)
(ContributedbyHugovanKemenadeingh-89416.)
• AddMIMEtypesforimageswithRFCs:
– RFC1494: CCITTGroup3(.g3)
– RFC3362: Real-timeFacsimile,T.38(.t38)
– RFC3745: JPEG2000(.jp2),extension(.jpx)andcompound(.jpm)
– RFC3950: TagImageFileFormatFaxeXtended,TIFF-FX(.tfx)
– RFC4047: FlexibleImageTransportSystem(.fits)
– RFC7903: EnhancedMetafile(.emf)andWindowsMetafile(.wmf)
(ContributedbyHugovanKemenadeingh-85957.)
24

### 第25页

• MoreMIMEtypechanges:
– RFC2361: Changetypefor.avitovideo/vnd.aviandfor.wavtoaudio/vnd.wave
– RFC4337: AddMPEG-4audio/mp4(.m4a)
– RFC5334: AddOggmedia(.oga,.oggand.ogx)
– RFC6713: Addgzipapplication/gzip(.gz)
– RFC9639: AddFLACaudio/flac(.flac)
– Add7zapplication/x-7z-compressed(.7z)
– AddAndroidPackageapplication/vnd.android.package-archive(.apk)whennotstrict
– Adddebapplication/x-debian-package(.deb)
– AddglTFbinarymodel/gltf-binary(.glb)
– AddglTFJSON/ASCIImodel/gltf+json(.gltf)
– AddM4Vvideo/x-m4v(.m4v)
– AddPHPapplication/x-httpd-php(.php)
– AddRARapplication/vnd.rar(.rar)
– AddRPMapplication/x-rpm(.rpm)
– AddSTLmodel/stl(.stl)
– AddWindowsMediaVideovideo/x-ms-wmv(.wmv)
– Defacto: AddWebMaudio/webm(.weba)
– ECMA-376: Add.docx,.pptxand.xlsxtypes
– OASIS:AddOpenDocument.odg,.odp,.odsand.odttypes
– W3C:AddEPUBapplication/epub+zip(.epub)
(ContributedbyHugovanKemenadeingh-129965.)
• AddRFC9512application/yamlMIMEtypeforYAMLfiles(.yamland.yml). (ContributedbySasha
“Nelie”ChernykhandHugovanKemenadeingh-132056.)
7.33 multiprocessing
• ThedefaultstartmethodchangedfromforktoforkserveronplatformsotherthanmacOSandWindowswhere
itwasalreadyspawn.
If the threading incompatible fork method is required, you must explicitly request it via a context
from multiprocessing.get_context() (preferred) or change the default via multiprocessing.
set_start_method().
See forkserver restrictions for information and differences with the fork method and how this change may
affectexistingcodewithmutableglobalsharedvariablesand/orsharedobjectsthatcannotbeautomatically
pickled.
(ContributedbyGregoryP.Smithingh-84559.)
• multiprocessing’s"forkserver"startmethodnowauthenticatesitscontrolsockettoavoidsolelyrelying
onfilesystempermissionstorestrictwhatotherprocessescouldcausetheforkservertospawnworkersandrun
code. (ContributedbyGregoryP.Smithforgh-97514.)
• Themultiprocessingproxyobjectsforlistanddicttypesgainpreviouslyoverlookedmissingmethods:
– clear()andcopy()forproxiesoflist
– fromkeys(),reversed(d),d | {},{} | d,d |= {'b': 2}forproxiesofdict
(ContributedbyRoyHyunjinHanforgh-103134.)
25

### 第26页

• Add support for shared set objects via SyncManager.set(). The set() in multiprocessing.
Manager()methodisnowavailable. (ContributedbyMingyuParkingh-129949.)
• Addmultiprocessing.Process.interrupt()whichterminatesthechildprocessbysendingSIGINT.
Thisenablesfinallyclausestoprintastacktracefortheterminatedprocess. (ContributedbyArtemPulkin
ingh-131913.)
7.34 operator
• Two new functions operator.is_none() and operator.is_not_none() have been added, such that
operator.is_none(obj)isequivalenttoobj is Noneandoperator.is_not_none(obj)isequiv-
alenttoobj is not None. (ContributedbyRaymondHettingerandNicoMexisingh-115808.)
7.35 os
• Addtheos.reload_environ()functiontoupdateos.environandos.environbwithchangestothe
environment made by os.putenv(), by os.unsetenv(), or made outside Python in the same process.
(ContributedbyVictorStinneringh-120057.)
• AddtheSCHED_DEADLINEandSCHED_NORMALconstantstotheosmodule. (ContributedbyJamesRoyin
gh-127688.)
• Addtheos.readinto()functiontoreadintoabufferobjectfromafiledescriptor. (ContributedbyCody
Maloneyingh-129205.)
7.36 os.path
• The strict parameterto os.path.realpath() accepts a new value, os.path.ALLOW_MISSING. If used,
errorsotherthanFileNotFoundErrorwillbere-raised;theresultingpathcanbemissingbutitwillbefree
ofsymlinks. (ContributedbyPetrViktorinforCVE2025-4517.)
7.37 pathlib
• Addmethodstopathlib.Pathtorecursivelycopyormovefilesanddirectories:
– copy()copiesafileordirectorytreetoadestination.
– copy_into()copiesintoadestinationdirectory.
– move()movesafileordirectorytreetoadestination.
– move_into()movesintoadestinationdirectory.
(ContributedbyBarneyGaleingh-73991.)
• Addpathlib.Path.infoattribute,whichstoresanobjectimplementingthepathlib.types.PathInfo
protocol(alsonew). Theobjectsupportsqueryingthefiletypeandinternallycachingstat()results. Path
objectsgeneratedbyiterdir()areinitializedwithfiletypeinformationgleanedfromscanningtheparent
directory. (ContributedbyBarneyGaleingh-125413.)
7.38 pdb
• Hardcodedbreakpoints(breakpoint()andpdb.set_trace())nowreusethemostrecentPdbinstance
thatcallsset_trace(), insteadofcreatinganewoneeachtime. Asaresult, alltheinstancespecificdata
likedisplayandcommandsarepreservedacrosshardcodedbreakpoints. (ContributedbyTianGaoingh-
121450.)
• Add a new argument mode to pdb.Pdb. Disable the restart command when pdb is in inline mode.
(ContributedbyTianGaoingh-123757.)
• Aconfirmationpromptwillbeshownwhentheusertriestoquitpdbininlinemode. y,Y,<Enter>orEOF
willconfirmthequitandcallsys.exit(),insteadofraisingbdb.BdbQuit. (ContributedbyTianGaoin
gh-124704.)
26

### 第27页

• Inlinebreakpointslikebreakpoint()orpdb.set_trace()willalwaysstoptheprogramatcallingframe,
ignoringtheskippattern(ifany). (ContributedbyTianGaoingh-130493.)
• <tab> at the beginning of the line in pdb multi-line input will fill in a 4-space indentation now, instead of
insertinga\tcharacter. (ContributedbyTianGaoingh-130471.)
• Auto-indentisintroducedinpdbmulti-lineinput. Itwilleitherkeeptheindentationofthelastlineorinserta
4-spaceindentationwhenitdetectsanewcodeblock. (ContributedbyTianGaoingh-133350.)
• $_asynctask is added to access the current asyncio task if applicable. (Contributed by Tian Gao in gh-
124367.)
• pdb.set_trace_async() is added to support debugging asyncio coroutines. await statements are sup-
portedwiththisfunction. (ContributedbyTianGaoingh-132576.)
• Sourcecodedisplayedinpdbwillbesyntax-highlighted. Thisfeaturecanbecontrolledusingthesamemethods
asPyREPL,inadditiontothenewlyaddedcolorizeargumentofpdb.Pdb. (ContributedbyTianGaoand
ŁukaszLangaingh-133355.)
7.39 pickle
• Setthedefaultprotocolversiononthepicklemoduleto5. Formoredetails,seepickleprotocols.
• Addnotesforpickleserializationerrorsthatallowtoidentifythesourceoftheerror. (ContributedbySerhiy
Storchakaingh-122213.)
7.40 platform
• Addplatform.invalidate_caches()toinvalidatethecachedresults. (ContributedbyBénédiktTranin
gh-122549.)
7.41 pydoc
• Annotationsinhelpoutputarenowusuallydisplayedinaformatclosertothatintheoriginalsource. (Con-
tributedbyJelleZijlstraingh-101552.)
7.42 socket
• ImproveandfixsupportforBluetoothsockets.
– FixsupportofBluetoothsocketsonNetBSDandDragonFlyBSD.(ContributedbySerhiyStorchakain
gh-132429.)
– FixsupportforBTPROTO_HCIonFreeBSD.(ContributedbyVictorStinneringh-111178.)
– AddsupportforBTPROTO_SCOonFreeBSD.(ContributedbySerhiyStorchakaingh-85302.)
– Addsupportforcidandbdaddr_typeintheaddressforBTPROTO_L2CAPonFreeBSD.(Contributedby
SerhiyStorchakaingh-132429.)
– AddsupportforchannelintheaddressforBTPROTO_HCIonLinux. (ContributedbySerhiyStorchaka
ingh-70145.)
– Accept an integer as the address for BTPROTO_HCI on Linux. (Contributed by Serhiy Storchaka in
gh-132099.)
– Returncidingetsockname()forBTPROTO_L2CAP.(ContributedbySerhiyStorchakaingh-132429.)
– Addmanynewconstants. (ContributedbySerhiyStorchakaingh-132734.)
7.43 ssl
• Indicatethroughssl.HAS_PHAwhetherthesslmodulesupportsTLSv1.3post-handshakeclientauthenti-
cation(PHA).(ContributedbyWillChilds-Kleiningh-128036.)
27

### 第28页

7.44 struct
• Supportthefloat complexanddouble complexCtypesinthestructmodule(formattingcharacters
'F'and'D'respectively). (ContributedbySergeyBKirpichevingh-121249.)
7.45 symtable
• Exposethefollowingsymtable.Symbolmethods:
– is_comp_cell()
– is_comp_iter()
– is_free_class()
(ContributedbyBénédiktTraningh-120029.)
7.46 sys
• Thepreviouslyundocumentedspecialfunctionsys.getobjects(),whichonlyexistsinspecializedbuilds
ofPython,maynowreturnobjectsfromotherinterpretersthantheoneit’scalledin.
• Addsys._is_immortal()fordeterminingifanobjectisimmortal. (ContributedbyPeterBiermaingh-
128509.)
• OnFreeBSD,sys.platformdoesn’tcontainthemajorversionanymore. Itisalways'freebsd',instead
of'freebsd13'or'freebsd14'.
• RaiseDeprecationWarningforsys._clear_type_cache(). ThisfunctionwasdeprecatedinPython
3.13butitdidn’traisearuntimewarning.
7.47 sys.monitoring
• Twoneweventsareadded: BRANCH_LEFTandBRANCH_RIGHT.TheBRANCHeventisdeprecated.
7.48 sysconfig
• Add ABIFLAGS key to sysconfig.get_config_vars() on Windows. (Contributed by Xuehai Pan in
gh-131799.)
7.49 tarfile
• data_filter()nownormalizessymboliclinktargetsinordertoavoidpathtraversalattacks. (Contributed
byPetrViktoriningh-127987andCVE2025-4138.)
• extractall()nowskipsfixingupdirectoryattributeswhenadirectorywasremovedorreplacedbyanother
kindoffile. (ContributedbyPetrViktoriningh-127987andCVE2024-12718.)
• extract()andextractall()now(re-)applytheextractionfilterwhensubstitutingalink(hardorsym-
bolic)withacopyofanotherarchivemember, andwhenfixingupdirectoryattributes. Theformerraisesa
newexception,LinkFallbackError. (ContributedbyPetrViktorinforCVE2025-4330andCVE2024-
12718.)
• extract()andextractall()nolongerextractrejectedmemberswhenerrorlevel()iszero. (Con-
tributedbyMattProdaniandPetrViktoriningh-112887andCVE2025-4435.)
7.50 threading
• threading.Thread.start()nowsetstheoperatingsystemthreadnametothreading.Thread.name.
(ContributedbyVictorStinneringh-59705.)
28

### 第29页

7.51 tkinter
• Maketkinterwidgetmethodsafter()andafter_idle()acceptargumentspassedbykeyword. (Con-
tributedbyZhikangYaningh-126899.)
• Addabilitytospecifynamefortkinter.OptionMenuandtkinter.ttk.OptionMenu. (Contributedby
ZhikangYaningh-130482.)
7.52 turtle
• Add context managers for turtle.fill(), turtle.poly() and turtle.no_animation(). (Con-
tributedbyMarieRoaldandYngveMardalMoeingh-126350.)
7.53 types
• types.UnionTypeisnowanaliasfortyping.Union. Seebelowformoredetails. (ContributedbyJelle
Zijlstraingh-105499.)
7.54 typing
• types.UnionTypeandtyping.Unionarenowaliasesforeachother,meaningthatbothold-styleunions
(createdwithUnion[int, str])andnew-styleunions(int | str)nowcreateinstancesofthesamerun-
timetype. Thisunifiesthebehaviorbetweenthetwosyntaxes,butleadstosomedifferencesinbehaviorthat
mayaffectuserswhointrospecttypesatruntime:
– Bothsyntaxesforcreatingaunionnowproducethesamestringrepresentationinrepr(). Forexample,
repr(Union[int, str])isnow"int | str"insteadof"typing.Union[int, str]".
– Unions created using the old syntax are no longer cached. Previously, running Union[int, str]
multiple times would return the same object (Union[int, str] is Union[int, str] would be
True),butnowitwillreturntwodifferentobjects. Usersshoulduse==tocompareunionsforequality,
notis. New-styleunionshaveneverbeencachedthisway. Thischangecouldincreasememoryusage
forsomeprogramsthatusealargenumberofunionscreatedbysubscriptingtyping.Union. However,
severalfactorsoffsetthiscost: unionsusedinannotationsarenolongerevaluatedbydefaultinPython
3.14 because of PEP 649; an instance of types.UnionType is itself much smaller than the object
returnedbyUnion[]wasonpriorPythonversions;andremovingthecachealsosavessomespace. Itis
thereforeunlikelythatthischangewillcauseasignificantincreaseinmemoryusageformostusers.
– Previously,old-styleunionswereimplementedusingtheprivateclasstyping._UnionGenericAlias.
Thisclassisnolongerneededfortheimplementation, butithasbeenretainedforbackwardcompati-
bility, with removal scheduled for Python 3.17. Users should use documented introspection helpers
liketyping.get_origin()andtyping.get_args()insteadofrelyingonprivateimplementation
details.
– It is now possible to use typing.Union itself in isinstance() checks. For example,
isinstance(int | str, typing.Union)willreturnTrue;previouslythisraisedTypeError.
– The__args__attributeoftyping.Unionobjectsisnolongerwritable.
– Itisnolongerpossibletosetanyattributesontyping.Unionobjects. Thisonlyeverworkedfordunder
attributesonpreviousversions,wasneverdocumentedtowork,andwassubtlybrokeninmanycases.
(ContributedbyJelleZijlstraingh-105499.)
• typing.TypeAliasTypenowsupportsstarunpacking.
7.55 unicodedata
• TheUnicodedatabasehasbeenupdatedtoUnicode16.0.0.
29

### 第30页

7.56 unittest
• unittestoutputisnowcoloredbydefault. Thiscanbecontrolledbyenvironmentvariables. (Contributed
byHugovanKemenadeingh-127221.)
• unittestdiscoverysupportsnamespacepackageasstartdirectoryagain. ItwasremovedinPython3.11. (Con-
tributedbyJacobWallsingh-80958.)
• AnumberofnewmethodswereaddedintheTestCaseclassthatprovidemorespecializedtests.
– assertHasAttr()andassertNotHasAttr()checkwhethertheobjecthasaparticularattribute.
– assertIsSubclass() and assertNotIsSubclass() check whether the object is a subclass of a
particularclass,orofoneofatupleofclasses.
– assertStartsWith(), assertNotStartsWith(), assertEndsWith() and
assertNotEndsWith() check whether the Unicode or byte string starts or ends with particular
strings.
(ContributedbySerhiyStorchakaingh-71339.)
7.57 urllib
• UpgradeHTTPdigestauthenticationalgorithmforurllib.requestbysupportingSHA-256digestauthen-
ticationasspecifiedinRFC7616. (ContributedbyCalvinBuiingh-128193.)
• Improveergonomicsandstandardscompliancewhenparsingandemittingfile: URLs.
Inurllib.request.url2pathname():
– AcceptacompleteURLwhenthenewrequire_schemeargumentissettotrue.
– DiscardURLauthorityifitmatchesthelocalhostname.
– DiscardURLauthorityifitresolvestoalocalIPaddresswhenthenewresolve_host argumentissetto
true.
– DiscardURLqueryandfragmentcomponents.
– Raise URLError if a URL authority isn’t local, except on Windows where we return a UNC path as
before.
Inurllib.request.pathname2url():
– ReturnacompleteURLwhenthenewadd_schemeargumentissettotrue.
– IncludeanemptyURLauthoritywhenapathbeginswithaslash. Forexample,thepath/etc/hosts
isconvertedtotheURL///etc/hosts.
OnWindows,drivelettersarenolongerconvertedtouppercase,and: charactersnotfollowingadriveletter
nolongercauseanOSErrorexceptiontoberaised.
(ContributedbyBarneyGaleingh-125866.)
7.58 uuid
• Add support for UUID versions 6, 7, and 8 via uuid.uuid6(), uuid.uuid7(), and uuid.uuid8() re-
spectively,asspecifiedinRFC9562. (ContributedbyBénédiktTraningh-89083.)
• uuid.NILanduuid.MAXarenowavailabletorepresenttheNilandMaxUUIDformatsasdefinedbyRFC
9562. (ContributedbyNickPopeingh-128427.)
• AllowtogeneratemultipleUUIDsatonceviapython -m uuid --count. (ContributedbySimonLegner
ingh-131236.)
30

### 第31页

7.59 webbrowser
• NamesintheBROWSERenvironmentvariablecannowrefertoalreadyregisteredbrowsersforthewebbrowser
module,insteadofalwaysgeneratinganewbrowsercommand.
ThismakesitpossibletosetBROWSERtothevalueofoneofthesupportedbrowsersonmacOS.
7.60 zipfile
• Added ZipInfo._for_archive to resolve suitable defaults for a ZipInfo object as used by ZipFile.
writestr. (ContributedbyBénédiktTraningh-123424.)
• zipfile.ZipFile.writestr() now respects SOURCE_DATE_EPOCH that distributions can set centrally
and have build tools consume this in order to produce reproducible output. (Contributed by Jiahao Li in
gh-91279.)
8 Optimizations
• Theimporttimeforseveralstandardlibrarymoduleshasbeenimproved, includingannotationlib, ast,
asyncio, base64, cmd, csv, gettext, importlib.util, locale, mimetypes, optparse, pickle,
pprint,pstats,shlex,socket,string,subprocess,threading,tomllib,types,andzipfile.
(Contributed by Adam Turner, Bénédikt Tran, Chris Markiewicz, Eli Schwartz, Hugo van Kemenade, Jelle
Zijlstra,andothersingh-118761.)
8.1 asyncio
• Standard benchmark results have improved by 10-20%, following the implementation of a new per-thread
doublelinkedlistfornative tasks,alsoreducingmemoryusage. Thisenablesexternalintrospectiontools
suchaspython-masynciopstreetointrospectthecallgraphofasynciotasksrunninginallthreads. (Contributed
byKumarAdityaingh-107803.)
• Themodulenowhasfirstclasssupportforfree-threadingbuilds. Thisenablesparallelexecutionofmultiple
eventloopsacrossdifferentthreads,scalinglinearlywiththenumberofthreads. (ContributedbyKumarAditya
ingh-128002.)
8.2 base64
• b16decode()isnowuptosixtimesfaster. (ContributedbyBénédiktTran, ChrisMarkiewicz, andAdam
Turneringh-118761.)
8.3 bdb
• The basic debugger now has a sys.monitoring-based backend, which can be selected via the passing
'monitoring'totheBdbclass’snewbackendparameter. (ContributedbyTianGaoingh-124533.)
8.4 difflib
• TheIS_LINE_JUNK()functionisnowuptotwiceasfast. (ContributedbyAdamTurnerandSemyonMoroz
ingh-130167.)
8.5 gc
• Thenewincrementalgarbagecollectormeansthatmaximumpausetimesarereducedbyanorderofmagnitude
ormoreforlargerheaps.
Becauseofthisoptimization,themeaningoftheresultsofget_threshold()andset_threshold()have
changed,alongwithget_count()andget_stats().
31

### 第32页

– Forbackwardscompatibility,get_threshold()continuestoreturnathree-itemtuple. Thefirstvalue
isthethresholdforyoungcollections, asbefore; thesecondvaluedeterminestherateatwhichtheold
collectionisscanned(thedefaultis10,andhighervaluesmeanthattheoldcollectionisscannedmore
slowly). Thethirdvalueisnowmeaninglessandisalwayszero.
– set_threshold()nowignoresanyitemsafterthesecond.
– get_count()andget_stats()continuetoreturnthesameformatofresults. Theonlydifferenceis
thatinsteadoftheresultsreferringtotheyoung,agingandoldgenerations,theresultsrefertotheyoung
generationandtheagingandcollectingspacesoftheoldgeneration.
Insummary,codethatattemptedtomanipulatethebehaviorofthecycleGCmaynotworkexactlyasintended,
butitisveryunlikelytobeharmful. Allothercodewillworkjustfine.
(ContributedbyMarkShannoningh-108362.)
8.6 io
• Openingandreadingfilesnowexecutesfewersystemcalls. Readingasmalloperatingsystemcachedfilein
fullisupto15%faster. (ContributedbyCodyMaloneyandVictorStinneringh-120754andgh-90102.)
8.7 pathlib
• Path.read_bytesnowusesunbufferedmodetoopenfiles,whichisbetween9%and17%fastertoreadin
full. (ContributedbyCodyMaloneyingh-120754.)
8.8 pdb
• pdb now supports two backends, based on either sys.settrace() or sys.monitoring. Using the pdb
CLIorbreakpoint()willalwaysusethesys.monitoringbackend. Explicitlyinstantiatingpdb.Pdband
itsderivedclasseswillusethesys.settrace()backendbydefault,whichisconfigurable. (Contributedby
TianGaoingh-124533.)
8.9 uuid
• uuid3() and uuid5() are now both roughly 40% faster for 16-byte names and 20% faster for 1024-byte
names. Performanceforlongernamesremainsunchanged. (ContributedbyBénédiktTraningh-128150.)
• uuid4()isnowc. 30%faster. (ContributedbyBénédiktTraningh-128150.)
8.10 zlib
• OnWindows, zlib-ngisnowusedastheimplementationofthezlibmoduleinthedefaultbinaries. There
arenoknownincompatibilitiesbetweenzlib-ngandthepreviously-usedzlibimplementation. Thisshould
resultinbetterperformanceatallcompressionlevels.
Itisworthnotingthatzlib.Z_BEST_SPEED(1)mayresultinsignificantlylesscompressionthantheprevious
implementation,whilstalsosignificantlyreducingthetimetakentocompress.
(ContributedbySteveDoweringh-91349.)
9 Removed
9.1 argparse
• Removethetype,choices,andmetavar parametersofBooleanOptionalAction. Thesehavebeendepre-
catedsincePython3.12. (ContributedbyNikitaSobolevingh-118805.)
• Calling add_argument_group() on an argument group now raises a ValueError. Similarly,
add_argument_group() or add_mutually_exclusive_group() on a mutually exclusive group now
32

### 第33页

bothraiseValueErrors. This‘nesting’wasneversupported,oftenfailedtoworkcorrectly,andwasuninten-
tionallyexposedthroughinheritance. ThisfunctionalityhasbeendeprecatedsincePython3.11. (Contributed
bySavannahOstrowskiingh-127186.)
9.2 ast
• Removethefollowingclasses, whichhavebeendeprecatedaliasesofConstantsincePython3.8andhave
emitteddeprecationwarningssincePython3.12:
– Bytes
– Ellipsis
– NameConstant
– Num
– Str
As a consequence of these removals, user-defined visit_Num, visit_Str, visit_Bytes,
visit_NameConstant and visit_Ellipsis methods on custom NodeVisitor subclasses will no
longer be called when the NodeVisitor subclass is visiting an AST. Define a visit_Constant method
instead.
(ContributedbyAlexWaygoodingh-119562.)
• Removethefollowingdeprecatedpropertiesonast.Constant, whichwerepresentforcompatibilitywith
thenow-removedASTclasses:
– Constant.n
– Constant.s
UseConstant.valueinstead. (ContributedbyAlexWaygoodingh-119562.)
9.3 asyncio
• Removethefollowingclasses,methods,andfunctions,whichhavebeendeprecatedsincePython3.12:
– AbstractChildWatcher
– FastChildWatcher
– MultiLoopChildWatcher
– PidfdChildWatcher
– SafeChildWatcher
– ThreadedChildWatcher
– AbstractEventLoopPolicy.get_child_watcher()
– AbstractEventLoopPolicy.set_child_watcher()
– get_child_watcher()
– set_child_watcher()
(ContributedbyKumarAdityaingh-120804.)
• asyncio.get_event_loop()nowraisesaRuntimeErrorifthereisnocurrenteventloop,andnolonger
implicitlycreatesaneventloop.
(ContributedbyKumarAdityaingh-126353.)
There’safewpatternsthatuseasyncio.get_event_loop(),mostofthemcanbereplacedwithasyncio.
run().
Ifyou’rerunninganasyncfunction,simplyuseasyncio.run().
Before:
33

### 第34页

async def main():
...
loop = asyncio.get_event_loop()
try:
loop.run_until_complete(main())
finally:
loop.close()
After:
async def main():
...
asyncio.run(main())
Ifyouneedtostartsomething,forexample,aserverlisteningonasocketandthenrunforever,useasyncio.
run()andanasyncio.Event.
Before:
def start_server(loop): ...
loop = asyncio.get_event_loop()
try:
start_server(loop)
loop.run_forever()
finally:
loop.close()
After:
def start_server(loop): ...
async def main():
start_server(asyncio.get_running_loop())
await asyncio.Event().wait()
asyncio.run(main())
Ifyouneedtorunsomethinginaneventloop,thenrunsomeblockingcodearoundit,useasyncio.Runner.
Before:
async def operation_one(): ...
def blocking_code(): ...
async def operation_two(): ...
loop = asyncio.get_event_loop()
try:
loop.run_until_complete(operation_one())
blocking_code()
loop.run_until_complete(operation_two())
finally:
loop.close()
After:
34

### 第35页

async def operation_one(): ...
def blocking_code(): ...
async def operation_two(): ...
with asyncio.Runner() as runner:
runner.run(operation_one())
blocking_code()
runner.run(operation_two())
9.4 email
• Removeemail.utils.localtime()’sisdstparameter,whichwasdeprecatedinandhasbeenignoredsince
Python3.12. (ContributedbyHugovanKemenadeingh-118798.)
9.5 importlib.abc
• Removedeprecatedimportlib.abcclasses:
– ResourceReader(useTraversableResources)
– Traversable(useTraversable)
– TraversableResources(useTraversableResources)
(ContributedbyJasonR.CoombsandHugovanKemenadeingh-93963.)
9.6 itertools
• Removesupportforcopy,deepcopy,andpickleoperationsfromitertoolsiterators. Thesehaveemitteda
DeprecationWarningsincePython3.12. (ContributedbyRaymondHettingeringh-101588.)
9.7 pathlib
• RemovesupportforpassingadditionalkeywordargumentstoPath. Inpreviousversions,anysucharguments
areignored. (ContributedbyBarneyGaleingh-74033.)
• Remove support for passing additional positional arguments to PurePath.relative_to() and
is_relative_to(). Inpreviousversions,anysuchargumentsarejoinedontoother. (ContributedbyBarney
Galeingh-78707.)
9.8 pkgutil
• Removetheget_loader()andfind_loader()functions,whichhavebeendeprecatedsincePython3.12.
(ContributedbyBénédiktTraningh-97850.)
9.9 pty
• Removethemaster_open()andslave_open()functions,whichhavebeendeprecatedsincePython3.12.
Usepty.openpty()instead. (ContributedbyNikitaSobolevingh-118824.)
9.10 sqlite3
• Remove version and version_info from the sqlite3 module; use sqlite_version and
sqlite_version_infofortheactualversionnumberoftheruntimeSQLitelibrary. (ContributedbyHugo
vanKemenadeingh-118924.)
• Using a sequence of parameters with named placeholders now raises a ProgrammingError, having been
deprecatedsincePython3.12. (ContributedbyErlendE.Aaslandingh-118928andgh-101693.)
35

### 第36页

9.11 urllib
• RemovetheQuoterclassfromurllib.parse,whichhasbeendeprecatedsincePython3.11. (Contributed
byNikitaSobolevingh-118827.)
• Remove the URLopener and FancyURLopener classes from urllib.request, which have been depre-
catedsincePython3.3.
myopener.open() can be replaced with urlopen(). myopener.retrieve() can be replaced with
urlretrieve(). Customisations to the opener classes can be replaced by passing customized handlers to
build_opener(). (ContributedbyBarneyGaleingh-84850.)
10 Deprecated
10.1 New deprecations
• Passing a complex number as the real or imag argument in the complex() constructor is now deprecated;
complexnumbersshouldonlybepassedasasinglepositionalargument. (ContributedbySerhiyStorchakain
gh-109218.)
• argparse:
– Passingtheundocumentedkeywordargumentprefix_charstotheadd_argument_group()methodis
nowdeprecated. (ContributedbySavannahOstrowskiingh-125563.)
– Deprecated the argparse.FileType type converter. Anything relating to resource management
should be handled downstream, after the arguments have been parsed. (Contributed by Serhiy Stor-
chakaingh-58032.)
• asyncio:
– Theasyncio.iscoroutinefunction()isnowdeprecatedandwillberemovedinPython3.16;use
inspect.iscoroutinefunction() instead. (Contributed by Jiahao Li and Kumar Aditya in gh-
122875.)
– TheasynciopolicysystemisdeprecatedandwillberemovedinPython3.16. Inparticular,thefollow-
ingclassesandfunctionsaredeprecated:
∗ asyncio.AbstractEventLoopPolicy
∗ asyncio.DefaultEventLoopPolicy
∗ asyncio.WindowsSelectorEventLoopPolicy
∗ asyncio.WindowsProactorEventLoopPolicy
∗ asyncio.get_event_loop_policy()
∗ asyncio.set_event_loop_policy()
Users should use asyncio.run() or asyncio.Runner with the loop_factory argument to use the
desiredeventloopimplementation.
Forexample,touseasyncio.SelectorEventLooponWindows:
import asyncio
async def main():
...
asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)
(ContributedbyKumarAdityaingh-127949.)
• codecs: Thecodecs.open()functionisnowdeprecated,andwillberemovedinafutureversionofPython.
Useopen()instead. (ContributedbyInadaNaokiingh-133036.)
36

### 第37页

• ctypes:
– Onnon-Windowsplatforms,settingStructure._pack_touseaMSVC-compatibledefaultmemory
layoutisnow deprecatedinfavor ofsetting Structure._layout_ to 'ms', andwill be removed in
Python3.19. (ContributedbyPetrViktoriningh-131747.)
– Calling ctypes.POINTER() on a string is now deprecated. Use incomplete types for self-referential
structures. Also, the internal ctypes._pointer_type_cache is deprecated. See ctypes.
POINTER()forupdatedimplementationdetails. (ContributedbySergeyMyrianovingh-100926.)
• functools: CallingthePythonimplementationoffunctools.reduce()withfunctionorsequenceaskey-
wordargumentsisnowdeprecated;theparameterswillbemadepositional-onlyinPython3.16. (Contributed
byKirillPodoprigoraingh-121676.)
• logging: Supportforcustomlogginghandlerswiththestrmargumentisnowdeprecatedandscheduledfor
removalinPython3.16. Definehandlerswiththestreamargumentinstead. (ContributedbyMariuszFelisiak
ingh-115032.)
• mimetypes: Valid extensions are either empty or must start with ‘.’ for mimetypes.MimeTypes.
add_type(). UndottedextensionsaredeprecatedandwillraiseaValueErrorinPython3.16. (Contributed
byHugovanKemenadeingh-75223.)
• nturl2path: This module is now deprecated. Call urllib.request.url2pathname() and
pathname2url()instead. (ContributedbyBarneyGaleingh-125866.)
• os: The os.popen() and os.spawn* functions are now soft deprecated. They should no longer be used
to write new code. The subprocess module is recommended instead. (Contributed by Victor Stinner in
gh-120743.)
• pathlib: pathlib.PurePath.as_uri() is now deprecated and scheduled for removal in Python 3.19.
Usepathlib.Path.as_uri()instead. (ContributedbyBarneyGaleingh-123599.)
• pdb: The undocumented pdb.Pdb.curframe_locals attribute is now a deprecated read-only property,
whichwillberemovedinafutureversionofPython. Thelowoverheaddynamicframelocalsaccessaddedin
Python3.13byPEP667meanstheframelocalscachereferencepreviouslystoredinthisattributeisnolonger
needed. Deriveddebuggersshouldaccesspdb.Pdb.curframe.f_localsdirectlyinPython3.13andlater
versions. (ContributedbyTianGaoingh-124369andgh-125951.)
• symtable: Deprecate symtable.Class.get_methods() due to the lack of interest, scheduled for re-
movalinPython3.16. (ContributedbyBénédiktTraningh-119698.)
• tkinter: The tkinter.Variable methods trace_variable(), trace_vdelete() and
trace_vinfo() are now deprecated. Use trace_add(), trace_remove() and trace_info()
instead. (ContributedbySerhiyStorchakaingh-120220.)
• urllib.parse: Acceptingobjectswithfalsevalues(like0and[])exceptemptystrings,bytes-likeobjects
andNoneinparse_qsl()andparse_qs()isnowdeprecated. (ContributedbySerhiyStorchakaingh-
116897.)
10.2 Pending removal in Python 3.15
• Theimportsystem:
– Setting __cached__ on a module while failing to set __spec__.cached is deprecated. In Python
3.15, __cached__ will cease to be set or take into consideration by the import system or standard
library. (gh-97879)
– Setting __package__ on a module while failing to set __spec__.parent is deprecated. In Python
3.15, __package__ will cease to be set or take into consideration by the import system or standard
library. (gh-97879)
• ctypes:
– Theundocumentedctypes.SetPointerType()functionhasbeendeprecatedsincePython3.13.
• http.server:
37

### 第38页

– TheobsoleteandrarelyusedCGIHTTPRequestHandlerhasbeendeprecatedsincePython3.13. No
directreplacementexists. AnythingisbetterthanCGItointerfaceawebserverwitharequesthandler.
– The--cgiflagtothepython -m http.servercommand-lineinterfacehasbeendeprecatedsince
Python3.13.
• importlib:
– load_module()method: useexec_module()instead.
• locale:
– The getdefaultlocale() function has been deprecated since Python 3.11. Its removal was origi-
nallyplannedforPython3.13(gh-90817),buthasbeenpostponedtoPython3.15. Usegetlocale(),
setlocale(),andgetencoding()instead. (ContributedbyHugovanKemenadeingh-111187.)
• pathlib:
– PurePath.is_reserved()hasbeendeprecatedsincePython3.13. Useos.path.isreserved()
todetectreservedpathsonWindows.
• platform:
– java_ver() hasbeendeprecatedsincePython3.13. ThisfunctionisonlyusefulforJythonsupport,
hasaconfusingAPI,andislargelyuntested.
• sysconfig:
– The check_home argument of sysconfig.is_python_build() has been deprecated since Python
3.12.
• threading:
– RLock() will take no arguments in Python 3.15. Passing any arguments has been deprecated since
Python3.14,asthePythonversiondoesnotpermitanyarguments,buttheCversionallowsanynumber
ofpositionalorkeywordarguments,ignoringeveryargument.
• types:
– types.CodeType: Accessingco_lnotabwasdeprecatedinPEP626since3.10andwasplannedto
beremovedin3.12,butitonlygotaproperDeprecationWarningin3.12. Mayberemovedin3.15.
(ContributedbyNikitaSobolevingh-101866.)
• typing:
– The undocumented keyword argument syntax for creating NamedTuple classes (for example, Point
= NamedTuple("Point", x=int, y=int))hasbeendeprecatedsincePython3.13. Usetheclass-
basedsyntaxorthefunctionalsyntaxinstead.
– WhenusingthefunctionalsyntaxofTypedDicts,failingtopassavaluetothefieldsparameter(TD =
TypedDict("TD"))orpassingNone(TD = TypedDict("TD", None))hasbeendeprecatedsince
Python 3.13. Use class TD(TypedDict): pass or TD = TypedDict("TD", {}) to create a
TypedDictwithzerofield.
– The typing.no_type_check_decorator() decorator function has been deprecated since Python
3.13. Aftereightyearsinthetypingmodule,ithasyettobesupportedbyanymajortypechecker.
• wave:
– The getmark(), setmark(), and getmarkers() methods of the Wave_read and Wave_write
classeshavebeendeprecatedsincePython3.13.
• zipimport:
– load_module()hasbeendeprecatedsincePython3.10. Useexec_module()instead. (Contributed
byJiahaoLiingh-125746.)
38

### 第39页

10.3 Pending removal in Python 3.16
• Theimportsystem:
– Setting __loader__ on a module while failing to set __spec__.loader is deprecated. In Python
3.16,__loader__willceasetobesetortakenintoconsiderationbytheimportsystemorthestandard
library.
• array:
– The'u'formatcode(wchar_t)hasbeendeprecatedindocumentationsincePython3.3andatruntime
sincePython3.13. Usethe'w'formatcode(Py_UCS4)forUnicodecharactersinstead.
• asyncio:
– asyncio.iscoroutinefunction() is deprecated and will be removed in Python 3.16; use
inspect.iscoroutinefunction() instead. (Contributed by Jiahao Li and Kumar Aditya in gh-
122875.)
– asynciopolicysystemisdeprecatedandwillberemovedinPython3.16. Inparticular,thefollowing
classesandfunctionsaredeprecated:
∗ asyncio.AbstractEventLoopPolicy
∗ asyncio.DefaultEventLoopPolicy
∗ asyncio.WindowsSelectorEventLoopPolicy
∗ asyncio.WindowsProactorEventLoopPolicy
∗ asyncio.get_event_loop_policy()
∗ asyncio.set_event_loop_policy()
Usersshoulduseasyncio.run()orasyncio.Runnerwithloop_factorytousethedesiredeventloop
implementation.
Forexample,touseasyncio.SelectorEventLooponWindows:
import asyncio
async def main():
...
asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)
(ContributedbyKumarAdityaingh-127949.)
• builtins:
– Bitwise inversion on boolean types, ~True or ~False has been deprecated since Python 3.12, as it
producessurprisingandunintuitiveresults(-2and-1). Usenot xinsteadforthelogicalnegationofa
Boolean. Intherarecasethatyouneedthebitwiseinversionoftheunderlyinginteger,converttoint
explicitly(~int(x)).
• functools:
– Calling the Python implementation of functools.reduce() with function or sequence as keyword
argumentshasbeendeprecatedsincePython3.14.
• logging:
SupportforcustomlogginghandlerswiththestrmargumentisdeprecatedandscheduledforremovalinPython
3.16. Definehandlerswiththestreamargumentinstead. (ContributedbyMariuszFelisiakingh-115032.)
• mimetypes:
– Valid extensions start with a ‘.’ or are empty for mimetypes.MimeTypes.add_type(). Undotted
extensions are deprecated and will raise a ValueError in Python 3.16. (Contributed by Hugo van
Kemenadeingh-75223.)
39

### 第40页

• shutil:
– TheExecErrorexceptionhasbeendeprecatedsincePython3.14. Ithasnotbeenusedbyanyfunction
inshutilsincePython3.4,andisnowanaliasofRuntimeError.
• symtable:
– TheClass.get_methodsmethodhasbeendeprecatedsincePython3.14.
• sys:
– The_enablelegacywindowsfsencoding()functionhasbeendeprecatedsincePython3.13. Use
thePYTHONLEGACYWINDOWSFSENCODINGenvironmentvariableinstead.
• sysconfig:
– Thesysconfig.expand_makefile_vars()functionhasbeendeprecatedsincePython3.14. Use
thevarsargumentofsysconfig.get_paths()instead.
• tarfile:
– TheundocumentedandunusedTarFile.tarfileattributehasbeendeprecatedsincePython3.13.
10.4 Pending removal in Python 3.17
• collections.abc:
– collections.abc.ByteStringisscheduledforremovalinPython3.17.
Useisinstance(obj, collections.abc.Buffer)totestifobjimplementsthebufferprotocol
atruntime. Foruseintypeannotations,eitheruseBufferoraunionthatexplicitlyspecifiesthetypes
yourcodesupports(e.g.,bytes | bytearray | memoryview).
ByteString was originally intended to be an abstract class that would serve as a supertype of both
bytesandbytearray. However,sincetheABCneverhadanymethods,knowingthatanobjectwas
an instance of ByteString never actually told you anything useful about the object. Other common
buffer types such as memoryview were also never understood as subtypes of ByteString (either at
runtimeorbystatictypecheckers).
SeePEP688formoredetails. (ContributedbyShantanuJainingh-91896.)
• typing:
– Before Python 3.14, old-style unions were implemented using the private class typing.
_UnionGenericAlias. Thisclassisnolongerneededfortheimplementation,butithasbeenretained
for backward compatibility, with removal scheduled for Python 3.17. Users should use documented
introspection helpers like typing.get_origin() and typing.get_args() instead of relying on
privateimplementationdetails.
– typing.ByteString,deprecatedsincePython3.9,isscheduledforremovalinPython3.17.
Useisinstance(obj, collections.abc.Buffer)totestifobjimplementsthebufferprotocol
atruntime. Foruseintypeannotations,eitheruseBufferoraunionthatexplicitlyspecifiesthetypes
yourcodesupports(e.g.,bytes | bytearray | memoryview).
ByteString was originally intended to be an abstract class that would serve as a supertype of both
bytesandbytearray. However,sincetheABCneverhadanymethods,knowingthatanobjectwas
an instance of ByteString never actually told you anything useful about the object. Other common
buffer types such as memoryview were also never understood as subtypes of ByteString (either at
runtimeorbystatictypecheckers).
SeePEP688formoredetails. (ContributedbyShantanuJainingh-91896.)
40

### 第41页

10.5 Pending removal in Python 3.19
• ctypes:
– Implicitly switching to the MSVC-compatible struct layout by setting _pack_ but not _layout_ on
non-Windowsplatforms.
10.6 Pending removal in future versions
ThefollowingAPIswillberemovedinthefuture,althoughthereiscurrentlynodatescheduledfortheirremoval.
• argparse:
– Nestingargumentgroupsandnestingmutuallyexclusivegroupsaredeprecated.
– Passingtheundocumentedkeywordargumentprefix_charstoadd_argument_group()isnowdepre-
cated.
– Theargparse.FileTypetypeconverterisdeprecated.
• builtins:
– bool(NotImplemented).
– Generators: throw(type, exc, tb) and athrow(type, exc, tb) signature is deprecated: use
throw(exc)andathrow(exc)instead,thesingleargumentsignature.
– CurrentlyPythonacceptsnumericliteralsimmediatelyfollowedbykeywords,forexample0in x,1or
x,0if 1else 2. Itallowsconfusingandambiguousexpressionslike[0x1for x in y](whichcan
be interpreted as [0x1 for x in y] or [0x1f or x in y]). A syntax warning is raised if the
numericliteralisimmediatelyfollowedbyoneofkeywordsand,else,for,if,in,isandor. Ina
futurereleaseitwillbechangedtoasyntaxerror. (gh-87999)
– Supportfor__index__()and__int__()methodreturningnon-inttype: thesemethodswillbere-
quiredtoreturnaninstanceofastrictsubclassofint.
– Supportfor__float__()methodreturningastrictsubclassoffloat: thesemethodswillberequired
toreturnaninstanceoffloat.
– Support for __complex__() method returning a strict subclass of complex: these methods will be
requiredtoreturnaninstanceofcomplex.
– Delegationofint()to__trunc__()method.
– Passingacomplexnumberastherealorimagargumentinthecomplex()constructorisnowdeprecated;
itshouldonlybepassedasasinglepositionalargument. (ContributedbySerhiyStorchakaingh-109218.)
• calendar: calendar.January and calendar.February constants are deprecated and replaced by
calendar.JANUARYandcalendar.FEBRUARY.(ContributedbyPrinceRoshaningh-103636.)
• codecs: useopen()insteadofcodecs.open(). (gh-133038)
• codeobject.co_lnotab: usethecodeobject.co_lines()methodinstead.
• datetime:
– utcnow(): usedatetime.datetime.now(tz=datetime.UTC).
– utcfromtimestamp(): use datetime.datetime.fromtimestamp(timestamp,
tz=datetime.UTC).
• gettext: Pluralvaluemustbeaninteger.
• importlib:
– cache_from_source() debug_override parameter is deprecated: use the optimization parameter in-
stead.
• importlib.metadata:
– EntryPointstupleinterface.
41

### 第42页

– ImplicitNoneonreturnvalues.
• logging: thewarn()methodhasbeendeprecatedsincePython3.3,usewarning()instead.
• mailbox: UseofStringIOinputandtextmodeisdeprecated,useBytesIOandbinarymodeinstead.
• os: Callingos.register_at_fork()inmulti-threadedprocess.
• pydoc.ErrorDuringImport: Atuplevalueforexc_infoparameterisdeprecated,useanexceptioninstance.
• re: Morestrictrulesarenowappliedfornumericalgroupreferencesandgroupnamesinregularexpressions.
OnlysequenceofASCIIdigitsisnowacceptedasanumericalreference. Thegroupnameinbytespatterns
andreplacementstringscannowonlycontainASCIIlettersanddigitsandunderscore. (ContributedbySerhiy
Storchakaingh-91760.)
• sre_compile,sre_constantsandsre_parsemodules.
• shutil: rmtree()’sonerrorparameterisdeprecatedinPython3.12;usetheonexcparameterinstead.
• ssloptionsandprotocols:
– ssl.SSLContextwithoutprotocolargumentisdeprecated.
– ssl.SSLContext: set_npn_protocols()andselected_npn_protocol()aredeprecated: use
ALPNinstead.
– ssl.OP_NO_SSL*options
– ssl.OP_NO_TLS*options
– ssl.PROTOCOL_SSLv3
– ssl.PROTOCOL_TLS
– ssl.PROTOCOL_TLSv1
– ssl.PROTOCOL_TLSv1_1
– ssl.PROTOCOL_TLSv1_2
– ssl.TLSVersion.SSLv3
– ssl.TLSVersion.TLSv1
– ssl.TLSVersion.TLSv1_1
• threadingmethods:
– threading.Condition.notifyAll(): usenotify_all().
– threading.Event.isSet(): useis_set().
– threading.Thread.isDaemon(), threading.Thread.setDaemon(): use threading.
Thread.daemonattribute.
– threading.Thread.getName(), threading.Thread.setName(): use threading.Thread.
nameattribute.
– threading.currentThread(): usethreading.current_thread().
– threading.activeCount(): usethreading.active_count().
• typing.Text(gh-92332).
• The internal class typing._UnionGenericAlias is no longer used to implement typing.Union. To
preservecompatibilitywithusersusingthisprivateclass,acompatibilityshimwillbeprovideduntilatleast
Python3.17. (ContributedbyJelleZijlstraingh-105499.)
• unittest.IsolatedAsyncioTestCase: it is deprecated to return a value that is not None from a test
case.
• urllib.parsedeprecatedfunctions: urlparse()instead
– splitattr()
42

### 第43页

– splithost()
– splitnport()
– splitpasswd()
– splitport()
– splitquery()
– splittag()
– splittype()
– splituser()
– splitvalue()
– to_bytes()
• wsgiref: SimpleHandler.stdout.write()shouldnotdopartialwrites.
• xml.etree.ElementTree: TestingthetruthvalueofanElementisdeprecated. Inafuturereleaseitwill
alwaysreturnTrue. Preferexplicitlen(elem)orelem is not Nonetestsinstead.
• sys._clear_type_cache()isdeprecated: usesys._clear_internal_caches()instead.
11 CPython bytecode changes
• ReplacedtheopcodeBINARY_SUBSCRbytheBINARY_OPopcodewiththeNB_SUBSCRoparg. (Contributed
byIritKatrielingh-100239.)
• Add the BUILD_INTERPOLATION and BUILD_TEMPLATE opcodes to construct new Interpolation and
Template instances, respectively. (Contributed by Lysandros Nikolaou and others in gh-132661; see also
PEP750: Templatestrings).
• RemovetheBUILD_CONST_KEY_MAPopcode. UseBUILD_MAPinstead. (ContributedbyMarkShannonin
gh-122160.)
• ReplacetheLOAD_ASSERTION_ERRORopcodewithLOAD_COMMON_CONSTANTandaddsupportforloading
NotImplementedError.
• AddtheLOAD_FAST_BORROWandLOAD_FAST_BORROW_LOAD_FAST_BORROWopcodestoreducereference
countingoverheadwhentheinterpretercanprovethatthereferenceintheframeoutlivesthereferenceloaded
ontothestack. (ContributedbyMattPageingh-130704.)
• Add the LOAD_SMALL_INT opcode, which pushes a small integer equal to the oparg to the stack. The
RETURN_CONSTopcodeisremovedasitisnolongerused. (ContributedbyMarkShannoningh-125837.)
• Add the new LOAD_SPECIAL instruction. Generate code for with and async with statements using the
newinstruction. RemovedtheBEFORE_WITHandBEFORE_ASYNC_WITHinstructions. (ContributedbyMark
Shannoningh-120507.)
• AddthePOP_ITERopcodetosupport‘virtual’iterators. (ContributedbyMarkShannoningh-132554.)
11.1 Pseudo-instructions
• AddtheANNOTATIONS_PLACEHOLDERpseudoinstructiontosupportpartiallyexecutedmodule-levelanno-
tationswithdeferredevaluationofannotations. (ContributedbyJelleZijlstraingh-130907.)
• AddtheBINARY_OP_EXTENDpseudoinstruction,whichexecutesapairoffunctions(guardandspecialization
functions)accessedfromtheinlinecache. (ContributedbyIritKatrielingh-100239.)
• Add three specializations for CALL_KW; CALL_KW_PY for calls to Python functions,
CALL_KW_BOUND_METHOD for calls to bound methods, and CALL_KW_NON_PY for all other calls. (Con-
tributedbyMarkShannoningh-118093.)
43

### 第44页

• AddtheJUMP_IF_TRUEandJUMP_IF_FALSEpseudoinstructions,conditionaljumpswhichdonotimpact
thestack. ReplacedbythesequenceCOPY 1,TO_BOOL,POP_JUMP_IF_TRUE/FALSE.(ContributedbyIrit
Katrielingh-124285.)
• AddtheLOAD_CONST_MORTALpseudoinstruction. (ContributedbyMarkShannoningh-128685.)
• Add the LOAD_CONST_IMMORTAL pseudo instruction, which does the same as LOAD_CONST, but is more
efficientforimmortalobjects. (ContributedbyMarkShannoningh-125837.)
• Add the NOT_TAKEN pseudo instruction, used by sys.monitoring to record branch events (such as
BRANCH_LEFT).(ContributedbyMarkShannoningh-122548.)
12 C API changes
12.1 New features in the C API
• AddPy_PACK_VERSION()andPy_PACK_FULL_VERSION(),twonewmacrosforbit-packingPythonver-
sionnumbers. ThisisusefulforcomparisonswithPy_VersionorPY_VERSION_HEX.(ContributedbyPetr
Viktoriningh-128629.)
• Add PyBytes_Join(sep, iterable) function, similar to sep.join(iterable) in Python. (Con-
tributedbyVictorStinneringh-121645.)
• Add functions to manipulate the configuration of the current runtime Python interpreter (PEP 741: Python
configurationCAPI):
– PyConfig_Get()
– PyConfig_GetInt()
– PyConfig_Set()
– PyConfig_Names()
(ContributedbyVictorStinneringh-107954.)
• AddfunctionstoconfigurePythoninitialization(PEP741: PythonconfigurationCAPI):
– Py_InitializeFromInitConfig()
– PyInitConfig_AddModule()
– PyInitConfig_Create()
– PyInitConfig_Free()
– PyInitConfig_FreeStrList()
– PyInitConfig_GetError()
– PyInitConfig_GetExitCode()
– PyInitConfig_GetInt()
– PyInitConfig_GetStr()
– PyInitConfig_GetStrList()
– PyInitConfig_HasOption()
– PyInitConfig_SetInt()
– PyInitConfig_SetStr()
– PyInitConfig_SetStrList()
(ContributedbyVictorStinneringh-107954.)
• AddPy_fopen()functiontoopenafile. ThisworkssimilarlytothestandardCfopen()function,instead
acceptingaPythonobjectforthepathparameterandsettinganexceptiononerror. Thecorrespondingnew
Py_fclose()functionshouldbeusedtocloseafile. (ContributedbyVictorStinneringh-127350.)
44

### 第45页

• AddPy_HashBuffer()tocomputeandreturnthehashvalueofabuffer. (ContributedbyAntoinePitrou
andVictorStinneringh-122854.)
• AddPyImport_ImportModuleAttr()andPyImport_ImportModuleAttrString()helperfunctions
toimportamoduleandgetanattributeofthemodule. (ContributedbyVictorStinneringh-128911.)
• AddPyIter_NextItem()toreplacePyIter_Next(),whichhasanambiguousreturnvalue. (Contributed
byIritKatrielandErlendAaslandingh-105201.)
• Add PyLong_GetSign() function to get the sign of int objects. (Contributed by Sergey B Kirpichev in
gh-116560.)
• Add PyLong_IsPositive(), PyLong_IsNegative() and PyLong_IsZero() for checking if
PyLongObject is positive, negative, or zero, respectively. (Contributed by James Roy and Sergey B Kir-
pichevingh-126061.)
• AddnewfunctionstoconvertC<stdint.h>numbersto/fromPythonintobjects:
– PyLong_AsInt32()
– PyLong_AsInt64()
– PyLong_AsUInt32()
– PyLong_AsUInt64()
– PyLong_FromInt32()
– PyLong_FromInt64()
– PyLong_FromUInt32()
– PyLong_FromUInt64()
(ContributedbyVictorStinneringh-120389.)
• AddanewimportandexportAPIforPythonintobjects(PEP757):
– PyLong_GetNativeLayout()
– PyLong_Export()
– PyLong_FreeExport()
– PyLongWriter_Create()
– PyLongWriter_Finish()
– PyLongWriter_Discard()
(ContributedbySergeyBKirpichevandVictorStinneringh-102471.)
• Add PyMonitoring_FireBranchLeftEvent() and PyMonitoring_FireBranchRightEvent() for
generating BRANCH_LEFT and BRANCH_RIGHT events, respectively. (Contributed by Mark Shannon in gh-
122548.)
• AddPyType_Freeze()functiontomakeatypeimmutable. (ContributedbyVictorStinneringh-121654.)
• Add PyType_GetBaseByToken() and Py_tp_token slot for easier superclass identification, which at-
temptstoresolvethetypecheckingissuementionedinPEP630. (Contributedingh-124153.)
• AddanewPyUnicode_Equal()functiontotestiftwostringsareequal. Thefunctionisalsoaddedtothe
LimitedCAPI.(ContributedbyVictorStinneringh-124502.)
• AddanewPyUnicodeWriterAPItocreateaPythonstrobject,withthefollowingfunctions:
– PyUnicodeWriter_Create()
– PyUnicodeWriter_DecodeUTF8Stateful()
– PyUnicodeWriter_Discard()
– PyUnicodeWriter_Finish()
45

### 第46页

– PyUnicodeWriter_Format()
– PyUnicodeWriter_WriteASCII()
– PyUnicodeWriter_WriteChar()
– PyUnicodeWriter_WriteRepr()
– PyUnicodeWriter_WriteStr()
– PyUnicodeWriter_WriteSubstring()
– PyUnicodeWriter_WriteUCS4()
– PyUnicodeWriter_WriteUTF8()
– PyUnicodeWriter_WriteWideChar()
(ContributedbyVictorStinneringh-119182.)
• The k and K formats in PyArg_ParseTuple() and similar functions now use __index__() if available,
likeallotherintegerformats. (ContributedbySerhiyStorchakaingh-112068.)
• Add support for a new p format unit in Py_BuildValue() that produces a Python bool object from a C
integer. (ContributedbyPabloGalindoinbpo-45325.)
• AddPyUnstable_IsImmortal()fordeterminingifanobjectisimmortal,fordebuggingpurposes. (Con-
tributedbyPeterBiermaingh-128509.)
• Add PyUnstable_Object_EnableDeferredRefcount() for enabling deferred reference counting, as
outlinedinPEP703.
• AddPyUnstable_Object_IsUniquelyReferenced()asareplacementforPy_REFCNT(op) == 1on
freethreadedbuilds. (ContributedbyPeterBiermaingh-133140.)
• Add PyUnstable_Object_IsUniqueReferencedTemporary() to determine if an object is a unique
temporary object on the interpreter’s operand stack. This can be used in some cases as a replacement for
checkingifPy_REFCNT()is1forPythonobjectspassedasargumentstoCAPIfunctions. (Contributedby
SamGrossingh-133164.)
12.2 Limited C API changes
• In the limited C API version 3.14 and newer, Py_TYPE() and Py_REFCNT() are now implemented as an
opaque function call to hide implementation details. (Contributed by Victor Stinner in gh-120600 and gh-
124127.)
• Remove the PySequence_Fast_GET_SIZE, PySequence_Fast_GET_ITEM, and
PySequence_Fast_ITEMS macros from the limited C API, since they have always been broken in
thelimitedCAPI.(ContributedbyVictorStinneringh-91417.)
12.3 Removed C APIs
• Creating immutable types with mutable bases was deprecated in Python 3.12, and now raises a
TypeError. (ContributedbyNikitaSobolevingh-119775.)
• Remove PyDictObject.ma_version_tag member, which was deprecated in Python 3.12. Use the
PyDict_AddWatcher()APIinstead. (ContributedbySamGrossingh-124296.)
• Remove the private _Py_InitializeMain() function. It was a provisional API added to Python 3.8 by
PEP587. (ContributedbyVictorStinneringh-129033.)
• Remove the undocumented APIs Py_C_RECURSION_LIMIT and PyThreadState.
c_recursion_remaining. These were added in 3.13 and have been removed without deprecation.
Use Py_EnterRecursiveCall() to guard against runaway recursion in C code. (Removed by Petr
Viktoriningh-133079,seealsogh-130396.)
46

### 第47页

12.4 Deprecated C APIs
• The Py_HUGE_VAL macro is now soft deprecated. Use Py_INFINITY instead. (Contributed by Sergey B
Kirpichevingh-120026.)
• The Py_IS_NAN, Py_IS_INFINITY, and Py_IS_FINITE macros are now soft deprecated. Use isnan,
isinf and isfinite instead, available from math.h since C99. (Contributed by Sergey B Kirpichev in
gh-119613.)
• Non-tuplesequencesarenowdeprecatedasargumentforthe(items)formatunitinPyArg_ParseTuple()
andotherargumentparsingfunctionsifitemscontainsformatunitswhichstoreaborrowedbufferoraborrowed
reference. (ContributedbySerhiyStorchakaingh-50333.)
• The_PyMonitoring_FireBranchEventfunctionisnowdeprecatedandshouldbereplacedwithcallsto
PyMonitoring_FireBranchLeftEvent()andPyMonitoring_FireBranchRightEvent().
• The previously undocumented function PySequence_In() is now soft deprecated. Use
PySequence_Contains()instead. (ContributedbyYukiKobayashiingh-127896.)
PendingremovalinPython3.15
• ThePyImport_ImportModuleNoBlock(): UsePyImport_ImportModule()instead.
• PyWeakref_GetObject()andPyWeakref_GET_OBJECT(): UsePyWeakref_GetRef()instead. The
pythoncapi-compatprojectcanbeusedtogetPyWeakref_GetRef()onPython3.12andolder.
• Py_UNICODEtypeandthePy_UNICODE_WIDEmacro: Usewchar_tinstead.
• PyUnicode_AsDecodedObject(): UsePyCodec_Decode()instead.
• PyUnicode_AsDecodedUnicode(): UsePyCodec_Decode()instead;Notethatsomecodecs(forexam-
ple,“base64”)mayreturnatypeotherthanstr,suchasbytes.
• PyUnicode_AsEncodedObject(): UsePyCodec_Encode()instead.
• PyUnicode_AsEncodedUnicode(): UsePyCodec_Encode()instead;Notethatsomecodecs(forexam-
ple,“base64”)mayreturnatypeotherthanbytes,suchasstr.
• Pythoninitializationfunctions,deprecatedinPython3.13:
– Py_GetPath(): UsePyConfig_Get("module_search_paths")(sys.path)instead.
– Py_GetPrefix(): Use PyConfig_Get("base_prefix") (sys.base_prefix) instead. Use
PyConfig_Get("prefix")(sys.prefix)ifvirtualenvironmentsneedtobehandled.
– Py_GetExecPrefix(): Use PyConfig_Get("base_exec_prefix") (sys.
base_exec_prefix) instead. Use PyConfig_Get("exec_prefix") (sys.exec_prefix)
ifvirtualenvironmentsneedtobehandled.
– Py_GetProgramFullPath(): UsePyConfig_Get("executable")(sys.executable)instead.
– Py_GetProgramName(): UsePyConfig_Get("executable")(sys.executable)instead.
– Py_GetPythonHome(): Use PyConfig_Get("home") or the PYTHONHOME environment variable
instead.
Thepythoncapi-compatprojectcanbeusedtogetPyConfig_Get()onPython3.13andolder.
• FunctionstoconfigurePython’sinitialization,deprecatedinPython3.11:
– PySys_SetArgvEx(): SetPyConfig.argvinstead.
– PySys_SetArgv(): SetPyConfig.argvinstead.
– Py_SetProgramName(): SetPyConfig.program_nameinstead.
– Py_SetPythonHome(): SetPyConfig.homeinstead.
– PySys_ResetWarnOptions(): Clearsys.warnoptionsandwarnings.filtersinstead.
ThePy_InitializeFromConfig()APIshouldbeusedwithPyConfiginstead.
47

### 第48页

• Globalconfigurationvariables:
– Py_DebugFlag: UsePyConfig.parser_debugorPyConfig_Get("parser_debug")instead.
– Py_VerboseFlag: UsePyConfig.verboseorPyConfig_Get("verbose")instead.
– Py_QuietFlag: UsePyConfig.quietorPyConfig_Get("quiet")instead.
– Py_InteractiveFlag: Use PyConfig.interactive or PyConfig_Get("interactive") in-
stead.
– Py_InspectFlag: UsePyConfig.inspectorPyConfig_Get("inspect")instead.
– Py_OptimizeFlag: Use PyConfig.optimization_level or
PyConfig_Get("optimization_level")instead.
– Py_NoSiteFlag: UsePyConfig.site_importorPyConfig_Get("site_import")instead.
– Py_BytesWarningFlag: Use PyConfig.bytes_warning or
PyConfig_Get("bytes_warning")instead.
– Py_FrozenFlag: Use PyConfig.pathconfig_warnings or
PyConfig_Get("pathconfig_warnings")instead.
– Py_IgnoreEnvironmentFlag: Use PyConfig.use_environment or
PyConfig_Get("use_environment")instead.
– Py_DontWriteBytecodeFlag: Use PyConfig.write_bytecode or
PyConfig_Get("write_bytecode")instead.
– Py_NoUserSiteDirectory: Use PyConfig.user_site_directory or
PyConfig_Get("user_site_directory")instead.
– Py_UnbufferedStdioFlag: Use PyConfig.buffered_stdio or
PyConfig_Get("buffered_stdio")instead.
– Py_HashRandomizationFlag: Use PyConfig.use_hash_seed and PyConfig.hash_seed or
PyConfig_Get("hash_seed")instead.
– Py_IsolatedFlag: UsePyConfig.isolatedorPyConfig_Get("isolated")instead.
– Py_LegacyWindowsFSEncodingFlag: Use PyPreConfig.legacy_windows_fs_encoding or
PyConfig_Get("legacy_windows_fs_encoding")instead.
– Py_LegacyWindowsStdioFlag: Use PyConfig.legacy_windows_stdio or
PyConfig_Get("legacy_windows_stdio")instead.
– Py_FileSystemDefaultEncoding, Py_HasFileSystemDefaultEncoding: Use PyConfig.
filesystem_encodingorPyConfig_Get("filesystem_encoding")instead.
– Py_FileSystemDefaultEncodeErrors: Use PyConfig.filesystem_errors or
PyConfig_Get("filesystem_errors")instead.
– Py_UTF8Mode: Use PyPreConfig.utf8_mode or PyConfig_Get("utf8_mode") instead. (see
Py_PreInitialize())
The Py_InitializeFromConfig() API should be used with PyConfig to set these options. Or
PyConfig_Get()canbeusedtogettheseoptionsatruntime.
PendingremovalinPython3.16
• Thebundledcopyoflibmpdec.
PendingremovalinPython3.18
• ThefollowingprivatefunctionsaredeprecatedandplannedforremovalinPython3.18:
– _PyBytes_Join(): usePyBytes_Join().
– _PyDict_GetItemStringWithError(): usePyDict_GetItemStringRef().
48

### 第49页

– _PyDict_Pop(): usePyDict_Pop().
– _PyLong_Sign(): usePyLong_GetSign().
– _PyLong_FromDigits()and_PyLong_New(): usePyLongWriter_Create().
– _PyThreadState_UncheckedGet(): usePyThreadState_GetUnchecked().
– _PyUnicode_AsString(): usePyUnicode_AsUTF8().
– _PyUnicodeWriter_Init(): replace _PyUnicodeWriter_Init(&writer) with writer =
PyUnicodeWriter_Create(0).
– _PyUnicodeWriter_Finish(): replace _PyUnicodeWriter_Finish(&writer) with
PyUnicodeWriter_Finish(writer).
– _PyUnicodeWriter_Dealloc(): replace _PyUnicodeWriter_Dealloc(&writer) with
PyUnicodeWriter_Discard(writer).
– _PyUnicodeWriter_WriteChar(): replace _PyUnicodeWriter_WriteChar(&writer, ch)
withPyUnicodeWriter_WriteChar(writer, ch).
– _PyUnicodeWriter_WriteStr(): replace _PyUnicodeWriter_WriteStr(&writer, str)
withPyUnicodeWriter_WriteStr(writer, str).
– _PyUnicodeWriter_WriteSubstring():replace_PyUnicodeWriter_WriteSubstring(&writer,
str, start, end) with PyUnicodeWriter_WriteSubstring(writer, str, start,
end).
– _PyUnicodeWriter_WriteASCIIString():replace_PyUnicodeWriter_WriteASCIIString(&wri
str)withPyUnicodeWriter_WriteASCII(writer, str).
– _PyUnicodeWriter_WriteLatin1String():replace_PyUnicodeWriter_WriteLatin1String(&w
str)withPyUnicodeWriter_WriteUTF8(writer, str).
– _PyUnicodeWriter_Prepare(): (noreplacement).
– _PyUnicodeWriter_PrepareKind(): (noreplacement).
– _Py_HashPointer(): usePy_HashPointer().
– _Py_fopen_obj(): usePy_fopen().
Thepythoncapi-compatprojectcanbeusedtogetthesenewpublicfunctionsonPython3.13andolder. (Con-
tributedbyVictorStinneringh-128863.)
Pendingremovalinfutureversions
The following APIs are deprecated and will be removed, although there is currently no date scheduled for their
removal.
• Py_TPFLAGS_HAVE_FINALIZE:UnneededsincePython3.8.
• PyErr_Fetch(): UsePyErr_GetRaisedException()instead.
• PyErr_NormalizeException(): UsePyErr_GetRaisedException()instead.
• PyErr_Restore(): UsePyErr_SetRaisedException()instead.
• PyModule_GetFilename(): UsePyModule_GetFilenameObject()instead.
• PyOS_AfterFork(): UsePyOS_AfterFork_Child()instead.
• PySlice_GetIndicesEx(): UsePySlice_Unpack()andPySlice_AdjustIndices()instead.
• PyUnicode_READY(): UnneededsincePython3.12
• PyErr_Display(): UsePyErr_DisplayException()instead.
• _PyErr_ChainExceptions(): Use_PyErr_ChainExceptions1()instead.
• PyBytesObject.ob_shashmember: callPyObject_Hash()instead.
49

### 第50页

• ThreadLocalStorage(TLS)API:
– PyThread_create_key(): UsePyThread_tss_alloc()instead.
– PyThread_delete_key(): UsePyThread_tss_free()instead.
– PyThread_set_key_value(): UsePyThread_tss_set()instead.
– PyThread_get_key_value(): UsePyThread_tss_get()instead.
– PyThread_delete_key_value(): UsePyThread_tss_delete()instead.
– PyThread_ReInitTLS(): UnneededsincePython3.7.
13 Build Changes
• GNUAutoconf2.72isnowrequiredtogenerateconfigure. (ContributedbyErlendAaslandingh-115765.)
• wasm32-unknown-emscripten is now a PEP 11 tier 3 platform. (Contributed by R. Hood Chatham in
gh-127146,gh-127683,andgh-136931.)
• #pragma-basedlinkingwithpython3*.libcannowbeswitchedoffwithPy_NO_LINK_LIB.(Contributed
byJean-ChristopheFillion-Robiningh-82909.)
• CPython now enables a set of recommended compiler options by default for improved security. Use the
--disable-safetyconfigureoptiontodisablethem,orthe--enable-slower-safetyoptionfora
largersetofcompileroptions,albeitwithaperformancecost.
• TheWITH_FREELISTSmacroand--without-freelistsconfigureoptionhavebeenremoved.
• Thenewconfigureoption--with-tail-call-interpmaybeusedtoenabletheexperimentaltailcall
interpreter. SeeAnewtypeofinterpreterforfurtherdetails.
• Todisablethenewremotedebuggingsupport,usethe--without-remote-debugconfigureoption. This
maybeusefulforsecurityreasons.
13.1 build-details.json
InstallationsofPythonnowcontainanewfile,build-details.json. ThisisastaticJSONdocumentcontaining
builddetailsforCPython,toallowforintrospectionwithoutneedingtoruncode. Thisishelpfulforuse-casessuch
asPythonlaunchers,cross-compilation,andsoon.
build-details.jsonmustbeinstalledintheplatform-independentstandardlibrarydirectory. Thiscorresponds
tothe‘stdlib’sysconfiginstallationpath,whichcanbefoundbyrunningsysconfig.get_path('stdlib').
(cid:181) Seealso
PEP739–build-details.json1.0–astaticdescriptionfileforPythonbuilddetails
13.2 Discontinuation of PGP signatures
PGP(PrettyGoodPrivacy)signatureswillnotbeprovidedforreleasesofPython3.14orfutureversions. Toverify
CPython artifacts, users must use Sigstore verification materials. Releases have been signed using Sigstore since
Python3.11.
ThischangeinreleaseprocesswasspecifiedinPEP761.
14 Porting to Python 3.14
Thissectionlistspreviouslydescribedchangesandotherbugfixesthatmayrequirechangestoyourcode.
50

| (cid:181) Seealso |
| --- |
| PEP739–build-details.json1.0–astaticdescriptionfileforPythonbuilddetails |

### 第51页

14.1 Changes in the Python API
• functools.partialisnowamethoddescriptor. Wrapitinstaticmethod()ifyouwanttopreservethe
oldbehavior. (ContributedbySerhiyStorchakaandDominykasGrigonisingh-121027.)
• Thegarbagecollectorisnowincremental,whichmeansthatthebehaviorofgc.collect()changesslightly:
– gc.collect(1): Performsanincrementofgarbagecollection,ratherthancollectinggeneration1.
– Othercallstogc.collect()areunchanged.
• Thelocale.nl_langinfo()functionnowtemporarilysetstheLC_CTYPElocaleinsomecases. Thistem-
porarychangeaffectsotherthreads. (ContributedbySerhiyStorchakaingh-69998.)
• types.UnionTypeisnowanaliasfortyping.Union,causingchangesinsomebehaviors. Seeabovefor
moredetails. (ContributedbyJelleZijlstraingh-105499.)
• Theruntimebehaviorofannotationshaschangedinvariousways;seeabovefordetails. Whilemostcodethat
interactswithannotationsshouldcontinuetowork,someundocumenteddetailsmaybehavedifferently.
14.2 Changes in the C API
• Py_Finalize()nowdeletesallinternedstrings. ThisisbackwardsincompatibletoanyCextensionthatholds
ontoaninternedstringafteracalltoPy_Finalize()andisthenreusedafteracalltoPy_Initialize().
Any issues arising from this behavior will normally result in crashes during the execution of the subsequent
calltoPy_Initialize()fromaccessinguninitializedmemory. Tofix,useanaddresssanitizertoidentify
anyuse-after-freecomingfromaninternedstringanddeallocateitduringmoduleshutdown. (Contributedby
EddieElizondoingh-113601.)
• The Unicode Exception Objects C API now raises a TypeError if its exception argument is not a
UnicodeErrorobject. (ContributedbyBénédiktTraningh-127691.)
• The interpreter internally avoids some reference count modifications when loading objects onto the
operands stack by borrowing references when possible. This can lead to smaller reference count
values compared to previous Python versions. C API extensions that checked Py_REFCNT() of
1 to determine if an function argument is not referenced by any other code should instead use
PyUnstable_Object_IsUniqueReferencedTemporary()asasaferreplacement.
• PrivatefunctionspromotedtopublicCAPIs:
– _PyBytes_Join(): PyBytes_Join()
– _PyLong_IsNegative(): PyLong_IsNegative()
– _PyLong_IsPositive(): PyLong_IsPositive()
– _PyLong_IsZero(): PyLong_IsZero()
– _PyLong_Sign(): PyLong_GetSign()
– _PyUnicodeWriter_Dealloc(): PyUnicodeWriter_Discard()
– _PyUnicodeWriter_Finish(): PyUnicodeWriter_Finish()
– _PyUnicodeWriter_Init(): usePyUnicodeWriter_Create()
– _PyUnicodeWriter_Prepare(): (noreplacement)
– _PyUnicodeWriter_PrepareKind(): (noreplacement)
– _PyUnicodeWriter_WriteChar(): PyUnicodeWriter_WriteChar()
– _PyUnicodeWriter_WriteStr(): PyUnicodeWriter_WriteStr()
– _PyUnicodeWriter_WriteSubstring(): PyUnicodeWriter_WriteSubstring()
– _PyUnicode_EQ(): PyUnicode_Equal()
– _PyUnicode_Equal(): PyUnicode_Equal()
– _Py_GetConfig(): PyConfig_Get()andPyConfig_GetInt()
51

### 第52页

– _Py_HashBytes(): Py_HashBuffer()
– _Py_fopen_obj(): Py_fopen()
– PyMutex_IsLocked(): PyMutex_IsLocked()
Thepythoncapi-compatprojectcanbeusedtogetmostofthesenewfunctionsonPython3.13andolder.
52

### 第53页

Index
B
PYTHONLEGACYWINDOWSFSENCODING,40
BROWSER,31
PYTHONSTARTUP,16
R
C
RFC
Common Vulnerabilities and Exposures
RFC 1494,24
CVE 2024-12718,28
RFC 2104,18,23
CVE 2025-4138,28
RFC 2177,23
CVE 2025-4330,28
RFC 2361,25
CVE 2025-4435,28
RFC 3362,24
CVE 2025-4517,26
RFC 3745,24
E RFC 3950,24
RFC 4047,24
environment variable
RFC 4337,25
BROWSER,31
RFC 5334,25
PYTHON_BASIC_REPL,16
RFC 6713,25
PYTHON_DISABLE_REMOTE_DEBUG,7
RFC 7616,30
PYTHON_JIT,17
RFC 7903,24
PYTHONHOME,47
RFC 8081,24
PYTHONLEGACYWINDOWSFSENCODING,40
RFC 9512,25
PYTHONSTARTUP,16
RFC 9559,24
P RFC 9562,30
RFC 9639,25
Python Enhancement Proposals
PEP 11,50
PEP 11#tier-3,17
PEP 563,10
PEP 587,13,46
PEP 626,38
PEP 630#type-checking,45
PEP 649,4,9,10,29
PEP 659,16
PEP 667,37
PEP 684,5
PEP 688#current-options,40
PEP 703,16,46
PEP 734,6,20
PEP 739,50
PEP 741,13
PEP 744,17
PEP 745,3
PEP 749,4,9,10,19
PEP 750,4,7
PEP 757,45
PEP 758,9
PEP 761,50
PEP 765,19
PEP 768,79
PEP 776,17
PEP 779,5
PEP 784,4,8
PYTHON_BASIC_REPL,16
PYTHON_DISABLE_REMOTE_DEBUG,7
PYTHON_JIT,17
PYTHONHOME,47
53

