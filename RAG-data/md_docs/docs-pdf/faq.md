### 第1页

Python Frequently Asked Questions
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 GeneralPythonFAQ 1
1.1 GeneralInformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.1 WhatisPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.2 WhatisthePythonSoftwareFoundation? . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.3 AretherecopyrightrestrictionsontheuseofPython? . . . . . . . . . . . . . . . . . . . 1
1.1.4 WhywasPythoncreatedinthefirstplace? . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.5 WhatisPythongoodfor? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.1.6 HowdoesthePythonversionnumberingschemework? . . . . . . . . . . . . . . . . . . 2
1.1.7 HowdoIobtainacopyofthePythonsource? . . . . . . . . . . . . . . . . . . . . . . . 3
1.1.8 HowdoIgetdocumentationonPython? . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.1.9 I’veneverprogrammedbefore. IsthereaPythontutorial? . . . . . . . . . . . . . . . . . 3
1.1.10 IsthereanewsgroupormailinglistdevotedtoPython?. . . . . . . . . . . . . . . . . . . 3
1.1.11 HowdoIgetabetatestversionofPython? . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.1.12 HowdoIsubmitbugreportsandpatchesforPython? . . . . . . . . . . . . . . . . . . . 3
1.1.13 ArethereanypublishedarticlesaboutPythonthatIcanreference? . . . . . . . . . . . . 3
1.1.14 ArethereanybooksonPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.1.15 Whereintheworldiswww.python.orglocated? . . . . . . . . . . . . . . . . . . . . . . 4
1.1.16 WhyisitcalledPython?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.1.17 DoIhavetolike“MontyPython’sFlyingCircus”? . . . . . . . . . . . . . . . . . . . . . 4
1.2 Pythonintherealworld . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2.1 HowstableisPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2.2 HowmanypeopleareusingPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2.3 HaveanysignificantprojectsbeendoneinPython? . . . . . . . . . . . . . . . . . . . . . 4
1.2.4 WhatnewdevelopmentsareexpectedforPythoninthefuture? . . . . . . . . . . . . . . 4
1.2.5 IsitreasonabletoproposeincompatiblechangestoPython? . . . . . . . . . . . . . . . . 5
1.2.6 IsPythonagoodlanguageforbeginningprogrammers? . . . . . . . . . . . . . . . . . . 5
2 ProgrammingFAQ 7
2.1 GeneralQuestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Isthereasourcecodeleveldebuggerwithbreakpoints,single-stepping,etc.? . . . . . . . 7
2.1.2 Aretheretoolstohelpfindbugsorperformstaticanalysis? . . . . . . . . . . . . . . . . 7
2.1.3 HowcanIcreateastand-alonebinaryfromaPythonscript? . . . . . . . . . . . . . . . . 7
2.1.4 AretherecodingstandardsorastyleguideforPythonprograms? . . . . . . . . . . . . . 8
2.2 CoreLanguage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.1 WhyamIgettinganUnboundLocalErrorwhenthevariablehasavalue? . . . . . . . . . 8
2.2.2 WhataretherulesforlocalandglobalvariablesinPython? . . . . . . . . . . . . . . . . 9
2.2.3 Whydolambdasdefinedinaloopwithdifferentvaluesallreturnthesameresult? . . . . . 9
2.2.4 HowdoIshareglobalvariablesacrossmodules? . . . . . . . . . . . . . . . . . . . . . . 10
2.2.5 Whatarethe“bestpractices”forusingimportinamodule? . . . . . . . . . . . . . . . . 10
2.2.6 Whyaredefaultvaluessharedbetweenobjects? . . . . . . . . . . . . . . . . . . . . . . 11
2.2.7 HowcanIpassoptionalorkeywordparametersfromonefunctiontoanother? . . . . . . 12
2.2.8 Whatisthedifferencebetweenargumentsandparameters? . . . . . . . . . . . . . . . . 12
2.2.9 Whydidchanginglist‘y’alsochangelist‘x’? . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2.10 HowdoIwriteafunctionwithoutputparameters(callbyreference)? . . . . . . . . . . . 13
i

### 第4页

2.2.11 HowdoyoumakeahigherorderfunctioninPython? . . . . . . . . . . . . . . . . . . . 14
2.2.12 HowdoIcopyanobjectinPython?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2.13 HowcanIfindthemethodsorattributesofanobject? . . . . . . . . . . . . . . . . . . . 15
2.2.14 Howcanmycodediscoverthenameofanobject? . . . . . . . . . . . . . . . . . . . . . 16
2.2.15 What’supwiththecommaoperator’sprecedence? . . . . . . . . . . . . . . . . . . . . . 16
2.2.16 IsthereanequivalentofC’s“?:” ternaryoperator? . . . . . . . . . . . . . . . . . . . . . 16
2.2.17 Isitpossibletowriteobfuscatedone-linersinPython? . . . . . . . . . . . . . . . . . . . 17
2.2.18 Whatdoestheslash(/)intheparameterlistofafunctionmean? . . . . . . . . . . . . . . 17
2.3 Numbersandstrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3.1 HowdoIspecifyhexadecimalandoctalintegers? . . . . . . . . . . . . . . . . . . . . . 18
2.3.2 Whydoes-22//10return-3? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3.3 HowdoIgetintliteralattributeinsteadofSyntaxError? . . . . . . . . . . . . . . . . . . 18
2.3.4 HowdoIconvertastringtoanumber? . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3.5 HowdoIconvertanumbertoastring? . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3.6 HowdoImodifyastringinplace? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.3.7 HowdoIusestringstocallfunctions/methods?. . . . . . . . . . . . . . . . . . . . . . . 19
2.3.8 IsthereanequivalenttoPerl’schomp()forremovingtrailingnewlinesfromstrings? . . . 20
2.3.9 Isthereascanf()orsscanf()equivalent? . . . . . . . . . . . . . . . . . . . . . . . 20
2.3.10 WhatdoesUnicodeDecodeErrororUnicodeEncodeErrorerrormean? . . . . . . . 21
2.3.11 CanIendarawstringwithanoddnumberofbackslashes? . . . . . . . . . . . . . . . . 21
2.4 Performance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.4.1 Myprogramistooslow. HowdoIspeeditup? . . . . . . . . . . . . . . . . . . . . . . . 21
2.4.2 Whatisthemostefficientwaytoconcatenatemanystringstogether?. . . . . . . . . . . . 22
2.5 Sequences(Tuples/Lists) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.5.1 HowdoIconvertbetweentuplesandlists? . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.5.2 What’sanegativeindex? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5.3 HowdoIiterateoverasequenceinreverseorder? . . . . . . . . . . . . . . . . . . . . . 23
2.5.4 Howdoyouremoveduplicatesfromalist? . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5.5 Howdoyouremovemultipleitemsfromalist . . . . . . . . . . . . . . . . . . . . . . . 23
2.5.6 HowdoyoumakeanarrayinPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.5.7 HowdoIcreateamultidimensionallist? . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.5.8 HowdoIapplyamethodorfunctiontoasequenceofobjects?. . . . . . . . . . . . . . . 24
2.5.9 Whydoesa_tuple[i]+=[‘item’]raiseanexceptionwhentheadditionworks? . . . . . . . 25
2.5.10 Iwanttodoacomplicatedsort: canyoudoaSchwartzianTransforminPython? . . . . . 26
2.5.11 HowcanIsortonelistbyvaluesfromanotherlist? . . . . . . . . . . . . . . . . . . . . . 26
2.6 Objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.6.1 Whatisaclass? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.6.2 Whatisamethod?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.6.3 Whatisself? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.6.4 HowdoIcheckifanobjectisaninstanceofagivenclassorofasubclassofit? . . . . . . 27
2.6.5 Whatisdelegation? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.6.6 HowdoIcallamethoddefinedinabaseclassfromaderivedclassthatextendsit? . . . . 29
2.6.7 HowcanIorganizemycodetomakeiteasiertochangethebaseclass? . . . . . . . . . . 29
2.6.8 HowdoIcreatestaticclassdataandstaticclassmethods? . . . . . . . . . . . . . . . . . 29
2.6.9 HowcanIoverloadconstructors(ormethods)inPython? . . . . . . . . . . . . . . . . . 30
2.6.10 Itrytouse__spamandIgetanerrorabout_SomeClassName__spam. . . . . . . . . . . 30
2.6.11 Myclassdefines__del__butitisnotcalledwhenIdeletetheobject. . . . . . . . . . . . 31
2.6.12 HowdoIgetalistofallinstancesofagivenclass? . . . . . . . . . . . . . . . . . . . . . 31
2.6.13 Whydoestheresultofid()appeartobenotunique? . . . . . . . . . . . . . . . . . . . 31
2.6.14 WhencanIrelyonidentitytestswiththeisoperator? . . . . . . . . . . . . . . . . . . . 32
2.6.15 Howcanasubclasscontrolwhatdataisstoredinanimmutableinstance? . . . . . . . . . 33
2.6.16 HowdoIcachemethodcalls? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
2.7 Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.7.1 HowdoIcreatea.pycfile? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.7.2 HowdoIfindthecurrentmodulename? . . . . . . . . . . . . . . . . . . . . . . . . . . 35
2.7.3 HowcanIhavemodulesthatmutuallyimporteachother? . . . . . . . . . . . . . . . . . 36
2.7.4 __import__(‘x.y.z’)returns<module‘x’>;howdoIgetz? . . . . . . . . . . . . . . . . . 36
ii

### 第5页

2.7.5 When I edit an importedmodule and reimport it, thechanges don’t show up. Whydoes
thishappen? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3 DesignandHistoryFAQ 39
3.1 WhydoesPythonuseindentationforgroupingofstatements? . . . . . . . . . . . . . . . . . . . . 39
3.2 WhyamIgettingstrangeresultswithsimplearithmeticoperations? . . . . . . . . . . . . . . . . . 39
3.3 Whyarefloating-pointcalculationssoinaccurate? . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.4 WhyarePythonstringsimmutable? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.5 Whymust‘self’beusedexplicitlyinmethoddefinitionsandcalls?. . . . . . . . . . . . . . . . . . 40
3.6 Whycan’tIuseanassignmentinanexpression? . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.7 WhydoesPythonusemethodsforsomefunctionality(e.g. list.index())butfunctionsforother(e.g.
len(list))? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.8 Whyisjoin()astringmethodinsteadofalistortuplemethod? . . . . . . . . . . . . . . . . . . . 41
3.9 Howfastareexceptions? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.10 Whyisn’tthereaswitchorcasestatementinPython? . . . . . . . . . . . . . . . . . . . . . . . . 42
3.11 Can’tyouemulatethreadsintheinterpreterinsteadofrelyingonanOS-specificthreadimplemen-
tation? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.12 Whycan’tlambdaexpressionscontainstatements? . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.13 CanPythonbecompiledtomachinecode,Corsomeotherlanguage? . . . . . . . . . . . . . . . 43
3.14 HowdoesPythonmanagememory? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.15 Whydoesn’tCPythonuseamoretraditionalgarbagecollectionscheme? . . . . . . . . . . . . . . 44
3.16 Whyisn’tallmemoryfreedwhenCPythonexits? . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.17 Whyarethereseparatetupleandlistdatatypes? . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.18 HowarelistsimplementedinCPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.19 HowaredictionariesimplementedinCPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
3.20 Whymustdictionarykeysbeimmutable? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.21 Whydoesn’tlist.sort()returnthesortedlist? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.22 HowdoyouspecifyandenforceaninterfacespecinPython? . . . . . . . . . . . . . . . . . . . . 46
3.23 Whyistherenogoto? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.24 Whycan’trawstrings(r-strings)endwithabackslash? . . . . . . . . . . . . . . . . . . . . . . . 47
3.25 Whydoesn’tPythonhavea“with”statementforattributeassignments? . . . . . . . . . . . . . . . 47
3.26 Whydon’tgeneratorssupportthewithstatement? . . . . . . . . . . . . . . . . . . . . . . . . . . 48
3.27 Whyarecolonsrequiredfortheif/while/def/classstatements?. . . . . . . . . . . . . . . . . . . . 48
3.28 WhydoesPythonallowcommasattheendoflistsandtuples? . . . . . . . . . . . . . . . . . . . 49
4 LibraryandExtensionFAQ 51
4.1 GeneralLibraryQuestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.1.1 HowdoIfindamoduleorapplicationtoperformtaskX? . . . . . . . . . . . . . . . . . 51
4.1.2 Whereisthemath.py(socket.py,regex.py,etc.) sourcefile? . . . . . . . . . . . . . . . . 51
4.1.3 HowdoImakeaPythonscriptexecutableonUnix? . . . . . . . . . . . . . . . . . . . . 51
4.1.4 Isthereacurses/termcappackageforPython? . . . . . . . . . . . . . . . . . . . . . . . 52
4.1.5 IsthereanequivalenttoC’sonexit()inPython? . . . . . . . . . . . . . . . . . . . . . . 52
4.1.6 Whydon’tmysignalhandlerswork? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.2 Commontasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.2.1 HowdoItestaPythonprogramorcomponent? . . . . . . . . . . . . . . . . . . . . . . 52
4.2.2 HowdoIcreatedocumentationfromdocstrings? . . . . . . . . . . . . . . . . . . . . . 53
4.2.3 HowdoIgetasinglekeypressatatime? . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3 Threads . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.1 HowdoIprogramusingthreads? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.2 Noneofmythreadsseemtorun: why? . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.3 HowdoIparceloutworkamongabunchofworkerthreads? . . . . . . . . . . . . . . . 54
4.3.4 Whatkindsofglobalvaluemutationarethread-safe? . . . . . . . . . . . . . . . . . . . . 55
4.3.5 Can’twegetridoftheGlobalInterpreterLock? . . . . . . . . . . . . . . . . . . . . . . 55
4.4 InputandOutput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.4.1 HowdoIdeleteafile? (Andotherfilequestions…) . . . . . . . . . . . . . . . . . . . . 56
4.4.2 HowdoIcopyafile? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.4.3 HowdoIread(orwrite)binarydata? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.4.4 Ican’tseemtouseos.read()onapipecreatedwithos.popen();why?. . . . . . . . . . . . 57
iii

### 第6页

4.4.5 HowdoIaccesstheserial(RS232)port? . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.4.6 Whydoesn’tclosingsys.stdout(stdin,stderr)reallycloseit? . . . . . . . . . . . . . . . . 57
4.5 Network/InternetProgramming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.5.1 WhatWWWtoolsarethereforPython? . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.5.2 WhatmoduleshouldIusetohelpwithgeneratingHTML? . . . . . . . . . . . . . . . . . 58
4.5.3 HowdoIsendmailfromaPythonscript? . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.5.4 HowdoIavoidblockingintheconnect()methodofasocket? . . . . . . . . . . . . . . . 58
4.6 Databases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.6.1 ArethereanyinterfacestodatabasepackagesinPython?. . . . . . . . . . . . . . . . . . 59
4.6.2 HowdoyouimplementpersistentobjectsinPython? . . . . . . . . . . . . . . . . . . . . 59
4.7 MathematicsandNumerics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.7.1 HowdoIgeneraterandomnumbersinPython?. . . . . . . . . . . . . . . . . . . . . . . 59
5 Extending/EmbeddingFAQ 61
5.1 CanIcreatemyownfunctionsinC? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5.2 CanIcreatemyownfunctionsinC++? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5.3 WritingCishard;arethereanyalternatives? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5.4 HowcanIexecutearbitraryPythonstatementsfromC? . . . . . . . . . . . . . . . . . . . . . . . 61
5.5 HowcanIevaluateanarbitraryPythonexpressionfromC? . . . . . . . . . . . . . . . . . . . . . 61
5.6 HowdoIextractCvaluesfromaPythonobject? . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5.7 HowdoIusePy_BuildValue()tocreateatupleofarbitrarylength? . . . . . . . . . . . . . . . . . 62
5.8 HowdoIcallanobject’smethodfromC? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
5.9 HowdoIcatchtheoutputfromPyErr_Print()(oranythingthatprintstostdout/stderr)? . . . . . . 62
5.10 HowdoIaccessamodulewritteninPythonfromC? . . . . . . . . . . . . . . . . . . . . . . . . 63
5.11 HowdoIinterfacetoC++objectsfromPython?. . . . . . . . . . . . . . . . . . . . . . . . . . . 63
5.12 IaddedamoduleusingtheSetupfileandthemakefails;why? . . . . . . . . . . . . . . . . . . . 63
5.13 HowdoIdebuganextension? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
5.14 IwanttocompileaPythonmoduleonmyLinuxsystem,butsomefilesaremissing. Why? . . . . . 64
5.15 HowdoItell“incompleteinput”from“invalidinput”? . . . . . . . . . . . . . . . . . . . . . . . 64
5.16 HowdoIfindundefinedg++symbols__builtin_newor__pure_virtual? . . . . . . . . . . . . . . 64
5.17 CanIcreateanobjectclasswithsomemethodsimplementedinCandothersinPython(e.g. through
inheritance)? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
6 PythononWindowsFAQ 65
6.1 HowdoIrunaPythonprogramunderWindows? . . . . . . . . . . . . . . . . . . . . . . . . . . 65
6.2 HowdoImakePythonscriptsexecutable? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.3 WhydoesPythonsometimestakesolongtostart? . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.4 HowdoImakeanexecutablefromaPythonscript? . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.5 Isa*.pydfilethesameasaDLL? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.6 HowcanIembedPythonintoaWindowsapplication? . . . . . . . . . . . . . . . . . . . . . . . 67
6.7 HowdoIkeepeditorsfrominsertingtabsintomyPythonsource? . . . . . . . . . . . . . . . . . 68
6.8 HowdoIcheckforakeypresswithoutblocking? . . . . . . . . . . . . . . . . . . . . . . . . . . 68
6.9 HowdoIsolvethemissingapi-ms-win-crt-runtime-l1-1-0.dllerror? . . . . . . . . . . . . . . . . 68
7 GraphicUserInterfaceFAQ 69
7.1 GeneralGUIQuestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.2 WhatGUItoolkitsexistforPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.3 Tkinterquestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.3.1 HowdoIfreezeTkinterapplications?. . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
7.3.2 CanIhaveTkeventshandledwhilewaitingforI/O? . . . . . . . . . . . . . . . . . . . . 69
7.3.3 Ican’tgetkeybindingstoworkinTkinter: why? . . . . . . . . . . . . . . . . . . . . . . 69
8 “WhyisPythonInstalledonmyComputer?” FAQ 71
8.1 WhatisPython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.2 WhyisPythoninstalledonmymachine? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.3 CanIdeletePython? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
A Glossary 73
iv

### 第7页

B Aboutthisdocumentation 91
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
C HistoryandLicense 93
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 94
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 94
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 95
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 95
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 96
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 97
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 97
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
D Copyright 113
Index 115
v

### 第8页

vi

### 第9页

CHAPTER
ONE
GENERAL PYTHON FAQ
1.1 General Information
1.1.1 What is Python?
Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions,
dynamictyping,veryhighleveldynamicdatatypes,andclasses. Itsupportsmultipleprogrammingparadigmsbeyond
object-orientedprogramming,suchasproceduralandfunctionalprogramming. Pythoncombinesremarkablepower
with very clear syntax. It has interfaces to many system calls and libraries, as well as to various window systems,
andisextensibleinCorC++. Itisalsousableasanextensionlanguageforapplicationsthatneedaprogrammable
interface. Finally,Pythonisportable: itrunsonmanyUnixvariantsincludingLinuxandmacOS,andonWindows.
Tofindoutmore,startwithtutorial-index. TheBeginner’sGuidetoPythonlinkstootherintroductorytutorialsand
resourcesforlearningPython.
1.1.2 What is the Python Software Foundation?
ThePythonSoftwareFoundationisanindependentnon-profitorganizationthatholdsthecopyrightonPythonver-
sions2.1andnewer. ThePSF’smissionistoadvanceopensourcetechnologyrelatedtothePythonprogramming
languageandtopublicizetheuseofPython. ThePSF’shomepageisathttps://www.python.org/psf/.
DonationstothePSFaretax-exemptintheUS.IfyouusePythonandfindithelpful,pleasecontributeviathePSF
donationpage.
1.1.3 Are there copyright restrictions on the use of Python?
Youcandoanythingyouwantwiththesource,aslongasyouleavethecopyrightsinanddisplaythosecopyrights
in any documentation about Python that you produce. If you honor the copyright rules, it’s OK to use Python for
commercialuse,tosellcopiesofPythoninsourceorbinaryform(modifiedorunmodified),ortosellproductsthat
incorporatePythoninsomeform. WewouldstillliketoknowaboutallcommercialuseofPython,ofcourse.
SeethelicensepagetofindfurtherexplanationsandthefulltextofthePSFLicense.
ThePythonlogoistrademarked,andincertaincasespermissionisrequiredtouseit. ConsulttheTrademarkUsage
Policyformoreinformation.
1.1.4 Why was Python created in the first place?
Here’saverybriefsummaryofwhatstarteditall,writtenbyGuidovanRossum:
IhadextensiveexperiencewithimplementinganinterpretedlanguageintheABCgroupatCWI,and
fromworkingwiththisgroupIhadlearnedalotaboutlanguagedesign. ThisistheoriginofmanyPython
features,includingtheuseofindentationforstatementgroupingandtheinclusionofvery-high-leveldata
types(althoughthedetailsarealldifferentinPython).
IhadanumberofgripesabouttheABClanguage,butalsolikedmanyofitsfeatures. Itwasimpossible
to extend the ABC language (or its implementation) to remedy my complaints – in fact its lack of
extensibilitywasoneofitsbiggestproblems. IhadsomeexperiencewithusingModula-2+andtalked
1

### 第10页

withthedesignersofModula-3andreadtheModula-3report. Modula-3istheoriginofthesyntaxand
semanticsusedforexceptions,andsomeotherPythonfeatures.
IwasworkingintheAmoebadistributedoperatingsystemgroupatCWI.Weneededabetterwayto
dosystemadministrationthanbywritingeitherCprogramsorBourneshellscripts,sinceAmoebahad
itsownsystemcallinterfacewhichwasn’teasilyaccessiblefromtheBourneshell. Myexperiencewith
errorhandlinginAmoebamademeacutelyawareoftheimportanceofexceptionsasaprogramming
languagefeature.
ItoccurredtomethatascriptinglanguagewithasyntaxlikeABCbutwithaccesstotheAmoebasystem
callswouldfilltheneed. IrealizedthatitwouldbefoolishtowriteanAmoeba-specificlanguage,soI
decidedthatIneededalanguagethatwasgenerallyextensible.
Duringthe1989Christmasholidays,Ihadalotoftimeonmyhand,soIdecidedtogiveitatry. During
thenextyear,whilestillmostlyworkingonitinmyowntime,PythonwasusedintheAmoebaproject
withincreasingsuccess,andthefeedbackfromcolleaguesmademeaddmanyearlyimprovements.
InFebruary1991, afterjustoverayearofdevelopment,IdecidedtoposttoUSENET.Therestisin
theMisc/HISTORYfile.
1.1.5 What is Python good for?
Pythonisahigh-levelgeneral-purposeprogramminglanguagethatcanbeappliedtomanydifferentclassesofprob-
lems.
The language comes with a large standard library that covers areas such as string processing (regular expressions,
Unicode, calculatingdifferencesbetweenfiles), internetprotocols(HTTP,FTP,SMTP,XML-RPC,POP,IMAP),
softwareengineering(unittesting,logging,profiling,parsingPythoncode),andoperatingsysteminterfaces(system
calls,filesystems,TCP/IPsockets). Lookatthetableofcontentsforlibrary-indextogetanideaofwhat’savailable.
Awidevarietyofthird-partyextensionsarealsoavailable. ConsultthePythonPackageIndextofindpackagesof
interesttoyou.
1.1.6 How does the Python version numbering scheme work?
Pythonversionsarenumbered“A.B.C”or“A.B”:
• Aisthemajorversionnumber–itisonlyincrementedforreallymajorchangesinthelanguage.
• Bistheminorversionnumber–itisincrementedforlessearth-shatteringchanges.
• C isthemicroversionnumber–itisincrementedforeachbugfixrelease.
Notallreleasesarebugfixreleases. Intherun-uptoanewfeaturerelease,aseriesofdevelopmentreleasesaremade,
denoted as alpha, beta, or release candidate. Alphas are early releases in which interfaces aren’t yet finalized; it’s
not unexpected to see an interface change between two alpha releases. Betas are more stable, preserving existing
interfacesbutpossiblyaddingnewmodules,andreleasecandidatesarefrozen,makingnochangesexceptasneeded
tofixcriticalbugs.
Alpha,betaandreleasecandidateversionshaveanadditionalsuffix:
• Thesuffixforanalphaversionis“aN”forsomesmallnumberN.
• Thesuffixforabetaversionis“bN”forsomesmallnumberN.
• Thesuffixforareleasecandidateversionis“rcN”forsomesmallnumberN.
Inotherwords,allversionslabeled2.0aNprecedetheversionslabeled2.0bN,whichprecedeversionslabeled2.0rcN,
andthoseprecede2.0.
Youmayalsofindversionnumberswitha“+”suffix,e.g. “2.2+”. Theseareunreleasedversions,builtdirectlyfrom
theCPythondevelopmentrepository. Inpractice,afterafinalminorreleaseismade,theversionisincrementedto
thenextminorversion,whichbecomesthe“a0”version,e.g. “2.4a0”.
See the Developer’s Guide for more information about the development cycle, and PEP 387 to learn more about
Python’s backward compatibility policy. See also the documentation for sys.version, sys.hexversion, and
sys.version_info.
2 Chapter1. GeneralPythonFAQ

### 第11页

1.1.7 How do I obtain a copy of the Python source?
The latest Python source distribution is always available from python.org, at https://www.python.org/downloads/.
Thelatestdevelopmentsourcescanbeobtainedathttps://github.com/python/cpython/.
The source distribution is a gzipped tar file containing the complete C source, Sphinx-formatted documentation,
Python library modules, example programs, and several useful pieces of freely distributable software. The source
willcompileandrunoutoftheboxonmostUNIXplatforms.
ConsulttheGettingStartedsectionofthePythonDeveloper’sGuideformoreinformationongettingthesourcecode
andcompilingit.
1.1.8 How do I get documentation on Python?
ThestandarddocumentationforthecurrentstableversionofPythonisavailableathttps://docs.python.org/3/. PDF,
plaintext,anddownloadableHTMLversionsarealsoavailableathttps://docs.python.org/3/download.html.
The documentation is written in reStructuredText and processed by the Sphinx documentation tool. The reStruc-
turedTextsourceforthedocumentationispartofthePythonsourcedistribution.
1.1.9 I’ve never programmed before. Is there a Python tutorial?
Therearenumeroustutorialsandbooksavailable. Thestandarddocumentationincludestutorial-index.
ConsulttheBeginner’sGuidetofindinformationforbeginningPythonprogrammers,includinglistsoftutorials.
1.1.10 Is there a newsgroup or mailing list devoted to Python?
There is a newsgroup, comp.lang.python, and a mailing list, python-list. The newsgroup and mailing list are
gatewayed into each other – if you can read news it’s unnecessary to subscribe to the mailing list. comp.lang.
python is high-traffic, receiving hundreds of postings every day, and Usenet readers are often more able to cope
withthisvolume.
Announcementsofnewsoftwarereleasesandeventscanbefoundincomp.lang.python.announce,alow-trafficmod-
eratedlistthatreceivesaboutfivepostingsperday. It’savailableasthepython-announcemailinglist.
Moreinfoaboutothermailinglistsandnewsgroupscanbefoundathttps://www.python.org/community/lists/.
1.1.11 How do I get a beta test version of Python?
Alphaandbetareleasesareavailablefromhttps://www.python.org/downloads/. Allreleasesareannouncedonthe
comp.lang.pythonandcomp.lang.python.announcenewsgroupsandonthePythonhomepageathttps://www.python.
org/;anRSSfeedofnewsisavailable.
YoucanalsoaccessthedevelopmentversionofPythonthroughGit. SeeThePythonDeveloper’sGuidefordetails.
1.1.12 How do I submit bug reports and patches for Python?
Toreportabugorsubmitapatch,usetheissuetrackerathttps://github.com/python/cpython/issues.
FormoreinformationonhowPythonisdeveloped,consultthePythonDeveloper’sGuide.
1.1.13 Are there any published articles about Python that I can reference?
It’sprobablybesttociteyourfavoritebookaboutPython.
TheveryfirstarticleaboutPythonwaswrittenin1991andisnowquiteoutdated.
Guido van Rossum and Jelke de Boer, “Interactively Testing Remote Servers Using the Python Pro-
grammingLanguage”,CWIQuarterly,Volume4,Issue4(December1991),Amsterdam,pp283–303.
1.1. GeneralInformation 3

### 第12页

1.1.14 Are there any books on Python?
Yes, there are many, and more are being published. See the python.org wiki at https://wiki.python.org/moin/
PythonBooksforalist.
Youcanalsosearchonlinebookstoresfor“Python”andfilterouttheMontyPythonreferences;orperhapssearchfor
“Python”and“language”.
1.1.15 Where in the world is www.python.org located?
ThePythonproject’sinfrastructureislocatedallovertheworldandismanagedbythePythonInfrastructureTeam.
Detailshere.
1.1.16 Why is it called Python?
When he began implementing Python, Guido van Rossum was also reading the published scripts from “Monty
Python’s Flying Circus”, a BBC comedy series from the 1970s. Van Rossum thought he needed a name that was
short,unique,andslightlymysterious,sohedecidedtocallthelanguagePython.
1.1.17 Do I have to like “Monty Python’s Flying Circus”?
No,butithelps. :)
1.2 Python in the real world
1.2.1 How stable is Python?
Very stable. New, stable releases have been coming out roughly every 6 to 18 months since 1991, and this seems
likelytocontinue. Asofversion3.9,Pythonwillhaveanewfeaturereleaseevery12months(PEP602).
Thedevelopersissuebugfixreleasesofolderversions,sothestabilityofexistingreleasesgraduallyimproves. Bugfix
releases, indicatedby a third component ofthe version number (e.g. 3.5.3, 3.6.2), aremanaged for stability; only
fixesforknownproblemsareincludedinabugfixrelease, andit’sguaranteedthatinterfaceswillremainthesame
throughoutaseriesofbugfixreleases.
ThelateststablereleasescanalwaysbefoundonthePythondownloadpage. Python3.xistherecommendedversion
andsupportedbymostwidelyusedlibraries. Python2.xisnotmaintainedanymore.
1.2.2 How many people are using Python?
Thereareprobablymillionsofusers,thoughit’sdifficulttoobtainanexactcount.
Pythonisavailableforfreedownload,sotherearenosalesfigures,andit’savailablefrommanydifferentsitesand
packagedwithmanyLinuxdistributions,sodownloadstatisticsdon’ttellthewholestoryeither.
Thecomp.lang.pythonnewsgroupisveryactive,butnotallPythonusersposttothegrouporevenreadit.
1.2.3 Have any significant projects been done in Python?
Seehttps://www.python.org/about/successforalistofprojectsthatusePython. Consultingtheproceedingsforpast
Pythonconferenceswillrevealcontributionsfrommanydifferentcompaniesandorganizations.
High-profilePythonprojectsincludetheMailmanmailinglistmanagerandtheZopeapplicationserver. SeveralLinux
distributions,mostnotablyRedHat,havewrittenpartoralloftheirinstallerandsystemadministrationsoftwarein
Python. CompaniesthatusePythoninternallyincludeGoogle,Yahoo,andLucasfilmLtd.
1.2.4 What new developments are expected for Python in the future?
Seehttps://peps.python.org/forthePythonEnhancementProposals(PEPs). PEPsaredesigndocumentsdescribing
asuggestednewfeatureforPython,providingaconcisetechnicalspecificationandarationale. LookforaPEPtitled
“PythonX.YReleaseSchedule”,whereX.Yisaversionthathasn’tbeenpubliclyreleasedyet.
4 Chapter1. GeneralPythonFAQ

### 第13页

Newdevelopmentisdiscussedonthepython-devmailinglist.
1.2.5 Is it reasonable to propose incompatible changes to Python?
Ingeneral,no. TherearealreadymillionsoflinesofPythoncodearoundtheworld,soanychangeinthelanguage
thatinvalidatesmorethanaverysmallfractionofexistingprogramshastobefrownedupon. Evenifyoucanprovide
aconversionprogram,there’sstilltheproblemofupdatingalldocumentation;manybookshavebeenwrittenabout
Python,andwedon’twanttoinvalidatethemallatasinglestroke.
Providingagradualupgradepathisnecessaryifafeaturehastobechanged. PEP5describestheprocedurefollowed
forintroducingbackward-incompatiblechangeswhileminimizingdisruptionforusers.
1.2.6 Is Python a good language for beginning programmers?
Yes.
ItisstillcommontostartstudentswithaproceduralandstaticallytypedlanguagesuchasPascal,C,orasubsetof
C++orJava. StudentsmaybebetterservedbylearningPythonastheirfirstlanguage. Pythonhasaverysimpleand
consistentsyntaxandalargestandardlibraryand,mostimportantly,usingPythoninabeginningprogrammingcourse
letsstudentsconcentrateonimportantprogrammingskillssuchasproblemdecompositionanddatatypedesign. With
Python,studentscanbequicklyintroducedtobasicconceptssuchasloopsandprocedures. Theycanprobablyeven
workwithuser-definedobjectsintheirveryfirstcourse.
For a student who has never programmed before, using a statically typed language seems unnatural. It presents
additionalcomplexitythatthestudentmustmasterandslowsthepaceofthecourse. Thestudentsaretryingtolearn
to think like a computer, decompose problems, design consistent interfaces, and encapsulate data. While learning
touseastaticallytypedlanguageisimportantinthelongterm,itisnotnecessarilythebesttopictoaddressinthe
students’firstprogrammingcourse.
Many other aspects of Python make it a good first language. Like Java, Python has a large standard library so
thatstudentscanbeassignedprogrammingprojectsveryearlyinthecoursethatdosomething. Assignmentsaren’t
restricted to the standard four-function calculator and check balancing programs. By using the standard library,
studentscangainthesatisfactionofworkingonrealisticapplicationsastheylearnthefundamentalsofprogramming.
Using the standard library also teaches students about code reuse. Third-party modules such as PyGame are also
helpfulinextendingthestudents’reach.
Python’sinteractiveinterpreterenablesstudentstotestlanguagefeatureswhilethey’reprogramming. Theycankeep
a window with the interpreter running while they enter their program’s source in another window. If they can’t
rememberthemethodsforalist,theycandosomethinglikethis:
>>> L = []
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
'reverse', 'sort']
>>> [d for d in dir(L) if '__' not in d]
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
,→'reverse', 'sort']
>>> help(L.append)
Help on built-in function append:
append(...)
L.append(object) -> None -- append object to end
(continuesonnextpage)
1.2. Pythonintherealworld 5

### 第14页

(continuedfrompreviouspage)
>>> L.append(1)
>>> L
[1]
Withtheinterpreter,documentationisneverfarfromthestudentastheyareprogramming.
TherearealsogoodIDEsforPython. IDLEisacross-platformIDEforPythonthatiswritteninPythonusingTkinter.
Emacs users will be happy to know that there is a very good Python mode for Emacs. All of these programming
environments provide syntax highlighting, auto-indenting, and access to the interactive interpreter while coding.
ConsultthePythonwikiforafulllistofPythoneditingenvironments.
IfyouwanttodiscussPython’suseineducation,youmaybeinterestedinjoiningtheedu-sigmailinglist.
6 Chapter1. GeneralPythonFAQ

### 第15页

CHAPTER
TWO
PROGRAMMING FAQ
2.1 General Questions
2.1.1 Is there a source code level debugger with breakpoints, single-stepping,
etc.?
Yes.
SeveraldebuggersforPythonaredescribedbelow,andthebuilt-infunctionbreakpoint()allowsyoutodropinto
anyofthem.
Thepdbmoduleisasimplebutadequateconsole-modedebuggerforPython. ItispartofthestandardPythonlibrary,
andisdocumented in the Library Reference Manual. Youcanalsowriteyourowndebuggerbyusingthe
codeforpdbasanexample.
TheIDLEinteractivedevelopmentenvironment,whichispartofthestandardPythondistribution(normallyavailable
asTools/scripts/idle3),includesagraphicaldebugger.
PythonWinisaPythonIDEthatincludesaGUIdebuggerbasedonpdb. ThePythonWindebuggercolorsbreakpoints
and has quite a few cool features such as debugging non-PythonWin programs. PythonWin is available as part of
pywin32projectandasapartoftheActivePythondistribution.
EricisanIDEbuiltonPyQtandtheScintillaeditingcomponent.
trepan3kisagdb-likedebugger.
VisualStudioCodeisanIDEwithdebuggingtoolsthatintegrateswithversion-controlsoftware.
ThereareanumberofcommercialPythonIDEsthatincludegraphicaldebuggers. Theyinclude:
• WingIDE
• KomodoIDE
• PyCharm
2.1.2 Are there tools to help find bugs or perform static analysis?
Yes.
PylintandPyflakesdobasiccheckingthatwillhelpyoucatchbugssooner.
StatictypecheckerssuchasMypy,Pyre,andPytypecanchecktypehintsinPythonsourcecode.
2.1.3 How can I create a stand-alone binary from a Python script?
You don’t need the ability to compile Python to C code if all you want is a stand-alone program that users can
downloadandrunwithouthavingtoinstallthePythondistributionfirst. Thereareanumberoftoolsthatdetermine
thesetofmodulesrequiredbyaprogramandbindthesemodulestogetherwithaPythonbinarytoproduceasingle
executable.
7

### 第16页

Oneistousethefreezetool, whichisincludedinthePythonsourcetreeasTools/freeze. ItconvertsPythonbyte
codetoCarrays;withaCcompileryoucanembedallyourmodulesintoanewprogram,whichisthenlinkedwith
thestandardPythonmodules.
Itworksbyscanningyoursourcerecursivelyforimportstatements(inbothforms)andlookingforthemodulesinthe
standardPythonpathaswellasinthesourcedirectory(forbuilt-inmodules). Itthenturnsthebytecodeformodules
writteninPythonintoCcode(arrayinitializersthatcanbeturnedintocodeobjectsusingthemarshalmodule)and
createsacustom-madeconfigfilethatonlycontainsthosebuilt-inmoduleswhichareactuallyusedintheprogram.
ItthencompilesthegeneratedCcodeandlinksitwiththerestofthePythoninterpretertoformaself-contained
binarywhichactsexactlylikeyourscript.
ThefollowingpackagescanhelpwiththecreationofconsoleandGUIexecutables:
• Nuitka(Cross-platform)
• PyInstaller(Cross-platform)
• PyOxidizer(Cross-platform)
• cx_Freeze(Cross-platform)
• py2app(macOSonly)
• py2exe(Windowsonly)
2.1.4 Are there coding standards or a style guide for Python programs?
Yes. ThecodingstylerequiredforstandardlibrarymodulesisdocumentedasPEP8.
2.2 Core Language
2.2.1 Why am I getting an UnboundLocalError when the variable has a value?
ItcanbeasurprisetogettheUnboundLocalErrorinpreviouslyworkingcodewhenitismodifiedbyaddingan
assignmentstatementsomewhereinthebodyofafunction.
Thiscode:
>>> x = 10
>>> def bar():
... print(x)
...
>>> bar()
10
works,butthiscode:
>>> x = 10
>>> def foo():
... print(x)
... x += 1
resultsinanUnboundLocalError:
>>> foo()
Traceback (most recent call last):
...
UnboundLocalError: local variable 'x' referenced before assignment
This is because when you make an assignment to a variable in a scope, that variable becomes local to that scope
and shadows any similarly named variable in the outer scope. Since the last statement in foo assigns a new value
tox,thecompilerrecognizesitasalocalvariable. Consequentlywhentheearlierprint(x)attemptstoprintthe
uninitializedlocalvariableandanerrorresults.
8 Chapter2. ProgrammingFAQ

### 第17页

Intheexampleaboveyoucanaccesstheouterscopevariablebydeclaringitglobal:
>>> x = 10
>>> def foobar():
... global x
... print(x)
... x += 1
...
>>> foobar()
10
Thisexplicitdeclarationisrequiredinordertoremindyouthat(unlikethesuperficiallyanalogoussituationwithclass
andinstancevariables)youareactuallymodifyingthevalueofthevariableintheouterscope:
>>> print(x)
11
Youcandoasimilarthinginanestedscopeusingthenonlocalkeyword:
>>> def foo():
... x = 10
... def bar():
... nonlocal x
... print(x)
... x += 1
... bar()
... print(x)
...
>>> foo()
10
11
2.2.2 What are the rules for local and global variables in Python?
InPython,variablesthatareonlyreferencedinsideafunctionareimplicitlyglobal. Ifavariableisassignedavalue
anywherewithinthefunction’sbody,it’sassumedtobealocalunlessexplicitlydeclaredasglobal.
Thoughabitsurprisingatfirst,amoment’sconsiderationexplainsthis. Ononehand,requiringglobalforassigned
variables provides a bar against unintended side-effects. On the other hand, if global wasrequired for all global
references,you’dbeusingglobalallthetime. You’dhavetodeclareasglobaleveryreferencetoabuilt-infunction
ortoacomponentofanimportedmodule. Thisclutterwoulddefeattheusefulnessoftheglobaldeclarationfor
identifyingside-effects.
2.2.3 Why do lambdas defined in a loop with different values all return the same
result?
Assumeyouuseaforlooptodefineafewdifferentlambdas(orevenplainfunctions),e.g.:
>>> squares = []
>>> for x in range(5):
... squares.append(lambda: x**2)
Thisgivesyoualistthatcontains5lambdasthatcalculatex**2. Youmightexpectthat, whencalled, theywould
return,respectively,0,1,4,9,and16. However,whenyouactuallytryyouwillseethattheyallreturn16:
>>> squares[2]()
16
>>> squares[4]()
16
2.2. CoreLanguage 9

### 第18页

This happens because x is not local to the lambdas, but is defined in the outer scope, and it is accessed when the
lambdaiscalled—notwhenitisdefined. Attheendoftheloop,thevalueofxis4,soallthefunctionsnowreturn
4**2,i.e. 16. Youcanalsoverifythisbychangingthevalueofxandseehowtheresultsofthelambdaschange:
>>> x = 8
>>> squares[2]()
64
Inordertoavoidthis,youneedtosavethevaluesinvariableslocaltothelambdas,sothattheydon’trelyonthevalue
oftheglobalx:
>>> squares = []
>>> for x in range(5):
... squares.append(lambda n=x: n**2)
Here,n=xcreatesanewvariablenlocaltothelambdaandcomputedwhenthelambdaisdefinedsothatithasthe
samevaluethatxhadatthatpointintheloop. Thismeansthatthevalueofnwillbe0inthefirstlambda,1inthe
second,2inthethird,andsoon. Thereforeeachlambdawillnowreturnthecorrectresult:
>>> squares[2]()
4
>>> squares[4]()
16
Notethatthisbehaviourisnotpeculiartolambdas,butappliestoregularfunctionstoo.
2.2.4 How do I share global variables across modules?
Thecanonicalwaytoshareinformationacrossmoduleswithinasingleprogramistocreateaspecialmodule(often
called config or cfg). Just import the config module in all modules of your application; the module then becomes
available as a global name. Because there is only one instance of each module, any changes made to the module
objectgetreflectedeverywhere. Forexample:
config.py:
x = 0 # Default value of the 'x' configuration setting
mod.py:
import config
config.x = 1
main.py:
import config
import mod
print(config.x)
Notethatusingamoduleisalsothebasisforimplementingthesingletondesignpattern,forthesamereason.
2.2.5 What are the “best practices” for using import in a module?
In general, don’t use from modulename import *. Doing so clutters the importer’s namespace, and makes it
muchharderforlinterstodetectundefinednames.
Import modules at the top of a file. Doing so makes it clear what other modules your code requires and avoids
questionsofwhetherthemodulenameisinscope. Usingoneimportperlinemakesiteasytoaddanddeletemodule
imports,butusingmultipleimportsperlineuseslessscreenspace.
It’sgoodpracticeifyouimportmodulesinthefollowingorder:
1. standardlibrarymodules–e.g. sys,os,argparse,re
10 Chapter2. ProgrammingFAQ

### 第19页

2. third-party library modules (anything installed in Python’s site-packages directory) – e.g. dateutil,
requests,PIL.Image
3. locallydevelopedmodules
Itissometimesnecessarytomoveimportstoafunctionorclasstoavoidproblemswithcircularimports. Gordon
McMillansays:
Circular imports are fine where both modules use the “import <module>” form of import. They fail
whenthe2ndmodulewantstograbanameoutofthefirst(“frommoduleimportname”)andtheimport
isatthetoplevel. That’sbecausenamesinthe1starenotyetavailable,becausethefirstmoduleisbusy
importingthe2nd.
Inthiscase,ifthesecondmoduleisonlyusedinonefunction,thentheimportcaneasilybemovedintothatfunction.
By the time the import is called, the first module will have finished initializing, and the second module can do its
import.
Itmayalsobenecessarytomoveimportsoutofthetoplevelofcodeifsomeofthemodulesareplatform-specific.
Inthatcase,itmaynotevenbepossibletoimportallofthemodulesatthetopofthefile. Inthiscase,importingthe
correctmodulesinthecorrespondingplatform-specificcodeisagoodoption.
Onlymoveimportsintoalocalscope,suchasinsideafunctiondefinition,ifit’snecessarytosolveaproblemsuch
asavoidingacircularimportoraretryingtoreducetheinitializationtimeofamodule. Thistechniqueisespecially
helpfulifmanyoftheimportsareunnecessarydependingonhowtheprogramexecutes. Youmayalsowanttomove
importsintoafunctionifthemodulesareonlyeverusedinthatfunction. Notethatloadingamodulethefirsttime
maybeexpensivebecauseoftheonetimeinitializationofthemodule,butloadingamodulemultipletimesisvirtually
free, costing only a couple of dictionary lookups. Even if the module name has gone out of scope, the module is
probablyavailableinsys.modules.
2.2.6 Why are default values shared between objects?
Thistypeofbugcommonlybitesneophyteprogrammers. Considerthisfunction:
def foo(mydict={}): # Danger: shared reference to one dict for all calls
... compute something ...
mydict[key] = value
return mydict
Thefirsttimeyoucallthisfunction,mydictcontainsasingleitem. Thesecondtime,mydictcontainstwoitems
becausewhenfoo()beginsexecuting,mydictstartsoutwithanitemalreadyinit.
Itisoftenexpectedthatafunctioncallcreatesnewobjectsfordefaultvalues. Thisisnotwhathappens. Defaultvalues
arecreatedexactlyonce,whenthefunctionisdefined. Ifthatobjectischanged,likethedictionaryinthisexample,
subsequentcallstothefunctionwillrefertothischangedobject.
By definition, immutable objects such as numbers, strings, tuples, and None, are safe from change. Changes to
mutableobjectssuchasdictionaries,lists,andclassinstancescanleadtoconfusion.
Becauseofthisfeature,itisgoodprogrammingpracticetonotusemutableobjectsasdefaultvalues. Instead,useNone
asthedefaultvalueandinsidethefunction,checkiftheparameterisNoneandcreateanewlist/dictionary/whatever
ifitis. Forexample,don’twrite:
def foo(mydict={}):
...
but:
def foo(mydict=None):
if mydict is None:
mydict = {} # create a new dict for local namespace
2.2. CoreLanguage 11

### 第20页

Thisfeaturecanbeuseful. Whenyouhaveafunctionthat’stime-consumingtocompute,acommontechniqueisto
cache the parameters and the resulting value of each call to the function, and return the cached value if the same
valueisrequestedagain. Thisiscalled“memoizing”,andcanbeimplementedlikethis:
# Callers can only provide two parameters and optionally pass _cache by keyword
def expensive(arg1, arg2, *, _cache={}):
if (arg1, arg2) in _cache:
return _cache[(arg1, arg2)]
# Calculate the value
result = ... expensive computation ...
_cache[(arg1, arg2)] = result # Store result in the cache
return result
Youcoulduseaglobalvariablecontainingadictionaryinsteadofthedefaultvalue;it’samatteroftaste.
2.2.7 How can I pass optional or keyword parameters from one function to an-
other?
Collect the arguments using the * and ** specifiers in the function’s parameter list; this gives you the positional
argumentsasatupleandthekeywordargumentsasadictionary. Youcanthenpasstheseargumentswhencalling
anotherfunctionbyusing*and**:
def f(x, *args, **kwargs):
...
kwargs['width'] = '14.3c'
...
g(x, *args, **kwargs)
2.2.8 What is the difference between arguments and parameters?
Parametersaredefinedbythenamesthatappearinafunctiondefinition,whereasargumentsarethevaluesactually
passedtoafunctionwhencallingit. Parametersdefinewhatkindofargumentsafunctioncanaccept. Forexample,
giventhefunctiondefinition:
def func(foo, bar=None, **kwargs):
pass
foo,barandkwargsareparametersoffunc. However,whencallingfunc,forexample:
func(42, bar=314, extra=somevar)
thevalues42,314,andsomevararearguments.
2.2.9 Why did changing list ‘y’ also change list ‘x’?
Ifyouwrotecodelike:
>>> x = []
>>> y = x
>>> y.append(10)
>>> y
[10]
>>> x
[10]
youmightbewonderingwhyappendinganelementtoychangedxtoo.
Therearetwofactorsthatproducethisresult:
12 Chapter2. ProgrammingFAQ

### 第21页

1) Variablesaresimplynamesthatrefertoobjects. Doingy = xdoesn’tcreateacopyofthelist–itcreatesa
newvariableythatreferstothesameobjectxrefersto. Thismeansthatthereisonlyoneobject(thelist),and
bothxandyrefertoit.
2) Listsaremutable,whichmeansthatyoucanchangetheircontent.
Afterthecalltoappend(),thecontentofthemutableobjecthaschangedfrom[]to[10]. Sinceboththevariables
refertothesameobject,usingeithernameaccessesthemodifiedvalue[10].
Ifweinsteadassignanimmutableobjecttox:
>>> x = 5 # ints are immutable
>>> y = x
>>> x = x + 1 # 5 can't be mutated, we are creating a new object here
>>> x
6
>>> y
5
wecanseethatinthiscasexandyarenotequalanymore. Thisisbecauseintegersareimmutable,andwhenwedo
x = x + 1wearenotmutatingtheint5byincrementingitsvalue;instead,wearecreatinganewobject(theint6)
andassigningittox(thatis,changingwhichobjectxrefersto). Afterthisassignmentwehavetwoobjects(theints
6and5)andtwovariablesthatrefertothem(xnowrefersto6butystillrefersto5).
Some operations (for example y.append(10) and y.sort()) mutate the object, whereas superficially similar
operations (for example y = y + [10] and sorted(y)) create a new object. In general in Python (and in all
casesinthestandardlibrary)amethodthatmutatesanobjectwillreturnNonetohelpavoidgettingthetwotypesof
operationsconfused. Soifyoumistakenlywritey.sort()thinkingitwillgiveyouasortedcopyofy,you’llinstead
endupwithNone,whichwilllikelycauseyourprogramtogenerateaneasilydiagnosederror.
However,thereisoneclassofoperationswherethesameoperationsometimeshasdifferentbehaviorswithdifferent
types: theaugmentedassignmentoperators. Forexample,+=mutateslistsbutnottuplesorints(a_list += [1,
2, 3]isequivalenttoa_list.extend([1, 2, 3])andmutatesa_list,whereassome_tuple += (1, 2,
3)andsome_int += 1createnewobjects).
Inotherwords:
• Ifwehaveamutableobject(list,dict,set,etc.),wecanusesomespecificoperationstomutateitandall
thevariablesthatrefertoitwillseethechange.
• Ifwehaveanimmutableobject(str,int,tuple,etc.),allthevariablesthatrefertoitwillalwaysseethe
samevalue,butoperationsthattransformthatvalueintoanewvaluealwaysreturnanewobject.
If you want to know if two variables refer to the same object or not, you can use the is operator, or the built-in
functionid().
2.2.10 How do I write a function with output parameters (call by reference)?
RememberthatargumentsarepassedbyassignmentinPython. Sinceassignmentjustcreatesreferencestoobjects,
there’snoaliasbetweenanargumentnameinthecallerandcallee,andsonocall-by-referenceperse. Youcanachieve
thedesiredeffectinanumberofways.
1) Byreturningatupleoftheresults:
>>> def func1(a, b):
... a = 'new-value' # a and b are local names
... b = b + 1 # assigned to new objects
... return a, b # return new values
...
>>> x, y = 'old-value', 99
>>> func1(x, y)
('new-value', 100)
Thisisalmostalwaystheclearestsolution.
2.2. CoreLanguage 13

### 第22页

2) Byusingglobalvariables. Thisisn’tthread-safe,andisnotrecommended.
3) Bypassingamutable(changeablein-place)object:
>>> def func2(a):
... a[0] = 'new-value' # 'a' references a mutable list
... a[1] = a[1] + 1 # changes a shared object
...
>>> args = ['old-value', 99]
>>> func2(args)
>>> args
['new-value', 100]
4) Bypassinginadictionarythatgetsmutated:
>>> def func3(args):
... args['a'] = 'new-value' # args is a mutable dictionary
... args['b'] = args['b'] + 1 # change it in-place
...
>>> args = {'a': 'old-value', 'b': 99}
>>> func3(args)
>>> args
{'a': 'new-value', 'b': 100}
5) Orbundleupvaluesinaclassinstance:
>>> class Namespace:
... def __init__(self, /, **args):
... for key, value in args.items():
... setattr(self, key, value)
...
>>> def func4(args):
... args.a = 'new-value' # args is a mutable Namespace
... args.b = args.b + 1 # change object in-place
...
>>> args = Namespace(a='old-value', b=99)
>>> func4(args)
>>> vars(args)
{'a': 'new-value', 'b': 100}
There’salmostneveragoodreasontogetthiscomplicated.
Yourbestchoiceistoreturnatuplecontainingthemultipleresults.
2.2.11 How do you make a higher order function in Python?
Youhavetwochoices: youcanusenestedscopesoryoucanusecallableobjects. Forexample,supposeyouwanted
todefinelinear(a,b)whichreturnsafunctionf(x)thatcomputesthevaluea*x+b. Usingnestedscopes:
def linear(a, b):
def result(x):
return a * x + b
return result
Orusingacallableobject:
class linear:
def __init__(self, a, b):
(continuesonnextpage)
14 Chapter2. ProgrammingFAQ

### 第23页

(continuedfrompreviouspage)
self.a, self.b = a, b
def __call__(self, x):
return self.a * x + self.b
Inbothcases,
taxes = linear(0.3, 2)
givesacallableobjectwheretaxes(10e6) == 0.3 * 10e6 + 2.
Thecallableobjectapproachhasthedisadvantagethatitisabitslowerandresultsinslightlylongercode. However,
notethatacollectionofcallablescansharetheirsignatureviainheritance:
class exponential(linear):
# __init__ inherited
def __call__(self, x):
return self.a * (x ** self.b)
Objectcanencapsulatestateforseveralmethods:
class counter:
value = 0
def set(self, x):
self.value = x
def up(self):
self.value = self.value + 1
def down(self):
self.value = self.value - 1
count = counter()
inc, dec, reset = count.up, count.down, count.set
Hereinc(),dec()andreset()actlikefunctionswhichsharethesamecountingvariable.
2.2.12 How do I copy an object in Python?
Ingeneral,trycopy.copy()orcopy.deepcopy()forthegeneralcase. Notallobjectscanbecopied,butmost
can.
Someobjectscanbecopiedmoreeasily. Dictionarieshaveacopy()method:
newdict = olddict.copy()
Sequencescanbecopiedbyslicing:
new_l = l[:]
2.2.13 How can I find the methods or attributes of an object?
Foraninstancexofauser-definedclass,dir(x)returnsanalphabetizedlistofthenamescontainingtheinstance
attributesandmethodsandattributesdefinedbyitsclass.
2.2. CoreLanguage 15

### 第24页

2.2.14 How can my code discover the name of an object?
Generallyspeaking,itcan’t,becauseobjectsdon’treallyhavenames. Essentially,assignmentalwaysbindsanameto
avalue;thesameistrueofdefandclassstatements,butinthatcasethevalueisacallable. Considerthefollowing
code:
>>> class A:
... pass
...
>>> B = A
>>> a = B()
>>> b = a
>>> print(b)
<__main__.A object at 0x16D07CC>
>>> print(a)
<__main__.A object at 0x16D07CC>
Arguablytheclasshasaname: eventhoughitisboundtotwonamesandinvokedthroughthenameBthecreated
instanceisstillreportedasaninstanceofclassA.However,itisimpossibletosaywhethertheinstance’snameisa
orb,sincebothnamesareboundtothesamevalue.
Generallyspeakingitshouldnotbenecessaryforyourcodeto“knowthenames”ofparticularvalues. Unlessyouare
deliberatelywritingintrospectiveprograms,thisisusuallyanindicationthatachangeofapproachmightbebeneficial.
Incomp.lang.python,FredrikLundhoncegaveanexcellentanalogyinanswertothisquestion:
Thesamewayasyougetthenameofthatcatyoufoundonyourporch: thecat(object)itselfcannot
tellyouitsname,anditdoesn’treallycare–sotheonlywaytofindoutwhatit’scalledistoaskallyour
neighbours(namespaces)ifit’stheircat(object)…
….anddon’tbesurprisedifyou’llfindthatit’sknownbymanynames,ornonameatall!
2.2.15 What’s up with the comma operator’s precedence?
CommaisnotanoperatorinPython. Considerthissession:
>>> "a" in "b", "a"
(False, 'a')
Sincethecommaisnotanoperator,butaseparatorbetweenexpressionstheaboveisevaluatedasifyouhadentered:
("a" in "b"), "a"
not:
"a" in ("b", "a")
Thesameistrueofthevariousassignmentoperators(=,+=etc). Theyarenottrulyoperatorsbutsyntacticdelimiters
inassignmentstatements.
2.2.16 Is there an equivalent of C’s “?:” ternary operator?
Yes,thereis. Thesyntaxisasfollows:
[on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y
BeforethissyntaxwasintroducedinPython2.5,acommonidiomwastouselogicaloperators:
16 Chapter2. ProgrammingFAQ

### 第25页

[expression] and [on_true] or [on_false]
However,thisidiomisunsafe,asitcangivewrongresultswhenon_truehasafalsebooleanvalue. Therefore,itis
alwaysbettertousethe... if ... else ...form.
2.2.17 Is it possible to write obfuscated one-liners in Python?
Yes. Usuallythisisdonebynestinglambdawithinlambda. Seethefollowingthreeexamples,slightlyadaptedfrom
UlfBartelt:
from functools import reduce
# Primes < 1000
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))
# First 10 Fibonacci numbers
print(list(map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1:
f(x,f), range(10))))
# Mandelbrot set
print((lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+'\n'+y,map(lambda y,
Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
>=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24))
# \___ ___/ \___ ___/ | | |__ lines on screen
# V V | |______ columns on screen
# | | |__________ maximum of "iterations"
# | |_________________ range on y axis
# |____________________________ range on x axis
Don’ttrythisathome,kids!
2.2.18 What does the slash(/) in the parameter list of a function mean?
A slash in the argument list of a function denotes that the parameters prior to it are positional-only. Positional-
onlyparametersaretheoneswithoutanexternallyusablename. Uponcallingafunctionthatacceptspositional-only
parameters,argumentsaremappedtoparametersbasedsolelyontheirposition. Forexample,divmod()isafunction
thatacceptspositional-onlyparameters. Itsdocumentationlookslikethis:
>>> help(divmod)
Help on built-in function divmod in module builtins:
divmod(x, y, /)
Return the tuple (x//y, x%y). Invariant: div*y + mod == x.
Theslashattheendoftheparameterlistmeansthatbothparametersarepositional-only. Thus,callingdivmod()
withkeywordargumentswouldleadtoanerror:
>>> divmod(x=3, y=4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: divmod() takes no keyword arguments
2.2. CoreLanguage 17

### 第26页

2.3 Numbers and strings
2.3.1 How do I specify hexadecimal and octal integers?
Tospecifyanoctaldigit,precedetheoctalvaluewithazero,andthenaloweroruppercase“o”. Forexample,toset
thevariable“a”totheoctalvalue“10”(8indecimal),type:
>>> a = 0o10
>>> a
8
Hexadecimalisjustaseasy. Simplyprecedethehexadecimalnumberwithazero,andthenaloweroruppercase“x”.
Hexadecimaldigitscanbespecifiedinloweroruppercase. Forexample,inthePythoninterpreter:
>>> a = 0xa5
>>> a
165
>>> b = 0XB2
>>> b
178
2.3.2 Why does -22 // 10 return -3?
It’sprimarilydrivenbythedesirethati % jhavethesamesignasj. Ifyouwantthat,andalsowant:
i == (i // j) * j + (i % j)
thenintegerdivisionhastoreturnthefloor. Calsorequiresthatidentitytohold,andthencompilersthattruncatei
// jneedtomakei % jhavethesamesignasi.
Therearefewrealusecasesfori % jwhenjisnegative. Whenjispositive,therearemany,andinvirtuallyallof
themit’smoreusefulfori % jtobe>= 0. Iftheclocksays10now,whatdiditsay200hoursago? -190 % 12
== 2isuseful;-190 % 12 == -10isabugwaitingtobite.
2.3.3 How do I get int literal attribute instead of SyntaxError?
TryingtolookupanintliteralattributeinthenormalmannergivesaSyntaxErrorbecausetheperiodisseenas
adecimalpoint:
>>> 1.__class__
File "<stdin>", line 1
1.__class__
^
SyntaxError: invalid decimal literal
Thesolutionistoseparatetheliteralfromtheperiodwitheitheraspaceorparentheses.
>>> 1 .__class__
<class 'int'>
>>> (1).__class__
<class 'int'>
2.3.4 How do I convert a string to a number?
Forintegers,usethebuilt-inint()typeconstructor,e.g. int('144') == 144. Similarly,float()convertsto
afloating-pointnumber,e.g. float('144') == 144.0.
Bydefault,theseinterpretthenumberasdecimal,sothatint('0144') == 144holdstrue,andint('0x144')
raisesValueError. int(string, base)takesthebasetoconvertfromasasecondoptionalargument,soint(
18 Chapter2. ProgrammingFAQ

### 第27页

'0x144', 16) == 324. Ifthebaseisspecifiedas0,thenumberisinterpretedusingPython’srules: aleading‘0o’
indicatesoctal,and‘0x’indicatesahexnumber.
Donotusethebuilt-infunctioneval()ifallyouneedistoconvertstringstonumbers. eval()willbesignificantly
sloweranditpresentsasecurityrisk: someonecouldpassyouaPythonexpressionthatmighthaveunwantedside
effects. Forexample,someonecouldpass__import__('os').system("rm -rf $HOME")whichwoulderase
yourhomedirectory.
eval()alsohastheeffectofinterpretingnumbersasPythonexpressions,sothate.g. eval('09')givesasyntax
errorbecausePythondoesnotallowleading‘0’inadecimalnumber(except‘0’).
2.3.5 How do I convert a number to a string?
To convert, e.g., the number 144 to the string '144', use the built-in type constructor str(). If you want a
hexadecimal or octal representation, use the built-in functions hex() or oct(). For fancy formatting, see the f-
stringsandformatstringssections, e.g. "{:04d}".format(144)yields'0144'and"{:.3f}".format(1.0/
3.0)yields'0.333'.
2.3.6 How do I modify a string in place?
You can’t, because strings are immutable. In most situations, you should simply construct a new string from the
various parts you want to assemble it from. However, if you need an object with the ability to modify in-place
unicodedata,tryusinganio.StringIOobjectorthearraymodule:
>>> import io
>>> s = "Hello, world"
>>> sio = io.StringIO(s)
>>> sio.getvalue()
'Hello, world'
>>> sio.seek(7)
7
>>> sio.write("there!")
6
>>> sio.getvalue()
'Hello, there!'
>>> import array
>>> a = array.array('w', s)
>>> print(a)
array('w', 'Hello, world')
>>> a[0] = 'y'
>>> print(a)
array('w', 'yello, world')
>>> a.tounicode()
'yello, world'
2.3.7 How do I use strings to call functions/methods?
Therearevarioustechniques.
• Thebestistouseadictionarythatmapsstringstofunctions. Theprimaryadvantageofthistechniqueisthat
thestringsdonotneedtomatchthenamesofthefunctions. Thisisalsotheprimarytechniqueusedtoemulate
acaseconstruct:
def a():
pass
def b():
pass
(continuesonnextpage)
2.3. Numbersandstrings 19

### 第28页

(continuedfrompreviouspage)
dispatch = {'go': a, 'stop': b} # Note lack of parens for funcs
dispatch[get_input()]() # Note trailing parens to call function
• Usethebuilt-infunctiongetattr():
import foo
getattr(foo, 'bar')()
Notethatgetattr()worksonanyobject,includingclasses,classinstances,modules,andsoon.
Thisisusedinseveralplacesinthestandardlibrary,likethis:
class Foo:
def do_foo(self):
...
def do_bar(self):
...
f = getattr(foo_instance, 'do_' + opname)
f()
• Uselocals()toresolvethefunctionname:
def myFunc():
print("hello")
fname = "myFunc"
f = locals()[fname]
f()
2.3.8 Is there an equivalent to Perl’s chomp() for removing trailing newlines from
strings?
You can use S.rstrip("\r\n") to remove all occurrences of any line terminator from the end of the string S
withoutremovingothertrailingwhitespace. IfthestringSrepresentsmorethanoneline,withseveralemptylinesat
theend,thelineterminatorsforalltheblanklineswillberemoved:
>>> lines = ("line 1 \r\n"
... "\r\n"
... "\r\n")
>>> lines.rstrip("\n\r")
'line 1 '
Sincethisistypicallyonlydesiredwhenreadingtextonelineatatime,usingS.rstrip()thiswayworkswell.
2.3.9 Is there a scanf() or sscanf() equivalent?
Notassuch.
Forsimpleinputparsing,theeasiestapproachisusuallytosplitthelineintowhitespace-delimitedwordsusingthe
split() method of string objects and then convert decimal strings to numeric values using int() or float().
split()supportsanoptional“sep”parameterwhichisusefulifthelineusessomethingotherthanwhitespaceasa
separator.
20 Chapter2. ProgrammingFAQ

### 第29页

Formorecomplicatedinputparsing,regularexpressionsaremorepowerfulthanC’ssscanfandbettersuitedfor
thetask.
2.3.10 What does UnicodeDecodeError or UnicodeEncodeError error mean?
Seetheunicode-howto.
2.3.11 Can I end a raw string with an odd number of backslashes?
Arawstringendingwithanoddnumberofbackslasheswillescapethestring’squote:
>>> r'C:\this\will\not\work\'
File "<stdin>", line 1
r'C:\this\will\not\work\'
^
SyntaxError: unterminated string literal (detected at line 1)
Thereareseveralworkaroundsforthis. Oneistouseregularstringsanddoublethebackslashes:
>>> 'C:\\this\\will\\work\\'
'C:\\this\\will\\work\\'
Anotheristoconcatenatearegularstringcontaininganescapedbackslashtotherawstring:
>>> r'C:\this\will\work' '\\'
'C:\\this\\will\\work\\'
Itisalsopossibletouseos.path.join()toappendabackslashonWindows:
>>> os.path.join(r'C:\this\will\work', '')
'C:\\this\\will\\work\\'
Note that while a backslash will “escape” a quote for the purposes of determining where the raw string ends, no
escapingoccurswheninterpretingthevalueoftherawstring. Thatis,thebackslashremainspresentinthevalueof
therawstring:
>>> r'backslash\'preserved'
"backslash\\'preserved"
Alsoseethespecificationinthelanguagereference.
2.4 Performance
2.4.1 My program is too slow. How do I speed it up?
That’satoughone,ingeneral. First,herearealistofthingstorememberbeforedivingfurther:
• PerformancecharacteristicsvaryacrossPythonimplementations. ThisFAQfocusesonCPython.
• Behaviourcanvaryacrossoperatingsystems,especiallywhentalkingaboutI/Oormulti-threading.
• Youshouldalwaysfindthehotspotsinyourprogrambeforeattemptingtooptimizeanycode(seetheprofile
module).
• Writingbenchmarkscriptswillallowyoutoiteratequicklywhensearchingforimprovements(seethetimeit
module).
• It is highly recommended to have good code coverage (through unit testing or any other technique) before
potentiallyintroducingregressionshiddeninsophisticatedoptimizations.
Thatbeingsaid,therearemanytrickstospeedupPythoncode. Herearesomegeneralprincipleswhichgoalong
waytowardsreachingacceptableperformancelevels:
2.4. Performance 21

### 第30页

• Makingyouralgorithmsfaster(orchangingtofasterones)canyieldmuchlargerbenefitsthantryingtosprinkle
micro-optimizationtricksalloveryourcode.
• Usetherightdatastructures. Studydocumentationforthebltin-typesandthecollectionsmodule.
• Whenthestandardlibraryprovidesaprimitivefordoingsomething,itislikely(althoughnotguaranteed)to
befasterthananyalternativeyoumaycomeupwith. ThisisdoublytrueforprimitiveswritteninC,suchas
builtinsandsomeextensiontypes. Forexample,besuretouseeitherthelist.sort()built-inmethodor
therelatedsorted()functiontodosorting(andseethesortinghowtoforexamplesofmoderatelyadvanced
usage).
• Abstractions tend to create indirections and force the interpreter to work more. If the levels of indirection
outweightheamountofusefulworkdone,yourprogramwillbeslower. Youshouldavoidexcessiveabstraction,
especiallyundertheformoftinyfunctionsormethods(whicharealsooftendetrimentaltoreadability).
IfyouhavereachedthelimitofwhatpurePythoncanallow,therearetoolstotakeyoufurtheraway. Forexample,
CythoncancompileaslightlymodifiedversionofPythoncodeintoaCextension,andcanbeusedonmanydifferent
platforms. Cythoncantakeadvantageofcompilation(andoptionaltypeannotations)tomakeyourcodesignificantly
fasterthanwheninterpreted. IfyouareconfidentinyourCprogrammingskills, youcanalsowriteaCextension
moduleyourself.
(cid:181) Seealso
Thewikipagedevotedtoperformancetips.
2.4.2 What is the most efficient way to concatenate many strings together?
strandbytesobjectsareimmutable,thereforeconcatenatingmanystringstogetherisinefficientaseachconcate-
nationcreatesanewobject. Inthegeneralcase,thetotalruntimecostisquadraticinthetotalstringlength.
Toaccumulatemanystrobjects,therecommendedidiomistoplacethemintoalistandcallstr.join()atthe
end:
chunks = []
for s in my_strings:
chunks.append(s)
result = ''.join(chunks)
(anotherreasonablyefficientidiomistouseio.StringIO)
Toaccumulatemanybytesobjects,therecommendedidiomistoextendabytearrayobjectusingin-placecon-
catenation(the+=operator):
result = bytearray()
for b in my_bytes_objects:
result += b
2.5 Sequences (Tuples/Lists)
2.5.1 How do I convert between tuples and lists?
Thetypeconstructortuple(seq)convertsanysequence(actually,anyiterable)intoatuplewiththesameitemsin
thesameorder.
Forexample,tuple([1, 2, 3])yields(1, 2, 3)andtuple('abc')yields('a', 'b', 'c'). Ifthear-
gumentisatuple,itdoesnotmakeacopybutreturnsthesameobject,soitischeaptocalltuple()whenyouaren’t
surethatanobjectisalreadyatuple.
The type constructor list(seq) converts any sequence or iterable into a list with the same items in the same
order. Forexample,list((1, 2, 3))yields[1, 2, 3]andlist('abc')yields['a', 'b', 'c']. Ifthe
argumentisalist,itmakesacopyjustlikeseq[:] would.
22 Chapter2. ProgrammingFAQ

| (cid:181) Seealso |
| --- |
| Thewikipagedevotedtoperformancetips. |

### 第31页

2.5.2 What’s a negative index?
Pythonsequencesareindexedwithpositivenumbersandnegativenumbers. Forpositivenumbers0isthefirstindex
1isthesecondindexandsoforth. Fornegativeindices-1isthelastindexand-2isthepenultimate(nexttolast)
indexandsoforth. Thinkofseq[-n]asthesameasseq[len(seq)-n].
Usingnegativeindicescanbeveryconvenient. ForexampleS[:-1]isallofthestringexceptforitslastcharacter,
whichisusefulforremovingthetrailingnewlinefromastring.
2.5.3 How do I iterate over a sequence in reverse order?
Usethereversed()built-infunction:
for x in reversed(sequence):
... # do something with x ...
Thiswon’ttouchyouroriginalsequence,butbuildanewcopywithreversedordertoiterateover.
2.5.4 How do you remove duplicates from a list?
SeethePythonCookbookforalongdiscussionofmanywaystodothis:
https://code.activestate.com/recipes/52560/
Ifyoudon’tmindreorderingthelist,sortitandthenscanfromtheendofthelist,deletingduplicatesasyougo:
if mylist:
mylist.sort()
last = mylist[-1]
for i in range(len(mylist)-2, -1, -1):
if last == mylist[i]:
del mylist[i]
else:
last = mylist[i]
Ifallelementsofthelistmaybeusedassetkeys(i.e. theyareallhashable)thisisoftenfaster
mylist = list(set(mylist))
Thisconvertsthelistintoaset,therebyremovingduplicates,andthenbackintoalist.
2.5.5 How do you remove multiple items from a list
Aswithremovingduplicates,explicitlyiteratinginreversewithadeleteconditionisonepossibility. However,itis
easierandfastertouseslicereplacementwithanimplicitorexplicitforwarditeration. Herearethreevariations.:
mylist[:] = filter(keep_function, mylist)
mylist[:] = (x for x in mylist if keep_condition)
mylist[:] = [x for x in mylist if keep_condition]
Thelistcomprehensionmaybefastest.
2.5.6 How do you make an array in Python?
Usealist:
["this", 1, "is", "an", "array"]
ListsareequivalenttoCorPascalarraysintheirtimecomplexity; theprimarydifferenceisthataPythonlistcan
containobjectsofmanydifferenttypes.
2.5. Sequences(Tuples/Lists) 23

### 第32页

Thearraymodulealsoprovidesmethodsforcreatingarraysoffixedtypeswithcompactrepresentations,butthey
areslowertoindexthanlists. AlsonotethatNumPyandotherthirdpartypackagesdefinearray-likestructureswith
variouscharacteristicsaswell.
TogetLisp-stylelinkedlists,youcanemulateconscellsusingtuples:
lisp_list = ("like", ("this", ("example", None) ) )
Ifmutabilityisdesired,youcoulduselistsinsteadoftuples. HeretheanalogueofaLispcarislisp_list[0]and
theanalogueofcdrislisp_list[1]. Onlydothisifyou’resureyoureallyneedto,becauseit’susuallyalotslower
thanusingPythonlists.
2.5.7 How do I create a multidimensional list?
Youprobablytriedtomakeamultidimensionalarraylikethis:
>>> A = [[None] * 2] * 3
Thislookscorrectifyouprintit:
>>> A
[[None, None], [None, None], [None, None]]
Butwhenyouassignavalue,itshowsupinmultipleplaces:
>>> A[0][0] = 5
>>> A
[[5, None], [5, None], [5, None]]
Thereasonisthatreplicatingalistwith*doesn’tcreatecopies,itonlycreatesreferencestotheexistingobjects. The
*3 creates a list containing 3 references to the same list of length two. Changes to one row will show in all rows,
whichisalmostcertainlynotwhatyouwant.
Thesuggestedapproachistocreatealistofthedesiredlengthfirstandthenfillineachelementwithanewlycreated
list:
A = [None] * 3
for i in range(3):
A[i] = [None] * 2
Thisgeneratesalistcontaining3differentlistsoflengthtwo. Youcanalsousealistcomprehension:
w, h = 2, 3
A = [[None] * w for i in range(h)]
Or,youcanuseanextensionthatprovidesamatrixdatatype;NumPyisthebestknown.
2.5.8 How do I apply a method or function to a sequence of objects?
Tocallamethodorfunctionandaccumulatethereturnvaluesisalist,alistcomprehensionisanelegantsolution:
result = [obj.method() for obj in mylist]
result = [function(obj) for obj in mylist]
Tojustrunthemethodorfunctionwithoutsavingthereturnvalues,aplainforloopwillsuffice:
for obj in mylist:
obj.method()
(continuesonnextpage)
24 Chapter2. ProgrammingFAQ

### 第33页

(continuedfrompreviouspage)
for obj in mylist:
function(obj)
2.5.9 Whydoesa_tuple[i]+=[‘item’]raiseanexceptionwhentheadditionworks?
Thisisbecauseofacombinationofthefactthataugmentedassignmentoperatorsareassignmentoperators,andthe
differencebetweenmutableandimmutableobjectsinPython.
Thisdiscussionappliesingeneralwhenaugmentedassignmentoperatorsareappliedtoelementsofatuplethatpoint
tomutableobjects,butwe’llusealistand+=asourexemplar.
Ifyouwrote:
>>> a_tuple = (1, 2)
>>> a_tuple[0] += 1
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
The reason for the exception should be immediately clear: 1 is added to the object a_tuple[0] points to (1),
producingtheresultobject,2,butwhenweattempttoassigntheresultofthecomputation,2,toelement0ofthe
tuple,wegetanerrorbecausewecan’tchangewhatanelementofatuplepointsto.
Underthecovers,whatthisaugmentedassignmentstatementisdoingisapproximatelythis:
>>> result = a_tuple[0] + 1
>>> a_tuple[0] = result
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
Itistheassignmentpartoftheoperationthatproducestheerror,sinceatupleisimmutable.
Whenyouwritesomethinglike:
>>> a_tuple = (['foo'], 'bar')
>>> a_tuple[0] += ['item']
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
Theexceptionisabitmoresurprising,andevenmoresurprisingisthefactthateventhoughtherewasanerror,the
appendworked:
>>> a_tuple[0]
['foo', 'item']
To see why this happens, you need to know that (a) if an object implements an __iadd__() magic method, it
getscalledwhenthe+=augmentedassignmentisexecuted,anditsreturnvalueiswhatgetsusedintheassignment
statement;and(b)forlists,__iadd__()isequivalenttocallingextend()onthelistandreturningthelist. That’s
whywesaythatforlists,+=isa“shorthand”forlist.extend():
>>> a_list = []
>>> a_list += [1]
>>> a_list
[1]
Thisisequivalentto:
2.5. Sequences(Tuples/Lists) 25

### 第34页

>>> result = a_list.__iadd__([1])
>>> a_list = result
Theobjectpointedtobya_listhasbeenmutated,andthepointertothemutatedobjectisassignedbacktoa_list.
The end result of the assignment is a no-op, since it is a pointer to the same object that a_list was previously
pointingto,buttheassignmentstillhappens.
Thus,inourtupleexamplewhatishappeningisequivalentto:
>>> result = a_tuple[0].__iadd__(['item'])
>>> a_tuple[0] = result
Traceback (most recent call last):
...
TypeError: 'tuple' object does not support item assignment
The __iadd__() succeeds, and thus the list is extended, but even though result points to the same object that
a_tuple[0]alreadypointsto,thatfinalassignmentstillresultsinanerror,becausetuplesareimmutable.
2.5.10 I want to do a complicated sort: can you do a Schwartzian Transform in
Python?
Thetechnique,attributedtoRandalSchwartzofthePerlcommunity,sortstheelementsofalistbyametricwhich
mapseachelementtoits“sortvalue”. InPython,usethekeyargumentforthelist.sort()method:
Isorted = L[:]
Isorted.sort(key=lambda s: int(s[10:15]))
2.5.11 How can I sort one list by values from another list?
Mergethemintoaniteratoroftuples,sorttheresultinglist,andthenpickouttheelementyouwant.
>>> list1 = ["what", "I'm", "sorting", "by"]
>>> list2 = ["something", "else", "to", "sort"]
>>> pairs = zip(list1, list2)
>>> pairs = sorted(pairs)
>>> pairs
[("I'm", 'else'), ('by', 'sort'), ('sorting', 'to'), ('what', 'something')]
>>> result = [x[1] for x in pairs]
>>> result
['else', 'sort', 'to', 'something']
2.6 Objects
2.6.1 What is a class?
Aclassistheparticularobjecttypecreatedbyexecutingaclassstatement. Classobjectsareusedastemplatesto
createinstanceobjects,whichembodyboththedata(attributes)andcode(methods)specifictoadatatype.
Aclasscanbebasedononeormoreotherclasses,calleditsbaseclass(es). Ittheninheritstheattributesandmeth-
ods of its base classes. This allows an object model to be successively refined by inheritance. You might have a
genericMailboxclassthatprovidesbasicaccessormethodsforamailbox,andsubclassessuchasMboxMailbox,
MaildirMailbox,OutlookMailboxthathandlevariousspecificmailboxformats.
26 Chapter2. ProgrammingFAQ

### 第35页

2.6.2 What is a method?
Amethodisafunctiononsomeobjectxthatyounormallycallasx.name(arguments...). Methodsaredefined
asfunctionsinsidetheclassdefinition:
class C:
def meth(self, arg):
return arg * 2 + self.attribute
2.6.3 What is self?
Selfismerelyaconventionalnameforthefirstargumentofamethod. Amethoddefinedasmeth(self, a, b,
c)shouldbecalledasx.meth(a, b, c)forsomeinstancexoftheclassinwhichthedefinitionoccurs;thecalled
methodwillthinkitiscalledasmeth(x, a, b, c).
SeealsoWhymust‘self’beusedexplicitlyinmethoddefinitionsandcalls?.
2.6.4 How do I check if an object is an instance of a given class or of a subclass
of it?
Use the built-in function isinstance(obj, cls). You can check if an object is an instance of any of a num-
ber of classes by providing a tuple instead of a single class, e.g. isinstance(obj, (class1, class2, ..
.)), and can also check whether an object is one of Python’s built-in types, e.g. isinstance(obj, str) or
isinstance(obj, (int, float, complex)).
Note that isinstance() also checks for virtual inheritance from an abstract base class. So, the test will return
Trueforaregisteredclassevenifhasn’tdirectlyorindirectlyinheritedfromit. Totestfor“trueinheritance”,scan
theMROoftheclass:
from collections.abc import Mapping
class P:
pass
class C(P):
pass
Mapping.register(P)
>>> c = C()
>>> isinstance(c, C) # direct
True
>>> isinstance(c, P) # indirect
True
>>> isinstance(c, Mapping) # virtual
True
# Actual inheritance chain
>>> type(c).__mro__
(<class 'C'>, <class 'P'>, <class 'object'>)
# Test for "true inheritance"
>>> Mapping in type(c).__mro__
False
Notethatmostprogramsdonotuseisinstance()onuser-definedclassesveryoften. Ifyouaredevelopingthe
classesyourself,amoreproperobject-orientedstyleistodefinemethodsontheclassesthatencapsulateaparticular
behaviour,insteadofcheckingtheobject’sclassanddoingadifferentthingbasedonwhatclassitis. Forexample,if
youhaveafunctionthatdoessomething:
2.6. Objects 27

### 第36页

def search(obj):
if isinstance(obj, Mailbox):
... # code to search a mailbox
elif isinstance(obj, Document):
... # code to search a document
elif ...
Abetterapproachistodefineasearch()methodonalltheclassesandjustcallit:
class Mailbox:
def search(self):
... # code to search a mailbox
class Document:
def search(self):
... # code to search a document
obj.search()
2.6.5 What is delegation?
Delegationisanobjectorientedtechnique(alsocalledadesignpattern). Let’ssayyouhaveanobjectxandwantto
changethebehaviourofjustoneofitsmethods. Youcancreateanewclassthatprovidesanewimplementationof
themethodyou’reinterestedinchanginganddelegatesallothermethodstothecorrespondingmethodofx.
Python programmers can easily implement delegation. For example, the following class implements a class that
behaveslikeafilebutconvertsallwrittendatatouppercase:
class UpperOut:
def __init__(self, outfile):
self._outfile = outfile
def write(self, s):
self._outfile.write(s.upper())
def __getattr__(self, name):
return getattr(self._outfile, name)
HeretheUpperOutclassredefinesthewrite()methodtoconverttheargumentstringtouppercasebeforecall-
ingtheunderlyingself._outfile.write()method. Allothermethodsaredelegatedtotheunderlyingself.
_outfileobject. Thedelegationisaccomplishedviathe__getattr__()method;consultthelanguagereference
formoreinformationaboutcontrollingattributeaccess.
Note that for more general cases delegation can get trickier. When attributes must be set as well as retrieved,
the class must define a __setattr__() method too, and it must do so carefully. The basic implementation of
__setattr__()isroughlyequivalenttothefollowing:
class X:
...
def __setattr__(self, name, value):
self.__dict__[name] = value
...
Many__setattr__()implementationscallobject.__setattr__()tosetanattributeonselfwithoutcausing
infiniterecursion:
28 Chapter2. ProgrammingFAQ

### 第37页

class X:
def __setattr__(self, name, value):
# Custom logic here...
object.__setattr__(self, name, value)
Alternatively,itispossibletosetattributesbyinsertingentriesintoself.__dict__directly.
2.6.6 How do I call a method defined in a base class from a derived class that
extends it?
Usethebuilt-insuper()function:
class Derived(Base):
def meth(self):
super().meth() # calls Base.meth
Intheexample,super()willautomaticallydeterminetheinstancefromwhichitwascalled(theselfvalue),look
upthemethodresolutionorder (MRO)withtype(self).__mro__,andreturnthenextinlineafterDerivedin
theMRO:Base.
2.6.7 How can I organize my code to make it easier to change the base class?
Youcouldassignthebaseclasstoanaliasandderivefromthealias. Thenallyouhavetochangeisthevalueassigned
tothealias. Incidentally,thistrickisalsohandyifyouwanttodecidedynamically(e.g. dependingonavailabilityof
resources)whichbaseclasstouse. Example:
class Base:
...
BaseAlias = Base
class Derived(BaseAlias):
...
2.6.8 How do I create static class data and static class methods?
Bothstaticdataandstaticmethods(inthesenseofC++orJava)aresupportedinPython.
Forstaticdata,simplydefineaclassattribute. Toassignanewvaluetotheattribute,youhavetoexplicitlyusethe
classnameintheassignment:
class C:
count = 0 # number of times C.__init__ called
def __init__(self):
C.count = C.count + 1
def getcount(self):
return C.count # or return self.count
c.countalsoreferstoC.countforanycsuchthatisinstance(c, C)holds,unlessoverriddenbycitselforby
someclassonthebase-classsearchpathfromc.__class__backtoC.
Caution: withinamethodofC,anassignmentlikeself.count = 42createsanewandunrelatedinstancenamed
“count” in self’s own dict. Rebinding of a class-static data name must always specify the class whether inside a
methodornot:
C.count = 314
2.6. Objects 29

### 第38页

Staticmethodsarepossible:
class C:
@staticmethod
def static(arg1, arg2, arg3):
# No 'self' parameter!
...
However,afarmorestraightforwardwaytogettheeffectofastaticmethodisviaasimplemodule-levelfunction:
def getcount():
return C.count
Ifyourcodeisstructuredsoastodefineoneclass(ortightlyrelatedclasshierarchy)permodule, thissuppliesthe
desiredencapsulation.
2.6.9 How can I overload constructors (or methods) in Python?
Thisansweractuallyappliestoallmethods,butthequestionusuallycomesupfirstinthecontextofconstructors.
InC++you’dwrite
class C {
C() { cout << "No arguments\n"; }
C(int i) { cout << "Argument is " << i << "\n"; }
}
InPythonyouhavetowriteasingleconstructorthatcatchesallcasesusingdefaultarguments. Forexample:
class C:
def __init__(self, i=None):
if i is None:
print("No arguments")
else:
print("Argument is", i)
Thisisnotentirelyequivalent,butcloseenoughinpractice.
Youcouldalsotryavariable-lengthargumentlist,e.g.
def __init__(self, *args):
...
Thesameapproachworksforallmethoddefinitions.
2.6.10 I try to use __spam and I get an error about _SomeClassName__spam.
Variablenameswithdoubleleadingunderscoresare“mangled”toprovideasimplebuteffectivewaytodefineclass
privatevariables. Anyidentifieroftheform__spam(atleasttwoleadingunderscores,atmostonetrailingunder-
score)istextuallyreplacedwith_classname__spam,whereclassnameisthecurrentclassnamewithanyleading
underscoresstripped.
Theidentifiercanbeusedunchangedwithintheclass,buttoaccessitoutsidetheclass,themanglednamemustbe
used:
class A:
def __one(self):
return 1
def two(self):
return 2 * self.__one()
(continuesonnextpage)
30 Chapter2. ProgrammingFAQ

### 第39页

(continuedfrompreviouspage)
class B(A):
def three(self):
return 3 * self._A__one()
four = 4 * A()._A__one()
Inparticular,thisdoesnotguaranteeprivacysinceanoutsideusercanstilldeliberatelyaccesstheprivateattribute;
manyPythonprogrammersneverbothertouseprivatevariablenamesatall.
(cid:181) Seealso
Theprivatenamemanglingspecificationsfordetailsandspecialcases.
2.6.11 My class defines __del__ but it is not called when I delete the object.
Thereareseveralpossiblereasonsforthis.
Thedelstatementdoesnotnecessarilycall__del__()–itsimplydecrementstheobject’sreferencecount,andif
thisreacheszero__del__()iscalled.
Ifyourdatastructurescontaincircularlinks(e.g. atreewhereeachchildhasaparentreferenceandeachparenthas
alistofchildren)thereferencecountswillnevergobacktozero. OnceinawhilePythonrunsanalgorithmtodetect
suchcycles,butthegarbagecollectormightrunsometimeafterthelastreferencetoyourdatastructurevanishes,so
your__del__()methodmaybecalledataninconvenientandrandomtime. Thisisinconvenientifyou’retrying
toreproduceaproblem. Worse,theorderinwhichobject’s__del__()methodsareexecutedisarbitrary. Youcan
rungc.collect()toforceacollection,buttherearepathologicalcaseswhereobjectswillneverbecollected.
Despitethecyclecollector,it’sstillagoodideatodefineanexplicitclose()methodonobjectstobecalledwhen-
everyou’redonewiththem. Theclose() methodcanthenremoveattributesthatrefertosubobjects. Don’tcall
__del__()directly–__del__()shouldcallclose()andclose()shouldmakesurethatitcanbecalledmore
thanonceforthesameobject.
Anotherwaytoavoidcyclicalreferencesistousetheweakrefmodule,whichallowsyoutopointtoobjectswithout
incrementingtheirreferencecount. Treedatastructures,forinstance,shoulduseweakreferencesfortheirparentand
siblingreferences(iftheyneedthem!).
Finally,ifyour__del__()methodraisesanexception,awarningmessageisprintedtosys.stderr.
2.6.12 How do I get a list of all instances of a given class?
Pythondoesnotkeeptrackofallinstancesofaclass(orofabuilt-intype). Youcanprogramtheclass’sconstructor
tokeeptrackofallinstancesbykeepingalistofweakreferencestoeachinstance.
2.6.13 Why does the result of id() appear to be not unique?
Theid()builtinreturnsanintegerthatisguaranteedtobeuniqueduringthelifetimeoftheobject. SinceinCPython,
thisistheobject’smemoryaddress,ithappensfrequentlythatafteranobjectisdeletedfrommemory,thenextfreshly
createdobjectisallocatedatthesamepositioninmemory. Thisisillustratedbythisexample:
>>> id(1000)
13901272
>>> id(2000)
13901272
Thetwoidsbelongtodifferentintegerobjectsthatarecreatedbefore,anddeletedimmediatelyafterexecutionofthe
id()call. Tobesurethatobjectswhoseidyouwanttoexaminearestillalive,createanotherreferencetotheobject:
2.6. Objects 31

| (cid:181) Seealso |
| --- |
| Theprivatenamemanglingspecificationsfordetailsandspecialcases. |

### 第40页

>>> a = 1000; b = 2000
>>> id(a)
13901272
>>> id(b)
13891296
2.6.14 When can I rely on identity tests with the is operator?
Theisoperatortestsforobjectidentity. Thetesta is bisequivalenttoid(a) == id(b).
Themostimportantpropertyofanidentitytestisthatanobjectisalwaysidenticaltoitself,a is aalwaysreturns
True. Identitytestsareusuallyfasterthanequalitytests. Andunlikeequalitytests,identitytestsareguaranteedto
returnabooleanTrueorFalse.
However,identitytestscanonlybesubstitutedforequalitytestswhenobjectidentityisassured. Generally,thereare
threecircumstanceswhereidentityisguaranteed:
1) Assignments create new names but do not change object identity. After the assignment new = old, it is
guaranteedthatnew is old.
2) Putting an object in a container that stores object references does not change object identity. After the list
assignments[0] = x,itisguaranteedthats[0] is x.
3) Ifanobjectisasingleton,itmeansthatonlyoneinstanceofthatobjectcanexist. Aftertheassignmentsa =
Noneandb = None,itisguaranteedthata is bbecauseNoneisasingleton.
Inmostothercircumstances,identitytestsareinadvisableandequalitytestsarepreferred. Inparticular,identitytests
shouldnotbeusedtocheckconstantssuchasintandstrwhicharen’tguaranteedtobesingletons:
>>> a = 1000
>>> b = 500
>>> c = b + 500
>>> a is c
False
>>> a = 'Python'
>>> b = 'Py'
>>> c = b + 'thon'
>>> a is c
False
Likewise,newinstancesofmutablecontainersareneveridentical:
>>> a = []
>>> b = []
>>> a is b
False
Inthestandardlibrarycode,youwillseeseveralcommonpatternsforcorrectlyusingidentitytests:
1) As recommended by PEP 8, an identity test is the preferred way to check for None. This reads like plain
Englishincodeandavoidsconfusionwithotherobjectsthatmayhavebooleanvaluesthatevaluatetofalse.
2) Detecting optional arguments can be tricky when None is a valid input value. In those situations, you can
create a singleton sentinel object guaranteed to be distinct from other objects. For example, here is how to
implementamethodthatbehaveslikedict.pop():
_sentinel = object()
def pop(self, key, default=_sentinel):
if key in self:
(continuesonnextpage)
32 Chapter2. ProgrammingFAQ

### 第41页

(continuedfrompreviouspage)
value = self[key]
del self[key]
return value
if default is _sentinel:
raise KeyError(key)
return default
3) Container implementations sometimes need to augment equality tests with identity tests. This prevents the
codefrombeingconfusedbyobjectssuchasfloat('NaN')thatarenotequaltothemselves.
Forexample,hereistheimplementationofcollections.abc.Sequence.__contains__():
def __contains__(self, value):
for v in self:
if v is value or v == value:
return True
return False
2.6.15 Howcanasubclasscontrolwhatdataisstoredinanimmutableinstance?
Whensubclassinganimmutabletype,overridethe__new__()methodinsteadofthe__init__()method. The
latteronlyrunsafteraninstanceiscreated,whichistoolatetoalterdatainanimmutableinstance.
Alloftheseimmutableclasseshaveadifferentsignaturethantheirparentclass:
from datetime import date
class FirstOfMonthDate(date):
"Always choose the first day of the month"
def __new__(cls, year, month, day):
return super().__new__(cls, year, month, 1)
class NamedInt(int):
"Allow text names for some numbers"
xlat = {'zero': 0, 'one': 1, 'ten': 10}
def __new__(cls, value):
value = cls.xlat.get(value, value)
return super().__new__(cls, value)
class TitleStr(str):
"Convert str to name suitable for a URL path"
def __new__(cls, s):
s = s.lower().replace(' ', '-')
s = ''.join([c for c in s if c.isalnum() or c == '-'])
return super().__new__(cls, s)
Theclassescanbeusedlikethis:
>>> FirstOfMonthDate(2012, 2, 14)
FirstOfMonthDate(2012, 2, 1)
>>> NamedInt('ten')
10
>>> NamedInt(20)
20
>>> TitleStr('Blog: Why Python Rocks')
'blog-why-python-rocks'
2.6. Objects 33

### 第42页

2.6.16 How do I cache method calls?
The two principal tools for caching methods are functools.cached_property() and functools.
lru_cache(). Theformerstoresresultsattheinstancelevelandthelatterattheclasslevel.
Thecached_propertyapproachonlyworkswithmethodsthatdonottakeanyarguments. Itdoesnotcreateareference
totheinstance. Thecachedmethodresultwillbekeptonlyaslongastheinstanceisalive.
Theadvantageisthatwhenaninstanceisnolongerused,thecachedmethodresultwillbereleasedrightaway. The
disadvantage is that if instances accumulate, so too will the accumulated method results. They can grow without
bound.
The lru_cache approach works with methods that have hashable arguments. It creates a reference to the instance
unlessspecialeffortsaremadetopassinweakreferences.
Theadvantageoftheleastrecentlyusedalgorithmisthatthecacheisboundedbythespecifiedmaxsize. Thedisad-
vantageisthatinstancesarekeptaliveuntiltheyageoutofthecacheoruntilthecacheiscleared.
Thisexampleshowsthevarioustechniques:
class Weather:
"Lookup weather information on a government website"
def __init__(self, station_id):
self._station_id = station_id
# The _station_id is private and immutable
def current_temperature(self):
"Latest hourly observation"
# Do not cache this because old results
# can be out of date.
@cached_property
def location(self):
"Return the longitude/latitude coordinates of the station"
# Result only depends on the station_id
@lru_cache(maxsize=20)
def historic_rainfall(self, date, units='mm'):
"Rainfall on a given date"
# Depends on the station_id, date, and units.
The above example assumes that the station_id never changes. If the relevant instance attributes are mutable, the
cached_propertyapproachcan’tbemadetoworkbecauseitcannotdetectchangestotheattributes.
Tomakethelru_cacheapproachworkwhenthestation_id ismutable,theclassneedstodefinethe__eq__()and
__hash__()methodssothatthecachecandetectrelevantattributeupdates:
class Weather:
"Example with a mutable station identifier"
def __init__(self, station_id):
self.station_id = station_id
def change_station(self, station_id):
self.station_id = station_id
def __eq__(self, other):
return self.station_id == other.station_id
def __hash__(self):
(continuesonnextpage)
34 Chapter2. ProgrammingFAQ

### 第43页

(continuedfrompreviouspage)
return hash(self.station_id)
@lru_cache(maxsize=20)
def historic_rainfall(self, date, units='cm'):
'Rainfall on a given date'
# Depends on the station_id, date, and units.
2.7 Modules
2.7.1 How do I create a .pyc file?
Whenamoduleisimportedforthefirsttime(orwhenthesourcefilehaschangedsincethecurrentcompiledfilewas
created)a.pycfilecontainingthecompiledcodeshouldbecreatedina__pycache__subdirectoryofthedirectory
containingthe.pyfile. The.pycfilewillhaveafilenamethatstartswiththesamenameasthe.pyfile,andends
with.pyc,withamiddlecomponentthatdependsontheparticularpythonbinarythatcreatedit. (SeePEP3147
fordetails.)
Onereasonthata .pycfilemaynotbecreatedisapermissionsproblemwiththedirectorycontainingthesource
file,meaningthatthe__pycache__subdirectorycannotbecreated. Thiscanhappen,forexample,ifyoudevelop
asoneuserbutrunasanother,suchasifyouaretestingwithawebserver.
UnlessthePYTHONDONTWRITEBYTECODEenvironmentvariableisset,creationofa.pycfileisautomaticifyou’re
importingamoduleandPythonhastheability(permissions,freespace,etc…)tocreatea__pycache__subdirectory
andwritethecompiledmoduletothatsubdirectory.
RunningPythononatoplevelscriptisnotconsideredanimportandno.pycwillbecreated. Forexample,ifyou
haveatop-levelmodulefoo.pythatimportsanothermodulexyz.py,whenyourunfoo(bytypingpython foo.
pyasashellcommand),a.pycwillbecreatedforxyzbecausexyzisimported,butno.pycfilewillbecreated
forfoosincefoo.pyisn’tbeingimported.
Ifyouneedtocreatea.pycfileforfoo–thatis,tocreatea.pycfileforamodulethatisnotimported–youcan,
usingthepy_compileandcompileallmodules.
Thepy_compile modulecanmanuallycompileanymodule. Onewayisto use thecompile() functioninthat
moduleinteractively:
>>> import py_compile
>>> py_compile.compile('foo.py')
Thiswillwritethe.pyctoa__pycache__subdirectoryinthesamelocationasfoo.py(oryoucanoverridethat
withtheoptionalparametercfile).
Youcanalsoautomaticallycompileallfilesinadirectoryordirectoriesusingthecompileallmodule. Youcando
itfromtheshellpromptbyrunningcompileall.pyandprovidingthepathofadirectorycontainingPythonfiles
tocompile:
python -m compileall .
2.7.2 How do I find the current module name?
Amodulecanfindoutitsownmodulenamebylookingatthepredefinedglobalvariable__name__. Ifthishasthe
value'__main__',theprogramisrunningasascript. Manymodulesthatareusuallyusedbyimportingthemalso
provideacommand-lineinterfaceoraself-test,andonlyexecutethiscodeafterchecking__name__:
def main():
print('Running test...')
...
(continuesonnextpage)
2.7. Modules 35

### 第44页

(continuedfrompreviouspage)
if __name__ == '__main__':
main()
2.7.3 How can I have modules that mutually import each other?
Supposeyouhavethefollowingmodules:
foo.py:
from bar import bar_var
foo_var = 1
bar.py:
from foo import foo_var
bar_var = 2
Theproblemisthattheinterpreterwillperformthefollowingsteps:
• mainimportsfoo
• Emptyglobalsforfooarecreated
• fooiscompiledandstartsexecuting
• fooimportsbar
• Emptyglobalsforbararecreated
• bariscompiledandstartsexecuting
• barimportsfoo(whichisano-opsincetherealreadyisamodulenamedfoo)
• Theimportmechanismtriestoreadfoo_varfromfooglobals,tosetbar.foo_var = foo.foo_var
Thelaststepfails,becausePythonisn’tdonewithinterpretingfooyetandtheglobalsymboldictionaryforfoois
stillempty.
Thesamethinghappenswhenyouuseimport foo,andthentrytoaccessfoo.foo_varinglobalcode.
Thereare(atleast)threepossibleworkaroundsforthisproblem.
GuidovanRossumrecommends avoidingalluses of from <module> import ..., andplacingall codeinside
functions. Initializationsofglobalvariablesandclassvariablesshoulduseconstantsorbuilt-infunctionsonly. This
meanseverythingfromanimportedmoduleisreferencedas<module>.<name>.
JimRoskindsuggestsperformingstepsinthefollowingorderineachmodule:
• exports(globals,functions,andclassesthatdon’tneedimportedbaseclasses)
• importstatements
• activecode(includingglobalsthatareinitializedfromimportedvalues).
VanRossumdoesn’tlikethisapproachmuchbecausetheimportsappearinastrangeplace,butitdoeswork.
MatthiasUrlichsrecommendsrestructuringyourcodesothattherecursiveimportisnotnecessaryinthefirstplace.
Thesesolutionsarenotmutuallyexclusive.
2.7.4 __import__(‘x.y.z’) returns <module ‘x’>; how do I get z?
Considerusingtheconveniencefunctionimport_module()fromimportlibinstead:
z = importlib.import_module('x.y.z')
36 Chapter2. ProgrammingFAQ

### 第45页

2.7.5 When I edit an imported module and reimport it, the changes don’t show
up. Why does this happen?
For reasons of efficiency as well as consistency, Python only reads the module file on the first time a module is
imported. Ifitdidn’t,inaprogramconsistingofmanymoduleswhereeachoneimportsthesamebasicmodule,the
basicmodulewouldbeparsedandre-parsedmanytimes. Toforcere-readingofachangedmodule,dothis:
import importlib
import modname
importlib.reload(modname)
Warning: thistechniqueisnot100%fool-proof. Inparticular,modulescontainingstatementslike
from modname import some_objects
willcontinuetoworkwiththeoldversionoftheimportedobjects. Ifthemodulecontainsclassdefinitions,existing
class instances will not be updated to use the new class definition. This can result in the following paradoxical
behaviour:
>>> import importlib
>>> import cls
>>> c = cls.C() # Create an instance of C
>>> importlib.reload(cls)
<module 'cls' from 'cls.py'>
>>> isinstance(c, cls.C) # isinstance is false?!?
False
Thenatureoftheproblemismadeclearifyouprintoutthe“identity”oftheclassobjects:
>>> hex(id(c.__class__))
'0x7352a0'
>>> hex(id(cls.C))
'0x4198d0'
2.7. Modules 37

### 第46页

38 Chapter2. ProgrammingFAQ

### 第47页

CHAPTER
THREE
DESIGN AND HISTORY FAQ
3.1 Why does Python use indentation for grouping of statements?
GuidovanRossumbelievesthatusingindentationforgroupingisextremelyelegantandcontributesalottotheclarity
oftheaveragePythonprogram. Mostpeoplelearntolovethisfeatureafterawhile.
Sincetherearenobegin/endbracketstherecannotbeadisagreementbetweengroupingperceivedbytheparserand
thehumanreader. OccasionallyCprogrammerswillencounterafragmentofcodelikethis:
if (x <= y)
x++;
y--;
z++;
Onlythex++statementisexecutediftheconditionistrue,buttheindentationleadsmanytobelieveotherwise. Even
experiencedCprogrammerswillsometimesstareatitalongtimewonderingastowhyyisbeingdecrementedeven
forx > y.
Becausetherearenobegin/endbrackets,Pythonismuchlesspronetocoding-styleconflicts. InCtherearemany
different ways to place the braces. After becoming used to reading and writing code using a particular style, it is
normaltofeelsomewhatuneasywhenreading(orbeingrequiredtowrite)inadifferentone.
Manycodingstylesplacebegin/endbracketsonalinebythemselves. Thismakesprogramsconsiderablylongerand
wastesvaluablescreenspace,makingithardertogetagoodoverviewofaprogram. Ideally,afunctionshouldfiton
onescreen(say,20–30lines). 20linesofPythoncandoalotmoreworkthan20linesofC.Thisisnotsolelydueto
thelackofbegin/endbrackets–thelackofdeclarationsandthehigh-leveldatatypesarealsoresponsible–butthe
indentation-basedsyntaxcertainlyhelps.
3.2 Why am I getting strange results with simple arithmetic opera-
tions?
Seethenextquestion.
3.3 Why are floating-point calculations so inaccurate?
Usersareoftensurprisedbyresultslikethis:
>>> 1.2 - 1.0
0.19999999999999996
and think it is a bug in Python. It’s not. This has little to do with Python, and much more to do with how the
underlyingplatformhandlesfloating-pointnumbers.
ThefloattypeinCPythonusesaCdoubleforstorage. Afloatobject’svalueisstoredinbinaryfloating-point
with a fixed precision (typically 53 bits) and Python uses C operations, which in turn rely on the hardware imple-
39

### 第48页

mentationintheprocessor,toperformfloating-pointoperations. Thismeansthatasfarasfloating-pointoperations
areconcerned,PythonbehaveslikemanypopularlanguagesincludingCandJava.
Many numbers that can be written easily in decimal notation cannot be expressed exactly in binary floating point.
Forexample,after:
>>> x = 1.2
thevaluestoredforxisa(verygood)approximationtothedecimalvalue1.2,butisnotexactlyequaltoit. Ona
typicalmachine,theactualstoredvalueis:
1.0011001100110011001100110011001100110011001100110011 (binary)
whichisexactly:
1.1999999999999999555910790149937383830547332763671875 (decimal)
Thetypicalprecisionof53bitsprovidesPythonfloatswith15–16decimaldigitsofaccuracy.
Forafullerexplanation,pleaseseethefloating-pointarithmeticchapterinthePythontutorial.
3.4 Why are Python strings immutable?
Thereareseveraladvantages.
Oneisperformance: knowingthatastringisimmutablemeanswecanallocatespaceforitatcreationtime,andthe
storagerequirementsarefixedandunchanging. Thisisalsooneofthereasonsforthedistinctionbetweentuplesand
lists.
Another advantage is that strings in Python are considered as “elemental” as numbers. No amount of activity will
changethevalue8toanythingelse,andinPython,noamountofactivitywillchangethestring“eight”toanything
else.
3.5 Why must ‘self’ be used explicitly in method definitions and
calls?
TheideawasborrowedfromModula-3. Itturnsouttobeveryuseful,foravarietyofreasons.
First,it’smoreobviousthatyouareusingamethodorinstanceattributeinsteadofalocalvariable. Readingself.x
orself.meth()makesitabsolutelyclearthataninstancevariableormethodisusedevenifyoudon’tknowthe
classdefinitionbyheart. InC++, youcansortoftellbythelackofalocalvariabledeclaration(assumingglobals
arerareoreasilyrecognizable)–butinPython,therearenolocalvariabledeclarations,soyou’dhavetolookupthe
classdefinitiontobesure. SomeC++andJavacodingstandardscallforinstanceattributestohaveanm_prefix,so
thisexplicitnessisstillusefulinthoselanguages,too.
Second, it means that no special syntax is necessary if you want to explicitly reference or call the method from a
particularclass. InC++,ifyouwanttouseamethodfromabaseclasswhichisoverriddeninaderivedclass,you
havetousethe:: operator–inPythonyoucanwritebaseclass.methodname(self, <argument list>).
Thisisparticularlyusefulfor__init__()methods,andingeneralincaseswhereaderivedclassmethodwantsto
extendthebaseclassmethodofthesamenameandthushastocallthebaseclassmethodsomehow.
Finally,forinstancevariablesitsolvesasyntacticproblemwithassignment: sincelocalvariablesinPythonare(by
definition!) thosevariablestowhichavalueisassignedinafunctionbody(andthataren’texplicitlydeclaredglobal),
therehastobesomewaytotelltheinterpreterthatanassignmentwasmeanttoassigntoaninstancevariableinstead
oftoalocalvariable,anditshouldpreferablybesyntactic(forefficiencyreasons). C++doesthisthroughdeclarations,
butPythondoesn’thavedeclarationsanditwouldbeapityhavingtointroducethemjustforthispurpose. Usingthe
explicitself.varsolvesthisnicely. Similarly,forusinginstancevariables,havingtowriteself.varmeansthat
referencestounqualifiednamesinsideamethoddon’thavetosearchtheinstance’sdirectories. Toputitanotherway,
localvariablesandinstancevariablesliveintwodifferentnamespaces,andyouneedtotellPythonwhichnamespace
touse.
40 Chapter3. DesignandHistoryFAQ

### 第49页

3.6 Why can’t I use an assignment in an expression?
StartinginPython3.8,youcan!
Assignmentexpressionsusingthewalrusoperator:=assignavariableinanexpression:
while chunk := fp.read(200):
print(chunk)
SeePEP572formoreinformation.
3.7 Why does Python use methods for some functionality (e.g.
list.index()) but functions for other (e.g. len(list))?
AsGuidosaid:
(a) For some operations, prefix notation just reads better than postfix – prefix (and infix!) operations
have a long tradition in mathematics which likes notations where the visuals help the mathematician
thinkingaboutaproblem. Comparetheeasywithwhichwerewriteaformulalikex*(a+b)intox*a+
x*btotheclumsinessofdoingthesamethingusingarawOOnotation.
(b) When I read code that says len(x) I know that it is asking for the length of something. This tells
me two things: the result is an integer, and the argument is some kind of container. To the contrary,
whenIreadx.len(),Ihavetoalreadyknowthatxissomekindofcontainerimplementinganinterface
orinheritingfromaclassthathasastandardlen(). Witnesstheconfusionweoccasionallyhavewhena
classthatisnotimplementingamappinghasaget()orkeys()method,orsomethingthatisn’tafilehas
awrite()method.
—https://mail.python.org/pipermail/python-3000/2006-November/004643.html
3.8 Why is join() a string method instead of a list or tuple method?
StringsbecamemuchmorelikeotherstandardtypesstartinginPython1.6,whenmethodswereaddedwhichgive
thesamefunctionalitythathasalwaysbeenavailable usingthefunctionsofthestringmodule. Mostofthesenew
methodshavebeenwidelyaccepted,buttheonewhichappearstomakesomeprogrammersfeeluncomfortableis:
", ".join(['1', '2', '4', '8', '16'])
whichgivestheresult:
"1, 2, 4, 8, 16"
Therearetwocommonargumentsagainstthisusage.
Thefirstrunsalongthelinesof: “Itlooksreallyuglyusingamethodofastringliteral(stringconstant)”,towhichthe
answeristhatitmight,butastringliteralisjustafixedvalue. Ifthemethodsaretobeallowedonnamesboundto
stringsthereisnologicalreasontomakethemunavailableonliterals.
Thesecondobjectionistypicallycastas: “Iamreallytellingasequencetojoinitsmemberstogetherwithastring
constant”. Sadly,youaren’t. Forsomereasonthereseemstobemuchlessdifficultywithhavingsplit()asastring
method,sinceinthatcaseitiseasytoseethat
"1, 2, 4, 8, 16".split(", ")
isaninstructiontoastringliteraltoreturnthesubstringsdelimitedbythegivenseparator(or,bydefault,arbitrary
runsofwhitespace).
join()isastringmethodbecauseinusingityouaretellingtheseparatorstringtoiterateoverasequenceofstrings
andinsertitselfbetweenadjacentelements. Thismethodcanbeusedwithanyargumentwhichobeystherulesfor
sequenceobjects,includinganynewclassesyoumightdefineyourself. Similarmethodsexistforbytesandbytearray
objects.
3.6. Whycan’tIuseanassignmentinanexpression? 41

### 第50页

3.9 How fast are exceptions?
Atry/exceptblockisextremelyefficientifnoexceptionsareraised. Actuallycatchinganexceptionisexpensive.
InversionsofPythonpriorto2.0itwascommontousethisidiom:
try:
value = mydict[key]
except KeyError:
mydict[key] = getvalue(key)
value = mydict[key]
This only made sense when you expected the dict to have the key almost all the time. If that wasn’t the case, you
codeditlikethis:
if key in mydict:
value = mydict[key]
else:
value = mydict[key] = getvalue(key)
Forthisspecificcase,youcouldalsousevalue = dict.setdefault(key, getvalue(key)),butonlyifthe
getvalue()callischeapenoughbecauseitisevaluatedinallcases.
3.10 Why isn’t there a switch or case statement in Python?
Ingeneral,structuredswitchstatementsexecuteoneblockofcodewhenanexpressionhasaparticularvalueorsetof
values. SincePython3.10onecaneasilymatchliteralvalues,orconstantswithinanamespace,withamatch ...
casestatement. Anolderalternativeisasequenceofif... elif... elif... else.
Forcaseswhereyouneedtochoosefromaverylargenumberofpossibilities,youcancreateadictionarymapping
casevaluestofunctionstocall. Forexample:
functions = {'a': function_1,
'b': function_2,
'c': self.method_1}
func = functions[value]
func()
Forcallingmethodsonobjects, youcansimplifyyetfurtherbyusingthegetattr()built-intoretrievemethods
withaparticularname:
class MyVisitor:
def visit_a(self):
...
def dispatch(self, value):
method_name = 'visit_' + str(value)
method = getattr(self, method_name)
method()
It’ssuggestedthatyouuseaprefixforthemethodnames,suchasvisit_inthisexample. Withoutsuchaprefix,if
valuesarecomingfromanuntrustedsource,anattackerwouldbeabletocallanymethodonyourobject.
Imitatingswitchwithfallthrough,aswithC’sswitch-case-default,ispossible,muchharder,andlessneeded.
42 Chapter3. DesignandHistoryFAQ

### 第51页

3.11 Can’t you emulate threads in the interpreter instead of relying
on an OS-specific thread implementation?
Answer 1: Unfortunately, the interpreter pushes at least one C stack frame for each Python stack frame. Also,
extensions can call back into Python at almost random moments. Therefore, a complete threads implementation
requiresthreadsupportforC.
Answer2: Fortunately,thereisStacklessPython,whichhasacompletelyredesignedinterpreterloopthatavoidsthe
Cstack.
3.12 Why can’t lambda expressions contain statements?
PythonlambdaexpressionscannotcontainstatementsbecausePython’ssyntacticframeworkcan’thandlestatements
nestedinsideexpressions. However,inPython,thisisnotaseriousproblem. Unlikelambdaformsinotherlanguages,
wheretheyaddfunctionality,Pythonlambdasareonlyashorthandnotationifyou’retoolazytodefineafunction.
FunctionsarealreadyfirstclassobjectsinPython,andcanbedeclaredinalocalscope. Thereforetheonlyadvantage
of using a lambda instead of a locally defined function is that you don’t need to invent a name for the function –
butthat’sjustalocalvariabletowhichthefunctionobject(whichisexactlythesametypeofobjectthatalambda
expressionyields)isassigned!
3.13 Can Python be compiled to machine code, C or some other
language?
Cython compiles a modified version of Python with optional annotations into C extensions. Nuitka is an up-and-
comingcompilerofPythonintoC++code,aimingtosupportthefullPythonlanguage.
3.14 How does Python manage memory?
ThedetailsofPythonmemorymanagementdependontheimplementation. ThestandardimplementationofPython,
CPython,usesreferencecountingtodetectinaccessibleobjects,andanothermechanismtocollectreferencecycles,
periodicallyexecutingacycledetectionalgorithmwhichlooksforinaccessiblecyclesanddeletestheobjectsinvolved.
Thegcmoduleprovidesfunctionstoperformagarbagecollection,obtaindebuggingstatistics,andtunethecollector’s
parameters.
Otherimplementations(suchasJythonorPyPy),however,canrelyonadifferentmechanismsuchasafull-blown
garbage collector. This difference can cause some subtle porting problems if your Python code depends on the
behaviorofthereferencecountingimplementation.
InsomePythonimplementations,thefollowingcode(whichisfineinCPython)willprobablyrunoutoffiledescrip-
tors:
for file in very_long_list_of_files:
f = open(file)
c = f.read(1)
Indeed,usingCPython’sreferencecountinganddestructorscheme,eachnewassignmenttofclosesthepreviousfile.
WithatraditionalGC,however, thosefileobjectswillonlygetcollected(andclosed)atvaryingandpossiblylong
intervals.
IfyouwanttowritecodethatwillworkwithanyPythonimplementation,youshouldexplicitlyclosethefileoruse
thewithstatement;thiswillworkregardlessofmemorymanagementscheme:
for file in very_long_list_of_files:
with open(file) as f:
c = f.read(1)
3.11. Can’tyouemulatethreadsintheinterpreterinsteadofrelyingonanOS-specificthread 43

### 第52页

3.15 Why doesn’t CPython use a more traditional garbage collec-
tion scheme?
Foronething,thisisnotaCstandardfeatureandhenceit’snotportable. (Yes,weknowabouttheBoehmGClibrary.
Ithasbitsofassemblercodeformost commonplatforms,notforallofthem,andalthoughitismostlytransparent,
itisn’tcompletelytransparent;patchesarerequiredtogetPythontoworkwithit.)
Traditional GC also becomes a problem when Python is embedded into other applications. While in a standalone
Pythonit’sfinetoreplacethestandardmalloc()andfree()withversionsprovidedbytheGClibrary,anapplica-
tionembeddingPythonmaywanttohaveitsownsubstituteformalloc()andfree(),andmaynotwantPython’s.
Rightnow,CPythonworkswithanythingthatimplementsmalloc()andfree()properly.
3.16 Why isn’t all memory freed when CPython exits?
Objects referenced from the global namespaces of Python modules are not always deallocated when Python exits.
Thismayhappeniftherearecircularreferences. TherearealsocertainbitsofmemorythatareallocatedbytheC
librarythatareimpossibletofree(e.g. atoollikePurifywillcomplainaboutthese). Pythonis,however,aggressive
aboutcleaningupmemoryonexitanddoestrytodestroyeverysingleobject.
IfyouwanttoforcePythontodeletecertainthingsondeallocationusetheatexitmoduletorunafunctionthat
willforcethosedeletions.
3.17 Why are there separate tuple and list data types?
Listsandtuples,whilesimilarinmanyrespects,aregenerallyusedinfundamentallydifferentways. Tuplescanbe
thoughtofasbeingsimilartoPascalrecordsorCstructs;they’resmallcollectionsofrelateddatawhichmaybe
ofdifferenttypeswhichareoperatedonasagroup. Forexample,aCartesiancoordinateisappropriatelyrepresented
asatupleoftwoorthreenumbers.
Lists,ontheotherhand,aremorelikearraysinotherlanguages. Theytendtoholdavaryingnumberofobjectsall
ofwhichhavethesametypeandwhichareoperatedonone-by-one. Forexample,os.listdir('.')returnsalist
ofstringsrepresentingthefilesinthecurrentdirectory. Functionswhichoperateonthisoutputwouldgenerallynot
breakifyouaddedanotherfileortwotothedirectory.
Tuplesareimmutable,meaningthatonceatuplehasbeencreated,youcan’treplaceanyofitselementswithanew
value. Listsaremutable,meaningthatyoucanalwayschangealist’selements. Onlyimmutableelementscanbeused
asdictionarykeys,andhenceonlytuplesandnotlistscanbeusedaskeys.
3.18 How are lists implemented in CPython?
CPython’s lists are really variable-length arrays, not Lisp-style linked lists. The implementation uses a contiguous
arrayofreferencestootherobjects,andkeepsapointertothisarrayandthearray’slengthinalistheadstructure.
This makes indexing a list a[i] an operation whose cost is independent of the size of the list or the value of the
index.
Whenitemsareappendedorinserted,thearrayofreferencesisresized. Someclevernessisappliedtoimprovethe
performanceofappendingitemsrepeatedly;whenthearraymustbegrown,someextraspaceisallocatedsothenext
fewtimesdon’trequireanactualresize.
3.19 How are dictionaries implemented in CPython?
CPython’sdictionariesareimplementedasresizablehashtables. ComparedtoB-trees,thisgivesbetterperformance
forlookup(themostcommonoperationbyfar)undermostcircumstances,andtheimplementationissimpler.
Dictionariesworkbycomputingahashcodeforeachkeystoredinthedictionaryusingthehash()built-infunction.
The hash code varies widely depending on the key and a per-process seed; for example, 'Python' could hash to
-539294296while'python', astringthatdiffersbyasinglebit, couldhashto1142331976. Thehashcodeis
44 Chapter3. DesignandHistoryFAQ

### 第53页

then used to calculate a location in an internal array where the value will be stored. Assuming that you’re storing
keysthatallhavedifferenthashvalues,thismeansthatdictionariestakeconstanttime–O(1),inBig-Onotation–to
retrieveakey.
3.20 Why must dictionary keys be immutable?
Thehashtableimplementationofdictionariesusesahashvaluecalculatedfromthekeyvaluetofindthekey. Ifthe
keywereamutableobject,itsvaluecouldchange,andthusitshashcouldalsochange. Butsincewhoeverchanges
thekeyobjectcan’ttellthatitwasbeingusedasadictionarykey,itcan’tmovetheentryaroundinthedictionary.
Then,whenyoutrytolookupthesameobjectinthedictionaryitwon’tbefoundbecauseitshashvalueisdifferent.
Ifyoutriedtolookuptheoldvalueitwouldn’tbefoundeither,becausethevalueoftheobjectfoundinthathashbin
wouldbedifferent.
Ifyouwantadictionaryindexedwithalist,simplyconvertthelisttoatuplefirst;thefunctiontuple(L)createsa
tuplewiththesameentriesasthelistL.Tuplesareimmutableandcanthereforebeusedasdictionarykeys.
Someunacceptablesolutionsthathavebeenproposed:
• Hash lists by their address (object ID). This doesn’t work because if you construct a new list with the same
valueitwon’tbefound;e.g.:
mydict = {[1, 2]: '12'}
print(mydict[[1, 2]])
wouldraiseaKeyErrorexceptionbecausetheidofthe[1, 2]usedinthesecondlinediffersfromthatin
thefirstline. Inotherwords,dictionarykeysshouldbecomparedusing==,notusingis.
• Make a copy when using a list as a key. This doesn’t work because the list, being a mutable object, could
containareferencetoitself,andthenthecopyingcodewouldrunintoaninfiniteloop.
• Allowlistsaskeysbuttelltheusernottomodifythem. Thiswouldallowaclassofhard-to-trackbugsinpro-
gramswhenyouforgotormodifiedalistbyaccident. Italsoinvalidatesanimportantinvariantofdictionaries:
everyvalueind.keys()isusableasakeyofthedictionary.
• Marklistsasread-onlyoncetheyareusedasadictionarykey. Theproblemisthatit’snotjustthetop-level
objectthatcouldchangeitsvalue;youcoulduseatuplecontainingalistasakey. Enteringanythingasakeyinto
adictionarywouldrequiremarkingallobjectsreachablefromthereasread-only–andagain,self-referential
objectscouldcauseaninfiniteloop.
Thereisatricktogetaroundthisifyouneedto,butuseitatyourownrisk: Youcanwrapamutablestructureinside
aclassinstancewhichhasbotha__eq__()anda__hash__()method. Youmustthenmakesurethatthehash
valueforallsuchwrapperobjectsthatresideinadictionary(orotherhashbasedstructure),remainfixedwhilethe
objectisinthedictionary(orotherstructure).
class ListWrapper:
def __init__(self, the_list):
self.the_list = the_list
def __eq__(self, other):
return self.the_list == other.the_list
def __hash__(self):
l = self.the_list
result = 98767 - len(l)*555
for i, el in enumerate(l):
try:
result = result + (hash(el) % 9999999) * 1001 + i
except Exception:
result = (result % 7777777) + i * 333
return result
3.20. Whymustdictionarykeysbeimmutable? 45

### 第54页

Notethatthehashcomputationiscomplicatedbythepossibilitythatsomemembersofthelistmaybeunhashable
andalsobythepossibilityofarithmeticoverflow.
Furthermore it must always be the case that if o1 == o2 (ie o1.__eq__(o2) is True) then hash(o1) ==
hash(o2)(ie,o1.__hash__() == o2.__hash__()),regardlessofwhethertheobjectisinadictionaryornot.
Ifyoufailtomeettheserestrictionsdictionariesandotherhashbasedstructureswillmisbehave.
InthecaseofListWrapper, wheneverthewrapperobjectisinadictionarythewrappedlistmustnotchangeto
avoidanomalies. Don’tdothisunlessyouarepreparedtothinkhardabouttherequirementsandtheconsequences
ofnotmeetingthemcorrectly. Consideryourselfwarned.
3.21 Why doesn’t list.sort() return the sorted list?
Insituationswhereperformancematters,makingacopyofthelistjusttosortitwouldbewasteful. Therefore,list.
sort()sortsthelistinplace. Inordertoremindyouofthatfact,itdoesnotreturnthesortedlist. Thisway,you
won’tbefooledintoaccidentallyoverwritingalistwhenyouneedasortedcopybutalsoneedtokeeptheunsorted
versionaround.
Ifyouwanttoreturnanewlist,usethebuilt-insorted()functioninstead. Thisfunctioncreatesanewlistfrom
aprovidediterable,sortsitandreturnsit. Forexample,here’showtoiterateoverthekeysofadictionaryinsorted
order:
for key in sorted(mydict):
... # do whatever with mydict[key]...
3.22 How do you specify and enforce an interface spec in Python?
AninterfacespecificationforamoduleasprovidedbylanguagessuchasC++andJavadescribestheprototypesfor
themethodsandfunctionsofthemodule. Manyfeelthatcompile-timeenforcementofinterfacespecificationshelps
intheconstructionoflargeprograms.
Python2.6addsanabcmodulethatletsyoudefineAbstractBaseClasses(ABCs). Youcanthenuseisinstance()
andissubclass()tocheckwhetheraninstanceoraclassimplementsaparticularABC.Thecollections.abc
moduledefinesasetofusefulABCssuchasIterable,Container,andMutableMapping.
ForPython,manyoftheadvantagesofinterfacespecificationscanbeobtainedbyanappropriatetestdisciplinefor
components.
Agoodtestsuiteforamodulecanbothprovidearegressiontestandserveasamoduleinterfacespecificationanda
setofexamples. ManyPythonmodulescanberunasascripttoprovideasimple“selftest.” Evenmoduleswhichuse
complexexternalinterfacescanoftenbetestedinisolationusingtrivial“stub”emulationsoftheexternalinterface.
Thedoctestandunittestmodulesorthird-partytestframeworkscanbeusedtoconstructexhaustivetestsuites
thatexerciseeverylineofcodeinamodule.
An appropriate testing discipline can help build large complex applications in Python as well as having interface
specifications would. In fact, it can be better because an interface specification cannot test certain properties of a
program. Forexample,thelist.append()methodisexpectedtoaddnewelementstotheendofsomeinternal
list;aninterfacespecificationcannottestthatyourlist.append()implementationwillactuallydothiscorrectly,
butit’strivialtocheckthispropertyinatestsuite.
Writingtestsuitesisveryhelpful,andyoumightwanttodesignyourcodetomakeiteasilytested. Oneincreasingly
populartechnique,test-drivendevelopment,callsforwritingpartsofthetestsuitefirst,beforeyouwriteanyofthe
actualcode. OfcoursePythonallowsyoutobesloppyandnotwritetestcasesatall.
3.23 Why is there no goto?
Inthe1970speoplerealizedthatunrestrictedgotocouldleadtomessy“spaghetti”codethatwashardtounderstand
and revise. In a high-level language, it is also unneeded as long as there are ways to branch (in Python, with if
statementsandor,and,andif/elseexpressions)andloop(withwhileandforstatements,possiblycontaining
continueandbreak).
46 Chapter3. DesignandHistoryFAQ

### 第55页

Onecanalsouseexceptionstoprovidea“structuredgoto”thatworksevenacrossfunctioncalls. Manyfeelthatex-
ceptionscanconvenientlyemulateallreasonableusesofthegoorgotoconstructsofC,Fortran,andotherlanguages.
Forexample:
class label(Exception): pass # declare a label
try:
...
if condition: raise label() # goto label
...
except label: # where to goto
pass
...
Thisdoesn’tallowyoutojumpintothemiddleofaloop,butthat’susuallyconsideredanabuseofgotoanyway. Use
sparingly.
3.24 Why can’t raw strings (r-strings) end with a backslash?
More precisely, they can’t end with an odd number of backslashes: the unpaired backslash at the end escapes the
closingquotecharacter,leavinganunterminatedstring.
Rawstringsweredesignedtoeasecreatinginputforprocessors(chieflyregularexpressionengines)thatwanttodo
their own backslash escape processing. Such processors consider an unmatched trailing backslash to be an error
anyway, sorawstringsdisallowthat. Inreturn, theyallowyoutopassonthestringquotecharacterbyescapingit
withabackslash. Theserulesworkwellwhenr-stringsareusedfortheirintendedpurpose.
Ifyou’retryingtobuildWindowspathnames,notethatallWindowssystemcallsacceptforwardslashestoo:
f = open("/mydir/file.txt") # works fine!
Ifyou’retryingtobuildapathnameforaDOScommand,trye.g. oneof
dir = r"\this\is\my\dos\dir" "\\"
dir = r"\this\is\my\dos\dir\ "[:-1]
dir = "\\this\\is\\my\\dos\\dir\\"
3.25 Why doesn’t Python have a “with” statement for attribute as-
signments?
Python has a with statement that wraps the execution of a block, calling code on the entrance and exit from the
block. Somelanguageshaveaconstructthatlookslikethis:
with obj:
a = 1 # equivalent to obj.a = 1
total = total + 1 # obj.total = obj.total + 1
InPython,suchaconstructwouldbeambiguous.
Otherlanguages,suchasObjectPascal,Delphi,andC++,usestatictypes,soit’spossibletoknow,inanunambiguous
way,whatmemberisbeingassignedto. Thisisthemainpointofstatictyping–thecompileralwaysknowsthescope
ofeveryvariableatcompiletime.
Pythonusesdynamictypes. Itisimpossibletoknowinadvancewhichattributewillbereferencedatruntime. Member
attributesmaybeaddedorremovedfromobjectsonthefly. Thismakesitimpossibletoknow,fromasimplereading,
whatattributeisbeingreferenced: alocalone,aglobalone,oramemberattribute?
Forinstance,takethefollowingincompletesnippet:
3.24. Whycan’trawstrings(r-strings)endwithabackslash? 47

### 第56页

def foo(a):
with a:
print(x)
Thesnippetassumesthatamusthaveamemberattributecalledx. However,thereisnothinginPythonthattellsthe
interpreterthis. Whatshouldhappenifais,letussay,aninteger? Ifthereisaglobalvariablenamedx,willitbe
usedinsidethewithblock? Asyousee,thedynamicnatureofPythonmakessuchchoicesmuchharder.
The primary benefit of with and similar language features (reduction of code volume) can, however, easily be
achievedinPythonbyassignment. Insteadof:
function(args).mydict[index][index].a = 21
function(args).mydict[index][index].b = 42
function(args).mydict[index][index].c = 63
writethis:
ref = function(args).mydict[index][index]
ref.a = 21
ref.b = 42
ref.c = 63
Thisalsohastheside-effectofincreasingexecutionspeedbecausenamebindingsareresolvedatrun-timeinPython,
andthesecondversiononlyneedstoperformtheresolutiononce.
Similarproposalsthatwouldintroducesyntaxtofurtherreducecodevolume,suchasusinga‘leadingdot’,havebeen
rejectedinfavourofexplicitness(seehttps://mail.python.org/pipermail/python-ideas/2016-May/040070.html).
3.26 Why don’t generators support the with statement?
Fortechnicalreasons,ageneratoruseddirectlyasacontextmanagerwouldnotworkcorrectly. When,asismostcom-
mon,ageneratorisusedasaniteratorruntocompletion,noclosingisneeded. Whenitis,wrapitascontextlib.
closing(generator)inthewithstatement.
3.27 Why are colons required for the if/while/def/class statements?
Thecolonisrequiredprimarilytoenhancereadability(oneoftheresultsoftheexperimentalABClanguage). Con-
siderthis:
if a == b
print(a)
versus
if a == b:
print(a)
Noticehowthesecondoneisslightlyeasiertoread. NoticefurtherhowacolonsetsofftheexampleinthisFAQ
answer;it’sastandardusageinEnglish.
Anotherminorreasonisthatthecolonmakesiteasierforeditorswithsyntaxhighlighting;theycanlookforcolons
todecidewhenindentationneedstobeincreasedinsteadofhavingtodoamoreelaborateparsingoftheprogram
text.
48 Chapter3. DesignandHistoryFAQ

### 第57页

3.28 Why does Python allow commas at the end of lists and tuples?
Pythonletsyouaddatrailingcommaattheendoflists,tuples,anddictionaries:
[1, 2, 3,]
('a', 'b', 'c',)
d = {
"A": [1, 5],
"B": [6, 7], # last trailing comma is optional but good style
}
Thereareseveralreasonstoallowthis.
When you have a literal value for a list, tuple, or dictionary spread across multiple lines, it’s easier to add more
elementsbecauseyoudon’thavetoremembertoaddacommatothepreviousline. Thelinescanalsobereordered
withoutcreatingasyntaxerror.
Accidentallyomittingthecommacanleadtoerrorsthatarehardtodiagnose. Forexample:
x = [
"fee",
"fie"
"foo",
"fum"
]
Thislistlookslikeithasfourelements,butitactuallycontainsthree: “fee”,“fiefoo”and“fum”. Alwaysaddingthe
commaavoidsthissourceoferror.
Allowingthetrailingcommamayalsomakeprogrammaticcodegenerationeasier.
3.28. WhydoesPythonallowcommasattheendoflistsandtuples? 49

### 第58页

50 Chapter3. DesignandHistoryFAQ

### 第59页

CHAPTER
FOUR
LIBRARY AND EXTENSION FAQ
4.1 General Library Questions
4.1.1 How do I find a module or application to perform task X?
ChecktheLibraryReferencetoseeifthere’sarelevantstandardlibrarymodule. (Eventuallyyou’lllearnwhat’sin
thestandardlibraryandwillbeabletoskipthisstep.)
Forthird-partypackages,searchthePythonPackageIndexortryGoogleoranotherwebsearchengine. Searching
for“Python”plusakeywordortwoforyourtopicofinterestwillusuallyfindsomethinghelpful.
4.1.2 Where is the math.py (socket.py, regex.py, etc.) source file?
Ifyoucan’tfindasourcefileforamoduleitmaybeabuilt-inordynamicallyloadedmoduleimplementedinC,C++
orothercompiledlanguage. Inthiscaseyoumaynothavethesourcefileoritmaybesomethinglikemathmodule.c,
somewhereinaCsourcedirectory(notonthePythonPath).
Thereare(atleast)threekindsofmodulesinPython:
1) moduleswritteninPython(.py);
2) moduleswritteninCanddynamicallyloaded(.dll,.pyd,.so,.sl,etc);
3) moduleswritteninCandlinkedwiththeinterpreter;togetalistofthese,type:
import sys
print(sys.builtin_module_names)
4.1.3 How do I make a Python script executable on Unix?
Youneedtodotwothings: thescriptfile’smodemustbeexecutableandthefirstlinemustbeginwith#!followed
bythepathofthePythoninterpreter.
Thefirstisdonebyexecutingchmod +x scriptfileorperhapschmod 755 scriptfile.
Thesecondcanbedoneinanumberofways. Themoststraightforwardwayistowrite
#!/usr/local/bin/python
astheveryfirstlineofyourfile,usingthepathnameforwherethePythoninterpreterisinstalledonyourplatform.
IfyouwouldlikethescripttobeindependentofwherethePythoninterpreterlives,youcanusetheenvprogram.
AlmostallUnixvariantssupportthefollowing,assumingthePythoninterpreterisinadirectoryontheuser’sPATH:
#!/usr/bin/env python
Don’tdothisforCGIscripts. ThePATHvariableforCGIscriptsisoftenveryminimal,soyouneedtousetheactual
absolutepathnameoftheinterpreter.
Occasionally,auser’senvironmentissofullthatthe/usr/bin/envprogramfails;orthere’snoenvprogramatall.
Inthatcase,youcantrythefollowinghack(duetoAlexRezinsky):
51

### 第60页

#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""
Theminordisadvantageisthatthisdefinesthescript’s__doc__string. However,youcanfixthatbyadding
__doc__ = """...Whatever..."""
4.1.4 Is there a curses/termcap package for Python?
ForUnixvariants: ThestandardPythonsourcedistributioncomeswithacursesmoduleintheModulessubdirectory,
thoughit’snotcompiledbydefault. (NotethatthisisnotavailableintheWindowsdistribution–thereisnocurses
moduleforWindows.)
ThecursesmodulesupportsbasiccursesfeaturesaswellasmanyadditionalfunctionsfromncursesandSYSVcurses
suchascolour,alternativecharactersetsupport,pads,andmousesupport. Thismeansthemoduleisn’tcompatible
withoperatingsystemsthatonlyhaveBSDcurses,buttheredon’tseemtobeanycurrentlymaintainedOSesthatfall
intothiscategory.
4.1.5 Is there an equivalent to C’s onexit() in Python?
TheatexitmoduleprovidesaregisterfunctionthatissimilartoC’sonexit().
4.1.6 Why don’t my signal handlers work?
Themostcommonproblemisthatthesignalhandlerisdeclaredwiththewrongargumentlist. Itiscalledas
handler(signum, frame)
soitshouldbedeclaredwithtwoparameters:
def handler(signum, frame):
...
4.2 Common tasks
4.2.1 How do I test a Python program or component?
Pythoncomeswithtwotestingframeworks. Thedoctestmodulefindsexamplesinthedocstringsforamoduleand
runsthem,comparingtheoutputwiththeexpectedoutputgiveninthedocstring.
TheunittestmoduleisafanciertestingframeworkmodelledonJavaandSmalltalktestingframeworks.
Tomaketestingeasier,youshouldusegoodmodulardesigninyourprogram. Yourprogramshouldhavealmostall
functionalityencapsulatedineitherfunctionsorclassmethods–andthissometimeshasthesurprisinganddelightful
effectofmakingtheprogramrunfaster(becauselocalvariableaccessesarefasterthanglobalaccesses). Furthermore
theprogramshouldavoiddependingonmutatingglobalvariables,sincethismakestestingmuchmoredifficulttodo.
The“globalmainlogic”ofyourprogrammaybeassimpleas
if __name__ == "__main__":
main_logic()
atthebottomofthemainmoduleofyourprogram.
Once your program is organized as a tractable collection of function and class behaviours, you should write test
functionsthatexercisethebehaviours. Atestsuitethatautomatesasequenceoftestscanbeassociatedwitheach
module. Thissoundslikealotofwork,butsincePythonissoterseandflexibleit’ssurprisinglyeasy. Youcanmake
52 Chapter4. LibraryandExtensionFAQ

### 第61页

codingmuchmorepleasantandfunbywritingyourtestfunctionsinparallelwiththe“productioncode”,sincethis
makesiteasytofindbugsandevendesignflawsearlier.
“Supportmodules”thatarenotintendedtobethemainmoduleofaprogrammayincludeaself-testofthemodule.
if __name__ == "__main__":
self_test()
Evenprogramsthatinteractwithcomplexexternalinterfacesmaybetestedwhentheexternalinterfacesareunavail-
ablebyusing“fake”interfacesimplementedinPython.
4.2.2 How do I create documentation from doc strings?
ThepydocmodulecancreateHTMLfromthedocstringsinyourPythonsourcecode. Analternativeforcreating
APIdocumentationpurelyfromdocstringsisepydoc. Sphinxcanalsoincludedocstringcontent.
4.2.3 How do I get a single keypress at a time?
ForUnixvariantsthereareseveralsolutions. It’sstraightforwardtodothisusingcurses,butcursesisafairlylarge
moduletolearn.
4.3 Threads
4.3.1 How do I program using threads?
Besuretousethethreadingmoduleandnotthe_threadmodule. Thethreadingmodulebuildsconvenient
abstractionsontopofthelow-levelprimitivesprovidedbythe_threadmodule.
4.3.2 None of my threads seem to run: why?
Assoonasthemainthreadexits,allthreadsarekilled. Yourmainthreadisrunningtooquickly,givingthethreads
notimetodoanywork.
Asimplefixistoaddasleeptotheendoftheprogramthat’slongenoughforallthethreadstofinish:
import threading, time
def thread_task(name, n):
for i in range(n):
print(name, i)
for i in range(10):
T = threading.Thread(target=thread_task, args=(str(i), i))
T.start()
time.sleep(10) # <---------------------------!
But now (on many platforms) the threads don’t run in parallel, but appear to run sequentially, one at a time! The
reasonisthattheOSthreadschedulerdoesn’tstartanewthreaduntilthepreviousthreadisblocked.
Asimplefixistoaddatinysleeptothestartoftherunfunction:
def thread_task(name, n):
time.sleep(0.001) # <--------------------!
for i in range(n):
print(name, i)
for i in range(10):
T = threading.Thread(target=thread_task, args=(str(i), i))
(continuesonnextpage)
4.3. Threads 53

### 第62页

(continuedfrompreviouspage)
T.start()
time.sleep(10)
Insteadoftryingtoguessagooddelayvaluefortime.sleep(),it’sbettertousesomekindofsemaphoremech-
anism. Oneideaistousethequeuemoduletocreateaqueueobject,leteachthreadappendatokentothequeue
whenitfinishes,andletthemainthreadreadasmanytokensfromthequeueastherearethreads.
4.3.3 How do I parcel out work among a bunch of worker threads?
Theeasiestwayistousetheconcurrent.futuresmodule,especiallytheThreadPoolExecutorclass.
Or,ifyouwantfinecontroloverthedispatchingalgorithm,youcanwriteyourownlogicmanually. Usethequeue
moduletocreateaqueuecontainingalistofjobs. TheQueueclassmaintainsalistofobjectsandhasa.put(obj)
methodthataddsitemstothequeueanda.get()methodtoreturnthem. Theclasswilltakecareofthelocking
necessarytoensurethateachjobishandedoutexactlyonce.
Here’satrivialexample:
import threading, queue, time
# The worker thread gets jobs off the queue. When the queue is empty, it
# assumes there will be no more work and exits.
# (Realistically workers will run until terminated.)
def worker():
print('Running worker')
time.sleep(0.1)
while True:
try:
arg = q.get(block=False)
except queue.Empty:
print('Worker', threading.current_thread(), end=' ')
print('queue empty')
break
else:
print('Worker', threading.current_thread(), end=' ')
print('running with argument', arg)
time.sleep(0.5)
# Create queue
q = queue.Queue()
# Start a pool of 5 workers
for i in range(5):
t = threading.Thread(target=worker, name='worker %i' % (i+1))
t.start()
# Begin adding work to the queue
for i in range(50):
q.put(i)
# Give threads time to run
print('Main thread sleeping')
time.sleep(5)
Whenrun,thiswillproducethefollowingoutput:
54 Chapter4. LibraryandExtensionFAQ

### 第63页

Running worker
Running worker
Running worker
Running worker
Running worker
Main thread sleeping
Worker <Thread(worker 1, started 130283832797456)> running with argument 0
Worker <Thread(worker 2, started 130283824404752)> running with argument 1
Worker <Thread(worker 3, started 130283816012048)> running with argument 2
Worker <Thread(worker 4, started 130283807619344)> running with argument 3
Worker <Thread(worker 5, started 130283799226640)> running with argument 4
Worker <Thread(worker 1, started 130283832797456)> running with argument 5
...
Consultthemodule’sdocumentationformoredetails;theQueueclassprovidesafeaturefulinterface.
4.3.4 What kinds of global value mutation are thread-safe?
Aglobalinterpreterlock(GIL)isusedinternallytoensurethatonlyonethreadrunsinthePythonVMatatime. In
general,Pythonofferstoswitchamongthreadsonlybetweenbytecodeinstructions; howfrequentlyitswitchescan
besetviasys.setswitchinterval(). EachbytecodeinstructionandthereforealltheCimplementationcode
reachedfromeachinstructionisthereforeatomicfromthepointofviewofaPythonprogram.
Intheory,thismeansanexactaccountingrequiresanexactunderstandingofthePVMbytecodeimplementation. In
practice,itmeansthatoperationsonsharedvariablesofbuilt-indatatypes(ints,lists,dicts,etc)that“lookatomic”
reallyare.
Forexample,thefollowingoperationsareallatomic(L,L1,L2arelists,D,D1,D2aredicts,x,yareobjects,i,jare
ints):
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop()
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()
Thesearen’t:
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1
Operationsthatreplaceotherobjectsmayinvokethoseotherobjects’__del__()methodwhentheirreferencecount
reacheszero,andthatcanaffectthings. Thisisespeciallytrueforthemassupdatestodictionariesandlists. Whenin
doubt,useamutex!
4.3.5 Can’t we get rid of the Global Interpreter Lock?
The global interpreter lock (GIL) is often seen as a hindrance to Python’s deployment on high-end multiprocessor
servermachines,becauseamulti-threadedPythonprogrameffectivelyonlyusesoneCPU,duetotheinsistencethat
(almost)allPythoncodecanonlyrunwhiletheGILisheld.
4.3. Threads 55

### 第64页

With the approval of PEP 703 work is now underway to remove the GIL from the CPython implementation of
Python. Initiallyitwillbeimplementedasanoptionalcompilerflagwhenbuildingtheinterpreter,andsoseparate
buildswillbeavailablewithandwithouttheGIL.Long-term,thehopeistosettleonasinglebuild,oncetheperfor-
manceimplicationsofremovingtheGILarefullyunderstood. Python3.13islikelytobethefirstreleasecontaining
thiswork,althoughitmaynotbecompletelyfunctionalinthisrelease.
ThecurrentworktoremovetheGILisbasedonaforkofPython3.9withtheGILremovedbySamGross. Prior
tothat,inthedaysofPython1.5,GregSteinactuallyimplementedacomprehensivepatchset(the“freethreading”
patches)thatremovedtheGILandreplaceditwithfine-grainedlocking. AdamOlsendidasimilarexperimentinhis
python-safethreadproject. Unfortunately,bothoftheseearlierexperimentsexhibitedasharpdropinsingle-thread
performance(atleast30%slower),duetotheamountoffine-grainedlockingnecessarytocompensatefortheremoval
oftheGIL.ThePython3.9forkisthefirstattemptatremovingtheGILwithanacceptableperformanceimpact.
ThepresenceoftheGILincurrentPythonreleasesdoesn’tmeanthatyoucan’tmakegooduseofPythononmulti-
CPU machines! You just have to be creative with dividing the work up between multiple processes rather than
multiplethreads. TheProcessPoolExecutorclassinthenewconcurrent.futuresmoduleprovidesaneasy
way of doing so; the multiprocessing module provides a lower-level API in case you want more control over
dispatchingoftasks.
JudicioususeofCextensionswillalsohelp;ifyouuseaCextensiontoperformatime-consumingtask,theextension
canreleasetheGILwhilethethreadofexecutionisintheCcodeandallowotherthreadstogetsomeworkdone.
Somestandardlibrarymodulessuchaszlibandhashlibalreadydothis.
AnalternativeapproachtoreducingtheimpactoftheGIListomaketheGILaper-interpreter-statelockratherthan
truly global. This was first implemented in Python 3.12 and is available in the C API. A Python interface to it is
expectedinPython3.13. Themainlimitationtoitatthemomentislikelytobe3rdpartyextensionmodules,since
thesemustbewrittenwithmultipleinterpretersinmindinordertobeusable,somanyolderextensionmoduleswill
notbeusable.
4.4 Input and Output
4.4.1 How do I delete a file? (And other file questions…)
Useos.remove(filename)oros.unlink(filename);fordocumentation,seetheosmodule. Thetwofunc-
tionsareidentical;unlink()issimplythenameoftheUnixsystemcallforthisfunction.
Toremoveadirectory, useos.rmdir(); useos.mkdir()tocreateone. os.makedirs(path)willcreateany
intermediatedirectoriesinpaththatdon’texist. os.removedirs(path)willremoveintermediatedirectoriesas
longasthey’reempty;ifyouwanttodeleteanentiredirectorytreeanditscontents,useshutil.rmtree().
Torenameafile,useos.rename(old_path, new_path).
Totruncateafile,openitusingf = open(filename, "rb+"),andusef.truncate(offset);offsetdefaults
tothecurrentseekposition. There’salsoos.ftruncate(fd, offset)forfilesopenedwithos.open(),where
fdisthefiledescriptor(asmallinteger).
The shutil module also contains a number of functions to work on files including copyfile(), copytree(),
andrmtree().
4.4.2 How do I copy a file?
The shutil module contains a copyfile() function. Note that on Windows NTFS volumes, it does not copy
alternatedatastreamsnorresourceforksonmacOSHFS+volumes,thoughbotharenowrarelyused. Italsodoesn’t
copyfilepermissionsandmetadata,thoughusingshutil.copy2()insteadwillpreservemost(thoughnotall)of
it.
4.4.3 How do I read (or write) binary data?
To read or write complex binary data formats, it’s best to use the struct module. It allows you to take a string
containingbinarydata(usuallynumbers)andconvertittoPythonobjects;andviceversa.
Forexample,thefollowingcodereadstwo2-byteintegersandone4-byteintegerinbig-endianformatfromafile:
56 Chapter4. LibraryandExtensionFAQ

### 第65页

import struct
with open(filename, "rb") as f:
s = f.read(8)
x, y, z = struct.unpack(">hhl", s)
The‘>’intheformatstringforcesbig-endiandata;theletter‘h’readsone“shortinteger”(2bytes),and‘l’readsone
“longinteger”(4bytes)fromthestring.
Fordatathatismoreregular(e.g. ahomogeneouslistofintsorfloats),youcanalsousethearraymodule.
(cid:174) Note
Toreadandwritebinarydata,itismandatorytoopenthefileinbinarymode(here,passing"rb"toopen()).
Ifyouuse "r" instead(thedefault), thefilewillbe openintextmodeand f.read() willreturnstr objects
ratherthanbytesobjects.
4.4.4 I can’t seem to use os.read() on a pipe created with os.popen(); why?
os.read()isalow-levelfunctionwhichtakesafiledescriptor, asmallintegerrepresentingtheopenedfile. os.
popen()createsahigh-levelfileobject, thesametypereturnedbythebuilt-inopen()function. Thus, toreadn
bytesfromapipepcreatedwithos.popen(),youneedtousep.read(n).
4.4.5 How do I access the serial (RS232) port?
ForWin32,OSX,Linux,BSD,Jython,IronPython:
pyserial
ForUnix,seeaUsenetpostbyMitchChapman:
https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com
4.4.6 Why doesn’t closing sys.stdout (stdin, stderr) really close it?
Pythonfileobjectsareahigh-levellayerofabstractiononlow-levelCfiledescriptors.
FormostfileobjectsyoucreateinPythonviathebuilt-inopen()function,f.close()marksthePythonfileobject
as being closed from Python’s point of view, and also arranges to close the underlying C file descriptor. This also
happensautomaticallyinf’sdestructor,whenfbecomesgarbage.
Butstdin, stdoutandstderraretreatedspeciallybyPython, becauseofthespecialstatusalsogiventothembyC.
Runningsys.stdout.close()marksthePython-levelfileobjectasbeingclosed,butdoesnotclosetheassociated
Cfiledescriptor.
ToclosetheunderlyingCfiledescriptorforoneofthesethree,youshouldfirstbesurethat’swhatyoureallywantto
do(e.g.,youmayconfuseextensionmodulestryingtodoI/O).Ifitis,useos.close():
os.close(stdin.fileno())
os.close(stdout.fileno())
os.close(stderr.fileno())
Oryoucanusethenumericconstants0,1and2,respectively.
4.5 Network/Internet Programming
4.5.1 What WWW tools are there for Python?
See the chapters titled internet and netdata in the Library Reference Manual. Python has many modules that will
helpyoubuildserver-sideandclient-sidewebsystems.
4.5. Network/InternetProgramming 57

### 第66页

A summary of available frameworks is maintained by Paul Boddie at https://wiki.python.org/moin/
WebProgramming.
4.5.2 What module should I use to help with generating HTML?
YoucanfindacollectionofusefullinksontheWebProgrammingwikipage.
4.5.3 How do I send mail from a Python script?
Usethestandardlibrarymodulesmtplib.
Here’saverysimpleinteractivemailsenderthatusesit. ThismethodwillworkonanyhostthatsupportsanSMTP
listener.
import sys, smtplib
fromaddr = input("From: ")
toaddrs = input("To: ").split(',')
print("Enter message, end with ^D:")
msg = ''
while True:
line = sys.stdin.readline()
if not line:
break
msg += line
# The actual mail send
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
AUnix-onlyalternativeusessendmail. Thelocationofthesendmailprogramvariesbetweensystems;sometimesit
is/usr/lib/sendmail,sometimes/usr/sbin/sendmail. Thesendmailmanualpagewillhelpyouout. Here’s
somesamplecode:
import os
SENDMAIL = "/usr/sbin/sendmail" # sendmail location
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write("To: receiver@example.com\n")
p.write("Subject: test\n")
p.write("\n") # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
print("Sendmail exit status", sts)
4.5.4 How do I avoid blocking in the connect() method of a socket?
TheselectmoduleiscommonlyusedtohelpwithasynchronousI/Oonsockets.
To prevent theTCP connectfrom blocking, you canset the socketto non-blockingmode. Then whenyou dothe
connect(), you will either connect immediately (unlikely) or get an exception that contains the error number as
.errno. errno.EINPROGRESSindicatesthattheconnectionisinprogress,buthasn’tfinishedyet. DifferentOSes
willreturndifferentvalues,soyou’regoingtohavetocheckwhat’sreturnedonyoursystem.
Youcanusetheconnect_ex()methodtoavoidcreatinganexception. Itwilljustreturntheerrnovalue. Topoll,
youcancallconnect_ex()againlater–0orerrno.EISCONNindicatethatyou’reconnected–oryoucanpass
thissockettoselect.select()tocheckifit’swritable.
58 Chapter4. LibraryandExtensionFAQ

### 第67页

(cid:174) Note
The asyncio module provides a general purpose single-threaded and concurrent asynchronous library, which
canbeusedforwritingnon-blockingnetworkcode. Thethird-partyTwistedlibraryisapopularandfeature-rich
alternative.
4.6 Databases
4.6.1 Are there any interfaces to database packages in Python?
Yes.
Interfaces to disk-based hashes such as DBM and GDBM are also included with standard Python. There is also the
sqlite3module,whichprovidesalightweightdisk-basedrelationaldatabase.
Supportformostrelationaldatabasesisavailable. SeetheDatabaseProgrammingwikipagefordetails.
4.6.2 How do you implement persistent objects in Python?
The pickle library module solves this in a very general way (though you still can’t store things like open files,
socketsorwindows),andtheshelvelibrarymoduleusespickleand(g)dbmtocreatepersistentmappingscontaining
arbitraryPythonobjects.
4.7 Mathematics and Numerics
4.7.1 How do I generate random numbers in Python?
Thestandardmodulerandomimplementsarandomnumbergenerator. Usageissimple:
import random
random.random()
Thisreturnsarandomfloating-pointnumberintherange[0,1).
Therearealsomanyotherspecializedgeneratorsinthismodule,suchas:
• randrange(a, b)choosesanintegerintherange[a,b).
• uniform(a, b)choosesafloating-pointnumberintherange[a,b).
• normalvariate(mean, sdev)samplesthenormal(Gaussian)distribution.
Somehigher-levelfunctionsoperateonsequencesdirectly,suchas:
• choice(S)choosesarandomelementfromagivensequence.
• shuffle(L)shufflesalistin-place,i.e. permutesitrandomly.
There’salsoaRandomclassyoucaninstantiatetocreateindependentmultiplerandomnumbergenerators.
4.6. Databases 59

### 第68页

60 Chapter4. LibraryandExtensionFAQ

### 第69页

CHAPTER
FIVE
EXTENDING/EMBEDDING FAQ
5.1 Can I create my own functions in C?
Yes, you can create built-in modules containing functions, variables, exceptions and even new types in C. This is
explainedinthedocumentextending-index.
MostintermediateoradvancedPythonbookswillalsocoverthistopic.
5.2 Can I create my own functions in C++?
Yes,usingtheCcompatibilityfeaturesfoundinC++. Placeextern "C" { ... }aroundthePythonincludefiles
andputextern "C"beforeeachfunctionthatisgoingtobecalledbythePythoninterpreter. GlobalorstaticC++
objectswithconstructorsareprobablynotagoodidea.
5.3 Writing C is hard; are there any alternatives?
ThereareanumberofalternativestowritingyourownCextensions,dependingonwhatyou’retryingtodo. Rec-
ommendedthirdpartytoolsofferbothsimplerandmoresophisticatedapproachestocreatingCandC++extensions
forPython.
5.4 How can I execute arbitrary Python statements from C?
Thehighest-levelfunctiontodothisisPyRun_SimpleString()whichtakesasinglestringargumenttobeexecuted
in the context of the module __main__ and returns 0 for success and -1 when an exception occurred (including
SyntaxError). Ifyouwantmorecontrol,usePyRun_String(); seethesourceforPyRun_SimpleString()
inPython/pythonrun.c.
5.5 How can I evaluate an arbitrary Python expression from C?
CallthefunctionPyRun_String()fromthepreviousquestionwiththestartsymbolPy_eval_input; itparses
anexpression,evaluatesitandreturnsitsvalue.
5.6 How do I extract C values from a Python object?
Thatdependsontheobject’stype. Ifit’satuple, PyTuple_Size()returnsitslengthandPyTuple_GetItem()
returnstheitemataspecifiedindex. Listshavesimilarfunctions,PyList_Size()andPyList_GetItem().
Forbytes,PyBytes_Size()returnsitslengthandPyBytes_AsStringAndSize()providesapointertoitsvalue
anditslength. NotethatPythonbytesobjectsmaycontainnullbytessoC’sstrlen()shouldnotbeused.
Totestthetypeofanobject,firstmakesureitisn’tNULL,andthenusePyBytes_Check(),PyTuple_Check(),
PyList_Check(),etc.
61

### 第70页

There is also a high-level API to Python objects which is provided by the so-called ‘abstract’ interface – read
Include/abstract.hforfurtherdetails. ItallowsinterfacingwithanykindofPythonsequenceusingcallslike
PySequence_Length(),PySequence_GetItem(),etc. aswellasmanyotherusefulprotocolssuchasnumbers
(PyNumber_Index()etal.) andmappingsinthePyMappingAPIs.
5.7 How do I use Py_BuildValue() to create a tuple of arbitrary
length?
Youcan’t. UsePyTuple_Pack()instead.
5.8 How do I call an object’s method from C?
ThePyObject_CallMethod()functioncanbeusedtocallanarbitrarymethodofanobject. Theparametersare
theobject,thenameofthemethodtocall,aformatstringlikethatusedwithPy_BuildValue(),andtheargument
values:
PyObject *
PyObject_CallMethod(PyObject *object, const char *method_name,
const char *arg_format, ...);
This works for any object that has methods – whether built-in or user-defined. You are responsible for eventually
Py_DECREF()‘ingthereturnvalue.
Tocall,e.g.,afileobject’s“seek”methodwitharguments10,0(assumingthefileobjectpointeris“f”):
res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
if (res == NULL) {
... an exception occurred ...
}
else {
Py_DECREF(res);
}
Note that since PyObject_CallObject() always wants a tuple for the argument list, to call a function without
arguments,pass“()”fortheformat,andtocallafunctionwithoneargument,surroundtheargumentinparentheses,
e.g. “(i)”.
5.9 How do I catch the output from PyErr_Print() (or anything that
prints to stdout/stderr)?
InPythoncode,defineanobjectthatsupportsthewrite()method. Assignthisobjecttosys.stdoutandsys.
stderr. Callprint_error,orjustallowthestandardtracebackmechanismtowork. Then,theoutputwillgowherever
yourwrite()methodsendsit.
Theeasiestwaytodothisistousetheio.StringIOclass:
>>> import io, sys
>>> sys.stdout = io.StringIO()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(sys.stdout.getvalue())
foo
hello world!
Acustomobjecttodothesamewouldlooklikethis:
62 Chapter5. Extending/EmbeddingFAQ

### 第71页

>>> import io, sys
>>> class StdoutCatcher(io.TextIOBase):
... def __init__(self):
... self.data = []
... def write(self, stuff):
... self.data.append(stuff)
...
>>> import sys
>>> sys.stdout = StdoutCatcher()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(''.join(sys.stdout.data))
foo
hello world!
5.10 How do I access a module written in Python from C?
Youcangetapointertothemoduleobjectasfollows:
module = PyImport_ImportModule("<modulename>");
If the module hasn’t been imported yet (i.e. it is not yet present in sys.modules), this initializes the module;
otherwiseitsimplyreturnsthevalueofsys.modules["<modulename>"]. Notethatitdoesn’tenterthemodule
intoanynamespace–itonlyensuresithasbeeninitializedandisstoredinsys.modules.
Youcanthenaccessthemodule’sattributes(i.e. anynamedefinedinthemodule)asfollows:
attr = PyObject_GetAttrString(module, "<attrname>");
CallingPyObject_SetAttrString()toassigntovariablesinthemodulealsoworks.
5.11 How do I interface to C++ objects from Python?
Dependingonyourrequirements,therearemanyapproaches. Todothismanually,beginbyreadingthe“Extending
andEmbedding”document. RealizethatforthePythonrun-timesystem,thereisn’tawholelotofdifferencebetween
CandC++–sothestrategyofbuildinganewPythontypearoundaCstructure(pointer)typewillalsoworkfor
C++objects.
ForC++libraries,seeWritingCishard;arethereanyalternatives?.
5.12 I added a module using the Setup file and the make fails; why?
Setupmustendinanewline,ifthereisnonewlinethere,thebuildprocessfails. (Fixingthisrequiressomeuglyshell
scripthackery,andthisbugissominorthatitdoesn’tseemworththeeffort.)
5.13 How do I debug an extension?
WhenusingGDBwithdynamicallyloadedextensions,youcan’tsetabreakpointinyourextensionuntilyourextension
isloaded.
Inyour.gdbinitfile(orinteractively),addthecommand:
br _PyImport_LoadDynamicModule
Then,whenyourunGDB:
5.10. HowdoIaccessamodulewritteninPythonfromC? 63

### 第72页

$ gdb /local/bin/python
gdb) run myscript.py
gdb) continue # repeat until your extension is loaded
gdb) finish # so that your extension is loaded
gdb) br myfunction.c:50
gdb) continue
5.14 I want to compile a Python module on my Linux system, but
some files are missing. Why?
MostpackagedversionsofPythonomitsomefilesrequiredforcompilingPythonextensions.
ForRedHat,installthepython3-develRPMtogetthenecessaryfiles.
ForDebian,runapt-get install python3-dev.
5.15 How do I tell “incomplete input” from “invalid input”?
SometimesyouwanttoemulatethePythoninteractiveinterpreter’sbehavior,whereitgivesyouacontinuationprompt
whentheinputisincomplete(e.g. youtypedthestartofan“if”statementoryoudidn’tcloseyourparenthesesor
triplestringquotes),butitgivesyouasyntaxerrormessageimmediatelywhentheinputisinvalid.
InPythonyoucanusethecodeopmodule,whichapproximatestheparser’sbehaviorsufficiently. IDLEusesthis,
forexample.
The easiest way to do it in C is to call PyRun_InteractiveLoop() (perhaps in a separate thread) and let the
Pythoninterpreterhandletheinputforyou. YoucanalsosetthePyOS_ReadlineFunctionPointer()topoint
atyourcustominputfunction. SeeModules/readline.candParser/myreadline.cformorehints.
5.16 How do I find undefined g++ symbols __builtin_new or
__pure_virtual?
Todynamicallyloadg++extensionmodules,youmustrecompilePython,relinkitusingg++(changeLINKCCin
thePythonModulesMakefile),andlinkyourextensionmoduleusingg++(e.g.,g++ -shared -o mymodule.so
mymodule.o).
5.17 Can I create an object class with some methods implemented
in C and others in Python (e.g. through inheritance)?
Yes,youcaninheritfrombuilt-inclassessuchasint,list,dict,etc.
The Boost Python Library (BPL, https://www.boost.org/libs/python/doc/index.html) provides a way of doing this
fromC++(i.e. youcaninheritfromanextensionclasswritteninC++usingtheBPL).
64 Chapter5. Extending/EmbeddingFAQ

### 第73页

CHAPTER
SIX
PYTHON ON WINDOWS FAQ
6.1 How do I run a Python program under Windows?
Thisisnotnecessarilyastraightforwardquestion. IfyouarealreadyfamiliarwithrunningprogramsfromtheWin-
dowscommandlinetheneverythingwillseemobvious;otherwise,youmightneedalittlemoreguidance.
Unlessyouusesomesortofintegrateddevelopmentenvironment,youwillenduptypingWindowscommandsinto
whatisreferredtoasa“Commandpromptwindow”. Usuallyyoucancreatesuchawindowfromyoursearchbar
bysearchingforcmd. Youshouldbeabletorecognizewhenyouhavestartedsuchawindowbecauseyouwillseea
Windows“commandprompt”,whichusuallylookslikethis:
C:\>
Thelettermaybedifferent,andtheremightbeotherthingsafterit,soyoumightjustaseasilyseesomethinglike:
D:\YourName\Projects\Python>
dependingonhowyourcomputerhasbeensetupandwhatelseyouhaverecentlydonewithit. Onceyouhavestarted
suchawindow,youarewellonthewaytorunningPythonprograms.
YouneedtorealizethatyourPythonscriptshavetobeprocessedbyanotherprogramcalledthePythoninterpreter.
Theinterpreterreadsyourscript,compilesitintobytecodes,andthenexecutesthebytecodestorunyourprogram.
So,howdoyouarrangefortheinterpretertohandleyourPython?
First, you need to make sure that your command window recognises the word “py” as an instruction to start the
interpreter. Ifyouhaveopenedacommandwindow,youshouldtryenteringthecommandpyandhittingreturn:
C:\Users\YourName> py
Youshouldthenseesomethinglike:
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]␣
,→on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Youhavestartedtheinterpreterin“interactivemode”. ThatmeansyoucanenterPythonstatementsorexpressions
interactivelyandhavethemexecutedorevaluatedwhileyouwait. ThisisoneofPython’sstrongestfeatures. Check
itbyenteringafewexpressionsofyourchoiceandseeingtheresults:
>>> print("Hello")
Hello
>>> "Hello" * 3
'HelloHelloHello'
Manypeopleusetheinteractivemodeasaconvenientyethighlyprogrammablecalculator. Whenyouwanttoend
yourinteractivePythonsession,calltheexit()functionorholdtheCtrlkeydownwhileyouenteraZ,thenhit
the“Enter”keytogetbacktoyourWindowscommandprompt.
65

### 第74页

YoumayalsofindthatyouhaveaStart-menuentrysuchasStart‣Programs‣Python3.x‣Python(commandline)
thatresultsinyouseeingthe>>>promptinanewwindow. Ifso,thewindowwilldisappearafteryoucalltheexit()
functionorentertheCtrl-Zcharacter;Windowsisrunningasingle“python”commandinthewindow,andcloses
itwhenyouterminatetheinterpreter.
Nowthatweknowthepycommandisrecognized,youcangiveyourPythonscripttoit. You’llhavetogiveeitheran
absoluteorarelativepathtothePythonscript. Let’ssayyourPythonscriptislocatedinyourdesktopandisnamed
hello.py,andyourcommandpromptisnicelyopenedinyourhomedirectorysoyou’reseeingsomethingsimilar
to:
C:\Users\YourName>
Sonowyou’llaskthepycommandtogiveyourscripttoPythonbytypingpyfollowedbyyourscriptpath:
C:\Users\YourName> py Desktop\hello.py
hello
6.2 How do I make Python scripts executable?
OnWindows,thestandardPythoninstalleralreadyassociatesthe.pyextensionwithafiletype(Python.File)andgives
thatfiletypeanopencommandthatrunstheinterpreter(D:\Program Files\Python\python.exe "%1" %*).
Thisisenoughtomakescriptsexecutablefromthecommandpromptas‘foo.py’. Ifyou’dratherbeabletoexecute
thescriptbysimpletyping‘foo’withnoextensionyouneedtoadd.pytothePATHEXTenvironmentvariable.
6.3 Why does Python sometimes take so long to start?
UsuallyPythonstartsveryquicklyonWindows,butoccasionallytherearebugreportsthatPythonsuddenlybegins
totakealongtimetostartup. ThisismadeevenmorepuzzlingbecausePythonwillworkfineonotherWindows
systemswhichappeartobeconfiguredidentically.
Theproblemmaybecausedbyamisconfigurationofviruscheckingsoftwareontheproblemmachine. Somevirus
scannershavebeenknowntointroducestartupoverheadoftwoordersofmagnitudewhenthescannerisconfigured
tomonitorallreadsfromthefilesystem. Trycheckingtheconfigurationofvirusscanningsoftwareonyoursystems
toensurethattheyareindeedconfiguredidentically. McAfee,whenconfiguredtoscanallfilesystemreadactivity,
isaparticularoffender.
6.4 How do I make an executable from a Python script?
SeeHowcanIcreateastand-alonebinaryfromaPythonscript? foralistoftoolsthatcanbeusedtomakeexecutables.
6.5 Is a *.pyd file the same as a DLL?
Yes, .pyd files are dll’s, but there are a few differences. If you have a DLL named foo.pyd, then it must have a
functionPyInit_foo(). YoucanthenwritePython“importfoo”,andPythonwillsearchforfoo.pyd(aswellas
foo.py,foo.pyc)andifitfindsit,willattempttocallPyInit_foo()toinitializeit. Youdonotlinkyour.exewith
foo.lib,asthatwouldcauseWindowstorequiretheDLLtobepresent.
Notethatthesearchpathforfoo.pydisPYTHONPATH,notthesameasthepaththatWindowsusestosearchfor
foo.dll. Also,foo.pydneednotbepresenttorunyourprogram,whereasifyoulinkedyourprogramwithadll,the
dllisrequired. Ofcourse,foo.pydisrequiredifyouwanttosayimport foo. InaDLL,linkageisdeclaredinthe
sourcecodewith__declspec(dllexport). Ina.pyd,linkageisdefinedinalistofavailablefunctions.
66 Chapter6. PythononWindowsFAQ

### 第75页

6.6 How can I embed Python into a Windows application?
EmbeddingthePythoninterpreterinaWindowsappcanbesummarizedasfollows:
1. Do not build Python into your .exe file directly. On Windows, Python must be a DLL to handle importing
modulesthatarethemselvesDLL’s. (Thisisthefirstkeyundocumentedfact.) Instead,linktopythonNN.dll;
itistypicallyinstalledinC:\Windows\System. NNisthePythonversion,anumbersuchas“33”forPython
3.3.
YoucanlinktoPythonintwodifferentways. Load-timelinkingmeanslinkingagainstpythonNN.lib,while
run-time linking means linking against pythonNN.dll. (General note: pythonNN.lib is the so-called
“importlib”correspondingtopythonNN.dll. Itmerelydefinessymbolsforthelinker.)
Run-time linking greatly simplifies link options; everything happens at run time. Your code must load
pythonNN.dll using the Windows LoadLibraryEx() routine. The code must also use access rou-
tines and data in pythonNN.dll (that is, Python’s C API’s) using pointers obtained by the Windows
GetProcAddress() routine. Macros can make using these pointers transparent to any C code that calls
routinesinPython’sCAPI.
2. IfyouuseSWIG,itiseasytocreateaPython“extensionmodule”thatwillmaketheapp’sdataandmethods
availabletoPython. SWIGwillhandlejustaboutallthegrungydetailsforyou. TheresultisCcodethatyou
linkintoyour.exefile(!) YoudonothavetocreateaDLLfile,andthisalsosimplifieslinking.
3. SWIGwillcreateaninitfunction(aCfunction)whosenamedependsonthenameoftheextensionmodule.
For example, if the name of the module is leo, the init function will be called initleo(). If you use SWIG
shadowclasses,asyoushould,theinitfunctionwillbecalledinitleoc(). Thisinitializesamostlyhiddenhelper
classusedbytheshadowclass.
The reason you can link the C code in step 2 into your .exe file is that calling the initialization function is
equivalenttoimportingthemoduleintoPython! (Thisisthesecondkeyundocumentedfact.)
4. Inshort,youcanusethefollowingcodetoinitializethePythoninterpreterwithyourextensionmodule.
#include <Python.h>
...
Py_Initialize(); // Initialize Python.
initmyAppc(); // Initialize (import) the helper class.
PyRun_SimpleString("import myApp"); // Import the shadow class.
5. There are two problems with Python’s C API which will become apparent if you use a compiler other than
MSVC,thecompilerusedtobuildpythonNN.dll.
Problem1: Theso-called“VeryHighLevel”functionsthattakeFILE *argumentswillnotworkinamulti-
compilerenvironmentbecauseeachcompiler’snotionofastruct FILEwillbedifferent. Fromanimple-
mentationstandpointtheseareverylowlevelfunctions.
Problem2: SWIGgeneratesthefollowingcodewhengeneratingwrapperstovoidfunctions:
Py_INCREF(Py_None);
_resultobj = Py_None;
return _resultobj;
Alas,Py_Noneisamacrothatexpandstoareferencetoacomplexdatastructurecalled_Py_NoneStructinside
pythonNN.dll. Again,thiscodewillfailinamult-compilerenvironment. Replacesuchcodeby:
return Py_BuildValue("");
ItmaybepossibletouseSWIG’s%typemapcommandtomakethechangeautomatically,thoughIhavenot
beenabletogetthistowork(I’macompleteSWIGnewbie).
6. Using a Python shell script to put up a Python interpreter window from inside your Windows app is not a
good idea; the resulting window will be independent of your app’s windowing system. Rather, you (or the
wxPythonWindowclass)shouldcreatea“native”interpreterwindow. Itiseasytoconnectthatwindowtothe
6.6. HowcanIembedPythonintoaWindowsapplication? 67

### 第76页

Pythoninterpreter. YoucanredirectPython’si/oto_any_objectthatsupportsreadandwrite,soallyouneed
isaPythonobject(definedinyourextensionmodule)thatcontainsread()andwrite()methods.
6.7 How do I keep editors from inserting tabs into my Python
source?
TheFAQdoesnotrecommendusingtabs,andthePythonstyleguide,PEP8,recommends4spacesfordistributed
Pythoncode;thisisalsotheEmacspython-modedefault.
Underanyeditor,mixingtabsandspacesisabadidea. MSVCisnodifferentinthisrespect,andiseasilyconfigured
tousespaces: TakeTools‣Options‣Tabs,andforfiletype“Default”set“Tabsize”and“Indentsize”to4,andselect
the“Insertspaces”radiobutton.
PythonraisesIndentationErrororTabErrorifmixedtabsandspacesarecausingproblemsinleadingwhites-
pace. Youmayalsorunthetabnannymoduletocheckadirectorytreeinbatchmode.
6.8 How do I check for a keypress without blocking?
Use the msvcrt module. This is a standard Windows-specific extension module. It defines a function kbhit()
whichcheckswhetherakeyboardhitispresent,andgetch()whichgetsonecharacterwithoutechoingit.
6.9 How do I solve the missing api-ms-win-crt-runtime-l1-1-0.dll er-
ror?
ThiscanoccuronPython3.5andlaterwhenusingWindows8.1orearlierwithoutallupdateshavingbeeninstalled.
First ensure your operating system is supported and is up to date, and if that does not resolve the issue, visit the
MicrosoftsupportpageforguidanceonmanuallyinstallingtheCRuntimeupdate.
68 Chapter6. PythononWindowsFAQ

### 第77页

CHAPTER
SEVEN
GRAPHIC USER INTERFACE FAQ
7.1 General GUI Questions
7.2 What GUI toolkits exist for Python?
StandardbuildsofPythonincludeanobject-orientedinterfacetotheTcl/Tkwidgetset,calledtkinter. Thisisprobably
theeasiesttoinstall(sinceitcomesincludedwithmostbinarydistributionsofPython)anduse. Formoreinfoabout
Tk, includingpointerstothesource, seetheTcl/Tkhomepage. Tcl/TkisfullyportabletothemacOS,Windows,
andUnixplatforms.
Depending on what platform(s) you are aiming at, there are also several alternatives. A list of cross-platform and
platform-specificGUIframeworkscanbefoundonthepythonwiki.
7.3 Tkinter questions
7.3.1 How do I freeze Tkinter applications?
Freezeisatooltocreatestand-aloneapplications. WhenfreezingTkinterapplications,theapplicationswillnotbe
trulystand-alone,astheapplicationwillstillneedtheTclandTklibraries.
One solution is to ship the application with the Tcl and Tk libraries, and point to them at run-time using the
TCL_LIBRARYandTK_LIBRARYenvironmentvariables.
Variousthird-partyfreezelibrariessuchaspy2exeandcx_FreezehavehandlingforTkinterapplicationsbuilt-in.
7.3.2 Can I have Tk events handled while waiting for I/O?
OnplatformsotherthanWindows,yes,andyoudon’tevenneedthreads! Butyou’llhavetorestructureyourI/Ocode
abit. TkhastheequivalentofXt’sXtAddInput()call,whichallowsyoutoregisteracallbackfunctionwhichwill
becalledfromtheTkmainloopwhenI/Oispossibleonafiledescriptor. Seetkinter-file-handlers.
7.3.3 I can’t get key bindings to work in Tkinter: why?
An often-heard complaint is that event handlers bound to events with the bind() method don’t get handled even
whentheappropriatekeyispressed.
Themostcommoncauseisthatthewidgettowhichthebindingappliesdoesn’thave“keyboardfocus”. Checkout
theTkdocumentationforthefocuscommand. Usuallyawidgetisgiventhekeyboardfocusbyclickinginit(butnot
forlabels;seethetakefocusoption).
69

### 第78页

70 Chapter7. GraphicUserInterfaceFAQ

### 第79页

CHAPTER
EIGHT
“WHY IS PYTHON INSTALLED ON MY COMPUTER?” FAQ
8.1 What is Python?
Python is a programming language. It’s used for many different applications. It’s used in some high schools and
collegesasanintroductoryprogramminglanguagebecausePythoniseasytolearn,butit’salsousedbyprofessional
softwaredevelopersatplacessuchasGoogle,NASA,andLucasfilmLtd.
IfyouwishtolearnmoreaboutPython,startwiththeBeginner’sGuidetoPython.
8.2 Why is Python installed on my machine?
IfyoufindPythoninstalledonyoursystembutdon’trememberinstallingit,thereareseveralpossiblewaysitcould
havegottenthere.
• Perhapsanotheruseronthecomputerwantedtolearnprogrammingandinstalledit;you’llhavetofigureout
who’sbeenusingthemachineandmighthaveinstalledit.
• Athird-partyapplicationinstalledonthemachinemighthavebeenwritteninPythonandincludedaPython
installation. There are many such applications, from GUI programs to network servers and administrative
scripts.
• SomeWindowsmachinesalsohavePythoninstalled. Atthiswritingwe’reawareofcomputersfromHewlett-
PackardandCompaqthatincludePython. ApparentlysomeofHP/Compaq’sadministrativetoolsarewritten
inPython.
• ManyUnix-compatibleoperatingsystems,suchasmacOSandsomeLinuxdistributions,havePythoninstalled
bydefault;it’sincludedinthebaseinstallation.
8.3 Can I delete Python?
ThatdependsonwherePythoncamefrom.
Ifsomeoneinstalleditdeliberately,youcanremoveitwithouthurtinganything. OnWindows,usetheAdd/Remove
ProgramsiconintheControlPanel.
IfPythonwasinstalledbyathird-partyapplication,youcanalsoremoveit,butthatapplicationwillnolongerwork.
Youshouldusethatapplication’suninstallerratherthanremovingPythondirectly.
IfPythoncamewithyouroperatingsystem,removingitisnotrecommended. Ifyouremoveit,whatevertoolswere
writteninPythonwillnolongerrun, andsomeofthemmightbeimportanttoyou. Reinstallingthewholesystem
wouldthenberequiredtofixthingsagain.
71

### 第80页

72 Chapter8. “WhyisPythonInstalledonmyComputer?” FAQ

### 第81页

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
73

### 第82页

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
74 AppendixA. Glossary

### 第83页

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
75

### 第84页

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
76 AppendixA. Glossary

### 第85页

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
77

### 第86页

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
78 AppendixA. Glossary

### 第87页

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
79

### 第88页

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
80 AppendixA. Glossary

### 第89页

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
81

### 第90页

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
82 AppendixA. Glossary

### 第91页

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
83

### 第92页

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
84 AppendixA. Glossary

### 第93页

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
Seealsotheargument glossaryentry,theFAQquestiononthedifferencebetweenargumentsandparameters,
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
85

### 第94页

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
86 AppendixA. Glossary

### 第95页

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
87

### 第96页

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
88 AppendixA. Glossary

### 第97页

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
89

### 第98页

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
90 AppendixA. Glossary

### 第99页

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
91

### 第100页

92 AppendixB. Aboutthisdocumentation

### 第101页

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
93

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

### 第102页

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
94 AppendixC. HistoryandLicense

### 第103页

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
C.2. TermsandconditionsforaccessingorotherwiseusingPython 95

### 第104页

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
96 AppendixC. HistoryandLicense

### 第105页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 97

### 第106页

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
98 AppendixC. HistoryandLicense

### 第107页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 99

### 第108页

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
100 AppendixC. HistoryandLicense

### 第109页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 101

### 第110页

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
102 AppendixC. HistoryandLicense

### 第111页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 103

### 第112页

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
104 AppendixC. HistoryandLicense

### 第113页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 105

### 第114页

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
106 AppendixC. HistoryandLicense

### 第115页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 107

### 第116页

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
108 AppendixC. HistoryandLicense

### 第117页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 109

### 第118页

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
110 AppendixC. HistoryandLicense

### 第119页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 111

### 第120页

112 AppendixC. HistoryandLicense

### 第121页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
113

### 第122页

114 AppendixD. Copyright

### 第123页

INDEX
Non-alphabetical
cyclic isolate,77
...,73
D
ellipsis literal,73
>>>,73 decorator,77
__future__,79 descriptor,77
__slots__,87 dictionary,77
dictionary comprehension,77
A
dictionary view,77
abstract base class,73 docstring,77
annotate function,73 duck-typing,78
annotation,73 dunder,78
argument,73
E
difference from parameter,12
asynchronous context manager,74 EAFP,78
asynchronous generator,74 environment variable
asynchronous generator iterator,74 PATH,51
asynchronous iterable,74 PYTHON_GIL,80
asynchronous iterator,74 PYTHONDONTWRITEBYTECODE,35
attached thread state,74 evaluate function,78
attribute,74 expression,78
awaitable,75 extension module,78
B F
BDFL,75 f-string,78
binary file,75 f-strings,78
borrowed reference,75 file object,78
bytecode,75 file-like object,78
bytes-like object,75 filesystem encoding and error handler,78
finder,79
C floor division,79
callable,75 Fortran contiguous,76
callback,75 free threading,79
C-contiguous,76 free variable,79
class,75
function,79
class variable,75 function annotation,79
closure variable,76
G
complex number,76
context,76 garbage collection,79
context management protocol,76 generator,79
context manager,76 generator expression,80
context variable,76 generator iterator,80
contiguous,76 generic function,80
coroutine,76 generic type,80
coroutine function,76 GIL,80
CPython,77 global interpreter lock,80
current context,77
115

### 第124页

H P
hash-based pyc,80 package,84
hashable,80 parameter,85
difference from argument,12
I
PATH,51
IDLE,81 path based finder,85
immortal,81 path entry,85
immutable,81 path entry finder,85
import path,81 path entry hook,85
importer,81 path-like object,85
importing,81 PEP,85
interactive,81 portion,86
interpreted,81 positional argument,86
interpreter shutdown,81 provisional API,86
iterable,81 provisional package,86
iterator,82 Python 3000,86
Python Enhancement Proposals
K
PEP 1,86
key function,82 PEP 5,5
keyword argument,82 PEP 8,8,32,68
PEP 238,79
L PEP 278,89
lambda,82 PEP 302,83
LBYL,82 PEP 343,76
lexical analyzer,82 PEP 362,74,85
list,82 PEP 373,4
list comprehension,82 PEP 387,2
loader,82 PEP 411,86
locale encoding,83 PEP 420,84,86
PEP 443,80
M PEP 483,80
PEP 484,73,79,80,89,90
magic
PEP 492,7477
method,83
PEP 498,78
magic method,83
PEP 519,85
mapping,83
PEP 525,74
meta path finder,83
PEP 526,73,90
metaclass,83
PEP 572,41
method,83
PEP 585,80
magic,83
PEP 602,4
special,88
PEP 649,73
method resolution order,83
PEP 683,81
module,83
PEP 703,56,79,80
module spec,83
PEP 3116,89
MRO,83
PEP 3147,35
mutable,83
PEP 3155,86
N PYTHON_GIL,80
PYTHONDONTWRITEBYTECODE,35
named tuple,84
Pythonic,86
namespace,84
namespace package,84 Q
nested scope,84
qualified name,86
new-style class,84
R
O
reference count,87
object,84
regular package,87
optimized scope,84
REPL,87
116 Index

### 第125页

S
sequence,87
set comprehension,87
single dispatch,87
slice,87
soft deprecated,87
special
method,88
special method,88
standard library,88
statement,88
static type checker,88
stdlib,88
strong reference,88
T
t-string,88
t-strings,88
text encoding,88
text file,88
thread state,88
token,89
triple-quoted string,89
type,89
type alias,89
type hint,89
U
universal newlines,89
V
variable annotation,89
virtual environment,90
virtual machine,90
W
walrus operator,90
Z
Zen of Python,90
Index 117

