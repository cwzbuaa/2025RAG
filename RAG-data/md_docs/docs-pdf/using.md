### 第1页

Python Setup and Usage
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 Commandlineandenvironment 3
1.1 Commandline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.1.1 Interfaceoptions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.1.2 Genericoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.1.3 Miscellaneousoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.1.4 Controllingcolor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.2 Environmentvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.2.1 Debug-modevariables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2 UsingPythononUnixplatforms 19
2.1 GettingandinstallingthelatestversionofPython . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.1.1 OnLinux . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.1.2 OnFreeBSDandOpenBSD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.2 BuildingPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3 Python-relatedpathsandfiles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.4 Miscellaneous. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.5 CustomOpenSSL. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3 ConfigurePython 23
3.1 BuildRequirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2 Generatedfiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2.1 configurescript . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.3 ConfigureOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.3.1 GeneralOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.3.2 Ccompileroptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.3.3 Linkeroptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.3.4 Optionsforthird-partydependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.3.5 WebAssemblyOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3.6 InstallOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3.7 Performanceoptions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.3.8 PythonDebugBuild . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3.9 Debugoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3.10 Linkeroptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.11 Librariesoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.12 SecurityOptions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.3.13 macOSOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.3.14 iOSOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.3.15 CrossCompilingOptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.4 PythonBuildSystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.4.1 Mainfilesofthebuildsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.4.2 Mainbuildsteps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.4.3 MainMakefiletargets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.4.4 Cextensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.5 Compilerandlinkerflags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
i

### 第4页

3.5.1 Preprocessorflags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.5.2 Compilerflags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.5.3 Linkerflags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4 UsingPythononWindows 43
4.1 PythonInstallManager . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.1.1 Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.1.2 BasicUse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.1.3 CommandHelp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.1.4 ListingRuntimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.1.5 InstallingRuntimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.1.6 OfflineInstalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.1.7 UninstallingRuntimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.1.8 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.1.9 Shebanglines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.1.10 AdvancedInstallation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.1.11 AdministrativeConfiguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.1.12 InstallingFree-threadedBinaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.1.13 Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.2 Theembeddablepackage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.2.1 PythonApplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.2.2 EmbeddingPython . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.3 Thenuget.orgpackages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.3.1 Free-threadedpackages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.4 Alternativebundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.5 SupportedWindowsversions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.6 RemovingtheMAX_PATHLimitation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.7 UTF-8mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.8 Findingmodules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.9 Additionalmodules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.9.1 PyWin32 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.9.2 cx_Freeze . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.10 CompilingPythononWindows. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.11 Thefullinstaller(deprecated) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.11.1 Installationsteps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.11.2 RemovingtheMAX_PATHLimitation . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.11.3 InstallingWithoutUI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.11.4 InstallingWithoutDownloading. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.11.5 Modifyinganinstall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.11.6 InstallingFree-threadedBinaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.12 PythonLauncherforWindows(Deprecated) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.12.1 Gettingstarted . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.12.2 ShebangLines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.12.3 Argumentsinshebanglines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.12.4 Customization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.12.5 Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.12.6 DryRun . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.12.7 Installondemand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.12.8 Returncodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
5 UsingPythononmacOS 69
5.1 UsingPythonformacOSfrompython.org . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.1.1 Installationsteps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.1.2 HowtorunaPythonscript . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
5.2 AlternativeDistributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
5.3 InstallingAdditionalPythonPackages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
5.4 GUIProgramming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
5.5 AdvancedTopics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
ii

### 第5页

5.5.1 InstallingFree-threadedBinaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.5.2 Installingusingthecommandline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.5.3 DistributingPythonApplications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5.5.4 AppStoreCompliance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5.6 OtherResources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
6 UsingPythononAndroid 83
6.1 AddingPythontoanAndroidapp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6.2 BuildingaPythonpackageforAndroid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
7 UsingPythononiOS 85
7.1 PythonatruntimeoniOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
7.1.1 iOSversioncompatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
7.1.2 Platformidentification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
7.1.3 Standardlibraryavailability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
7.1.4 Binaryextensionmodules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.1.5 Compilerstubbinaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.2 InstallingPythononiOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.2.1 ToolsforbuildingiOSapps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
7.2.2 AddingPythontoaniOSproject . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
7.2.3 TestingaPythonpackage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
7.3 AppStoreCompliance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
8 EditorsandIDEs 91
8.1 IDLE—Pythoneditorandshell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
8.2 OtherEditorsandIDEs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
A Glossary 93
B Aboutthisdocumentation 111
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
C HistoryandLicense 113
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 114
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 114
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 115
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 115
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 116
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 117
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 117
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
iii

### 第6页

C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
D Copyright 133
Index 135
iv

### 第7页

ThispartofthedocumentationisdevotedtogeneralinformationonthesetupofthePythonenvironmentondifferent
platforms,theinvocationoftheinterpreterandthingsthatmakeworkingwithPythoneasier.
CONTENTS 1

### 第8页

2 CONTENTS

### 第9页

CHAPTER
ONE
COMMAND LINE AND ENVIRONMENT
TheCPythoninterpreterscansthecommandlineandtheenvironmentforvarioussettings.
CPythonimplementationdetail: Otherimplementations’commandlineschemesmaydiffer. Seeimplementations
forfurtherresources.
1.1 Command line
WheninvokingPython,youmayspecifyanyoftheseoptions:
python [-bBdEhiIOPqRsSuvVWx?] [-c command | -m module-name | script | - ] [args]
Themostcommonusecaseis,ofcourse,asimpleinvocationofascript:
python myscript.py
1.1.1 Interface options
TheinterpreterinterfaceresemblesthatoftheUNIXshell,butprovidessomeadditionalmethodsofinvocation:
• Whencalledwithstandardinputconnectedtoattydevice,itpromptsforcommandsandexecutesthemuntilan
EOF(anend-of-filecharacter,youcanproducethatwithCtrl-DonUNIXorCtrl-Z,EnteronWindows)
isread. Formoreoninteractivemode,seetut-interac.
• Whencalledwithafilenameargumentorwithafileasstandardinput,itreadsandexecutesascriptfromthat
file.
• Whencalledwithadirectorynameargument,itreadsandexecutesanappropriatelynamedscriptfromthat
directory.
• Whencalledwith-c command,itexecutesthePythonstatement(s)givenascommand. Herecommandmay
containmultiplestatementsseparatedbynewlines. LeadingwhitespaceissignificantinPythonstatements!
• Whencalledwith-m module-name,thegivenmoduleislocatedonthePythonmodulepathandexecutedas
ascript.
Innon-interactivemode,theentireinputisparsedbeforeitisexecuted.
Aninterfaceoptionterminatesthelistofoptionsconsumedbytheinterpreter,allconsecutiveargumentswillendup
insys.argv–notethatthefirstelement,subscriptzero(sys.argv[0]),isastringreflectingtheprogram’ssource.
-c <command>
ExecutethePythoncodeincommand. commandcanbeoneormorestatementsseparatedbynewlines,with
significantleadingwhitespaceasinnormalmodulecode.
Ifthisoptionisgiven,thefirstelementofsys.argvwillbe"-c"andthecurrentdirectorywillbeaddedto
thestartofsys.path(allowingmodulesinthatdirectorytobeimportedastoplevelmodules).
Raisesanauditingeventcpython.run_commandwithargumentcommand.
3

### 第10页

Changedinversion3.14: commandisautomaticallydedentedbeforeexecution.
-m <module-name>
Searchsys.pathforthenamedmoduleandexecuteitscontentsasthe__main__module.
Sincetheargumentisamodulename,youmustnotgiveafileextension(.py). Themodulenameshouldbe
avalidabsolutePythonmodulename,buttheimplementationmaynotalwaysenforcethis(e.g. itmayallow
youtouseanamethatincludesahyphen).
Packagenames(includingnamespacepackages)arealsopermitted. Whenapackagenameissuppliedinstead
of a normal module, the interpreter will execute <pkg>.__main__ as the main module. This behaviour is
deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script
argument.
(cid:174) Note
Thisoptioncannotbeusedwithbuilt-inmodulesandextensionmoduleswritteninC,sincetheydonot
havePythonmodulefiles. However,itcanstillbeusedforprecompiledmodules,eveniftheoriginalsource
fileisnotavailable.
Ifthisoptionisgiven,thefirstelementofsys.argvwillbethefullpathtothemodulefile(whilethemodule
fileisbeinglocated,thefirstelementwillbesetto"-m"). Aswiththe-coption,thecurrentdirectorywillbe
addedtothestartofsys.path.
-Ioptioncanbeusedtorunthescriptinisolatedmodewheresys.pathcontainsneitherthecurrentdirectory
northeuser’ssite-packagesdirectory. AllPYTHON*environmentvariablesareignored,too.
Manystandardlibrarymodulescontaincodethatisinvokedontheirexecutionasascript. Anexampleisthe
timeitmodule:
python -m timeit -s "setup here" "benchmarked code here"
python -m timeit -h # for details
Raisesanauditingeventcpython.run_modulewithargumentmodule-name.
(cid:181) Seealso
runpy.run_module()
EquivalentfunctionalitydirectlyavailabletoPythoncode
PEP338–Executingmodulesasscripts
Changedinversion3.1: Supplythepackagenametoruna__main__submodule.
Changedinversion3.4: namespacepackagesarealsosupported
-
Readcommandsfromstandardinput(sys.stdin). Ifstandardinputisaterminal,-iisimplied.
Ifthisoptionisgiven,thefirstelementofsys.argvwillbe"-"andthecurrentdirectorywillbeaddedto
thestartofsys.path.
Raisesanauditingeventcpython.run_stdinwithnoarguments.
<script>
ExecutethePythoncodecontainedinscript,whichmustbeafilesystempath(absoluteorrelative)referringto
eitheraPythonfile,adirectorycontaininga__main__.pyfile,orazipfilecontaininga__main__.pyfile.
Ifthisoptionisgiven,thefirstelementofsys.argvwillbethescriptnameasgivenonthecommandline.
4 Chapter1. Commandlineandenvironment

| (cid:181) Seealso |
| --- |
| runpy.run_module()
EquivalentfunctionalitydirectlyavailabletoPythoncode
PEP338–Executingmodulesasscripts |

### 第11页

If the script name refers directly to a Python file, the directory containing that file is added to the start of
sys.path,andthefileisexecutedasthe__main__module.
Ifthescriptnamereferstoadirectoryorzipfile,thescriptnameisaddedtothestartofsys.pathandthe
__main__.pyfileinthatlocationisexecutedasthe__main__module.
-Ioptioncanbeusedtorunthescriptinisolatedmodewheresys.pathcontainsneitherthescript’sdirectory
northeuser’ssite-packagesdirectory. AllPYTHON*environmentvariablesareignored,too.
Raisesanauditingeventcpython.run_filewithargumentfilename.
(cid:181) Seealso
runpy.run_path()
EquivalentfunctionalitydirectlyavailabletoPythoncode
Ifnointerfaceoptionisgiven,-iisimplied,sys.argv[0]isanemptystring("")andthecurrentdirectorywill
beaddedtothestartofsys.path. Also,tab-completionandhistoryeditingisautomaticallyenabled,ifavailable
onyourplatform(seerlcompleter-config).
(cid:181) Seealso
tut-invoking
Changedinversion3.4: Automaticenablingoftab-completionandhistoryediting.
1.1.2 Generic options
-?
-h
--help
Printashortdescriptionofallcommandlineoptionsandcorrespondingenvironmentvariablesandexit.
--help-env
PrintashortdescriptionofPython-specificenvironmentvariablesandexit.
Addedinversion3.11.
--help-xoptions
Printadescriptionofimplementation-specific-X optionsandexit.
Addedinversion3.11.
--help-all
Printcompleteusageinformationandexit.
Addedinversion3.11.
-V
--version
PrintthePythonversionnumberandexit. Exampleoutputcouldbe:
Python 3.8.0b2+
Whengiventwice,printmoreinformationaboutthebuild,like:
Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
[GCC 6.2.0 20161005]
1.1. Commandline 5

| (cid:181) Seealso |
| --- |
| runpy.run_path()
EquivalentfunctionalitydirectlyavailabletoPythoncode |


| (cid:181) Seealso |
| --- |
| tut-invoking |

### 第12页

Addedinversion3.6: The-VVoption.
1.1.3 Miscellaneous options
-b
Issue a warning when converting bytes or bytearray to str without specifying encoding or comparing
bytesorbytearraywithstrorbyteswithint. Issueanerrorwhentheoptionisgiventwice(-bb).
Changedinversion3.5: Affectsalsocomparisonsofbyteswithint.
-B
If given, Python won’t try to write .pyc files on the import of source modules. See also
PYTHONDONTWRITEBYTECODE.
--check-hash-based-pycs default|always|never
Controlthevalidationbehaviorofhash-based.pycfiles. Seepyc-invalidation. Whensettodefault,checked
anduncheckedhash-basedbytecodecachefilesarevalidatedaccordingtotheirdefaultsemantics. Whensetto
always,allhash-based.pycfiles,whethercheckedorunchecked,arevalidatedagainsttheircorresponding
source file. When set to never, hash-based .pyc files are not validated against their corresponding source
files.
Thesemanticsoftimestamp-based.pycfilesareunaffectedbythisoption.
-d
Turnonparserdebuggingoutput(forexpertonly). SeealsothePYTHONDEBUGenvironmentvariable.
ThisoptionrequiresadebugbuildofPython,otherwiseit’signored.
-E
IgnoreallPYTHON*environmentvariables,e.g. PYTHONPATHandPYTHONHOME,thatmightbeset.
Seealsothe-Pand-I(isolated)options.
-i
Enterinteractivemodeafterexecution.
Usingthe-ioptionwillenterinteractivemodeinanyofthefollowingcircumstances:
• Whenascriptispassedasfirstargument
• Whenthe-coptionisused
• Whenthe-moptionisused
Interactivemodewillstartevenwhensys.stdindoesnotappeartobeaterminal. ThePYTHONSTARTUP
fileisnotread.
This can be useful to inspect global variables or a stack trace when a script raises an exception. See also
PYTHONINSPECT.
-I
RunPythoninisolatedmode. Thisalsoimplies-E,-Pand-soptions.
Inisolatedmodesys.pathcontainsneitherthescript’sdirectorynortheuser’ssite-packagesdirectory. All
PYTHON* environment variables are ignored, too. Further restrictions may be imposed to prevent the user
frominjectingmaliciouscode.
Addedinversion3.4.
-O
Remove assert statements and any code conditional on the value of __debug__. Augment the filename
for compiled (bytecode) files by adding .opt-1 before the .pyc extension (see PEP 488). See also
PYTHONOPTIMIZE.
Changedinversion3.5: Modify.pycfilenamesaccordingtoPEP488.
6 Chapter1. Commandlineandenvironment

### 第13页

-OO
Do -O and also discard docstrings. Augment the filename for compiled (bytecode) files by adding .opt-2
beforethe.pycextension(seePEP488).
Changedinversion3.5: Modify.pycfilenamesaccordingtoPEP488.
-P
Don’tprependapotentiallyunsafepathtosys.path:
• python -m modulecommandline: Don’tprependthecurrentworkingdirectory.
• python script.pycommandline: Don’tprependthescript’sdirectory. Ifit’sasymboliclink,resolve
symboliclinks.
• python -c codeandpython(REPL)commandlines: Don’tprependanemptystring,whichmeans
thecurrentworkingdirectory.
SeealsothePYTHONSAFEPATHenvironmentvariable,and-Eand-I(isolated)options.
Addedinversion3.11.
-q
Don’tdisplaythecopyrightandversionmessagesevenininteractivemode.
Addedinversion3.2.
-R
Turnonhashrandomization. ThisoptiononlyhasaneffectifthePYTHONHASHSEEDenvironmentvariableis
settoanythingotherthanrandom,sincehashrandomizationisenabledbydefault.
OnpreviousversionsofPython,thisoptionturnsonhashrandomization,sothatthe__hash__()valuesof
strandbytesobjectsare“salted”withanunpredictablerandomvalue. Althoughtheyremainconstantwithin
anindividualPythonprocess,theyarenotpredictablebetweenrepeatedinvocationsofPython.
Hashrandomizationisintendedtoprovideprotectionagainstadenial-of-servicecausedbycarefullychosen
inputsthatexploittheworstcaseperformanceofadictconstruction,O(n2)complexity. Seehttp://ocert.org/
advisories/ocert-2011-003.htmlfordetails.
PYTHONHASHSEEDallowsyoutosetafixedvalueforthehashseedsecret.
Addedinversion3.2.3.
Changedinversion3.7: Theoptionisnolongerignored.
-s
Don’taddtheuser site-packages directorytosys.path.
SeealsoPYTHONNOUSERSITE.
(cid:181) Seealso
PEP370–Perusersite-packagesdirectory
-S
Disable the import of the module site and the site-dependent manipulations of sys.path that it entails.
Alsodisablethesemanipulationsifsiteisexplicitlyimportedlater(callsite.main()ifyouwantthemto
betriggered).
-u
Forcethestdoutandstderrstreamstobeunbuffered. Thisoptionhasnoeffectonthestdinstream.
SeealsoPYTHONUNBUFFERED.
Changedinversion3.7: Thetextlayerofthestdoutandstderrstreamsnowisunbuffered.
1.1. Commandline 7

| (cid:181) Seealso |
| --- |
| PEP370–Perusersite-packagesdirectory |

### 第14页

-v
Printamessageeachtimeamoduleisinitialized,showingtheplace(filenameorbuilt-inmodule)fromwhich
itisloaded. Whengiventwice(-vv), printamessageforeachfilethatischeckedforwhensearchingfora
module. Alsoprovidesinformationonmodulecleanupatexit.
Changedinversion3.10: Thesitemodulereportsthesite-specificpathsand.pthfilesbeingprocessed.
SeealsoPYTHONVERBOSE.
-W arg
Warningcontrol. Python’swarningmachinerybydefaultprintswarningmessagestosys.stderr.
Thesimplestsettingsapplyaparticularactionunconditionallytoallwarningsemittedbyaprocess(eventhose
thatareotherwiseignoredbydefault):
-Wdefault # Warn once per call location
-Werror # Convert to exceptions
-Walways # Warn every time
-Wall # Same as -Walways
-Wmodule # Warn once per calling module
-Wonce # Warn once per Python process
-Wignore # Never warn
Theactionnamescanbeabbreviatedasdesiredandtheinterpreterwillresolvethemtotheappropriateaction
name. Forexample,-Wiisthesameas-Wignore.
Thefullformofargumentis:
action:message:category:module:lineno
Empty fields match all values; trailing empty fields may be omitted. For example -W
ignore::DeprecationWarningignoresallDeprecationWarningwarnings.
Theactionfieldisasexplainedabovebutonlyappliestowarningsthatmatchtheremainingfields.
Themessagefieldmustmatchthewholewarningmessage;thismatchiscase-insensitive.
Thecategoryfieldmatchesthewarningcategory(ex: DeprecationWarning). Thismustbeaclassname;the
matchtestwhethertheactualwarningcategoryofthemessageisasubclassofthespecifiedwarningcategory.
Themodulefieldmatchesthe(fullyqualified)modulename;thismatchiscase-sensitive.
The lineno field matches the line number, where zero matches all line numbers and is thus equivalent to an
omittedlinenumber.
Multiple -W options can be given; when a warning matches more than one option, the action for the last
matching option is performed. Invalid -W options are ignored (though, a warning message is printed about
invalidoptionswhenthefirstwarningisissued).
WarningscanalsobecontrolledusingthePYTHONWARNINGSenvironmentvariableandfromwithinaPython
program using the warnings module. For example, the warnings.filterwarnings() function can be
usedtousearegularexpressiononthewarningmessage.
Seewarning-filteranddescribing-warning-filtersformoredetails.
-x
Skipthefirstlineofthesource,allowinguseofnon-Unixformsof#!cmd. ThisisintendedforaDOSspecific
hackonly.
-X
Reservedforvariousimplementation-specificoptions. CPythoncurrentlydefinesthefollowingpossiblevalues:
• -X faulthandlertoenablefaulthandler. SeealsoPYTHONFAULTHANDLER.
Addedinversion3.3.
8 Chapter1. Commandlineandenvironment

### 第15页

• -X showrefcount to outputthe totalreference countand numberof used memory blockswhen the
programfinishesoraftereachstatementintheinteractiveinterpreter. Thisonlyworksondebugbuilds.
Addedinversion3.4.
• -X tracemalloctostarttracingPythonmemoryallocationsusingthetracemallocmodule. Byde-
fault, onlythemostrecentframeisstoredinatracebackofatrace. Use-X tracemalloc=NFRAME
to start tracing with a traceback limit of NFRAME frames. See tracemalloc.start() and
PYTHONTRACEMALLOCformoreinformation.
Addedinversion3.4.
• -X int_max_str_digits configures the integer string conversion length limitation. See also
PYTHONINTMAXSTRDIGITS.
Addedinversion3.11.
• -X importtimetoshowhowlongeachimporttakes. Itshowsmodulename,cumulativetime(including
nestedimports)andselftime(excludingnestedimports). Notethatitsoutputmaybebrokeninmulti-
threadedapplication. Typicalusageispython -X importtime -c 'import asyncio'.
-X importtime=2enablesadditionaloutputthatindicateswhenanimportedmodulehasalreadybeen
loaded. Insuchcases,thestringcachedwillbeprintedinbothtimecolumns.
SeealsoPYTHONPROFILEIMPORTTIME.
Addedinversion3.7.
Changedinversion3.14: Added-X importtime=2toalsotraceimportsofloadedmodules,andre-
servedvaluesotherthan1and2forfutureuse.
• -X dev: enablePythonDevelopmentMode,introducingadditionalruntimechecksthataretooexpen-
sivetobeenabledbydefault. SeealsoPYTHONDEVMODE.
Addedinversion3.7.
• -X utf8enablesthePythonUTF-8Mode. -X utf8=0explicitlydisablesPythonUTF-8Mode(even
whenitwouldotherwiseactivateautomatically). SeealsoPYTHONUTF8.
Addedinversion3.7.
• -X pycache_prefix=PATHenableswriting.pycfilestoaparalleltreerootedatthegivendirectory
insteadoftothecodetree. SeealsoPYTHONPYCACHEPREFIX.
Addedinversion3.8.
• -X warn_default_encodingissuesaEncodingWarningwhenthelocale-specificdefaultencoding
isusedforopeningfiles. SeealsoPYTHONWARNDEFAULTENCODING.
Addedinversion3.10.
• -X no_debug_ranges disables the inclusion of the tables mapping extra location information (end
line,startcolumnoffsetandendcolumnoffset)toeveryinstructionincodeobjects. Thisisusefulwhen
smallercodeobjectsandpycfilesaredesiredaswellassuppressingtheextravisuallocationindicators
whentheinterpreterdisplaystracebacks. SeealsoPYTHONNODEBUGRANGES.
Addedinversion3.11.
• -X frozen_modulesdetermineswhetherornotfrozenmodulesareignoredbytheimportmachinery.
A value of on means they get imported and off means they are ignored. The default is on if this is
an installed Python (the normal case). If it’s under development (running from the source tree) then
thedefaultisoff. Notethattheimportlib_bootstrapandimportlib_bootstrap_external
frozenmodulesarealwaysused,evenifthisflagissettooff. SeealsoPYTHON_FROZEN_MODULES.
Addedinversion3.11.
• -X perfenablessupportfortheLinuxperfprofiler. Whenthisoptionisprovided,theperfprofiler
willbeabletoreportPythoncalls. Thisoptionisonlyavailableonsomeplatformsandwilldonothingif
isnotsupportedonthecurrentsystem. Thedefaultvalueis“off”. SeealsoPYTHONPERFSUPPORT and
perf_profiling.
1.1. Commandline 9

### 第16页

Addedinversion3.12.
• -X perf_jitenablessupportfortheLinuxperfprofilerwithDWARFsupport. Whenthisoptionis
provided,theperfprofilerwillbeabletoreportPythoncallsusingDWARFinformation. Thisoption
isonlyavailableonsomeplatformsandwilldonothingifisnotsupportedonthecurrentsystem. The
defaultvalueis“off”. SeealsoPYTHON_PERF_JIT_SUPPORTandperf_profiling.
Addedinversion3.13.
• -X disable_remote_debugdisablestheremotedebuggingsupportasdescribedinPEP768. This
includesboththefunctionalitytoschedulecodeforexecutioninanotherprocessandthefunctionalityto
receivecodeforexecutioninthecurrentprocess.
This option is only available on some platforms and will do nothing if is not supported on the current
system. SeealsoPYTHON_DISABLE_REMOTE_DEBUGandPEP768.
Addedinversion3.14.
• -X cpu_count=n overrides os.cpu_count(), os.process_cpu_count(), and
multiprocessing.cpu_count(). n must be greater than or equal to 1. This option may be
usefulforuserswhoneedtolimitCPUresourcesofacontainersystem. SeealsoPYTHON_CPU_COUNT.
Ifnisdefault,nothingisoverridden.
Addedinversion3.13.
• -X presite=package.modulespecifiesamodulethatshouldbeimportedbeforethesitemodule
isexecutedandbeforethe__main__moduleexists. Therefore,theimportedmoduleisn’t__main__.
ThiscanbeusedtoexecutecodeearlyduringPythoninitialization. Pythonneedstobebuiltindebug
modeforthisoptiontoexist. SeealsoPYTHON_PRESITE.
Addedinversion3.13.
• -X gil=0,1forcestheGILtobedisabledorenabled,respectively. Settingto0isonlyavailableinbuilds
configuredwith--disable-gil. SeealsoPYTHON_GILandwhatsnew313-free-threaded-cpython.
Addedinversion3.13.
• -X thread_inherit_context=0,1 causes Thread to, by default, use a copy of context of the
caller of Thread.start() when starting. Otherwise, threads will start with an empty context. If
unset, the value of this option defaults to 1 on free-threaded builds and to 0 otherwise. See also
PYTHON_THREAD_INHERIT_CONTEXT.
Addedinversion3.14.
• -X context_aware_warnings=0,1causesthewarnings.catch_warningscontextmanagerto
useaContextVartostorewarningsfilterstate. Ifunset,thevalueofthisoptiondefaultsto1onfree-
threadedbuildsandto0otherwise. SeealsoPYTHON_CONTEXT_AWARE_WARNINGS.
Addedinversion3.14.
• -X tlbc=0,1 enables (1, the default) or disables (0) thread-local bytecode in builds configured
with --disable-gil. When disabled, this also disables the specializing interpreter. See also
PYTHON_TLBC.
Addedinversion3.14.
Italsoallowspassingarbitraryvaluesandretrievingthemthroughthesys._xoptionsdictionary.
Addedinversion3.2.
Changedinversion3.9: Removedthe-X showalloccountoption.
Changedinversion3.10: Removedthe-X oldparseroption.
Removedinversion3.14: -JisnolongerreservedforusebyJython,andnowhasnospecialmeaning.
10 Chapter1. Commandlineandenvironment

### 第17页

1.1.4 Controlling color
ThePythoninterpreterisconfiguredbydefaulttousecolorstohighlightoutputincertainsituationssuchaswhen
displayingtracebacks. Thisbehaviorcanbecontrolledbysettingdifferentenvironmentvariables.
SettingtheenvironmentvariableTERMtodumbwilldisablecolor.
IftheFORCE_COLORenvironmentvariableisset,thencolorwillbeenabledregardlessofthevalueofTERM.This
isusefulonCIsystemswhicharen’tterminalsbutcanstilldisplayANSIescapesequences.
IftheNO_COLORenvironmentvariableisset,Pythonwilldisableallcolorintheoutput. Thistakesprecedenceover
FORCE_COLOR.
Alltheseenvironmentvariablesareusedalsobyothertoolstocontrolcoloroutput. Tocontrolthecoloroutputonly
inthePythoninterpreter,thePYTHON_COLORSenvironmentvariablecanbeused. Thisvariabletakesprecedence
overNO_COLOR,whichinturntakesprecedenceoverFORCE_COLOR.
1.2 Environment variables
TheseenvironmentvariablesinfluencePython’sbehavior,theyareprocessedbeforethecommand-lineswitchesother
than-Eor-I.Itiscustomarythatcommand-lineswitchesoverrideenvironmentalvariableswherethereisaconflict.
PYTHONHOME
Change the location of the standard Python libraries. By default, the libraries are searched in prefix/
lib/pythonversionandexec_prefix/lib/pythonversion, whereprefix andexec_prefix are
installation-dependentdirectories,bothdefaultingto/usr/local.
WhenPYTHONHOMEissettoasingledirectory,itsvaluereplacesbothprefixandexec_prefix. Tospecify
differentvaluesforthese,setPYTHONHOMEtoprefix:exec_prefix.
PYTHONPATH
Augment the default search path for module files. The format is the same as the shell’s PATH: one or more
directory pathnames separated by os.pathsep (e.g. colons on Unix or semicolons on Windows). Non-
existentdirectoriesaresilentlyignored.
Inadditiontonormaldirectories,individualPYTHONPATHentriesmayrefertozipfilescontainingpurePython
modules(ineithersourceorcompiledform). Extensionmodulescannotbeimportedfromzipfiles.
Thedefaultsearchpathisinstallationdependent,butgenerallybeginswithprefix/lib/pythonversion
(seePYTHONHOMEabove). ItisalwaysappendedtoPYTHONPATH.
AnadditionaldirectorywillbeinsertedinthesearchpathinfrontofPYTHONPATHasdescribedaboveunder
Interface options. The search path can be manipulated from within a Python program as the variable sys.
path.
PYTHONSAFEPATH
Ifthisissettoanon-emptystring,don’tprependapotentiallyunsafepathtosys.path: seethe-Poptionfor
details.
Addedinversion3.11.
PYTHONPLATLIBDIR
Ifthisissettoanon-emptystring,itoverridesthesys.platlibdirvalue.
Addedinversion3.9.
PYTHONSTARTUP
Ifthisisthenameofareadablefile,thePythoncommandsinthatfileareexecutedbeforethefirstpromptis
displayed in interactive mode. The file is executed in the same namespace where interactive commands are
executedsothatobjectsdefinedorimportedinitcanbeusedwithoutqualificationintheinteractivesession.
Youcanalsochangethepromptssys.ps1andsys.ps2andthehooksys.__interactivehook__inthis
file.
1.2. Environmentvariables 11

### 第18页

Raisesanauditingeventcpython.run_startupwiththefilenameastheargumentwhencalledonstartup.
PYTHONOPTIMIZE
Ifthisissettoanon-emptystringitisequivalenttospecifyingthe-Ooption. Ifsettoaninteger,itisequivalent
tospecifying-Omultipletimes.
PYTHONBREAKPOINT
Ifthisisset, itnamesacallableusingdotted-pathnotation. Themodulecontainingthecallablewillbeim-
portedandthenthecallablewillberunbythedefaultimplementationofsys.breakpointhook()which
itselfiscalledbybuilt-inbreakpoint(). Ifnotset,orsettotheemptystring,itisequivalenttothevalue
“pdb.set_trace”. Settingthistothestring“0”causesthedefaultimplementationofsys.breakpointhook()
todonothingbutreturnimmediately.
Addedinversion3.7.
PYTHONDEBUG
Ifthisissettoanon-emptystringitisequivalenttospecifyingthe-doption. Ifsettoaninteger,itisequivalent
tospecifying-dmultipletimes.
ThisenvironmentvariablerequiresadebugbuildofPython,otherwiseit’signored.
PYTHONINSPECT
Ifthisissettoanon-emptystringitisequivalenttospecifyingthe-ioption.
This variable can also be modified by Python code using os.environ to force inspect mode on program
termination.
Raisesanauditingeventcpython.run_stdinwithnoarguments.
Changedinversion3.12.5: (also3.11.10,3.10.15,3.9.20,and3.8.20)Emitsauditevents.
Changedinversion3.13: UsesPyREPLifpossible,inwhichcasePYTHONSTARTUPisalsoexecuted. Emits
auditevents.
PYTHONUNBUFFERED
Ifthisissettoanon-emptystringitisequivalenttospecifyingthe-uoption.
PYTHONVERBOSE
Ifthisissettoanon-emptystringitisequivalenttospecifyingthe-voption. Ifsettoaninteger,itisequivalent
tospecifying-vmultipletimes.
PYTHONCASEOK
Ifthisisset,Pythonignorescaseinimportstatements. ThisonlyworksonWindowsandmacOS.
PYTHONDONTWRITEBYTECODE
Ifthisissettoanon-emptystring,Pythonwon’ttrytowrite.pycfilesontheimportofsourcemodules. This
isequivalenttospecifyingthe-Boption.
PYTHONPYCACHEPREFIX
Ifthisisset,Pythonwillwrite.pycfilesinamirrordirectorytreeatthispath,insteadofin__pycache__
directorieswithinthesourcetree. Thisisequivalenttospecifyingthe-X pycache_prefix=PATHoption.
Addedinversion3.8.
PYTHONHASHSEED
Ifthisvariableisnotsetorsettorandom,arandomvalueisusedtoseedthehashesofstrandbytesobjects.
IfPYTHONHASHSEEDissettoanintegervalue,itisusedasafixedseedforgeneratingthehash()ofthetypes
coveredbythehashrandomization.
Itspurposeistoallowrepeatablehashing,suchasforselftestsfortheinterpreteritself,ortoallowaclusterof
pythonprocessestosharehashvalues.
Theintegermustbeadecimalnumberintherange[0,4294967295]. Specifyingthevalue0willdisablehash
randomization.
Addedinversion3.2.3.
12 Chapter1. Commandlineandenvironment

### 第19页

PYTHONINTMAXSTRDIGITS
Ifthisvariableissettoaninteger,itisusedtoconfiguretheinterpreter’sglobalintegerstringconversionlength
limitation.
Addedinversion3.11.
PYTHONIOENCODING
Ifthisissetbeforerunningtheinterpreter,itoverridestheencodingusedforstdin/stdout/stderr,inthesyntax
encodingname:errorhandler. Boththeencodingnameandthe:errorhandlerpartsareoptionaland
havethesamemeaningasinstr.encode().
Forstderr,the:errorhandlerpartisignored;thehandlerwillalwaysbe'backslashreplace'.
Changedinversion3.4: Theencodingnamepartisnowoptional.
Changedinversion3.6: OnWindows,theencodingspecifiedbythisvariableisignoredforinteractivecon-
solebuffersunlessPYTHONLEGACYWINDOWSSTDIO isalsospecified. Filesandpipesredirectedthroughthe
standardstreamsarenotaffected.
PYTHONNOUSERSITE
Ifthisisset,Pythonwon’taddtheuser site-packages directorytosys.path.
(cid:181) Seealso
PEP370–Perusersite-packagesdirectory
PYTHONUSERBASE
Defines the user base directory, which is used to compute the path of the user site-packages
directoryandinstallationpathsforpython -m pip install --user.
(cid:181) Seealso
PEP370–Perusersite-packagesdirectory
PYTHONEXECUTABLE
Ifthisenvironmentvariableisset,sys.argv[0]willbesettoitsvalueinsteadofthevaluegotthroughthe
Cruntime. OnlyworksonmacOS.
PYTHONWARNINGS
Thisisequivalenttothe-Woption. Ifsettoacommaseparatedstring,itisequivalenttospecifying-Wmultiple
times,withfilterslaterinthelisttakingprecedenceoverthoseearlierinthelist.
Thesimplestsettingsapplyaparticularactionunconditionallytoallwarningsemittedbyaprocess(eventhose
thatareotherwiseignoredbydefault):
PYTHONWARNINGS=default # Warn once per call location
PYTHONWARNINGS=error # Convert to exceptions
PYTHONWARNINGS=always # Warn every time
PYTHONWARNINGS=all # Same as PYTHONWARNINGS=always
PYTHONWARNINGS=module # Warn once per calling module
PYTHONWARNINGS=once # Warn once per Python process
PYTHONWARNINGS=ignore # Never warn
Seewarning-filteranddescribing-warning-filtersformoredetails.
PYTHONFAULTHANDLER
Ifthisenvironmentvariableissettoanon-emptystring,faulthandler.enable()iscalledatstartup:install
ahandlerforSIGSEGV,SIGFPE,SIGABRT,SIGBUSandSIGILLsignalstodumpthePythontraceback. This
isequivalentto-X faulthandleroption.
1.2. Environmentvariables 13

| (cid:181) Seealso |
| --- |
| PEP370–Perusersite-packagesdirectory |


| (cid:181) Seealso |
| --- |
| PEP370–Perusersite-packagesdirectory |

### 第20页

Addedinversion3.3.
PYTHONTRACEMALLOC
If this environment variable is set to a non-empty string, start tracing Python memory allocations using the
tracemallocmodule. Thevalueofthevariableisthemaximumnumberofframesstoredinatracebackof
atrace. Forexample,PYTHONTRACEMALLOC=1storesonlythemostrecentframe. Seethetracemalloc.
start()functionformoreinformation. Thisisequivalenttosettingthe-X tracemallocoption.
Addedinversion3.4.
PYTHONPROFILEIMPORTTIME
If this environment variable is set to 1, Python will show how long each import takes. If set to 2, Python
willincludeoutputforimportedmodulesthathavealreadybeenloaded. Thisisequivalenttosettingthe-X
importtimeoption.
Addedinversion3.7.
Changedinversion3.14: AddedPYTHONPROFILEIMPORTTIME=2toalsotraceimportsofloadedmodules.
PYTHONASYNCIODEBUG
Ifthisenvironmentvariableissettoanon-emptystring,enablethedebugmodeoftheasynciomodule.
Addedinversion3.4.
PYTHONMALLOC
SetthePythonmemoryallocatorsand/orinstalldebughooks.
SetthefamilyofmemoryallocatorsusedbyPython:
• default: usethedefaultmemoryallocators.
• malloc: use the malloc() function of the C library for all domains (PYMEM_DOMAIN_RAW,
PYMEM_DOMAIN_MEM,PYMEM_DOMAIN_OBJ).
• pymalloc:usethepymallocallocatorforPYMEM_DOMAIN_MEMandPYMEM_DOMAIN_OBJdomainsand
usethemalloc()functionforthePYMEM_DOMAIN_RAWdomain.
• mimalloc: use the mimalloc allocator for PYMEM_DOMAIN_MEM and PYMEM_DOMAIN_OBJ domains
andusethemalloc()functionforthePYMEM_DOMAIN_RAWdomain.
Installdebughooks:
• debug: installdebughooksontopofthedefaultmemoryallocators.
• malloc_debug: sameasmallocbutalsoinstalldebughooks.
• pymalloc_debug: sameaspymallocbutalsoinstalldebughooks.
• mimalloc_debug: sameasmimallocbutalsoinstalldebughooks.
Addedinversion3.6.
Changedinversion3.7: Addedthe"default"allocator.
PYTHONMALLOCSTATS
Ifsettoanon-emptystring, Pythonwillprintstatisticsofthepymallocmemoryallocatoreverytimeanew
pymallocobjectarenaiscreated,andonshutdown.
ThisvariableisignoredifthePYTHONMALLOCenvironmentvariableisusedtoforcethemalloc()allocator
oftheClibrary,orifPythonisconfiguredwithoutpymallocsupport.
Changedinversion3.6: ThisvariablecannowalsobeusedonPythoncompiledinreleasemode. Itnowhas
noeffectifsettoanemptystring.
PYTHONLEGACYWINDOWSFSENCODING
Ifsettoanon-emptystring,thedefaultfilesystemencodinganderrorhandlermodewillreverttotheirpre-3.6
valuesof‘mbcs’and‘replace’,respectively. Otherwise,thenewdefaults‘utf-8’and‘surrogatepass’areused.
Thismayalsobeenabledatruntimewithsys._enablelegacywindowsfsencoding().
14 Chapter1. Commandlineandenvironment

### 第21页

Availability: Windows.
Addedinversion3.6: SeePEP529formoredetails.
PYTHONLEGACYWINDOWSSTDIO
Ifsettoanon-emptystring,doesnotusethenewconsolereaderandwriter. ThismeansthatUnicodecharacters
willbeencodedaccordingtotheactiveconsolecodepage,ratherthanusingutf-8.
Thisvariableisignoredifthestandardstreamsareredirected(tofilesorpipes)ratherthanreferringtoconsole
buffers.
Availability: Windows.
Addedinversion3.6.
PYTHONCOERCECLOCALE
Ifsettothevalue0,causesthemainPythoncommandlineapplicationtoskipcoercingthelegacyASCII-based
CandPOSIXlocalestoamorecapableUTF-8basedalternative.
Ifthisvariableisnot set(orissettoavalueotherthan0),theLC_ALLlocaleoverrideenvironmentvariable
isalsonotset,andthecurrentlocalereportedfortheLC_CTYPEcategoryiseitherthedefaultClocale,orelse
theexplicitlyASCII-basedPOSIXlocale,thenthePythonCLIwillattempttoconfigurethefollowinglocales
fortheLC_CTYPEcategoryintheorderlistedbeforeloadingtheinterpreterruntime:
• C.UTF-8
• C.utf8
• UTF-8
If setting one of these locale categories succeeds, then the LC_CTYPE environment variable will also be set
accordinglyinthecurrentprocessenvironmentbeforethePythonruntimeisinitialized. Thisensuresthatin
additiontobeingseenbyboththeinterpreteritselfandotherlocale-awarecomponentsrunninginthesame
process (such as the GNU readline library), the updated setting is also seen in subprocesses (regardless
of whether or not those processes are running a Python interpreter), as well as in operations that query the
environmentratherthanthecurrentClocale(suchasPython’sownlocale.getdefaultlocale()).
Configuring one of these locales (either explicitly or via the above implicit locale coercion) automatically
enablesthesurrogateescapeerrorhandlerforsys.stdinandsys.stdout(sys.stderrcontinuesto
use backslashreplace as it does in any other locale). This stream handling behavior can be overridden
usingPYTHONIOENCODINGasusual.
Fordebuggingpurposes,settingPYTHONCOERCECLOCALE=warnwillcausePythontoemitwarningmessages
onstderrifeitherthelocalecoercionactivates,orelseifalocalethatwouldhavetriggeredcoercionisstill
activewhenthePythonruntimeisinitialized.
Also note that even when locale coercion is disabled, or when it fails to find a suitable target locale,
PYTHONUTF8 will still activate by default in legacy ASCII-based locales. Both features must be disabled
inordertoforcetheinterpretertouseASCIIinsteadofUTF-8forsysteminterfaces.
Availability: Unix.
Addedinversion3.7: SeePEP538formoredetails.
PYTHONDEVMODE
Ifthisenvironmentvariableissettoanon-emptystring,enablePythonDevelopmentMode,introducingad-
ditionalruntimechecksthataretooexpensivetobeenabledbydefault. Thisisequivalenttosettingthe-X
devoption.
Addedinversion3.7.
PYTHONUTF8
Ifsetto1,enablethePythonUTF-8Mode.
Ifsetto0,disablethePythonUTF-8Mode.
Settinganyothernon-emptystringcausesanerrorduringinterpreterinitialisation.
1.2. Environmentvariables 15

### 第22页

Addedinversion3.7.
PYTHONWARNDEFAULTENCODING
Ifthisenvironmentvariableissettoanon-emptystring,issueaEncodingWarningwhenthelocale-specific
defaultencodingisused.
Seeio-encoding-warningfordetails.
Addedinversion3.10.
PYTHONNODEBUGRANGES
Ifthisvariableisset,itdisablestheinclusionofthetablesmappingextralocationinformation(endline,start
columnoffsetandendcolumnoffset)toeveryinstructionincodeobjects. Thisisusefulwhensmallercode
objectsandpycfilesaredesiredaswellassuppressingtheextravisuallocationindicatorswhentheinterpreter
displaystracebacks.
Addedinversion3.11.
PYTHONPERFSUPPORT
Ifthisvariableissettoanonzerovalue,itenablessupportfortheLinuxperfprofilersoPythoncallscanbe
detectedbyit.
Ifsetto0,disableLinuxperfprofilersupport.
Seealsothe-X perf command-lineoptionandperf_profiling.
Addedinversion3.12.
PYTHON_PERF_JIT_SUPPORT
Ifthisvariableissettoanonzerovalue,itenablessupportfortheLinuxperfprofilersoPythoncallscanbe
detectedbyitusingDWARFinformation.
Ifsetto0,disableLinuxperfprofilersupport.
Seealsothe-X perf_jitcommand-lineoptionandperf_profiling.
Addedinversion3.13.
PYTHON_DISABLE_REMOTE_DEBUG
Ifthisvariableissettoanon-emptystring, itdisablestheremotedebuggingfeaturedescribedinPEP768.
Thisincludesboththefunctionalitytoschedulecodeforexecutioninanotherprocessandthefunctionalityto
receivecodeforexecutioninthecurrentprocess.
Seealsothe-X disable_remote_debugcommand-lineoption.
Addedinversion3.14.
PYTHON_CPU_COUNT
If this variable is set to a positive integer, it overrides the return values of os.cpu_count() and os.
process_cpu_count().
Seealsothe-X cpu_countcommand-lineoption.
Addedinversion3.13.
PYTHON_FROZEN_MODULES
If this variable is set to on or off, it determines whether or not frozen modules are ignored by the import
machinery. A valueof on means theygetimportedand off means theyareignored. Thedefaultis on for
non-debug builds (the normal case) and off for debug builds. Note that the importlib_bootstrap and
importlib_bootstrap_externalfrozenmodulesarealwaysused,evenifthisflagissettooff.
Seealsothe-X frozen_modulescommand-lineoption.
Addedinversion3.13.
16 Chapter1. Commandlineandenvironment

### 第23页

PYTHON_COLORS
Ifthisvariableissetto1,theinterpreterwillcolorizevariouskindsofoutput. Settingitto0deactivatesthis
behavior. SeealsoControllingcolor.
Addedinversion3.13.
PYTHON_BASIC_REPL
Ifthisvariableissettoanyvalue,theinterpreterwillnotattempttoloadthePython-basedREPLthatrequires
cursesandreadline,andwillinsteadusethetraditionalparser-basedREPL.
Addedinversion3.13.
PYTHON_HISTORY
This environment variable can be used to set the location of a .python_history file (by default, it is .
python_historyintheuser’shomedirectory).
Addedinversion3.13.
PYTHON_GIL
Ifthisvariableissetto1,theglobalinterpreterlock(GIL)willbeforcedon. Settingitto0forcestheGILoff
(needsPythonconfiguredwiththe--disable-gilbuildoption).
Seealsothe-X gilcommand-lineoption,whichtakesprecedenceoverthisvariable,andwhatsnew313-free-
threaded-cpython.
Addedinversion3.13.
PYTHON_THREAD_INHERIT_CONTEXT
Ifthisvariableissetto1thenThreadwill,bydefault,useacopyofcontextofthecallerofThread.start()
whenstarting. Otherwise,newthreadswillstartwithanemptycontext. Ifunset,thisvariabledefaultsto1on
free-threadedbuildsandto0otherwise. Seealso-X thread_inherit_context.
Addedinversion3.14.
PYTHON_CONTEXT_AWARE_WARNINGS
If set to 1 then the warnings.catch_warnings context manager will use a ContextVar to store warn-
ings filter state. If unset, this variable defaults to 1 on free-threaded builds and to 0 otherwise. See -X
context_aware_warnings.
Addedinversion3.14.
PYTHON_JIT
Onbuildswhereexperimentaljust-in-timecompilationisavailable,thisvariablecanforcetheJITtobedisabled
(0)orenabled(1)atinterpreterstartup.
Addedinversion3.13.
PYTHON_TLBC
Ifsetto1enablesthread-localbytecode. Ifsetto0thread-localbytecodeandthespecializinginterpreterare
disabled. Onlyappliestobuildsconfiguredwith--disable-gil.
Seealsothe-X tlbccommand-lineoption.
Addedinversion3.14.
1.2.1 Debug-mode variables
PYTHONDUMPREFS
Ifset,Pythonwilldumpobjectsandreferencecountsstillaliveaftershuttingdowntheinterpreter.
NeedsPythonconfiguredwiththe--with-trace-refsbuildoption.
1.2. Environmentvariables 17

### 第24页

PYTHONDUMPREFSFILE
Ifset,Pythonwilldumpobjectsandreferencecountsstillaliveaftershuttingdowntheinterpreterintoafile
underthepathgivenasthevaluetothisenvironmentvariable.
NeedsPythonconfiguredwiththe--with-trace-refsbuildoption.
Addedinversion3.11.
PYTHON_PRESITE
If this variable is set to a module, that module will be imported early in the interpreter lifecycle, before the
site module is executed, and before the __main__ module is created. Therefore, the imported module is
nottreatedas__main__.
ThiscanbeusedtoexecutecodeearlyduringPythoninitialization.
Toimportasubmodule,usepackage.moduleasthevalue,likeinanimportstatement.
Seealsothe-X presitecommand-lineoption,whichtakesprecedenceoverthisvariable.
NeedsPythonconfiguredwiththe--with-pydebugbuildoption.
Addedinversion3.13.
18 Chapter1. Commandlineandenvironment

### 第25页

CHAPTER
TWO
USING PYTHON ON UNIX PLATFORMS
2.1 Getting and installing the latest version of Python
2.1.1 On Linux
PythoncomespreinstalledonmostLinuxdistributions, andisavailableasapackageonallothers. Howeverthere
arecertainfeaturesyoumightwanttousethatarenotavailableonyourdistro’spackage. Youcancompilethelatest
versionofPythonfromsource.
IntheeventthatthelatestversionofPythondoesn’tcomepreinstalledandisn’tintherepositoriesaswell,youcan
makepackagesforyourowndistro. Havealookatthefollowinglinks:
(cid:181) Seealso
https://www.debian.org/doc/manuals/maint-guide/first.en.html
forDebianusers
https://en.opensuse.org/Portal:Packaging
forOpenSuseusers
https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/
forFedorausers
https://slackbook.org/html/package-management-making-packages.html
forSlackwareusers
InstallingIDLE
Insomecases,IDLEmightnotbeincludedinyourPythoninstallation.
• ForDebianandUbuntuusers:
sudo apt update
sudo apt install idle
• ForFedora,RHEL,andCentOSusers:
sudo dnf install python3-idle
• ForSUSEandOpenSUSEusers:
sudo zypper install python3-idle
• ForAlpineLinuxusers:
sudo apk add python3-idle
19

### 第26页

2.1.2 On FreeBSD and OpenBSD
• FreeBSDusers,toaddthepackageuse:
pkg install python3
• OpenBSDusers,toaddthepackageuse:
pkg_add -r python
pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your␣
,→architecture here>/python-<version>.tgz
Forexamplei386usersgetthe2.5.1versionofPythonusing:
pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz
2.2 Building Python
IfyouwanttocompileCPythonyourself,firstthingyoushoulddoisgetthesource. Youcandownloadeitherthe
latestrelease’ssourceorjustgrabafreshclone. (Ifyouwanttocontributepatches,youwillneedaclone.)
Thebuildprocessconsistsoftheusualcommands:
./configure
make
make install
ConfigurationoptionsandcaveatsforspecificUnixplatformsareextensivelydocumentedintheREADME.rstfilein
therootofthePythonsourcetree.
(cid:193) Warning
make install can overwrite or masquerade the python3 binary. make altinstall is therefore recom-
mendedinsteadofmake installsinceitonlyinstallsexec_prefix/bin/pythonversion.
2.3 Python-related paths and files
These are subject to difference depending on local installation conventions; prefix and exec_prefix are
installation-dependentandshouldbeinterpretedasforGNUsoftware;theymaybethesame.
Forexample,onmostLinuxsystems,thedefaultforbothis/usr.
File/directory Meaning
exec_prefix/bin/python3 Recommendedlocationoftheinterpreter.
prefix/lib/pythonversion, Recommended locations of the directories containing the standard
exec_prefix/lib/pythonversion modules.
prefix/include/pythonversion, Recommendedlocationsofthedirectoriescontainingtheincludefiles
exec_prefix/include/ needed for developing Python extensions and embedding the inter-
pythonversion preter.
20 Chapter2. UsingPythononUnixplatforms

| (cid:193) Warning |
| --- |
| make install can overwrite or masquerade the python3 binary. make altinstall is therefore recom-
mendedinsteadofmake installsinceitonlyinstallsexec_prefix/bin/pythonversion. |


| File/directory | Meaning |
| --- | --- |
| exec_prefix/bin/python3 | Recommendedlocationoftheinterpreter. |
| prefix/lib/pythonversion,
exec_prefix/lib/pythonversion | Recommended locations of the directories containing the standard
modules. |
| prefix/include/pythonversion,
exec_prefix/include/
pythonversion | Recommendedlocationsofthedirectoriescontainingtheincludefiles
needed for developing Python extensions and embedding the inter-
preter. |

### 第27页

2.4 Miscellaneous
ToeasilyusePythonscriptsonUnix,youneedtomakethemexecutable,e.g. with
$ chmod +x script
andputanappropriateShebanglineatthetopofthescript. Agoodchoiceisusually
#!/usr/bin/env python3
whichsearchesforthePythoninterpreterinthewholePATH.However,someUnicesmaynothavetheenvcommand,
soyoumayneedtohardcode/usr/bin/python3astheinterpreterpath.
TouseshellcommandsinyourPythonscripts,lookatthesubprocessmodule.
2.5 Custom OpenSSL
1. Touseyourvendor’sOpenSSLconfigurationandsystemtruststore,locatethedirectorywithopenssl.cnf
fileorsymlinkin/etc. Onmostdistributionthefileiseitherin/etc/sslor/etc/pki/tls. Thedirectory
shouldalsocontainacert.pemfileand/oracertsdirectory.
$ find /etc/ -name openssl.cnf -printf "%h\n"
/etc/ssl
2. Download,build,andinstallOpenSSL.Makesureyouuseinstall_swandnotinstall. Theinstall_sw
targetdoesnotoverrideopenssl.cnf.
$ curl -O https://www.openssl.org/source/openssl-VERSION.tar.gz
$ tar xzf openssl-VERSION
$ pushd openssl-VERSION
$ ./config \
--prefix=/usr/local/custom-openssl \
--libdir=lib \
--openssldir=/etc/ssl
$ make -j1 depend
$ make -j8
$ make install_sw
$ popd
3. Build Python with custom OpenSSL (see the configure --with-openssl and --with-openssl-rpath
options)
$ pushd python-3.x.x
$ ./configure -C \
--with-openssl=/usr/local/custom-openssl \
--with-openssl-rpath=auto \
--prefix=/usr/local/python-3.x.x
$ make -j8
$ make altinstall
(cid:174) Note
Patch releases of OpenSSL have a backwards compatible ABI. You don’t need to recompile Python to update
OpenSSL.It’ssufficienttoreplacethecustomOpenSSLinstallationwithanewerversion.
2.4. Miscellaneous 21

### 第28页

22 Chapter2. UsingPythononUnixplatforms

### 第29页

CHAPTER
THREE
CONFIGURE PYTHON
3.1 Build Requirements
FeaturesandminimumversionsrequiredtobuildCPython:
• AC11compiler. OptionalC11featuresarenotrequired.
• OnWindows,MicrosoftVisualStudio2017orlaterisrequired.
• SupportforIEEE754floating-pointnumbersandfloating-pointNot-a-Number(NaN).
• Supportforthreads.
• OpenSSL1.1.1istheminimumversionandOpenSSL3.0.16istherecommendedminimumversionforthe
sslandhashlibextensionmodules.
• SQLite3.15.2forthesqlite3extensionmodule.
• Tcl/Tk8.5.12forthetkintermodule.
• libmpdec2.5.0forthedecimalmodule.
• Autoconf2.72andaclocal1.16.5arerequiredtoregeneratetheconfigurescript.
Changedinversion3.1: Tcl/Tkversion8.3.1isnowrequired.
Changedinversion3.5:OnWindows,VisualStudio2015orlaterisnowrequired. Tcl/Tkversion8.4isnowrequired.
Changedinversion3.6: SelectedC99featuresarenowrequired,like<stdint.h>andstatic inlinefunctions.
Changedinversion3.7: ThreadsupportandOpenSSL1.0.2arenowrequired.
Changedinversion3.10: OpenSSL1.1.1isnowrequired. RequireSQLite3.7.15.
Changedinversion3.11: C11compiler,IEEE754andNaNsupportarenowrequired. OnWindows,VisualStudio
2017orlaterisrequired. Tcl/Tkversion8.5.12isnowrequiredforthetkintermodule.
Changedinversion3.13: Autoconf2.71,aclocal1.16.5andSQLite3.15.2arenowrequired.
Changedinversion3.14: Autoconf2.72isnowrequired.
SeealsoPEP7“StyleGuideforCCode”andPEP11“CPythonplatformsupport”.
3.2 Generated files
To reduce build dependencies, Python source code contains multiple generated files. Commands to regenerate all
generatedfiles:
make regen-all
make regen-stdlib-module-names
make regen-limited-abi
make regen-configure
23

### 第30页

TheMakefile.pre.infiledocumentsgeneratedfiles,theirinputs,andtoolsusedtoregeneratethem. Searchfor
regen-*maketargets.
3.2.1 configure script
The make regen-configure command regenerates the aclocal.m4 file and the configure script using the
Tools/build/regen-configure.shshellscriptwhichusesanUbuntucontainertogetthesametoolsversions
andhaveareproducibleoutput.
Thecontainerisoptional,thefollowingcommandcanberunlocally:
autoreconf -ivf -Werror
Thegeneratedfilescanchangedependingontheexactautoconf-archive,aclocalandpkg-configversions.
3.3 Configure Options
Listallconfigurescriptoptionsusing:
./configure --help
SeealsotheMisc/SpecialBuilds.txtinthePythonsourcedistribution.
3.3.1 General Options
--enable-loadable-sqlite-extensions
Supportloadableextensionsinthe_sqliteextensionmodule(defaultisno)ofthesqlite3module.
Seethesqlite3.Connection.enable_load_extension()methodofthesqlite3module.
Addedinversion3.6.
--disable-ipv6
DisableIPv6support(enabledbydefaultifsupported),seethesocketmodule.
--enable-big-digits=[15|30]
DefinethesizeinbitsofPythonintdigits: 15or30bits.
Bydefault,thedigitsizeis30.
DefinethePYLONG_BITS_IN_DIGITto15or30.
Seesys.int_info.bits_per_digit.
--with-suffix=SUFFIX
SetthePythonexecutablesuffixtoSUFFIX.
Thedefaultsuffixis.exeonWindowsandmacOS(python.exeexecutable), .jsonEmscriptennode, .
htmlonEmscriptenbrowser,.wasmonWASI,andanemptystringonotherplatforms(pythonexecutable).
Changedinversion3.11: ThedefaultsuffixonWASMplatformisoneof.js,.htmlor.wasm.
--with-tzpath=<list of absolute paths separated by pathsep>
Selectthedefaulttimezonesearchpathforzoneinfo.TZPATH.SeetheCompile-timeconfigurationofthe
zoneinfomodule.
Default: /usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/
zoneinfo.
Seeos.pathseppathseparator.
Addedinversion3.9.
24 Chapter3. ConfigurePython

### 第31页

--without-decimal-contextvar
Buildthe_decimalextensionmoduleusingathread-localcontextratherthanacoroutine-localcontext(de-
fault),seethedecimalmodule.
Seedecimal.HAVE_CONTEXTVARandthecontextvarsmodule.
Addedinversion3.9.
--with-dbmliborder=<list of backend names>
Overrideordertocheckdbbackendsforthedbmmodule
Avalidvalueisacolon(:) separatedstringwiththebackendnames:
• ndbm;
• gdbm;
• bdb.
--without-c-locale-coercion
DisableClocalecoerciontoaUTF-8basedlocale(enabledbydefault).
Don’tdefinethePY_COERCE_C_LOCALEmacro.
SeePYTHONCOERCECLOCALEandthePEP538.
--with-platlibdir=DIRNAME
Pythonlibrarydirectoryname(defaultislib).
FedoraandSuSEuselib64on64-bitplatforms.
Seesys.platlibdir.
Addedinversion3.9.
--with-wheel-pkg-dir=PATH
Directoryofwheelpackagesusedbytheensurepipmodule(nonebydefault).
SomeLinuxdistributionpackagingpoliciesrecommendagainstbundlingdependencies. Forexample,Fedora
installswheelpackagesinthe/usr/share/python-wheels/directoryanddon’tinstalltheensurepip.
_bundledpackage.
Addedinversion3.10.
--with-pkg-config=[check|yes|no]
Whetherconfigureshouldusepkg-configtodetectbuilddependencies.
• check(default): pkg-configisoptional
• yes: pkg-configismandatory
• no: configuredoesnotusepkg-configevenwhenpresent
Addedinversion3.11.
--enable-pystats
TurnoninternalPythonperformancestatisticsgathering.
Bydefault, statisticsgatheringisoff. Usepython3 -X pystatscommandorsetPYTHONSTATS=1envi-
ronmentvariabletoturnonstatisticsgatheringatPythonstartup.
AtPythonexit,dumpstatisticsifstatisticsgatheringwasonandnotcleared.
Effects:
• Add-X pystatscommandlineoption.
• AddPYTHONSTATSenvironmentvariable.
• DefinethePy_STATSmacro.
3.3. ConfigureOptions 25

### 第32页

• Addfunctionstothesysmodule:
– sys._stats_on(): Turnsonstatisticsgathering.
– sys._stats_off(): Turnsoffstatisticsgathering.
– sys._stats_clear(): Clearsthestatistics.
– sys._stats_dump(): Dumpstatisticstofile,andclearsthestatistics.
Thestatisticswillbedumpedtoaarbitrary(probablyunique)filein/tmp/py_stats/(Unix)orC:\temp\
py_stats\(Windows). Ifthatdirectorydoesnotexist,resultswillbeprintedonstderr.
UseTools/scripts/summarize_stats.pytoreadthestats.
Statistics:
• Opcode:
– Specialization: success,failure,hit,deferred,miss,deopt,failures;
– Executioncount;
– Paircount.
• Call:
– InlinedPythoncalls;
– PyEvalcalls;
– Framespushed;
– Frameobjectcreated;
– Evalcalls: vector,generator,legacy,functionVECTORCALL,buildclass,slot,function“ex”,API,
method.
• Object:
– increfanddecref;
– interpreterincrefanddecref;
– allocations: all,512bytes,4kiB,big;
– free;
– to/fromfreelists;
– dictionarymaterialized/dematerialized;
– typecache;
– optimizationattempts;
– optimizationtracescreated/executed;
– uopsexecuted.
• Garbagecollector:
– Garbagecollections;
– Objectsvisited;
– Objectscollected.
Addedinversion3.11.
26 Chapter3. ConfigurePython

### 第33页

--disable-gil
EnablessupportforrunningPythonwithouttheglobalinterpreterlock(GIL):freethreadingbuild.
DefinesthePy_GIL_DISABLEDmacroandadds"t"tosys.abiflags.
Seewhatsnew313-free-threaded-cpythonformoredetail.
Addedinversion3.13.
--enable-experimental-jit=[no|yes|yes-off|interpreter]
Indicatehowtointegratetheexperimentaljust-in-timecompiler.
• no: Don’tbuildtheJIT.
• yes: EnabletheJIT.Todisableitatruntime,settheenvironmentvariablePYTHON_JIT=0.
• yes-off: BuildtheJIT,butdisableitbydefault. Toenableitatruntime,settheenvironmentvariable
PYTHON_JIT=1.
• interpreter: Enablethe“JITinterpreter”(onlyusefulforthosedebuggingtheJITitself). Todisable
itatruntime,settheenvironmentvariablePYTHON_JIT=0.
--enable-experimental-jit=no is the default behavior if the option is not provided, and
--enable-experimental-jit is shorthand for --enable-experimental-jit=yes. See Tools/
jit/README.mdformoreinformation,includinghowtoinstallthenecessarybuild-timedependencies.
(cid:174) Note
WhenbuildingCPythonwithJITenabled,ensurethatyoursystemhasPython3.11orlaterinstalled.
Addedinversion3.13.
PKG_CONFIG
Pathtopkg-configutility.
PKG_CONFIG_LIBDIR
PKG_CONFIG_PATH
pkg-configoptions.
3.3.2 C compiler options
CC
Ccompilercommand.
CFLAGS
Ccompilerflags.
CPP
Cpreprocessorcommand.
CPPFLAGS
Cpreprocessorflags,e.g. -Iinclude_dir.
3.3.3 Linker options
LDFLAGS
Linkerflags,e.g. -Llibrary_directory.
LIBS
Librariestopasstothelinker,e.g. -llibrary.
3.3. ConfigureOptions 27

### 第34页

MACHDEP
Nameformachine-dependentlibraryfiles.
3.3.4 Options for third-party dependencies
Addedinversion3.11.
BZIP2_CFLAGS
BZIP2_LIBS
CcompilerandlinkerflagstolinkPythontolibbz2,usedbybz2module,overridingpkg-config.
CURSES_CFLAGS
CURSES_LIBS
C compiler and linker flags for libncurses or libncursesw, used by curses module, overriding
pkg-config.
GDBM_CFLAGS
GDBM_LIBS
Ccompilerandlinkerflagsforgdbm.
LIBB2_CFLAGS
LIBB2_LIBS
Ccompilerandlinkerflagsforlibb2(BLAKE2),usedbyhashlibmodule,overridingpkg-config.
LIBEDIT_CFLAGS
LIBEDIT_LIBS
Ccompilerandlinkerflagsforlibedit,usedbyreadlinemodule,overridingpkg-config.
LIBFFI_CFLAGS
LIBFFI_LIBS
Ccompilerandlinkerflagsforlibffi,usedbyctypesmodule,overridingpkg-config.
LIBMPDEC_CFLAGS
LIBMPDEC_LIBS
Ccompilerandlinkerflagsforlibmpdec,usedbydecimalmodule,overridingpkg-config.
(cid:174) Note
Theseenvironmentvariableshavenoeffectunless--with-system-libmpdecisspecified.
LIBLZMA_CFLAGS
LIBLZMA_LIBS
Ccompilerandlinkerflagsforliblzma,usedbylzmamodule,overridingpkg-config.
LIBREADLINE_CFLAGS
LIBREADLINE_LIBS
Ccompilerandlinkerflagsforlibreadline,usedbyreadlinemodule,overridingpkg-config.
LIBSQLITE3_CFLAGS
LIBSQLITE3_LIBS
Ccompilerandlinkerflagsforlibsqlite3,usedbysqlite3module,overridingpkg-config.
28 Chapter3. ConfigurePython

### 第35页

LIBUUID_CFLAGS
LIBUUID_LIBS
Ccompilerandlinkerflagsforlibuuid,usedbyuuidmodule,overridingpkg-config.
LIBZSTD_CFLAGS
LIBZSTD_LIBS
Ccompilerandlinkerflagsforlibzstd,usedbycompression.zstdmodule,overridingpkg-config.
Addedinversion3.14.
PANEL_CFLAGS
PANEL_LIBS
CcompilerandlinkerflagsforPANEL,overridingpkg-config.
C compiler and linker flags for libpanel or libpanelw, used by curses.panel module, overriding
pkg-config.
TCLTK_CFLAGS
TCLTK_LIBS
CcompilerandlinkerflagsforTCLTK,overridingpkg-config.
ZLIB_CFLAGS
ZLIB_LIBS
Ccompilerandlinkerflagsforlibzlib,usedbygzipmodule,overridingpkg-config.
3.3.5 WebAssembly Options
--enable-wasm-dynamic-linking
TurnondynamiclinkingsupportforWASM.
Dynamiclinkingenablesdlopen. Filesizeoftheexecutableincreasesduetolimiteddeadcodeelimination
andadditionalfeatures.
Addedinversion3.11.
--enable-wasm-pthreads
TurnonpthreadssupportforWASM.
Addedinversion3.11.
3.3.6 Install Options
--prefix=PREFIX
Installarchitecture-independentfilesinPREFIX.OnUnix,itdefaultsto/usr/local.
Thisvaluecanberetrievedatruntimeusingsys.prefix.
Asanexample,onecanuse--prefix="$HOME/.local/"toinstallaPythoninitshomedirectory.
--exec-prefix=EPREFIX
Installarchitecture-dependentfilesinEPREFIX,defaultsto--prefix.
Thisvaluecanberetrievedatruntimeusingsys.exec_prefix.
--disable-test-modules
Don’t build nor install test modules, like the test package or the _testcapi extension module (built and
installedbydefault).
Addedinversion3.10.
3.3. ConfigureOptions 29

### 第36页

--with-ensurepip=[upgrade|install|no]
SelecttheensurepipcommandrunonPythoninstallation:
• upgrade(default): runpython -m ensurepip --altinstall --upgradecommand.
• install: runpython -m ensurepip --altinstallcommand;
• no: don’trunensurepip;
Addedinversion3.6.
3.3.7 Performance options
ConfiguringPythonusing--enable-optimizations --with-lto(PGO+LTO)isrecommendedforbestper-
formance. Theexperimental--enable-boltflagcanalsobeusedtoimproveperformance.
--enable-optimizations
EnableProfileGuidedOptimization(PGO)usingPROFILE_TASK (disabledbydefault).
TheCcompilerClangrequiresllvm-profdataprogramforPGO.OnmacOS,GCCalsorequiresit: GCC
isjustanaliastoClangonmacOS.
Disable also semantic interposition in libpython if --enable-shared and GCC is used: add
-fno-semantic-interpositiontothecompilerandlinkerflags.
(cid:174) Note
During the build, you may encounter compiler warnings about profile data not being available for
some source files. These warnings are harmless, as only a subset of the code is exercised dur-
ing profile data acquisition. To disable these warnings on Clang, manually suppress them by adding
-Wno-profile-instr-unprofiledtoCFLAGS.
Addedinversion3.6.
Changedinversion3.10: Use-fno-semantic-interpositiononGCC.
PROFILE_TASK
EnvironmentvariableusedintheMakefile: PythoncommandlineargumentsforthePGOgenerationtask.
Default: -m test --pgo --timeout=$(TESTTIMEOUT).
Addedinversion3.8.
Changedinversion3.13: Taskfailureisnolongerignoredsilently.
--with-lto=[full|thin|no|yes]
EnableLinkTimeOptimization(LTO)inanybuild(disabledbydefault).
TheCcompilerClangrequiresllvm-arforLTO(aronmacOS),aswellasanLTO-awarelinker(ld.gold
orlld).
Addedinversion3.6.
Addedinversion3.11: TouseThinLTOfeature,use--with-lto=thinonClang.
Changedinversion3.12: UseThinLTOasthedefaultoptimizationpolicyonClangifthecompileraccepts
theflag.
--enable-bolt
EnableusageoftheBOLTpost-linkbinaryoptimizer(disabledbydefault).
BOLTispartoftheLLVMprojectbutisnotalwaysincludedintheirbinarydistributions. Thisflagrequires
thatllvm-boltandmerge-fdataareavailable.
BOLT is still a fairly new project so this flag should be considered experimental for now. Because this tool
operates on machine code its success is dependent on a combination of the build environment + the other
30 Chapter3. ConfigurePython

### 第37页

optimizationconfigureargs+theCPUarchitecture,andnotallcombinationsaresupported. BOLTversions
before LLVM 16 are known to crash BOLT under some scenarios. Use of LLVM 16 or newer for BOLT
optimizationisstronglyencouraged.
TheBOLT_INSTRUMENT_FLAGSandBOLT_APPLY_FLAGSconfigurevariablescanbedefinedtooverride
thedefaultsetofargumentsforllvm-bolttoinstrumentandapplyBOLTdatatobinaries,respectively.
Addedinversion3.12.
BOLT_APPLY_FLAGS
Argumentstollvm-boltwhencreatingaBOLToptimizedbinary.
Addedinversion3.12.
BOLT_INSTRUMENT_FLAGS
Argumentstollvm-boltwheninstrumentingbinaries.
Addedinversion3.12.
--with-computed-gotos
Enablecomputedgotosinevaluationloop(enabledbydefaultonsupportedcompilers).
--with-tail-call-interp
EnableinterpretersusingtailcallsinCPython. Ifenabled,enablingPGO(--enable-optimizations)is
highly recommended. This option specifically requires a C compiler with proper tail call support, and the
preserve_nonecallingconvention. Forexample,Clang19andnewersupportsthisfeature.
Addedinversion3.14.
--without-mimalloc
Disablethefastmimallocallocator(enabledbydefault).
SeealsoPYTHONMALLOCenvironmentvariable.
--without-pymalloc
DisablethespecializedPythonmemoryallocatorpymalloc(enabledbydefault).
SeealsoPYTHONMALLOCenvironmentvariable.
--without-doc-strings
Disable static documentation strings to reduce the memory footprint (enabled by default). Documentation
stringsdefinedinPythonarenotaffected.
Don’tdefinetheWITH_DOC_STRINGSmacro.
SeethePyDoc_STRVAR()macro.
--enable-profiling
EnableC-levelcodeprofilingwithgprof(disabledbydefault).
--with-strict-overflow
Add-fstrict-overflowtotheCcompilerflags(bydefaultweadd-fno-strict-overflowinstead).
--without-remote-debug
DeactivateremotedebuggingsupportdescribedinPEP768(enabledbydefault). Whenthisflagisprovided
thecodethatallowstheinterpretertoscheduletheexecutionofaPythonfileinaseparateprocessasdescribed
in PEP 768 is not compiled. This includes both the functionality to schedule code to be executed and the
functionalitytoreceivecodetobeexecuted.
Py_REMOTE_DEBUG
Thismacroisdefinedbydefault,unlessPythonisconfiguredwith--without-remote-debug.
Note that even if the macro is defined, remote debugging may not be available (for example, on an
incompatibleplatform).
Addedinversion3.14.
3.3. ConfigureOptions 31

### 第38页

3.3.8 Python Debug Build
AdebugbuildisPythonbuiltwiththe--with-pydebugconfigureoption.
Effectsofadebugbuild:
• Displayallwarningsbydefault: thelistofdefaultwarningfiltersisemptyinthewarningsmodule.
• Adddtosys.abiflags.
• Addsys.gettotalrefcount()function.
• Add-X showrefcountcommandlineoption.
• Add-dcommandlineoptionandPYTHONDEBUGenvironmentvariabletodebugtheparser.
• Addsupportforthe__lltrace__variable: enablelow-leveltracinginthebytecodeevaluationloopifthe
variableisdefined.
• Installdebughooksonmemoryallocatorstodetectbufferoverflowandothermemoryerrors.
• DefinePy_DEBUGandPy_REF_DEBUGmacros.
• Add runtime checks: code surrounded by #ifdef Py_DEBUG and #endif. Enable assert(...) and
_PyObject_ASSERT(...) assertions: don’t set the NDEBUG macro (see also the --with-assertions
configureoption). Mainruntimechecks:
– Addsanitychecksonthefunctionarguments.
– Unicodeandintobjectsarecreatedwiththeirmemoryfilledwithapatterntodetectusageofuninitialized
objects.
– Ensurethatfunctionswhichcanclearorreplacethecurrentexceptionarenotcalledwithanexception
raised.
– Checkthatdeallocatorfunctionsdon’tchangethecurrentexception.
– Thegarbagecollector(gc.collect()function)runssomebasicchecksonobjectsconsistency.
– ThePy_SAFE_DOWNCAST()macrochecksforintegerunderflowandoverflowwhendowncastingfrom
widetypestonarrowtypes.
SeealsothePythonDevelopmentModeandthe--with-trace-refsconfigureoption.
Changedinversion3.8: ReleasebuildsanddebugbuildsarenowABIcompatible: definingthePy_DEBUGmacrono
longerimpliesthePy_TRACE_REFSmacro(seethe--with-trace-refsoption).
3.3.9 Debug options
--with-pydebug
BuildPythonindebugmode: definethePy_DEBUGmacro(disabledbydefault).
--with-trace-refs
Enabletracingreferencesfordebuggingpurpose(disabledbydefault).
Effects:
• DefinethePy_TRACE_REFSmacro.
• Addsys.getobjects()function.
• AddPYTHONDUMPREFSenvironmentvariable.
ThePYTHONDUMPREFSenvironmentvariablecanbeusedtodumpobjectsandreferencecountsstillaliveat
Pythonexit.
Staticallyallocatedobjectsarenottraced.
Addedinversion3.8.
Changedinversion3.13: ThisbuildisnowABIcompatiblewithreleasebuildanddebugbuild.
32 Chapter3. ConfigurePython

### 第39页

--with-assertions
BuildwithCassertionsenabled(defaultisno): assert(...);and_PyObject_ASSERT(...);.
Ifset,theNDEBUGmacroisnotdefinedintheOPTcompilervariable.
Seealsothe--with-pydebugoption(debugbuild)whichalsoenablesassertions.
Addedinversion3.6.
--with-valgrind
EnableValgrindsupport(defaultisno).
--with-dtrace
EnableDTracesupport(defaultisno).
SeeInstrumentingCPythonwithDTraceandSystemTap.
Addedinversion3.6.
--with-address-sanitizer
EnableAddressSanitizermemoryerrordetector,asan(defaultisno). ToimproveASandetectioncapabili-
tiesyoumayalsowanttocombinethiswith--without-pymalloctodisablethespecializedsmall-object
allocatorwhoseallocationsarenottrackedbyASan.
Addedinversion3.6.
--with-memory-sanitizer
EnableMemorySanitizerallocationerrordetector,msan(defaultisno).
Addedinversion3.6.
--with-undefined-behavior-sanitizer
EnableUndefinedBehaviorSanitizerundefinedbehaviourdetector,ubsan(defaultisno).
Addedinversion3.6.
--with-thread-sanitizer
EnableThreadSanitizerdataracedetector,tsan(defaultisno).
Addedinversion3.13.
3.3.10 Linker options
--enable-shared
EnablebuildingasharedPythonlibrary: libpython(defaultisno).
--without-static-libpython
DonotbuildlibpythonMAJOR.MINOR.aanddonotinstallpython.o(builtandenabledbydefault).
Addedinversion3.10.
3.3.11 Libraries options
--with-libs='lib1 ...'
Linkagainstadditionallibraries(defaultisno).
--with-system-expat
Buildthepyexpatmoduleusinganinstalledexpatlibrary(defaultisno).
--with-system-libmpdec
Buildthe_decimalextensionmoduleusinganinstalledmpdecimallibrary,seethedecimalmodule(default
isyes).
Addedinversion3.3.
Changedinversion3.13: Defaulttousingtheinstalledmpdecimallibrary.
3.3. ConfigureOptions 33

### 第40页

Deprecated since version 3.13, will be removed in version 3.15: A copy of the mpdecimal library sources
willnolongerbedistributedwithPython3.15.
(cid:181) Seealso
LIBMPDEC_CFLAGSandLIBMPDEC_LIBS.
--with-readline=readline|editline
Designateabackendlibraryforthereadlinemodule.
• readline: Usereadlineasthebackend.
• editline: Useeditlineasthebackend.
Addedinversion3.10.
--without-readline
Don’tbuildthereadlinemodule(builtbydefault).
Don’tdefinetheHAVE_LIBREADLINEmacro.
Addedinversion3.10.
--with-libm=STRING
OverridelibmmathlibrarytoSTRING(defaultissystem-dependent).
--with-libc=STRING
OverridelibcClibrarytoSTRING(defaultissystem-dependent).
--with-openssl=DIR
RootoftheOpenSSLdirectory.
Addedinversion3.7.
--with-openssl-rpath=[no|auto|DIR]
Setruntimelibrarydirectory(rpath)forOpenSSLlibraries:
• no(default): don’tsetrpath;
• auto: auto-detectrpathfrom--with-opensslandpkg-config;
• DIR:setanexplicitrpath.
Addedinversion3.10.
3.3.12 Security Options
--with-hash-algorithm=[fnv|siphash13|siphash24]
SelecthashalgorithmforuseinPython/pyhash.c:
• siphash13(default);
• siphash24;
• fnv.
Addedinversion3.4.
Addedinversion3.11: siphash13isaddedanditisthenewdefault.
--with-builtin-hashlib-hashes=md5,sha1,sha256,sha512,sha3,blake2
Built-inhashmodules:
• md5;
• sha1;
34 Chapter3. ConfigurePython

| (cid:181) Seealso |
| --- |
| LIBMPDEC_CFLAGSandLIBMPDEC_LIBS. |

### 第41页

• sha256;
• sha512;
• sha3(withshake);
• blake2.
Addedinversion3.9.
--with-ssl-default-suites=[python|openssl|STRING]
OverridetheOpenSSLdefaultciphersuitesstring:
• python(default): usePython’spreferredselection;
• openssl: leaveOpenSSL’sdefaultsuntouched;
• STRING:useacustomstring
Seethesslmodule.
Addedinversion3.7.
Changedinversion3.10: ThesettingspythonandSTRINGalsosetTLS1.2asminimumprotocolversion.
--disable-safety
DisablecompileroptionsthatarerecommendedbyOpenSSFforsecurityreasonswithnoperformanceover-
head. Ifthisoptionisnotenabled,CPythonwillbebuiltbasedonsafetycompileroptionswithnoslowdown.
Whenthisoptionisenabled,CPythonwillnotbebuiltwiththecompileroptionslistedbelow.
Thefollowingcompileroptionsaredisabledwith--disable-safety:
• -fstack-protector-strong: Enablerun-timechecksforstack-basedbufferoverflows.
• -Wtrampolines: Enablewarningsabouttrampolinesthatrequireexecutablestacks.
Addedinversion3.14.
--enable-slower-safety
EnablecompileroptionsthatarerecommendedbyOpenSSFforsecurityreasonswhichrequireoverhead. If
this option is not enabled, CPython will not be built based on safety compiler options which performance
impact. Whenthisoptionisenabled,CPythonwillbebuiltwiththecompileroptionslistedbelow.
Thefollowingcompileroptionsareenabledwith--enable-slower-safety:
• -D_FORTIFY_SOURCE=3: Fortify sources with compile- and run-time checks for unsafe libc usage
andbufferoverflows.
Addedinversion3.14.
3.3.13 macOS Options
SeeMac/README.rst.
--enable-universalsdk
--enable-universalsdk=SDKDIR
Create a universal binary build. SDKDIR specifies which macOS SDK should be used to perform the build
(defaultisno).
--enable-framework
--enable-framework=INSTALLDIR
CreateaPython.frameworkratherthanatraditionalUnixinstall. OptionalINSTALLDIRspecifiestheinstal-
lationpath(defaultisno).
3.3. ConfigureOptions 35

### 第42页

--with-universal-archs=ARCH
Specify the kind of universal binary that should be created. This option is only valid when
--enable-universalsdkisset.
Options:
• universal2(x86-64andarm64);
• 32-bit(PPCandi386);
• 64-bit(PPC64andx86-64);
• 3-way(i386,PPCandx86-64);
• intel(i386andx86-64);
• intel-32(i386);
• intel-64(x86-64);
• all(PPC,i386,PPC64andx86-64).
Notethatvaluesforthisconfigurationitemarenotthesameastheidentifiersusedforuniversalbinarywheels
onmacOS.SeethePythonPackagingUserGuidefordetailsonthepackagingplatformcompatibilitytagsused
onmacOS
--with-framework-name=FRAMEWORK
SpecifythenameforthepythonframeworkonmacOSonlyvalidwhen--enable-frameworkisset(default:
Python).
--with-app-store-compliance
--with-app-store-compliance=PATCH-FILE
ThePythonstandardlibrarycontainsstringsthatareknowntotriggerautomatedinspectiontoolerrorswhen
submitted for distribution by the macOS and iOS App Stores. If enabled, this option will apply the list of
patchesthatareknowntocorrectappstorecompliance. Acustompatchfilecanalsobespecified. Thisoption
isdisabledbydefault.
Addedinversion3.13.
3.3.14 iOS Options
SeeiOS/README.rst.
--enable-framework=INSTALLDIR
Create a Python.framework. Unlike macOS, the INSTALLDIR argument specifying the installation path is
mandatory.
--with-framework-name=FRAMEWORK
Specifythenamefortheframework(default: Python).
3.3.15 Cross Compiling Options
Crosscompiling,alsoknownascrossbuilding,canbeusedtobuildPythonforanotherCPUarchitectureorplatform.
CrosscompilingrequiresaPythoninterpreterforthebuildplatform. TheversionofthebuildPythonmustmatch
theversionofthecrosscompiledhostPython.
--build=BUILD
configureforbuildingonBUILD,usuallyguessedbyconfig.guess.
--host=HOST
cross-compiletobuildprogramstorunonHOST(targetplatform)
36 Chapter3. ConfigurePython

### 第43页

--with-build-python=path/to/python
pathtobuildpythonbinaryforcrosscompiling
Addedinversion3.11.
CONFIG_SITE=file
Anenvironmentvariablethatpointstoafilewithconfigureoverrides.
Exampleconfig.sitefile:
# config.site-aarch64
ac_cv_buggy_getaddrinfo=no
ac_cv_file__dev_ptmx=yes
ac_cv_file__dev_ptc=no
HOSTRUNNER
ProgramtorunCPythonforthehostplatformforcross-compilation.
Addedinversion3.11.
Crosscompilingexample:
CONFIG_SITE=config.site-aarch64 ../configure \
--build=x86_64-pc-linux-gnu \
--host=aarch64-unknown-linux-gnu \
--with-build-python=../x86_64/python
3.4 Python Build System
3.4.1 Main files of the build system
• configure.ac=>configure;
• Makefile.pre.in=>Makefile(createdbyconfigure);
• pyconfig.h(createdbyconfigure);
• Modules/Setup: CextensionsbuiltbytheMakefileusingModule/makesetupshellscript;
3.4.2 Main build steps
• Cfiles(.c)arebuiltasobjectfiles(.o).
• Astaticlibpythonlibrary(.a)iscreatedfromobjectsfiles.
• python.oandthestaticlibpythonlibraryarelinkedintothefinalpythonprogram.
• CextensionsarebuiltbytheMakefile(seeModules/Setup).
3.4.3 Main Makefile targets
make
Forthemostpart,whenrebuildingaftereditingsomecodeorrefreshingyourcheckoutfromupstream,allyouneed
todoisexecutemake,which(perMake’ssemantics)buildsthedefaulttarget,thefirstonedefinedintheMakefile.
By tradition (including in the CPython project) this is usually the all target. The configure script expands an
autoconfvariable,@DEF_MAKE_ALL_RULE@todescribepreciselywhichtargetsmake allwillbuild. Thethree
choicesare:
• profile-opt(configuredwith--enable-optimizations)
• build_wasm(chosenifthehostplatformmatcheswasm32-wasi*orwasm32-emscripten)
• build_all(configuredwithoutexplicitlyusingeitheroftheothers)
3.4. PythonBuildSystem 37

### 第44页

Dependingonthemostrecentsourcefilechanges,Makewillrebuildanytargets(objectfilesandexecutables)deemed
out-of-date,includingrunningconfigureagainifnecessary. Source/targetdependenciesaremanyandmaintained
manuallyhowever,soMakesometimesdoesn’thavealltheinformationnecessarytocorrectlydetectalltargetswhich
needtoberebuilt. Dependingonwhichtargetsaren’trebuilt,youmightexperienceanumberofproblems. Ifyou
have build or test problems which you can’t otherwise explain, make clean && make should work around most
dependencyproblems,attheexpenseoflongerbuildtimes.
makeplatform
Build the python program, but don’t build the standard library extension modules. This generates a file named
platformwhichcontainsasinglelinedescribingthedetailsofthebuildplatform,e.g.,macosx-14.3-arm64-3.
12orlinux-x86_64-3.13.
makeprofile-opt
Build Python using profile-guided optimization (PGO). You can use the configure --enable-optimizations
optiontomakethisthedefaulttargetofthemakecommand(make allorjustmake).
makeclean
Removebuiltfiles.
makedistclean
Inadditiontotheworkdonebymake clean,removefilescreatedbytheconfigurescript. configurewillhaveto
berunbeforebuildingagain.1
makeinstall
BuildthealltargetandinstallPython.
maketest
BuildthealltargetandrunthePythontestsuitewiththe--fast-cioptionwithoutGUItests. Variables:
• TESTOPTS:additionalregrtestcommand-lineoptions.
• TESTPYTHONOPTS:additionalPythoncommand-lineoptions.
• TESTTIMEOUT:timeoutinseconds(default: 10minutes).
makeci
Thisissimilartomake test,butusesthe-uguitoalsorunGUItests.
Addedinversion3.14.
makebuildbottest
This is similar to make test, but uses the --slow-ci option and default timeout of 20 minutes, instead of
--fast-cioption.
makeregen-all
Regenerate(almost)allgeneratedfiles. Theseinclude(butarenotlimitedto)bytecodecases,andparsergenerator
file. make regen-stdlib-module-names and autoconf must be run separately for the remaining generated
files.
1git clean -fdxisanevenmoreextremewayto“clean”yourcheckout. ItremovesallfilesnotknowntoGit. Whenbughuntingusing
git bisect,thisisrecommendedbetweenprobestoguaranteeacompletelycleanbuild. Usewithcare,asitwilldeleteallfilesnotchecked
intoGit,includingyournew,uncommittedwork.
38 Chapter3. ConfigurePython

### 第45页

3.4.4 C extensions
Some C extensions are built as built-in modules, like the sys module. They are built with the
Py_BUILD_CORE_BUILTINmacrodefined. Built-inmoduleshaveno__file__attribute:
>>> import sys
>>> sys
<module 'sys' (built-in)>
>>> sys.__file__
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute '__file__'
Other C extensions are built as dynamic libraries, like the _asyncio module. They are built with the
Py_BUILD_CORE_MODULEmacrodefined. ExampleonLinuxx86-64:
>>> import _asyncio
>>> _asyncio
<module '_asyncio' from '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_
,→64-linux-gnu.so'>
>>> _asyncio.__file__
'/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'
Modules/SetupisusedtogenerateMakefiletargetstobuildCextensions. Atthebeginningofthefiles,Cextensions
arebuiltasbuilt-inmodules. Extensionsdefinedafterthe*shared*markerarebuiltasdynamiclibraries.
The PyAPI_FUNC(), PyAPI_DATA() and PyMODINIT_FUNC macros of Include/exports.h are defined dif-
ferentlydependingifthePy_BUILD_CORE_MODULEmacroisdefined:
• UsePy_EXPORTED_SYMBOLifthePy_BUILD_CORE_MODULEisdefined
• UsePy_IMPORTED_SYMBOLotherwise.
If the Py_BUILD_CORE_BUILTIN macro is used by mistake on a C extension built as a shared library, its
PyInit_xxx()functionisnotexported,causinganImportErroronimport.
3.5 Compiler and linker flags
Optionssetbythe./configurescriptandenvironmentvariablesandusedbyMakefile.
3.5.1 Preprocessor flags
CONFIGURE_CPPFLAGS
ValueofCPPFLAGSvariablepassedtothe./configurescript.
Addedinversion3.6.
CPPFLAGS
(Objective)C/C++preprocessorflags,e.g. -Iinclude_dirifyouhaveheadersinanonstandarddirectory
include_dir.
BothCPPFLAGS andLDFLAGS needtocontaintheshell’svaluetobeabletobuildextensionmodulesusing
thedirectoriesspecifiedintheenvironmentvariables.
BASECPPFLAGS
Addedinversion3.4.
PY_CPPFLAGS
Extrapreprocessorflagsaddedforbuildingtheinterpreterobjectfiles.
Default: $(BASECPPFLAGS) -I. -I$(srcdir)/Include $(CONFIGURE_CPPFLAGS)
$(CPPFLAGS).
3.5. Compilerandlinkerflags 39

### 第46页

Addedinversion3.2.
3.5.2 Compiler flags
CC
Ccompilercommand.
Example: gcc -pthread.
CXX
C++compilercommand.
Example: g++ -pthread.
CFLAGS
Ccompilerflags.
CFLAGS_NODIST
CFLAGS_NODIST is used for building the interpreter and stdlib C extensions. Use it when a compiler flag
shouldnotbepartofCFLAGSoncePythonisinstalled(gh-65320).
Inparticular,CFLAGSshouldnotcontain:
• thecompilerflag-I(forsettingthesearchpathforincludefiles). The-Iflagsareprocessedfromleft
toright,andanyflagsinCFLAGSwouldtakeprecedenceoveruser-andpackage-supplied-Iflags.
• hardening flags such as -Werror because distributions cannot control whether packages installed by
usersconformtosuchheightenedstandards.
Addedinversion3.5.
COMPILEALL_OPTS
OptionspassedtothecompileallcommandlinewhenbuildingPYCfilesinmake install. Default: -j0.
Addedinversion3.12.
EXTRA_CFLAGS
ExtraCcompilerflags.
CONFIGURE_CFLAGS
ValueofCFLAGSvariablepassedtothe./configurescript.
Addedinversion3.2.
CONFIGURE_CFLAGS_NODIST
ValueofCFLAGS_NODISTvariablepassedtothe./configurescript.
Addedinversion3.5.
BASECFLAGS
Basecompilerflags.
OPT
Optimizationflags.
CFLAGS_ALIASING
Strictornon-strictaliasingflagsusedtocompilePython/dtoa.c.
Addedinversion3.7.
CCSHARED
Compilerflagsusedtobuildasharedlibrary.
Forexample,-fPICisusedonLinuxandonBSD.
40 Chapter3. ConfigurePython

### 第47页

CFLAGSFORSHARED
ExtraCflagsaddedforbuildingtheinterpreterobjectfiles.
Default: $(CCSHARED)when--enable-sharedisused,oranemptystringotherwise.
PY_CFLAGS
Default: $(BASECFLAGS) $(OPT) $(CONFIGURE_CFLAGS) $(CFLAGS) $(EXTRA_CFLAGS).
PY_CFLAGS_NODIST
Default: $(CONFIGURE_CFLAGS_NODIST) $(CFLAGS_NODIST) -I$(srcdir)/Include/internal.
Addedinversion3.5.
PY_STDMODULE_CFLAGS
Cflagsusedforbuildingtheinterpreterobjectfiles.
Default: $(PY_CFLAGS) $(PY_CFLAGS_NODIST) $(PY_CPPFLAGS) $(CFLAGSFORSHARED).
Addedinversion3.7.
PY_CORE_CFLAGS
Default: $(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE.
Addedinversion3.2.
PY_BUILTIN_MODULE_CFLAGS
Compilerflagstobuildastandardlibraryextensionmoduleasabuilt-inmodule,liketheposixmodule.
Default: $(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN.
Addedinversion3.8.
PURIFY
Purifycommand. Purifyisamemorydebuggerprogram.
Default: emptystring(notused).
3.5.3 Linker flags
LINKCC
Linkercommandusedtobuildprogramslikepythonand_testembed.
Default: $(PURIFY) $(CC).
CONFIGURE_LDFLAGS
ValueofLDFLAGSvariablepassedtothe./configurescript.
AvoidassigningCFLAGS,LDFLAGS,etc. souserscanusethemonthecommandlinetoappendtothesevalues
withoutstompingthepre-setvalues.
Addedinversion3.2.
LDFLAGS_NODIST
LDFLAGS_NODIST isusedinthesamemannerasCFLAGS_NODIST.Useitwhenalinkerflagshouldnot be
partofLDFLAGSoncePythonisinstalled(gh-65320).
Inparticular,LDFLAGSshouldnotcontain:
• thecompilerflag-L(forsettingthesearchpathforlibraries). The-Lflagsareprocessedfromleftto
right,andanyflagsinLDFLAGSwouldtakeprecedenceoveruser-andpackage-supplied-Lflags.
CONFIGURE_LDFLAGS_NODIST
ValueofLDFLAGS_NODISTvariablepassedtothe./configurescript.
Addedinversion3.8.
3.5. Compilerandlinkerflags 41

### 第48页

LDFLAGS
Linkerflags,e.g. -Llib_dirifyouhavelibrariesinanonstandarddirectorylib_dir.
BothCPPFLAGS andLDFLAGS needtocontaintheshell’svaluetobeabletobuildextensionmodulesusing
thedirectoriesspecifiedintheenvironmentvariables.
LIBS
LinkerflagstopasslibrariestothelinkerwhenlinkingthePythonexecutable.
Example: -lrt.
LDSHARED
Commandtobuildasharedlibrary.
Default: @LDSHARED@ $(PY_LDFLAGS).
BLDSHARED
Commandtobuildlibpythonsharedlibrary.
Default: @BLDSHARED@ $(PY_CORE_LDFLAGS).
PY_LDFLAGS
Default: $(CONFIGURE_LDFLAGS) $(LDFLAGS).
PY_LDFLAGS_NODIST
Default: $(CONFIGURE_LDFLAGS_NODIST) $(LDFLAGS_NODIST).
Addedinversion3.8.
PY_CORE_LDFLAGS
Linkerflagsusedforbuildingtheinterpreterobjectfiles.
Addedinversion3.8.
42 Chapter3. ConfigurePython

### 第49页

CHAPTER
FOUR
USING PYTHON ON WINDOWS
ThisdocumentaimstogiveanoverviewofWindows-specificbehaviouryoushouldknowaboutwhenusingPython
onMicrosoftWindows.
UnlikemostUnixsystemsandservices,WindowsdoesnotincludeasystemsupportedinstallationofPython. Instead,
Python can be obtained from a number of distributors, including directly from the CPython team. Each Python
distributionwillhaveitsownbenefitsanddrawbacks,however,consistencywithothertoolsyouareusingisgenerally
aworthwhilebenefit. Beforecommittingtotheprocessdescribedhere, werecommendinvestigatingyourexisting
toolstoseeiftheycanprovidePythondirectly.
To obtain Python from the CPython team, use the Python Install Manager. This is a standalone tool that makes
PythonavailableasglobalcommandsonyourWindowsmachine,integrateswiththesystem,andsupportsupdates
overtime. YoucandownloadthePythonInstallManagerfrompython.org/downloadsorthroughtheMicrosoftStore
app.
Once you have installed the Python Install Manager, the global python command can be used from any terminal
tolaunchyourcurrentlatestversionofPython. Thisversionmaychangeovertimeasyouaddorremovedifferent
versions,andthepy listcommandwillshowwhichiscurrent.
In general, we recommend that you create a virtual environment for each project and run <env>\Scripts\
Activateinyourterminaltouseit. Thisprovidesisolationbetweenprojects,consistencyovertime,andensures
thatadditionalcommandsaddedbypackagesarealsoavailableinyoursession. Createavirtualenvironmentusing
python -m venv <env path>.
Ifthepythonorpycommandsdonotseemtobeworking,pleaseseetheTroubleshootingsectionbelow. Thereare
sometimesadditionalmanualstepsrequiredtoconfigureyourPC.
Apart from using the Python install manager, Python can also be obtained as NuGet packages. See The nuget.org
packagesbelowformoreinformationonthesepackages.
TheembeddabledistrosareminimalpackagesofPythonsuitableforembeddingintolargerapplications. Theycan
be installed using the Python install manager. See The embeddable package below for more information on these
packages.
4.1 Python Install Manager
4.1.1 Installation
The Python install manager can be installed from the Microsoft Store app or downloaded and installed from
python.org/downloads. Thetwoversionsareidentical.
ToinstallthroughtheStore,simplyclick“Install”. Afterithascompleted,openaterminalandtypepythontoget
started.
Toinstallthefiledownloadedfrompython.org,eitherdouble-clickandselect“Install”,orrunAdd-AppxPackage
<path to MSIX>inWindowsPowershell.
Afterinstallation,thepython,py,andpymanagercommandsshouldbeavailable. Ifyouhaveexistinginstallations
ofPython,oryouhavemodifiedyourPATHvariable,youmayneedtoremovethemorundothemodifications. See
Troubleshootingformorehelpwithfixingnon-workingcommands.
43

### 第50页

Whenyoufirstinstallaruntime,youwilllikelybepromptedtoaddadirectorytoyourPATH.Thisisoptional,ifyou
prefertousethepycommand,butisofferedforthosewhopreferthefullrangeofaliases(suchaspython3.14.
exe)tobeavailable. Thedirectorywillbe%LocalAppData%\Python\binbydefault,butmaybecustomizedby
an administrator. Click Start and search for “Edit environment variables for your account” for the system settings
pagetoaddthepath.
EachPythonruntimeyouinstallwillhaveitsowndirectoryforscripts. ThesealsoneedtobeaddedtoPATHifyou
wanttousethem.
ThePythoninstallmanagerwillbeautomaticallyupdatedtonewreleases. ThisdoesnotaffectanyinstallsofPython
runtimes. UninstallingthePythoninstallmanagerdoesnotuninstallanyPythonruntimes.
IfyouarenotabletoinstallanMSIXinyourcontext,forexample,youareusingautomateddeploymentsoftware
that does not support it, or are targeting Windows Server 2019, please see Advanced Installation below for more
information.
4.1.2 Basic Use
TherecommendedcommandforlaunchingPythonispython,whichwilleitherlaunchtheversionrequestedbythe
scriptbeinglaunched,anactivevirtualenvironment,orthedefaultinstalledversion,whichwillbethelateststable
releaseunlessconfiguredotherwise. Ifnoversionisspecificallyrequestedandnoruntimesareinstalledatall, the
currentlatestreleasewillbeinstalledautomatically.
Forallscenariosinvolvingmultipleruntimeversions,therecommendedcommandispy. Thismaybeusedanywhere
inplaceofpythonortheolderpy.exelauncher. Bydefault,pymatchesthebehaviourofpython,butalsoallows
commandlineoptionstoselectaspecificversionaswellassubcommandstomanageinstallations. Thesearedetailed
below.
Becausethepycommandmayalreadybetakenbythepreviousversion,thereisalsoanunambiguouspymanager
command. ScriptedinstallsthatareintendingtousePythoninstallmanagershouldconsiderusingpymanager,due
tothelowerchanceofencounteringaconflictwithexistinginstalls. Theonlydifferencebetweenthetwocommands
iswhenrunningwithoutanyarguments: pywillinstallandlaunchyourdefaultinterpreter,whilepymanagerwill
displayhelp(pymanager exec ...providesequivalentbehaviourtopy ...).
Each of these commands also has a windowed version that avoids creating a console window. These are pyw,
pythonw and pymanagerw. A python3 command is also included that mimics the python command. It is in-
tendedtocatchaccidentalusesofthetypicalPOSIXcommandonWindows,butisnotmeanttobewidelyusedor
recommended.
Tolaunchyourdefaultruntime,runpythonorpywiththeargumentsyouwanttobepassedtotheruntime(such
asscriptfilesorthemoduletolaunch):
$> py
...
$> python my-script.py
...
$> py -m this
...
ThedefaultruntimecanbeoverriddenwiththePYTHON_MANAGER_DEFAULTenvironmentvariable,oraconfigura-
tionfile. SeeConfigurationforinformationaboutconfigurationsettings.
Tolaunchaspecificruntime, the py commandacceptsa -V:<TAG> option. Thisoptionmustbe specifiedbefore
anyothers. Thetagispartoralloftheidentifierfortheruntime;forthosefromtheCPythonteam,itlookslikethe
version,potentiallywiththeplatform. Forcompatibility,theV:maybeomittedincaseswherethetagreferstoan
officialreleaseandstartswith3.
$> py -V:3.14 ...
$> py -V:3-arm64 ...
Runtimesfromotherdistributorsmayrequirethecompanytobeincludedaswell. Thisshouldbeseparatedfromthe
tagbyaslash,andmaybeaprefix. SpecifyingthecompanyisoptionalwhenitisPythonCore,andspecifyingthe
tagisoptional(butnottheslash)whenyouwantthelatestreleasefromaspecificcompany.
44 Chapter4. UsingPythononWindows

### 第51页

$> py -V:Distributor\1.0 ...
$> py -V:distrib/ ...
Ifnoversionisspecified,butascriptfileispassed,thescriptwillbeinspectedforashebangline. Thisisaspecial
formatforthefirstlineinafilethatallowsoverridingthecommand. SeeShebanglinesformoreinformation. When
thereisnoshebangline,oritcannotberesolved,thescriptwillbelaunchedwiththedefaultruntime.
Ifyouarerunninginanactivevirtualenvironment,havenotrequestedaparticularversion,andthereisnoshebang
line,thedefaultruntimewillbethatvirtualenvironment. Inthisscenario,thepythoncommandwaslikelyalready
overriddenandnoneofthesechecksoccurred. However,thisbehaviourensuresthatthepycommandcanbeused
interchangeably.
Whenyoulauncheitherpythonorpybutdonothaveanyruntimesinstalled,andtherequestedversionisthedefault,
itwillbeinstalledautomaticallyandthenlaunched. Otherwise,therequestedversionwillbeinstalledifautomatic
installationisconfigured(mostlikelybysettingPYTHON_MANAGER_AUTOMATIC_INSTALLtotrue),orifthepy
execorpymanager execformsofthecommandwereused.
4.1.3 Command Help
Thepy helpcommandwilldisplaythefulllistofsupportedcommands,alongwiththeiroptions. Anycommand
maybepassedthe-?optiontodisplayitshelp,oritsnamepassedtopy help.
$> py help
$> py help install
$> py install /?
Allcommandssupportsomecommonoptions,whichwillbeshownbypy help. Theseoptionsmustbespecified
after any subcommand. Specifying -v or --verbose will increase the amount of output shown, and -vv will
increaseitfurtherfordebuggingpurposes. Passing-qor--quietwillreduceoutput,and-qqwillreduceitfurther.
The --config=<PATH> option allows specifying a configuration file to override multiple settings at once. See
Configurationbelowformoreinformationaboutthesefiles.
4.1.4 Listing Runtimes
$> py list [-f=|--format=<FMT>] [-1|--one] [--online|-s=|--source=<URL>] [<TAG>...]
Thelistofinstalledruntimescanbeseenusingpy list. Afiltermaybeaddedintheformofoneormoretags
(withorwithoutcompanyspecifier),andeachmayincludea<,<=,>=or>prefixtorestricttoarange.
Arangeofformatsaresupported,andcanbepassedasthe--format=<FMT>or-f <FMT>option. Formatsinclude
table(auserfriendlytableview), csv(comma-separatedtable), json(asingleJSONblob), jsonl(oneJSON
blobperresult),exe(justtheexecutablepath),prefix(justtheprefixpath).
The--oneor-1optiononlydisplaysasingleresult. Ifthedefaultruntimeisincluded,itwillbetheone. Otherwise,
the“best”resultisshown(“best”isdeliberatelyvaguelydefined, butwillusuallybethemostrecentversion). The
resultshownbypy list --one <TAG>willmatchtheruntimethatwouldbelaunchedbypy -V:<TAG>.
The--only-managedoptionexcludesresultsthatwerenotinstalledbythePythoninstallmanager. Thisisuseful
whendeterminingwhichruntimesmaybeupdatedoruninstalledthroughthepycommand.
The--onlineoptionisshortforpassing--source=<URL>withthedefaultsource. Passingeitheroftheseoptions
willsearchtheonlineindexforruntimesthatcanbeinstalled. Theresultshownbypy list --online --one
<TAG>willmatchtheruntimethatwouldbeinstalledbypy install <TAG>.
$> py list --online 3.14
Forcompatibilitywiththeoldlauncher, the--list, --list-paths, -0and-0pcommands(e.g. py -0p)are
retained. Theydonotallowadditionaloptions,andwillproducelegacyformattedoutput.
4.1. PythonInstallManager 45

### 第52页

4.1.5 Installing Runtimes
$> py install [-s=|--source=<URL>] [-f|--force] [-u|--update] [--dry-run] [<TAG>...
,→]
New runtime versions may be added using py install. One or more tags may be specified, and the special tag
defaultmaybeusedtoselectthedefault. Rangesarenotsupportedforinstallation.
The--source=<URL>optionallowsoverridingtheonlineindexthatisusedtoobtainruntimes. Thismaybeused
withanofflineindex,asshowninOfflineInstalls.
Passing--forcewillignoreanycachedfilesandremoveanyexistinginstalltoreplaceitwiththespecifiedone.
Passing--updatewillreplaceexistinginstallsifthenewversionisnewer. Otherwise,theywillbeleft. Ifnotags
areprovidedwith--update,allinstallsmanagedbythePythoninstallmanagerwillbeupdatedifnewerversions
areavailable. Updateswillremoveanymodificationsmadetotheinstall,includinggloballyinstalledpackages,but
virtualenvironmentswillcontinuetowork.
Passing--dry-runwillgenerateoutputandlogs,butwillnotmodifyanyinstalls.
Inadditiontotheaboveoptions,the--targetoptionwillextracttheruntimetothespecifieddirectoryinsteadof
doinganormalinstall. Thisisusefulforembeddingruntimesintolargerapplications.
$> py install ... [-t=|--target=<PATH>] <TAG>
4.1.6 Offline Installs
To perform offline installs of Python, you will need to first create an offline index on a machine that has network
access.
$> py install --download=<PATH> ... <TAG>...
The--download=<PATH>optionwilldownloadthepackagesforthelistedtagsandcreateadirectorycontaining
themandanindex.jsonfilesuitableforlaterinstallation. Thisentiredirectorycanbemovedtotheofflinemachine
andusedtoinstalloneormoreofthebundledruntimes:
$> py install --source="<PATH>\index.json" <TAG>...
The Python install manager can be installed by downloading its installer and moving it to another machine before
installing.
Alternatively,theZIPfilesinanofflineindexdirectorycansimplybetransferredtoanothermachineandextracted.
Thiswillnotregistertheinstallinanyway,andsoitmustbelaunchedbydirectlyreferencingtheexecutablesinthe
extracteddirectory,butitissometimesapreferableapproachincaseswhereinstallingthePythoninstallmanageris
notpossibleorconvenient.
Inthisway,Pythonruntimescanbeinstalledandmanagedonamachinewithoutaccesstotheinternet.
4.1.7 Uninstalling Runtimes
$> py uninstall [-y|--yes] <TAG>...
Runtimesmayberemovedusingthepy uninstallcommand. Oneormoretagsmustbespecified. Rangesare
notsupportedhere.
The--yesoptionbypassestheconfirmationpromptbeforeuninstalling.
Insteadofpassingtagsindividually,the--purgeoptionmaybespecified. Thiswillremoveallruntimesmanagedby
thePythoninstallmanager,includingcleaninguptheStartmenu,registry,andanydownloadcaches. Runtimesthat
werenotinstalledbythePythoninstallmanagerwillnotbeimpacted,andneitherwillmanuallycreatedconfiguration
files.
46 Chapter4. UsingPythononWindows

### 第53页

$> py uninstall [-y|--yes] --purge
The Python install manager can be uninstalled through the Windows “Installed apps” settings page. This does not
removeanyruntimes, andtheywillstillbeusable, thoughtheglobalpythonandpycommandswillberemoved.
ReinstallingthePythoninstallmanagerwillallowyoutomanagetheseruntimesagain. Tocompletelycleanupall
Pythonruntimes,runwith--purgebeforeuninstallingthePythoninstallmanager.
4.1.8 Configuration
Python install manager is configured with a hierarchy of configuration files, environment variables, command-line
options, and registry settings. In general, configuration files have the ability to configure everything, including the
locationofotherconfigurationfiles,whileregistrysettingsareadministrator-onlyandwilloverrideconfigurationfiles.
Command-lineoptionsoverrideallothersettings,butnoteveryoptionisavailable.
Thissectionwilldescribethedefaults,butbeawarethatmodifiedoroverriddeninstallsmayresolvesettingsdiffer-
ently.
Aglobalconfigurationfilemaybeconfiguredbyanadministrator, andwouldbereadfirst. Theuserconfiguration
file is stored at %AppData%\Python\pymanager.json (by default) and is read next, overwriting any settings
fromearlierfiles. AnadditionalconfigurationfilemaybespecifiedasthePYTHON_MANAGER_CONFIGenvironment
variableorthe--configcommandlineoption(butnotboth).
Thefollowingsettingsarethosethatareconsideredlikelytobemodifiedinnormaluse. Latersectionslistthosethat
areintendedforadministrativecustomization.
4.1. PythonInstallManager 47

### 第54页

Standardconfigurationoptions
ConfigKey EnvironmentVariable Description
default_tag The preferred default version to
PYTHON_MANAGER_DEFAULT launch or install. By default,
this is interpreted as the most re-
cent non-prerelease version from
theCPythonteam.
default_platform PYTHON_MANAGER_DEFAULT_PLATFTORheM preferred default platform to
launch or install. This is treated as
a suffix to the specified tag, such
that py -V:3.14 would prefer an
installfor3.14-64ifitexists(and
default_platform is -64), but
willuse3.14ifnotaggedinstallex-
ists.
logs_dir PYTHON_MANAGER_LOGS The location where log files are
written. Bydefault,%TEMP%.
automatic_install PYTHON_MANAGER_AUTOMATIC_INSTTAruLeL to allow automatic installs
when specifying a particular run-
timetolaunch. Bydefault,true.
include_unmanaged PYTHON_MANAGER_INCLUDE_UNMANTAGruEeDto allow listing and launching
runtimes that were not installed by
thePythoninstallmanager,orfalse
toexcludethem. Bydefault,true.
shebang_can_run_anything PYTHON_MANAGER_SHEBANG_CAN_RTUNru_eAtNoYaTlHloIwNGshebangsin.pyfiles
to launch applications other than
Pythonruntimes,orfalsetoprevent
it. Bydefault,true.
log_level PYMANAGER_VERBOSE, Set the default level of output (0-
PYMANAGER_DEBUG 50). By default, 20. Lower val-
uesproducemoreoutput. Theenvi-
ronmentvariablesareboolean,and
mayproduceadditionaloutputdur-
ing startup that is later suppressed
byotherconfiguration.
confirm PYTHON_MANAGER_CONFIRM Truetoconfirmcertainactionsbe-
foretakingthem(suchasuninstall),
orfalsetoskiptheconfirmation. By
default,true.
install.source PYTHON_MANAGER_SOURCE_URL Override the index feed to obtain
newinstallsfrom.
list.format PYTHON_MANAGER_LIST_FORMAT Specify the default format used by
the py list command. By de-
fault,table.
DottednamesshouldbenestedinsideJSONobjects,forexample,list.formatwouldbespecifiedas{"list":
{"format": "table"}}.
4.1.9 Shebang lines
Ifthefirstlineofascriptfilestartswith#!, itisknownasa“shebang”line. LinuxandotherUnixlikeoperating
systemshavenativesupportforsuchlinesandtheyarecommonlyusedonsuchsystemstoindicatehowascriptshould
beexecuted. ThepythonandpycommandsallowthesamefacilitiestobeusedwithPythonscriptsonWindows.
ToallowshebanglinesinPythonscriptstobeportablebetweenUnixandWindows,anumberof‘virtual’commands
aresupportedtospecifywhichinterpretertouse. Thesupportedvirtualcommandsare:
48 Chapter4. UsingPythononWindows

| ConfigKey | EnvironmentVariable | Description |
| --- | --- | --- |
| default_tag | PYTHON_MANAGER_DEFAULT | The preferred default version to
launch or install. By default,
this is interpreted as the most re-
cent non-prerelease version from
theCPythonteam. |
| default_platform | PYTHON_MANAGER_DEFAULT_PLAT | FTORheM preferred default platform to
launch or install. This is treated as
a suffix to the specified tag, such
that py -V:3.14 would prefer an
installfor3.14-64ifitexists(and
default_platform is -64), but
willuse3.14ifnotaggedinstallex-
ists. |
| logs_dir | PYTHON_MANAGER_LOGS | The location where log files are
written. Bydefault,%TEMP%. |
| automatic_install | PYTHON_MANAGER_AUTOMATIC_IN | STTAruLeL to allow automatic installs
when specifying a particular run-
timetolaunch. Bydefault,true. |
| include_unmanaged | PYTHON_MANAGER_INCLUDE_UNMA | NTAGruEeDto allow listing and launching
runtimes that were not installed by
thePythoninstallmanager,orfalse
toexcludethem. Bydefault,true. |
| shebang_can_run_anything | PYTHON_MANAGER_SHEBANG_CAN_ | RTUNru_eAtNoYaTlHloIwNGshebangsin.pyfiles
to launch applications other than
Pythonruntimes,orfalsetoprevent
it. Bydefault,true. |
| log_level | PYMANAGER_VERBOSE,
PYMANAGER_DEBUG | Set the default level of output (0-
50). By default, 20. Lower val-
uesproducemoreoutput. Theenvi-
ronmentvariablesareboolean,and
mayproduceadditionaloutputdur-
ing startup that is later suppressed
byotherconfiguration. |
| confirm | PYTHON_MANAGER_CONFIRM | Truetoconfirmcertainactionsbe-
foretakingthem(suchasuninstall),
orfalsetoskiptheconfirmation. By
default,true. |
| install.source | PYTHON_MANAGER_SOURCE_URL | Override the index feed to obtain
newinstallsfrom. |
| list.format | PYTHON_MANAGER_LIST_FORMAT | Specify the default format used by
the py list command. By de-
fault,table. |

### 第55页

• /usr/bin/env <ALIAS>
• /usr/bin/env -S <ALIAS>
• /usr/bin/<ALIAS>
• /usr/local/bin/<ALIAS>
• <ALIAS>
Forexample,ifthefirstlineofyourscriptstartswith
#! /usr/bin/python
ThedefaultPythonoranactivevirtualenvironmentwillbelocatedandused. AsmanyPythonscriptswrittentowork
onUnixwillalreadyhavethisline,youshouldfindthesescriptscanbeusedbythelauncherwithoutmodification. If
youarewritinganewscriptonWindowswhichyouhopewillbeusefulonUnix,youshoulduseoneoftheshebang
linesstartingwith/usr.
Anyoftheabovevirtualcommandscanhave<ALIAS>replacedbyanaliasfromaninstalledruntime. Thatis,any
commandgeneratedintheglobalaliasesdirectory(whichyoumayhaveaddedtoyourPATHenvironmentvariable)
canbeusedinashebang,evenifitisnotonyourPATH.Thisallowstheuseofshebangslike/usr/bin/python3.12
toselectaparticularruntime.
Ifnoruntimesareinstalled,orifautomaticinstallationisenabled,therequestedruntimewillbeinstalledifnecessary.
SeeConfigurationforinformationaboutconfigurationsettings.
The /usr/bin/env form of shebang line will also search the PATH environment variable for unrecognized com-
mands. ThiscorrespondstothebehaviouroftheUnixenvprogram,whichperformsthesamesearch,butprefers
launchingknownPythoncommands. Awarningmaybedisplayedwhensearchingforarbitraryexecutables,andthis
searchmaybedisabledbytheshebang_can_run_anythingconfigurationoption.
ShebanglinesthatdonotmatchanyofpatternsaretreatedasWindowsexecutablepathsthatareabsoluteorrelative
tothedirectorycontainingthescriptfile. ThisisaconvenienceforWindows-onlyscripts,suchasthosegenerated
by an installer, since the behavior is not compatible with Unix-style shells. These paths may be quoted, and may
includemultiplearguments,afterwhichthepathtothescriptandanyadditionalargumentswillbeappended. This
functionalitymaybedisabledbytheshebang_can_run_anythingconfigurationoption.
(cid:174) Note
ThebehaviourofshebangsinthePythoninstallmanagerissubtlydifferentfromthepreviouspy.exelauncher,
andtheoldconfigurationoptionsnolongerapply. Ifyouarespecificallyreliantontheoldbehaviourorconfig-
uration, werecommendkeepingthelegacylauncher. Itmaybedownloadedindependentlyandinstalledonits
own. Thelegacylauncher’spycommandwilloverridePyManager’sone,andyouwillneedtousepymanager
commandsforinstallinganduninstalling.
4.1.10 Advanced Installation
For situations where an MSIX cannot be installed, such as some older administrative distribution platforms, there
is an MSI available from the python.org downloads page. This MSI has no user interface, and can only perform
per-machineinstallstoitsdefaultlocationinProgramFiles. ItwillattempttomodifythesystemPATHenvironment
variabletoincludethisinstalllocation,butbesuretovalidatethisonyourconfiguration.
(cid:174) Note
WindowsServer2019istheonlyversionofWindowsthatCPythonsupportsthatdoesnotsupportMSIX.For
WindowsServer2019,youshouldusetheMSI.
Be aware that the MSI package does not bundle any runtimes, and so is not suitable for installs into offline en-
vironments without also creating an offline install index. See Offline Installs and Administrative Configuration for
informationonhandlingthesescenarios.
4.1. PythonInstallManager 49

### 第56页

RuntimesinstalledbytheMSIaresharedwiththoseinstalledbytheMSIX,andareallper-useronly. ThePython
install manager does not support installing runtimes per-machine. To emulate a per-machine install, you can use
py install --target=<shared location>asadministratorandaddyourownsystem-widemodificationsto
PATH,theregistry,ortheStartmenu.
When the MSIX is installed, but commands are not available in the PATH environment variable, they
can be found under %LocalAppData%\Microsoft\WindowsApps\PythonSoftwareFoundation.
PythonManager_3847v3x7pw1km or %LocalAppData%\Microsoft\WindowsApps\
PythonSoftwareFoundation.PythonManager_qbz5n2kfra8p0, depending on whether it was installed
from python.org or through the Windows Store. Attempting to run the executable directly from Program Files is
notrecommended.
ToprogrammaticallyinstallthePythoninstallmanager,itiseasiesttouseWinGet,whichisincludedwithallsup-
portedversionsofWindows:
$> winget install 9NQ7512CXL7T -e --accept-package-agreements --disable-
,→interactivity
# Optionally run the configuration checker and accept all changes
$> py install --configure -y
TodownloadthePythoninstallmanagerandinstallonanothermachine,thefollowingWinGetcommandwilldown-
loadtherequiredfilesfromtheStoretoyourDownloadsdirectory(add-d <location>tocustomizetheoutput
location). ThisalsogeneratesaYAMLfilethatappearstobeunnecessary,asthedownloadedMSIXcanbeinstalled
bylaunchingorusingthecommandsbelow.
$> winget download 9NQ7512CXL7T -e --skip-license --accept-package-agreements --
,→accept-source-agreements
To programmatically install or uninstall an MSIX using only PowerShell, the Add-AppxPackage and Remove-
AppxPackagePowerShellcmdletsarerecommended:
$> Add-AppxPackage C:\Downloads\python-manager-25.0.msix
...
$> Get-AppxPackage PythonSoftwareFoundation.PythonManager | Remove-AppxPackage
The latest release can be downloaded and installed by Windows by passing the AppInstaller file to the Add-
AppxPackage command. This installs using the MSIX on python.org, and is only recommended for cases where
installingviatheStore(interactivelyorusingWinGet)isnotpossible.
$> Add-AppxPackage -AppInstallerFile https://www.python.org/ftp/python/pymanager/
,→pymanager.appinstaller
OthertoolsandAPIsmayalsobeusedtoprovisionanMSIXpackageforallusersonamachine,butPythondoesnot
considerthisasupportedscenario. WesuggestlookingintothePowerShellAdd-AppxProvisionedPackagecmdlet,
thenativeWindowsPackageManagerclass,orthedocumentationandsupportforyourdeploymenttool.
Regardlessoftheinstallmethod,userswillstillneedtoinstalltheirowncopiesofPythonitself,asthereisnoway
totriggerthoseinstallswithoutbeingaloggedinuser. WhenusingtheMSIX,thelatestversionofPythonwillbe
availableforalluserstoinstallwithoutnetworkaccess.
Note that the MSIX downloadable from the Store and from the Python website are subtly different and cannot be
installed at the same time. Wherever possible, we suggest using the above WinGet commands to download the
packagefromtheStoretoreducetheriskofsettingupconflictinginstalls. Therearenolicensingrestrictionsonthe
PythoninstallmanagerthatwouldpreventusingtheStorepackageinthisway.
50 Chapter4. UsingPythononWindows

### 第57页

4.1.11 Administrative Configuration
ThereareanumberofoptionsthatmaybeusefulforadministratorstooverrideconfigurationofthePythoninstall
manager. Thesecanbeusedtoprovidelocalcaching,disablecertainshortcuttypes,overridebundledcontent. All
oftheaboveconfigurationoptionsmaybeset,aswellasthosebelow.
Configuration options may be overridden in the registry by setting values under HKEY_LOCAL_MACHINE\
Software\Policies\Python\PyManager, wherethevaluenamematchestheconfigurationkeyandthevalue
typeisREG_SZ.Notethatthiskeycanitselfbecustomized, butonlybymodifyingthecoreconfigfiledistributed
withthePythoninstallmanager. Werecommend,however,thatregistryvaluesareusedonlytosetbase_config
toaJSONfilecontainingthefullsetofoverrides. Registrykeyoverrideswillreplaceanyotherconfiguredsetting,
whilebase_configallowsuserstofurthermodifysettingstheymayneed.
Notethatmostsettingswithenvironmentvariablessupportthosevariablesbecausetheirdefaultsettingspecifiesthe
variable. If you override them, the environment variable will no longer work, unless you override it with another
one. Forexample,thedefaultvalueofconfirmisliterally%PYTHON_MANAGER_CONFIRM%,whichwillresolvethe
variableatloadtime. Ifyouoverridethevaluetoyes,thentheenvironmentvariablewillnolongerbeused. Ifyou
overridethevalueto%CONFIRM%,thenthatenvironmentvariablewillbeusedinstead.
Configurationsettingsthatarepathsareinterpretedasrelativetothedirectorycontainingtheconfigurationfilethat
specifiedthem.
Administrativeconfigurationoptions
ConfigKey Description
base_config Thehighestpriorityconfigurationfiletoread. Notethatonlythebuilt-inconfiguration
fileandtheregistrycanmodifythissetting.
user_config Thesecondconfigurationfiletoread.
additional_config Thethirdconfigurationfiletoread.
registry_override_keyRegistrylocationtocheckforoverrides. Notethatonlythebuilt-inconfigurationfile
canmodifythissetting.
bundled_dir Read-onlydirectorycontaininglocallycachedfiles.
install. PathorURLtoanindextoconsultwhenthemainindexcannotbeaccessed.
fallback_source
install. Comma-separatedlistofshortcutkindstoallow(e.g. "pep514,start"). Enabled
enable_shortcut_kindsshortcutsmaystillbedisabledbydisable_shortcut_kinds.
install. Comma-separatedlistofshortcutkindstoexclude(e.g. "pep514,start"). Dis-
disable_shortcut_kindasbledshortcutsarenotreactivatedbyenable_shortcut_kinds.
pep514_root Registry location to read and write PEP 514 entries into. By default,
HKEY_CURRENT_USER\Software\Python.
start_folder Startmenufoldertowriteshortcutsinto. Bydefault,Python. Thispathisrelative
totheuser’sProgramsfolder.
virtual_env Pathtotheactivevirtualenvironment. Bydefault,thisis%VIRTUAL_ENV%,butmay
besetemptytodisablevenvdetection.
shebang_can_run_anythTirnuge_tsoisluepnprtelsysvisiblewarningswhenashebanglaunchesanapplicationotherthan
aPythonruntime.
4.1.12 Installing Free-threaded Binaries
Addedinversion3.13: (Experimental)
(cid:174) Note
Everything described in this section is considered experimental, and should be expected to change in future
releases.
Pre-builtdistributionsoftheexperimentalfree-threadedbuildareavailablebyinstallingtagswiththetsuffix.
4.1. PythonInstallManager 51

| ConfigKey | Description |
| --- | --- |
| base_config | Thehighestpriorityconfigurationfiletoread. Notethatonlythebuilt-inconfiguration
fileandtheregistrycanmodifythissetting. |
| user_config | Thesecondconfigurationfiletoread. |
| additional_config | Thethirdconfigurationfiletoread. |
| registry_override_ke | yRegistrylocationtocheckforoverrides. Notethatonlythebuilt-inconfigurationfile
canmodifythissetting. |
| bundled_dir | Read-onlydirectorycontaininglocallycachedfiles. |
| install.
fallback_source | PathorURLtoanindextoconsultwhenthemainindexcannotbeaccessed. |
| install.
enable_shortcut_kind | Comma-separatedlistofshortcutkindstoallow(e.g. "pep514,start"). Enabled
sshortcutsmaystillbedisabledbydisable_shortcut_kinds. |
| install.
disable_shortcut_kin | Comma-separatedlistofshortcutkindstoexclude(e.g. "pep514,start"). Dis-
dasbledshortcutsarenotreactivatedbyenable_shortcut_kinds. |
| pep514_root | Registry location to read and write PEP 514 entries into. By default,
HKEY_CURRENT_USER\Software\Python. |
| start_folder | Startmenufoldertowriteshortcutsinto. Bydefault,Python. Thispathisrelative
totheuser’sProgramsfolder. |
| virtual_env | Pathtotheactivevirtualenvironment. Bydefault,thisis%VIRTUAL_ENV%,butmay
besetemptytodisablevenvdetection. |
| shebang_can_run_anyt | hTirnuge_tsoisluepnprtelsysvisiblewarningswhenashebanglaunchesanapplicationotherthan
aPythonruntime. |

### 第58页

$> py install 3.14t
$> py install 3.14t-arm64
$> py install 3.14t-32
Thiswillinstallandregisterasnormal. Ifyouhavenootherruntimesinstalled,thenpythonwilllaunchthisone.
Otherwise,youwillneedtousepy -V:3.14t ...or,ifyouhaveaddedtheglobalaliasesdirectorytoyourPATH
environmentvariable,thepython3.14t.execommands.
4.1.13 Troubleshooting
IfyourPythoninstallmanagerdoesnotseemtobeworkingcorrectly,pleaseworkthroughthesetestsandfixestosee
ifithelps. Ifnot,pleasereportanissueatourbugtracker,includinganyrelevantlogfiles(writtentoyour%TEMP%
directorybydefault).
52 Chapter4. UsingPythononWindows

### 第59页

Troubleshooting
Symptom Thingstotry
python gives me a DidyouinstallthePythoninstallmanager?
“command not found”
errororopenstheStore
app when I type it in
myterminal.
ClickStart,open“Manageappexecutionaliases”,andcheckthatthealiasesfor“Python
(default)”areenabled. Iftheyalreadyare,trydisablingandre-enablingtorefreshthe
command. The“Python(defaultwindowed)”and“Pythoninstallmanager”commands
mayalsoneedrefreshing.
Checkthatthepyandpymanagercommandswork.
py gives me a “com- DidyouinstallthePythoninstallmanager?
mand not found” error
whenItypeitinmyter-
minal.
ClickStart,open“Manageappexecutionaliases”,andcheckthatthealiasesfor“Python
(default)”areenabled. Iftheyalreadyare,trydisablingandre-enablingtorefreshthe
command. The“Python(defaultwindowed)”and“Pythoninstallmanager”commands
mayalsoneedrefreshing.
py gives me a “can’t This usually means you have the legacy launcher installed and it has priority over
open file” error when I thePythoninstallmanager. Toremove, clickStart, open“Installedapps”, searchfor
type commands in my “Pythonlauncher”anduninstallit.
terminal.
python doesn’t launch Click Start, open “Installed apps”, look for any existing Python runtimes, and either
thesameruntimeaspy removethemorModifyanddisablethePATHoptions.
ClickStart,open“Manageappexecutionaliases”,andcheckthatyourpython.exe
aliasissetto“Python(default)”
python and py don’t Check your PYTHON_MANAGER_DEFAULT environment variable or default_tag
launchtheruntimeIex- configuration. Thepy listcommandwillshowyourdefaultbasedonthesesettings.
pect
Installs that are managed by the Python install manager will be chosen ahead of un-
managed installs. Use py install to install the runtime you expect, or configure
yourdefaulttag.
PrereleaseandexperimentalinstallsthatarenotmanagedbythePythoninstallmanager
may be chosen ahead of stable releases. Configure your default tag or uninstall the
prereleaseruntimeandreinstallusingpy install.
pythonw or pyw don’t ClickStart,open“Manageappexecutionaliases”,andcheckthatyourpythonw.exe
launch the same run- andpyw.exealiasesareconsistentwithyourothers.
timeaspythonorpy
pip gives me a “com- Have you activated a virtual environment? Run the .venv\Scripts\activate
mand not found” error scriptinyourterminaltoactivate.
whenItypeitinmyter-
minal.
Thepackagemaybeavailablebutmissingthegeneratedexecutable. Werecommend
using the python -m pip command instead, or alternatively the python -m pip
install --force pip command will recreate the executables and show you the
path to add to PATH. These scripts are separated for each runtime, and so you may
needtoaddmultiplepaths.
4.2 The embeddable package
Addedinversion3.5.
TheembeddeddistributionisaZIPfilecontainingaminimalPythonenvironment. Itisintendedforactingaspart
4.2. Theembeddablepackage 53

| Symptom | Thingstotry |
| --- | --- |
| python gives me a
“command not found”
errororopenstheStore
app when I type it in
myterminal. | DidyouinstallthePythoninstallmanager? |
|  | ClickStart,open“Manageappexecutionaliases”,andcheckthatthealiasesfor“Python
(default)”areenabled. Iftheyalreadyare,trydisablingandre-enablingtorefreshthe
command. The“Python(defaultwindowed)”and“Pythoninstallmanager”commands
mayalsoneedrefreshing. |
|  | Checkthatthepyandpymanagercommandswork. |
| py gives me a “com-
mand not found” error
whenItypeitinmyter-
minal. | DidyouinstallthePythoninstallmanager? |
|  | ClickStart,open“Manageappexecutionaliases”,andcheckthatthealiasesfor“Python
(default)”areenabled. Iftheyalreadyare,trydisablingandre-enablingtorefreshthe
command. The“Python(defaultwindowed)”and“Pythoninstallmanager”commands
mayalsoneedrefreshing. |
| py gives me a “can’t
open file” error when I
type commands in my
terminal. | This usually means you have the legacy launcher installed and it has priority over
thePythoninstallmanager. Toremove, clickStart, open“Installedapps”, searchfor
“Pythonlauncher”anduninstallit. |
| python doesn’t launch
thesameruntimeaspy | Click Start, open “Installed apps”, look for any existing Python runtimes, and either
removethemorModifyanddisablethePATHoptions. |
|  | ClickStart,open“Manageappexecutionaliases”,andcheckthatyourpython.exe
aliasissetto“Python(default)” |
| python and py don’t
launchtheruntimeIex-
pect | Check your PYTHON_MANAGER_DEFAULT environment variable or default_tag
configuration. Thepy listcommandwillshowyourdefaultbasedonthesesettings. |
|  | Installs that are managed by the Python install manager will be chosen ahead of un-
managed installs. Use py install to install the runtime you expect, or configure
yourdefaulttag. |
|  | PrereleaseandexperimentalinstallsthatarenotmanagedbythePythoninstallmanager
may be chosen ahead of stable releases. Configure your default tag or uninstall the
prereleaseruntimeandreinstallusingpy install. |
| pythonw or pyw don’t
launch the same run-
timeaspythonorpy | ClickStart,open“Manageappexecutionaliases”,andcheckthatyourpythonw.exe
andpyw.exealiasesareconsistentwithyourothers. |
| pip gives me a “com-
mand not found” error
whenItypeitinmyter-
minal. | Have you activated a virtual environment? Run the .venv\Scripts\activate
scriptinyourterminaltoactivate. |
|  | Thepackagemaybeavailablebutmissingthegeneratedexecutable. Werecommend
using the python -m pip command instead, or alternatively the python -m pip
install --force pip command will recreate the executables and show you the
path to add to PATH. These scripts are separated for each runtime, and so you may
needtoaddmultiplepaths. |

### 第60页

ofanotherapplication,ratherthanbeingdirectlyaccessedbyend-users.
Toinstallanembeddeddistribution,werecommendusingpy installwiththe--targetoption:
$> py install 3.14-embed --target=runtime
Whenextracted,theembeddeddistributionis(almost)fullyisolatedfromtheuser’ssystem,includingenvironment
variables, system registry settings, and installed packages. The standard library is included as pre-compiled and
optimized .pyc files in a ZIP, and python3.dll, python313.dll, python.exe and pythonw.exe are all
provided. Tcl/tk(includingalldependents,suchasIdle),pipandthePythondocumentationarenotincluded.
A default ._pth file is included, which further restricts the default search paths (as described below in Finding
modules). Thisfileisintendedforembedderstomodifyasnecessary.
Third-partypackagesshouldbeinstalledbytheapplicationinstalleralongsidetheembeddeddistribution. Usingpip
tomanagedependenciesasforaregularPythoninstallationisnotsupportedwiththisdistribution,thoughwithsome
care it may be possible to include and use pip for automatic updates. In general, third-party packages should be
treatedaspartoftheapplication(“vendoring”)sothatthedevelopercanensurecompatibilitywithnewerversions
beforeprovidingupdatestousers.
Thetworecommendedusecasesforthisdistributionaredescribedbelow.
4.2.1 Python Application
An application written in Python does not necessarily require users to be aware of that fact. The embedded dis-
tributionmaybeusedinthiscasetoincludeaprivateversionofPythoninaninstallpackage. Dependingonhow
transparentitshouldbe(orconversely,howprofessionalitshouldappear),therearetwooptions.
Usingaspecializedexecutableasalauncherrequiressomecoding,butprovidesthemosttransparentexperiencefor
users. Withacustomizedlauncher, therearenoobviousindicationsthattheprogramisrunningonPython: icons
canbecustomized,companyandversioninformationcanbespecified,andfileassociationsbehaveproperly. Inmost
cases,acustomlaunchershouldsimplybeabletocallPy_Mainwithahard-codedcommandline.
Thesimplerapproachistoprovideabatchfileorgeneratedshortcutthatdirectlycallsthepython.exeorpythonw.
exewiththerequiredcommand-linearguments. Inthiscase, theapplicationwillappeartobePythonandnotits
actualname,andusersmayhavetroubledistinguishingitfromotherrunningPythonprocessesorfileassociations.
Withthelatterapproach,packagesshouldbeinstalledasdirectoriesalongsidethePythonexecutabletoensurethey
are available on the path. With the specialized launcher, packages can be located in other locations as there is an
opportunitytospecifythesearchpathbeforelaunchingtheapplication.
4.2.2 Embedding Python
Applicationswritteninnativecodeoftenrequiresomeformofscriptinglanguage,andtheembeddedPythondistri-
butioncanbeusedforthispurpose. Ingeneral,themajorityoftheapplicationisinnativecode,andsomepartwill
eitherinvokepython.exeordirectlyusepython3.dll. Foreithercase,extractingtheembeddeddistributionto
asubdirectoryoftheapplicationinstallationissufficienttoprovidealoadablePythoninterpreter.
As with the application use, packages can be installed to any location as there is an opportunity to specify search
pathsbeforeinitializingtheinterpreter. Otherwise,thereisnofundamentaldifferencesbetweenusingtheembedded
distributionandaregularinstallation.
4.3 The nuget.org packages
Addedinversion3.5.2.
Thenuget.orgpackageisareducedsizePythonenvironmentintendedforuseoncontinuousintegrationandbuild
systemsthatdonothaveasystem-wideinstallofPython. Whilenugetis“thepackagemanagerfor.NET”,italso
worksperfectlyfineforpackagescontainingbuild-timetools.
Visitnuget.orgforthemostup-to-dateinformationonusingnuget. Whatfollowsisasummarythatissufficientfor
Pythondevelopers.
54 Chapter4. UsingPythononWindows

### 第61页

The nuget.exe command line tool may be downloaded directly from https://aka.ms/nugetclidl, for ex-
ample,usingcurlorPowerShell. Withthetool,thelatestversionofPythonfor64-bitor32-bitmachinesisinstalled
using:
nuget.exe install python -ExcludeVersion -OutputDirectory .
nuget.exe install pythonx86 -ExcludeVersion -OutputDirectory .
To select a particular version, add a -Version 3.x.y. The output directory may be changed from ., and the
package will be installed into a subdirectory. By default, the subdirectory is named the same as the package, and
withoutthe-ExcludeVersionoptionthisnamewillincludethespecificversioninstalled. Insidethesubdirectory
isatoolsdirectorythatcontainsthePythoninstallation:
# Without -ExcludeVersion
> .\python.3.5.2\tools\python.exe -V
Python 3.5.2
# With -ExcludeVersion
> .\python\tools\python.exe -V
Python 3.5.2
Ingeneral,nugetpackagesarenotupgradeable,andnewerversionsshouldbeinstalledside-by-sideandreferenced
usingthefullpath. Alternatively,deletethepackagedirectorymanuallyandinstallitagain. ManyCIsystemswill
dothisautomaticallyiftheydonotpreservefilesbetweenbuilds.
Alongside the tools directory is a build\native directory. This contains a MSBuild properties file python.
propsthatcanbeusedinaC++projecttoreferencethePythoninstall. Includingthesettingswillautomaticallyuse
theheadersandimportlibrariesinyourbuild.
The package information pages on nuget.org are www.nuget.org/packages/python for the 64-bit version,
www.nuget.org/packages/pythonx86 for the 32-bit version, and www.nuget.org/packages/pythonarm64 for the
ARM64version
4.3.1 Free-threaded packages
Addedinversion3.13: (Experimental)
(cid:174) Note
Everything described in this section is considered experimental, and should be expected to change in future
releases.
Packages containing free-threaded binaries are named python-freethreaded for the 64-bit version, pythonx86-
freethreadedforthe32-bitversion,andpythonarm64-freethreadedfortheARM64version. Thesepackagescontain
boththepython3.13t.exeandpython.exeentrypoints,bothofwhichrunfreethreaded.
4.4 Alternative bundles
BesidesthestandardCPythondistribution,therearemodifiedpackagesincludingadditionalfunctionality. Thefol-
lowingisalistofpopularversionsandtheirkeyfeatures:
ActivePython
Installerwithmulti-platformcompatibility,documentation,PyWin32
Anaconda
Popularscientificmodules(suchasnumpy,scipyandpandas)andthecondapackagemanager.
EnthoughtDeploymentManager
“TheNextGenerationPythonEnvironmentandPackageManager”.
PreviouslyEnthoughtprovidedCanopy,butitreachedendoflifein2016.
4.4. Alternativebundles 55

### 第62页

WinPython
Windows-specificdistributionwithprebuiltscientificpackagesandtoolsforbuildingpackages.
NotethatthesepackagesmaynotincludethelatestversionsofPythonorotherlibraries,andarenotmaintainedor
supportedbythecorePythonteam.
4.5 Supported Windows versions
AsspecifiedinPEP11,aPythonreleaseonlysupportsaWindowsplatformwhileMicrosoftconsiderstheplatform
underextendedsupport. ThismeansthatPython3.14supportsWindows10andnewer. IfyourequireWindows7
support,pleaseinstallPython3.8. IfyourequireWindows8.1support,pleaseinstallPython3.12.
4.6 Removing the MAX_PATH Limitation
Windowshistoricallyhaslimitedpathlengthsto260characters. Thismeantthatpathslongerthanthiswouldnot
resolveanderrorswouldresult.
InthelatestversionsofWindows,thislimitationcanbeexpandedtoover32,000characters. Youradministratorwill
needto activatethe“EnableWin32longpaths”grouppolicy, orset LongPathsEnabled to 1 intheregistrykey
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem.
Thisallowstheopen()function,theosmoduleandmostotherpathfunctionalitytoacceptandreturnpathslonger
than260characters.
Afterchangingtheaboveoptionandrebooting,nofurtherconfigurationisrequired.
4.7 UTF-8 mode
Addedinversion3.7.
Windowsstilluseslegacyencodingsforthesystemencoding(theANSICodePage). Pythonusesitforthedefault
encodingoftextfiles(e.g. locale.getencoding()).
ThismaycauseissuesbecauseUTF-8iswidelyusedontheinternetandmostUnixsystems,includingWSL(Windows
SubsystemforLinux).
YoucanusethePythonUTF-8ModetochangethedefaulttextencodingtoUTF-8. YoucanenablethePythonUTF-
8Modeviathe-X utf8commandlineoption,orthePYTHONUTF8=1environmentvariable. SeePYTHONUTF8for
enablingUTF-8mode,andPythonInstallManagerforhowtomodifyenvironmentvariables.
When the Python UTF-8 Mode is enabled, you can still use the system encoding (the ANSI Code Page) via the
“mbcs”codec.
Note that adding PYTHONUTF8=1 to the default environment variables will affect all Python 3.7+ applications on
yoursystem. IfyouhaveanyPython3.7+applicationswhichrelyonthelegacysystemencoding,itisrecommended
tosettheenvironmentvariabletemporarilyorusethe-X utf8commandlineoption.
(cid:174) Note
EvenwhenUTF-8modeisdisabled,PythonusesUTF-8bydefaultonWindowsfor:
• ConsoleI/OincludingstandardI/O(seePEP528fordetails).
• Thefilesystemencoding(seePEP529fordetails).
4.8 Finding modules
Thesenotessupplementthedescriptionatsys-path-initwithdetailedWindowsnotes.
Whenno._pthfileisfound,thisishowsys.pathispopulatedonWindows:
56 Chapter4. UsingPythononWindows

### 第63页

• Anemptyentryisaddedatthestart,whichcorrespondstothecurrentdirectory.
• IftheenvironmentvariablePYTHONPATH exists,asdescribedinEnvironmentvariables,itsentriesareadded
next. NotethatonWindows,pathsinthisvariablemustbeseparatedbysemicolons,todistinguishthemfrom
thecolonusedindriveidentifiers(C:\etc.).
• Additional “application paths” can be added in the registry as subkeys of \SOFTWARE\Python\
PythonCore{version}\PythonPathunderboththeHKEY_CURRENT_USERandHKEY_LOCAL_MACHINE
hives. Subkeyswhichhavesemicolon-delimitedpathstringsastheirdefaultvaluewillcauseeachpathtobe
addedtosys.path. (NotethatallknowninstallersonlyuseHKLM,soHKCUistypicallyempty.)
• If the environment variable PYTHONHOME is set, it is assumed as “Python Home”. Otherwise, the path of
the main Python executable is used to locate a “landmark file” (either Lib\os.py or pythonXY.zip) to
deducethe“PythonHome”. IfaPythonhomeisfound,therelevantsub-directoriesaddedtosys.path(Lib,
plat-win,etc)arebasedonthatfolder. Otherwise,thecorePythonpathisconstructedfromthePythonPath
storedintheregistry.
• IfthePythonHomecannotbelocated,noPYTHONPATHisspecifiedintheenvironment,andnoregistryentries
canbefound,adefaultpathwithrelativeentriesisused(e.g. .\Lib;.\plat-win,etc).
Ifapyvenv.cfgfileisfoundalongsidethemainexecutableorinthedirectoryonelevelabovetheexecutable,the
followingvariationsapply:
• If home is an absolute path and PYTHONHOME is not set, this path is used instead of the path to the main
executablewhendeducingthehomelocation.
Theendresultofallthisis:
• When running python.exe, or any other .exe in the main Python directory (either an installed version, or
directlyfromthePCbuilddirectory),thecorepathisdeduced,andthecorepathsintheregistryareignored.
Other“applicationpaths”intheregistryarealwaysread.
• WhenPythonishostedinanother.exe(differentdirectory,embeddedviaCOM,etc),the“PythonHome”will
notbededuced,sothecorepathfromtheregistryisused. Other“applicationpaths”intheregistryarealways
read.
• IfPythoncan’tfinditshomeandtherearenoregistryvalue(frozen.exe,someverystrangeinstallationsetup)
yougetapathwithsomedefault,butrelative,paths.
ForthosewhowanttobundlePythonintotheirapplicationordistribution,thefollowingadvicewillpreventconflicts
withotherinstallations:
• Include a ._pth file alongside your executable containing the directories to include. This will ignore paths
listedintheregistryandenvironmentvariables,andalsoignoresiteunlessimport siteislisted.
• If you are loading python3.dll or python37.dll in your own executable, explicitly set PyConfig.
module_search_pathsbeforePy_InitializeFromConfig().
• Clearand/oroverwritePYTHONPATH andsetPYTHONHOMEbeforelaunchingpython.exefromyourappli-
cation.
• If you cannot use the previous suggestions (for example, you are a distribution that allows people to run
python.exe directly), ensure that the landmark file (Lib\os.py) exists in your install directory. (Note
thatitwillnotbedetectedinsideaZIPfile,butacorrectlynamedZIPfilewillbedetectedinstead.)
Thesewillensurethatthefilesinasystem-wideinstallationwillnottakeprecedenceoverthecopyofthestandard
librarybundledwithyourapplication. Otherwise,yourusersmayexperienceproblemsusingyourapplication. Note
thatthefirstsuggestionisthebest,astheothersmaystillbesusceptibletonon-standardpathsintheregistryanduser
site-packages.
Changedinversion3.6: Add._pthfilesupportandremovesapplocaloptionfrompyvenv.cfg.
Changedinversion3.6: AddpythonXX.zipasapotentiallandmarkwhendirectlyadjacenttotheexecutable.
Deprecatedsinceversion3.6: ModulesspecifiedintheregistryunderModules(notPythonPath)maybeimported
byimportlib.machinery.WindowsRegistryFinder. ThisfinderisenabledonWindowsin3.6.0andearlier,
butmayneedtobeexplicitlyaddedtosys.meta_pathinthefuture.
4.8. Findingmodules 57

### 第64页

4.9 Additional modules
EventhoughPythonaimstobeportableamongallplatforms,therearefeaturesthatareuniquetoWindows. Acouple
ofmodules,bothinthestandardlibraryandexternal,andsnippetsexisttousethesefeatures.
TheWindows-specificstandardmodulesaredocumentedinmswin-specific-services.
4.9.1 PyWin32
ThePyWin32modulebyMarkHammondisacollectionofmodulesforadvancedWindows-specificsupport. This
includesutilitiesfor:
• ComponentObjectModel(COM)
• Win32APIcalls
• Registry
• Eventlog
• MicrosoftFoundationClasses(MFC)userinterfaces
PythonWinisasampleMFCapplicationshippedwithPyWin32. ItisanembeddableIDEwithabuilt-indebugger.
(cid:181) Seealso
Win32HowDoI…?
byTimGolden
PythonandCOM
byDavidandPaulBoddie
4.9.2 cx_Freeze
cx_Freeze wrapsPython scripts into executable Windows programs (*.exe files). Whenyou have done this, you
candistributeyourapplicationwithoutrequiringyouruserstoinstallPython.
4.10 Compiling Python on Windows
IfyouwanttocompileCPythonyourself,firstthingyoushoulddoisgetthesource. Youcandownloadeitherthe
latestrelease’ssourceorjustgrabafreshcheckout.
ThesourcetreecontainsabuildsolutionandprojectfilesforMicrosoftVisualStudio,whichisthecompilerusedto
buildtheofficialPythonreleases. ThesefilesareinthePCbuilddirectory.
CheckPCbuild/readme.txtforgeneralinformationonthebuildprocess.
Forextensionmodules,consultbuilding-on-windows.
4.11 The full installer (deprecated)
Deprecatedsinceversion3.14: Thisinstallerisdeprecatedsince3.14andwillnotbeproducedforPython3.16or
later. SeePythonInstallManagerforthemoderninstaller.
4.11.1 Installation steps
FourPython3.14installersareavailablefordownload-twoeachforthe32-bitand64-bitversionsoftheinterpreter.
Thewebinstallerisasmallinitialdownload,anditwillautomaticallydownloadtherequiredcomponentsasneces-
sary. Theofflineinstaller includesthecomponentsnecessaryforadefaultinstallationandonlyrequiresaninternet
connection for optional features. See Installing Without Downloading for other ways to avoid downloading during
installation.
58 Chapter4. UsingPythononWindows

| (cid:181) Seealso |
| --- |
| Win32HowDoI…?
byTimGolden
PythonandCOM
byDavidandPaulBoddie |

### 第65页

Afterstartingtheinstaller,oneoftwooptionsmaybeselected:
Ifyouselect“InstallNow”:
• Youwillnotneedtobeanadministrator(unlessasystemupdatefortheCRuntimeLibraryisrequiredoryou
installthePythonInstallManagerforallusers)
• Pythonwillbeinstalledintoyouruserdirectory
• ThePythonInstallManagerwillbeinstalledaccordingtotheoptionatthebottomofthefirstpage
• Thestandardlibrary,testsuite,launcherandpipwillbeinstalled
• Ifselected,theinstalldirectorywillbeaddedtoyourPATH
• Shortcutswillonlybevisibleforthecurrentuser
Selecting“Customizeinstallation”willallowyoutoselectthefeaturestoinstall, theinstallationlocationandother
optionsorpost-installactions. Toinstalldebuggingsymbolsorbinaries,youwillneedtousethisoption.
Toperformanall-usersinstallation,youshouldselect“Customizeinstallation”. Inthiscase:
• Youmayberequiredtoprovideadministrativecredentialsorapproval
• PythonwillbeinstalledintotheProgramFilesdirectory
• ThePythonInstallManagerwillbeinstalledintotheWindowsdirectory
• Optionalfeaturesmaybeselectedduringinstallation
• Thestandardlibrarycanbepre-compiledtobytecode
• Ifselected,theinstalldirectorywillbeaddedtothesystemPATH
• Shortcutsareavailableforallusers
4.11.2 Removing the MAX_PATH Limitation
Windowshistoricallyhaslimitedpathlengthsto260characters. Thismeantthatpathslongerthanthiswouldnot
resolveanderrorswouldresult.
4.11. Thefullinstaller(deprecated) 59

### 第66页

InthelatestversionsofWindows,thislimitationcanbeexpandedtoapproximately32,000characters. Youradmin-
istrator will need to activate the “Enable Win32 long paths” group policy, or set LongPathsEnabled to 1 in the
registrykeyHKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem.
Thisallowstheopen()function,theosmoduleandmostotherpathfunctionalitytoacceptandreturnpathslonger
than260characters.
Afterchangingtheaboveoption,nofurtherconfigurationisrequired.
Changedinversion3.6: SupportforlongpathswasenabledinPython.
4.11.3 Installing Without UI
All of the options available in the installer UI can also be specified from the command line, allowing scripted in-
stallerstoreplicateaninstallationonmanymachineswithoutuserinteraction. Theseoptionsmayalsobesetwithout
suppressingtheUIinordertochangesomeofthedefaults.
Thefollowingoptions(foundbyexecutingtheinstallerwith/?)canbepassedintotheinstaller:
Name Description
/passive todisplayprogresswithoutrequiringuserinteraction
/quiet toinstall/uninstallwithoutdisplayinganyUI
/simple topreventusercustomization
/uninstall toremovePython(withoutconfirmation)
/layout[directory] topre-downloadallcomponents
/log[filename] tospecifylogfileslocation
Allotheroptionsarepassedasname=value,wherethevalueisusually0todisableafeature,1toenableafeature,
orapath. Thefulllistofavailableoptionsisshownbelow.
60 Chapter4. UsingPythononWindows

| Name | Description |
| --- | --- |
| /passive | todisplayprogresswithoutrequiringuserinteraction |
| /quiet | toinstall/uninstallwithoutdisplayinganyUI |
| /simple | topreventusercustomization |
| /uninstall | toremovePython(withoutconfirmation) |
| /layout[directory] | topre-downloadallcomponents |
| /log[filename] | tospecifylogfileslocation |

### 第67页

Name Description Default
InstallAl- Perform a system-wide installa- 0
lUsers tion.
TargetDir Theinstallationdirectory SelectedbasedonInstallAllUsers
Default- The default installation directory %ProgramFiles%\Python X.Y or
AllUser- forall-userinstalls %ProgramFiles(x86)%\Python X.Y
sTarget-
Dir
De- The default install directory for %LocalAppData%\Programs\Python\PythonXY or
faultJust- just-for-meinstalls %LocalAppData%\Programs\Python\PythonXY-32 or
ForMeTar- %LocalAppData%\Programs\Python\PythonXY-64
getDir
Default- The default custom install direc- (empty)
Custom- torydisplayedintheUI
Target-
Dir
Associ- Create file associations if the 1
ateFiles launcherisalsoinstalled.
Com- Compileall.pyfilesto.pyc. 0
pileAll
Prepend- Prepend install and Scripts direc- 0
Path tories to PATH and add .PY to
PATHEXT
Append- Append install and Scripts direc- 0
Path tories to PATH and add .PY to
PATHEXT
Shortcuts Create shortcuts for the inter- 1
preter,documentationandIDLEif
installed.
In- InstallPythonmanual 1
clude_doc
In- Installdebugbinaries 0
clude_debug
In- Install developer headers and li- 1
clude_dev braries. Omittingthismayleadto
anunusableinstallation.
In- Install python.exe and related 1
clude_exe files. Omittingthismayleadtoan
unusableinstallation.
In- InstallPythonInstallManager. 1
clude_launcher
Install- Installs the launcher for 1
Launcher- all users. Also requires
AllUsers Include_launcher to be
setto1
In- Install standard library and exten- 1
clude_lib sion modules. Omitting this may
leadtoanunusableinstallation.
In- Installbundledpipandsetuptools 1
clude_pip
In- Install debugging symbols (*. 0
clude_symboplsdb)
In- InstallTcl/TksupportandIDLE 1
clude_tcltk
In- Installstandardlibrarytestsuite 1
clude_test
In- Installutilityscripts 1
clude_tools
LauncherOnlOynly installs the launcher. This 0
4.11. Thefullinstaller(deprecated) 61

| Name | Description | Default |
| --- | --- | --- |
| InstallAl-
lUsers | Perform a system-wide installa-
tion. | 0 |
| TargetDir | Theinstallationdirectory | SelectedbasedonInstallAllUsers |
| Default-
AllUser-
sTarget-
Dir | The default installation directory
forall-userinstalls | %ProgramFiles%\Python X.Y or
%ProgramFiles(x86)%\Python X.Y |
| De-
faultJust-
ForMeTar-
getDir | The default install directory for
just-for-meinstalls | %LocalAppData%\Programs\Python\PythonXY or
%LocalAppData%\Programs\Python\PythonXY-32 or
%LocalAppData%\Programs\Python\PythonXY-64 |
| Default-
Custom-
Target-
Dir | The default custom install direc-
torydisplayedintheUI | (empty) |
| Associ-
ateFiles | Create file associations if the
launcherisalsoinstalled. | 1 |
| Com-
pileAll | Compileall.pyfilesto.pyc. | 0 |
| Prepend-
Path | Prepend install and Scripts direc-
tories to PATH and add .PY to
PATHEXT | 0 |
| Append-
Path | Append install and Scripts direc-
tories to PATH and add .PY to
PATHEXT | 0 |
| Shortcuts | Create shortcuts for the inter-
preter,documentationandIDLEif
installed. | 1 |
| In-
clude_doc | InstallPythonmanual | 1 |
| In-
clude_debu | Installdebugbinaries
g | 0 |
| In-
clude_dev | Install developer headers and li-
braries. Omittingthismayleadto
anunusableinstallation. | 1 |
| In-
clude_exe | Install python.exe and related
files. Omittingthismayleadtoan
unusableinstallation. | 1 |
| In-
clude_laun | InstallPythonInstallManager.
cher | 1 |
| Install-
Launcher-
AllUsers | Installs the launcher for
all users. Also requires
Include_launcher to be
setto1 | 1 |
| In-
clude_lib | Install standard library and exten-
sion modules. Omitting this may
leadtoanunusableinstallation. | 1 |
| In-
clude_pip | Installbundledpipandsetuptools | 1 |
| In-
clude_symb | Install debugging symbols (*.
oplsdb) | 0 |
| In-
clude_tcltk | InstallTcl/TksupportandIDLE | 1 |
| In-
clude_test | Installstandardlibrarytestsuite | 1 |
| In-
clude_tools | Installutilityscripts | 1 |
|  |  |  |
| LauncherO
4.11. The | nlOynly installs the launcher. This
fullinstaller(deprecated) | 0
61 |

### 第68页

Forexample,tosilentlyinstalladefault,system-widePythoninstallation,youcouldusethefollowingcommand(from
anelevatedcommandprompt):
python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
ToallowuserstoeasilyinstallapersonalcopyofPythonwithoutthetestsuite,youcouldprovideashortcutwiththe
followingcommand. Thiswilldisplayasimplifiedinitialpageanddisallowcustomization:
python-3.9.0.exe InstallAllUsers=0 Include_launcher=0 Include_test=0
SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."
(Notethatomittingthelauncheralsoomitsfileassociations,andisonlyrecommendedforper-userinstallswhenthere
isalsoasystem-wideinstallationthatincludedthelauncher.)
The options listed above can also be provided in a file named unattend.xml alongside the executable. This file
specifiesalistofoptionsandvalues. Whenavalueisprovidedasanattribute, itwillbeconvertedtoanumberif
possible. Valuesprovidedaselementtextarealwaysleftasstrings. Thisexamplefilesetsthesameoptionsasthe
previousexample:
<Options>
<Option Name="InstallAllUsers" Value="no" />
<Option Name="Include_launcher" Value="0" />
<Option Name="Include_test" Value="no" />
<Option Name="SimpleInstall" Value="yes" />
<Option Name="SimpleInstallDescription">Just for me, no test suite</Option>
</Options>
4.11.4 Installing Without Downloading
AssomefeaturesofPythonarenotincludedintheinitialinstallerdownload,selectingthosefeaturesmayrequirean
internetconnection. Toavoidthisneed,allpossiblecomponentsmaybedownloadedon-demandtocreateacomplete
layoutthatwillnolongerrequireaninternetconnectionregardlessoftheselectedfeatures. Notethatthisdownload
maybebiggerthanrequired,butwherealargenumberofinstallationsaregoingtobeperformeditisveryusefulto
havealocallycachedcopy.
Execute the following command from Command Prompt to download all possible required files. Remember to
substitutepython-3.9.0.exefortheactualnameofyourinstaller,andtocreatelayoutsintheirowndirectories
toavoidcollisionsbetweenfileswiththesamename.
python-3.9.0.exe /layout [optional target directory]
Youmayalsospecifythe/quietoptiontohidetheprogressdisplay.
4.11.5 Modifying an install
OncePythonhasbeeninstalled,youcanaddorremovefeaturesthroughtheProgramsandFeaturestoolthatispart
ofWindows. SelectthePythonentryandchoose“Uninstall/Change”toopentheinstallerinmaintenancemode.
“Modify”allowsyoutoaddorremovefeaturesbymodifyingthecheckboxes-unchangedcheckboxeswillnotinstall
orremoveanything. Someoptionscannotbechangedinthismode,suchastheinstalldirectory;tomodifythese,you
willneedtoremoveandthenreinstallPythoncompletely.
“Repair” will verify all the files that should be installed using the current settings and replace any that have been
removedormodified.
“Uninstall”willremovePythonentirely,withtheexceptionofthePythonInstallManager,whichhasitsownentry
inProgramsandFeatures.
62 Chapter4. UsingPythononWindows

### 第69页

4.11.6 Installing Free-threaded Binaries
Addedinversion3.13: (Experimental)
(cid:174) Note
Everything described in this section is considered experimental, and should be expected to change in future
releases.
Toinstallpre-builtbinarieswithfree-threadingenabled(seePEP703),youshouldselect“Customizeinstallation”.
Thesecondpageofoptionsincludesthe“Downloadfree-threadedbinaries”checkbox.
Selecting this option will download and install additional binaries to the same location as the main Python install.
Themainexecutableiscalledpython3.13t.exe,andotherbinarieseitherreceiveatsuffixorafullABIsuffix.
Pythonsourcefilesandbundledthird-partydependenciesaresharedwiththemaininstall.
Thefree-threadedversionisregisteredasaregularPythoninstallwiththetag3.13t(witha-32or-arm64suffixas
normalforthoseplatforms). Thisallowstoolstodiscoverit,andforthePythonInstallManagertosupportpy.exe
-3.13t. Notethatthelauncherwillinterpretpy.exe -3(orapython3shebang)as“thelatest3.xinstall”,which
willpreferthefree-threadedbinariesovertheregularones,whilepy.exe -3.13willnot. Ifyouusetheshortstyle
ofoption,youmayprefertonotinstallthefree-threadedbinariesatthistime.
Tospecifytheinstalloptionatthecommandline,useInclude_freethreaded=1. SeeInstallingWithoutDown-
loadingforinstructionsonpre-emptivelydownloadingtheadditionalbinariesforofflineinstall. Theoptionstoinclude
debugsymbolsandbinariesalsoapplytothefree-threadedbuilds.
Free-threadedbinariesarealsoavailableonnuget.org.
4.12 Python Launcher for Windows (Deprecated)
Deprecated since version 3.14: The launcher and this documentation have been superseded by the Python Install
Managerdescribedabove. Thisispreservedtemporarilyforhistoricalinterest.
Addedinversion3.3.
4.12. PythonLauncherforWindows(Deprecated) 63

### 第70页

ThePythonlauncherforWindowsisautilitywhichaidsinlocatingandexecutingofdifferentPythonversions. It
allowsscripts(orthecommand-line)toindicateapreferenceforaspecificPythonversion,andwilllocateandexecute
thatversion.
UnlikethePATHvariable,thelauncherwillcorrectlyselectthemostappropriateversionofPython. Itwillpreferper-
userinstallationsoversystem-wideones,andordersbylanguageversionratherthanusingthemostrecentlyinstalled
version.
ThelauncherwasoriginallyspecifiedinPEP397.
4.12.1 Getting started
Fromthecommand-line
Changedinversion3.6.
System-wide installations of Python 3.3 and later will put the launcher on your PATH. The launcher is compatible
withallavailableversionsofPython,soitdoesnotmatterwhichversionisinstalled. Tocheckthatthelauncheris
available,executethefollowingcommandinCommandPrompt:
py
YoushouldfindthatthelatestversionofPythonyouhaveinstalledisstarted-itcanbeexitedasnormal,andany
additionalcommand-lineargumentsspecifiedwillbesentdirectlytoPython.
If you have multiple versions of Python installed (e.g., 3.7 and 3.14) you will have noticed that Python 3.14 was
started-tolaunchPython3.7,trythecommand:
py -3.7
IfyouwantthelatestversionofPython2youhaveinstalled,trythecommand:
py -2
Ifyouseethefollowingerror,youdonothavethelauncherinstalled:
'py' is not recognized as an internal or external command,
operable program or batch file.
Thecommand:
py --list
displaysthecurrentlyinstalledversion(s)ofPython.
The-x.yargumentistheshortformofthe-V:Company/Tagargument,whichallowsselectingaspecificPython
runtime, including those that may have come from somewhere other than python.org. Any runtime registered by
followingPEP514willbediscoverable. The--listcommandlistsallavailableruntimesusingthe-V:format.
When using the -V: argument, specifying the Company will limit selection to runtimes from that provider, while
specifyingonlytheTagwillselectfromallproviders. Notethatomittingtheslashimpliesatag:
# Select any '3.*' tagged runtime
py -V:3
# Select any 'PythonCore' released runtime
py -V:PythonCore/
# Select PythonCore's latest Python 3 runtime
py -V:PythonCore/3
Theshortformoftheargument(-3)onlyeverselectsfromcorePythonreleases,andnototherdistributions. However,
thelongerform(-V:3)willselectfromany.
64 Chapter4. UsingPythononWindows

### 第71页

TheCompanyismatchedonthefullstring,case-insensitive. TheTagismatchedoneitherthefullstring,oraprefix,
provided the next character is a dot or a hyphen. This allows -V:3.1 to match 3.1-32, but not 3.10. Tags are
sortedusingnumericalordering(3.10isnewerthan3.1),butarecomparedusingtext(-V:3.01doesnotmatch
3.1).
Virtualenvironments
Addedinversion3.5.
If the launcher is run with no explicit Python version specification, and a virtual environment (created with the
standardlibraryvenvmoduleortheexternalvirtualenvtool)active,thelauncherwillrunthevirtualenvironment’s
interpreter rather than the global one. To run the global interpreter, either deactivate the virtual environment, or
explicitlyspecifytheglobalPythonversion.
Fromascript
Let’screateatestPythonscript-createafilecalledhello.pywiththefollowingcontents
#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
Fromthedirectoryinwhichhello.pylives,executethecommand:
py hello.py
YoushouldnoticetheversionnumberofyourlatestPython2.xinstallationisprinted. Nowtrychangingthefirstline
tobe:
#! python3
Re-executing the command should now print the latest Python 3.x information. As with the above command-line
examples,youcanspecifyamoreexplicitversionqualifier. AssumingyouhavePython3.7installed,trychanging
thefirstlineto#! python3.7andyoushouldfindthe3.7versioninformationprinted.
Note that unlike interactive use, a bare “python” will use the latest version of Python 2.x that you have installed.
ThisisforbackwardcompatibilityandforcompatibilitywithUnix,wherethecommandpythontypicallyrefersto
Python2.
Fromfileassociations
The launcher should have been associated with Python files (i.e. .py, .pyw, .pyc files) when it was installed.
Thismeansthatwhenyoudouble-clickononeofthesefilesfromWindowsexplorerthelauncherwillbeused,and
thereforeyoucanusethesamefacilitiesdescribedabovetohavethescriptspecifytheversionwhichshouldbeused.
ThekeybenefitofthisisthatasinglelaunchercansupportmultiplePythonversionsatthesametimedependingon
thecontentsofthefirstline.
4.12.2 Shebang Lines
Ifthefirstlineofascriptfilestartswith#!, itisknownasa“shebang”line. LinuxandotherUnixlikeoperating
systems have native support for such lines and they are commonly used on such systems to indicate how a script
should be executed. This launcher allows the same facilities to be used with Python scripts on Windows and the
examplesabovedemonstratetheiruse.
ToallowshebanglinesinPythonscriptstobeportablebetweenUnixandWindows,thislaunchersupportsanumber
of‘virtual’commandstospecifywhichinterpretertouse. Thesupportedvirtualcommandsare:
• /usr/bin/env
• /usr/bin/python
• /usr/local/bin/python
4.12. PythonLauncherforWindows(Deprecated) 65

### 第72页

• python
Forexample,ifthefirstlineofyourscriptstartswith
#! /usr/bin/python
ThedefaultPythonoranactivevirtualenvironmentwillbelocatedandused. AsmanyPythonscriptswrittentowork
onUnixwillalreadyhavethisline,youshouldfindthesescriptscanbeusedbythelauncherwithoutmodification. If
youarewritinganewscriptonWindowswhichyouhopewillbeusefulonUnix,youshoulduseoneoftheshebang
linesstartingwith/usr.
Any of the above virtual commands can be suffixed with an explicit version (either just the major version, or the
majorandminorversion). Furthermorethe32-bitversioncanberequestedbyadding“-32”aftertheminorversion.
I.e. /usr/bin/python3.7-32willrequestusageofthe32-bitPython3.7. Ifavirtualenvironmentisactive,the
versionwillbeignoredandtheenvironmentwillbeused.
Addedinversion3.7: Beginningwithpythonlauncher3.7itispossibletorequest64-bitversionbythe“-64”suffix.
Furthermoreitispossibletospecifyamajorandarchitecturewithoutminor(i.e. /usr/bin/python3-64).
Changed in version 3.11: The “-64” suffix is deprecated, and now implies “any architecture that is not provably
i386/32-bit”. Torequestaspecificenvironment,usethenew-V:TAGargumentwiththecompletetag.
Changed in version 3.13: Virtual commands referencing python now prefer an active virtual environment rather
thansearchingPATH.Thishandlescaseswheretheshebangspecifies/usr/bin/env python3butpython3.exe
isnotpresentintheactiveenvironment.
The/usr/bin/envformofshebanglinehasonefurtherspecialproperty. BeforelookingforinstalledPythoninter-
preters,thisformwillsearchtheexecutablePATHforaPythonexecutablematchingthenameprovidedasthefirstar-
gument. ThiscorrespondstothebehaviouroftheUnixenvprogram,whichperformsaPATHsearch. Ifanexecutable
matchingthefirstargumentaftertheenvcommandcannotbefound,buttheargumentstartswithpython,itwillbe
handledasdescribedfortheothervirtualcommands. TheenvironmentvariablePYLAUNCHER_NO_SEARCH_PATH
maybeset(toanyvalue)toskipthissearchofPATH.
Shebanglinesthatdonotmatchanyofthesepatternsarelookedupinthe [commands] sectionofthelauncher’s
.INIfile. Thismaybeusedtohandlecertaincommandsinawaythatmakessenseforyoursystem. Thenameofthe
commandmustbeasingleargument(nospacesintheshebangexecutable),andthevaluesubstitutedisthefullpath
totheexecutable(additionalargumentsspecifiedinthe.INIwillbequotedaspartofthefilename).
[commands]
/bin/xpython=C:\Program Files\XPython\python.exe
Anycommandsnotfoundinthe.INIfilearetreatedasWindowsexecutablepathsthatareabsoluteorrelativetothe
directorycontainingthescriptfile. ThisisaconvenienceforWindows-onlyscripts, suchasthosegeneratedbyan
installer,sincethebehaviorisnotcompatiblewithUnix-styleshells. Thesepathsmaybequoted,andmayinclude
multiplearguments,afterwhichthepathtothescriptandanyadditionalargumentswillbeappended.
4.12.3 Arguments in shebang lines
TheshebanglinescanalsospecifyadditionaloptionstobepassedtothePythoninterpreter. Forexample,ifyouhave
ashebangline:
#! /usr/bin/python -v
ThenPythonwillbestartedwiththe-voption
4.12.4 Customization
CustomizationviaINIfiles
Two .ini files will be searched by the launcher - py.ini in the current user’s application data directory
(%LOCALAPPDATA% or$env:LocalAppData)and py.ini inthesamedirectoryas thelauncher. Thesame.ini
filesareusedforboththe‘console’versionofthelauncher(i.e. py.exe)andforthe‘windows’version(i.e. pyw.exe).
66 Chapter4. UsingPythononWindows

### 第73页

Customizationspecifiedinthe“applicationdirectory”willhaveprecedenceovertheonenexttotheexecutable,soa
user,whomaynothavewriteaccesstothe.inifilenexttothelauncher,canoverridecommandsinthatglobal.ini
file.
CustomizingdefaultPythonversions
Insomecases,aversionqualifiercanbeincludedinacommandtodictatewhichversionofPythonwillbeusedby
thecommand. Aversionqualifierstartswithamajorversionnumberandcanoptionallybefollowedbyaperiod(‘.’)
andaminorversionspecifier. Furthermoreitispossibletospecifyifa32or64bitimplementationshallberequested
byadding“-32”or“-64”.
Forexample,ashebanglineof#!pythonhasnoversionqualifier,while#!python3hasaversionqualifierwhich
specifiesonlyamajorversion.
If no version qualifiers are found in a command, the environment variable PY_PYTHON can be set to specify the
defaultversionqualifier. Ifitisnotset,thedefaultis“3”. Thevariablecanspecifyanyvaluethatmaybepassedon
thecommandline, suchas“3”, “3.7”, “3.7-32”or“3.7-64”. (Notethatthe“-64”optionisonlyavailablewiththe
launcherincludedwithPython3.7ornewer.)
If no minor version qualifiers are found, the environment variable PY_PYTHON{major} (where {major} is the
currentmajorversionqualifierasdeterminedabove)canbesettospecifythefullversion. Ifnosuchoptionisfound,
thelauncherwillenumeratetheinstalledPythonversionsandusethelatestminorreleasefoundforthemajorversion,
whichislikely,althoughnotguaranteed,tobethemostrecentlyinstalledversioninthatfamily.
On64-bitWindowswithboth32-bitand64-bitimplementationsofthesame(major.minor)Pythonversioninstalled,
the 64-bit version will always be preferred. This will be true for both 32-bit and 64-bit implementations of the
launcher-a32-bitlauncherwillprefertoexecutea64-bitPythoninstallationofthespecifiedversionifavailable.
This is so the behavior of the launcher can be predicted knowing only what versions are installed on the PC and
without regard to the order in which they were installed (i.e., without knowing whether a 32 or 64-bit version of
Pythonandcorrespondinglauncherwasinstalledlast). Asnotedabove,anoptional“-32”or“-64”suffixcanbeused
onaversionspecifiertochangethisbehaviour.
Examples:
• If no relevant options are set, the commands python and python2 will use the latest Python 2.x version
installedandthecommandpython3willusethelatestPython3.xinstalled.
• Thecommandpython3.7willnotconsultanyoptionsatallastheversionsarefullyspecified.
• IfPY_PYTHON=3,thecommandspythonandpython3willbothusethelatestinstalledPython3version.
• IfPY_PYTHON=3.7-32,thecommandpythonwillusethe32-bitimplementationof3.7whereasthecom-
mandpython3willusethelatestinstalledPython(PY_PYTHONwasnotconsideredatallasamajorversion
wasspecified.)
• IfPY_PYTHON=3andPY_PYTHON3=3.7,thecommandspythonandpython3willbothusespecifically3.7
Inadditiontoenvironmentvariables,thesamesettingscanbeconfiguredinthe.INIfileusedbythelauncher. The
sectionintheINIfileiscalled[defaults]andthekeynamewillbethesameastheenvironmentvariableswithout
theleadingPY_prefix(andnotethatthekeynamesintheINIfilearecaseinsensitive.) Thecontentsofanenvironment
variablewilloverridethingsspecifiedintheINIfile.
Forexample:
• SettingPY_PYTHON=3.7isequivalenttotheINIfilecontaining:
[defaults]
python=3.7
• SettingPY_PYTHON=3andPY_PYTHON3=3.7isequivalenttotheINIfilecontaining:
[defaults]
python=3
python3=3.7
4.12. PythonLauncherforWindows(Deprecated) 67

### 第74页

4.12.5 Diagnostics
IfanenvironmentvariablePYLAUNCHER_DEBUGisset(toanyvalue),thelauncherwillprintdiagnosticinformation
tostderr(i.e. totheconsole). Whilethisinformationmanagestobesimultaneouslyverboseandterse,itshouldallow
youtoseewhatversionsofPythonwerelocated,whyaparticularversionwaschosenandtheexactcommand-line
usedtoexecutethetargetPython. Itisprimarilyintendedfortestinganddebugging.
4.12.6 Dry Run
If an environment variable PYLAUNCHER_DRYRUN is set (to any value), the launcher will output the command it
wouldhaverun, butwillnotactuallylaunchPython. Thismaybeusefulfortoolsthatwanttousethelauncherto
detectandthenlaunchPythondirectly. Notethatthecommandwrittentostandardoutputisalwaysencodedusing
UTF-8,andmaynotrendercorrectlyintheconsole.
4.12.7 Install on demand
IfanenvironmentvariablePYLAUNCHER_ALLOW_INSTALLisset(toanyvalue),andtherequestedPythonversion
isnotinstalledbutisavailableontheMicrosoftStore,thelauncherwillattempttoinstallit. Thismayrequireuser
interactiontocomplete,andyoumayneedtorunthecommandagain.
AnadditionalPYLAUNCHER_ALWAYS_INSTALLvariablecausesthelaunchertoalwaystrytoinstallPython,evenif
itisdetected. Thisismainlyintendedfortesting(andshouldbeusedwithPYLAUNCHER_DRYRUN).
4.12.8 Return codes
ThefollowingexitcodesmaybereturnedbythePythonlauncher. Unfortunately,thereisnowaytodistinguishthese
fromtheexitcodeofPythonitself.
Thenamesofcodesareasusedinthesources,andareonlyforreference. Thereisnowaytoaccessorresolvethem
apartfromreadingthispage. Entriesarelistedinalphabeticalorderofnames.
Name Value Description
RC_BAD_VENV_CFG 107 Apyvenv.cfgwasfoundbutiscorrupt.
RC_CREATE_PROCESS 101 FailedtolaunchPython.
RC_INSTALLING 111 Aninstallwasstarted,butthecommandwillneedtobere-runafteritcom-
pletes.
RC_INTERNAL_ERROR 109 Unexpectederror. Pleasereportabug.
RC_NO_COMMANDLINE108 Unabletoobtaincommandlinefromtheoperatingsystem.
RC_NO_PYTHON 103 Unabletolocatetherequestedversion.
RC_NO_VENV_CFG 106 Apyvenv.cfgwasrequiredbutnotfound.
68 Chapter4. UsingPythononWindows

| Name | Value | Description |
| --- | --- | --- |
| RC_BAD_VENV_CFG | 107 | Apyvenv.cfgwasfoundbutiscorrupt. |
| RC_CREATE_PROCESS | 101 | FailedtolaunchPython. |
| RC_INSTALLING | 111 | Aninstallwasstarted,butthecommandwillneedtobere-runafteritcom-
pletes. |
| RC_INTERNAL_ERROR | 109 | Unexpectederror. Pleasereportabug. |
| RC_NO_COMMANDLIN | E108 | Unabletoobtaincommandlinefromtheoperatingsystem. |
| RC_NO_PYTHON | 103 | Unabletolocatetherequestedversion. |
| RC_NO_VENV_CFG | 106 | Apyvenv.cfgwasrequiredbutnotfound. |

### 第75页

CHAPTER
FIVE
USING PYTHON ON MACOS
ThisdocumentaimstogiveanoverviewofmacOS-specificbehavioryoushouldknowabouttogetstartedwithPython
onMaccomputers. PythononaMacrunningmacOSisverysimilartoPythononotherUnix-derivedplatforms,but
therearesomedifferencesininstallationandsomefeatures.
There are various ways to obtain and install Python for macOS. Pre-built versions of the most recent versions of
Pythonareavailablefromanumberofdistributors. MuchofthisdocumentdescribesuseofthePythonsprovided
bytheCPythonreleaseteamfordownloadfromthepython.orgwebsite. SeeAlternativeDistributionsforsomeother
options.
5.1 Using Python for macOS from python.org
5.1.1 Installation steps
ForcurrentPythonversions(otherthanthoseinsecuritystatus),thereleaseteamproducesaPythonformacOS
installerpackageforeachnewrelease. Alistofavailableinstallersisavailablehere. Werecommendusingthemost
recentsupportedPythonversionwherepossible. Currentinstallersprovideauniversal2binarybuildofPythonwhich
runsnativelyonallMacs(AppleSiliconandIntel)thataresupportedbyawiderangeofmacOSversions,currently
typicallyfromatleastmacOS10.15Catalinaon.
ThedownloadedfileisastandardmacOSinstallerpackagefile(.pkg). Fileintegrityinformation(checksum,size,
sigstoresignature,etc)foreachfileisincludedonthereleasedownloadpage. Installerpackagesandtheircontents
aresignedandnotarizedwithPython Software FoundationAppleDeveloperIDcertificatestomeetmacOS
Gatekeeperrequirements.
For a default installation, double-click on the downloaded installer package file. This should launch the standard
macOSInstallerappanddisplaythefirstofseveralinstallerwindowssteps.
69

### 第76页

ClickingontheContinuebuttonbringsuptheReadMeforthisinstaller. Besidesotherimportantinformation,the
ReadMedocumentswhichPythonversionisgoingtobeinstalledandonwhatversionsofmacOSitissupported. You
mayneedtoscrollthroughtoreadthewholefile. Bydefault,thisReadMewillalsobeinstalledin/Applications/
Python 3.14/andavailabletoreadanytime.
70 Chapter5. UsingPythononmacOS

### 第77页

ClickingonContinueproceedstodisplaythelicenseforPythonandforotherincludedsoftware. Youwillthenneed
toAgreetothelicensetermsbeforeproceedingtothenextstep. Thislicensefilewillalsobeinstalledandavailable
tobereadlater.
5.1. UsingPythonformacOSfrom 71

### 第78页

Afterthelicensetermsareaccepted,thenextstepistheInstallationTypedisplay. Formostuses,thestandardset
ofinstallationoperationsisappropriate.
72 Chapter5. UsingPythononmacOS

### 第79页

BypressingtheCustomizebutton,youcanchoosetoomitorselectcertainpackagecomponentsoftheinstaller. Click
oneachpackagenametoseeadescriptionofwhatitinstalls. Toalsoinstallsupportfortheoptionalfree-threaded
feature,seeInstallingFree-threadedBinaries.
5.1. UsingPythonformacOSfrom 73

### 第80页

Ineithercase,clickingInstallwillbegintheinstallprocessbyaskingpermissiontoinstallnewsoftware. AmacOS
usernamewithAdministratorprivilegeisneededastheinstalledPythonwillbeavailabletoallusersoftheMac.
Whentheinstallationiscomplete,theSummarywindowwillappear.
74 Chapter5. UsingPythononmacOS

### 第81页

Double-click on the Install Certificates.command icon or file in the /Applications/Python 3.14/
windowtocompletetheinstallation.
ThiswillopenatemporaryTerminalshellwindowthatwillusethenewPythontodownloadandinstallSSLroot
certificatesforitsuse.
5.1. UsingPythonformacOSfrom 75

### 第82页

IfSuccessfully installed certifiandupdate completeappearsintheterminalwindow,theinstallation
iscomplete. Closethisterminalwindowandtheinstallerwindow.
Adefaultinstallwillinclude:
• APython 3.14folderinyourApplicationsfolder. InhereyoufindIDLE,thedevelopmentenvironment
thatisastandardpartofofficialPythondistributions;andPython Launcher,whichhandlesdouble-clicking
PythonscriptsfromthemacOSFinder.
• A framework /Library/Frameworks/Python.framework, which includes the Python executable and
libraries. Theinstalleraddsthislocationtoyourshellpath. TouninstallPython,youcanremovethesethree
things. SymlinkstothePythonexecutableareplacedin/usr/local/bin/.
(cid:174) Note
RecentversionsofmacOSincludeapython3commandin/usr/bin/python3thatlinkstoausuallyolder
and incomplete version of Python provided by and for use by the Apple development tools, Xcode or the
Command Line Tools for Xcode. You should never modify or attempt to delete this installation, as it is
Apple-controlledandisusedbyApple-providedorthird-partysoftware. IfyouchoosetoinstallanewerPython
versionfrompython.org,youwillhavetwodifferentbutfunctionalPythoninstallationsonyourcomputerthat
can co-exist. The default installer options should ensure that its python3 will be used instead of the system
python3.
76 Chapter5. UsingPythononmacOS

### 第83页

5.1.2 How to run a Python script
TherearetwowaystoinvokethePythoninterpreter. IfyouarefamiliarwithusingaUnixshellinaterminalwindow,
youcaninvokepython3.14orpython3optionallyfollowedbyoneormorecommandlineoptions(describedin
Commandlineandenvironment). ThePythontutorialalsohasausefulsectiononusingPythoninteractivelyfroma
shell.
Youcanalsoinvoketheinterpreterthroughanintegrateddevelopmentenvironment. idleisabasiceditorandinter-
preterenvironmentwhichisincludedwiththestandarddistributionofPython. IDLEincludesaHelpmenuthatallows
youtoaccessPythondocumentation. IfyouarecompletelynewtoPython,youcanreadthetutorialintroductionin
thatdocument.
TherearemanyothereditorsandIDEsavailable,seeEditorsandIDEsformoreinformation.
TorunaPythonscriptfilefromtheterminalwindow,youcaninvoketheinterpreterwiththenameofthescriptfile:
python3.14myscript.py
TorunyourscriptfromtheFinder,youcaneither:
• DragittoPython Launcher.
• SelectPython Launcherasthedefaultapplicationtoopenyourscript(orany.pyscript)throughtheFinder
Info window and double-click it. Python Launcher has various preferences to control how your script is
launched. Option-draggingallowsyoutochangetheseforoneinvocation,oruseitsPreferencesmenuto
changethingsglobally.
BeawarethatrunningthescriptdirectlyfromthemacOSFindermightproducedifferentresultsthanwhenrunning
from a terminal window as the script will not be run in the usual shell environment including any setting of envi-
ronment variables in shell profiles. And, as with any other script or program, be certain of what you are about to
run.
5.2 Alternative Distributions
Besidesthestandardpython.orgformacOSinstaller,therearethird-partydistributionsformacOSthatmayinclude
additionalfunctionality. Somepopulardistributionsandtheirkeyfeatures:
ActivePython
Installerwithmulti-platformcompatibility,documentation
Anaconda
Popularscientificmodules(suchasnumpy,scipy,andpandas)andthecondapackagemanager.
Homebrew
PackagemanagerformacOSincludingmultipleversionsofPythonandmanythird-partyPython-basedpack-
ages(includingnumpy,scipy,andpandas).
MacPorts
Another package manager for macOS including multiple versions of Python and many third-party Python-
basedpackages. Mayincludepre-builtversionsofPythonandmanypackagesforolderversionsofmacOS.
NotethatdistributionsmightnotincludethelatestversionsofPythonorotherlibraries,andarenotmaintainedor
supportedbythecorePythonteam.
5.3 Installing Additional Python Packages
RefertothePythonPackagingUserGuideformoreinformation.
5.4 GUI Programming
ThereareseveraloptionsforbuildingGUIapplicationsontheMacwithPython.
5.2. AlternativeDistributions 77

### 第84页

ThestandardPythonGUItoolkitistkinter,basedonthecross-platformTktoolkit(https://www.tcl.tk). AmacOS-
nativeversionofTkisincludedwiththeinstaller.
PyObjC is a Python binding to Apple’s Objective-C/Cocoa framework. Information on PyObjC is available from
pyobjc.
AnumberofalternativemacOSGUItoolkitsareavailableincluding:
• PySide: OfficialPythonbindingstotheQtGUItoolkit.
• PyQt: AlternativePythonbindingstoQt.
• Kivy: Across-platformGUItoolkitthatsupportsdesktopandmobileplatforms.
• Toga: PartoftheBeeWareProject;supportsdesktop,mobile,webandconsoleapps.
• wxPython: Across-platformtoolkitthatsupportsdesktopoperatingsystems.
5.5 Advanced Topics
5.5.1 Installing Free-threaded Binaries
Addedinversion3.13.
Thepython.orgPythonformacOSinstallerpackagecanoptionallyinstallanadditionalbuildofPython3.14that
supportsPEP703,thefree-threadingfeature(runningwiththeglobalinterpreterlockdisabled). Checktherelease
pageonpython.orgforpossibleupdatedinformation.
Thefree-threadedmodeisworkingandcontinuestobeimproved,butthereissomeadditionaloverheadinsingle-
threaded workloads compared to the regular build. Additionally, third-party packages, in particular ones with an
extension module, may not be ready for use in a free-threaded build, and will re-enable the GIL. Therefore, the
supportforfree-threadingisnotinstalledbydefault. Itispackagedasaseparateinstalloption,availablebyclicking
theCustomizebuttonontheInstallationTypestepoftheinstallerasdescribedabove.
78 Chapter5. UsingPythononmacOS

### 第85页

IftheboxnexttotheFree-threadedPythonpackagenameischecked,aseparatePythonT.frameworkwillalso
be installed alongside the normal Python.framework in /Library/Frameworks. This configuration allows a
free-threaded Python 3.14 build to co-exist on your system with a traditional (GIL only) Python 3.14 build with
minimalriskwhileinstallingortesting. Thisinstallationlayoutmaychangeinfuturereleases.
Knowncautionsandlimitations:
• TheUNIXcommand-linetoolspackage,whichisselectedbydefault,willinstalllinksin/usr/local/bin
forpython3.14t,thefree-threadedinterpreter,andpython3.14t-config,aconfigurationutilitywhich
maybeusefulforpackagebuilders. Since/usr/local/binistypicallyincludedinyourshellPATH,inmost
casesnochangestoyourPATHenvironmentvariablesshouldbeneededtousepython3.14t.
• For this release, the Shell profile updater package and the Update Shell Profile.command in /
Applications/Python 3.14/donotsupportthefree-threadedpackage.
• The free-threaded build and the traditional build have separate search paths and separate site-packages
directoriesso,bydefault,ifyouneedapackageavailableinbothbuilds,itmayneedtobeinstalledinboth.
Thefree-threadedpackagewillinstallaseparateinstanceofpipforusewithpython3.14t.
– Toinstallapackageusingpipwithoutavenv:
python3.14t -m pip install <package_name>
• When working with multiple Python environments, it is usually safest and easiest to create and use virtual
environments. ThiscanavoidpossiblecommandnameconflictsandconfusionaboutwhichPythonisinuse:
python3.14t -m venv <venv_name>
thenactivate.
• Torunafree-threadedversionofIDLE:
python3.14t -m idlelib
• TheinterpretersinbothbuildsrespondtothesamePYTHONenvironmentvariableswhichmayhaveunexpected
results,forexample,ifyouhavePYTHONPATHsetinashellprofile. Ifnecessary,therearecommandlineoptions
like-Etoignoretheseenvironmentvariables.
• The free-threaded build links to the third-party shared libraries, such as OpenSSL and Tk, installed in the
traditionalframework. Thismeansthatbothbuildsalsoshareonesetoftrustcertificatesasinstalledbythe
Install Certificates.commandscript,thusitonlyneedstoberunonce.
• Ifyoucannotdependonthelinkin/usr/local/binpointingtothepython.orgfree-threadedpython3.
14t (for example, if you want to install your own version there or some other distribution does), you can
explicitlysetyourshellPATHenvironmentvariabletoincludethePythonTframeworkbindirectory:
export PATH="/Library/Frameworks/PythonT.framework/Versions/3.14/bin":"$PATH"
The traditional framework installation by default does something similar, except for Python.framework.
Be aware that having both framework bin directories in PATH can lead to confusion if there are duplicate
nameslikepython3.14inboth;whichoneisactuallyuseddependsontheordertheyappearinPATH.The
which python3.x or which python3.xt commands can show which path is being used. Using virtual
environmentscanhelpavoidsuchambiguities. Anotheroptionmightbetocreateashellaliastothedesired
interpreter,like:
alias py3.14="/Library/Frameworks/Python.framework/Versions/3.14/bin/python3.
,→14"
alias py3.14t="/Library/Frameworks/PythonT.framework/Versions/3.14/bin/python3.
,→14t"
5.5.2 Installing using the command line
Ifyouwanttouseautomationtoinstallthepython.orginstallerpackage(ratherthanbyusingthefamiliarmacOS
Installer GUI app), the macOS command line installer utility lets you select non-default options, too. If
you are not familiar with installer, it can be somewhat cryptic (see man installer for more information).
As an example, the following shell snippet shows one way to do it, using the 3.14.0b2 release and selecting the
free-threadedinterpreteroption:
5.5. AdvancedTopics 79

### 第86页

RELEASE="python-3.140b2-macos11.pkg"
# download installer pkg
curl -O https://www.python.org/ftp/python/3.14.0/${RELEASE}
# create installer choicechanges to customize the install:
# enable the PythonTFramework-3.14 package
# while accepting the other defaults (install all other packages)
cat > ./choicechanges.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/
,→PropertyList-1.0.dtd">
<plist version="1.0">
<array>
<dict>
<key>attributeSetting</key>
<integer>1</integer>
<key>choiceAttribute</key>
<string>selected</string>
<key>choiceIdentifier</key>
<string>org.python.Python.PythonTFramework-3.14</string>
</dict>
</array>
</plist>
EOF
sudo installer -pkg ./${RELEASE} -applyChoiceChangesXML ./choicechanges.plist␣
,→-target /
Youcanthentestthatbothinstallerbuildsarenowavailablewithsomethinglike:
$ # test that the free-threaded interpreter was installed if the Unix Command␣
,→Tools package was enabled
$ /usr/local/bin/python3.14t -VV
Python 3.14.0b2 free-threading build (v3.14.0b2:3a83b172af, Jun 5 2024, 12:57:31)␣
,→[Clang 15.0.0 (clang-1500.3.9.4)]
$ # and the traditional interpreter
$ /usr/local/bin/python3.14 -VV
Python 3.14.0b2 (v3.14.0b2:3a83b172af, Jun 5 2024, 12:50:24) [Clang 15.0.0␣
,→(clang-1500.3.9.4)]
$ # test that they are also available without the prefix if /usr/local/bin is on
,→$PATH
$ python3.14t -VV
Python 3.14.0b2 free-threading build (v3.14.0b2:3a83b172af, Jun 5 2024, 12:57:31)␣
,→[Clang 15.0.0 (clang-1500.3.9.4)]
$ python3.14 -VV
Python 3.14.0b2 (v3.14.0b2:3a83b172af, Jun 5 2024, 12:50:24) [Clang 15.0.0␣
,→(clang-1500.3.9.4)]
(cid:174) Note
Currentpython.orginstallersonlyinstalltofixedlocationslike/Library/Frameworks/,/Applications,
and/usr/local/bin. Youcannotusetheinstaller-domainoptiontoinstalltootherlocations.
80 Chapter5. UsingPythononmacOS

### 第87页

5.5.3 Distributing Python Applications
ArangeoftoolsexistforconvertingyourPythoncodeintoastandalonedistributableapplication:
• py2app: SupportscreatingmacOS.appbundlesfromaPythonproject.
• Briefcase:PartoftheBeeWareProject;across-platformpackagingtoolthatsupportscreationof.appbundles
onmacOS,aswellasmanagingsigningandnotarization.
• PyInstaller: Across-platformpackagingtoolthatcreatesasinglefileorfolderasadistributableartifact.
5.5.4 App Store Compliance
AppssubmittedfordistributionthroughthemacOSAppStoremustpassApple’sappreviewprocess. Thisprocess
includesasetofautomatedvalidationrulesthatinspectthesubmittedapplicationbundleforproblematiccode.
ThePythonstandardlibrarycontainssomecodethatisknowntoviolatetheseautomatedrules. Whiletheseviolations
appeartobefalsepositives,Apple’sreviewrulescannotbechallenged. Therefore,itisnecessarytomodifythePython
standardlibraryforanapptopassAppStorereview.
The Python source tree contains a patch file that will remove all code that is known to cause issues with
the App Store review process. This patch is applied automatically when CPython is configured with the
--with-app-store-complianceoption.
ThispatchisnotnormallyrequiredtouseCPythononaMac;norisitrequiredifyouaredistributinganappoutside
themacOSAppStore. ItisonlyrequiredifyouareusingthemacOSAppStoreasadistributionchannel.
5.6 Other Resources
Thepython.orgHelppagehaslinkstomanyusefulresources. ThePythonmac-SIGmailinglistisanothersupport
resourcespecificallyforPythonusersanddevelopersontheMac.
5.6. OtherResources 81

### 第88页

82 Chapter5. UsingPythononmacOS

### 第89页

CHAPTER
SIX
USING PYTHON ON ANDROID
PythononAndroidisunlikePythonondesktopplatforms. Onadesktopplatform,Pythonisgenerallyinstalledasa
systemresourcethatcanbeusedbyanyuserofthatcomputer. UserstheninteractwithPythonbyrunningapython
executableandenteringcommandsataninteractiveprompt,orbyrunningaPythonscript.
OnAndroid,thereisnoconceptofinstallingasasystemresource. Theonlyunitofsoftwaredistributionisan“app”.
Thereisalsonoconsolewhereyoucouldrunapythonexecutable,orinteractwithaPythonREPL.
Asaresult,theonlywayyoucanusePythononAndroidisinembeddedmode–thatis,bywritinganativeAndroid
application,embeddingaPythoninterpreterusinglibpython,andinvokingPythoncodeusingthePythonembed-
dingAPI.ThefullPythoninterpreter,thestandardlibrary,andallyourPythoncodeisthenpackagedintoyourapp
foritsownprivateuse.
ThePythonstandardlibraryhassomenotableomissionsandrestrictionsonAndroid. SeetheAPIavailabilityguide
fordetails.
6.1 Adding Python to an Android app
Mostappdevelopersshoulduseoneofthefollowingtools,whichwillprovideamucheasierexperience:
• Briefcase,fromtheBeeWareproject
• Buildozer,fromtheKivyproject
• Chaquopy
• pyqtdeploy
• Termux
Ifyou’resureyouwanttodoallofthismanually,readon. Youcanusethetestbedappasaguide;eachstepbelow
containsalinktotherelevantfile.
• First,acquireabuildofPythonforAndroid:
– TheeasiestwayistodownloadanAndroidreleasefrompython.org. Theprefixdirectorymentioned
belowisatthetoplevelofthepackage.
– Or if you want to build it yourself, follow the instructions in Android/README.md. The prefix
directorywillbecreatedundercross-build/HOST.
• Addcodetoyourbuild.gradlefiletocopythefollowingitemsintoyourproject. AllexceptyourownPython
codecanbecopiedfromprefix/lib:
– InyourJNIlibraries:
∗ libpython*.*.so
∗ lib*_python.so(externallibrariessuchasOpenSSL)
– Inyourassets:
∗ python*.*(thePythonstandardlibrary)
∗ python*.*/site-packages(yourownPythoncode)
83

### 第90页

• Addcodetoyourapptoextracttheassetstothefilesystem.
• AddcodetoyourapptostartPythoninembeddedmode. ThiswillneedtobeCcodecalledviaJNI.
6.2 Building a Python package for Android
PythonpackagescanbebuiltforAndroidaswheelsandreleasedonPyPI.Therecommendedtoolfordoingthisis
cibuildwheel,whichautomatesallthedetailsofsettingupacross-compilationenvironment,buildingthewheel,and
testingitonanemulator.
84 Chapter6. UsingPythononAndroid

### 第91页

CHAPTER
SEVEN
USING PYTHON ON IOS
Authors
RussellKeith-Magee(2024-03)
Python on iOS is unlike Python on desktop platforms. On a desktop platform, Python is generally installed as a
systemresourcethatcanbeusedbyanyuserofthatcomputer. UserstheninteractwithPythonbyrunningapython
executableandenteringcommandsataninteractiveprompt,orbyrunningaPythonscript.
On iOS, there is no concept of installing as a system resource. The only unit of software distribution is an “app”.
Thereisalsonoconsolewhereyoucouldrunapythonexecutable,orinteractwithaPythonREPL.
Asaresult,theonlywayyoucanusePythononiOSisinembeddedmode-thatis,bywritinganativeiOSapplication,
andembeddingaPythoninterpreterusinglibPython,andinvokingPythoncodeusingthePythonembeddingAPI.
ThefullPythoninterpreter,thestandardlibrary,andallyourPythoncodeisthenpackagedasastandalonebundle
thatcanbedistributedviatheiOSAppStore.
Ifyou’relookingtoexperimentforthefirsttimewithwritinganiOSappinPython,projectssuchasBeeWareand
Kivywillprovideamuchmoreapproachableuserexperience. Theseprojectsmanagethecomplexitiesassociated
withgettinganiOSprojectrunning,soyouonlyneedtodealwiththePythoncodeitself.
7.1 Python at runtime on iOS
7.1.1 iOS version compatibility
The minimum supported iOS version is specified at compile time, using the --host option to configure. By
default, when compiled for iOS, Python will be compiled with a minimum supported iOS version of 13.0. To
use a different minimum iOS version, provide the version number as part of the --host argument - for exam-
ple,--host=arm64-apple-ios15.4-simulatorwouldcompileanARM64simulatorbuildwithadeployment
targetof15.4.
7.1.2 Platform identification
When executing on iOS, sys.platform will report as ios. This value will be returned on an iPhone or iPad,
regardlessofwhethertheappisrunningonthesimulatororaphysicaldevice.
Informationaboutthespecificruntimeenvironment,includingtheiOSversion,devicemodel,andwhetherthedevice
isasimulator,canbeobtainedusingplatform.ios_ver(). platform.system()willreportiOSoriPadOS,
dependingonthedevice.
os.uname()reportskernel-leveldetails;itwillreportanameofDarwin.
7.1.3 Standard library availability
ThePythonstandardlibraryhassomenotableomissionsandrestrictionsoniOS.SeetheAPIavailabilityguidefor
iOSfordetails.
85

### 第92页

7.1.4 Binary extension modules
One notable difference about iOS as a platform is that App Store distribution imposes hard requirements on the
packagingofanapplication. Oneoftheserequirementsgovernshowbinaryextensionmodulesaredistributed.
TheiOSAppStorerequiresthatallbinarymodulesinaniOSappmustbedynamiclibraries,containedinaframework
withappropriatemetadata,storedintheFrameworksfolderofthepackagedapp. Therecanbeonlyasinglebinary
perframework,andtherecanbenoexecutablebinarymaterialoutsidetheFrameworksfolder.
ThisconflictswiththeusualPythonapproachfordistributingbinaries,whichallowsabinaryextensionmoduletobe
loadedfromanylocationonsys.path. ToensurecompliancewithAppStorepolicies,aniOSprojectmustpost-
processanyPythonpackages,converting.sobinarymodulesintoindividualstandaloneframeworkswithappropriate
metadataandsigning. Fordetailsonhowtoperformthispost-processing,seetheguideforaddingPythontoyour
project.
TohelpPythondiscoverbinariesintheirnewlocation,theoriginal.sofileonsys.pathisreplacedwitha.fwork
file. Thisfileisatextfilecontainingthelocationoftheframeworkbinary,relativetotheappbundle. Toallowthe
framework to resolve back to the original location, the framework must contain a .origin file that contains the
locationofthe.fworkfile,relativetotheappbundle.
Forexample,considerthecaseofanimportfrom foo.bar import _whiz,where_whizisimplementedwith
the binary module sources/foo/bar/_whiz.abi3.so, with sources being the location registered on sys.
path, relative to the application bundle. This module must be distributed as Frameworks/foo.bar._whiz.
framework/foo.bar._whiz (creating the framework name from the full import path of the module), with an
Info.plist file in the .framework directory identifying the binary as a framework. The foo.bar._whiz
module would be represented in the original location with a sources/foo/bar/_whiz.abi3.fwork marker
file, containing the path Frameworks/foo.bar._whiz/foo.bar._whiz. The framework would also contain
Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin,containingthepathtothe.fworkfile.
WhenrunningoniOS,thePythoninterpreterwillinstallanAppleFrameworkLoaderthatisabletoreadandimport
.fworkfiles. Onceimported,the__file__attributeofthebinarymodulewillreportasthelocationofthe.fwork
file. However,theModuleSpecfortheloadedmodulewillreporttheoriginasthelocationofthebinaryinthe
frameworkfolder.
7.1.5 Compiler stub binaries
Xcodedoesn’texposeexplicitcompilersforiOS;instead,itusesanxcrunscriptthatresolvestoafullcompilerpath
(e.g.,xcrun --sdk iphoneos clangtogettheclangforaniPhonedevice). However,usingthisscriptposes
twoproblems:
• Theoutputofxcrunincludespathsthataremachinespecific,resultinginasysconfigmodulethatcannotbe
sharedbetweenusers;and
• ItresultsinCC/CPP/LD/ARdefinitionsthatincludespaces. ThereisalotofCecosystemtoolingthatassumes
thatyoucansplitacommandlineatthefirstspacetogetthepathtothecompilerexecutable;thisisn’tthecase
whenusingxcrun.
Toavoidtheseproblems,Pythonprovidedstubsforthesetools. Thesestubsareshellscriptwrappersaroundtheun-
deringlyxcruntools,distributedinabinfolderdistributedalongsidethecompilediOSframework. Thesescripts
arerelocatable, andwillalwaysresolvetotheappropriatelocalsystempaths. Byincludingthesescriptsinthebin
folderthataccompaniesaframework,thecontentsofthesysconfigmodulebecomesusefulforend-userstocom-
piletheirownmodules. Whencompilingthird-partyPythonmodulesforiOS,youshouldensurethesestubbinaries
areonyourpath.
7.2 Installing Python on iOS
7.2.1 Tools for building iOS apps
BuildingforiOSrequirestheuseofApple’sXcodetooling. Itisstronglyrecommendedthatyouusethemostrecent
stablereleaseofXcode. Thiswillrequiretheuseofthemost(orsecond-most)recentlyreleasedmacOSversion,as
AppledoesnotmaintainXcodeforoldermacOSversions. TheXcodeCommandLineToolsarenotsufficientfor
iOSdevelopment;youneedafullXcodeinstall.
86 Chapter7. UsingPythononiOS

### 第93页

IfyouwanttorunyourcodeontheiOSsimulator,you’llalsoneedtoinstallaniOSSimulatorPlatform. Youshouldbe
promptedtoselectaniOSSimulatorPlatformwhenyoufirstrunXcode. Alternatively,youcanaddaniOSSimulator
PlatformbyselectingfromthePlatformstaboftheXcodeSettingspanel.
7.2.2 Adding Python to an iOS project
PythoncanbeaddedtoanyiOSproject,usingeitherSwiftorObjectiveC.ThefollowingexampleswilluseObjective
C;ifyouareusingSwift,youmayfindalibrarylikePythonKittobehelpful.
ToaddPythontoaniOSXcodeproject:
1. BuildorobtainaPythonXCFramework. SeetheinstructionsinApple/iOS/README.md(intheCPython
source distribution) for details on how to build a Python XCFramework. At a minimum, you will
need a build that supports arm64-apple-ios, plus one of either arm64-apple-ios-simulator or
x86_64-apple-ios-simulator.
2. DragtheXCframeworkintoyouriOSproject. Inthefollowinginstructions,we’llassumeyou’vedroppedthe
XCframeworkintotherootofyourproject;however,youcanuseanyotherlocationthatyouwantbyadjusting
pathsasneeded.
3. AddyourapplicationcodeasafolderinyourXcodeproject. Inthefollowinginstructions,we’llassumethat
yourusercodeisinafoldernamedappintherootofyourproject;youcanuseanyotherlocationbyadjusting
pathsasneeded. Ensurethatthisfolderisassociatedwithyourapptarget.
4. SelecttheapptargetbyselectingtherootnodeofyourXcodeproject,thenthetargetnameinthesidebarthat
appears.
5. In the “General” settings, under “Frameworks, Libraries and Embedded Content”, add Python.
xcframework,with“Embed&Sign”selected.
6. Inthe“BuildSettings”tab,modifythefollowing:
• BuildOptions
– UserScriptSandboxing: No
– EnableTestability: Yes
• SearchPaths
– FrameworkSearchPaths: $(PROJECT_DIR)
– HeaderSearchPaths: "$(BUILT_PRODUCTS_DIR)/Python.framework/Headers"
• AppleClang-Warnings-Alllanguages
– QuotedIncludeInFrameworkHeader: No
7. Add a build step that processes the Python standard library, and your own Python binary dependencies. In
the“BuildPhases”tab,addanew“RunScript”buildstepbeforethe“EmbedFrameworks”step,butafterthe
“CopyBundleResources”step. Namethestep“ProcessPythonlibraries”,disablethe“Basedondependency
analysis”checkbox,andsetthescriptcontentto:
set -e
source $PROJECT_DIR/Python.xcframework/build/build_utils.sh
install_python Python.xcframework app
IfyouhaveplacedyourXCframeworksomewhereotherthantherootofyourproject,modifythepathtothe
firstargument.
8. AddObjectiveCcodetoinitializeanduseaPythoninterpreterinembeddedmode. Youshouldensurethat:
• UTF-8mode(PyPreConfig.utf8_mode)isenabled;
• Bufferedstdio(PyConfig.buffered_stdio)isdisabled;
• Writingbytecode(PyConfig.write_bytecode)isdisabled;
• Signalhandlers(PyConfig.install_signal_handlers)areenabled;
7.2. InstallingPythononiOS 87

### 第94页

• System logging (PyConfig.use_system_logger) is enabled (optional, but strongly recommended;
thisisenabledbydefault);
• PYTHONHOMEfortheinterpreterisconfiguredtopointatthepythonsubfolderofyourapp’sbundle;and
• ThePYTHONPATHfortheinterpreterincludes:
– thepython/lib/python3.Xsubfolderofyourapp’sbundle,
– thepython/lib/python3.X/lib-dynloadsubfolderofyourapp’sbundle,and
– theappsubfolderofyourapp’sbundle
Yourapp’sbundlelocationcanbedeterminedusing[[NSBundle mainBundle] resourcePath].
Steps7and8oftheseinstructionsassumethatyouhaveasinglefolderofpurePythonapplicationcode,namedapp.
Ifyouhavethird-partybinarymodulesinyourapp,someadditionalstepswillberequired:
• Youneedtoensurethatanyfolderscontainingthird-partybinariesareeitherassociatedwiththeapptarget,
or are explicitly copied as part of step 7. Step 7 should also purge any binaries that are not appropriate for
theplatformaspecificbuildistargeting(i.e.,deleteanydevicebinariesifyou’rebuildinganapptargetingthe
simulator).
• Ifyou’reusingaseparatefolderforthird-partypackages,ensurethatfolderisaddedtotheendofthecallto
install_pythoninstep7,andaspartofthePYTHONPATHconfigurationinstep8.
• Ifanyofthefoldersthatcontainthird-partypackageswillcontain.pthfiles,youshouldaddthatfolderasa
sitedirectory(usingsite.addsitedir()),ratherthanaddingtoPYTHONPATHorsys.pathdirectly.
7.2.3 Testing a Python package
TheCPythonsourcetreecontainsatestbedprojectthatisusedtoruntheCPythontestsuiteontheiOSsimulator.
ThistestbedcanalsobeusedasatestbedprojectforrunningyourPythonlibrary’stestsuiteoniOS.
AfterbuildingorobtaininganiOSXCFramework(seeApple/iOS/README.mdfordetails),createacloneofthe
PythoniOStestbedproject. IfyouusedtheApplebuildscripttobuildtheXCframework,youcanrun:
$ python cross-build/iOS/testbed clone --app <path/to/module1> --app <path/to/
,→module2> app-testbed
Or,ifyou’vesourcedyourownXCframework,byrunning:
$ python Apple/testbed clone --platform iOS --framework <path/to/Python.
,→xcframework> --app <path/to/module1> --app <path/to/module2> app-testbed
Anyfoldersspecifiedwiththe--appflagwillbecopiedintotheclonedtestbedproject. Theresultingtestbedwill
becreatedintheapp-testbedfolder. Inthisexample,themodule1andmodule2wouldbeimportablemodules
at runtime. If your project has additional dependencies, they can be installed into the app-testbed/Testbed/
app_packagesfolder(usingpip install --target app-testbed/Testbed/app_packagesorsimilar).
Youcanthenusetheapp-testbedfoldertorunthetestsuiteforyourapp,Forexample,ifmodule1.testswas
theentrypointtoyourtestsuite,youcouldrun:
$ python app-testbed run -- module1.tests
Thisistheequivalentofrunningpython -m module1.testsonadesktopPythonbuild. Anyargumentsafter
the--willbepassedtothetestbedasiftheywereargumentstopython -monadesktopmachine.
YoucanalsoopenthetestbedprojectinXcodebyrunning:
$ open app-testbed/iOSTestbed.xcodeproj
ThiswillallowyoutousethefullXcodesuiteoftoolsfordebugging.
88 Chapter7. UsingPythononiOS

### 第95页

Theargumentsusedtorunthetestsuitearedefinedaspartofthetestplan. Tomodifythetestplan,selectthetest
plannodeoftheprojecttree(itshouldbethefirstchildoftherootnode),andselectthe“Configurations”tab. Modify
the“ArgumentsPassedOnLaunch”valuetochangethetestingarguments.
Thetestplanalsodisablesparalleltesting,andspecifiestheuseoftheTestbed.lldbinitfileforprovidingconfigu-
rationofthedebugger. ThedefaultdebuggerconfigurationdisablesautomaticbreakpointsontheSIGINT,SIGUSR1,
SIGUSR2,andSIGXFSZsignals.
7.3 App Store Compliance
Theonlymechanismfordistributingappstothird-partyiOSdevicesistosubmittheapptotheiOSAppStore;apps
submittedfordistributionmustpassApple’sappreviewprocess. Thisprocessincludesasetofautomatedvalidation
rulesthatinspectthesubmittedapplicationbundleforproblematiccode.
ThePythonstandardlibrarycontainssomecodethatisknowntoviolatetheseautomatedrules. Whiletheseviolations
appear to be false positives, Apple’s review rules cannot be challenged; so, it is necessary to modify the Python
standardlibraryforanapptopassAppStorereview.
The Python source tree contains a patch file that will remove all code that is known to cause issues with the App
Storereviewprocess. ThispatchisappliedautomaticallywhenbuildingforiOS.
7.3. AppStoreCompliance 89

### 第96页

90 Chapter7. UsingPythononiOS

### 第97页

CHAPTER
EIGHT
EDITORS AND IDES
There are a number of IDEs that support Python programming language. Many editors and IDEs provide syntax
highlighting,debuggingtools,andPEP8checks.
8.1 IDLE — Python editor and shell
IDLEisPython’sIntegratedDevelopmentandLearningEnvironmentandisgenerallybundledwithPythoninstalls.
IfyouareonLinuxanddonothaveIDLEinstalledseeInstallingIDLEonLinux. FormoreinformationseetheIDLE
docs.
8.2 Other Editors and IDEs
Python’scommunitywikihasinformationsubmittedbythecommunityonEditorsandIDEs. PleasegotoPython
EditorsandIntegratedDevelopmentEnvironmentsforacomprehensivelist.
91

### 第98页

92 Chapter8. EditorsandIDEs

### 第99页

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
93

### 第100页

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
94 AppendixA. Glossary

### 第101页

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
95

### 第102页

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
96 AppendixA. Glossary

### 第103页

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
97

### 第104页

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
98 AppendixA. Glossary

### 第105页

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
99

### 第106页

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
100 AppendixA. Glossary

### 第107页

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
101

### 第108页

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
102 AppendixA. Glossary

### 第109页

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
103

### 第110页

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
104 AppendixA. Glossary

### 第111页

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
105

### 第112页

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
106 AppendixA. Glossary

### 第113页

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
107

### 第114页

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
108 AppendixA. Glossary

### 第115页

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
109

### 第116页

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
110 AppendixA. Glossary

### 第117页

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
111

### 第118页

112 AppendixB. Aboutthisdocumentation

### 第119页

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
113

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

### 第120页

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
114 AppendixC. HistoryandLicense

### 第121页

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
C.2. TermsandconditionsforaccessingorotherwiseusingPython 115

### 第122页

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
116 AppendixC. HistoryandLicense

### 第123页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 117

### 第124页

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
118 AppendixC. HistoryandLicense

### 第125页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 119

### 第126页

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
120 AppendixC. HistoryandLicense

### 第127页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 121

### 第128页

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
122 AppendixC. HistoryandLicense

### 第129页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 123

### 第130页

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
124 AppendixC. HistoryandLicense

### 第131页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 125

### 第132页

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
126 AppendixC. HistoryandLicense

### 第133页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 127

### 第134页

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
128 AppendixC. HistoryandLicense

### 第135页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 129

### 第136页

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
130 AppendixC. HistoryandLicense

### 第137页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 131

### 第138页

132 AppendixC. HistoryandLicense

### 第139页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
133

### 第140页

134 AppendixD. Copyright

### 第141页

INDEX
Non-alphabetical
command line option,3
...,93
callable,95
ellipsis literal,93
callback,95
CC
-?
command line option,5 command line option,27
>>>,93
C-contiguous,96
__future__,99
CFLAGS,30,40,41
__slots__,107 command line option,27
CFLAGS_NODIST,40,41
A --check-hash-based-pycs
command line option,6
abstract base class,93
class,95
annotate function,93
class variable,95
annotation,93
closure variable,96
argument,93
command line option
asynchronous context manager,94
-?,5
asynchronous generator,94
-B,6
asynchronous generator iterator,94
-b,6
asynchronous iterable,94
BOLT_APPLY_FLAGS,31
asynchronous iterator,94
BOLT_INSTRUMENT_FLAGS,31
attached thread state,94
--build,36
attribute,94
BZIP2_CFLAGS,28
awaitable,95
BZIP2_LIBS,28
B -c,3
CC,27
-B
CFLAGS,27
command line option,6
--check-hash-based-pycs,6
-b
CONFIG_SITE,37
command line option,6
CPP,27
BDFL,95
CPPFLAGS,27
binary file,95
CURSES_CFLAGS,28
BOLT_APPLY_FLAGS
CURSES_LIBS,28
command line option,31
-d,6
BOLT_INSTRUMENT_FLAGS
--disable-gil,26
command line option,31
--disable-ipv6,24
borrowed reference,95
--disable-safety,35
--build
--disable-test-modules,29
command line option,36
-E,6
bytecode,95
--enable-big-digits,24
bytes-like object,95
--enable-bolt,30
BZIP2_CFLAGS
--enable-experimental-jit,27
command line option,28
--enable-framework,35,36
BZIP2_LIBS
--enable-loadable-sqlite-extensions,
command line option,28
24
C --enable-optimizations,30
--enable-profiling,31
-c
135

### 第142页

--enable-pystats,25 --version,5
--enable-shared,33 -W,8
--enable-slower-safety,35 --with-address-sanitizer,33
--enable-universalsdk,35 --with-app-store-compliance,36
--enable-wasm-dynamic-linking,29 --with-assertions,32
--enable-wasm-pthreads,29 --with-build-python,36
--exec-prefix,29 --with-builtin-hashlib-hashes,34
GDBM_CFLAGS,28 --with-computed-gotos,31
GDBM_LIBS,28 --with-dbmliborder,25
-h,5 --with-dtrace,33
--help,5 --with-ensurepip,29
--help-all,5 --with-framework-name,36
--help-env,5 --with-hash-algorithm,34
--help-xoptions,5 --with-libc,34
--host,36 --with-libm,34
HOSTRUNNER,37 --with-libs,33
-I,6 --with-lto,30
-i,6 --with-memory-sanitizer,33
LDFLAGS,27 --with-openssl,34
LIBB2_CFLAGS,28 --with-openssl-rpath,34
LIBB2_LIBS,28 --without-c-locale-coercion,25
LIBEDIT_CFLAGS,28 --without-decimal-contextvar,24
LIBEDIT_LIBS,28 --without-doc-strings,31
LIBFFI_CFLAGS,28 --without-mimalloc,31
LIBFFI_LIBS,28 --without-pymalloc,31
LIBLZMA_CFLAGS,28 --without-readline,34
LIBLZMA_LIBS,28 --without-remote-debug,31
LIBMPDEC_CFLAGS,28 --without-static-libpython,33
LIBMPDEC_LIBS,28 --with-pkg-config,25
LIBREADLINE_CFLAGS,28 --with-platlibdir,25
LIBREADLINE_LIBS,28 --with-pydebug,32
LIBS,27 --with-readline,34
LIBSQLITE3_CFLAGS,28 --with-ssl-default-suites,35
LIBSQLITE3_LIBS,28 --with-strict-overflow,31
LIBUUID_CFLAGS,28 --with-suffix,24
LIBUUID_LIBS,29 --with-system-expat,33
LIBZSTD_CFLAGS,29 --with-system-libmpdec,33
LIBZSTD_LIBS,29 --with-tail-call-interp,31
-m,4 --with-thread-sanitizer,33
MACHDEP,27 --with-trace-refs,32
-O,6 --with-tzpath,24
-OO,6 --with-undefined-behavior-sanitizer,
-P,7 33
PANEL_CFLAGS,29 --with-universal-archs,35
PANEL_LIBS,29 --with-valgrind,33
PKG_CONFIG,27 --with-wheel-pkg-dir,25
PKG_CONFIG_LIBDIR,27 -X,8
PKG_CONFIG_PATH,27 -x,8
--prefix,29 ZLIB_CFLAGS,29
-q,7 ZLIB_LIBS,29
-R,7 complex number,96
-S,7 CONFIG_SITE
-s,7 command line option,37
TCLTK_CFLAGS,29 context,96
TCLTK_LIBS,29 context management protocol,96
-u,7 context manager,96
-V,5 context variable,96
-v,7 contiguous,96
136 Index

### 第143页

coroutine,96 --enable-universalsdk
coroutine function,96 command line option,35
CPP --enable-wasm-dynamic-linking
command line option,27 command line option,29
CPPFLAGS,39,42 --enable-wasm-pthreads
command line option,27 command line option,29
CPython,97 environment variable
current context,97 BASECFLAGS,40
CURSES_CFLAGS BASECPPFLAGS,39
command line option,28 BLDSHARED,42
CURSES_LIBS CC,40
command line option,28 CCSHARED,40
cyclic isolate,97 CFLAGS,30,40,41
CFLAGS_ALIASING,40
D
CFLAGS_NODIST,40,41
-d CFLAGSFORSHARED,40
command line option,6 COMPILEALL_OPTS,40
decorator,97 CONFIGURE_CFLAGS,40
descriptor,97 CONFIGURE_CFLAGS_NODIST,40
dictionary,97 CONFIGURE_CPPFLAGS,39
dictionary comprehension,97 CONFIGURE_LDFLAGS,41
dictionary view,97 CONFIGURE_LDFLAGS_NODIST,41
--disable-gil CPPFLAGS,39,42
command line option,26 CXX,40
--disable-ipv6 EXTRA_CFLAGS,40
command line option,24 LDFLAGS,39,41,42
--disable-safety LDFLAGS_NODIST,41
command line option,35 LDSHARED,42
--disable-test-modules LIBS,42
command line option,29 LINKCC,41
docstring,97 OPT,33,40
duck-typing,98 PATH,11,21,43,44,49,50,52,53,59,61,64,66
dunder,98 PATHEXT,61
PROFILE_TASK,30
E
PURIFY,41
-E
PY_BUILTIN_MODULE_CFLAGS,41
command line option,6 PY_CFLAGS,41
EAFP,98 PY_CFLAGS_NODIST,41
--enable-big-digits
PY_CORE_CFLAGS,41
command line option,24 PY_CORE_LDFLAGS,42
--enable-bolt
PY_CPPFLAGS,39
command line option,30 PY_LDFLAGS,42
--enable-experimental-jit
PY_LDFLAGS_NODIST,42
command line option,27 PY_STDMODULE_CFLAGS,41
--enable-framework
PYTHON_BASIC_REPL,17
command line option,35,36 PYTHON_COLORS,11,16
--enable-loadable-sqlite-extensions
PYTHON_CONTEXT_AWARE_WARNINGS,10,17
command line option,24 PYTHON_CPU_COUNT,10,16
--enable-optimizations
PYTHON_DISABLE_REMOTE_DEBUG,10,16
command line option,30 PYTHON_FROZEN_MODULES,9,16
--enable-profiling
PYTHON_GIL,10,17,100
command line option,31 PYTHON_HISTORY,17
--enable-pystats
PYTHON_JIT,17,27
command line option,25 PYTHON_MANAGER_DEFAULT,44,48,53
--enable-shared
PYTHON_PERF_JIT_SUPPORT,10,16
command line option,33 PYTHON_PRESITE,10,18
--enable-slower-safety
PYTHON_THREAD_INHERIT_CONTEXT,10,17
command line option,35 PYTHON_TLBC,10,17
Index 137

### 第144页

PYTHONASYNCIODEBUG,14 G
PYTHONBREAKPOINT,12
garbage collection,99
PYTHONCASEOK,12
GDBM_CFLAGS
PYTHONCOERCECLOCALE,15,25
command line option,28
PYTHONDEBUG,6,12,32
GDBM_LIBS
PYTHONDEVMODE,9,15
command line option,28
PYTHONDONTWRITEBYTECODE,6,12
generator,99
PYTHONDUMPREFS,17,32
generator expression,100
PYTHONDUMPREFSFILE,17
generator iterator,100
PYTHONEXECUTABLE,13
generic function,100
PYTHONFAULTHANDLER,8,13
generic type,100
PYTHONHASHSEED,7,12
GIL,100
PYTHONHOME,6,11,57,88
global interpreter lock,100
PYTHONINSPECT,6,12
PYTHONINTMAXSTRDIGITS,9,13 H
PYTHONIOENCODING,13,15
-h
PYTHONLEGACYWINDOWSFSENCODING,14
command line option,5
PYTHONLEGACYWINDOWSSTDIO,13,15
hash-based pyc,100
PYTHONMALLOC,14,31
hashable,100
PYTHONMALLOCSTATS,14
--help
PYTHONNODEBUGRANGES,9,16
command line option,5
PYTHONNOUSERSITE,7,13
--help-all
PYTHONOPTIMIZE,6,12
command line option,5
PYTHONPATH,6,11,57,88
--help-env
PYTHONPERFSUPPORT,9,16
command line option,5
PYTHONPLATLIBDIR,11
--help-xoptions
PYTHONPROFILEIMPORTTIME,9,14
command line option,5
PYTHONPYCACHEPREFIX,9,12
--host
PYTHONSAFEPATH,7,11
command line option,36
PYTHONSTARTUP,6,11,12
HOSTRUNNER
PYTHONTRACEMALLOC,9,14
command line option,37
PYTHONUNBUFFERED,7,12
PYTHONUSERBASE,13 I
PYTHONUTF8,9,15,56
-I
PYTHONVERBOSE,8,12
command line option,6
PYTHONWARNDEFAULTENCODING,9,16
-i
PYTHONWARNINGS,8,13
command line option,6
evaluate function,98
IDLE,101
--exec-prefix
immortal,101
command line option,29
immutable,101
expression,98
import path,101
extension module,98
importer,101
F importing,101
interactive,101
f-string,98
interpreted,101
f-strings,98
interpreter shutdown,101
file object,98
iterable,101
file-like object,98
iterator,102
filesystem encoding and error handler,98
finder,99 K
floor division,99
key function,102
Fortran contiguous,96
keyword argument,102
free threading,99
free variable,99 L
function,99
function annotation,99 lambda,102
LBYL,102
LDFLAGS,39,41,42
138 Index

### 第145页

command line option,27 magic,103
LDFLAGS_NODIST,41 special,108
lexical analyzer,102 method resolution order,103
LIBB2_CFLAGS module,103
command line option,28 module spec,103
LIBB2_LIBS MRO,103
command line option,28 mutable,103
LIBEDIT_CFLAGS
N
command line option,28
LIBEDIT_LIBS named tuple,104
command line option,28 namespace,104
LIBFFI_CFLAGS namespace package,104
command line option,28 nested scope,104
LIBFFI_LIBS new-style class,104
command line option,28
O
LIBLZMA_CFLAGS
command line option,28
-O
LIBLZMA_LIBS command line option,6
command line option,28 object,104
LIBMPDEC_CFLAGS
-OO
command line option,28 command line option,6
LIBMPDEC_LIBS OPT,33
command line option,28 optimized scope,104
LIBREADLINE_CFLAGS
command line option,28 P
LIBREADLINE_LIBS
-P
command line option,28
command line option,7
LIBS
package,104
command line option,27
PANEL_CFLAGS
LIBSQLITE3_CFLAGS
command line option,29
command line option,28
PANEL_LIBS
LIBSQLITE3_LIBS
command line option,29
command line option,28
parameter,105
LIBUUID_CFLAGS
PATH,11,21,43,44,49,50,52,53,59,61,64,66
command line option,28
path based finder,105
LIBUUID_LIBS
path entry,105
command line option,29
path entry finder,105
LIBZSTD_CFLAGS
path entry hook,105
command line option,29
path-like object,105
LIBZSTD_LIBS
PATHEXT,61
command line option,29
PEP,105
list,102
PKG_CONFIG
list comprehension,102
command line option,27
loader,102
PKG_CONFIG_LIBDIR
locale encoding,103
command line option,27
M PKG_CONFIG_PATH
command line option,27
-m portion,106
command line option,4 positional argument,106
MACHDEP
--prefix
command line option,27 command line option,29
magic PROFILE_TASK,30
method,103
provisional API,106
magic method,103 provisional package,106
mapping,103
Py_REMOTE_DEBUG(Cmacro),31
meta path finder,103 Python 3000,106
metaclass,103
Python Enhancement Proposals
method,103
PEP 1,106
Index 139

### 第146页

PEP 7,23 PYTHONMALLOC,14,31
PEP 8,91 PYTHONNODEBUGRANGES,9
PEP 11,23,56 PYTHONNOUSERSITE,7
PEP 238,99 PYTHONOPTIMIZE,6
PEP 278,109 PYTHONPATH,6,11,57,88
PEP 302,103 PYTHONPERFSUPPORT,9
PEP 338,4 PYTHONPROFILEIMPORTTIME,9
PEP 343,96 PYTHONPYCACHEPREFIX,9
PEP 362,94,105 PYTHONSAFEPATH,7
PEP 370,7,13 PYTHONSTARTUP,6,12
PEP 397,64 PYTHONTRACEMALLOC,9
PEP 411,106 PYTHONUNBUFFERED,7
PEP 420,104,106 PYTHONUTF8,9,15,56
PEP 443,100 PYTHONVERBOSE,8
PEP 483,100 PYTHONWARNDEFAULTENCODING,9
PEP 484,93,99,100,109,110 PYTHONWARNINGS,8
PEP 488,6,7
Q
PEP 492,9497
PEP 498,98 -q
PEP 514,64 command line option,7
PEP 519,105 qualified name,106
PEP 525,94
R
PEP 526,93,110
PEP 528,56
-R
PEP 529,15,56 command line option,7
PEP 538,15,25 reference count,107
PEP 585,100 regular package,107
PEP 649,93 REPL,107
PEP 683,101
PEP 703,63,78,99,100 S
PEP 768,10,16,31
-S
PEP 3116,109
command line option,7
PEP 3155,106
-s
PYTHON_COLORS,11
command line option,7
PYTHON_CONTEXT_AWARE_WARNINGS,10
sequence,107
PYTHON_CPU_COUNT,10
set comprehension,107
PYTHON_DISABLE_REMOTE_DEBUG,10
single dispatch,107
PYTHON_FROZEN_MODULES,9
slice,107
PYTHON_GIL,10,100
soft deprecated,107
PYTHON_JIT,27
special
PYTHON_MANAGER_DEFAULT,44,53
method,108
PYTHON_PERF_JIT_SUPPORT,10
special method,108
PYTHON_PRESITE,10
standard library,108
PYTHON_THREAD_INHERIT_CONTEXT,10
statement,108
PYTHON_TLBC,10
static type checker,108
PYTHONCOERCECLOCALE,25
stdlib,108
PYTHONDEBUG,6,32
strong reference,108
PYTHONDEVMODE,9
PYTHONDONTWRITEBYTECODE,6 T
PYTHONDUMPREFS,32
t-string,108
PYTHONFAULTHANDLER,8
t-strings,108
PYTHONHASHSEED,7,12
TCLTK_CFLAGS
PYTHONHOME,6,11,57,88
command line option,29
Pythonic,106
TCLTK_LIBS
PYTHONINSPECT,6
command line option,29
PYTHONINTMAXSTRDIGITS,9
text encoding,108
PYTHONIOENCODING,15
text file,108
PYTHONLEGACYWINDOWSSTDIO,13
thread state,108
140 Index

### 第147页

token,109 --with-openssl
triple-quoted string,109 command line option,34
type,109 --with-openssl-rpath
type alias,109 command line option,34
type hint,109 --without-c-locale-coercion
command line option,25
U
--without-decimal-contextvar
-u command line option,24
command line option,7 --without-doc-strings
universal newlines,109 command line option,31
--without-mimalloc
V
command line option,31
-V --without-pymalloc
command line option,5 command line option,31
-v --without-readline
command line option,7 command line option,34
variable annotation,109 --without-remote-debug
--version command line option,31
command line option,5 --without-static-libpython
virtual environment,110 command line option,33
virtual machine,110 --with-pkg-config
command line option,25
W
--with-platlibdir
command line option,25
-W
command line option,8 --with-pydebug
walrus operator,110 command line option,32
--with-readline
--with-address-sanitizer
command line option,33 command line option,34
--with-ssl-default-suites
--with-app-store-compliance
command line option,36 command line option,35
--with-strict-overflow
--with-assertions
command line option,32 command line option,31
--with-suffix
--with-build-python
command line option,36 command line option,24
--with-system-expat
--with-builtin-hashlib-hashes
command line option,34 command line option,33
--with-system-libmpdec
--with-computed-gotos
command line option,31 command line option,33
--with-tail-call-interp
--with-dbmliborder
command line option,25 command line option,31
--with-thread-sanitizer
--with-dtrace
command line option,33 command line option,33
--with-trace-refs
--with-ensurepip
command line option,29 command line option,32
--with-tzpath
--with-framework-name
command line option,36 command line option,24
--with-undefined-behavior-sanitizer
--with-hash-algorithm
command line option,34 command line option,33
--with-universal-archs
--with-libc
command line option,34 command line option,35
--with-valgrind
--with-libm
command line option,34 command line option,33
--with-wheel-pkg-dir
--with-libs
command line option,33 command line option,25
--with-lto
X
command line option,30
--with-memory-sanitizer -X
command line option,33 command line option,8
Index 141

### 第148页

-x
command line option,8
Z
Zen of Python,110
ZLIB_CFLAGS
command line option,29
ZLIB_LIBS
command line option,29
142 Index

