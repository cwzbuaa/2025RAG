### 第1页

Python Tutorial
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 WhettingYourAppetite 3
2 UsingthePythonInterpreter 5
2.1 InvokingtheInterpreter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.1 ArgumentPassing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.1.2 InteractiveMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 TheInterpreterandItsEnvironment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2.1 SourceCodeEncoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3 AnInformalIntroductiontoPython 7
3.1 UsingPythonasaCalculator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.1.1 Numbers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.1.2 Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.1.3 Lists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 FirstStepsTowardsProgramming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 MoreControlFlowTools 17
4.1 ifStatements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.2 forStatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.3 Therange()Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.4 breakandcontinueStatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.5 elseClausesonLoops . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.6 passStatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.7 matchStatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.8 DefiningFunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.9 MoreonDefiningFunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.9.1 DefaultArgumentValues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.9.2 KeywordArguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.9.3 Specialparameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.9.4 ArbitraryArgumentLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.9.5 UnpackingArgumentLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.9.6 LambdaExpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.9.7 DocumentationStrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.9.8 FunctionAnnotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.10 Intermezzo: CodingStyle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5 DataStructures 33
5.1 MoreonLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5.1.1 UsingListsasStacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.1.2 UsingListsasQueues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.1.3 ListComprehensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.1.4 NestedListComprehensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
5.2 Thedelstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.3 TuplesandSequences. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.4 Sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
i

### 第4页

5.5 Dictionaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.6 LoopingTechniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.7 MoreonConditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.8 ComparingSequencesandOtherTypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6 Modules 43
6.1 MoreonModules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
6.1.1 Executingmodulesasscripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
6.1.2 TheModuleSearchPath . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
6.1.3 “Compiled”Pythonfiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
6.2 StandardModules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
6.3 Thedir()Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.4 Packages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.4.1 Importing*FromaPackage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6.4.2 Intra-packageReferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.4.3 PackagesinMultipleDirectories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
7 InputandOutput 53
7.1 FancierOutputFormatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
7.1.1 FormattedStringLiterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
7.1.2 TheStringformat()Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
7.1.3 ManualStringFormatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.1.4 Oldstringformatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.2 ReadingandWritingFiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.2.1 MethodsofFileObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.2.2 Savingstructureddatawithjson . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
8 ErrorsandExceptions 61
8.1 SyntaxErrors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
8.2 Exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
8.3 HandlingExceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
8.4 RaisingExceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
8.5 ExceptionChaining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
8.6 User-definedExceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
8.7 DefiningClean-upActions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
8.8 PredefinedClean-upActions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
8.9 RaisingandHandlingMultipleUnrelatedExceptions . . . . . . . . . . . . . . . . . . . . . . . . 68
8.10 EnrichingExceptionswithNotes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
9 Classes 73
9.1 AWordAboutNamesandObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
9.2 PythonScopesandNamespaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
9.2.1 ScopesandNamespacesExample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
9.3 AFirstLookatClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
9.3.1 ClassDefinitionSyntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
9.3.2 ClassObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
9.3.3 InstanceObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
9.3.4 MethodObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
9.3.5 ClassandInstanceVariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
9.4 RandomRemarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
9.5 Inheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
9.5.1 MultipleInheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.6 PrivateVariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.7 OddsandEnds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
9.8 Iterators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
9.9 Generators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
9.10 GeneratorExpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
10 BriefTouroftheStandardLibrary 87
ii

### 第5页

10.1 OperatingSystemInterface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
10.2 FileWildcards . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
10.3 CommandLineArguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
10.4 ErrorOutputRedirectionandProgramTermination . . . . . . . . . . . . . . . . . . . . . . . . . 88
10.5 StringPatternMatching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
10.6 Mathematics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
10.7 InternetAccess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
10.8 DatesandTimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.9 DataCompression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.10 PerformanceMeasurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
10.11 QualityControl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.12 BatteriesIncluded. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
11 BriefTouroftheStandardLibrary—PartII 93
11.1 OutputFormatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
11.2 Templating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
11.3 WorkingwithBinaryDataRecordLayouts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
11.4 Multi-threading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
11.5 Logging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
11.6 WeakReferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
11.7 ToolsforWorkingwithLists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
11.8 DecimalFloating-PointArithmetic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
12 VirtualEnvironmentsandPackages 101
12.1 Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
12.2 CreatingVirtualEnvironments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
12.3 ManagingPackageswithpip . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
13 WhatNow? 105
14 InteractiveInputEditingandHistorySubstitution 107
14.1 TabCompletionandHistoryEditing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
14.2 AlternativestotheInteractiveInterpreter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
15 Floating-PointArithmetic: IssuesandLimitations 109
15.1 RepresentationError . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
16 Appendix 115
16.1 InteractiveMode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
16.1.1 ErrorHandling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
16.1.2 ExecutablePythonScripts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
16.1.3 TheInteractiveStartupFile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
16.1.4 TheCustomizationModules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
A Glossary 117
B Aboutthisdocumentation 135
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
C HistoryandLicense 137
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 138
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 138
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 139
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 139
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 140
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 141
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 141
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
iii

### 第6页

C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
D Copyright 157
Index 159
iv

### 第7页

(cid:98) Tip
This tutorial is designed for programmers that are new to the Python language, not beginners who are new to
programming.
Pythonisaneasytolearn,powerfulprogramminglanguage. Ithasefficienthigh-leveldatastructuresandasimple
buteffectiveapproachtoobject-orientedprogramming. Python’selegantsyntaxanddynamictyping,togetherwith
its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on
mostplatforms.
ThePythoninterpreterandtheextensivestandardlibraryarefreelyavailableinsourceorbinaryformforallmajor
platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also
containsdistributionsofandpointerstomanyfreethirdpartyPythonmodules,programsandtools,andadditional
documentation.
The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other
languagescallablefromC).Pythonisalsosuitableasanextensionlanguageforcustomizableapplications.
ThistutorialintroducesthereaderinformallytothebasicconceptsandfeaturesofthePythonlanguageandsystem.
Be aware that it expects you to have a basic understanding of programming in general. It helps to have a Python
interpreterhandyforhands-onexperience,butallexamplesareself-contained,sothetutorialcanbereadoff-lineas
well.
Foradescriptionofstandardobjectsandmodules,seelibrary-index. reference-indexgivesamoreformaldefinition
ofthelanguage. TowriteextensionsinCorC++,readextending-indexandc-api-index. Therearealsoseveralbooks
coveringPythonindepth.
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used
feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the
language’sflavorandstyle. Afterreadingit,youwillbeabletoreadandwritePythonmodulesandprograms,and
youwillbereadytolearnmoreaboutthevariousPythonlibrarymodulesdescribedinlibrary-index.
TheGlossaryisalsoworthgoingthrough.
CONTENTS 1

### 第8页

2 CONTENTS

### 第9页

CHAPTER
ONE
WHETTING YOUR APPETITE
Ifyoudomuchworkoncomputers,eventuallyyoufindthatthere’ssometaskyou’dliketoautomate. Forexample,
youmaywishtoperformasearch-and-replaceoveralargenumberoftextfiles, orrenameandrearrangeabunch
of photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI
application,orasimplegame.
Ifyou’reaprofessionalsoftwaredeveloper,youmayhavetoworkwithseveralC/C++/Javalibrariesbutfindtheusual
write/compile/test/re-compilecycleistooslow. Perhapsyou’rewritingatestsuiteforsuchalibraryandfindwriting
thetestingcodeatedioustask. Ormaybeyou’vewrittenaprogramthatcoulduseanextensionlanguage,andyou
don’twanttodesignandimplementawholenewlanguageforyourapplication.
Pythonisjustthelanguageforyou.
YoucouldwriteaUnixshellscriptorWindowsbatchfilesforsomeofthesetasks,butshellscriptsarebestatmoving
aroundfilesandchangingtextdata,notwell-suitedforGUIapplicationsorgames. YoucouldwriteaC/C++/Java
program,butitcantakealotofdevelopmenttimetogetevenafirst-draftprogram. Pythonissimplertouse,available
onWindows,macOS,andUnixoperatingsystems,andwillhelpyougetthejobdonemorequickly.
Pythonissimpletouse,butitisarealprogramminglanguage,offeringmuchmorestructureandsupportforlarge
programsthanshellscriptsorbatchfilescanoffer. Ontheotherhand,Pythonalsooffersmuchmoreerrorchecking
thanC,and,beingavery-high-levellanguage,ithashigh-leveldatatypesbuiltin,suchasflexiblearraysanddictio-
naries. BecauseofitsmoregeneraldatatypesPythonisapplicabletoamuchlargerproblemdomainthanAwkor
evenPerl,yetmanythingsareatleastaseasyinPythonasinthoselanguages.
PythonallowsyoutosplityourprogramintomodulesthatcanbereusedinotherPythonprograms. Itcomeswitha
largecollectionofstandardmodulesthatyoucanuseasthebasisofyourprograms—orasexamplestostartlearning
toprograminPython. SomeofthesemodulesprovidethingslikefileI/O,systemcalls,sockets,andeveninterfaces
tographicaluserinterfacetoolkitslikeTk.
Pythonisaninterpretedlanguage, whichcansaveyouconsiderabletimeduringprogramdevelopmentbecauseno
compilationandlinkingisnecessary. Theinterpretercanbeusedinteractively,whichmakesiteasytoexperimentwith
featuresofthelanguage,towritethrow-awayprograms,ortotestfunctionsduringbottom-upprogramdevelopment.
Itisalsoahandydeskcalculator.
Python enables programs to be written compactly and readably. Programs written in Python are typically much
shorterthanequivalentC,C++,orJavaprograms,forseveralreasons:
• thehigh-leveldatatypesallowyoutoexpresscomplexoperationsinasinglestatement;
• statementgroupingisdonebyindentationinsteadofbeginningandendingbrackets;
• novariableorargumentdeclarationsarenecessary.
Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the
interpreter,eithertoperformcriticaloperationsatmaximumspeed,ortolinkPythonprogramstolibrariesthatmay
onlybeavailableinbinaryform(suchasavendor-specificgraphicslibrary). Onceyouarereallyhooked, youcan
linkthePythoninterpreterintoanapplicationwritteninCanduseitasanextensionorcommandlanguageforthat
application.
Bytheway,thelanguageisnamedaftertheBBCshow“MontyPython’sFlyingCircus”andhasnothingtodowith
reptiles. MakingreferencestoMontyPythonskitsindocumentationisnotonlyallowed,itisencouraged!
3

### 第10页

NowthatyouareallexcitedaboutPython,you’llwanttoexamineitinsomemoredetail. Sincethebestwaytolearn
alanguageistouseit,thetutorialinvitesyoutoplaywiththePythoninterpreterasyouread.
Inthenextchapter, themechanicsofusingtheinterpreterareexplained. Thisisrathermundaneinformation, but
essentialfortryingouttheexamplesshownlater.
The rest of the tutorial introduces various features of the Python language and system through examples, begin-
ningwithsimpleexpressions,statementsanddatatypes,throughfunctionsandmodules,andfinallytouchingupon
advancedconceptslikeexceptionsanduser-definedclasses.
4 Chapter1. WhettingYourAppetite

### 第11页

CHAPTER
TWO
USING THE PYTHON INTERPRETER
2.1 Invoking the Interpreter
ThePythoninterpreterisusuallyinstalledas/usr/local/bin/python3.14onthosemachineswhereitisavail-
able;putting/usr/local/bininyourUnixshell’ssearchpathmakesitpossibletostartitbytypingthecommand:
python3.14
totheshell.1 Sincethechoiceofthedirectorywheretheinterpreterlivesisaninstallationoption,otherplacesare
possible; check with your local Python guru or system administrator. (E.g., /usr/local/python is a popular
alternativelocation.)
OnWindowsmachineswhereyouhaveinstalledPythonfromtheMicrosoftStore,thepython3.14commandwill
beavailable. Ifyouhavethepy.exelauncherinstalled,youcanusethepycommand. Seesetting-envvarsforother
waystolaunchPython.
Typinganend-of-filecharacter(Control-DonUnix,Control-ZonWindows)attheprimarypromptcausesthe
interpretertoexitwithazeroexitstatus. Ifthatdoesn’twork, youcanexittheinterpreterbytypingthefollowing
command: quit().
Theinterpreter’sline-editingfeaturesincludeinteractiveediting,historysubstitutionandcodecompletiononsystems
thatsupporttheGNUReadlinelibrary. Perhapsthequickestchecktoseewhethercommandlineeditingissupported
istypingControl-PtothefirstPythonpromptyouget. Ifitbeeps,youhavecommandlineediting;seeAppendix
InteractiveInputEditingandHistorySubstitutionforanintroductiontothekeys. Ifnothingappearstohappen,orif
^Pisechoed,commandlineeditingisn’tavailable;you’llonlybeabletousebackspacetoremovecharactersfrom
thecurrentline.
TheinterpreteroperatessomewhatliketheUnixshell: whencalledwithstandardinputconnectedtoattydevice,it
readsandexecutescommandsinteractively;whencalledwithafilenameargumentorwithafileasstandardinput,it
readsandexecutesascriptfromthatfile.
Asecondwayofstartingtheinterpreterispython -c command [arg] ...,whichexecutesthestatement(s)in
command,analogoustotheshell’s-coption. SincePythonstatementsoftencontainspacesorothercharactersthat
arespecialtotheshell,itisusuallyadvisedtoquotecommandinitsentirety.
Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ...,
whichexecutesthesourcefileformoduleasifyouhadspelledoutitsfullnameonthecommandline.
Whenascriptfileisused,itissometimesusefultobeabletorunthescriptandenterinteractivemodeafterwards.
Thiscanbedonebypassing-ibeforethescript.
Allcommandlineoptionsaredescribedinusing-on-general.
1OnUnix,thePython3.xinterpreterisbydefaultnotinstalledwiththeexecutablenamedpython,sothatitdoesnotconflictwithasimul-
taneouslyinstalledPython2.xexecutable.
5

### 第12页

2.1.1 Argument Passing
Whenknowntotheinterpreter,thescriptnameandadditionalargumentsthereafterareturnedintoalistofstrings
andassignedtotheargvvariableinthesysmodule. Youcanaccessthislistbyexecutingimport sys. Thelength
ofthelistisatleastone;whennoscriptandnoargumentsaregiven,sys.argv[0]isanemptystring. Whenthe
script name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used,
sys.argv[0]issetto'-c'. When-mmoduleisused,sys.argv[0]issettothefullnameofthelocatedmodule.
Optionsfoundafter-ccommandor-mmodulearenotconsumedbythePythoninterpreter’soptionprocessingbut
leftinsys.argvforthecommandormoduletohandle.
2.1.2 Interactive Mode
Whencommandsarereadfromatty, theinterpreterissaidtobeininteractivemode. Inthismodeitpromptsfor
thenextcommandwiththeprimaryprompt,usuallythreegreater-thansigns(>>>);forcontinuationlinesitprompts
withthesecondaryprompt,bydefaultthreedots(...). Theinterpreterprintsawelcomemessagestatingitsversion
numberandacopyrightnoticebeforeprintingthefirstprompt:
$ python3.14
Python 3.14 (default, April 4 2024, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
Continuationlinesareneededwhenenteringamulti-lineconstruct. Asanexample,takealookatthisifstatement:
>>> the_world_is_flat = True
>>> if the_world_is_flat:
... print("Be careful not to fall off!")
...
Be careful not to fall off!
Formoreoninteractivemode,seeInteractiveMode.
2.2 The Interpreter and Its Environment
2.2.1 Source Code Encoding
Bydefault,PythonsourcefilesaretreatedasencodedinUTF-8. Inthatencoding,charactersofmostlanguagesin
the world can be used simultaneously in string literals, identifiers and comments — although the standard library
only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these
characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the
charactersinthefile.
Todeclareanencodingotherthanthedefaultone,aspecialcommentlineshouldbeaddedasthefirstlineofthefile.
Thesyntaxisasfollows:
# -*- coding: encoding -*-
whereencodingisoneofthevalidcodecssupportedbyPython.
Forexample,todeclarethatWindows-1252encodingistobeused,thefirstlineofyoursourcecodefileshouldbe:
# -*- coding: cp1252 -*-
OneexceptiontothefirstlineruleiswhenthesourcecodestartswithaUNIX“shebang”line. Inthiscase,theencoding
declarationshouldbeaddedasthesecondlineofthefile. Forexample:
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
6 Chapter2. UsingthePythonInterpreter

### 第13页

CHAPTER
THREE
AN INFORMAL INTRODUCTION TO PYTHON
In the following examples, input and output are distinguished by the presence or absence of prompts (»> and …):
torepeattheexample,youmusttypeeverythingaftertheprompt,whenthepromptappears;linesthatdonotbegin
withapromptareoutputfromtheinterpreter. Notethatasecondarypromptonalinebyitselfinanexamplemeans
youmusttypeablankline;thisisusedtoendamulti-linecommand.
Manyoftheexamplesinthismanual,eventhoseenteredattheinteractiveprompt,includecomments. Comments
inPythonstartwiththehashcharacter,#,andextendtotheendofthephysicalline. Acommentmayappearatthe
startofalineorfollowingwhitespaceorcode,butnotwithinastringliteral. Ahashcharacterwithinastringliteral
isjustahashcharacter. SincecommentsaretoclarifycodeandarenotinterpretedbyPython,theymaybeomitted
whentypinginexamples.
Someexamples:
# this is the first comment
spam = 1 # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
3.1 Using Python as a Calculator
Let’strysomesimplePythoncommands. Starttheinterpreterandwaitfortheprimaryprompt,>>>. (Itshouldn’t
takelong.)
3.1.1 Numbers
Theinterpreteractsasasimplecalculator: youcantypeanexpressionatitanditwillwritethevalue. Expression
syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be
usedforgrouping. Forexample:
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5 # division always returns a floating-point number
1.6
Theintegernumbers(e.g. 2,4,20)havetypeint,theoneswithafractionalpart(e.g. 5.0,1.6)havetypefloat.
Wewillseemoreaboutnumerictypeslaterinthetutorial.
Division (/) always returns a float. To do floor division and get an integer result you can use the // operator; to
calculatetheremainderyoucanuse%:
7

### 第14页

>>> 17 / 3 # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3 # floor division discards the fractional part
5
>>> 17 % 3 # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2 # floored quotient * divisor + remainder
17
WithPython,itispossibletousethe**operatortocalculatepowers1:
>>> 5 ** 2 # 5 squared
25
>>> 2 ** 7 # 2 to the power of 7
128
Theequalsign(=)isusedtoassignavaluetoavariable. Afterwards,noresultisdisplayedbeforethenextinteractive
prompt:
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
Ifavariableisnot“defined”(assignedavalue),tryingtouseitwillgiveyouanerror:
>>> n # try to access an undefined variable
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
Thereisfullsupportforfloatingpoint; operatorswithmixedtypeoperandsconverttheintegeroperandtofloating
point:
>>> 4 * 3.75 - 1
14.0
In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using
Pythonasadeskcalculator,itissomewhateasiertocontinuecalculations,forexample:
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
Thisvariableshouldbetreatedasread-onlybytheuser. Don’texplicitlyassignavaluetoit—youwouldcreatean
independentlocalvariablewiththesamenamemaskingthebuilt-invariablewithitsmagicbehavior.
Inadditiontointandfloat,Pythonsupportsothertypesofnumbers,suchasDecimalandFraction. Python
alsohasbuilt-insupportforcomplexnumbers,andusesthejorJsuffixtoindicatetheimaginarypart(e.g. 3+5j).
1Since**hashigherprecedencethan-,-3**2willbeinterpretedas-(3**2)andthusresultin-9. Toavoidthisandget9,youcanuse
(-3)**2.
8 Chapter3. AnInformalIntroductiontoPython

### 第15页

3.1.2 Text
Pythoncanmanipulatetext(representedbytypestr,so-called“strings”)aswellasnumbers. Thisincludescharacters
“!”,words“rabbit”,names“Paris”,sentences“Got your back.”,etc. “Yay! :)”. Theycanbeenclosedin
singlequotes('...')ordoublequotes("...")withthesameresult2.
>>> 'spam eggs' # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!" # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975' # digits and numerals enclosed in quotes are also strings
'1975'
Toquoteaquote,weneedto“escape”it,byprecedingitwith\. Alternatively,wecanusetheothertypeofquotation
marks:
>>> 'doesn\'t' # use \' to escape the single quote...
"doesn't"
>>> "doesn't" # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
InthePythonshell,thestringdefinitionandoutputstringcanlookdifferent. Theprint()functionproducesamore
readableoutput,byomittingtheenclosingquotesandbyprintingescapedandspecialcharacters:
>>> s = 'First line.\nSecond line.' # \n means newline
>>> s # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s) # with print(), special characters are interpreted, so \n produces␣
,→new line
First line.
Second line.
Ifyoudon’twantcharactersprefacedby\tobeinterpretedasspecialcharacters,youcanuserawstringsbyadding
anrbeforethefirstquote:
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') # note the r before the quote
C:\some\name
Thereisonesubtleaspecttorawstrings: arawstringmaynotendinanoddnumberof\characters;seetheFAQ
entryformoreinformationandworkarounds.
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End-of-line
charactersareautomaticallyincludedinthestring,butit’spossibletopreventthisbyaddinga\attheendoftheline.
Inthefollowingexample,theinitialnewlineisnotincluded:
>>> print("""\
... Usage: thingy [OPTIONS]
... -h Display this usage message
(continuesonnextpage)
2Unlikeotherlanguages,specialcharacterssuchas\nhavethesamemeaningwithbothsingle('...')anddouble("...")quotes. The
onlydifferencebetweenthetwoisthatwithinsinglequotesyoudon’tneedtoescape"(butyouhavetoescape\')andviceversa.
3.1. UsingPythonasaCalculator 9

### 第16页

(continuedfrompreviouspage)
... -H hostname Hostname to connect to
... """)
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
>>>
Stringscanbeconcatenated(gluedtogether)withthe+operator,andrepeatedwith*:
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
Twoormorestringliterals(i.e. theonesenclosedbetweenquotes)nexttoeachotherareautomaticallyconcatenated.
>>> 'Py' 'thon'
'Python'
Thisfeatureisparticularlyusefulwhenyouwanttobreaklongstrings:
>>> text = ('Put several strings within parentheses '
... 'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
Thisonlyworkswithtwoliteralsthough,notwithvariablesorexpressions:
>>> prefix = 'Py'
>>> prefix 'thon' # can't concatenate a variable and a string literal
File "<stdin>", line 1
prefix 'thon'
^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
File "<stdin>", line 1
('un' * 3) 'ium'
^^^^^
SyntaxError: invalid syntax
Ifyouwanttoconcatenatevariablesoravariableandaliteral,use+:
>>> prefix + 'thon'
'Python'
Stringscanbeindexed (subscripted),withthefirstcharacterhavingindex0. Thereisnoseparatecharactertype;a
characterissimplyastringofsizeone:
>>> word = 'Python'
>>> word[0] # character in position 0
'P'
>>> word[5] # character in position 5
'n'
Indicesmayalsobenegativenumbers,tostartcountingfromtheright:
>>> word[-1] # last character
'n'
(continuesonnextpage)
10 Chapter3. AnInformalIntroductiontoPython

### 第17页

(continuedfrompreviouspage)
>>> word[-2] # second-last character
'o'
>>> word[-6]
'P'
Notethatsince-0isthesameas0,negativeindicesstartfrom-1.
Inadditiontoindexing,slicingisalsosupported. Whileindexingisusedtoobtainindividualcharacters,slicingallows
youtoobtainasubstring:
>>> word[0:2] # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5] # characters from position 2 (included) to 5 (excluded)
'tho'
Sliceindiceshaveusefuldefaults;anomittedfirstindexdefaultstozero,anomittedsecondindexdefaultstothesize
ofthestringbeingsliced.
>>> word[:2] # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:] # characters from position 4 (included) to the end
'on'
>>> word[-2:] # characters from the second-last (included) to the end
'on'
Notehowthestartisalwaysincluded,andtheendalwaysexcluded. Thismakessurethats[:i] + s[i:] isalways
equaltos:
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
Onewaytorememberhowslicesworkistothinkoftheindicesaspointingbetweencharacters,withtheleftedgeof
thefirstcharacternumbered0. Thentherightedgeofthelastcharacterofastringofncharactershasindexn,for
example:
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0 1 2 3 4 5 6
-6 -5 -4 -3 -2 -1
Thefirstrowofnumbersgivesthepositionoftheindices0…6inthestring;thesecondrowgivesthecorresponding
negativeindices. Theslicefromitojconsistsofallcharactersbetweentheedgeslabelediandj,respectively.
Fornon-negativeindices,thelengthofasliceisthedifferenceoftheindices,ifbotharewithinbounds. Forexample,
thelengthofword[1:3]is2.
Attemptingtouseanindexthatistoolargewillresultinanerror:
>>> word[42] # the word only has 6 characters
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: string index out of range
However,outofrangesliceindexesarehandledgracefullywhenusedforslicing:
3.1. UsingPythonasaCalculator 11

### 第18页

>>> word[4:42]
'on'
>>> word[42:]
''
Pythonstringscannotbechanged—theyareimmutable. Therefore, assigningtoanindexedpositioninthestring
resultsinanerror:
>>> word[0] = 'J'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
Ifyouneedadifferentstring,youshouldcreateanewone:
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
Thebuilt-infunctionlen()returnsthelengthofastring:
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
(cid:181) Seealso
textseq
Stringsareexamplesofsequencetypes,andsupportthecommonoperationssupportedbysuchtypes.
string-methods
Stringssupportalargenumberofmethodsforbasictransformationsandsearching.
f-strings
Stringliteralsthathaveembeddedexpressions.
formatstrings
Informationaboutstringformattingwithstr.format().
old-string-formatting
Theoldformattingoperationsinvokedwhenstringsaretheleftoperandofthe%operatoraredescribedin
moredetailhere.
3.1.3 Lists
Pythonknowsanumberofcompounddatatypes,usedtogrouptogetherothervalues. Themostversatileisthelist,
whichcanbewrittenasalistofcomma-separatedvalues(items)betweensquarebrackets. Listsmightcontainitems
ofdifferenttypes,butusuallytheitemsallhavethesametype.
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
Likestrings(andallotherbuilt-insequencetypes),listscanbeindexedandsliced:
12 Chapter3. AnInformalIntroductiontoPython

### 第19页

>>> squares[0] # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:] # slicing returns a new list
[9, 16, 25]
Listsalsosupportoperationslikeconcatenation:
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Unlikestrings,whichareimmutable,listsareamutabletype,i.e. itispossibletochangetheircontent:
>>> cubes = [1, 8, 27, 65, 125] # something's wrong here
>>> 4 ** 3 # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64 # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
Youcanalsoaddnewitemsattheendofthelist, byusingthelist.append()method (wewillseemoreabout
methodslater):
>>> cubes.append(216) # add the cube of 6
>>> cubes.append(7 ** 3) # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
SimpleassignmentinPythonnevercopiesdata. Whenyouassignalisttoavariable,thevariablereferstotheexisting
list. Anychangesyoumaketothelistthroughonevariablewillbeseenthroughallothervariablesthatrefertoit.:
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba) # they reference the same object
True
>>> rgba.append("Alph")
>>> rgb
["Red", "Green", "Blue", "Alph"]
Allsliceoperationsreturnanewlistcontainingtherequestedelements. Thismeansthatthefollowingslicereturnsa
shallowcopyofthelist:
>>> correct_rgba = rgba[:]
>>> correct_rgba[-1] = "Alpha"
>>> correct_rgba
["Red", "Green", "Blue", "Alpha"]
>>> rgba
["Red", "Green", "Blue", "Alph"]
Assignmenttoslicesisalsopossible,andthiscanevenchangethesizeofthelistorclearitentirely:
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
(continuesonnextpage)
3.1. UsingPythonasaCalculator 13

### 第20页

(continuedfrompreviouspage)
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
Thebuilt-infunctionlen()alsoappliestolists:
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
Itispossibletonestlists(createlistscontainingotherlists),forexample:
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
3.2 First Steps Towards Programming
Ofcourse,wecanusePythonformorecomplicatedtasksthanaddingtwoandtwotogether. Forinstance,wecan
writeaninitialsub-sequenceoftheFibonacciseriesasfollows:
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a, b = 0, 1
>>> while a < 10:
... print(a)
... a, b = b, a+b
...
0
1
1
2
3
5
8
Thisexampleintroducesseveralnewfeatures.
• Thefirstlinecontainsamultipleassignment: thevariablesaandbsimultaneouslygetthenewvalues0and1.
Onthelastlinethisisusedagain,demonstratingthattheexpressionsontheright-handsideareallevaluated
firstbeforeanyoftheassignmentstakeplace. Theright-handsideexpressionsareevaluatedfromtheleftto
theright.
• Thewhileloopexecutesaslongasthecondition(here: a < 10)remainstrue. InPython,likeinC,anynon-
zerointegervalueistrue;zeroisfalse. Theconditionmayalsobeastringorlistvalue,infactanysequence;
14 Chapter3. AnInformalIntroductiontoPython

### 第21页

anythingwithanon-zerolengthistrue,emptysequencesarefalse. Thetestusedintheexampleisasimple
comparison. ThestandardcomparisonoperatorsarewrittenthesameasinC:<(lessthan),>(greaterthan),
==(equalto),<=(lessthanorequalto),>=(greaterthanorequalto)and!=(notequalto).
• Thebodyoftheloopisindented:indentationisPython’swayofgroupingstatements. Attheinteractiveprompt,
youhavetotypeataborspace(s)foreachindentedline. Inpracticeyouwillpreparemorecomplicatedinput
forPythonwithatexteditor;alldecenttexteditorshaveanauto-indentfacility. Whenacompoundstatement
is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot
guess when you have typed the last line). Note that each line within a basic block must be indented by the
sameamount.
• Theprint()functionwritesthevalueoftheargument(s)itisgiven. Itdiffersfromjustwritingtheexpression
you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments,
floating-pointquantities,andstrings. Stringsareprintedwithoutquotes,andaspaceisinsertedbetweenitems,
soyoucanformatthingsnicely,likethis:
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
Thekeywordargumentendcanbeusedtoavoidthenewlineaftertheoutput,orendtheoutputwithadifferent
string:
>>> a, b = 0, 1
>>> while a < 1000:
... print(a, end=',')
... a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
3.2. FirstStepsTowardsProgramming 15

### 第22页

16 Chapter3. AnInformalIntroductiontoPython

### 第23页

CHAPTER
FOUR
MORE CONTROL FLOW TOOLS
Aswellasthewhilestatementjustintroduced,Pythonusesafewmorethatwewillencounterinthischapter.
4.1 if Statements
Perhapsthemostwell-knownstatementtypeistheifstatement. Forexample:
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
... x = 0
... print('Negative changed to zero')
... elif x == 0:
... print('Zero')
... elif x == 1:
... print('Single')
... else:
... print('More')
...
More
Therecanbezeroormoreelifparts,andtheelsepartisoptional. Thekeyword‘elif’isshortfor‘elseif’,andis
usefultoavoidexcessiveindentation. Anif…elif…elif…sequenceisasubstitutefortheswitchorcase
statementsfoundinotherlanguages.
If you’re comparing the same value to several constants, or checking for specific types or attributes, you may also
findthematchstatementuseful. FormoredetailsseematchStatements.
4.2 for Statements
TheforstatementinPythondiffersabitfromwhatyoumaybeusedtoinCorPascal. Ratherthanalwaysiterating
overanarithmeticprogressionofnumbers(likeinPascal),orgivingtheusertheabilitytodefineboththeiteration
stepandhaltingcondition(asC),Python’sforstatementiteratesovertheitemsofanysequence(alistorastring),
intheorderthattheyappearinthesequence. Forexample(nopunintended):
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
... print(w, len(w))
...
cat 3
window 6
defenestrate 12
Codethatmodifiesacollectionwhileiteratingoverthatsamecollectioncanbetrickytogetright. Instead,itisusually
morestraight-forwardtoloopoveracopyofthecollectionortocreateanewcollection:
17

### 第24页

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '(cid:0)(cid:0)(cid:0)': 'active'}
# Strategy: Iterate over a copy
for user, status in users.copy().items():
if status == 'inactive':
del users[user]
# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
if status == 'active':
active_users[user] = status
4.3 The range() Function
Ifyoudoneedtoiterateoverasequenceofnumbers,thebuilt-infunctionrange()comesinhandy. Itgenerates
arithmeticprogressions:
>>> for i in range(5):
... print(i)
...
0
1
2
3
4
Thegivenendpointisneverpartofthegeneratedsequence;range(10)generates10values,thelegalindicesfor
items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different
increment(evennegative;sometimesthisiscalledthe‘step’):
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(-10, -100, -30))
[-10, -40, -70]
Toiterateovertheindicesofasequence,youcancombinerange()andlen()asfollows:
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
... print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
Inmostsuchcases,however,itisconvenienttousetheenumerate()function,seeLoopingTechniques.
Astrangethinghappensifyoujustprintarange:
18 Chapter4. MoreControlFlowTools

### 第25页

>>> range(10)
range(0, 10)
Inmanywaystheobjectreturnedbyrange()behavesasifitisalist,butinfactitisn’t. Itisanobjectwhichreturns
thesuccessiveitemsofthedesiredsequencewhenyouiterateoverit,butitdoesn’treallymakethelist,thussaving
space.
Wesaysuchanobjectisiterable,thatis,suitableasatargetforfunctionsandconstructsthatexpectsomethingfrom
whichtheycanobtainsuccessiveitemsuntilthesupplyisexhausted. Wehaveseenthattheforstatementissucha
construct,whileanexampleofafunctionthattakesaniterableissum():
>>> sum(range(4)) # 0 + 1 + 2 + 3
6
Laterwewillseemorefunctionsthatreturniterablesandtakeiterablesasarguments. InchapterDataStructures,we
willdiscussinmoredetailaboutlist().
4.4 break and continue Statements
Thebreakstatementbreaksoutoftheinnermostenclosingfororwhileloop:
>>> for n in range(2, 10):
... for x in range(2, n):
... if n % x == 0:
... print(f"{n} equals {x} * {n//x}")
... break
...
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
Thecontinuestatementcontinueswiththenextiterationoftheloop:
>>> for num in range(2, 10):
... if num % 2 == 0:
... print(f"Found an even number {num}")
... continue
... print(f"Found an odd number {num}")
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
4.5 else Clauses on Loops
In a for or while loop the break statement may be paired with an else clause. If the loop finishes without
executingthebreak,theelseclauseexecutes.
Inaforloop,theelseclauseisexecutedaftertheloopfinishesitsfinaliteration,thatis,ifnobreakoccurred.
Inawhileloop,it’sexecutedaftertheloop’sconditionbecomesfalse.
4.4. and Statements 19

### 第26页

Ineitherkindofloop,theelseclauseisnotexecutediftheloopwasterminatedbyabreak. Ofcourse,otherways
ofendingtheloopearly,suchasareturnoraraisedexception,willalsoskipexecutionoftheelseclause.
Thisisexemplifiedinthefollowingforloop,whichsearchesforprimenumbers:
>>> for n in range(2, 10):
... for x in range(2, n):
... if n % x == 0:
... print(n, 'equals', x, '*', n//x)
... break
... else:
... # loop fell through without finding a factor
... print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
(Yes,thisisthecorrectcode. Lookclosely: theelseclausebelongstotheforloop,nottheifstatement.)
Onewaytothinkoftheelseclauseistoimagineitpairedwiththeifinsidetheloop. Astheloopexecutes,itwill
runasequencelikeif/if/if/else. Theifisinsidetheloop,encounteredanumberoftimes. Iftheconditionisever
true,abreakwillhappen. Iftheconditionisnevertrue,theelseclauseoutsidetheloopwillexecute.
Whenusedwithaloop,theelseclausehasmoreincommonwiththeelseclauseofatrystatementthanitdoes
withthatofifstatements: atrystatement’selseclauserunswhennoexceptionoccurs,andaloop’selseclause
runswhennobreakoccurs. Formoreonthetrystatementandexceptions,seeHandlingExceptions.
4.6 pass Statements
Thepassstatementdoesnothing. Itcanbeusedwhenastatementisrequiredsyntacticallybuttheprogramrequires
noaction. Forexample:
>>> while True:
... pass # Busy-wait for keyboard interrupt (Ctrl+C)
...
Thisiscommonlyusedforcreatingminimalclasses:
>>> class MyEmptyClass:
... pass
...
Anotherplacepasscanbeusedisasaplace-holderforafunctionorconditionalbodywhenyouareworkingonnew
code,allowingyoutokeepthinkingatamoreabstractlevel. Thepassissilentlyignored:
>>> def initlog(*args):
... pass # Remember to implement this!
...
Forthislastcase,manypeopleusetheellipsisliteral...insteadofpass. ThisusehasnospecialmeaningtoPython,
andisnotpartofthelanguagedefinition(youcoulduseanyconstantexpressionhere),but...isusedconventionally
asaplaceholderbodyaswell. Seebltin-ellipsis-object.
20 Chapter4. MoreControlFlowTools

### 第27页

4.7 match Statements
A match statement takes an expression and compares its value to successive patterns given as one or more case
blocks. ThisissuperficiallysimilartoaswitchstatementinC,JavaorJavaScript(andmanyotherlanguages),butit’s
moresimilartopatternmatchinginlanguageslikeRustorHaskell. Onlythefirstpatternthatmatchesgetsexecuted
anditcanalsoextractcomponents(sequenceelementsorobjectattributes)fromthevalueintovariables. Ifnocase
matches,noneofthebranchesisexecuted.
Thesimplestformcomparesasubjectvalueagainstoneormoreliterals:
def http_error(status):
match status:
case 400:
return "Bad request"
case 404:
return "Not found"
case 418:
return "I'm a teapot"
case _:
return "Something's wrong with the internet"
Notethelastblock: the“variablename”_actsasawildcardandneverfailstomatch.
Youcancombineseveralliteralsinasinglepatternusing|(“or”):
case 401 | 403 | 404:
return "Not allowed"
Patternscanlooklikeunpackingassignments,andcanbeusedtobindvariables:
# point is an (x, y) tuple
match point:
case (0, 0):
print("Origin")
case (0, y):
print(f"Y={y}")
case (x, 0):
print(f"X={x}")
case (x, y):
print(f"X={x}, Y={y}")
case _:
raise ValueError("Not a point")
Studythatonecarefully! Thefirstpatternhastwoliterals,andcanbethoughtofasanextensionoftheliteralpattern
shownabove. Butthenexttwopatternscombinealiteralandavariable,andthevariablebindsavaluefromthesubject
(point). Thefourthpatterncapturestwovalues,whichmakesitconceptuallysimilartotheunpackingassignment
(x, y) = point.
Ifyouareusingclassestostructureyourdatayoucanusetheclassnamefollowedbyanargumentlistresemblinga
constructor,butwiththeabilitytocaptureattributesintovariables:
class Point:
def __init__(self, x, y):
self.x = x
self.y = y
def where_is(point):
match point:
case Point(x=0, y=0):
(continuesonnextpage)
4.7. Statements 21

### 第28页

(continuedfrompreviouspage)
print("Origin")
case Point(x=0, y=y):
print(f"Y={y}")
case Point(x=x, y=0):
print(f"X={x}")
case Point():
print("Somewhere else")
case _:
print("Not a point")
Youcanusepositionalparameterswithsomebuiltinclassesthatprovideanorderingfortheirattributes(e.g. data-
classes). Youcanalsodefineaspecificpositionforattributesinpatternsbysettingthe__match_args__special
attributeinyourclasses. Ifit’ssetto(“x”,“y”),thefollowingpatternsareallequivalent(andallbindtheyattribute
tothevarvariable):
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
Arecommendedwaytoreadpatternsistolookatthemasanextendedformofwhatyouwouldputontheleftof
anassignment,tounderstandwhichvariableswouldbesettowhat. Onlythestandalonenames(likevarabove)are
assigned to by a match statement. Dotted names (like foo.bar), attribute names (the x= and y= above) or class
names(recognizedbythe“(…)”nexttothemlikePointabove)areneverassignedto.
Patternscanbearbitrarilynested. Forexample,ifwehaveashortlistofPoints,with__match_args__added,we
couldmatchitlikethis:
class Point:
__match_args__ = ('x', 'y')
def __init__(self, x, y):
self.x = x
self.y = y
match points:
case []:
print("No points")
case [Point(0, 0)]:
print("The origin")
case [Point(x, y)]:
print(f"Single point {x}, {y}")
case [Point(0, y1), Point(0, y2)]:
print(f"Two on the Y axis at {y1}, {y2}")
case _:
print("Something else")
Wecanaddanifclausetoapattern,knownasa“guard”. Iftheguardisfalse,matchgoesontotrythenextcase
block. Notethatvaluecapturehappensbeforetheguardisevaluated:
match point:
case Point(x, y) if x == y:
print(f"Y=X at {x}")
case Point(x, y):
print(f"Not on the diagonal")
Severalotherkeyfeaturesofthisstatement:
• Likeunpackingassignments,tupleandlistpatternshaveexactlythesamemeaningandactuallymatcharbitrary
sequences. Animportantexceptionisthattheydon’tmatchiteratorsorstrings.
22 Chapter4. MoreControlFlowTools

### 第29页

• Sequencepatternssupportextendedunpacking: [x, y, *rest]and(x, y, *rest)worksimilartoun-
packingassignments. Thenameafter*mayalsobe_, so(x, y, *_)matchesasequenceofatleasttwo
itemswithoutbindingtheremainingitems.
• Mappingpatterns:{"bandwidth": b, "latency": l}capturesthe"bandwidth"and"latency"val-
uesfromadictionary. Unlikesequencepatterns, extrakeysareignored. Anunpackinglike**restisalso
supported. (But**_wouldberedundant,soitisnotallowed.)
• Subpatternsmaybecapturedusingtheaskeyword:
case (Point(x1, y1), Point(x2, y2) as p2): ...
willcapturethesecondelementoftheinputasp2(aslongastheinputisasequenceoftwopoints)
• Most literals are compared by equality, however the singletons True, False and None are compared by
identity.
• Patterns may use named constants. These must be dotted names to prevent them from being interpreted as
capturevariable:
from enum import Enum
class Color(Enum):
RED = 'red'
GREEN = 'green'
BLUE = 'blue'
color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
match color:
case Color.RED:
print("I see red!")
case Color.GREEN:
print("Grass is green")
case Color.BLUE:
print("I'm feeling the blues :(")
Foramoredetailedexplanationandadditionalexamples,youcanlookintoPEP636whichiswritteninatutorial
format.
4.8 Defining Functions
WecancreateafunctionthatwritestheFibonacciseriestoanarbitraryboundary:
>>> def fib(n): # write Fibonacci series less than n
... """Print a Fibonacci series less than n."""
... a, b = 0, 1
... while a < n:
... print(a, end=' ')
... a, b = b, a+b
... print()
...
>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
Thekeyworddefintroducesafunctiondefinition. Itmustbefollowedbythefunctionnameandtheparenthesizedlist
offormalparameters. Thestatementsthatformthebodyofthefunctionstartatthenextline,andmustbeindented.
Thefirststatementofthefunctionbodycanoptionallybeastringliteral;thisstringliteralisthefunction’sdocumen-
tation string, or docstring. (More about docstrings can be found in the section Documentation Strings.) There are
4.8. DefiningFunctions 23

### 第30页

toolswhichusedocstringstoautomaticallyproduceonlineorprinteddocumentation,ortolettheuserinteractively
browsethroughcode;it’sgoodpracticetoincludedocstringsincodethatyouwrite,somakeahabitofit.
Theexecutionofafunctionintroducesanewsymboltableusedforthelocalvariablesofthefunction. Moreprecisely,
allvariableassignmentsinafunctionstorethevalueinthelocalsymboltable;whereasvariablereferencesfirstlook
inthelocalsymboltable,theninthelocalsymboltablesofenclosingfunctions,thenintheglobalsymboltable,and
finallyinthetableofbuilt-innames. Thus,globalvariablesandvariablesofenclosingfunctionscannotbedirectly
assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of
enclosingfunctions,namedinanonlocalstatement),althoughtheymaybereferenced.
Theactualparameters(arguments)toafunctioncallareintroducedinthelocalsymboltableofthecalledfunction
whenitiscalled;thus,argumentsarepassedusingcallbyvalue(wherethevalueisalwaysanobjectreference,not
thevalueoftheobject).1 Whenafunctioncallsanotherfunction,orcallsitselfrecursively,anewlocalsymboltable
iscreatedforthatcall.
Afunctiondefinitionassociatesthefunctionnamewiththefunctionobjectinthecurrentsymboltable. Theinterpreter
recognizestheobjectpointedtobythatnameasauser-definedfunction. Othernamescanalsopointtothatsame
functionobjectandcanalsobeusedtoaccessthefunction:
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
Comingfromotherlanguages,youmightobjectthatfibisnotafunctionbutaproceduresinceitdoesn’treturna
value. Infact,evenfunctionswithoutareturnstatementdoreturnavalue,albeitaratherboringone. Thisvalue
iscalledNone(it’sabuilt-inname). WritingthevalueNoneisnormallysuppressedbytheinterpreterifitwouldbe
theonlyvaluewritten. Youcanseeitifyoureallywanttousingprint():
>>> fib(0)
>>> print(fib(0))
None
ItissimpletowriteafunctionthatreturnsalistofthenumbersoftheFibonacciseries,insteadofprintingit:
>>> def fib2(n): # return Fibonacci series up to n
... """Return a list containing the Fibonacci series up to n."""
... result = []
... a, b = 0, 1
... while a < n:
... result.append(a) # see below
... a, b = b, a+b
... return result
...
>>> f100 = fib2(100) # call it
>>> f100 # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Thisexample,asusual,demonstratessomenewPythonfeatures:
• Thereturnstatementreturnswithavaluefromafunction. returnwithoutanexpressionargumentreturns
None. FallingofftheendofafunctionalsoreturnsNone.
• The statement result.append(a) calls a method of the list object result. A method is a function that
‘belongs’toanobjectandisnamedobj.methodname,whereobjissomeobject(thismaybeanexpression),
andmethodnameisthenameofamethodthatisdefinedbytheobject’stype. Differenttypesdefinedifferent
methods. Methodsofdifferenttypes mayhavethesamenamewithoutcausingambiguity. (Itispossibleto
define your own object types and methods, using classes, see Classes) The method append() shown in the
1Actually,callbyobjectreferencewouldbeabetterdescription,sinceifamutableobjectispassed,thecallerwillseeanychangesthecallee
makestoit(itemsinsertedintoalist).
24 Chapter4. MoreControlFlowTools

### 第31页

exampleisdefinedforlistobjects;itaddsanewelementattheendofthelist. Inthisexampleitisequivalent
toresult = result + [a],butmoreefficient.
4.9 More on Defining Functions
It is also possible to define functions with a variable number of arguments. There are three forms, which can be
combined.
4.9.1 Default Argument Values
The most useful form is to specify a default value for one or more arguments. This creates a function that can be
calledwithfewerargumentsthanitisdefinedtoallow. Forexample:
def ask_ok(prompt, retries=4, reminder='Please try again!'):
while True:
reply = input(prompt)
if reply in {'y', 'ye', 'yes'}:
return True
if reply in {'n', 'no', 'nop', 'nope'}:
return False
retries = retries - 1
if retries < 0:
raise ValueError('invalid user response')
print(reminder)
Thisfunctioncanbecalledinseveralways:
• givingonlythemandatoryargument: ask_ok('Do you really want to quit?')
• givingoneoftheoptionalarguments: ask_ok('OK to overwrite the file?', 2)
• or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes
or no!')
Thisexamplealsointroducestheinkeyword. Thistestswhetherornotasequencecontainsacertainvalue.
Thedefaultvaluesareevaluatedatthepointoffunctiondefinitioninthedefiningscope,sothat
i = 5
def f(arg=i):
print(arg)
i = 6
f()
willprint5.
Importantwarning: Thedefaultvalueisevaluatedonlyonce. Thismakesadifferencewhenthedefaultisamutable
objectsuchasalist, dictionary, orinstancesofmostclasses. Forexample, thefollowingfunctionaccumulatesthe
argumentspassedtoitonsubsequentcalls:
def f(a, L=[]):
L.append(a)
return L
print(f(1))
print(f(2))
print(f(3))
Thiswillprint
4.9. MoreonDefiningFunctions 25

### 第32页

[1]
[1, 2]
[1, 2, 3]
Ifyoudon’twantthedefaulttobesharedbetweensubsequentcalls,youcanwritethefunctionlikethisinstead:
def f(a, L=None):
if L is None:
L = []
L.append(a)
return L
4.9.2 Keyword Arguments
Functionscanalsobecalledusingkeywordargumentsoftheformkwarg=value. Forinstance,thefollowingfunc-
tion:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
print("-- This parrot wouldn't", action, end=' ')
print("if you put", voltage, "volts through it.")
print("-- Lovely plumage, the", type)
print("-- It's", state, "!")
acceptsonerequiredargument(voltage)andthreeoptionalarguments(state,action,andtype). Thisfunction
canbecalledinanyofthefollowingways:
parrot(1000) # 1 positional argument
parrot(voltage=1000) # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword
butallthefollowingcallswouldbeinvalid:
parrot() # required argument missing
parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
parrot(110, voltage=220) # duplicate value for the same argument
parrot(actor='John Cleese') # unknown keyword argument
In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must
matchoneoftheargumentsacceptedbythefunction(e.g. actorisnotavalidargumentfortheparrotfunction),
andtheirorderisnotimportant. Thisalsoincludesnon-optionalarguments(e.g. parrot(voltage=1000)isvalid
too). Noargumentmayreceiveavaluemorethanonce. Here’sanexamplethatfailsduetothisrestriction:
>>> def function(a):
... pass
...
>>> function(0, a=0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
Whenafinalformalparameteroftheform**nameispresent,itreceivesadictionary(seetypesmapping)containing
allkeywordargumentsexceptforthosecorrespondingtoaformalparameter. Thismaybecombinedwithaformal
parameter of the form *name (described in the next subsection) which receives a tuple containing the positional
arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a
functionlikethis:
26 Chapter4. MoreControlFlowTools

### 第33页

def cheeseshop(kind, *arguments, **keywords):
print("-- Do you have any", kind, "?")
print("-- I'm sorry, we're all out of", kind)
for arg in arguments:
print(arg)
print("-" * 40)
for kw in keywords:
print(kw, ":", keywords[kw])
Itcouldbecalledlikethis:
cheeseshop("Limburger", "It's very runny, sir.",
"It's really very, VERY runny, sir.",
shopkeeper="Michael Palin",
client="John Cleese",
sketch="Cheese Shop Sketch")
andofcourseitwouldprint:
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
Notethattheorderinwhichthekeywordargumentsareprintedisguaranteedtomatchtheorderinwhichtheywere
providedinthefunctioncall.
4.9.3 Special parameters
Bydefault,argumentsmaybepassedtoaPythonfunctioneitherbypositionorexplicitlybykeyword. Forreadability
andperformance,itmakessensetorestrictthewayargumentscanbepassedsothatadeveloperneedonlylookat
thefunctiondefinitiontodetermineifitemsarepassedbyposition,bypositionorkeyword,orbykeyword.
Afunctiondefinitionmaylooklike:
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
----------- ---------- ----------
| | |
| Positional or keyword |
| - Keyword only
-- Positional only
where/and*areoptional. Ifused,thesesymbolsindicatethekindofparameterbyhowtheargumentsmaybepassed
tothefunction: positional-only,positional-or-keyword,andkeyword-only. Keywordparametersarealsoreferredto
asnamedparameters.
Positional-or-KeywordArguments
If/and*arenotpresentinthefunctiondefinition,argumentsmaybepassedtoafunctionbypositionorbykeyword.
4.9. MoreonDefiningFunctions 27

### 第34页

Positional-OnlyParameters
Lookingatthisinabitmoredetail,itispossibletomarkcertainparametersaspositional-only. Ifpositional-only,the
parameters’ordermatters,andtheparameterscannotbepassedbykeyword. Positional-onlyparametersareplaced
before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the
parameters. Ifthereisno/inthefunctiondefinition,therearenopositional-onlyparameters.
Parametersfollowingthe/maybepositional-or-keywordorkeyword-only.
Keyword-OnlyArguments
Tomarkparametersaskeyword-only,indicatingtheparametersmustbepassedbykeywordargument,placean*in
theargumentslistjustbeforethefirstkeyword-onlyparameter.
FunctionExamples
Considerthefollowingexamplefunctiondefinitionspayingcloseattentiontothemarkers/and*:
>>> def standard_arg(arg):
... print(arg)
...
>>> def pos_only_arg(arg, /):
... print(arg)
...
>>> def kwd_only_arg(*, arg):
... print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
... print(pos_only, standard, kwd_only)
Thefirstfunctiondefinition,standard_arg,themostfamiliarform,placesnorestrictionsonthecallingconvention
andargumentsmaybepassedbypositionorkeyword:
>>> standard_arg(2)
2
>>> standard_arg(arg=2)
2
The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function
definition:
>>> pos_only_arg(1)
1
>>> pos_only_arg(arg=1)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword␣
,→arguments: 'arg'
Thethirdfunctionkwd_only_argonlyallowskeywordargumentsasindicatedbya*inthefunctiondefinition:
>>> kwd_only_arg(3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
>>> kwd_only_arg(arg=3)
3
28 Chapter4. MoreControlFlowTools

### 第35页

Andthelastusesallthreecallingconventionsinthesamefunctiondefinition:
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
>>> combined_example(1, 2, kwd_only=3)
1 2 3
>>> combined_example(1, standard=2, kwd_only=3)
1 2 3
>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword␣
,→arguments: 'pos_only'
Finally,considerthisfunctiondefinitionwhichhasapotentialcollisionbetweenthepositionalargumentnameand
**kwdswhichhasnameasakey:
def foo(name, **kwds):
return 'name' in kwds
ThereisnopossiblecallthatwillmakeitreturnTrueasthekeyword'name'willalwaysbindtothefirstparameter.
Forexample:
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>
Butusing/(positionalonlyarguments),itispossiblesinceitallowsnameasapositionalargumentand'name'as
akeyinthekeywordarguments:
>>> def foo(name, /, **kwds):
... return 'name' in kwds
...
>>> foo(1, **{'name': 2})
True
Inotherwords,thenamesofpositional-onlyparameterscanbeusedin**kwdswithoutambiguity.
Recap
Theusecasewilldeterminewhichparameterstouseinthefunctiondefinition:
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
Asguidance:
• Usepositional-onlyifyouwantthenameoftheparameterstonotbeavailabletotheuser. Thisisusefulwhen
parameternameshavenorealmeaning,ifyouwanttoenforcetheorderoftheargumentswhenthefunction
iscalledorifyouneedtotakesomepositionalparametersandarbitrarykeywords.
• Use keyword-only when names have meaning and the function definition is more understandable by being
explicitwithnamesoryouwanttopreventusersrelyingonthepositionoftheargumentbeingpassed.
4.9. MoreonDefiningFunctions 29

### 第36页

• ForanAPI,usepositional-onlytopreventbreakingAPIchangesiftheparameter’snameismodifiedinthe
future.
4.9.4 Arbitrary Argument Lists
Finally,theleastfrequentlyusedoptionistospecifythatafunctioncanbecalledwithanarbitrarynumberofargu-
ments. Theseargumentswillbewrappedupinatuple(seeTuplesandSequences). Beforethevariablenumberof
arguments,zeroormorenormalargumentsmayoccur.
def write_multiple_items(file, separator, *args):
file.write(separator.join(args))
Normally,thesevariadicargumentswillbelastinthelistofformalparameters,becausetheyscoopupallremaining
inputargumentsthatarepassedtothefunction. Anyformalparameterswhichoccurafterthe*argsparameterare
‘keyword-only’arguments,meaningthattheycanonlybeusedaskeywordsratherthanpositionalarguments.
>>> def concat(*args, sep="/"):
... return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
4.9.5 Unpacking Argument Lists
Thereversesituationoccurswhentheargumentsarealreadyinalistortuplebutneedtobeunpackedforafunctioncall
requiringseparatepositionalarguments. Forinstance,thebuilt-inrange()functionexpectsseparatestartandstop
arguments. Iftheyarenotavailableseparately,writethefunctioncallwiththe*-operatortounpackthearguments
outofalistortuple:
>>> list(range(3, 6)) # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args)) # call with arguments unpacked from a list
[3, 4, 5]
Inthesamefashion,dictionariescandeliverkeywordargumentswiththe**-operator:
>>> def parrot(voltage, state='a stiff', action='voom'):
... print("-- This parrot wouldn't", action, end=' ')
... print("if you put", voltage, "volts through it.", end=' ')
... print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin
,→' demised !
4.9.6 Lambda Expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two
arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They
are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function
definition. Likenestedfunctiondefinitions,lambdafunctionscanreferencevariablesfromthecontainingscope:
>>> def make_incrementor(n):
... return lambda x: x + n
(continuesonnextpage)
30 Chapter4. MoreControlFlowTools

### 第37页

(continuedfrompreviouspage)
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
The above example uses a lambda expression to return a function. Another use is to pass a small function as an
argument. Forinstance,list.sort()takesasortingkeyfunctionkeywhichcanbealambdafunction:
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
4.9.7 Documentation Strings
Herearesomeconventionsaboutthecontentandformattingofdocumentationstrings.
Thefirstlineshouldalwaysbeashort,concisesummaryoftheobject’spurpose. Forbrevity,itshouldnotexplicitly
statetheobject’snameortype, sincetheseareavailablebyothermeans(exceptifthenamehappensto be a verb
describingafunction’soperation). Thislineshouldbeginwithacapitalletterandendwithaperiod.
Iftherearemorelinesinthedocumentationstring,thesecondlineshouldbeblank,visuallyseparatingthesummary
fromtherestofthedescription. Thefollowinglinesshouldbeoneormoreparagraphsdescribingtheobject’scalling
conventions,itssideeffects,etc.
ThePythonparserdoesnotstripindentationfrommulti-linestringliteralsinPython,sotoolsthatprocessdocumen-
tationhavetostripindentationifdesired. Thisisdoneusingthefollowingconvention. Thefirstnon-blanklineafter
thefirstlineofthestringdeterminestheamountofindentationfortheentiredocumentationstring. (Wecan’tuse
thefirstlinesinceitisgenerallyadjacenttothestring’sopeningquotessoitsindentationisnotapparentinthestring
literal.) Whitespace “equivalent” to this indentationis then stripped from the startof all lines of the string. Lines
thatareindentedlessshouldnotoccur,butiftheyoccuralltheirleadingwhitespaceshouldbestripped. Equivalence
ofwhitespaceshouldbetestedafterexpansionoftabs(to8spaces,normally).
Hereisanexampleofamulti-linedocstring:
>>> def my_function():
... """Do nothing, but document it.
...
... No, really, it doesn't do anything.
... """
... pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.
No, really, it doesn't do anything.
4.9.8 Function Annotations
Functionannotationsarecompletelyoptionalmetadatainformationaboutthetypesusedbyuser-definedfunctions
(seePEP3107andPEP484formoreinformation).
Annotationsarestoredinthe__annotations__attributeofthefunctionasadictionaryandhavenoeffectonany
otherpartofthefunction. Parameterannotationsaredefinedbyacolonaftertheparametername,followedbyan
expressionevaluatingtothevalueoftheannotation. Returnannotationsaredefinedbyaliteral->,followedbyan
expression,betweentheparameterlistandthecolondenotingtheendofthedefstatement. Thefollowingexample
hasarequiredargument,anoptionalargument,andthereturnvalueannotated:
4.9. MoreonDefiningFunctions 31

### 第38页

>>> def f(ham: str, eggs: str = 'eggs') -> str:
... print("Annotations:", f.__annotations__)
... print("Arguments:", ham, eggs)
... return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
4.10 Intermezzo: Coding Style
Nowthatyouareabouttowritelonger,morecomplexpiecesofPython,itisagoodtimetotalkaboutcodingstyle.
Mostlanguagescanbewritten(ormoreconcise,formatted)indifferentstyles;somearemorereadablethanothers.
Makingiteasyforotherstoreadyourcodeisalwaysagoodidea,andadoptinganicecodingstylehelpstremendously
forthat.
For Python, PEP 8 has emerged as the style guide that most projects adhere to; it promotes a very readable and
eye-pleasingcodingstyle. EveryPythondevelopershouldreaditatsomepoint;herearethemostimportantpoints
extractedforyou:
• Use4-spaceindentation,andnotabs.
4spacesareagoodcompromisebetweensmallindentation(allowsgreaternestingdepth)andlargeindentation
(easiertoread). Tabsintroduceconfusion,andarebestleftout.
• Wraplinessothattheydon’texceed79characters.
This helps users with small displays and makes it possible to have several code files side-by-side on larger
displays.
• Useblanklinestoseparatefunctionsandclasses,andlargerblocksofcodeinsidefunctions.
• Whenpossible,putcommentsonalineoftheirown.
• Usedocstrings.
• Usespacesaroundoperatorsandaftercommas,butnotdirectlyinsidebracketingconstructs: a = f(1, 2)
+ g(3, 4).
• Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and
lowercase_with_underscores for functions and methods. Always use self as the name for the first
methodargument(seeAFirstLookatClassesformoreonclassesandmethods).
• Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default,
UTF-8,orevenplainASCIIworkbestinanycase.
• Likewise,don’tusenon-ASCIIcharactersinidentifiersifthereisonlytheslightestchancepeoplespeakinga
differentlanguagewillreadormaintainthecode.
32 Chapter4. MoreControlFlowTools

### 第39页

CHAPTER
FIVE
DATA STRUCTURES
Thischapterdescribessomethingsyou’velearnedaboutalreadyinmoredetail,andaddssomenewthingsaswell.
5.1 More on Lists
Thelistdatatypehassomemoremethods. Hereareallofthemethodsoflistobjects:
list.append(x)
Addanitemtotheendofthelist. Similartoa[len(a):] = [x].
list.extend(iterable)
Extendthelistbyappendingalltheitemsfromtheiterable. Similartoa[len(a):] = iterable.
list.insert(i,x)
Insertanitematagivenposition. Thefirstargumentistheindexoftheelementbeforewhichtoinsert,soa.
insert(0, x)insertsatthefrontofthelist,anda.insert(len(a), x)isequivalenttoa.append(x).
list.remove(x)
Removethefirstitemfromthelistwhosevalueisequaltox. ItraisesaValueErrorifthereisnosuchitem.
[ ]
list.pop( i )
Removetheitematthegivenpositioninthelist,andreturnit. Ifnoindexisspecified,a.pop()removesand
returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list
range.
list.clear()
Removeallitemsfromthelist. Similartodel a[:].
[ [ ]]
list.index(x ,start ,end )
Returnzero-basedindexofthefirstoccurrenceofxinthelist. RaisesaValueErrorifthereisnosuchitem.
Theoptionalargumentsstart andend areinterpretedasintheslicenotationandareusedtolimitthesearch
to a particular subsequence of the list. The returned index is computed relative to the beginning of the full
sequenceratherthanthestartargument.
list.count(x)
Returnthenumberoftimesxappearsinthelist.
list.sort(*(Keyword-onlyparametersseparator(PEP3102)),key=None,reverse=False)
Sorttheitemsofthelistinplace(theargumentscanbeusedforsortcustomization,seesorted()fortheir
explanation).
list.reverse()
Reversetheelementsofthelistinplace.
list.copy()
Returnashallowcopyofthelist. Similartoa[:].
Anexamplethatusesmostofthelistmethods:
33

### 第40页

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4) # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
Youmighthavenoticedthatmethodslikeinsert,removeorsortthatonlymodifythelisthavenoreturnvalue
printed–theyreturnthedefaultNone.1 ThisisadesignprincipleforallmutabledatastructuresinPython.
Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello',
10]doesn’tsortbecauseintegerscan’tbecomparedtostringsandNonecan’tbecomparedtoothertypes. Also,there
aresometypesthatdon’thaveadefinedorderingrelation. Forexample,3+4j < 5+7jisn’tavalidcomparison.
5.1.1 Using Lists as Stacks
Thelistmethodsmakeitveryeasytousealistasastack,wherethelastelementaddedisthefirstelementretrieved
(“last-in,first-out”). Toaddanitemtothetopofthestack,useappend(). Toretrieveanitemfromthetopofthe
stack,usepop()withoutanexplicitindex. Forexample:
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
5.1.2 Using Lists as Queues
Itisalsopossibletousealistasaqueue,wherethefirstelementaddedisthefirstelementretrieved(“first-in,first-
out”); however,listsarenotefficientforthispurpose. Whileappendsandpopsfromtheendoflistarefast,doing
insertsorpopsfromthebeginningofalistisslow(becausealloftheotherelementshavetobeshiftedbyone).
1Otherlanguagesmayreturnthemutatedobject,whichallowsmethodchaining,suchasd->insert("a")->remove("b")->sort();.
34 Chapter5. DataStructures

### 第41页

To implement a queue, use collections.deque which was designed to have fast appends and pops from both
ends. Forexample:
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") # Terry arrives
>>> queue.append("Graham") # Graham arrives
>>> queue.popleft() # The first to arrive now leaves
'Eric'
>>> queue.popleft() # The second to arrive now leaves
'John'
>>> queue # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
5.1.3 List Comprehensions
Listcomprehensionsprovideaconcisewaytocreatelists. Commonapplicationsaretomakenewlistswhereeach
element is the result of some operations applied to each member of another sequence or iterable, or to create a
subsequenceofthoseelementsthatsatisfyacertaincondition.
Forexample,assumewewanttocreatealistofsquares,like:
>>> squares = []
>>> for x in range(10):
... squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Notethatthiscreates(oroverwrites)avariablenamedxthatstillexistsaftertheloopcompletes. Wecancalculate
thelistofsquareswithoutanysideeffectsusing:
squares = list(map(lambda x: x**2, range(10)))
or,equivalently:
squares = [x**2 for x in range(10)]
whichismoreconciseandreadable.
Alistcomprehensionconsistsofbracketscontaininganexpressionfollowedbyaforclause,thenzeroormorefor
orifclauses. Theresultwillbeanewlistresultingfromevaluatingtheexpressioninthecontextoftheforandif
clauseswhichfollowit. Forexample,thislistcompcombinestheelementsoftwolistsiftheyarenotequal:
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
andit’sequivalentto:
>>> combs = []
>>> for x in [1,2,3]:
... for y in [3,1,4]:
... if x != y:
... combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
Notehowtheorderoftheforandifstatementsisthesameinboththesesnippets.
Iftheexpressionisatuple(e.g. the(x, y)inthepreviousexample),itmustbeparenthesized.
5.1. MoreonLists 35

### 第42页

>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = [' banana', ' loganberry ', 'passion fruit ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
File "<stdin>", line 1
[x, x**2 for x in range(6)]
^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
Listcomprehensionscancontaincomplexexpressionsandnestedfunctions:
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
5.1.4 Nested List Comprehensions
Theinitialexpressioninalistcomprehensioncanbeanyarbitraryexpression,includinganotherlistcomprehension.
Considerthefollowingexampleofa3x4matriximplementedasalistof3listsoflength4:
>>> matrix = [
... [1, 2, 3, 4],
... [5, 6, 7, 8],
... [9, 10, 11, 12],
... ]
Thefollowinglistcomprehensionwilltransposerowsandcolumns:
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Aswesawintheprevioussection,theinnerlistcomprehensionisevaluatedinthecontextoftheforthatfollowsit,
sothisexampleisequivalentto:
>>> transposed = []
>>> for i in range(4):
... transposed.append([row[i] for row in matrix])
...
(continuesonnextpage)
36 Chapter5. DataStructures

### 第43页

(continuedfrompreviouspage)
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
which,inturn,isthesameas:
>>> transposed = []
>>> for i in range(4):
... # the following 3 lines implement the nested listcomp
... transposed_row = []
... for row in matrix:
... transposed_row.append(row[i])
... transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Intherealworld,youshouldpreferbuilt-infunctionstocomplexflowstatements. Thezip()functionwoulddoa
greatjobforthisusecase:
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
SeeUnpackingArgumentListsfordetailsontheasteriskinthisline.
5.2 The del statement
Thereisawaytoremoveanitemfromalistgivenitsindexinsteadofitsvalue: thedelstatement. Thisdiffersfrom
thepop()methodwhichreturnsavalue. Thedelstatementcanalsobeusedtoremoveslicesfromalistorclear
theentirelist(whichwedidearlierbyassignmentofanemptylisttotheslice). Forexample:
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
delcanalsobeusedtodeleteentirevariables:
>>> del a
Referencingthenameahereafterisanerror(atleastuntilanothervalueisassignedtoit). We’llfindotherusesfor
dellater.
5.3 Tuples and Sequences
Wesawthatlistsandstringshavemanycommonproperties,suchasindexingandslicingoperations. Theyaretwo
examplesofsequencedatatypes(seetypesseq). SincePythonisanevolvinglanguage,othersequencedatatypesmay
beadded. Thereisalsoanotherstandardsequencedatatype: thetuple.
Atupleconsistsofanumberofvaluesseparatedbycommas,forinstance:
5.2. The statement 37

### 第44页

>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
Asyousee,onoutputtuplesarealwaysenclosedinparentheses,sothatnestedtuplesareinterpretedcorrectly;they
maybeinputwithorwithoutsurroundingparentheses,althoughoftenparenthesesarenecessaryanyway(ifthetuple
ispartofalargerexpression). Itisnotpossibletoassigntotheindividualitemsofatuple,howeveritispossibleto
createtupleswhichcontainmutableobjects,suchaslists.
Thoughtuplesmayseemsimilartolists,theyareoftenusedindifferentsituationsandfordifferentpurposes. Tuples
areimmutable,andusuallycontainaheterogeneoussequenceofelementsthatareaccessedviaunpacking(seelater
inthissection)orindexing(orevenbyattributeinthecaseofnamedtuples). Listsaremutable,andtheirelements
areusuallyhomogeneousandareaccessedbyiteratingoverthelist.
Aspecialproblemistheconstructionoftuplescontaining0or1items: thesyntaxhassomeextraquirkstoaccom-
modatethese. Emptytuplesareconstructedbyanemptypairofparentheses; atuplewithoneitemisconstructed
byfollowingavaluewithacomma(itisnotsufficienttoencloseasinglevalueinparentheses). Ugly,buteffective.
Forexample:
>>> empty = ()
>>> singleton = 'hello', # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and
'hello!'arepackedtogetherinatuple. Thereverseoperationisalsopossible:
>>> x, y, z = t
Thisiscalled,appropriatelyenough,sequenceunpackingandworksforanysequenceontheright-handside. Sequence
unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the
sequence. Notethatmultipleassignmentisreallyjustacombinationoftuplepackingandsequenceunpacking.
5.4 Sets
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses
includemembershiptestingandeliminatingduplicateentries. Setobjectsalsosupportmathematicaloperationslike
union,intersection,difference,andsymmetricdifference.
38 Chapter5. DataStructures

### 第45页

Curlybracesortheset()functioncanbeusedtocreatesets. Note: tocreateanemptysetyouhavetouseset(),
not{};thelattercreatesanemptydictionary,adatastructurethatwediscussinthenextsection.
Hereisabriefdemonstration:
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket) # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket # fast membership testing
True
>>> 'crabgrass' in basket
False
>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b # letters in both a and b
{'a', 'c'}
>>> a ^ b # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
Similarlytolistcomprehensions,setcomprehensionsarealsosupported:
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
5.5 Dictionaries
AnotherusefuldatatypebuiltintoPythonisthedictionary(seetypesmapping). Dictionariesaresometimesfound
inotherlanguagesas“associativememories”or“associativearrays”. Unlikesequences,whichareindexedbyarange
ofnumbers,dictionariesareindexedbykeys,whichcanbeanyimmutabletype;stringsandnumberscanalwaysbe
keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable
objecteitherdirectlyorindirectly,itcannotbeusedasakey. Youcan’tuselistsaskeys,sincelistscanbemodified
inplaceusingindexassignments,sliceassignments,ormethodslikeappend()andextend().
Itisbesttothinkofadictionaryasasetofkey: valuepairs,withtherequirementthatthekeysareunique(within
onedictionary). Apairofbracescreatesanemptydictionary: {}. Placingacomma-separatedlistofkey:valuepairs
withinthebracesaddsinitialkey:valuepairstothedictionary;thisisalsothewaydictionariesarewrittenonoutput.
Themainoperationsonadictionaryarestoringavaluewithsomekeyandextractingthevaluegiventhekey. Itisalso
possibletodeleteakey:valuepairwithdel. Ifyoustoreusingakeythatisalreadyinuse,theoldvalueassociated
withthatkeyisforgotten. Itisanerrortoextractavalueusinganon-existentkey.
Performinglist(d)onadictionaryreturnsalistofallthekeysusedinthedictionary, ininsertionorder(ifyou
wantitsorted,justusesorted(d)instead). Tocheckwhetherasinglekeyisinthedictionary,usetheinkeyword.
Hereisasmallexampleusingadictionary:
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
(continuesonnextpage)
5.5. Dictionaries 39

### 第46页

(continuedfrompreviouspage)
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
Thedict()constructorbuildsdictionariesdirectlyfromsequencesofkey-valuepairs:
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
Inaddition,dictcomprehensionscanbeusedtocreatedictionariesfromarbitrarykeyandvalueexpressions:
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
Whenthekeysaresimplestrings,itissometimeseasiertospecifypairsusingkeywordarguments:
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
5.6 Looping Techniques
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the
items()method.
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
... print(k, v)
...
gallahad the pure
robin the brave
Whenloopingthroughasequence,thepositionindexandcorrespondingvaluecanberetrievedatthesametimeusing
theenumerate()function.
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
... print(i, v)
...
0 tic
1 tac
2 toe
Toloopovertwoormoresequencesatthesametime,theentriescanbepairedwiththezip()function.
40 Chapter5. DataStructures

### 第47页

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
... print('What is your {0}? It is {1}.'.format(q, a))
...
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
Toloopoverasequenceinreverse,firstspecifythesequenceinaforwarddirectionandthencallthereversed()
function.
>>> for i in reversed(range(1, 10, 2)):
... print(i)
...
9
7
5
3
1
Toloopoverasequenceinsortedorder, usethesorted()functionwhichreturnsanewsortedlistwhileleaving
thesourceunaltered.
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
... print(i)
...
apple
apple
banana
orange
orange
pear
Usingset()onasequenceeliminatesduplicateelements. Theuseofsorted()incombinationwithset()over
asequenceisanidiomaticwaytoloopoveruniqueelementsofthesequenceinsortedorder.
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
... print(f)
...
apple
banana
orange
pear
Itissometimestemptingtochangealistwhileyouareloopingoverit;however,itisoftensimplerandsafertocreate
anewlistinstead.
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
... if not math.isnan(value):
... filtered_data.append(value)
...
(continuesonnextpage)
5.6. LoopingTechniques 41

### 第48页

(continuedfrompreviouspage)
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
5.7 More on Conditions
Theconditionsusedinwhileandifstatementscancontainanyoperators,notjustcomparisons.
Thecomparisonoperatorsinandnot inaremembershipteststhatdeterminewhetheravalueisin(ornotin)a
container. Theoperatorsisandis notcomparewhethertwoobjectsarereallythesameobject. Allcomparison
operatorshavethesamepriority,whichislowerthanthatofallnumericaloperators.
Comparisonscanbechained. Forexample,a < b == ctestswhetheraislessthanbandmoreoverbequalsc.
ComparisonsmaybecombinedusingtheBooleanoperatorsandandor,andtheoutcomeofacomparison(orof
any other Boolean expression) may be negated with not. These have lower priorities than comparison operators;
betweenthem,nothasthehighestpriorityandorthelowest,sothatA and not B or Cisequivalentto(A and
(not B)) or C.Asalways,parenthesescanbeusedtoexpressthedesiredcomposition.
TheBooleanoperatorsandandorareso-calledshort-circuit operators: theirargumentsareevaluatedfromleftto
right,andevaluationstopsassoonastheoutcomeisdetermined. Forexample,ifAandCaretruebutBisfalse,A
and B and CdoesnotevaluatetheexpressionC.WhenusedasageneralvalueandnotasaBoolean, thereturn
valueofashort-circuitoperatoristhelastevaluatedargument.
ItispossibletoassigntheresultofacomparisonorotherBooleanexpressiontoavariable. Forexample,
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
NotethatinPython, unlikeC,assignmentinsideexpressionsmustbedoneexplicitlywiththewalrusoperator:=.
ThisavoidsacommonclassofproblemsencounteredinCprograms:typing=inanexpressionwhen==wasintended.
5.8 Comparing Sequences and Other Types
Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses
lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of
thecomparison; iftheyareequal, thenexttwoitemsarecompared, andsoon, untileithersequenceisexhausted.
Iftwoitemstobecomparedarethemselvessequencesofthesametype,thelexicographicalcomparisoniscarried
outrecursively. Ifallitemsoftwosequencescompareequal,thesequencesareconsideredequal. Ifonesequence
isaninitialsub-sequenceoftheother,theshortersequenceisthesmaller(lesser)one. Lexicographicalorderingfor
stringsusestheUnicodecodepointnumbertoorderindividualcharacters. Someexamplesofcomparisonsbetween
sequencesofthesametype:
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
Notethatcomparingobjectsofdifferenttypeswith<or>islegalprovidedthattheobjectshaveappropriatecom-
parisonmethods. Forexample,mixednumerictypesarecomparedaccordingtotheirnumericvalue,so0equals0.0,
etc. Otherwise,ratherthanprovidinganarbitraryordering,theinterpreterwillraiseaTypeErrorexception.
42 Chapter5. DataStructures

### 第49页

CHAPTER
SIX
MODULES
If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables)
arelost. Therefore,ifyouwanttowriteasomewhatlongerprogram,youarebetteroffusingatexteditortoprepare
theinputfortheinterpreterandrunningitwiththatfileasinputinstead. Thisisknownascreatingascript. Asyour
programgetslonger,youmaywanttosplititintoseveralfilesforeasiermaintenance. Youmayalsowanttousea
handyfunctionthatyou’vewritteninseveralprogramswithoutcopyingitsdefinitionintoeachprogram.
To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance
oftheinterpreter. Suchafileiscalledamodule; definitionsfromamodulecanbeimported intoothermodulesor
intothemainmodule(thecollectionofvariablesthatyouhaveaccesstoinascriptexecutedatthetoplevelandin
calculatormode).
AmoduleisafilecontainingPythondefinitionsandstatements. Thefilenameisthemodulenamewiththesuffix
.py appended. Within a module, the module’s name (as a string) is available as the value of the global variable
__name__. Forinstance,useyourfavoritetexteditortocreateafilecalledfibo.pyinthecurrentdirectorywith
thefollowingcontents:
# Fibonacci numbers module
def fib(n):
"""Write Fibonacci series up to n."""
a, b = 0, 1
while a < n:
print(a, end=' ')
a, b = b, a+b
print()
def fib2(n):
"""Return Fibonacci series up to n."""
result = []
a, b = 0, 1
while a < n:
result.append(a)
a, b = b, a+b
return result
NowenterthePythoninterpreterandimportthismodulewiththefollowingcommand:
>>> import fibo
Thisdoesnotaddthenamesofthefunctionsdefinedinfibodirectlytothecurrentnamespace(seePythonScopes
andNamespacesformoredetails);itonlyaddsthemodulenamefibothere. Usingthemodulenameyoucanaccess
thefunctions:
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
(continuesonnextpage)
43

### 第50页

(continuedfrompreviouspage)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
Ifyouintendtouseafunctionoftenyoucanassignittoalocalname:
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
6.1 More on Modules
Amodulecancontainexecutablestatementsaswellasfunctiondefinitions. Thesestatementsareintendedtoinitialize
themodule. Theyareexecutedonlythefirst timethemodulenameisencounteredinanimportstatement.1 (They
arealsorunifthefileisexecutedasascript.)
Eachmodulehasitsownprivatenamespace,whichisusedastheglobalnamespacebyallfunctionsdefinedinthe
module. Thus, the author of a module can use global variables in the module without worrying about accidental
clasheswithauser’sglobalvariables. Ontheotherhand,ifyouknowwhatyouaredoingyoucantouchamodule’s
globalvariableswiththesamenotationusedtorefertoitsfunctions,modname.itemname.
Modulescanimportothermodules. Itiscustomarybutnotrequiredtoplaceallimportstatementsatthebeginning
ofamodule(orscript,forthatmatter). Theimportedmodulenames,ifplacedatthetoplevelofamodule(outside
anyfunctionsorclasses),areaddedtothemodule’sglobalnamespace.
Thereisavariantoftheimportstatementthatimportsnamesfromamoduledirectlyintotheimportingmodule’s
namespace. Forexample:
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Thisdoesnotintroducethemodulenamefromwhichtheimportsaretakeninthelocalnamespace(sointheexample,
fiboisnotdefined).
Thereisevenavarianttoimportallnamesthatamoduledefines:
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Thisimportsallnamesexceptthosebeginningwithanunderscore(_). InmostcasesPythonprogrammersdonot
use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you
havealreadydefined.
Note that in general the practice of importing * from a module or package is frowned upon, since it often causes
poorlyreadablecode. However,itisokaytouseittosavetypingininteractivesessions.
Ifthemodulenameisfollowedbyas,thenthenamefollowingasisbounddirectlytotheimportedmodule.
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Thisiseffectivelyimportingthemoduleinthesamewaythatimport fibowilldo,withtheonlydifferenceofit
beingavailableasfib.
Itcanalsobeusedwhenutilisingfromwithsimilareffects:
1Infactfunctiondefinitionsarealso‘statements’thatare‘executed’;theexecutionofamodule-levelfunctiondefinitionaddsthefunctionname
tothemodule’sglobalnamespace.
44 Chapter6. Modules

### 第51页

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
(cid:174) Note
For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change
your modules, you must restart the interpreter – or, if it’s just one module you want to test interactively, use
importlib.reload(),e.g. import importlib; importlib.reload(modulename).
6.1.1 Executing modules as scripts
WhenyourunaPythonmodulewith
python fibo.py <arguments>
thecodeinthemodulewillbeexecuted,justasifyouimportedit,butwiththe__name__setto"__main__". That
meansthatbyaddingthiscodeattheendofyourmodule:
if __name__ == "__main__":
import sys
fib(int(sys.argv[1]))
youcanmakethefileusableasascriptaswellasanimportablemodule,becausethecodethatparsesthecommand
lineonlyrunsifthemoduleisexecutedasthe“main”file:
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
Ifthemoduleisimported,thecodeisnotrun:
>>> import fibo
>>>
This is often used either to provide a convenient user interface to a module, or for testing purposes (running the
moduleasascriptexecutesatestsuite).
6.1.2 The Module Search Path
Whenamodulenamedspamisimported,theinterpreterfirstsearchesforabuilt-inmodulewiththatname. These
modulenamesarelistedinsys.builtin_module_names. Ifnotfound,itthensearchesforafilenamedspam.py
inalistofdirectoriesgivenbythevariablesys.path. sys.pathisinitializedfromtheselocations:
• Thedirectorycontainingtheinputscript(orthecurrentdirectorywhennofileisspecified).
• PYTHONPATH(alistofdirectorynames,withthesamesyntaxastheshellvariablePATH).
• Theinstallation-dependentdefault(byconventionincludingasite-packagesdirectory,handledbythesite
module).
Moredetailsareatsys-path-init.
(cid:174) Note
Onfilesystemswhichsupportsymlinks,thedirectorycontainingtheinputscriptiscalculatedafterthesymlink
isfollowed. Inotherwordsthedirectorycontainingthesymlinkisnotaddedtothemodulesearchpath.
6.1. MoreonModules 45

### 第52页

Afterinitialization,Pythonprogramscanmodifysys.path. Thedirectorycontainingthescriptbeingrunisplaced
atthebeginningofthesearchpath,aheadofthestandardlibrarypath. Thismeansthatscriptsinthatdirectorywill
beloadedinsteadofmodulesofthesamenameinthelibrarydirectory. Thisisanerrorunlessthereplacementis
intended. SeesectionStandardModulesformoreinformation.
6.1.3 “Compiled” Python files
Tospeeduploadingmodules,Pythoncachesthecompiledversionofeachmoduleinthe__pycache__directory
under the name module.version.pyc, where the version encodes the format of the compiled file; it generally
containsthePythonversionnumber. Forexample,inCPythonrelease3.3thecompiledversionofspam.pywould
be cached as __pycache__/spam.cpython-33.pyc. This naming convention allows compiled modules from
differentreleasesanddifferentversionsofPythontocoexist.
Pythonchecksthemodificationdateofthesourceagainstthecompiledversiontoseeifit’soutofdateandneeds
toberecompiled. Thisisacompletelyautomaticprocess. Also,thecompiledmodulesareplatform-independent,so
thesamelibrarycanbesharedamongsystemswithdifferentarchitectures.
Pythondoesnotcheckthecacheintwocircumstances. First,italwaysrecompilesanddoesnotstoretheresultfor
themodulethat’sloadeddirectlyfromthecommandline. Second,itdoesnotcheckthecacheifthereisnosource
module. Tosupportanon-source(compiledonly)distribution,thecompiledmodulemustbeinthesourcedirectory,
andtheremustnotbeasourcemodule.
Sometipsforexperts:
• Youcanusethe-Oor-OOswitchesonthePythoncommandtoreducethesizeofacompiledmodule. The-O
switchremovesassertstatements,the-OOswitchremovesbothassertstatementsand__doc__strings. Since
someprogramsmayrelyonhavingtheseavailable,youshouldonlyusethisoptionifyouknowwhatyou’re
doing. “Optimized”moduleshaveanopt-tagandareusuallysmaller. Futurereleasesmaychangetheeffects
ofoptimization.
• Aprogramdoesn’trunanyfasterwhenitisreadfroma.pycfilethanwhenitisreadfroma.pyfile;theonly
thingthat’sfasterabout.pycfilesisthespeedwithwhichtheyareloaded.
• Themodulecompileallcancreate.pycfilesforallmodulesinadirectory.
• Thereismoredetailonthisprocess,includingaflowchartofthedecisions,inPEP3147.
6.2 Standard Modules
Pythoncomeswithalibraryofstandardmodules,describedinaseparatedocument,thePythonLibraryReference
(“Library Reference” hereafter). Some modules are built into the interpreter; these provide access to operations
thatarenotpartofthecoreofthelanguagebutareneverthelessbuiltin, eitherforefficiencyortoprovideaccess
to operating system primitives such as system calls. The set of such modules is a configuration option which also
dependsontheunderlyingplatform. Forexample,thewinregmoduleisonlyprovidedonWindowssystems. One
particularmoduledeservessomeattention: sys,whichisbuiltintoeveryPythoninterpreter. Thevariablessys.ps1
andsys.ps2definethestringsusedasprimaryandsecondaryprompts:
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
Thesetwovariablesareonlydefinediftheinterpreterisininteractivemode.
Thevariablesys.pathisalistofstringsthatdeterminestheinterpreter’ssearchpathformodules. Itisinitialized
toadefaultpathtakenfromtheenvironmentvariablePYTHONPATH,orfromabuilt-indefaultifPYTHONPATHisnot
set. Youcanmodifyitusingstandardlistoperations:
46 Chapter6. Modules

### 第53页

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
6.3 The dir() Function
Thebuilt-infunctiondir()isusedtofindoutwhichnamesamoduledefines. Itreturnsasortedlistofstrings:
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
'__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
'__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
'_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
'_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
'warnoptions']
Withoutarguments,dir()liststhenamesyouhavedefinedcurrently:
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
Notethatitlistsalltypesofnames: variables,modules,functions,etc.
dir()doesnotlistthenamesofbuilt-infunctionsandvariables. Ifyouwantalistofthose,theyaredefinedinthe
standardmodulebuiltins:
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
(continuesonnextpage)
6.3. The Function 47

### 第54页

(continuedfrompreviouspage)
'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
'NotImplementedError', 'OSError', 'OverflowError',
'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
'__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
'zip']
6.4 Packages
PackagesareawayofstructuringPython’smodulenamespacebyusing“dottedmodulenames”. Forexample,the
module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the
authorsofdifferentmodulesfromhavingtoworryabouteachother’sglobalvariablenames,theuseofdottedmodule
namessavestheauthorsofmulti-modulepackageslikeNumPyorPillowfromhavingtoworryabouteachother’s
modulenames.
Supposeyouwanttodesignacollectionofmodules(a“package”)fortheuniformhandlingofsoundfilesandsound
data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .
aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between
thevariousfileformats. Therearealsomanydifferentoperationsyoumightwanttoperformonsounddata(suchas
mixing, addingecho, applyingan equalizerfunction, creatingan artificialstereoeffect), so inadditionyouwillbe
writinganever-endingstreamofmodulestoperformtheseoperations. Here’sapossiblestructureforyourpackage
(expressedintermsofahierarchicalfilesystem):
sound/ Top-level package
__init__.py Initialize the sound package
formats/ Subpackage for file format conversions
__init__.py
wavread.py
wavwrite.py
aiffread.py
aiffwrite.py
auread.py
auwrite.py
...
effects/ Subpackage for sound effects
__init__.py
echo.py
surround.py
reverse.py
...
filters/ Subpackage for filters
__init__.py
(continuesonnextpage)
48 Chapter6. Modules

### 第55页

(continuedfrompreviouspage)
equalizer.py
vocoder.py
karaoke.py
...
Whenimportingthepackage,Pythonsearchesthroughthedirectoriesonsys.pathlookingforthepackagesubdi-
rectory.
The __init__.py files are required to make Python treat directories containing the file as packages (unless us-
ing a namespace package, a relatively advanced feature). This prevents directories with a common name, such as
string,fromunintentionallyhidingvalidmodulesthatoccurlateronthemodulesearchpath. Inthesimplestcase,
__init__.pycanjustbeanemptyfile,butitcanalsoexecuteinitializationcodeforthepackageorsetthe__all__
variable,describedlater.
Usersofthepackagecanimportindividualmodulesfromthepackage,forexample:
import sound.effects.echo
Thisloadsthesubmodulesound.effects.echo. Itmustbereferencedwithitsfullname.
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
Analternativewayofimportingthesubmoduleis:
from sound.effects import echo
Thisalsoloadsthesubmoduleecho,andmakesitavailablewithoutitspackageprefix,soitcanbeusedasfollows:
echo.echofilter(input, output, delay=0.7, atten=4)
Yetanothervariationistoimportthedesiredfunctionorvariabledirectly:
from sound.effects.echo import echofilter
Again,thisloadsthesubmoduleecho,butthismakesitsfunctionechofilter()directlyavailable:
echofilter(input, output, delay=0.7, atten=4)
Notethatwhenusingfrom package import item,theitemcanbeeitherasubmodule(orsubpackage)ofthe
package,orsomeothernamedefinedinthepackage,likeafunction,classorvariable. Theimportstatementfirst
testswhethertheitemisdefinedinthepackage;ifnot,itassumesitisamoduleandattemptstoloadit. Ifitfailsto
findit,anImportErrorexceptionisraised.
Contrarily,whenusingsyntaxlikeimport item.subitem.subsubitem,eachitemexceptforthelastmustbea
package;thelastitemcanbeamoduleorapackagebutcan’tbeaclassorfunctionorvariabledefinedintheprevious
item.
6.4.1 Importing * From a Package
Now what happens when the user writes from sound.effects import *? Ideally, one would hope that this
somehowgoesouttothefilesystem,findswhichsubmodulesarepresentinthepackage,andimportsthemall. This
couldtakealongtimeandimportingsub-modulesmighthaveunwantedside-effectsthatshouldonlyhappenwhen
thesub-moduleisexplicitlyimported.
Theonlysolutionisforthepackageauthortoprovideanexplicitindexofthepackage. Theimportstatementuses
thefollowingconvention: ifapackage’s__init__.pycodedefinesalistnamed__all__,itistakentobethelist
ofmodulenamesthatshouldbeimportedwhenfrom package import *isencountered. Itisuptothepackage
authortokeepthislistup-to-datewhenanewversionofthepackageisreleased. Packageauthorsmayalsodecide
nottosupportit,iftheydon’tseeauseforimporting*fromtheirpackage. Forexample,thefilesound/effects/
__init__.pycouldcontainthefollowingcode:
6.4. Packages 49

### 第56页

__all__ = ["echo", "surround", "reverse"]
This would mean that from sound.effects import * would import the three named submodules of the
sound.effectspackage.
Beawarethatsubmodulesmightbecomeshadowedbylocallydefinednames. Forexample,ifyouaddedareverse
functiontothesound/effects/__init__.pyfile,thefrom sound.effects import *wouldonlyimport
thetwosubmodulesechoandsurround, butnot thereversesubmodule, becauseitisshadowedbythelocally
definedreversefunction:
__all__ = [
"echo", # refers to the 'echo.py' file
"surround", # refers to the 'surround.py' file
"reverse", # !!! refers to the 'reverse' function now !!!
]
def reverse(msg: str): # <-- this name shadows the 'reverse.py' submodule
return msg[::-1] # in the case of a 'from sound.effects import *'
If__all__isnotdefined,thestatementfrom sound.effects import *doesnotimportallsubmodulesfrom
the package sound.effects into the current namespace; it only ensures that the package sound.effects has
been imported (possibly running any initialization code in __init__.py) and then imports whatever names are
definedinthepackage. Thisincludesanynamesdefined(andsubmodulesexplicitlyloaded)by__init__.py. It
alsoincludesanysubmodulesofthepackagethatwereexplicitlyloadedbypreviousimportstatements. Consider
thiscode:
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
Inthisexample,theechoandsurroundmodulesareimportedinthecurrentnamespacebecausetheyaredefinedin
thesound.effectspackagewhenthefrom...importstatementisexecuted. (Thisalsoworkswhen__all__
isdefined.)
Althoughcertainmodulesaredesignedtoexportonlynamesthatfollowcertainpatternswhenyouuseimport *,
itisstillconsideredbadpracticeinproductioncode.
Remember, thereisnothingwrongwithusingfrom package import specific_submodule! Infact, thisis
therecommendednotationunlesstheimportingmoduleneedstousesubmoduleswiththesamenamefromdifferent
packages.
6.4.2 Intra-package References
Whenpackagesarestructuredintosubpackages(aswiththesoundpackageintheexample),youcanuseabsolute
importstorefertosubmodulesofsiblingspackages. Forexample,ifthemodulesound.filters.vocoderneeds
tousetheechomoduleinthesound.effectspackage,itcanusefrom sound.effects import echo.
Youcanalsowriterelativeimports,withthefrom module import nameformofimportstatement. Theseim-
portsuseleadingdotstoindicatethecurrentandparentpackagesinvolvedintherelativeimport. Fromthesurround
moduleforexample,youmightuse:
from . import echo
from .. import formats
from ..filters import equalizer
Note that relative imports are based on the name of the current module’s package. Since the main module does
nothaveapackage,modulesintendedforuseasthemainmoduleofaPythonapplicationmustalwaysuseabsolute
imports.
50 Chapter6. Modules

### 第57页

6.4.3 Packages in Multiple Directories
Packagessupportonemorespecialattribute,__path__. Thisisinitializedtobeasequenceofstringscontainingthe
nameofthedirectoryholdingthepackage’s__init__.pybeforethecodeinthatfileisexecuted. Thisvariablecan
bemodified;doingsoaffectsfuturesearchesformodulesandsubpackagescontainedinthepackage.
Whilethisfeatureisnotoftenneeded,itcanbeusedtoextendthesetofmodulesfoundinapackage.
6.4. Packages 51

### 第58页

52 Chapter6. Modules

### 第59页

CHAPTER
SEVEN
INPUT AND OUTPUT
Thereareseveralwaystopresenttheoutputofaprogram;datacanbeprintedinahuman-readableform,orwritten
toafileforfutureuse. Thischapterwilldiscusssomeofthepossibilities.
7.1 Fancier Output Formatting
Sofarwe’veencounteredtwowaysofwritingvalues: expressionstatementsandtheprint()function. (Athirdway
is using the write() method of file objects; the standard output file can be referenced as sys.stdout. See the
LibraryReferenceformoreinformationonthis.)
Oftenyou’llwantmorecontrolovertheformattingofyouroutputthansimplyprintingspace-separatedvalues. There
areseveralwaystoformatoutput.
• Touseformattedstringliterals,beginastringwithforFbeforetheopeningquotationmarkortriplequotation
mark. Inside this string, you can write a Python expression between { and } characters that can refer to
variablesorliteralvalues.
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
• Thestr.format()methodofstringsrequiresmoremanualeffort. You’llstilluse{and}tomarkwherea
variablewillbesubstitutedandcanprovidedetailedformattingdirectives,butyou’llalsoneedtoprovidethe
informationtobeformatted. Inthefollowingcodeblocktherearetwoexamplesofhowtoformatvariables:
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes 49.67%'
Notice how the yes_votes are padded with spaces and a negative sign only for negative numbers. The
examplealsoprintspercentagemultipliedby100,with2decimalplacesandfollowedbyapercentsign(see
formatspecfordetails).
• Finally,youcandoallthestringhandlingyourselfbyusingstringslicingandconcatenationoperationstocreate
any layout you can imagine. The string type has some methods that perform useful operations for padding
stringstoagivencolumnwidth.
Whenyoudon’tneedfancyoutputbutjustwantaquickdisplayofsomevariablesfordebuggingpurposes,youcan
convertanyvaluetoastringwiththerepr()orstr()functions.
The str() function is meant to return representations of values which are fairly human-readable, while repr()
ismeanttogeneraterepresentationswhichcanbereadbytheinterpreter(orwillforceaSyntaxErrorifthereis
noequivalentsyntax). Forobjectswhichdon’thaveaparticularrepresentationforhumanconsumption,str()will
returnthesamevalueasrepr(). Manyvalues, suchasnumbersorstructureslikelistsanddictionaries, havethe
samerepresentationusingeitherfunction. Strings,inparticular,havetwodistinctrepresentations.
53

### 第60页

Someexamples:
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
Thestringmodulecontainssupportforasimpletemplatingapproachbaseduponregularexpressions,viastring.
Template. Thisoffersyetanotherwaytosubstitutevaluesintostrings,usingplaceholderslike$xandreplacingthem
withvaluesfromadictionary. Thissyntaxiseasytouse,althoughitoffersmuchlesscontrolforformatting.
7.1.1 Formatted String Literals
Formattedstringliterals(alsocalledf-stringsforshort)letyouincludethevalueofPythonexpressionsinsideastring
byprefixingthestringwithforFandwritingexpressionsas{expression}.
Anoptionalformatspecifiercanfollowtheexpression. Thisallowsgreatercontroloverhowthevalueisformatted.
Thefollowingexampleroundspitothreeplacesafterthedecimal:
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
Passinganintegerafterthe':' willcausethatfieldtobeaminimumnumberofcharacterswide. Thisisusefulfor
makingcolumnslineup.
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
... print(f'{name:10} ==> {phone:10d}')
...
Sjoerd ==> 4127
Jack ==> 4098
Dcab ==> 7678
Othermodifierscanbeusedtoconvertthevaluebeforeitisformatted. '!a'appliesascii(),'!s'appliesstr(),
and'!r'appliesrepr():
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
54 Chapter7. InputandOutput

### 第61页

The=specifiercanbeusedtoexpandanexpressiontothetextoftheexpression,anequalsign,thentherepresentation
oftheevaluatedexpression:
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
Seeself-documentingexpressionsformoreinformationonthe=specifier. Forareferenceontheseformatspecifi-
cations,seethereferenceguidefortheformatspec.
7.1.2 The String format() Method
Basicusageofthestr.format()methodlookslikethis:
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
The brackets and characters within them (called format fields) are replaced with the objects passed into the str.
format() method. A number in the brackets can be used to refer to the position of the object passed into the
str.format()method.
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
Ifkeywordargumentsareusedinthestr.format()method,theirvaluesarereferredtobyusingthenameofthe
argument.
>>> print('This {food} is {adjective}.'.format(
... food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
Positionalandkeywordargumentscanbearbitrarilycombined:
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
... other='Georg'))
The story of Bill, Manfred, and Georg.
If you have a really long format string that you don’t want to split up, it would be nice if you could reference the
variables to be formatted by name instead of by position. This can be done by simply passing the dict and using
squarebrackets'[]'toaccessthekeys.
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
... 'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
Thiscouldalsobedonebypassingthetabledictionaryaskeywordargumentswiththe**notation.
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
Thisisparticularlyusefulincombinationwiththebuilt-infunctionvars(),whichreturnsadictionarycontaining
alllocalvariables:
7.1. FancierOutputFormatting 55

### 第62页

>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...
Asanexample,thefollowinglinesproduceatidilyalignedsetofcolumnsgivingintegersandtheirsquaresandcubes:
>>> for x in range(1, 11):
... print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
Foracompleteoverviewofstringformattingwithstr.format(),seeformatstrings.
7.1.3 Manual String Formatting
Here’sthesametableofsquaresandcubes,formattedmanually:
>>> for x in range(1, 11):
... print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
... # Note use of 'end' on previous line
... print(repr(x*x*x).rjust(4))
...
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
10 100 1000
(Notethattheonespacebetweeneachcolumnwasaddedbythewayprint()works: italwaysaddsspacesbetween
itsarguments.)
Thestr.rjust()methodofstringobjectsright-justifiesastringinafieldofagivenwidthbypaddingitwithspaces
ontheleft. Therearesimilarmethodsstr.ljust()andstr.center(). Thesemethodsdonotwriteanything,
theyjustreturnanewstring. Iftheinputstringistoolong,theydon’ttruncateit,butreturnitunchanged;thiswill
messupyourcolumnlay-outbutthat’susuallybetterthanthealternative, whichwouldbelyingaboutavalue. (If
youreallywanttruncationyoucanalwaysaddasliceoperation,asinx.ljust(n)[:n].)
Thereisanothermethod,str.zfill(),whichpadsanumericstringontheleftwithzeros. Itunderstandsabout
plusandminussigns:
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
(continuesonnextpage)
56 Chapter7. InputandOutput

### 第63页

(continuedfrompreviouspage)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
7.1.4 Old string formatting
The % operator (modulo) can also be used for string formatting. Given format % values (where format is a
string), %conversionspecificationsinformat arereplacedwithzeroormoreelementsofvalues. Thisoperationis
commonlyknownasstringinterpolation. Forexample:
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
Moreinformationcanbefoundintheold-string-formattingsection.
7.2 Reading and Writing Files
open()returnsafileobject,andismostcommonlyusedwithtwopositionalargumentsandonekeywordargument:
open(filename, mode, encoding=None)
>>> f = open('workfile', 'w', encoding="utf-8")
The first argument is a string containing the filename. The second argument is another string containing a few
charactersdescribingthewayinwhichthefilewillbeused. modecanbe'r'whenthefilewillonlyberead,'w'
foronlywriting(anexistingfilewiththesamenamewillbeerased),and'a'opensthefileforappending;anydata
written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode
argumentisoptional;'r'willbeassumedifit’somitted.
Normally,filesareopenedintextmode,thatmeans,youreadandwritestringsfromandtothefile,whichareencoded
inaspecificencoding. Ifencodingisnotspecified,thedefaultisplatformdependent(seeopen()). BecauseUTF-
8isthemodernde-factostandard, encoding="utf-8"isrecommendedunlessyouknowthatyouneedtousea
differentencoding. Appendinga'b'tothemodeopensthefileinbinarymode. Binarymodedataisreadandwritten
asbytesobjects. Youcannotspecifyencodingwhenopeningfileinbinarymode.
Intextmode,thedefaultwhenreadingistoconvertplatform-specificlineendings(\nonUnix,\r\nonWindows)
to just \n. When writing in text mode, the default is to convert occurrences of \n back to platform-specific line
endings. Thisbehind-the-scenesmodificationtofiledataisfinefortextfiles,butwillcorruptbinarydatalikethatin
JPEGorEXEfiles. Beverycarefultousebinarymodewhenreadingandwritingsuchfiles.
Itisgoodpracticetousethewithkeywordwhendealingwithfileobjects. Theadvantageisthatthefileisproperly
closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than
writingequivalenttry-finallyblocks:
>>> with open('workfile', encoding="utf-8") as f:
... read_data = f.read()
>>> # We can check that the file has been automatically closed.
>>> f.closed
True
Ifyou’renotusingthewithkeyword,thenyoushouldcallf.close()toclosethefileandimmediatelyfreeupany
systemresourcesusedbyit.
(cid:193) Warning
7.2. ReadingandWritingFiles 57

### 第64页

Callingf.write()withoutusingthewithkeywordorcallingf.close()mightresultintheargumentsof
f.write()notbeingcompletelywrittentothedisk,eveniftheprogramexitssuccessfully.
Afterafileobjectisclosed,eitherbyawithstatementorbycallingf.close(),attemptstousethefileobjectwill
automaticallyfail.
>>> f.close()
>>> f.read()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
7.2.1 Methods of File Objects
Therestoftheexamplesinthissectionwillassumethatafileobjectcalledfhasalreadybeencreated.
Toreadafile’scontents, callf.read(size), whichreadssomequantityofdataandreturnsitasastring(intext
mode)orbytesobject(inbinarymode). sizeisanoptionalnumericargument. Whensizeisomittedornegative,the
entirecontentsofthefilewillbereadandreturned; it’syourproblemifthefileistwiceaslargeasyourmachine’s
memory. Otherwise,atmostsizecharacters(intextmode)orsizebytes(inbinarymode)arereadandreturned. If
theendofthefilehasbeenreached,f.read()willreturnanemptystring('').
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
f.readline()readsasinglelinefromthefile;anewlinecharacter(\n)isleftattheendofthestring,andisonly
omittedonthelastlineofthefileifthefiledoesn’tendinanewline. Thismakesthereturnvalueunambiguous;if
f.readline()returnsanemptystring,theendofthefilehasbeenreached,whileablanklineisrepresentedby
'\n',astringcontainingonlyasinglenewline.
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple
code:
>>> for line in f:
... print(line, end='')
...
This is the first line of the file.
Second line of the file
Ifyouwanttoreadallthelinesofafileinalistyoucanalsouselist(f)orf.readlines().
f.write(string)writesthecontentsofstringtothefile,returningthenumberofcharacterswritten.
>>> f.write('This is a test\n')
15
Othertypesofobjectsneedtobeconverted–eithertoastring(intextmode)orabytesobject(inbinarymode)–
beforewritingthem:
58 Chapter7. InputandOutput

### 第65页

>>> value = ('the answer', 42)
>>> s = str(value) # convert the tuple to string
>>> f.write(s)
18
f.tell()returnsanintegergivingthefileobject’scurrentpositioninthefilerepresentedasnumberofbytesfrom
thebeginningofthefilewheninbinarymodeandanopaquenumberwhenintextmode.
Tochangethefileobject’sposition,usef.seek(offset, whence). Thepositioniscomputedfromaddingoffset
toareferencepoint;thereferencepointisselectedbythewhenceargument. Awhencevalueof0measuresfromthe
beginningofthefile,1usesthecurrentfileposition,and2usestheendofthefileasthereferencepoint. whencecan
beomittedanddefaultsto0,usingthebeginningofthefileasthereferencepoint.
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5) # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
Intextfiles(thoseopenedwithoutabinthemodestring),onlyseeksrelativetothebeginningofthefileareallowed
(theexceptionbeingseekingtotheveryfileendwithseek(0, 2))andtheonlyvalidoffsetvaluesarethosereturned
fromthef.tell(),orzero. Anyotheroffsetvalueproducesundefinedbehaviour.
File objects have some additional methods, such as isatty() and truncate() which are less frequently used;
consulttheLibraryReferenceforacompleteguidetofileobjects.
7.2.2 Saving structured data with json
Stringscaneasilybewrittentoandreadfromafile. Numberstakeabitmoreeffort,sincetheread()methodonly
returnsstrings,whichwillhavetobepassedtoafunctionlikeint(),whichtakesastringlike'123'andreturnsits
numericvalue123. Whenyouwanttosavemorecomplexdatatypeslikenestedlistsanddictionaries,parsingand
serializingbyhandbecomescomplicated.
Ratherthanhavingusersconstantlywritinganddebuggingcodetosavecomplicateddatatypestofiles,Pythonallows
youtousethepopulardatainterchangeformatcalledJSON(JavaScriptObjectNotation). Thestandardmodulecalled
jsoncantakePythondatahierarchies,andconvertthemtostringrepresentations;thisprocessiscalledserializing.
Reconstructingthedatafromthestringrepresentationiscalleddeserializing. Betweenserializinganddeserializing,
thestringrepresentingtheobjectmayhavebeenstoredinafileordata,orsentoveranetworkconnectiontosome
distantmachine.
(cid:174) Note
TheJSONformatiscommonlyusedbymodernapplicationstoallowfordataexchange. Manyprogrammersare
alreadyfamiliarwithit,whichmakesitagoodchoiceforinteroperability.
Ifyouhaveanobjectx,youcanviewitsJSONstringrepresentationwithasimplelineofcode:
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
7.2. ReadingandWritingFiles 59

### 第66页

Anothervariantofthedumps()function,calleddump(),simplyserializestheobjecttoatextfile. Soiffisatext
fileobjectopenedforwriting,wecandothis:
json.dump(x, f)
Todecodetheobjectagain,iffisabinaryfileortextfileobjectwhichhasbeenopenedforreading:
x = json.load(f)
(cid:174) Note
JSONfilesmustbeencodedinUTF-8. Useencoding="utf-8"whenopeningJSONfileasatextfileforboth
ofreadingandwriting.
Thissimpleserializationtechniquecanhandlelistsanddictionaries,butserializingarbitraryclassinstancesinJSON
requiresabitofextraeffort. Thereferenceforthejsonmodulecontainsanexplanationofthis.
(cid:181) Seealso
pickle-thepicklemodule
ContrarytoJSON,pickleisaprotocolwhichallowstheserializationofarbitrarilycomplexPythonobjects. As
such,itisspecifictoPythonandcannotbeusedtocommunicatewithapplicationswritteninotherlanguages. It
isalsoinsecurebydefault: deserializingpickledatacomingfromanuntrustedsourcecanexecutearbitrarycode,
ifthedatawascraftedbyaskilledattacker.
60 Chapter7. InputandOutput

| (cid:181) Seealso |
| --- |
| pickle-thepicklemodule
ContrarytoJSON,pickleisaprotocolwhichallowstheserializationofarbitrarilycomplexPythonobjects. As
such,itisspecifictoPythonandcannotbeusedtocommunicatewithapplicationswritteninotherlanguages. It
isalsoinsecurebydefault: deserializingpickledatacomingfromanuntrustedsourcecanexecutearbitrarycode,
ifthedatawascraftedbyaskilledattacker. |

### 第67页

CHAPTER
EIGHT
ERRORS AND EXCEPTIONS
Untilnowerrormessageshaven’tbeenmorethanmentioned,butifyouhavetriedouttheexamplesyouhaveprobably
seensome. Thereare(atleast)twodistinguishablekindsoferrors: syntaxerrorsandexceptions.
8.1 Syntax Errors
Syntaxerrors,alsoknownasparsingerrors,areperhapsthemostcommonkindofcomplaintyougetwhileyouare
stilllearningPython:
>>> while True print('Hello world')
File "<stdin>", line 1
while True print('Hello world')
^^^^^
SyntaxError: invalid syntax
Theparserrepeatstheoffendinglineanddisplayslittlearrows pointingattheplacewheretheerrorwasdetected.
Note that this is not always the place that needs to be fixed. In the example, the error is detected at the function
print(),sinceacolon(':') ismissingjustbeforeit.
Thefilename(<stdin>inourexample)andlinenumberareprintedsoyouknowwheretolookincasetheinput
camefromafile.
8.2 Exceptions
Evenifastatementorexpressionissyntacticallycorrect,itmaycauseanerrorwhenanattemptismadetoexecute
it. Errorsdetectedduringexecutionarecalledexceptionsandarenotunconditionallyfatal: youwillsoonlearnhow
to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error
messagesasshownhere:
>>> 10 * (1/0)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
10 * (1/0)
~^~
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
4 + spam*3
^^^^
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
'2' + 2
(continuesonnextpage)
61

### 第68页

(continuedfrompreviouspage)
~~~~^~~
TypeError: can only concatenate str (not "int") to str
The last line of the error message indicates what happened. Exceptions come in different types, and the type is
printedaspartofthemessage: thetypesintheexampleareZeroDivisionError,NameErrorandTypeError.
Thestringprintedastheexceptiontypeisthenameofthebuilt-inexceptionthatoccurred. Thisistrueforallbuilt-in
exceptions,butneednotbetrueforuser-definedexceptions(althoughitisausefulconvention). Standardexception
namesarebuilt-inidentifiers(notreservedkeywords).
Therestofthelineprovidesdetailbasedonthetypeofexceptionandwhatcausedit.
The preceding part of the error message shows the context where the exception occurred, in the form of a stack
traceback. Ingeneralitcontainsastacktracebacklistingsourcelines; however, itwillnotdisplaylinesreadfrom
standardinput.
bltin-exceptionsliststhebuilt-inexceptionsandtheirmeanings.
8.3 Handling Exceptions
It is possible to write programs that handle selected exceptions. Look at the following example, which asks the
userforinputuntilavalidintegerhasbeenentered,butallowstheusertointerrupttheprogram(usingControl-
C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the
KeyboardInterruptexception.
>>> while True:
... try:
... x = int(input("Please enter a number: "))
... break
... except ValueError:
... print("Oops! That was no valid number. Try again...")
...
Thetrystatementworksasfollows.
• First,thetryclause(thestatement(s)betweenthetryandexceptkeywords)isexecuted.
• Ifnoexceptionoccurs,theexceptclauseisskippedandexecutionofthetrystatementisfinished.
• Ifanexceptionoccursduringexecutionofthetryclause,therestoftheclauseisskipped. Then,ifitstype
matches the exception named after the except keyword, the except clause is executed, and then execution
continuesafterthetry/exceptblock.
• Ifanexceptionoccurswhichdoesnotmatchtheexceptionnamedintheexceptclause,itispassedontoouter
trystatements;ifnohandlerisfound,itisanunhandledexceptionandexecutionstopswithanerrormessage.
A try statement may have morethan one except clause, to specify handlers fordifferent exceptions. Atmost one
handlerwillbeexecuted. Handlersonlyhandleexceptionsthatoccurinthecorrespondingtryclause, notinother
handlersofthesametrystatement. Anexceptclausemaynamemultipleexceptionsasaparenthesizedtuple, for
example:
... except (RuntimeError, TypeError, NameError):
... pass
Aclassinanexceptclausematchesexceptionswhichareinstancesoftheclassitselforoneofitsderivedclasses
(butnottheotherwayaround—anexceptclauselistingaderivedclassdoesnotmatchinstancesofitsbaseclasses).
Forexample,thefollowingcodewillprintB,C,Dinthatorder:
class B(Exception):
pass
(continuesonnextpage)
62 Chapter8. ErrorsandExceptions

### 第69页

(continuedfrompreviouspage)
class C(B):
pass
class D(C):
pass
for cls in [B, C, D]:
try:
raise cls()
except D:
print("D")
except C:
print("C")
except B:
print("B")
Notethatiftheexceptclauseswerereversed(withexcept Bfirst),itwouldhaveprintedB,B,B—thefirstmatching
exceptclauseistriggered.
When an exception occurs, it may have associated values, also known as the exception’s arguments. The presence
andtypesoftheargumentsdependontheexceptiontype.
Theexceptclausemayspecifyavariableaftertheexceptionname. Thevariableisboundtotheexceptioninstance
which typically has an args attribute that stores the arguments. For convenience, builtin exception types define
__str__()toprintalltheargumentswithoutexplicitlyaccessing.args.
>>> try:
... raise Exception('spam', 'eggs')
... except Exception as inst:
... print(type(inst)) # the exception type
... print(inst.args) # arguments stored in .args
... print(inst) # __str__ allows args to be printed directly,
... # but may be overridden in exception subclasses
... x, y = inst.args # unpack args
... print('x =', x)
... print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
Theexception’s__str__()outputisprintedasthelastpart(‘detail’)ofthemessageforunhandledexceptions.
BaseExceptionisthecommonbaseclassofallexceptions. Oneofitssubclasses,Exception,isthebaseclassof
allthenon-fatalexceptions. ExceptionswhicharenotsubclassesofExceptionarenottypicallyhandled,because
they are used to indicate that the program should terminate. They include SystemExit which is raised by sys.
exit()andKeyboardInterruptwhichisraisedwhenauserwishestointerrupttheprogram.
Exceptioncanbeusedasawildcardthatcatches(almost)everything. However,itisgoodpracticetobeasspecific
aspossiblewiththetypesofexceptionsthatweintendtohandle,andtoallowanyunexpectedexceptionstopropagate
on.
ThemostcommonpatternforhandlingExceptionistoprintorlogtheexceptionandthenre-raiseit(allowinga
callertohandletheexceptionaswell):
import sys
(continuesonnextpage)
8.3. HandlingExceptions 63

### 第70页

(continuedfrompreviouspage)
try:
f = open('myfile.txt')
s = f.readline()
i = int(s.strip())
except OSError as err:
print("OS error:", err)
except ValueError:
print("Could not convert data to an integer.")
except Exception as err:
print(f"Unexpected {err=}, {type(err)=}")
raise
Thetry…exceptstatementhasanoptionalelseclause,which,whenpresent,mustfollowallexceptclauses. Itis
usefulforcodethatmustbeexecutedifthetryclausedoesnotraiseanexception. Forexample:
for arg in sys.argv[1:]:
try:
f = open(arg, 'r')
except OSError:
print('cannot open', arg)
else:
print(arg, 'has', len(f.readlines()), 'lines')
f.close()
The use of the else clause is better than adding additional code to the try clause because it avoids accidentally
catchinganexceptionthatwasn’traisedbythecodebeingprotectedbythetry…exceptstatement.
Exceptionhandlersdonothandleonlyexceptionsthatoccurimmediatelyinthetryclause,butalsothosethatoccur
insidefunctionsthatarecalled(evenindirectly)inthetryclause. Forexample:
>>> def this_fails():
... x = 1/0
...
>>> try:
... this_fails()
... except ZeroDivisionError as err:
... print('Handling run-time error:', err)
...
Handling run-time error: division by zero
8.4 Raising Exceptions
Theraisestatementallowstheprogrammertoforceaspecifiedexceptiontooccur. Forexample:
>>> raise NameError('HiThere')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
raise NameError('HiThere')
NameError: HiThere
Thesoleargumenttoraiseindicatestheexceptiontoberaised. Thismustbeeitheranexceptioninstanceoran
exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an
exceptionclassispassed,itwillbeimplicitlyinstantiatedbycallingitsconstructorwithnoarguments:
raise ValueError # shorthand for 'raise ValueError()'
64 Chapter8. ErrorsandExceptions

### 第71页

Ifyouneedtodeterminewhetheranexceptionwasraisedbutdon’tintendtohandleit,asimplerformoftheraise
statementallowsyoutore-raisetheexception:
>>> try:
... raise NameError('HiThere')
... except NameError:
... print('An exception flew by!')
... raise
...
An exception flew by!
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
raise NameError('HiThere')
NameError: HiThere
8.5 Exception Chaining
Ifanunhandledexceptionoccursinsideanexceptsection,itwillhavetheexceptionbeinghandledattachedtoit
andincludedintheerrormessage:
>>> try:
... open("database.sqlite")
... except OSError:
... raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
open("database.sqlite")
~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error
Toindicatethatanexceptionisadirectconsequenceofanother,theraisestatementallowsanoptionalfromclause:
# exc must be exception instance or None.
raise RuntimeError from exc
Thiscanbeusefulwhenyouaretransformingexceptions. Forexample:
>>> def func():
... raise ConnectionError
...
>>> try:
... func()
... except ConnectionError as exc:
... raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
func()
~~~~^^
(continuesonnextpage)
8.5. ExceptionChaining 65

### 第72页

(continuedfrompreviouspage)
File "<stdin>", line 2, in func
ConnectionError
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
Italsoallowsdisablingautomaticexceptionchainingusingthefrom Noneidiom:
>>> try:
... open('database.sqlite')
... except OSError:
... raise RuntimeError from None
...
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
raise RuntimeError from None
RuntimeError
Formoreinformationaboutchainingmechanics,seebltin-exceptions.
8.6 User-defined Exceptions
Programs may name their own exceptions by creating a new exception class (see Classes for more about Python
classes). ExceptionsshouldtypicallybederivedfromtheExceptionclass,eitherdirectlyorindirectly.
Exceptionclassescanbedefinedwhichdoanythinganyotherclasscando,butareusuallykeptsimple,oftenonly
offeringanumberofattributesthatallowinformationabouttheerrortobeextractedbyhandlersfortheexception.
Mostexceptionsaredefinedwithnamesthatendin“Error”,similartothenamingofthestandardexceptions.
Manystandardmodulesdefinetheirownexceptionstoreporterrorsthatmayoccurinfunctionstheydefine.
8.7 Defining Clean-up Actions
Thetrystatementhasanotheroptionalclausewhichisintendedtodefineclean-upactionsthatmustbeexecuted
underallcircumstances. Forexample:
>>> try:
... raise KeyboardInterrupt
... finally:
... print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
raise KeyboardInterrupt
KeyboardInterrupt
Ifafinallyclauseispresent,thefinallyclausewillexecuteasthelasttaskbeforethetrystatementcompletes.
The finally clause runs whether or not the try statement produces an exception. The following points discuss
morecomplexcaseswhenanexceptionoccurs:
• Ifanexceptionoccursduringexecutionofthetryclause,theexceptionmaybehandledbyanexceptclause.
Iftheexceptionisnothandledbyanexceptclause,theexceptionisre-raisedafterthefinallyclausehas
66 Chapter8. ErrorsandExceptions

### 第73页

beenexecuted.
• Anexceptioncouldoccurduringexecutionofanexceptorelseclause. Again,theexceptionisre-raised
afterthefinallyclausehasbeenexecuted.
• Ifthefinallyclauseexecutesabreak,continueorreturnstatement,exceptionsarenotre-raised. This
canbeconfusingandisthereforediscouraged. Fromversion3.14thecompileremitsaSyntaxWarningfor
it(seePEP765).
• Ifthetrystatementreachesabreak,continueorreturnstatement,thefinallyclausewillexecutejust
priortothebreak,continueorreturnstatement’sexecution.
• If a finally clause includes a return statement, the returned value will be the one from the finally
clause’sreturnstatement,notthevaluefromthetryclause’sreturnstatement. Thiscanbeconfusingand
isthereforediscouraged. Fromversion3.14thecompileremitsaSyntaxWarningforit(seePEP765).
Forexample:
>>> def bool_return():
... try:
... return True
... finally:
... return False
...
>>> bool_return()
False
Amorecomplicatedexample:
>>> def divide(x, y):
... try:
... result = x / y
... except ZeroDivisionError:
... print("division by zero!")
... else:
... print("result is", result)
... finally:
... print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
divide("2", "1")
~~~~~~^^^^^^^^^^
File "<stdin>", line 3, in divide
result = x / y
~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
Asyoucansee,thefinallyclauseisexecutedinanyevent. TheTypeErrorraisedbydividingtwostringsisnot
handledbytheexceptclauseandthereforere-raisedafterthefinallyclausehasbeenexecuted.
In real world applications, the finally clause is useful for releasing external resources (such as files or network
connections),regardlessofwhethertheuseoftheresourcewassuccessful.
8.7. DefiningClean-upActions 67

### 第74页

8.8 Predefined Clean-up Actions
Someobjectsdefinestandardclean-upactionstobeundertakenwhentheobjectisnolongerneeded,regardlessof
whetherornottheoperationusingtheobjectsucceededorfailed. Lookatthefollowingexample,whichtriestoopen
afileandprintitscontentstothescreen.
for line in open("myfile.txt"):
print(line, end="")
Theproblemwiththiscodeisthatitleavesthefileopenforanindeterminateamountoftimeafterthispartofthe
codehasfinishedexecuting. Thisisnotanissueinsimplescripts,butcanbeaproblemforlargerapplications. The
with statementallowsobjectslikefilesto be used ina waythatensuresthey arealwayscleaneduppromptlyand
correctly.
with open("myfile.txt") as f:
for line in f:
print(line, end="")
Afterthestatementisexecuted,thefilef isalwaysclosed,evenifaproblemwasencounteredwhileprocessingthe
lines. Objectswhich,likefiles,providepredefinedclean-upactionswillindicatethisintheirdocumentation.
8.9 Raising and Handling Multiple Unrelated Exceptions
Therearesituationswhereitisnecessarytoreportseveralexceptionsthathaveoccurred. Thisisoftenthecasein
concurrencyframeworks,whenseveraltasksmayhavefailedinparallel,buttherearealsootherusecaseswhereit
isdesirabletocontinueexecutionandcollectmultipleerrorsratherthanraisethefirstexception.
ThebuiltinExceptionGroupwrapsalistofexceptioninstancessothattheycanberaisedtogether. Itisanexception
itself,soitcanbecaughtlikeanyotherexception.
>>> def f():
... excs = [OSError('error 1'), SystemError('error 2')]
... raise ExceptionGroup('there were problems', excs)
...
>>> f()
+ Exception Group Traceback (most recent call last):
| File "<stdin>", line 1, in <module>
| f()
| ~^^
| File "<stdin>", line 3, in f
| raise ExceptionGroup('there were problems', excs)
| ExceptionGroup: there were problems (2 sub-exceptions)
+-+---------------- 1 ----------------
| OSError: error 1
+---------------- 2 ----------------
| SystemError: error 2
+------------------------------------
>>> try:
... f()
... except Exception as e:
... print(f'caught {type(e)}: e')
...
caught <class 'ExceptionGroup'>: e
>>>
Byusingexcept*insteadofexcept,wecanselectivelyhandleonlytheexceptionsinthegroupthatmatchacertain
type. Inthefollowingexample,whichshowsanestedexceptiongroup,eachexcept*clauseextractsfromthegroup
exceptionsofacertaintypewhilelettingallotherexceptionspropagatetootherclausesandeventuallytobereraised.
68 Chapter8. ErrorsandExceptions

### 第75页

>>> def f():
... raise ExceptionGroup(
... "group1",
... [
... OSError(1),
... SystemError(2),
... ExceptionGroup(
... "group2",
... [
... OSError(3),
... RecursionError(4)
... ]
... )
... ]
... )
...
>>> try:
... f()
... except* OSError as e:
... print("There were OSErrors")
... except* SystemError as e:
... print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
+ Exception Group Traceback (most recent call last):
| File "<stdin>", line 2, in <module>
| f()
| ~^^
| File "<stdin>", line 2, in f
| raise ExceptionGroup(
| ...<12 lines>...
| )
| ExceptionGroup: group1 (1 sub-exception)
+-+---------------- 1 ----------------
| ExceptionGroup: group2 (1 sub-exception)
+-+---------------- 1 ----------------
| RecursionError: 4
+------------------------------------
>>>
Notethattheexceptionsnestedinanexceptiongroupmustbeinstances,nottypes. Thisisbecauseinpracticethe
exceptions would typically be ones that have already been raised and caught by the program, along the following
pattern:
>>> excs = []
... for test in tests:
... try:
... test.run()
... except Exception as e:
... excs.append(e)
...
>>> if excs:
... raise ExceptionGroup("Test Failures", excs)
...
8.9. RaisingandHandlingMultipleUnrelatedExceptions 69

### 第76页

8.10 Enriching Exceptions with Notes
Whenanexceptioniscreatedinordertoberaised,itisusuallyinitializedwithinformationthatdescribestheerror
that has occurred. There are cases where it is useful to add information after the exception was caught. For this
purpose,exceptionshaveamethodadd_note(note)thatacceptsastringandaddsittotheexception’snoteslist.
Thestandardtracebackrenderingincludesallnotes,intheordertheywereadded,aftertheexception.
>>> try:
... raise TypeError('bad type')
... except Exception as e:
... e.add_note('Add some information')
... e.add_note('Add some more information')
... raise
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
raise TypeError('bad type')
TypeError: bad type
Add some information
Add some more information
>>>
Forexample, whencollectingexceptionsintoanexceptiongroup, wemaywanttoaddcontextinformationforthe
individualerrors. Inthefollowingeachexceptioninthegrouphasanoteindicatingwhenthiserrorhasoccurred.
>>> def f():
... raise OSError('operation failed')
...
>>> excs = []
>>> for i in range(3):
... try:
... f()
... except Exception as e:
... e.add_note(f'Happened in Iteration {i+1}')
... excs.append(e)
...
>>> raise ExceptionGroup('We have some problems', excs)
+ Exception Group Traceback (most recent call last):
| File "<stdin>", line 1, in <module>
| raise ExceptionGroup('We have some problems', excs)
| ExceptionGroup: We have some problems (3 sub-exceptions)
+-+---------------- 1 ----------------
| Traceback (most recent call last):
| File "<stdin>", line 3, in <module>
| f()
| ~^^
| File "<stdin>", line 2, in f
| raise OSError('operation failed')
| OSError: operation failed
| Happened in Iteration 1
+---------------- 2 ----------------
| Traceback (most recent call last):
| File "<stdin>", line 3, in <module>
| f()
| ~^^
| File "<stdin>", line 2, in f
| raise OSError('operation failed')
| OSError: operation failed
(continuesonnextpage)
70 Chapter8. ErrorsandExceptions

### 第77页

(continuedfrompreviouspage)
| Happened in Iteration 2
+---------------- 3 ----------------
| Traceback (most recent call last):
| File "<stdin>", line 3, in <module>
| f()
| ~^^
| File "<stdin>", line 2, in f
| raise OSError('operation failed')
| OSError: operation failed
| Happened in Iteration 3
+------------------------------------
>>>
8.10. EnrichingExceptionswithNotes 71

### 第78页

72 Chapter8. ErrorsandExceptions

### 第79页

CHAPTER
NINE
CLASSES
Classesprovideameansofbundlingdataandfunctionalitytogether. Creatinganewclasscreatesanewtypeofobject,
allowingnewinstancesofthattypetobemade. Eachclassinstancecanhaveattributesattachedtoitformaintaining
itsstate. Classinstancescanalsohavemethods(definedbyitsclass)formodifyingitsstate.
Comparedwithotherprogramminglanguages,Python’sclassmechanismaddsclasseswithaminimumofnewsyntax
andsemantics. ItisamixtureoftheclassmechanismsfoundinC++andModula-3. Pythonclassesprovideallthe
standardfeaturesofObjectOrientedProgramming: theclassinheritancemechanismallowsmultiplebaseclasses,a
derivedclasscanoverrideanymethodsofitsbaseclassorclasses,andamethodcancallthemethodofabaseclass
withthesamename. Objectscancontainarbitraryamountsandkindsofdata. Asistrueformodules,classespartake
ofthedynamicnatureofPython: theyarecreatedatruntime,andcanbemodifiedfurtheraftercreation.
In C++ terminology, normally class members (including the data members) are public (except see below Private
Variables),andallmemberfunctionsarevirtual. AsinModula-3,therearenoshorthandsforreferencingtheobject’s
membersfromitsmethods: themethodfunctionisdeclaredwithanexplicitfirstargumentrepresentingtheobject,
whichisprovidedimplicitlybythecall. AsinSmalltalk,classesthemselvesareobjects. Thisprovidessemanticsfor
importingandrenaming. UnlikeC++andModula-3,built-intypescanbeusedasbaseclassesforextensionbythe
user. Also,likeinC++,mostbuilt-inoperatorswithspecialsyntax(arithmeticoperators,subscriptingetc.) canbe
redefinedforclassinstances.
(Lacking universally accepted terminology to talk about classes, I will make occasional use of Smalltalk and C++
terms. IwoulduseModula-3terms,sinceitsobject-orientedsemanticsareclosertothoseofPythonthanC++,but
Iexpectthatfewreadershaveheardofit.)
9.1 A Word About Names and Objects
Objectshaveindividuality,andmultiplenames(inmultiplescopes)canbeboundtothesameobject. Thisisknown
asaliasinginotherlanguages. ThisisusuallynotappreciatedonafirstglanceatPython,andcanbesafelyignored
whendealingwithimmutablebasictypes(numbers,strings,tuples). However,aliasinghasapossiblysurprisingeffect
onthesemanticsofPythoncodeinvolvingmutableobjectssuchaslists,dictionaries,andmostothertypes. Thisis
usuallyusedtothebenefitoftheprogram,sincealiasesbehavelikepointersinsomerespects. Forexample,passing
anobjectischeapsinceonlyapointerispassedbytheimplementation;andifafunctionmodifiesanobjectpassedas
anargument,thecallerwillseethechange—thiseliminatestheneedfortwodifferentargumentpassingmechanisms
asinPascal.
9.2 Python Scopes and Namespaces
Beforeintroducingclasses,IfirsthavetotellyousomethingaboutPython’sscoperules. Classdefinitionsplaysome
neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what’s
goingon. Incidentally,knowledgeaboutthissubjectisusefulforanyadvancedPythonprogrammer.
Let’sbeginwithsomedefinitions.
Anamespaceisamappingfromnamestoobjects. MostnamespacesarecurrentlyimplementedasPythondictionar-
ies,butthat’snormallynotnoticeableinanyway(exceptforperformance),anditmaychangeinthefuture. Examples
of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names);
the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an
73

### 第80页

objectalsoformanamespace. Theimportantthingtoknowaboutnamespacesisthatthereisabsolutelynorelation
betweennamesindifferentnamespaces;forinstance,twodifferentmodulesmaybothdefineafunctionmaximize
withoutconfusion—usersofthemodulesmustprefixitwiththemodulename.
Bytheway,Iusethewordattributeforanynamefollowingadot—forexample,intheexpressionz.real,real
is an attribute of the object z. Strictly speaking, references to names in modules are attribute references: in the
expressionmodname.funcname,modnameisamoduleobjectandfuncnameisanattributeofit. Inthiscasethere
happenstobeastraightforwardmappingbetweenthemodule’sattributesandtheglobalnamesdefinedinthemodule:
theysharethesamenamespace!1
Attributesmayberead-onlyorwritable. Inthelattercase,assignmenttoattributesispossible. Moduleattributesare
writable: youcanwritemodname.the_answer = 42. Writableattributesmayalsobedeletedwiththedelstate-
ment. Forexample, del modname.the_answerwillremovetheattributethe_answerfromtheobjectnamed
bymodname.
Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in
names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module
iscreatedwhenthemoduledefinitionisreadin; normally, modulenamespacesalsolastuntiltheinterpreterquits.
Thestatementsexecutedbythetop-levelinvocationoftheinterpreter,eitherreadfromascriptfileorinteractively,
areconsideredpartofamodulecalled__main__, sotheyhavetheirownglobalnamespace. (Thebuilt-innames
actuallyalsoliveinamodule;thisiscalledbuiltins.)
Thelocalnamespaceforafunctioniscreatedwhenthefunctioniscalled,anddeletedwhenthefunctionreturnsor
raisesanexceptionthatisnothandledwithinthefunction. (Actually,forgettingwouldbeabetterwaytodescribe
whatactuallyhappens.) Ofcourse,recursiveinvocationseachhavetheirownlocalnamespace.
AscopeisatextualregionofaPythonprogramwhereanamespaceisdirectlyaccessible. “Directlyaccessible”here
meansthatanunqualifiedreferencetoanameattemptstofindthenameinthenamespace.
Althoughscopesaredeterminedstatically,theyareuseddynamically. Atanytimeduringexecution,thereare3or4
nestedscopeswhosenamespacesaredirectlyaccessible:
• theinnermostscope,whichissearchedfirst,containsthelocalnames
• the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain
non-local,butalsonon-globalnames
• thenext-to-lastscopecontainsthecurrentmodule’sglobalnames
• theoutermostscope(searchedlast)isthenamespacecontainingbuilt-innames
Ifanameisdeclaredglobal,thenallreferencesandassignmentsgodirectlytothenext-to-lastscopecontainingthe
module’sglobalnames. Torebindvariablesfoundoutsideoftheinnermostscope,thenonlocalstatementcanbe
used;ifnotdeclarednonlocal,thosevariablesareread-only(anattempttowritetosuchavariablewillsimplycreate
anewlocalvariableintheinnermostscope,leavingtheidenticallynamedoutervariableunchanged).
Usually, thelocalscopereferencesthelocalnamesofthe(textually)currentfunction. Outsidefunctions, thelocal
scopereferencesthesamenamespaceastheglobalscope:themodule’snamespace. Classdefinitionsplaceyetanother
namespaceinthelocalscope.
It is important to realize that scopes are determined textually: the global scope of a function defined in a module
is that module’s namespace, no matter from where or by what alias the function is called. On the other hand, the
actualsearchfornamesisdonedynamically,atruntime—however,thelanguagedefinitionisevolvingtowardsstatic
nameresolution, at“compile”time, sodon’trelyondynamicnameresolution! (Infact, localvariablesarealready
determinedstatically.)
AspecialquirkofPythonisthat–ifnoglobalornonlocalstatementisineffect–assignmentstonamesalways
gointotheinnermostscope. Assignmentsdonotcopydata—theyjustbindnamestoobjects. Thesameistruefor
deletions: thestatementdel xremovesthebindingofxfromthenamespacereferencedbythelocalscope. Infact,
alloperationsthatintroducenewnamesusethelocalscope: inparticular,importstatementsandfunctiondefinitions
bindthemoduleorfunctionnameinthelocalscope.
1Exceptforonething. Moduleobjectshaveasecretread-onlyattributecalled__dict__whichreturnsthedictionaryusedtoimplement
themodule’snamespace;thename__dict__isanattributebutnotaglobalname. Obviously,usingthisviolatestheabstractionofnamespace
implementation,andshouldberestrictedtothingslikepost-mortemdebuggers.
74 Chapter9. Classes

### 第81页

Theglobalstatementcanbeusedtoindicatethatparticularvariablesliveintheglobalscopeandshouldberebound
there;thenonlocalstatementindicatesthatparticularvariablesliveinanenclosingscopeandshouldberebound
there.
9.2.1 Scopes and Namespaces Example
This is an example demonstrating how to reference the different scopes and namespaces, and how global and
nonlocalaffectvariablebinding:
def scope_test():
def do_local():
spam = "local spam"
def do_nonlocal():
nonlocal spam
spam = "nonlocal spam"
def do_global():
global spam
spam = "global spam"
spam = "test spam"
do_local()
print("After local assignment:", spam)
do_nonlocal()
print("After nonlocal assignment:", spam)
do_global()
print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)
Theoutputoftheexamplecodeis:
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
Notehowthelocalassignment(whichisdefault)didn’tchangescope_test’sbindingofspam. Thenonlocalassign-
mentchangedscope_test’sbindingofspam,andtheglobalassignmentchangedthemodule-levelbinding.
Youcanalsoseethattherewasnopreviousbindingforspambeforetheglobalassignment.
9.3 A First Look at Classes
Classesintroducealittlebitofnewsyntax,threenewobjecttypes,andsomenewsemantics.
9.3.1 Class Definition Syntax
Thesimplestformofclassdefinitionlookslikethis:
class ClassName:
<statement-1>
.
.
.
<statement-N>
9.3. AFirstLookatClasses 75

### 第82页

Classdefinitions,likefunctiondefinitions(defstatements)mustbeexecutedbeforetheyhaveanyeffect. (Youcould
conceivablyplaceaclassdefinitioninabranchofanifstatement,orinsideafunction.)
Inpractice, thestatementsinsideaclassdefinitionwillusuallybefunctiondefinitions, butotherstatementsareal-
lowed,andsometimesuseful—we’llcomebacktothislater. Thefunctiondefinitionsinsideaclassnormallyhave
apeculiarformofargumentlist,dictatedbythecallingconventionsformethods—again,thisisexplainedlater.
Whenaclassdefinitionisentered,anewnamespaceiscreated,andusedasthelocalscope—thus,allassignments
tolocalvariablesgointothisnewnamespace. Inparticular,functiondefinitionsbindthenameofthenewfunction
here.
Whenaclassdefinitionisleftnormally(viatheend),aclassobjectiscreated. Thisisbasicallyawrapperaroundthe
contentsofthenamespacecreatedbytheclassdefinition;we’lllearnmoreaboutclassobjectsinthenextsection. The
originallocalscope(theoneineffectjustbeforetheclassdefinitionwasentered)isreinstated,andtheclassobjectis
boundheretotheclassnamegivenintheclassdefinitionheader(ClassNameintheexample).
9.3.2 Class Objects
Classobjectssupporttwokindsofoperations: attributereferencesandinstantiation.
Attributereferences usethestandardsyntaxusedforallattributereferencesinPython: obj.name. Validattribute
namesareallthenamesthatwereintheclass’snamespacewhentheclassobjectwascreated. So,iftheclassdefinition
lookedlikethis:
class MyClass:
"""A simple example class"""
i = 12345
def f(self):
return 'hello world'
thenMyClass.iandMyClass.farevalidattributereferences,returninganintegerandafunctionobject,respec-
tively. Classattributescanalsobeassignedto,soyoucanchangethevalueofMyClass.ibyassignment. __doc__
isalsoavalidattribute,returningthedocstringbelongingtotheclass: "A simple example class".
Classinstantiationusesfunctionnotation. Justpretendthattheclassobjectisaparameterlessfunctionthatreturnsa
newinstanceoftheclass. Forexample(assumingtheaboveclass):
x = MyClass()
createsanewinstanceoftheclassandassignsthisobjecttothelocalvariablex.
Theinstantiationoperation(“calling”aclassobject)createsanemptyobject. Manyclassesliketocreateobjectswith
instancescustomizedtoaspecificinitialstate. Thereforeaclassmaydefineaspecialmethodnamed__init__(),
likethis:
def __init__(self):
self.data = []
Whenaclassdefinesan__init__()method,classinstantiationautomaticallyinvokes__init__()forthenewly
createdclassinstance. Sointhisexample,anew,initializedinstancecanbeobtainedby:
x = MyClass()
Ofcourse,the__init__()methodmayhaveargumentsforgreaterflexibility. Inthatcase,argumentsgiventothe
classinstantiationoperatorarepassedonto__init__(). Forexample,
>>> class Complex:
... def __init__(self, realpart, imagpart):
... self.r = realpart
... self.i = imagpart
(continuesonnextpage)
76 Chapter9. Classes

### 第83页

(continuedfrompreviouspage)
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
9.3.3 Instance Objects
Nowwhatcanwedowithinstanceobjects? Theonlyoperationsunderstoodbyinstanceobjectsareattributerefer-
ences. Therearetwokindsofvalidattributenames: dataattributesandmethods.
Dataattributescorrespondto“instancevariables”inSmalltalk,andto“datamembers”inC++. Dataattributesneed
notbedeclared;likelocalvariables,theyspringintoexistencewhentheyarefirstassignedto. Forexample,ifxis
theinstanceofMyClasscreatedabove,thefollowingpieceofcodewillprintthevalue16,withoutleavingatrace:
x.counter = 1
while x.counter < 10:
x.counter = x.counter * 2
print(x.counter)
del x.counter
Theotherkindofinstanceattributereferenceisamethod. Amethodisafunctionthat“belongsto”anobject.
Validmethodnamesofaninstanceobjectdependonitsclass. Bydefinition,allattributesofaclassthatarefunction
objects define corresponding methods of its instances. So in our example, x.f is a valid method reference, since
MyClass.fisafunction,butx.iisnot,sinceMyClass.iisnot. Butx.fisnotthesamethingasMyClass.f—
itisamethodobject,notafunctionobject.
9.3.4 Method Objects
Usually,amethodiscalledrightafteritisbound:
x.f()
If x = MyClass(), as above, this will return the string 'hello world'. However, it is not necessary to call a
methodrightaway: x.fisamethodobject,andcanbestoredawayandcalledatalatertime. Forexample:
xf = x.f
while True:
print(xf())
willcontinuetoprinthello worlduntiltheendoftime.
Whatexactlyhappenswhenamethodiscalled? Youmayhavenoticedthatx.f()wascalledwithoutanargument
above,eventhoughthefunctiondefinitionforf()specifiedanargument. Whathappenedtotheargument? Surely
Pythonraisesanexceptionwhenafunctionthatrequiresanargumentiscalledwithoutany—eveniftheargument
isn’tactuallyused…
Actually,youmayhaveguessedtheanswer: thespecialthingaboutmethodsisthattheinstanceobjectispassedasthe
firstargumentofthefunction. Inourexample,thecallx.f()isexactlyequivalenttoMyClass.f(x). Ingeneral,
callingamethodwithalistofnargumentsisequivalenttocallingthecorrespondingfunctionwithanargumentlist
thatiscreatedbyinsertingthemethod’sinstanceobjectbeforethefirstargument.
Ingeneral,methodsworkasfollows. Whenanon-dataattributeofaninstanceisreferenced,theinstance’sclassis
searched. Ifthenamedenotesavalidclassattributethatisafunctionobject,referencestoboththeinstanceobject
andthefunctionobjectarepackedintoamethodobject. Whenthemethodobjectiscalledwithanargumentlist,a
newargumentlistisconstructedfromtheinstanceobjectandtheargumentlist,andthefunctionobjectiscalledwith
thisnewargumentlist.
9.3. AFirstLookatClasses 77

### 第84页

9.3.5 Class and Instance Variables
Generallyspeaking,instancevariablesarefordatauniquetoeachinstanceandclassvariablesareforattributesand
methodssharedbyallinstancesoftheclass:
class Dog:
kind = 'canine' # class variable shared by all instances
def __init__(self, name):
self.name = name # instance variable unique to each instance
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind # shared by all dogs
'canine'
>>> e.kind # shared by all dogs
'canine'
>>> d.name # unique to d
'Fido'
>>> e.name # unique to e
'Buddy'
As discussed in A Word About Names and Objects, shared data can have possibly surprising effects with involving
mutableobjectssuchaslistsanddictionaries. Forexample,thetrickslistinthefollowingcodeshouldnotbeusedas
aclassvariablebecausejustasinglelistwouldbesharedbyallDoginstances:
class Dog:
tricks = [] # mistaken use of a class variable
def __init__(self, name):
self.name = name
def add_trick(self, trick):
self.tricks.append(trick)
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks # unexpectedly shared by all dogs
['roll over', 'play dead']
Correctdesignoftheclassshoulduseaninstancevariableinstead:
class Dog:
def __init__(self, name):
self.name = name
self.tricks = [] # creates a new empty list for each dog
def add_trick(self, trick):
self.tricks.append(trick)
>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
(continuesonnextpage)
78 Chapter9. Classes

### 第85页

(continuedfrompreviouspage)
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
9.4 Random Remarks
Ifthesameattributenameoccursinbothaninstanceandinaclass,thenattributelookupprioritizestheinstance:
>>> class Warehouse:
... purpose = 'storage'
... region = 'west'
...
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
Dataattributesmaybereferencedbymethodsaswellasbyordinaryusers(“clients”)ofanobject. Inotherwords,
classesarenotusabletoimplementpureabstractdatatypes. Infact,nothinginPythonmakesitpossibletoenforce
data hiding — it is all based upon convention. (On the other hand, the Python implementation, written in C, can
completelyhideimplementationdetailsandcontrolaccesstoanobjectifnecessary;thiscanbeusedbyextensions
toPythonwritteninC.)
Clientsshouldusedataattributeswithcare—clientsmaymessupinvariantsmaintainedbythemethodsbystamping
ontheirdataattributes. Notethatclientsmayadddataattributesoftheirowntoaninstanceobjectwithoutaffecting
thevalidityofthemethods, aslongasnameconflictsareavoided—again, anamingconventioncansavealotof
headacheshere.
There is no shorthand for referencing data attributes (or other methods!) from within methods. I find that this
actuallyincreasesthereadabilityofmethods: thereisnochanceofconfusinglocalvariablesandinstancevariables
whenglancingthroughamethod.
Often,thefirstargumentofamethodiscalledself. Thisisnothingmorethanaconvention: thenameselfhas
absolutelynospecialmeaningtoPython. Note,however,thatbynotfollowingtheconventionyourcodemaybeless
readabletootherPythonprogrammers,anditisalsoconceivablethataclassbrowserprogrammightbewrittenthat
reliesuponsuchaconvention.
Anyfunctionobjectthatisaclassattributedefinesamethodforinstancesofthatclass. Itisnotnecessarythatthe
functiondefinitionistextuallyenclosedintheclassdefinition: assigningafunctionobjecttoalocalvariableinthe
classisalsook. Forexample:
# Function defined outside the class
def f1(self, x, y):
return min(x, x+y)
class C:
f = f1
def g(self):
return 'hello world'
h = g
9.4. RandomRemarks 79

### 第86页

Nowf,gandhareallattributesofclassCthatrefertofunctionobjects,andconsequentlytheyareallmethodsof
instancesofC—hbeingexactlyequivalenttog. Notethatthispracticeusuallyonlyservestoconfusethereaderof
aprogram.
Methodsmaycallothermethodsbyusingmethodattributesoftheselfargument:
class Bag:
def __init__(self):
self.data = []
def add(self, x):
self.data.append(x)
def addtwice(self, x):
self.add(x)
self.add(x)
Methods may reference global names in the same way as ordinary functions. The global scope associated with a
methodisthemodulecontainingitsdefinition. (Aclassisneverusedasaglobalscope.) Whileonerarelyencounters
agoodreasonforusingglobaldatainamethod,therearemanylegitimateusesoftheglobalscope: foronething,
functionsandmodulesimportedintotheglobalscopecanbeusedbymethods,aswellasfunctionsandclassesdefined
init. Usually,theclasscontainingthemethodisitselfdefinedinthisglobalscope,andinthenextsectionwe’llfind
somegoodreasonswhyamethodwouldwanttoreferenceitsownclass.
Eachvalueisanobject,andthereforehasaclass(alsocalleditstype). Itisstoredasobject.__class__.
9.5 Inheritance
Ofcourse,alanguagefeaturewouldnotbeworthyofthename“class”withoutsupportinginheritance. Thesyntax
foraderivedclassdefinitionlookslikethis:
class DerivedClassName(BaseClassName):
<statement-1>
.
.
.
<statement-N>
ThenameBaseClassNamemustbedefinedinanamespaceaccessiblefromthescopecontainingthederivedclass
definition. Inplaceofabaseclassname,otherarbitraryexpressionsarealsoallowed. Thiscanbeuseful,forexample,
whenthebaseclassisdefinedinanothermodule:
class DerivedClassName(modname.BaseClassName):
Executionofaderivedclassdefinitionproceedsthesameasforabaseclass. Whentheclassobjectisconstructed,
the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found
intheclass, thesearchproceedstolookinthebaseclass. Thisruleisappliedrecursivelyifthebaseclassitselfis
derivedfromsomeotherclass.
There’snothingspecialaboutinstantiationofderivedclasses: DerivedClassName()createsanewinstanceofthe
class. Methodreferencesareresolvedasfollows: thecorrespondingclassattributeissearched,descendingdownthe
chainofbaseclassesifnecessary,andthemethodreferenceisvalidifthisyieldsafunctionobject.
Derivedclassesmayoverridemethodsoftheirbaseclasses. Becausemethodshavenospecialprivilegeswhencalling
othermethodsofthesameobject,amethodofabaseclassthatcallsanothermethoddefinedinthesamebaseclass
mayendupcallingamethodofaderivedclassthatoverridesit. (ForC++programmers: allmethodsinPythonare
effectivelyvirtual.)
Anoverridingmethodinaderivedclassmayinfactwanttoextendratherthansimplyreplacethebaseclassmethod
of the same name. There is a simple way to call the base class method directly: just call BaseClassName.
80 Chapter9. Classes

### 第87页

methodname(self, arguments). This is occasionally useful to clients as well. (Note that this only works if
thebaseclassisaccessibleasBaseClassNameintheglobalscope.)
Pythonhastwobuilt-infunctionsthatworkwithinheritance:
• Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.
__class__isintorsomeclassderivedfromint.
• Useissubclass()tocheckclassinheritance: issubclass(bool, int)isTruesinceboolisasubclass
ofint. However,issubclass(float, int)isFalsesincefloatisnotasubclassofint.
9.5.1 Multiple Inheritance
Pythonsupportsaformofmultipleinheritanceaswell. Aclassdefinitionwithmultiplebaseclasseslookslikethis:
class DerivedClassName(Base1, Base2, Base3):
<statement-1>
.
.
.
<statement-N>
Formostpurposes,inthesimplestcases,youcanthinkofthesearchforattributesinheritedfromaparentclassas
depth-first,left-to-right,notsearchingtwiceinthesameclasswherethereisanoverlapinthehierarchy. Thus,ifan
attributeisnotfoundinDerivedClassName,itissearchedforinBase1,then(recursively)inthebaseclassesof
Base1,andifitwasnotfoundthere,itwassearchedforinBase2,andsoon.
Infact,itisslightlymorecomplexthanthat;themethodresolutionorderchangesdynamicallytosupportcooperative
callstosuper(). Thisapproachisknowninsomeothermultiple-inheritancelanguagesascall-next-methodandis
morepowerfulthanthesupercallfoundinsingle-inheritancelanguages.
Dynamicorderingisnecessarybecauseallcasesofmultipleinheritanceexhibitoneormorediamondrelationships
(where at least one of the parent classes can be accessed through multiple paths from the bottommost class). For
example,allclassesinheritfromobject,soanycaseofmultipleinheritanceprovidesmorethanonepathtoreach
object. Tokeepthebaseclassesfrombeingaccessedmorethanonce,thedynamicalgorithmlinearizesthesearch
orderinawaythatpreservestheleft-to-rightorderingspecifiedineachclass,thatcallseachparentonlyonce,andthat
ismonotonic(meaningthataclasscanbesubclassedwithoutaffectingtheprecedenceorderofitsparents). Taken
together, these properties make it possible to design reliable and extensible classes with multiple inheritance. For
moredetail,seepython_2.3_mro.
9.6 Private Variables
“Private”instancevariablesthatcannotbeaccessedexceptfrominsideanobjectdon’texistinPython. However,there
isaconventionthatisfollowedbymostPythoncode: anameprefixedwithanunderscore(e.g. _spam)shouldbe
treatedasanon-publicpartoftheAPI(whetheritisafunction,amethodoradatamember). Itshouldbeconsidered
animplementationdetailandsubjecttochangewithoutnotice.
Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names
defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of
the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with
_classname__spam,whereclassnameisthecurrentclassnamewithleadingunderscore(s)stripped. Thisman-
glingisdonewithoutregardtothesyntacticpositionoftheidentifier,aslongasitoccurswithinthedefinitionofa
class.
(cid:181) Seealso
Theprivatenamemanglingspecificationsfordetailsandspecialcases.
Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For
example:
9.6. PrivateVariables 81

| (cid:181) Seealso |
| --- |
| Theprivatenamemanglingspecificationsfordetailsandspecialcases. |

### 第88页

class Mapping:
def __init__(self, iterable):
self.items_list = []
self.__update(iterable)
def update(self, iterable):
for item in iterable:
self.items_list.append(item)
__update = update # private copy of original update() method
class MappingSubclass(Mapping):
def update(self, keys, values):
# provides new signature for update()
# but does not break __init__()
for item in zip(keys, values):
self.items_list.append(item)
The above example would work even if MappingSubclass were to introduce a __update identifier since
it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the
MappingSubclassclassrespectively.
Notethatthemanglingrulesaredesignedmostlytoavoidaccidents;itstillispossibletoaccessormodifyavariable
thatisconsideredprivate. Thiscanevenbeusefulinspecialcircumstances,suchasinthedebugger.
Noticethatcodepassedtoexec()oreval()doesnotconsidertheclassnameoftheinvokingclasstobethecurrent
class; thisissimilartotheeffectoftheglobalstatement,theeffectofwhichislikewiserestrictedtocodethatis
byte-compiledtogether. Thesamerestrictionappliestogetattr(),setattr()anddelattr(),aswellaswhen
referencing__dict__directly.
9.7 Odds and Ends
SometimesitisusefultohaveadatatypesimilartothePascal“record”orC“struct”,bundlingtogetherafewnamed
dataitems. Theidiomaticapproachistousedataclassesforthispurpose:
from dataclasses import dataclass
@dataclass
class Employee:
name: str
dept: str
salary: int
>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the
methodsofthatdatatypeinstead. Forinstance,ifyouhaveafunctionthatformatssomedatafromafileobject,you
candefineaclasswithmethodsread()andreadline()thatgetthedatafromastringbufferinstead,andpassit
asanargument.
Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.
__func__isthefunctionobjectcorrespondingtothemethod.
82 Chapter9. Classes

### 第89页

9.8 Iterators
Bynowyouhaveprobablynoticedthatmostcontainerobjectscanbeloopedoverusingaforstatement:
for element in [1, 2, 3]:
print(element)
for element in (1, 2, 3):
print(element)
for key in {'one':1, 'two':2}:
print(key)
for char in "123":
print(char)
for line in open("myfile.txt"):
print(line, end='')
This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind
the scenes, the for statement calls iter() on the container object. The function returns an iterator object that
definesthemethod__next__()whichaccesseselementsinthecontaineroneatatime. Whentherearenomore
elements,__next__()raisesaStopIterationexceptionwhichtellstheforlooptoterminate. Youcancallthe
__next__()methodusingthenext()built-infunction;thisexampleshowshowitallworks:
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
next(it)
StopIteration
Havingseenthemechanicsbehindtheiteratorprotocol,itiseasytoadditeratorbehaviortoyourclasses. Definean
__iter__()methodwhichreturnsanobjectwitha__next__()method. Iftheclassdefines__next__(),then
__iter__()canjustreturnself:
class Reverse:
"""Iterator for looping over a sequence backwards."""
def __init__(self, data):
self.data = data
self.index = len(data)
def __iter__(self):
return self
def __next__(self):
if self.index == 0:
raise StopIteration
self.index = self.index - 1
return self.data[self.index]
>>> rev = Reverse('spam')
>>> iter(rev)
(continuesonnextpage)
9.8. Iterators 83

### 第90页

(continuedfrompreviouspage)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
... print(char)
...
m
a
p
s
9.9 Generators
Generatorsareasimpleandpowerfultoolforcreatingiterators. Theyarewrittenlikeregularfunctionsbutusethe
yieldstatementwhenevertheywanttoreturndata. Eachtimenext()iscalledonit,thegeneratorresumeswhere
itleftoff(itremembersallthedatavaluesandwhichstatementwaslastexecuted). Anexampleshowsthatgenerators
canbetriviallyeasytocreate:
def reverse(data):
for index in range(len(data)-1, -1, -1):
yield data[index]
>>> for char in reverse('golf'):
... print(char)
...
f
l
o
g
Anything that can be done with generators can also be done with class-based iterators as described in the previ-
ous section. What makes generators so compact is that the __iter__() and __next__() methods are created
automatically.
Anotherkeyfeatureisthatthelocalvariablesandexecutionstateareautomaticallysavedbetweencalls. Thismade
thefunctioneasiertowriteandmuchmoreclearthananapproachusinginstancevariableslikeself.indexand
self.data.
Inadditiontoautomaticmethodcreationandsavingprogramstate, whengeneratorsterminate, theyautomatically
raise StopIteration. In combination, these features make it easy to create iterators with no more effort than
writingaregularfunction.
9.10 Generator Expressions
Somesimplegeneratorscanbecodedsuccinctlyasexpressionsusingasyntaxsimilartolistcomprehensionsbutwith
parentheses instead of square brackets. These expressions are designed for situations where the generator is used
rightawaybyanenclosingfunction. Generatorexpressionsaremorecompactbutlessversatilethanfullgenerator
definitionsandtendtobemorememoryfriendlythanequivalentlistcomprehensions.
Examples:
>>> sum(i*i for i in range(10)) # sum of squares
285
>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec)) # dot product
260
(continuesonnextpage)
84 Chapter9. Classes

### 第91页

(continuedfrompreviouspage)
>>> unique_words = set(word for line in page for word in line.split())
>>> valedictorian = max((student.gpa, student.name) for student in graduates)
>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
9.10. GeneratorExpressions 85

### 第92页

86 Chapter9. Classes

### 第93页

CHAPTER
TEN
BRIEF TOUR OF THE STANDARD LIBRARY
10.1 Operating System Interface
Theosmoduleprovidesdozensoffunctionsforinteractingwiththeoperatingsystem:
>>> import os
>>> os.getcwd() # Return the current working directory
'C:\\Python314'
>>> os.chdir('/server/accesslogs') # Change current working directory
>>> os.system('mkdir today') # Run the command mkdir in the system shell
0
Besuretousetheimport osstyleinsteadoffrom os import *. Thiswillkeepos.open()fromshadowing
thebuilt-inopen()functionwhichoperatesmuchdifferently.
Thebuilt-indir()andhelp()functionsareusefulasinteractiveaidsforworkingwithlargemoduleslikeos:
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
Fordailyfileanddirectorymanagementtasks,theshutilmoduleprovidesahigherlevelinterfacethatiseasierto
use:
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
10.2 File Wildcards
Theglobmoduleprovidesafunctionformakingfilelistsfromdirectorywildcardsearches:
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
10.3 Command Line Arguments
Common utility scripts often need to process command line arguments. These arguments are stored in the sys
module’sargvattributeasalist. Forinstance,let’stakethefollowingdemo.pyfile:
87

### 第94页

# File demo.py
import sys
print(sys.argv)
Hereistheoutputfromrunningpython demo.py one two threeatthecommandline:
['demo.py', 'one', 'two', 'three']
Theargparsemoduleprovidesamoresophisticatedmechanismtoprocesscommandlinearguments. Thefollowing
scriptextractsoneormorefilenamesandanoptionalnumberoflinestobedisplayed:
import argparse
parser = argparse.ArgumentParser(
prog='top',
description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
Whenrunatthecommandlinewithpython top.py --lines=5 alpha.txt beta.txt,thescriptsetsargs.
linesto5andargs.filenamesto['alpha.txt', 'beta.txt'].
10.4 Error Output Redirection and Program Termination
Thesysmodulealsohasattributesforstdin,stdout,andstderr. Thelatterisusefulforemittingwarningsanderror
messagestomakethemvisibleevenwhenstdouthasbeenredirected:
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
Themostdirectwaytoterminateascriptistousesys.exit().
10.5 String Pattern Matching
Theremoduleprovidesregularexpressiontoolsforadvancedstringprocessing. Forcomplexmatchingandmanip-
ulation,regularexpressionsoffersuccinct,optimizedsolutions:
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
Whenonlysimplecapabilitiesareneeded,stringmethodsarepreferredbecausetheyareeasiertoreadanddebug:
>>> 'tea for too'.replace('too', 'two')
'tea for two'
10.6 Mathematics
ThemathmodulegivesaccesstotheunderlyingClibraryfunctionsforfloating-pointmath:
88 Chapter10. BriefTouroftheStandardLibrary

### 第95页

>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
Therandommoduleprovidestoolsformakingrandomselections:
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10) # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random() # random float from the interval [0.0, 1.0)
0.17970987693706186
>>> random.randrange(6) # random integer chosen from range(6)
4
Thestatisticsmodulecalculatesbasicstatisticalproperties(themean,median,variance,etc.) ofnumericdata:
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
TheSciPyproject<https://scipy.org>hasmanyothermodulesfornumericalcomputations.
10.7 Internet Access
Thereareanumberofmodulesforaccessingtheinternetandprocessinginternetprotocols. Twoofthesimplestare
urllib.requestforretrievingdatafromURLsandsmtplibforsendingmail:
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
... for line in response:
... line = line.decode() # Convert bytes to a str
... if line.startswith('datetime'):
... print(line.rstrip()) # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00
>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
(Notethatthesecondexampleneedsamailserverrunningonlocalhost.)
10.7. InternetAccess 89

### 第96页

10.8 Dates and Times
Thedatetimemodulesuppliesclassesformanipulatingdatesandtimesinbothsimpleandcomplexways. While
dateandtimearithmeticissupported,thefocusoftheimplementationisonefficientmemberextractionforoutput
formattingandmanipulation. Themodulealsosupportsobjectsthataretimezoneaware.
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
10.9 Data Compression
Commondataarchivingandcompressionformatsaredirectlysupportedbymodulesincluding: zlib,gzip,bz2,
lzma,zipfileandtarfile.
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
10.10 Performance Measurement
SomePythonusersdevelopadeepinterestinknowingtherelativeperformanceofdifferentapproachestothesame
problem. Pythonprovidesameasurementtoolthatanswersthosequestionsimmediately.
Forexample,itmaybetemptingtousethetuplepackingandunpackingfeatureinsteadofthetraditionalapproach
toswappingarguments. Thetimeitmodulequicklydemonstratesamodestperformanceadvantage:
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
In contrast to timeit’s fine level of granularity, the profile and pstats modules provide tools for identifying
timecriticalsectionsinlargerblocksofcode.
90 Chapter10. BriefTouroftheStandardLibrary

### 第97页

10.11 Quality Control
One approach for developing high quality software is to write tests for each function as it is developed and to run
thosetestsfrequentlyduringthedevelopmentprocess.
Thedoctestmoduleprovidesatoolforscanningamoduleandvalidatingtestsembeddedinaprogram’sdocstrings.
Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. This
improvesthedocumentationbyprovidingtheuserwithanexampleanditallowsthedoctestmoduletomakesure
thecoderemainstruetothedocumentation:
def average(values):
"""Computes the arithmetic mean of a list of numbers.
>>> print(average([20, 30, 70]))
40.0
"""
return sum(values) / len(values)
import doctest
doctest.testmod() # automatically validate the embedded tests
Theunittestmoduleisnotaseffortlessasthedoctestmodule,butitallowsamorecomprehensivesetoftests
tobemaintainedinaseparatefile:
import unittest
class TestStatisticalFunctions(unittest.TestCase):
def test_average(self):
self.assertEqual(average([20, 30, 70]), 40.0)
self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
with self.assertRaises(ZeroDivisionError):
average([])
with self.assertRaises(TypeError):
average(20, 30, 70)
unittest.main() # Calling from the command line invokes all tests
10.12 Batteries Included
Pythonhasa“batteriesincluded”philosophy. Thisisbestseenthroughthesophisticatedandrobustcapabilitiesof
itslargerpackages. Forexample:
• The xmlrpc.client and xmlrpc.server modules make implementing remote procedure calls into an
almosttrivialtask. Despitethemodules’names,nodirectknowledgeorhandlingofXMLisneeded.
• Theemailpackageisalibraryformanagingemailmessages,includingMIMEandotherRFC2822-based
messagedocuments. Unlikesmtplibandpoplibwhichactuallysendandreceivemessages,theemailpack-
agehasacompletetoolsetforbuildingordecodingcomplexmessagestructures(includingattachments)and
forimplementinginternetencodingandheaderprotocols.
• Thejsonpackageprovidesrobustsupportforparsingthispopulardatainterchangeformat. Thecsvmod-
ulesupportsdirectreadingandwritingoffilesinComma-SeparatedValueformat, commonlysupportedby
databasesandspreadsheets. XMLprocessingissupportedbythexml.etree.ElementTree,xml.domand
xml.saxpackages. Together,thesemodulesandpackagesgreatlysimplifydatainterchangebetweenPython
applicationsandothertools.
• Thesqlite3moduleisawrapperfortheSQLitedatabaselibrary,providingapersistentdatabasethatcan
beupdatedandaccessedusingslightlynonstandardSQLsyntax.
10.11. QualityControl 91

### 第98页

• Internationalizationissupportedbyanumberofmodulesincludinggettext,locale,andthecodecspack-
age.
92 Chapter10. BriefTouroftheStandardLibrary

### 第99页

CHAPTER
ELEVEN
BRIEF TOUR OF THE STANDARD LIBRARY — PART II
Thissecondtourcoversmoreadvancedmodulesthatsupportprofessionalprogrammingneeds. Thesemodulesrarely
occurinsmallscripts.
11.1 Output Formatting
Thereprlibmoduleprovidesaversionofrepr()customizedforabbreviateddisplaysoflargeordeeplynested
containers:
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
Thepprintmoduleoffersmoresophisticatedcontroloverprintingbothbuilt-inanduserdefinedobjectsinaway
thatisreadablebytheinterpreter. Whentheresultislongerthanoneline,the“prettyprinter”addslinebreaksand
indentationtomoreclearlyrevealdatastructure:
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
... 'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
'white',
['green', 'red']],
[['magenta', 'yellow'],
'blue']]]
Thetextwrapmoduleformatsparagraphsoftexttofitagivenscreenwidth:
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
Thelocalemoduleaccessesadatabaseofculturespecificdataformats. Thegroupingattributeoflocale’sformat
functionprovidesadirectwayofformattingnumberswithgroupseparators:
93

### 第100页

>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv() # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
... conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
11.2 Templating
ThestringmoduleincludesaversatileTemplateclasswithasimplifiedsyntaxsuitableforeditingbyend-users.
Thisallowsuserstocustomizetheirapplicationswithouthavingtoaltertheapplication.
Theformatusesplaceholdernamesformedby$withvalidPythonidentifiers(alphanumericcharactersandunder-
scores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no
interveningspaces. Writing$$createsasingleescaped$:
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword
argument. Formail-mergestyleapplications,usersupplieddatamaybeincompleteandthesafe_substitute()
methodmaybemoreappropriate—itwillleaveplaceholdersunchangedifdataismissing:
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
Templatesubclassescanspecifyacustomdelimiter. Forexample,abatchrenamingutilityforaphotobrowsermay
electtousepercentsignsforplaceholderssuchasthecurrentdate,imagesequencenumber,orfileformat:
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
... delimiter = '%'
...
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
Enter rename style (%d-date %n-seqnum %f-format): Ashley_%n%f
>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
... base, ext = os.path.splitext(filename)
... newname = t.substitute(d=date, n=i, f=ext)
... print('{0} --> {1}'.format(filename, newname))
img_1074.jpg --> Ashley_0.jpg
(continuesonnextpage)
94 Chapter11. BriefTouroftheStandardLibrary—PartII

### 第101页

(continuedfrompreviouspage)
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
Another application for templating is separating program logic from the details of multiple output formats. This
makesitpossibletosubstitutecustomtemplatesforXMLfiles,plaintextreports,andHTMLwebreports.
11.3 Working with Binary Data Record Layouts
The struct module provides pack() and unpack() functions for working with variable length binary record
formats. The following example shows how to loop through header information in a ZIP file without using the
zipfilemodule. Packcodes"H"and"I"representtwoandfourbyteunsignednumbersrespectively. The"<"
indicatesthattheyarestandardsizeandinlittle-endianbyteorder:
import struct
with open('myfile.zip', 'rb') as f:
data = f.read()
start = 0
for i in range(3): # show the first 3 file headers
start += 14
fields = struct.unpack('<IIIHH', data[start:start+16])
crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
start += 16
filename = data[start:start+filenamesize]
start += filenamesize
extra = data[start:start+extra_size]
print(filename, hex(crc32), comp_size, uncomp_size)
start += extra_size + comp_size # skip to the next header
11.4 Multi-threading
Threadingisatechniquefordecouplingtaskswhicharenotsequentiallydependent. Threadscanbeusedtoimprove
theresponsivenessofapplicationsthatacceptuserinputwhileothertasksruninthebackground. Arelatedusecase
isrunningI/Oinparallelwithcomputationsinanotherthread.
Thefollowingcodeshowshowthehighlevelthreadingmodulecanruntasksinbackgroundwhilethemainprogram
continuestorun:
import threading, zipfile
class AsyncZip(threading.Thread):
def __init__(self, infile, outfile):
threading.Thread.__init__(self)
self.infile = infile
self.outfile = outfile
def run(self):
f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
f.write(self.infile)
f.close()
print('Finished background zip of:', self.infile)
(continuesonnextpage)
11.3. WorkingwithBinaryDataRecordLayouts 95

### 第102页

(continuedfrompreviouspage)
background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join() # Wait for the background task to finish
print('Main program waited until background was done.')
Theprincipalchallengeofmulti-threadedapplicationsiscoordinatingthreadsthatsharedataorotherresources. To
thatend, thethreading module providesa numberof synchronization primitivesincluding locks, events, condition
variables,andsemaphores.
While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. So, the
preferredapproachtotaskcoordinationistoconcentrateallaccesstoaresourceinasinglethreadandthenusethe
queuemoduletofeedthatthreadwithrequestsfromotherthreads. ApplicationsusingQueueobjectsforinter-thread
communicationandcoordinationareeasiertodesign,morereadable,andmorereliable.
11.5 Logging
Theloggingmoduleoffersafullfeaturedandflexibleloggingsystem. Atitssimplest,logmessagesaresenttoa
fileortosys.stderr:
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
Thisproducesthefollowingoutput:
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
By default, informational and debugging messages are suppressed and the output is sent to standard error. Other
outputoptionsincluderoutingmessagesthroughemail,datagrams,sockets,ortoanHTTPServer. Newfilterscan
selectdifferentroutingbasedonmessagepriority: DEBUG,INFO,WARNING,ERROR,andCRITICAL.
TheloggingsystemcanbeconfigureddirectlyfromPythonorcanbeloadedfromausereditableconfigurationfile
forcustomizedloggingwithoutalteringtheapplication.
11.6 Weak References
Pythondoesautomaticmemorymanagement(referencecountingformostobjectsandgarbagecollectiontoeliminate
cycles). Thememoryisfreedshortlyafterthelastreferencetoithasbeeneliminated.
Thisapproachworksfineformostapplicationsbutoccasionallythereisaneedtotrackobjectsonlyaslongasthey
arebeingusedbysomethingelse. Unfortunately,justtrackingthemcreatesareferencethatmakesthempermanent.
Theweakrefmoduleprovidestoolsfortrackingobjectswithoutcreatingareference. Whentheobjectisnolonger
needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. Typical
applicationsincludecachingobjectsthatareexpensivetocreate:
>>> import weakref, gc
>>> class A:
... def __init__(self, value):
... self.value = value
... def __repr__(self):
(continuesonnextpage)
96 Chapter11. BriefTouroftheStandardLibrary—PartII

### 第103页

(continuedfrompreviouspage)
... return str(self.value)
...
>>> a = A(10) # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a # does not create a reference
>>> d['primary'] # fetch the object if it is still alive
10
>>> del a # remove the one reference
>>> gc.collect() # run garbage collection right away
0
>>> d['primary'] # entry was automatically removed
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
d['primary'] # entry was automatically removed
File "C:/python314/lib/weakref.py", line 46, in __getitem__
o = self.data[key]()
KeyError: 'primary'
11.7 Tools for Working with Lists
Manydatastructureneedscanbemetwiththebuilt-inlisttype. However,sometimesthereisaneedforalternative
implementationswithdifferentperformancetrade-offs.
Thearraymoduleprovidesanarrayobjectthatislikealistthatstoresonlyhomogeneousdataandstoresitmore
compactly. Thefollowingexampleshowsanarrayofnumbersstoredastwobyteunsignedbinarynumbers(typecode
"H")ratherthantheusual16bytesperentryforregularlistsofPythonintobjects:
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
The collections module provides a deque object that is like a list with faster appends and pops from the left
sidebutslowerlookupsinthemiddle. Theseobjectsarewellsuitedforimplementingqueuesandbreadthfirsttree
searches:
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
node = unsearched.popleft()
for m in gen_moves(node):
if is_goal(m):
return m
unsearched.append(m)
In addition to alternative list implementations, the library also offers other tools such as the bisect module with
functionsformanipulatingsortedlists:
11.7. ToolsforWorkingwithLists 97

### 第104页

>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
The heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is
alwayskeptatpositionzero. Thisisusefulforapplicationswhichrepeatedlyaccessthesmallestelementbutdonot
wanttorunafulllistsort:
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data) # rearrange the list into heap order
>>> heappush(data, -5) # add a new entry
>>> [heappop(data) for i in range(3)] # fetch the three smallest entries
[-5, 0, 1]
11.8 Decimal Floating-Point Arithmetic
The decimal module offers a Decimal datatype for decimal floating-point arithmetic. Compared to the built-in
floatimplementationofbinaryfloatingpoint,theclassisespeciallyhelpfulfor
• financialapplicationsandotheruseswhichrequireexactdecimalrepresentation,
• controloverprecision,
• controloverroundingtomeetlegalorregulatoryrequirements,
• trackingofsignificantdecimalplaces,or
• applicationswheretheuserexpectstheresultstomatchcalculationsdonebyhand.
For example, calculating a 5% tax on a 70 cent phone charge gives different results in decimal floating point and
binaryfloatingpoint. Thedifferencebecomessignificantiftheresultsareroundedtothenearestcent:
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
TheDecimalresultkeepsatrailingzero,automaticallyinferringfourplacesignificancefrommultiplicandswithtwo
placesignificance. Decimalreproducesmathematicsasdonebyhandandavoidsissuesthatcanarisewhenbinary
floatingpointcannotexactlyrepresentdecimalquantities.
ExactrepresentationenablestheDecimalclasstoperformmodulocalculationsandequalityteststhatareunsuitable
forbinaryfloatingpoint:
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995
>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
Thedecimalmoduleprovidesarithmeticwithasmuchprecisionasneeded:
98 Chapter11. BriefTouroftheStandardLibrary—PartII

### 第105页

>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
11.8. DecimalFloating-PointArithmetic 99

### 第106页

100 Chapter11. BriefTouroftheStandardLibrary—PartII

### 第107页

CHAPTER
TWELVE
VIRTUAL ENVIRONMENTS AND PACKAGES
12.1 Introduction
Pythonapplicationswilloftenusepackagesandmodulesthatdon’tcomeaspartofthestandardlibrary. Applications
willsometimesneedaspecificversionofalibrary,becausetheapplicationmayrequirethataparticularbughasbeen
fixedortheapplicationmaybewrittenusinganobsoleteversionofthelibrary’sinterface.
This means it may not be possible for one Python installation to meet the requirements of every application. If
applicationAneedsversion1.0ofaparticularmodulebutapplicationBneedsversion2.0,thentherequirementsare
inconflictandinstallingeitherversion1.0or2.0willleaveoneapplicationunabletorun.
Thesolutionforthisproblemistocreateavirtualenvironment,aself-containeddirectorytreethatcontainsaPython
installationforaparticularversionofPython,plusanumberofadditionalpackages.
Different applications can then use different virtual environments. To resolve the earlier example of conflicting
requirements,applicationAcanhaveitsownvirtualenvironmentwithversion1.0installedwhileapplicationBhas
anothervirtualenvironmentwithversion2.0. IfapplicationBrequiresalibrarybeupgradedtoversion3.0,thiswill
notaffectapplicationA’senvironment.
12.2 Creating Virtual Environments
The module used to create and manage virtual environments is called venv. venv will install the Python version
fromwhichthecommandwasrun(asreportedbythe--versionoption). Forinstance, executingthecommand
withpython3.12willinstallversion3.12.
Tocreateavirtualenvironment,decideuponadirectorywhereyouwanttoplaceit,andrunthevenvmoduleasa
scriptwiththedirectorypath:
python -m venv tutorial-env
Thiswillcreatethetutorial-envdirectoryifitdoesn’texist,andalsocreatedirectoriesinsideitcontainingacopy
ofthePythoninterpreterandvarioussupportingfiles.
Acommondirectorylocationforavirtualenvironmentis.venv. Thisnamekeepsthedirectorytypicallyhidden
inyourshellandthusoutofthewaywhilegivingitanamethatexplainswhythedirectoryexists. Italsoprevents
clashingwith.envenvironmentvariabledefinitionfilesthatsometoolingsupports.
Onceyou’vecreatedavirtualenvironment,youmayactivateit.
OnWindows,run:
tutorial-env\Scripts\activate
OnUnixorMacOS,run:
source tutorial-env/bin/activate
(Thisscriptiswrittenforthebashshell. Ifyouusethecshorfishshells,therearealternateactivate.cshand
activate.fishscriptsyoushoulduseinstead.)
101

### 第108页

Activatingthevirtualenvironmentwillchangeyourshell’spromptto showwhatvirtualenvironmentyou’reusing,
andmodifytheenvironmentsothatrunningpythonwillgetyouthatparticularversionandinstallationofPython.
Forexample:
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May 6 2016, 10:59:36)
...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
Todeactivateavirtualenvironment,type:
deactivate
intotheterminal.
12.3 Managing Packages with pip
Youcaninstall,upgrade,andremovepackagesusingaprogramcalledpip. Bydefaultpipwillinstallpackagesfrom
thePythonPackageIndex. YoucanbrowsethePythonPackageIndexbygoingtoitinyourwebbrowser.
pip has a number of subcommands: “install”, “uninstall”, “freeze”, etc. (Consult the installing-index guide for
completedocumentationforpip.)
Youcaninstallthelatestversionofapackagebyspecifyingapackage’sname:
(tutorial-env) $ python -m pip install novas
Collecting novas
Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
Running setup.py install for novas
Successfully installed novas-3.1.1.3
You can also install a specific version of a package by giving the package name followed by == and the version
number:
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
Ifyoure-runthiscommand,pipwillnoticethattherequestedversionisalreadyinstalledanddonothing. Youcan
supplya differentversionnumberto getthatversion, oryoucanrun python -m pip install --upgrade to
upgradethepackagetothelatestversion:
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
Found existing installation: requests 2.6.0
Uninstalling requests-2.6.0:
Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
python -m pip uninstallfollowedbyoneormorepackagenameswillremovethepackagesfromthevirtual
environment.
102 Chapter12. VirtualEnvironmentsandPackages

### 第109页

python -m pip showwilldisplayinformationaboutaparticularpackage:
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
python -m pip listwilldisplayallofthepackagesinstalledinthevirtualenvironment:
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
python -m pip freezewillproduceasimilarlistoftheinstalledpackages,buttheoutputusestheformatthat
python -m pip installexpects. Acommonconventionistoputthislistinarequirements.txtfile:
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
Therequirements.txtcanthenbecommittedtoversioncontrolandshippedaspartofanapplication. Userscan
theninstallallthenecessarypackageswithinstall -r:
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
...
Installing collected packages: novas, numpy, requests
Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
piphasmanymoreoptions. Consulttheinstalling-indexguideforcompletedocumentationforpip. Whenyou’ve
written a package and want to make it available on the Python Package Index, consult the Python packaging user
guide.
12.3. ManagingPackageswithpip 103

### 第110页

104 Chapter12. VirtualEnvironmentsandPackages

### 第111页

CHAPTER
THIRTEEN
WHAT NOW?
ReadingthistutorialhasprobablyreinforcedyourinterestinusingPython—youshouldbeeagertoapplyPythonto
solvingyourreal-worldproblems. Whereshouldyougotolearnmore?
ThistutorialispartofPython’sdocumentationset. Someotherdocumentsinthesetare:
• library-index:
Youshouldbrowsethroughthismanual,whichgivescomplete(thoughterse)referencematerialabouttypes,
functions,andthemodulesinthestandardlibrary. ThestandardPythondistributionincludesalotofadditional
code. TherearemodulestoreadUnixmailboxes,retrievedocumentsviaHTTP,generaterandomnumbers,
parsecommand-lineoptions,compressdata,andmanyothertasks. SkimmingthroughtheLibraryReference
willgiveyouanideaofwhat’savailable.
• installing-indexexplainshowtoinstalladditionalmoduleswrittenbyotherPythonusers.
• reference-index: AdetailedexplanationofPython’ssyntaxandsemantics. It’sheavyreading,butisusefulas
acompleteguidetothelanguageitself.
MorePythonresources:
• https://www.python.org: ThemajorPythonwebsite. Itcontainscode,documentation,andpointerstoPython-
relatedpagesaroundtheweb.
• https://docs.python.org: FastaccesstoPython’sdocumentation.
• https://pypi.org: ThePythonPackageIndex,previouslyalsonicknamedtheCheeseShop1,isanindexofuser-
createdPython modulesthatareavailablefordownload. Onceyoubeginreleasingcode, youcanregisterit
heresothatotherscanfindit.
• https://code.activestate.com/recipes/langs/python/: ThePythonCookbookisasizablecollectionofcodeex-
amples,largermodules,andusefulscripts. Particularlynotablecontributionsarecollectedinabookalsotitled
PythonCookbook(O’Reilly&Associates,ISBN0-596-00797-3.)
• https://pyvideo.orgcollectslinkstoPython-relatedvideosfromconferencesanduser-groupmeetings.
• https://scipy.org:TheScientificPythonprojectincludesmodulesforfastarraycomputationsandmanipulations
plusahostofpackagesforsuchthingsaslinearalgebra,Fouriertransforms,non-linearsolvers,randomnumber
distributions,statisticalanalysisandthelike.
For Python-related questions and problem reports, you can post to the newsgroup comp.lang.python, or send
them to the mailing list at python-list@python.org. The newsgroup and mailing list are gatewayed, so messages
posted to one will automatically be forwarded to the other. There are hundreds of postings a day, asking (and
answering)questions, suggestingnewfeatures, andannouncingnewmodules. Mailinglistarchivesareavailableat
https://mail.python.org/pipermail/.
Before posting, be sure to check the list of Frequently Asked Questions (also called the FAQ). The FAQ answers
manyofthequestionsthatcomeupagainandagain,andmayalreadycontainthesolutionforyourproblem.
1“CheeseShop”isaMontyPython’ssketch:acustomerentersacheeseshop,butwhatevercheeseheasksfor,theclerksaysit’smissing.
105

### 第112页

106 Chapter13. WhatNow?

### 第113页

CHAPTER
FOURTEEN
INTERACTIVE INPUT EDITING AND HISTORY SUBSTITUTION
SomeversionsofthePythoninterpretersupporteditingofthecurrentinputlineandhistorysubstitution,similarto
facilities found in the Korn shell and the GNU Bash shell. This is implemented using the GNU Readline library,
whichsupportsvariousstylesofediting. Thislibraryhasitsowndocumentationwhichwewon’tduplicatehere.
14.1 Tab Completion and History Editing
CompletionofvariableandmodulenamesisautomaticallyenabledatinterpreterstartupsothattheTabkeyinvokes
the completion function; it looks at Python statement names, the current local variables, and the available module
names. Fordottedexpressionssuchasstring.a,itwillevaluatetheexpressionuptothefinal'.'andthensuggest
completions from the attributes of the resulting object. Note that this may execute application-defined code if an
objectwitha__getattr__()methodispartoftheexpression. Thedefaultconfigurationalsosavesyourhistory
into a file named .python_history in your user directory. The history will be available again during the next
interactiveinterpretersession.
14.2 Alternatives to the Interactive Interpreter
Thisfacilityisanenormousstepforwardcomparedtoearlierversionsoftheinterpreter;however,somewishesare
left: Itwouldbeniceiftheproperindentationweresuggestedoncontinuationlines(theparserknowsifanINDENT
tokenisrequirednext). Thecompletionmechanismmightusetheinterpreter’ssymboltable. Acommandtocheck
(orevensuggest)matchingparentheses,quotes,etc.,wouldalsobeuseful.
OnealternativeenhancedinteractiveinterpreterthathasbeenaroundforquitesometimeisIPython,whichfeatures
tab completion, object exploration and advanced history management. It can also be thoroughly customized and
embeddedintootherapplications. Anothersimilarenhancedinteractiveenvironmentisbpython.
107

### 第114页

108 Chapter14. InteractiveInputEditingandHistorySubstitution

### 第115页

CHAPTER
FIFTEEN
FLOATING-POINT ARITHMETIC: ISSUES AND LIMITATIONS
Floating-pointnumbersarerepresentedincomputerhardwareasbase2(binary)fractions. Forexample,thedecimal
fraction0.625hasvalue6/10+2/100+5/1000,andinthesamewaythebinaryfraction0.101hasvalue1/2+
0/4+1/8. Thesetwofractionshaveidenticalvalues,theonlyrealdifferencebeingthatthefirstiswritteninbase10
fractionalnotation,andthesecondinbase2.
Unfortunately, mostdecimalfractionscannotberepresentedexactlyasbinaryfractions. Aconsequenceisthat, in
general, thedecimalfloating-pointnumbersyouenterareonlyapproximatedbythebinaryfloating-pointnumbers
actuallystoredinthemachine.
Theproblemiseasiertounderstandatfirstinbase10. Considerthefraction1/3. Youcanapproximatethatasabase
10fraction:
0.3
or,better,
0.33
or,better,
0.333
andsoon. Nomatterhowmanydigitsyou’rewillingtowritedown,theresultwillneverbeexactly1/3,butwillbe
anincreasinglybetterapproximationof1/3.
Inthesameway,nomatterhowmanybase2digitsyou’rewillingtouse,thedecimalvalue0.1cannotberepresented
exactlyasabase2fraction. Inbase2,1/10istheinfinitelyrepeatingfraction
0.0001100110011001100110011001100110011001100110011...
Stopatanyfinitenumberofbits,andyougetanapproximation. Onmostmachinestoday,floatsareapproximated
usingabinaryfractionwiththenumeratorusingthefirst53bitsstartingwiththemostsignificantbitandwiththe
denominatorasapoweroftwo. Inthecaseof1/10,thebinaryfractionis3602879701896397 / 2 ** 55which
isclosetobutnotexactlyequaltothetruevalueof1/10.
Manyusersarenotawareoftheapproximationbecauseofthewayvaluesaredisplayed. Pythononlyprintsadecimal
approximationtothetruedecimalvalueofthebinaryapproximationstoredbythemachine. Onmostmachines,if
Pythonweretoprintthetruedecimalvalueofthebinaryapproximationstoredfor0.1,itwouldhavetodisplay:
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625
Thatismoredigitsthanmostpeoplefinduseful,soPythonkeepsthenumberofdigitsmanageablebydisplayinga
roundedvalueinstead:
>>> 1 / 10
0.1
109

### 第116页

Justremember,eventhoughtheprintedresultlooksliketheexactvalueof1/10,theactualstoredvalueisthenearest
representablebinaryfraction.
Interestingly, there are many different decimal numbers that share the same nearest approxi-
mate binary fraction. For example, the numbers 0.1 and 0.10000000000000001 and 0.
1000000000000000055511151231257827021181583404541015625 are all approximated by
3602879701896397 / 2 ** 55. Since all of these decimal values share the same approximation, any
oneofthemcouldbedisplayedwhilestillpreservingtheinvarianteval(repr(x)) == x.
Historically, the Python prompt and built-in repr() function would choose the one with 17 significant digits, 0.
10000000000000001. StartingwithPython3.1, Python(onmostsystems)isnowabletochoosetheshortestof
theseandsimplydisplay0.1.
Notethatthisisintheverynatureofbinaryfloatingpoint: thisisnotabuginPython, anditisnotabuginyour
codeeither. You’llseethesamekindofthinginalllanguagesthatsupportyourhardware’sfloating-pointarithmetic
(althoughsomelanguagesmaynotdisplaythedifferencebydefault,orinalloutputmodes).
Formorepleasantoutput,youmaywishtousestringformattingtoproducealimitednumberofsignificantdigits:
>>> format(math.pi, '.12g') # give 12 significant digits
'3.14159265359'
>>> format(math.pi, '.2f') # give 2 digits after the point
'3.14'
>>> repr(math.pi)
'3.141592653589793'
It’simportanttorealizethatthisis,inarealsense,anillusion: you’resimplyroundingthedisplayofthetruemachine
value.
Oneillusionmaybegetanother. Forexample, since0.1isnotexactly1/10, summingthreevaluesof0.1maynot
yieldexactly0.3,either:
>>> 0.1 + 0.1 + 0.1 == 0.3
False
Also,sincethe0.1cannotgetanyclosertotheexactvalueof1/10and0.3cannotgetanyclosertotheexactvalue
of3/10,thenpre-roundingwithround()functioncannothelp:
>>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
False
Thoughthenumberscannotbemadeclosertotheirintendedexactvalues,themath.isclose()functioncanbe
usefulforcomparinginexactvalues:
>>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
True
Alternatively,theround()functioncanbeusedtocompareroughapproximations:
>>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
True
Binaryfloating-pointarithmeticholdsmanysurpriseslikethis. Theproblemwith“0.1”isexplainedinprecisedetail
below,inthe“RepresentationError”section. SeeExamplesofFloatingPointProblemsforapleasantsummaryof
howbinaryfloatingpointworksandthekindsofproblemscommonlyencounteredinpractice. AlsoseeThePerils
ofFloatingPointforamorecompleteaccountofothercommonsurprises.
Asthatsaysneartheend, “therearenoeasyanswers.” Still, don’tbeundulywaryoffloatingpoint! Theerrorsin
Pythonfloatoperationsareinheritedfromthefloating-pointhardware,andonmostmachinesareontheorderofno
110 Chapter15. Floating-PointArithmetic: IssuesandLimitations

### 第117页

morethan1partin2**53peroperation. That’smorethanadequateformosttasks,butyoudoneedtokeepinmind
thatit’snotdecimalarithmeticandthateveryfloatoperationcansufferanewroundingerror.
While pathological cases do exist, for most casual use of floating-point arithmetic you’ll see the result you expect
intheendifyousimplyroundthedisplayofyourfinalresultstothenumberofdecimaldigitsyouexpect. str()
usuallysuffices,andforfinercontrolseethestr.format()method’sformatspecifiersinformatstrings.
Forusecaseswhichrequireexactdecimalrepresentation,tryusingthedecimalmodulewhichimplementsdecimal
arithmeticsuitableforaccountingapplicationsandhigh-precisionapplications.
Another form of exact arithmetic is supported by the fractions module which implements arithmetic based on
rationalnumbers(sothenumberslike1/3canberepresentedexactly).
Ifyouareaheavyuseroffloating-pointoperationsyoushouldtakealookattheNumPypackageandmanyother
packagesformathematicalandstatisticaloperationssuppliedbytheSciPyproject. See<https://scipy.org>.
Pythonprovidestoolsthatmayhelponthoserareoccasionswhenyoureallydowanttoknowtheexactvalueofa
float. Thefloat.as_integer_ratio()methodexpressesthevalueofafloatasafraction:
>>> x = 3.14159
>>> x.as_integer_ratio()
(3537115888337719, 1125899906842624)
Sincetheratioisexact,itcanbeusedtolosslesslyrecreatetheoriginalvalue:
>>> x == 3537115888337719 / 1125899906842624
True
Thefloat.hex()methodexpressesafloatinhexadecimal(base16),againgivingtheexactvaluestoredbyyour
computer:
>>> x.hex()
'0x1.921f9f01b866ep+1'
Thisprecisehexadecimalrepresentationcanbeusedtoreconstructthefloatvalueexactly:
>>> x == float.fromhex('0x1.921f9f01b866ep+1')
True
Sincetherepresentationisexact,itisusefulforreliablyportingvaluesacrossdifferentversionsofPython(platform
independence)andexchangingdatawithotherlanguagesthatsupportthesameformat(suchasJavaandC99).
Anotherhelpfultoolisthesum()functionwhichhelpsmitigateloss-of-precisionduringsummation. Itusesextended
precision for intermediate rounding steps as values are added onto a running total. That can make a difference in
overallaccuracysothattheerrorsdonotaccumulatetothepointwheretheyaffectthefinaltotal:
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
>>> sum([0.1] * 10) == 1.0
True
Themath.fsum()goesfurtherandtracksallofthe“lostdigits”asvaluesareaddedontoarunningtotalsothatthe
resulthasonlyasinglerounding. Thisisslowerthansum()butwillbemoreaccurateinuncommoncaseswhere
largemagnitudeinputsmostlycanceleachotheroutleavingafinalsumnearzero:
>>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
... -143401161400469.7, 266262841.31058735, -0.003244936839808227]
>>> float(sum(map(Fraction, arr))) # Exact summation with single rounding
8.042173697819788e-13
>>> math.fsum(arr) # Single rounding
8.042173697819788e-13
>>> sum(arr) # Multiple roundings in extended precision
(continuesonnextpage)
111

### 第118页

(continuedfrompreviouspage)
8.042178034628478e-13
>>> total = 0.0
>>> for x in arr:
... total += x # Multiple roundings in standard precision
...
>>> total # Straight addition has no correct digits!
-0.0051575902860057365
15.1 Representation Error
Thissectionexplainsthe“0.1”exampleindetail,andshowshowyoucanperformanexactanalysisofcaseslikethis
yourself. Basicfamiliaritywithbinaryfloating-pointrepresentationisassumed.
Representationerrorreferstothefactthatsome(most,actually)decimalfractionscannotberepresentedexactlyas
binary(base2)fractions. ThisisthechiefreasonwhyPython(orPerl,C,C++,Java,Fortran,andmanyothers)often
won’tdisplaytheexactdecimalnumberyouexpect.
Why is that? 1/10 is not exactly representable as a binary fraction. Since at least 2000, almost all machines use
IEEE754binaryfloating-pointarithmetic,andalmostallplatformsmapPythonfloatstoIEEE754binary64“double
precision”values. IEEE754binary64valuescontain53bitsofprecision,sooninputthecomputerstrivestoconvert
0.1totheclosestfractionitcanoftheformJ/2**N whereJ isanintegercontainingexactly53bits. Rewriting
1 / 10 ~= J / (2**N)
as
J ~= 2**N / 10
andrecallingthatJ hasexactly53bits(is>= 2**52but< 2**53),thebestvalueforN is56:
>>> 2**52 <= 2**56 // 10 < 2**53
True
Thatis,56istheonlyvalueforNthatleavesJwithexactly53bits. ThebestpossiblevalueforJisthenthatquotient
rounded:
>>> q, r = divmod(2**56, 10)
>>> r
6
Sincetheremainderismorethanhalfof10,thebestapproximationisobtainedbyroundingup:
>>> q+1
7205759403792794
Thereforethebestpossibleapproximationto1/10inIEEE754doubleprecisionis:
7205759403792794 / 2 ** 56
Dividingboththenumeratoranddenominatorbytworeducesthefractionto:
3602879701896397 / 2 ** 55
Notethatsinceweroundedup, thisisactuallya littlebitlargerthan1/10; ifwehadnotroundedup, thequotient
wouldhavebeenalittlebitsmallerthan1/10. Butinnocasecanitbeexactly1/10!
Sothecomputernever“sees”1/10: whatitseesistheexactfractiongivenabove,thebestIEEE754doubleapprox-
imationitcanget:
112 Chapter15. Floating-PointArithmetic: IssuesandLimitations

### 第119页

>>> 0.1 * 2 ** 55
3602879701896397.0
Ifwemultiplythatfractionby10**55,wecanseethevalueoutto55decimaldigits:
>>> 3602879701896397 * 10 ** 55 // 2 ** 55
1000000000000000055511151231257827021181583404541015625
meaning that the exact number stored in the computer is equal to the decimal value
0.1000000000000000055511151231257827021181583404541015625. Instead of displaying the full deci-
malvalue,manylanguages(includingolderversionsofPython),roundtheresultto17significantdigits:
>>> format(0.1, '.17f')
'0.10000000000000001'
Thefractionsanddecimalmodulesmakethesecalculationseasy:
>>> from decimal import Decimal
>>> from fractions import Fraction
>>> Fraction.from_float(0.1)
Fraction(3602879701896397, 36028797018963968)
>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)
>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> format(Decimal.from_float(0.1), '.17')
'0.10000000000000001'
15.1. RepresentationError 113

### 第120页

114 Chapter15. Floating-PointArithmetic: IssuesandLimitations

### 第121页

CHAPTER
SIXTEEN
APPENDIX
16.1 Interactive Mode
TherearetwovariantsoftheinteractiveREPL.Theclassicbasicinterpreterissupportedonallplatformswithminimal
linecontrolcapabilities.
On Windows, or Unix-like systems with curses support, a new interactive shell is used by default since Python
3.13. This one supports color, multiline editing, history browsing, and paste mode. To disable color, see using-
on-controlling-colorfordetails. Functionkeysprovidesomeadditionalfunctionality. F1enterstheinteractivehelp
browserpydoc. F2allowsforbrowsingcommand-linehistorywithneitheroutputnorthe»>and…prompts. F3
enters“pastemode”,whichmakespastinglargerblocksofcodeeasier. PressF3toreturntotheregularprompt.
When using the new interactive shell, exit the shell by typing exit or quit. Adding call parentheses after those
commandsisnotrequired.
Ifthenewinteractiveshellisnotdesired,itcanbedisabledviathePYTHON_BASIC_REPLenvironmentvariable.
16.1.1 Error Handling
Whenanerroroccurs,theinterpreterprintsanerrormessageandastacktrace. Ininteractivemode,itthenreturns
to the primary prompt; when input came from a file, it exits with a nonzero exit status after printing the stack
trace. (Exceptionshandledbyanexceptclauseinatrystatementarenoterrorsinthiscontext.) Someerrorsare
unconditionallyfatalandcauseanexitwithanonzeroexitstatus; thisappliestointernalinconsistenciesandsome
casesofrunningoutofmemory. Allerrormessagesarewrittentothestandarderrorstream; normaloutputfrom
executedcommandsiswrittentostandardoutput.
Typing the interrupt character (usually Control-C or Delete) to the primary or secondary prompt cancels
the input and returns to the primary prompt.1 Typing an interrupt while a command is executing raises the
KeyboardInterruptexception,whichmaybehandledbyatrystatement.
16.1.2 Executable Python Scripts
OnBSD’ishUnixsystems,Pythonscriptscanbemadedirectlyexecutable,likeshellscripts,byputtingtheline
#!/usr/bin/env python3
(assumingthattheinterpreterisontheuser’sPATH)atthebeginningofthescriptandgivingthefileanexecutable
mode. The#!mustbethefirsttwocharactersofthefile. Onsomeplatforms,thisfirstlinemustendwithaUnix-style
lineending('\n'),notaWindows('\r\n')lineending. Notethatthehash,orpound,character,'#',isusedto
startacommentinPython.
Thescriptcanbegivenanexecutablemode,orpermission,usingthechmodcommand.
$ chmod +x myscript.py
OnWindowssystems,thereisnonotionofan“executablemode”. ThePythoninstallerautomaticallyassociates.py
fileswithpython.exesothatadouble-clickonaPythonfilewillrunitasascript. Theextensioncanalsobe.pyw,
inthatcase,theconsolewindowthatnormallyappearsissuppressed.
1AproblemwiththeGNUReadlinepackagemaypreventthis.
115

### 第122页

16.1.3 The Interactive Startup File
WhenyouusePythoninteractively,itisfrequentlyhandytohavesomestandardcommandsexecutedeverytimethe
interpreterisstarted. YoucandothisbysettinganenvironmentvariablenamedPYTHONSTARTUPtothenameofa
filecontainingyourstart-upcommands. Thisissimilartothe.profilefeatureoftheUnixshells.
Thisfileisonlyreadininteractivesessions,notwhenPythonreadscommandsfromascript,andnotwhen/dev/tty
isgivenastheexplicitsourceofcommands(whichotherwisebehaveslikeaninteractivesession). Itisexecutedin
thesamenamespacewhereinteractivecommandsareexecuted,sothatobjectsthatitdefinesorimportscanbeused
withoutqualificationintheinteractivesession. Youcanalsochangethepromptssys.ps1andsys.ps2inthisfile.
Ifyouwanttoreadanadditionalstart-upfilefromthecurrentdirectory,youcanprogramthisintheglobalstart-up
fileusingcodelikeif os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read()). If
youwanttousethestartupfileinascript,youmustdothisexplicitlyinthescript:
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
with open(filename) as fobj:
startup_file = fobj.read()
exec(startup_file)
16.1.4 The Customization Modules
Pythonprovidestwohookstoletyoucustomizeit: sitecustomizeandusercustomize. Toseehowitworks,youneed
firsttofindthelocationofyourusersite-packagesdirectory. StartPythonandrunthiscode:
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.x/site-packages'
Nowyoucancreateafilenamedusercustomize.pyinthatdirectoryandputanythingyouwantinit. Itwillaffect
everyinvocationofPython,unlessitisstartedwiththe-soptiontodisabletheautomaticimport.
sitecustomizeworksinthesameway,butistypicallycreatedbyanadministratorofthecomputerintheglobalsite-
packages directory, and is imported before usercustomize. See the documentation of the site module for more
details.
116 Chapter16. Appendix

### 第123页

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
117

### 第124页

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
118 AppendixA. Glossary

### 第125页

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
119

### 第126页

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
120 AppendixA. Glossary

### 第127页

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
121

### 第128页

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
122 AppendixA. Glossary

### 第129页

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
123

### 第130页

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
124 AppendixA. Glossary

### 第131页

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
modulesandpackages(rememberhelp(x)). Formoreoninteractivemode,seeInteractiveMode.
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
125

### 第132页

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
126 AppendixA. Glossary

### 第133页

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
127

### 第134页

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
128 AppendixA. Glossary

### 第135页

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
129

### 第136页

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
130 AppendixA. Glossary

### 第137页

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
131

### 第138页

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
132 AppendixA. Glossary

### 第139页

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
133

### 第140页

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
134 AppendixA. Glossary

### 第141页

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
135

### 第142页

136 AppendixB. Aboutthisdocumentation

### 第143页

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
137

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

### 第144页

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
138 AppendixC. HistoryandLicense

### 第145页

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
C.2. TermsandconditionsforaccessingorotherwiseusingPython 139

### 第146页

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
140 AppendixC. HistoryandLicense

### 第147页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 141

### 第148页

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
142 AppendixC. HistoryandLicense

### 第149页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 143

### 第150页

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
144 AppendixC. HistoryandLicense

### 第151页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 145

### 第152页

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
146 AppendixC. HistoryandLicense

### 第153页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 147

### 第154页

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
148 AppendixC. HistoryandLicense

### 第155页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 149

### 第156页

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
150 AppendixC. HistoryandLicense

### 第157页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 151

### 第158页

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
152 AppendixC. HistoryandLicense

### 第159页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 153

### 第160页

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
154 AppendixC. HistoryandLicense

### 第161页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 155

### 第162页

156 AppendixC. HistoryandLicense

### 第163页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
157

### 第164页

158 AppendixD. Copyright

### 第165页

INDEX
Non-alphabetical C
...,117 callable,119
ellipsis literal,20,117 callback,119
#(hash) C-contiguous,120
comment,7 class,119
*(asterisk) class variable,119
in function calls,30 closure variable,120
** coding
in function calls,30 style,32
: (colon) complex number,120
function annotations,31 context,120
-> context management protocol,120
function annotations,31 context manager,120
>>>,117 context variable,120
__all__,49 contiguous,120
__future__,123 coroutine,120
__slots__,131 coroutine function,120
CPython,121
A
current context,121
abstract base class,117 cyclic isolate,121
annotate function,117
D
annotation,117
annotations decorator,121
function,31 descriptor,121
argument,117 dictionary,121
asynchronous context manager,118 dictionary comprehension,121
asynchronous generator,118 dictionary view,121
asynchronous generator iterator,118 docstring,121
asynchronous iterable,118 docstrings,23,31
asynchronous iterator,118 documentation strings,23,31
attached thread state,118 duck-typing,122
attribute,118 dunder,122
awaitable,119
E
B
EAFP,122
BDFL,119 environment variable
binary file,119 PATH,45,115
borrowed reference,119 PYTHON_BASIC_REPL,115
built-in function PYTHON_GIL,124
help,87 PYTHONPATH,45,46
open,57 PYTHONSTARTUP,116
builtins evaluate function,122
module,47 expression,122
bytecode,119 extension module,122
bytes-like object,119
159

### 第166页

F
keyword argument,126
f-string,122
L
f-strings,122
file lambda,126
object,57 LBYL,126
file object,122 lexical analyzer,126
file-like object,122 list,126
filesystem encoding and error handler,122 list comprehension,126
finder,123 loader,126
floor division,123 locale encoding,127
for
M
statement,17
formatted string literal,54 magic
Fortran contiguous,120 method,127
free threading,123 magic method,127
free variable,123 mangling
fstring,54 name,81
f-string,54 mapping,127
function,123 meta path finder,127
annotations,31 metaclass,127
function annotation,123 method,127
magic,127
G
object,77
garbage collection,123 special,132
generator,123 method resolution order,127
generator expression,124 module,127
generator iterator,124 builtins,47
generic function,124 json,59
generic type,124 searchpath,45
GIL,124 sys,46
global interpreter lock,124 module spec,127
MRO,127
H
mutable,127
hash-based pyc,124 N
hashable,124
help name
built-in function,87 mangling,81
named tuple,128
I
namespace,128
IDLE,125 namespace package,128
immortal,125 nested scope,128
immutable,125 new-style class,128
import path,125
O
importer,125
importing,125 object,128
interactive,125 file,57
interpolated string literal,54 method,77
interpreted,125 open
interpreter shutdown,125 built-in function,57
iterable,125 optimized scope,128
iterator,126
P
J
package,128
json parameter,129
module,59 PATH,45,115
path
K
modulesearch,45
key function,126 path based finder,129
160 Index

### 第167页

path entry,129 set comprehension,131
path entry finder,129 single dispatch,131
path entry hook,129 sitecustomize,116
path-like object,129 slice,131
PEP,129 soft deprecated,131
portion,130 special
positional argument,130 method,132
provisional API,130 special method,132
provisional package,130 standard library,132
Python 3000,130 statement,132
Python Enhancement Proposals for,17
PEP 1,130 static type checker,132
PEP 8,32 stdlib,132
PEP 238,123 string
PEP 278,133 formatted literal,54
PEP 302,127 interpolated literal,54
PEP 343,120 strings, documentation,23,31
PEP 362,118,129 strong reference,132
PEP 411,130 style
PEP 420,128,130 coding,32
PEP 443,124 sys
PEP 483,124 module,46
PEP 484,31,117,123,124,133,134
T
PEP 492,118121
PEP 498,122 t-string,132
PEP 519,129 t-strings,132
PEP 525,118 text encoding,132
PEP 526,117,134 text file,132
PEP 585,124 thread state,132
PEP 636,23 token,133
PEP 649,117 triple-quoted string,133
PEP 683,125 type,133
PEP 703,123,124 type alias,133
PEP 765,67 type hint,133
PEP 3107,31
U
PEP 3116,133
PEP 3147,46 universal newlines,133
PEP 3155,130 usercustomize,116
PYTHON_BASIC_REPL,115
PYTHON_GIL,124 V
Pythonic,130
variable annotation,133
PYTHONPATH,45,46
virtual environment,134
PYTHONSTARTUP,116
virtual machine,134
Q W
qualified name,130 walrus operator,134
R Z
reference count,131 Zen of Python,134
regular package,131
REPL,131
RFC
RFC 2822,91
S
search
path,module,45
sequence,131
Index 161

