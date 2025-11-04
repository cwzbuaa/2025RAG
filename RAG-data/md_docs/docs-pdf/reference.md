### 第1页

The Python Language Reference
Release 3.14.0rc3
Guido van Rossum and the Python development team
October 01, 2025
Python Software Foundation
Email: docs@python.org

### 第3页

CONTENTS
1 Introduction 3
1.1 AlternateImplementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2.1 LexicalandSyntacticdefinitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 Lexicalanalysis 7
2.1 Linestructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Logicallines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.2 Physicallines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.3 Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.4 Encodingdeclarations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.5 Explicitlinejoining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.6 Implicitlinejoining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.7 Blanklines. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.8 Indentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.9 Whitespacebetweentokens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.1.10 Endmarker . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2 Othertokens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3 Names(identifiersandkeywords) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3.1 Keywords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.3.2 SoftKeywords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.3.3 Reservedclassesofidentifiers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.4 Literals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5 StringandBytesliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5.1 Triple-quotedstrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5.2 Stringprefixes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.5.3 Formalgrammar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.5.4 Escapesequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.5.5 Bytesliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.5.6 Rawstringliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.5.7 f-strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.5.8 t-strings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.6 Numericliterals. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.6.1 Integerliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.6.2 Floating-pointliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.6.3 Imaginaryliterals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.7 Operatorsanddelimiters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3 Datamodel 23
3.1 Objects,valuesandtypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2 Thestandardtypehierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2.1 None. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2.2 NotImplemented . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2.3 Ellipsis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
i

### 第4页

3.2.4 numbers.Number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.2.5 Sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.2.6 Settypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.2.7 Mappings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2.8 Callabletypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.2.9 Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.2.10 Customclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.2.11 Classinstances. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.2.12 I/Oobjects(alsoknownasfileobjects) . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.2.13 Internaltypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.3 Specialmethodnames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.3.1 Basiccustomization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.3.2 Customizingattributeaccess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.3.3 Customizingclasscreation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.3.4 Customizinginstanceandsubclasschecks . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.3.5 Emulatinggenerictypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.3.6 Emulatingcallableobjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.3.7 Emulatingcontainertypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.3.8 Emulatingnumerictypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.3.9 WithStatementContextManagers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.3.10 Customizingpositionalargumentsinclasspatternmatching . . . . . . . . . . . . . . . . 60
3.3.11 Emulatingbuffertypes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.3.12 Annotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.3.13 Specialmethodlookup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.4 Coroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.4.1 AwaitableObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.4.2 CoroutineObjects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.4.3 AsynchronousIterators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
3.4.4 AsynchronousContextManagers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
4 Executionmodel 67
4.1 Structureofaprogram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.2 Namingandbinding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.2.1 Bindingofnames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.2.2 Resolutionofnames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.2.3 Annotationscopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.2.4 Lazyevaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.2.5 Builtinsandrestrictedexecution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.2.6 Interactionwithdynamicfeatures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.3 Exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
5 Theimportsystem 73
5.1 importlib. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.2 Packages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
5.2.1 Regularpackages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.2.2 Namespacepackages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.3 Searching . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.3.1 Themodulecache . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
5.3.2 Findersandloaders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
5.3.3 Importhooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
5.3.4 Themetapath . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
5.4 Loading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
5.4.1 Loaders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
5.4.2 Submodules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.4.3 Modulespecs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.4.4 __path__attributesonmodules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.4.5 Modulereprs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.4.6 Cachedbytecodeinvalidation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
ii

### 第5页

5.5 ThePathBasedFinder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
5.5.1 Pathentryfinders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
5.5.2 Pathentryfinderprotocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5.6 Replacingthestandardimportsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
5.7 PackageRelativeImports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
5.8 Specialconsiderationsfor__main__ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
5.8.1 __main__.__spec__ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
5.9 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6 Expressions 85
6.1 Arithmeticconversions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
6.2 Atoms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
6.2.1 Identifiers(Names) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
6.2.2 Literals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6.2.3 Parenthesizedforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
6.2.4 Displaysforlists,setsanddictionaries. . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
6.2.5 Listdisplays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.2.6 Setdisplays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.2.7 Dictionarydisplays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.2.8 Generatorexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
6.2.9 Yieldexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
6.3 Primaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
6.3.1 Attributereferences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
6.3.2 Subscriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
6.3.3 Slicings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
6.3.4 Calls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
6.4 Awaitexpression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
6.5 Thepoweroperator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
6.6 Unaryarithmeticandbitwiseoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
6.7 Binaryarithmeticoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
6.8 Shiftingoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
6.9 Binarybitwiseoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6.10 Comparisons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6.10.1 Valuecomparisons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6.10.2 Membershiptestoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
6.10.3 Identitycomparisons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
6.11 Booleanoperations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
6.12 Assignmentexpressions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
6.13 Conditionalexpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
6.14 Lambdas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.15 Expressionlists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.16 Evaluationorder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
6.17 Operatorprecedence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
7 Simplestatements 105
7.1 Expressionstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.2 Assignmentstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
7.2.1 Augmentedassignmentstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.2.2 Annotatedassignmentstatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.3 Theassertstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
7.4 Thepassstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7.5 Thedelstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7.6 Thereturnstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7.7 Theyieldstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
7.8 Theraisestatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
7.9 Thebreakstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
7.10 Thecontinuestatement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
7.11 Theimportstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
iii

### 第6页

7.11.1 Futurestatements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7.12 Theglobalstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.13 Thenonlocalstatement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
7.14 Thetypestatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
8 Compoundstatements 117
8.1 Theifstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
8.2 Thewhilestatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
8.3 Theforstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
8.4 Thetrystatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
8.4.1 exceptclause. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
8.4.2 except*clause . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
8.4.3 elseclause . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
8.4.4 finallyclause . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
8.5 Thewithstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
8.6 Thematchstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
8.6.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
8.6.2 Guards . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
8.6.3 IrrefutableCaseBlocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
8.6.4 Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
8.7 Functiondefinitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
8.8 Classdefinitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
8.9 Coroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
8.9.1 Coroutinefunctiondefinition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
8.9.2 Theasync forstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
8.9.3 Theasync withstatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
8.10 Typeparameterlists . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
8.10.1 Genericfunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
8.10.2 Genericclasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
8.10.3 Generictypealiases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
8.11 Annotations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
9 Top-levelcomponents 141
9.1 CompletePythonprograms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.2 Fileinput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.3 Interactiveinput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
9.4 Expressioninput . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
10 FullGrammarspecification 143
A Glossary 161
B Aboutthisdocumentation 179
B.1 ContributorstothePythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
C HistoryandLicense 181
C.1 Historyofthesoftware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
C.2 TermsandconditionsforaccessingorotherwiseusingPython . . . . . . . . . . . . . . . . . . . . 182
C.2.1 PYTHONSOFTWAREFOUNDATIONLICENSEVERSION2 . . . . . . . . . . . . . 182
C.2.2 BEOPEN.COMLICENSEAGREEMENTFORPYTHON2.0 . . . . . . . . . . . . . . 183
C.2.3 CNRILICENSEAGREEMENTFORPYTHON1.6.1 . . . . . . . . . . . . . . . . . . 183
C.2.4 CWILICENSEAGREEMENTFORPYTHON0.9.0THROUGH1.2 . . . . . . . . . . 184
C.2.5 ZERO-CLAUSEBSDLICENSEFORCODEINTHEPYTHONDOCUMENTATION . 185
C.3 LicensesandAcknowledgementsforIncorporatedSoftware . . . . . . . . . . . . . . . . . . . . . 185
C.3.1 MersenneTwister . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
C.3.2 Sockets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
C.3.3 Asynchronoussocketservices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
C.3.4 Cookiemanagement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
C.3.5 Executiontracing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
iv

### 第7页

C.3.6 UUencodeandUUdecodefunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
C.3.7 XMLRemoteProcedureCalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
C.3.8 test_epoll . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
C.3.9 Selectkqueue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
C.3.10 SipHash24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190
C.3.11 strtodanddtoa. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
C.3.12 OpenSSL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
C.3.13 expat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
C.3.14 libffi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
C.3.15 zlib . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
C.3.16 cfuhash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
C.3.17 libmpdec . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
C.3.18 W3CC14Ntestsuite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
C.3.19 mimalloc . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
C.3.20 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
C.3.21 GlobalUnboundedSequences(GUS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 198
C.3.22 Zstandardbindings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
D Copyright 201
Index 203
v

### 第8页

vi

### 第9页

This reference manual describes the syntax and “core semantics” of the language. It is terse, but attempts to be
exactandcomplete. Thesemanticsofnon-essentialbuilt-inobjecttypesandofthebuilt-infunctionsandmodules
are described in library-index. For an informal introduction to the language, see tutorial-index. For C or C++
programmers,twoadditionalmanualsexist:extending-indexdescribesthehigh-levelpictureofhowtowriteaPython
extensionmodule,andthec-api-indexdescribestheinterfacesavailabletoC/C++programmersindetail.
CONTENTS 1

### 第10页

2 CONTENTS

### 第11页

CHAPTER
ONE
INTRODUCTION
ThisreferencemanualdescribesthePythonprogramminglanguage. Itisnotintendedasatutorial.
WhileIamtryingtobeaspreciseaspossible,IchosetouseEnglishratherthanformalspecificationsforeverything
exceptsyntaxandlexicalanalysis. Thisshouldmakethedocumentmoreunderstandabletotheaveragereader,but
will leave room for ambiguities. Consequently, if you were coming from Mars and tried to re-implement Python
fromthisdocumentalone,youmighthavetoguessthingsandinfactyouwouldprobablyendupimplementingquite
adifferentlanguage. Ontheotherhand,ifyouareusingPythonandwonderwhatthepreciserulesaboutaparticular
area of the language are, you should definitely be able to find them here. If you would like to see a more formal
definitionofthelanguage,maybeyoucouldvolunteeryourtime—orinventacloningmachine:-).
Itisdangeroustoaddtoomanyimplementationdetailstoalanguagereferencedocument—theimplementationmay
change,andotherimplementationsofthesamelanguagemayworkdifferently. Ontheotherhand,CPythonisthe
one Python implementation in widespread use (although alternate implementations continue to gain support), and
itsparticularquirksaresometimesworthbeingmentioned,especiallywheretheimplementationimposesadditional
limitations. Therefore,you’llfindshort“implementationnotes”sprinkledthroughoutthetext.
Every Python implementation comes with a number of built-in and standard modules. These are documented in
library-index. Afewbuilt-inmodulesarementionedwhentheyinteractinasignificantwaywiththelanguagedefi-
nition.
1.1 Alternate Implementations
ThoughthereisonePythonimplementationwhichisbyfarthemostpopular,therearesomealternateimplementa-
tionswhichareofparticularinteresttodifferentaudiences.
Knownimplementationsinclude:
CPython
Thisistheoriginalandmost-maintainedimplementationofPython,writteninC.Newlanguagefeaturesgen-
erallyappearherefirst.
Jython
PythonimplementedinJava. ThisimplementationcanbeusedasascriptinglanguageforJavaapplications,
orcanbeusedtocreateapplicationsusingtheJavaclasslibraries. ItisalsooftenusedtocreatetestsforJava
libraries. MoreinformationcanbefoundattheJythonwebsite.
Pythonfor.NET
ThisimplementationactuallyusestheCPythonimplementation,butisamanaged.NETapplicationandmakes
.NETlibrariesavailable. ItwascreatedbyBrianLloyd. Formoreinformation,seethePythonfor.NEThome
page.
IronPython
AnalternatePythonfor.NET.UnlikePython.NET,thisisacompletePythonimplementationthatgenerates
IL,andcompilesPythoncodedirectlyto.NETassemblies. ItwascreatedbyJimHugunin,theoriginalcreator
ofJython. Formoreinformation,seetheIronPythonwebsite.
PyPy
AnimplementationofPythonwrittencompletelyinPython. Itsupportsseveraladvancedfeaturesnotfound
inotherimplementationslikestacklesssupportandaJustinTimecompiler. Oneofthegoalsoftheprojectis
3

### 第12页

toencourageexperimentationwiththelanguageitselfbymakingiteasiertomodifytheinterpreter(sinceitis
writteninPython). AdditionalinformationisavailableonthePyPyproject’shomepage.
Eachoftheseimplementationsvariesinsomewayfromthelanguageasdocumentedinthismanual,orintroducesspe-
cificinformationbeyondwhat’scoveredinthestandardPythondocumentation. Pleaserefertotheimplementation-
specificdocumentationtodeterminewhatelseyouneedtoknowaboutthespecificimplementationyou’reusing.
1.2 Notation
The descriptions of lexical analysis and syntax use a grammar notation that is a mixture of EBNF and PEG. For
example:
name: letter (letter | digit | "_")*
letter: "a"..."z" | "A"..."Z"
digit: "0"..."9"
Inthisexample,thefirstlinesaysthatanameisaletterfollowedbyasequenceofzeroormoreletters,digits,
andunderscores. Aletterinturnisanyofthesinglecharacters'a'through'z'andAthroughZ;adigitisa
singlecharacterfrom0to9.
Eachrulebeginswithaname(whichidentifiestherulethat’sbeingdefined)followedbyacolon,:. Thedefinition
totherightofthecolonusesthefollowingsyntaxelements:
• name: Anamereferstoanotherrule. Wherepossible,itisalinktotherule’sdefinition.
– TOKEN:Anuppercasenamereferstoatoken. Forthepurposesofgrammardefinitions, tokensarethe
sameasrules.
• "text",'text': Textinsingleordoublequotesmustmatchliterally(withoutthequotes). Thetypeofquote
ischosenaccordingtothemeaningoftext:
– 'if': Anameinsinglequotesdenotesakeyword.
– "case": Anameindoublequotesdenotesasoft-keyword.
– '@': Anon-lettersymbolinsinglequotesdenotesanOPtoken,thatis,adelimiteroroperator.
• e1 e2: Itemsseparatedonlybywhitespacedenoteasequence. Here,e1mustbefollowedbye2.
• e1 | e2: Averticalbarisusedtoseparatealternatives. ItdenotesPEG’s“orderedchoice”: ife1matches,
e2isnotconsidered. IntraditionalPEGgrammars,thisiswrittenasaslash,/,ratherthanaverticalbar. See
PEP617formorebackgroundanddetails.
• e*: Astarmeanszeroormorerepetitionsoftheprecedingitem.
• e+: Likewise,aplusmeansoneormorerepetitions.
• [e]: Aphraseenclosedinsquarebracketsmeanszerooroneoccurrences. Inotherwords,theenclosedphrase
isoptional.
• e?: Aquestionmarkhasexactlythesamemeaningassquarebrackets: theprecedingitemisoptional.
• (e): Parenthesesareusedforgrouping.
Thefollowingnotationisonlyusedinlexicaldefinitions.
• "a"..."z": Twoliteralcharactersseparatedbythreedotsmeanachoiceofanysinglecharacterinthegiven
(inclusive)rangeofASCIIcharacters.
• <...>: Aphrasebetweenangularbracketsgivesaninformaldescriptionofthematchedsymbol(forexample,
<any ASCII character except "\">), or an abbreviation that is defined in nearby text (for example,
<Lu>).
Somedefinitionsalsouselookaheads,whichindicatethatanelementmust(ormustnot)matchatagivenposition,
butwithoutconsuminganyinput:
• &e: apositivelookahead(thatis,eisrequiredtomatch)
4 Chapter1. Introduction

### 第13页

• !e: anegativelookahead(thatis,eisrequirednottomatch)
Theunaryoperators(*,+,?)bindastightlyaspossible;theverticalbar(|)bindsmostloosely.
Whitespaceisonlymeaningfultoseparatetokens.
Rulesarenormallycontainedonasingleline,butrulesthataretoolongmaybewrapped:
literal: stringliteral | bytesliteral
| integer | floatnumber | imagnumber
Alternatively, rules may be formatted with the first line ending at the colon, and each alternative beginning with a
verticalbaronanewline. Forexample:
literal:
| stringliteral
| bytesliteral
| integer
| floatnumber
| imagnumber
Thisdoesnotmeanthatthereisanemptyfirstalternative.
1.2.1 Lexical and Syntactic definitions
Thereissomedifferencebetweenlexicalandsyntacticanalysis: thelexicalanalyzeroperatesontheindividualchar-
acters of the input source, while the parser (syntactic analyzer) operates on the stream of tokens generated by the
lexicalanalysis. However,insomecasestheexactboundarybetweenthetwophasesisaCPythonimplementation
detail.
Thepracticaldifferencebetweenthetwoisthatinlexicaldefinitions,allwhitespaceissignificant. Thelexicalanalyzer
discardsallwhitespacethatisnotconvertedtotokensliketoken.INDENTorNEWLINE.Syntactic definitionsthen
usethesetokens,ratherthansourcecharacters.
ThisdocumentationusesthesameBNFgrammarforbothstylesofdefinitions. AllusesofBNFinthenextchapter
(Lexicalanalysis)arelexicaldefinitions;usesinsubsequentchaptersaresyntacticdefinitions.
1.2. Notation 5

### 第14页

6 Chapter1. Introduction

### 第15页

CHAPTER
TWO
LEXICAL ANALYSIS
A Python program is read by a parser. Input to the parser is a stream of tokens, generated by the lexical analyzer
(alsoknownasthetokenizer). Thischapterdescribeshowthelexicalanalyzerbreaksafileintotokens.
PythonreadsprogramtextasUnicodecodepoints;theencodingofasourcefilecanbegivenbyanencodingdec-
larationanddefaultstoUTF-8,seePEP3120fordetails. Ifthesourcefilecannotbedecoded,aSyntaxErroris
raised.
2.1 Line structure
APythonprogramisdividedintoanumberoflogicallines.
2.1.1 Logical lines
The end of a logical line is represented by the token NEWLINE. Statements cannot cross logical line boundaries
exceptwhereNEWLINEisallowedbythesyntax(e.g.,betweenstatementsincompoundstatements). Alogicalline
isconstructedfromoneormorephysicallinesbyfollowingtheexplicitorimplicitlinejoiningrules.
2.1.2 Physical lines
Aphysicallineisasequenceofcharactersterminatedbyonethefollowingend-of-linesequences:
• theUnixformusingASCIILF(linefeed),
• theWindowsformusingtheASCIIsequenceCRLF(returnfollowedbylinefeed),
• the‘ClassicMacOS’formusingtheASCIICR(return)character.
Regardlessofplatform,eachofthesesequencesisreplacedbyasingleASCIILF(linefeed)character. (Thisisdone
eveninsidestringliterals.) Eachlinecanuseanyofthesequences;theydonotneedtobeconsistentwithinafile.
Theendofinputalsoservesasanimplicitterminatorforthefinalphysicalline.
Formally:
newline: <ASCII LF> | <ASCII CR> <ASCII LF> | <ASCII CR>
2.1.3 Comments
A comment starts with a hash character (#) that is not part of a string literal, and ends at the end of the physical
line. Acommentsignifiestheendofthelogicallineunlesstheimplicitlinejoiningrulesareinvoked. Commentsare
ignoredbythesyntax.
2.1.4 Encoding declarations
IfacommentinthefirstorsecondlineofthePythonscriptmatchestheregularexpressioncoding[=:]\s*([-\
w.]+),thiscommentisprocessedasanencodingdeclaration;thefirstgroupofthisexpressionnamestheencoding
ofthesourcecodefile. Theencodingdeclarationmustappearonalineofitsown. Ifitisthesecondline,thefirst
linemustalsobeacomment-onlyline. Therecommendedformsofanencodingexpressionare
7

### 第16页

# -*- coding: <encoding-name> -*-
whichisrecognizedalsobyGNUEmacs,and
# vim:fileencoding=<encoding-name>
whichisrecognizedbyBramMoolenaar’sVIM.
Ifnoencodingdeclarationisfound, thedefaultencodingisUTF-8. Iftheimplicitorexplicitencodingofafileis
UTF-8,aninitialUTF-8byte-ordermark(b'\xef\xbb\xbf')isignoredratherthanbeingasyntaxerror.
Ifanencodingisdeclared,theencodingnamemustberecognizedbyPython(seestandard-encodings). Theencoding
isusedforalllexicalanalysis,includingstringliterals,commentsandidentifiers.
All lexical analysis, including string literals, comments and identifiers, works on Unicode text decoded using the
sourceencoding. AnyUnicodecodepoint,excepttheNULcontrolcharacter,canappearinPythonsource.
source_character: <any Unicode code point, except NUL>
2.1.5 Explicit line joining
Twoormorephysicallinesmaybejoinedintologicallinesusingbackslashcharacters(\),asfollows: whenaphysical
lineendsinabackslashthatisnotpartofastringliteralorcomment,itisjoinedwiththefollowingformingasingle
logicalline,deletingthebackslashandthefollowingend-of-linecharacter. Forexample:
if 1900 < year < 2100 and 1 <= month <= 12 \
and 1 <= day <= 31 and 0 <= hour < 24 \
and 0 <= minute < 60 and 0 <= second < 60: # Looks like a valid date
return 1
Alineendinginabackslashcannotcarryacomment. Abackslashdoesnotcontinueacomment. Abackslashdoes
notcontinueatokenexceptforstringliterals(i.e.,tokensotherthanstringliteralscannotbesplitacrossphysicallines
usingabackslash). Abackslashisillegalelsewhereonalineoutsideastringliteral.
2.1.6 Implicit line joining
Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without
usingbackslashes. Forexample:
month_names = ['Januari', 'Februari', 'Maart', # These are the
'April', 'Mei', 'Juni', # Dutch names
'Juli', 'Augustus', 'September', # for the months
'Oktober', 'November', 'December'] # of the year
Implicitlycontinuedlinescancarrycomments. Theindentationofthecontinuationlinesisnotimportant. Blankcon-
tinuationlinesareallowed. ThereisnoNEWLINEtokenbetweenimplicitcontinuationlines. Implicitlycontinued
linescanalsooccurwithintriple-quotedstrings(seebelow);inthatcasetheycannotcarrycomments.
2.1.7 Blank lines
Alogicallinethatcontainsonlyspaces,tabs,formfeedsandpossiblyacomment,isignored(i.e.,noNEWLINEtoken
isgenerated). Duringinteractiveinputofstatements, handlingofablanklinemaydifferdependingontheimple-
mentationoftheread-eval-printloop. Inthestandardinteractiveinterpreter, anentirelyblanklogicalline(thatis,
onecontainingnotevenwhitespaceoracomment)terminatesamulti-linestatement.
2.1.8 Indentation
Leadingwhitespace(spacesandtabs)atthebeginningofalogicallineisusedtocomputetheindentationlevelof
theline,whichinturnisusedtodeterminethegroupingofstatements.
8 Chapter2. Lexicalanalysis

### 第17页

Tabsarereplaced(fromlefttoright)byonetoeightspacessuchthatthetotalnumberofcharactersuptoandincluding
thereplacementisamultipleofeight(thisisintendedtobethesameruleasusedbyUnix). Thetotalnumberof
spacesprecedingthefirstnon-blankcharacterthendeterminestheline’sindentation. Indentationcannotbesplitover
multiplephysicallinesusingbackslashes;thewhitespaceuptothefirstbackslashdeterminestheindentation.
Indentationisrejectedasinconsistentifasourcefilemixestabsandspacesinawaythatmakesthemeaningdependent
ontheworthofatabinspaces;aTabErrorisraisedinthatcase.
Cross-platformcompatibilitynote: becauseofthenatureoftexteditorsonnon-UNIXplatforms,itisunwiseto
use a mixture of spaces and tabs for the indentation in a single source file. It should also be noted that different
platformsmayexplicitlylimitthemaximumindentationlevel.
Aformfeedcharactermaybepresentatthestartoftheline;itwillbeignoredfortheindentationcalculationsabove.
Formfeedcharactersoccurringelsewhereintheleadingwhitespacehaveanundefinedeffect(forinstance,theymay
resetthespacecounttozero).
TheindentationlevelsofconsecutivelinesareusedtogenerateINDENTandDEDENTtokens,usingastack,asfollows.
Beforethefirstlineofthefileisread,asinglezeroispushedonthestack;thiswillneverbepoppedoffagain. The
numberspushedonthestackwillalwaysbestrictlyincreasingfrombottomtotop. Atthebeginningofeachlogical
line,theline’sindentationleveliscomparedtothetopofthestack. Ifitisequal,nothinghappens. Ifitislarger,itis
pushedonthestack,andoneINDENTtokenisgenerated. Ifitissmaller,itmustbeoneofthenumbersoccurringon
thestack;allnumbersonthestackthatarelargerarepoppedoff,andforeachnumberpoppedoffaDEDENTtokenis
generated. Attheendofthefile,aDEDENTtokenisgeneratedforeachnumberremainingonthestackthatislarger
thanzero.
Hereisanexampleofacorrectly(thoughconfusingly)indentedpieceofPythoncode:
def perm(l):
# Compute the list of all permutations of l
if len(l) <= 1:
return [l]
r = []
for i in range(len(l)):
s = l[:i] + l[i+1:]
p = perm(s)
for x in p:
r.append(l[i:i+1] + x)
return r
Thefollowingexampleshowsvariousindentationerrors:
def perm(l): # error: first line indented
for i in range(len(l)): # error: not indented
s = l[:i] + l[i+1:]
p = perm(l[:i] + l[i+1:]) # error: unexpected indent
for x in p:
r.append(l[i:i+1] + x)
return r # error: inconsistent dedent
(Actually,thefirstthreeerrorsaredetectedbytheparser;onlythelasterrorisfoundbythelexicalanalyzer—the
indentationofreturn rdoesnotmatchalevelpoppedoffthestack.)
2.1.9 Whitespace between tokens
Exceptatthebeginningofalogicallineorinstringliterals,thewhitespacecharactersspace,tabandformfeedcanbe
usedinterchangeablytoseparatetokens. Whitespaceisneededbetweentwotokensonlyiftheirconcatenationcould
otherwisebeinterpretedasadifferenttoken. Forexample,abisonetoken,buta bistwotokens. However,+aand
+ abothproducetwotokens,+anda,as+aisnotavalidtoken.
2.1. Linestructure 9

### 第18页

2.1.10 End marker
Attheendofnon-interactiveinput,thelexicalanalyzergeneratesanENDMARKERtoken.
2.2 Other tokens
BesidesNEWLINE,INDENTandDEDENT,thefollowingcategoriesoftokensexist: identifiersandkeywords(NAME),
literals(suchasNUMBERandSTRING),andothersymbols(operatorsanddelimiters,OP).Whitespacecharacters(other
thanlogicallineterminators,discussedearlier)arenottokens,butservetodelimittokens. Whereambiguityexists,
atokencomprisesthelongestpossiblestringthatformsalegaltoken,whenreadfromlefttoright.
2.3 Names (identifiers and keywords)
NAMEtokensrepresentidentifiers,keywords,andsoftkeywords.
Within the ASCII range (U+0001..U+007F), the valid characters for names include the uppercase and lowercase
letters(A-Zanda-z),theunderscore_and,exceptforthefirstcharacter,thedigits0through9.
Namesmustcontainatleastonecharacter,buthavenoupperlengthlimit. Caseissignificant.
BesidesA-Z,a-z,_and0-9,namescanalsouse“letter-like”and“number-like”charactersfromoutsidetheASCII
range,asdetailedbelow.
AllidentifiersareconvertedintothenormalizationformNFKCwhileparsing;comparisonofidentifiersisbasedon
NFKC.
Formally,thefirstcharacterofanormalizedidentifiermustbelongtothesetid_start,whichistheunionof:
• Unicodecategory<Lu>-uppercaseletters(includesAtoZ)
• Unicodecategory<Ll>-lowercaseletters(includesatoz)
• Unicodecategory<Lt>-titlecaseletters
• Unicodecategory<Lm>-modifierletters
• Unicodecategory<Lo>-otherletters
• Unicodecategory<Nl>-letternumbers
• {"_"}-theunderscore
• <Other_ID_Start>-anexplicitsetofcharactersinPropList.txttosupportbackwardscompatibility
Theremainingcharactersmustbelongtothesetid_continue,whichistheunionof:
• allcharactersinid_start
• Unicodecategory<Nd>-decimalnumbers(includes0to9)
• Unicodecategory<Pc>-connectorpunctuations
• Unicodecategory<Mn>-nonspacingmarks
• Unicodecategory<Mc>-spacingcombiningmarks
• <Other_ID_Continue>-anotherexplicitsetofcharactersinPropList.txttosupportbackwardscompati-
bility
UnicodecategoriesusetheversionoftheUnicodeCharacterDatabaseasincludedintheunicodedatamodule.
ThesesetsarebasedontheUnicodestandardannexUAX-31. SeealsoPEP3131forfurtherdetails.
Evenmoreformally,namesaredescribedbythefollowinglexicaldefinitions:
NAME: xid_start xid_continue*
id_start: <Lu> | <Ll> | <Lt> | <Lm> | <Lo> | <Nl> | "_" | <Other_ID_Start>
id_continue: id_start | <Nd> | <Pc> | <Mn> | <Mc> | <Other_ID_Continue>
xid_start: <all characters in id_start whose NFKC normalization is
10 Chapter2. Lexicalanalysis

### 第19页

in (id_start xid_continue*)">
xid_continue: <all characters in id_continue whose NFKC normalization is
in (id_continue*)">
identifier: <NAME, except keywords>
Anon-normativelistingofallvalididentifiercharactersasdefinedbyUnicodeisavailableintheDerivedCoreProp-
erties.txtfileintheUnicodeCharacterDatabase.
2.3.1 Keywords
The following names are used as reserved words, or keywords of the language, and cannot be used as ordinary
identifiers. Theymustbespelledexactlyaswrittenhere:
False await else import pass
None break except in raise
True class finally is return
and continue for lambda try
as def from nonlocal while
assert del global not with
async elif if or yield
2.3.2 Soft Keywords
Addedinversion3.10.
Somenamesareonlyreservedunderspecificcontexts. Theseareknownassoftkeywords:
• match,case,and_,whenusedinthematchstatement.
• type,whenusedinthetypestatement.
Thesesyntacticallyactaskeywordsintheirspecificcontexts,butthisdistinctionisdoneattheparserlevel,notwhen
tokenizing.
As soft keywords, their use in the grammar is possible while still preserving compatibility with existing code that
usesthesenamesasidentifiernames.
Changedinversion3.12: typeisnowasoftkeyword.
2.3.3 Reserved classes of identifiers
Certainclassesofidentifiers(besideskeywords)havespecialmeanings. Theseclassesareidentifiedbythepatterns
ofleadingandtrailingunderscorecharacters:
_*
Notimportedbyfrom module import *.
_
Inacasepatternwithinamatchstatement,_isasoftkeywordthatdenotesawildcard.
Separately,theinteractiveinterpretermakestheresultofthelastevaluationavailableinthevariable_. (Itis
storedinthebuiltinsmodule,alongsidebuilt-infunctionslikeprint.)
Elsewhere,_isaregularidentifier. Itisoftenusedtoname“special”items,butitisnotspecialtoPythonitself.
(cid:174) Note
The name _ is often used in conjunction with internationalization; refer to the documentation for the
gettextmoduleformoreinformationonthisconvention.
Itisalsocommonlyusedforunusedvariables.
2.3. Names(identifiersandkeywords) 11

### 第20页

__*__
System-definednames,informallyknownas“dunder”names. Thesenamesaredefinedbytheinterpreterand
itsimplementation(includingthestandardlibrary). CurrentsystemnamesarediscussedintheSpecialmethod
names section and elsewhere. More will likely be defined in future versions of Python. Any use of __*__
names,inanycontext,thatdoesnotfollowexplicitlydocumenteduse,issubjecttobreakagewithoutwarning.
__*
Class-privatenames. Namesinthiscategory,whenusedwithinthecontextofaclassdefinition,arere-written
touseamangledformtohelpavoidnameclashesbetween“private”attributesofbaseandderivedclasses. See
sectionIdentifiers(Names).
2.4 Literals
Literalsarenotationsforconstantvaluesofsomebuilt-intypes.
Intermsoflexicalanalysis,Pythonhasstring,bytesandnumericliterals.
Other“literals”arelexicallydenotedusingkeywords(None,True,False)andthespecialellipsistoken(...).
2.5 String and Bytes literals
Stringliteralsaretextenclosedinsinglequotes(')ordoublequotes("). Forexample:
"spam"
'eggs'
Thequoteusedtostarttheliteralalsoterminatesit,soastringliteralcanonlycontaintheotherquote(exceptwith
escapesequences,seebelow). Forexample:
'Say "Hello", please.'
"Don't do that!"
Exceptforthislimitation,thechoiceofquotecharacter('or")doesnotaffecthowtheliteralisparsed.
Insideastringliteral,thebackslash(\)characterintroducesanescapesequence,whichhasspecialmeaningdepending
onthecharacterafterthebackslash. Forexample,\"denotesthedoublequotecharacter,anddoesnotendthestring:
>>> print("Say \"Hello\" to everyone!")
Say "Hello" to everyone!
Seeescapesequencesbelowforafulllistofsuchsequences,andmoredetails.
2.5.1 Triple-quoted strings
Stringscanalsobeenclosedinmatchinggroupsofthreesingleordoublequotes. Thesearegenerallyreferredtoas
triple-quotedstrings:
"""This is a triple-quoted string."""
Intriple-quotedliterals,unescapedquotesareallowed(andareretained),exceptthatthreeunescapedquotesinarow
terminatetheliteral,iftheyareofthesamekind('or")usedatthestart:
"""This string has "quotes" inside."""
Unescapednewlinesarealsoallowedandretained:
'''This triple-quoted string
continues on the next line.'''
12 Chapter2. Lexicalanalysis

### 第21页

2.5.2 String prefixes
Stringliteralscanhaveanoptionalprefixthatinfluenceshowthecontentoftheliteralisparsed,forexample:
b"data"
f'{result=}'
Theallowedprefixesare:
• b: Bytesliteral
• r: Rawstring
• f: Formattedstringliteral(“f-string”)
• t: Templatestringliteral(“t-string”)
• u: Noeffect(allowedforbackwardscompatibility)
Seethelinkedsectionsfordetailsoneachtype.
Prefixesarecase-insensitive(forexample,‘B’worksthesameas‘b’). The‘r’prefixcanbecombinedwith‘f’,‘t’or
‘b’,so‘fr’,‘rf’,‘tr’,‘rt’,‘br’,and‘rb’arealsovalidprefixes.
Addedinversion3.3: The'rb'prefixofrawbytesliteralshasbeenaddedasasynonymof'br'.
Supportfortheunicodelegacyliteral(u'value')wasreintroducedtosimplifythemaintenanceofdualPython2.x
and3.xcodebases. SeePEP414formoreinformation.
2.5.3 Formal grammar
Stringliterals,except“f-strings” and“t-strings”,aredescribedbythefollowinglexicaldefinitions.
Thesedefinitionsusenegativelookaheads(!)toindicatethatanendingquoteendstheliteral.
STRING: [stringprefix] (stringcontent)
stringprefix: <("r" | "u" | "b" | "br" | "rb"), case-insensitive>
stringcontent:
| "'''" ( !"'''" longstringitem)* "'''"
| '"""' ( !'"""' longstringitem)* '"""'
| "'" ( !"'" stringitem)* "'"
| '"' ( !'"' stringitem)* '"'
stringitem: stringchar | stringescapeseq
stringchar: <any source_character, except backslash and newline>
longstringitem: stringitem | newline
stringescapeseq: "\" <any source_character>
Notethatasinalllexicaldefinitions,whitespaceissignificant. Inparticular,theprefix(ifany)mustbeimmediately
followedbythestartingquote.
2.5.4 Escape sequences
Unlessan‘r’or‘R’prefixispresent,escapesequencesinstringandbytesliteralsareinterpretedaccordingtorules
similartothoseusedbyStandardC.Therecognizedescapesequencesare:
2.5. StringandBytesliterals 13

### 第22页

EscapeSequence Meaning
\<newline> Ignoredendofline
\\ Backslash
\' Singlequote
\" Doublequote
\a ASCIIBell(BEL)
\b ASCIIBackspace(BS)
\f ASCIIFormfeed(FF)
\n ASCIILinefeed(LF)
\r ASCIICarriageReturn(CR)
\t ASCIIHorizontalTab(TAB)
\v ASCIIVerticalTab(VT)
\ooo Octalcharacter
\xhh Hexadecimalcharacter
\N{name} NamedUnicodecharacter
\uxxxx HexadecimalUnicodecharacter
\Uxxxxxxxx HexadecimalUnicodecharacter
Ignoredendofline
Abackslashcanbeaddedattheendofalinetoignorethenewline:
>>> 'This string will not include \
... backslashes or newline characters.'
'This string will not include backslashes or newline characters.'
Thesameresultcanbeachievedusingtriple-quotedstrings,orparenthesesandstringliteralconcatenation.
Escapedcharacters
To include a backslash in a non-raw Python string literal, it must be doubled. The \\ escape sequence denotes a
singlebackslashcharacter:
>>> print('C:\\Program Files')
C:\Program Files
Similarly,the\'and\"sequencesdenotethesingleanddoublequotecharacter,respectively:
>>> print('\' and \"')
' and "
Octalcharacter
Thesequence\ooodenotesacharacterwiththeoctal(base8)valueooo:
>>> '\120'
'P'
Uptothreeoctaldigits(0through7)areaccepted.
Inabytesliteral,charactermeansabytewiththegivenvalue. Inastringliteral,itmeansaUnicodecharacterwith
thegivenvalue.
Changedinversion3.11: Octalescapeswithvaluelargerthan0o377(255)produceaDeprecationWarning.
Changedinversion3.12: Octalescapeswithvaluelargerthan0o377(255)produceaSyntaxWarning. Inafuture
PythonversiontheywillraiseaSyntaxError.
14 Chapter2. Lexicalanalysis

| EscapeSequence | Meaning |
| --- | --- |
| \<newline> | Ignoredendofline |
| \\ | Backslash |
| \' | Singlequote |
| \" | Doublequote |
| \a | ASCIIBell(BEL) |
| \b | ASCIIBackspace(BS) |
| \f | ASCIIFormfeed(FF) |
| \n | ASCIILinefeed(LF) |
| \r | ASCIICarriageReturn(CR) |
| \t | ASCIIHorizontalTab(TAB) |
| \v | ASCIIVerticalTab(VT) |
| \ooo | Octalcharacter |
| \xhh | Hexadecimalcharacter |
| \N{name} | NamedUnicodecharacter |
| \uxxxx | HexadecimalUnicodecharacter |
| \Uxxxxxxxx | HexadecimalUnicodecharacter |

### 第23页

Hexadecimalcharacter
Thesequence\xhhdenotesacharacterwiththehex(base16)valuehh:
>>> '\x50'
'P'
UnlikeinStandardC,exactlytwohexdigitsarerequired.
Inabytesliteral,charactermeansabytewiththegivenvalue. Inastringliteral,itmeansaUnicodecharacterwith
thegivenvalue.
NamedUnicodecharacter
Thesequence\N{name}denotesaUnicodecharacterwiththegivenname:
>>> '\N{LATIN CAPITAL LETTER P}'
'P'
>>> '\N{SNAKE}'
'(cid:0)'
Thissequencecannotappearinbytesliterals.
Changedinversion3.3: Supportfornamealiaseshasbeenadded.
HexadecimalUnicodecharacters
Thesesequences\uxxxxand\UxxxxxxxxdenotetheUnicodecharacterwiththegivenhex(base16)value. Exactly
fourdigitsarerequiredfor\u;exactlyeightdigitsarerequiredfor\U.ThelattercanencodeanyUnicodecharacter.
>>> '\u1234'
'(cid:0)'
>>> '\U0001f40d'
'(cid:0)'
Thesesequencescannotappearinbytesliterals.
Unrecognizedescapesequences
UnlikeinStandardC,allunrecognizedescapesequencesareleftinthestringunchanged,thatis,thebackslashisleft
intheresult:
>>> print('\q')
\q
>>> list('\q')
['\\', 'q']
Notethatforbytesliterals,theescapesequencesonlyrecognizedinstringliterals(\N...,\u...,\U...)fallinto
thecategoryofunrecognizedescapes.
Changedinversion3.6: UnrecognizedescapesequencesproduceaDeprecationWarning.
Changedinversion3.12: UnrecognizedescapesequencesproduceaSyntaxWarning. InafuturePythonversion
theywillraiseaSyntaxError.
2.5.5 Bytes literals
Bytesliteralsarealwaysprefixedwith‘b’or‘B’;theyproduceaninstanceofthebytestypeinsteadofthestrtype.
TheymayonlycontainASCIIcharacters;byteswithanumericvalueof128orgreatermustbeexpressedwithescape
sequences(typicallyHexadecimalcharacterorOctalcharacter):
2.5. StringandBytesliterals 15

### 第24页

>>> b'\x89PNG\r\n\x1a\n'
b'\x89PNG\r\n\x1a\n'
>>> list(b'\x89PNG\r\n\x1a\n')
[137, 80, 78, 71, 13, 10, 26, 10]
Similarly,azerobytemustbeexpressedusinganescapesequence(typically\0or\x00).
2.5.6 Raw string literals
Bothstringandbytesliteralsmayoptionallybeprefixedwithaletter‘r’or‘R’;suchconstructsarecalledrawstring
literalsandrawbytesliteralsrespectivelyandtreatbackslashesasliteralcharacters. Asaresult,inrawstringliterals,
escapesequencesarenottreatedspecially:
>>> r'\d{4}-\d{2}-\d{2}'
'\\d{4}-\\d{2}-\\d{2}'
Eveninarawliteral,quotescanbeescapedwithabackslash,butthebackslashremainsintheresult;forexample,
r"\""isavalidstringliteralconsistingoftwocharacters: abackslashandadoublequote;r"\"isnotavalidstring
literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw literal cannot end in a
singlebackslash(sincethebackslashwouldescapethefollowingquotecharacter). Notealsothatasinglebackslash
followedbyanewlineisinterpretedasthosetwocharactersaspartoftheliteral,notasalinecontinuation.
2.5.7 f-strings
Addedinversion3.6.
Aformattedstringliteralorf-stringisastringliteralthatisprefixedwith‘f’or‘F’.Thesestringsmaycontainreplace-
mentfields, whichareexpressionsdelimitedbycurlybraces{}. Whileotherstringliteralsalwayshaveaconstant
value,formattedstringsarereallyexpressionsevaluatedatruntime.
Escapesequencesaredecodedlikeinordinarystringliterals(exceptwhenaliteralisalsomarkedasarawstring).
Afterdecoding,thegrammarforthecontentsofthestringis:
f_string: (literal_char | "{{" | "}}" | replacement_field)*
replacement_field: "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression: (conditional_expression | "*" or_expr)
("," conditional_expression | "," "*" or_expr)* [","]
| yield_expression
conversion: "s" | "r" | "a"
format_spec: (literal_char | replacement_field)*
literal_char: <any code point except "{", "}" or NULL>
Thepartsofthestringoutsidecurlybracesaretreatedliterally,exceptthatanydoubledcurlybraces'{{'or'}}'
arereplacedwiththecorrespondingsinglecurlybrace. Asingleopeningcurlybracket'{'marksareplacementfield,
whichstartswithaPythonexpression. Todisplayboththeexpressiontextanditsvalueafterevaluation,(usefulin
debugging),anequalsign'='maybeaddedaftertheexpression. Aconversionfield,introducedbyanexclamation
point'!'mayfollow. Aformatspecifiermayalsobeappended, introducedbyacolon':'. Areplacementfield
endswithaclosingcurlybracket'}'.
ExpressionsinformattedstringliteralsaretreatedlikeregularPythonexpressionssurroundedbyparentheses,with
a few exceptions. An empty expression is not allowed, and both lambda and assignment expressions := must be
surrounded by explicit parentheses. Each expression is evaluated in the context where the formatted string literal
appears,inorderfromlefttoright. Replacementexpressionscancontainnewlinesinbothsingle-quotedandtriple-
quoted f-strings and they can contain comments. Everything that comes after a # inside a replacement field is a
comment(evenclosingbracesandquotes). Inthatcase,replacementfieldsmustbeclosedinadifferentline.
>>> f"abc{a # This is a comment }"
... + 3}"
'abc5'
16 Chapter2. Lexicalanalysis

### 第25页

Changedinversion3.7: PriortoPython3.7,anawaitexpressionandcomprehensionscontaininganasync for
clausewereillegalintheexpressionsinformattedstringliteralsduetoaproblemwiththeimplementation.
Changedinversion3.12: PriortoPython3.12,commentswerenotallowedinsidef-stringreplacementfields.
When the equal sign '=' is provided, the output will have the expression text, the '=' and the evaluated value.
Spacesaftertheopeningbrace'{',withintheexpressionandafterthe'='areallretainedintheoutput. Bydefault,
the'='causestherepr()oftheexpressiontobeprovided, unlessthereisaformatspecified. Whenaformatis
specifieditdefaultstothestr()oftheexpressionunlessaconversion'!r'isdeclared.
Addedinversion3.8: Theequalsign'='.
Ifaconversionisspecified,theresultofevaluatingtheexpressionisconvertedbeforeformatting. Conversion'!s'
callsstr()ontheresult,'!r'callsrepr(),and'!a'callsascii().
The result is then formatted using the format() protocol. The format specifier is passed to the __format__()
methodoftheexpressionorconversionresult. Anemptystringispassedwhentheformatspecifierisomitted. The
formattedresultisthenincludedinthefinalvalueofthewholestring.
Top-levelformatspecifiersmayincludenestedreplacementfields. Thesenestedfieldsmayincludetheirowncon-
versionfieldsandformatspecifiers,butmaynotincludemoredeeplynestedreplacementfields. Theformatspecifier
mini-languageisthesameasthatusedbythestr.format()method.
Formattedstringliteralsmaybeconcatenated,butreplacementfieldscannotbesplitacrossliterals.
Someexamplesofformattedstringliterals:
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}." # repr() is equivalent to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}" # nested fields
'result: 12.35'
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}" # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}" # using integer format specifier
'0x400'
>>> foo = "bar"
>>> f"{ foo = }" # preserves whitespace
" foo = 'bar'"
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" '
Reusingtheouterf-stringquotingtypeinsideareplacementfieldispermitted:
>>> a = dict(x=2)
>>> f"abc {a["x"]} def"
'abc 2 def'
2.5. StringandBytesliterals 17

### 第26页

Changedinversion3.12: PriortoPython3.12,reuseofthesamequotingtypeoftheouterf-stringinsideareplace-
mentfieldwasnotpossible.
Backslashesarealsoallowedinreplacementfieldsandareevaluatedthesamewayasinanyothercontext:
>>> a = ["a", "b", "c"]
>>> print(f"List a contains:\n{"\n".join(a)}")
List a contains:
a
b
c
Changedinversion3.12: PriortoPython3.12,backslasheswerenotpermittedinsideanf-stringreplacementfield.
Formattedstringliteralscannotbeusedasdocstrings,eveniftheydonotincludeexpressions.
>>> def foo():
... f"Not a docstring"
...
>>> foo.__doc__ is None
True
See also PEP 498 for the proposal that added formatted string literals, and str.format(), which uses a related
formatstringmechanism.
2.5.8 t-strings
Addedinversion3.14.
Atemplatestringliteralort-stringisastringliteralthatisprefixedwith‘t’or‘T’.Thesestringsfollowthesamesyntax
andevaluationrulesasformattedstringliterals,withthefollowingdifferences:
• Rather than evaluating to a str object, template string literals evaluate to a string.templatelib.
Templateobject.
• The format() protocol is not used. Instead, the format specifier and conversions (if any) are passed to a
newInterpolationobjectthatiscreatedforeachevaluatedexpression. Itisuptocodethatprocessesthe
resultingTemplateobjecttodecidehowtohandleformatspecifiersandconversions.
• Format specifiers containing nested replacement fields are evaluated eagerly, prior to being passed to the
Interpolationobject. Forinstance,aninterpolationoftheform{amount:.{precision}f}willevalu-
atetheinnerexpression{precision}todeterminethevalueoftheformat_specattribute. Ifprecision
weretobe2,theresultingformatspecifierwouldbe'.2f'.
• Whentheequalssign'='isprovidedinaninterpolationexpression, thetextoftheexpressionisappended
totheliteralstringthatprecedestherelevantinterpolation. Thisincludestheequalssignandanysurround-
ing whitespace. The Interpolation instance for the expression will be created as normal, except that
conversionwillbesetto‘r’(repr())bydefault. Ifanexplicitconversionorformatspecifierareprovided,
thiswilloverridethedefaultbehaviour.
2.6 Numeric literals
NUMBER tokens represent numeric literals, of which there are three types: integers, floating-point numbers, and
imaginarynumbers.
NUMBER: integer | floatnumber | imagnumber
Thenumericvalueofanumericliteralisthesameasifitwerepassedasastringtotheint,floatorcomplex
classconstructor,respectively. Notethatnotallvalidinputsforthoseconstructorsarealsovalidliterals.
Numericliteralsdonotincludeasign;aphraselike-1isactuallyanexpressioncomposedoftheunaryoperator‘-’
andtheliteral1.
18 Chapter2. Lexicalanalysis

### 第27页

2.6.1 Integer literals
Integerliteralsdenotewholenumbers. Forexample:
7
3
2147483647
Thereisnolimitforthelengthofintegerliteralsapartfromwhatcanbestoredinavailablememory:
7922816251426433759354395033679228162514264337593543950336
Underscorescanbeusedtogroupdigitsforenhancedreadability,andareignoredfordeterminingthenumericvalue
oftheliteral. Forexample,thefollowingliteralsareequivalent:
100_000_000_000
100000000000
1_00_00_00_00_000
Underscorescanonlyoccurbetweendigits. Forexample,_123,321_,and123__321arenotvalidliterals.
Integerscanbespecifiedinbinary(base2),octal(base8),orhexadecimal(base16)usingtheprefixes0b,0oand
0x,respectively. Hexadecimaldigits10through15arerepresentedbylettersA-F,case-insensitive. Forexample:
0b100110111
0b_1110_0101
0o177
0o377
0xdeadbeef
0xDead_Beef
Anunderscorecanfollowthebasespecifier. Forexample,0x_1fisavalidliteral,but0_x1fand0x__1farenot.
Leadingzerosinanon-zerodecimalnumberarenotallowed. Forexample, 0123isnotavalidliteral. Thisisfor
disambiguationwithC-styleoctalliterals,whichPythonusedbeforeversion3.0.
Formally,integerliteralsaredescribedbythefollowinglexicaldefinitions:
integer: decinteger | bininteger | octinteger | hexinteger | zerointeger
decinteger: nonzerodigit (["_"] digit)*
bininteger: "0" ("b" | "B") (["_"] bindigit)+
octinteger: "0" ("o" | "O") (["_"] octdigit)+
hexinteger: "0" ("x" | "X") (["_"] hexdigit)+
zerointeger: "0"+ (["_"] "0")*
nonzerodigit: "1"..."9"
digit: "0"..."9"
bindigit: "0" | "1"
octdigit: "0"..."7"
hexdigit: digit | "a"..."f" | "A"..."F"
Changedinversion3.6: Underscoresarenowallowedforgroupingpurposesinliterals.
2.6.2 Floating-point literals
Floating-point(float)literals,suchas3.14or1.5,denoteapproximationsofrealnumbers.
Theyconsistofinteger andfractionparts, eachcomposedofdecimaldigits. Thepartsareseparatedbyadecimal
point,.:
2.71828
4.0
2.6. Numericliterals 19

### 第28页

Unlikeinintegerliterals,leadingzerosareallowedinthenumericparts. Forexample,077.010islegal,anddenotes
thesamenumberas77.10.
Asinintegerliterals,singleunderscoresmayoccurbetweendigitstohelpreadability:
96_485.332_123
3.14_15_93
Eitheroftheseparts,butnotboth,canbeempty. Forexample:
10. # (equivalent to 10.0)
.001 # (equivalent to 0.001)
Optionally,theintegerandfractionmaybefollowedbyanexponent: thelettereorE,followedbyanoptionalsign,
+or-,andanumberinthesameformatastheintegerandfractionparts. TheeorErepresents“timestenraisedto
thepowerof”:
1.0e3 # (represents 1.0×10³, or 1000.0)
1.166e-5 # (represents 1.166×10⁻⁵, or 0.00001166)
6.02214076e+23 # (represents 6.02214076×10²³, or 602214076000000000000000.)
Infloatswithonlyintegerandexponentparts,thedecimalpointmaybeomitted:
1e3 # (equivalent to 1.e3 and 1.0e3)
0e0 # (equivalent to 0.)
Formally,floating-pointliteralsaredescribedbythefollowinglexicaldefinitions:
floatnumber:
| digitpart "." [digitpart] [exponent]
| "." digitpart [exponent]
| digitpart exponent
digitpart: digit (["_"] digit)*
exponent: ("e" | "E") ["+" | "-"] digitpart
Changedinversion3.6: Underscoresarenowallowedforgroupingpurposesinliterals.
2.6.3 Imaginary literals
Pythonhascomplexnumberobjects, butnocomplexliterals. Instead, imaginaryliterals denotecomplexnumbers
withazerorealpart.
Forexample,inmath,thecomplexnumber3+4.2iiswrittenastherealnumber3addedtotheimaginarynumber
4.2i. Pythonusesasimilarsyntax,excepttheimaginaryunitiswrittenasjratherthani:
3+4.2j
Thisisanexpressioncomposedoftheintegerliteral3,theoperator‘+’,andtheimaginaryliteral4.2j. Sincethese
arethreeseparatetokens,whitespaceisallowedbetweenthem:
3 + 4.2j
Nowhitespaceisallowedwithineachtoken. Inparticular,thejsuffix,maynotbeseparatedfromthenumberbefore
it.
The number before the j has the same syntax as a floating-point literal. Thus, the following are valid imaginary
literals:
4.2j
3.14j
10.j
(continuesonnextpage)
20 Chapter2. Lexicalanalysis

### 第29页

(continuedfrompreviouspage)
.001j
1e100j
3.14e-10j
3.14_15_93j
Unlikeinafloating-pointliteralthedecimalpointcanbeomittediftheimaginarynumberonlyhasanintegerpart.
Thenumberisstillevaluatedasafloating-pointnumber,notaninteger:
10j
0j
1000000000000000000000000j # equivalent to 1e+24j
Thejsuffixiscase-insensitive. ThatmeansyoucanuseJinstead:
3.14J # equivalent to 3.14j
Formally,imaginaryliteralsaredescribedbythefollowinglexicaldefinition:
imagnumber: (floatnumber | digitpart) ("j" | "J")
2.7 Operators and delimiters
Thefollowinggrammardefinesoperatoranddelimitertokens,thatis,thegenericOPtokentype. Alistofthesetokens
andtheirnamesisalsoavailableinthetokenmoduledocumentation.
OP:
| assignment_operator
| bitwise_operator
| comparison_operator
| enclosing_delimiter
| other_delimiter
| arithmetic_operator
| "..."
| other_op
assignment_operator: "+=" | "-=" | "*=" | "**=" | "/=" | "//=" | "%=" |
"&=" | "|=" | "^=" | "<<=" | ">>=" | "@=" | ":="
bitwise_operator: "&" | "|" | "^" | "~" | "<<" | ">>"
comparison_operator: "<=" | ">=" | "<" | ">" | "==" | "!="
enclosing_delimiter: "(" | ")" | "[" | "]" | "{" | "}"
other_delimiter: "," | ":" | "!" | ";" | "=" | "->"
arithmetic_operator: "+" | "-" | "**" | "*" | "//" | "/" | "%"
other_op: "." | "@"
(cid:174) Note
Generally,operatorsareusedtocombineexpressions,whiledelimitersserveotherpurposes. However,thereisno
clear,formaldistinctionbetweenthetwocategories.
Sometokenscanserveaseitheroperatorsordelimiters, dependingonusage. Forexample, *isboththemul-
tiplicationoperatorandadelimiterusedforsequenceunpacking,and@isboththematrixmultiplicationanda
delimiterthatintroducesdecorators.
Forsometokens,thedistinctionisunclear. Forexample,somepeopleconsider.,(,and)tobedelimiters,while
othersseethegetattr()operatorandthefunctioncalloperator(s).
Some of Python’s operators, like and, or, and not in, use keyword tokens rather than “symbols” (operator
tokens).
2.7. Operatorsanddelimiters 21

### 第30页

Asequenceofthreeconsecutiveperiods(...)hasaspecialmeaningasanEllipsisliteral.
22 Chapter2. Lexicalanalysis

### 第31页

CHAPTER
THREE
DATA MODEL
3.1 Objects, values and types
Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations
betweenobjects. (Inasense,andinconformancetoVonNeumann’smodelofa“storedprogramcomputer”,codeis
alsorepresentedbyobjects.)
Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you
maythinkofitastheobject’saddressinmemory. Theisoperatorcomparestheidentityoftwoobjects;theid()
functionreturnsanintegerrepresentingitsidentity.
CPythonimplementationdetail: ForCPython,id(x)isthememoryaddresswherexisstored.
Anobject’stypedeterminestheoperationsthattheobjectsupports(e.g.,“doesithavealength?”) andalsodefines
thepossiblevaluesforobjectsofthattype. Thetype()functionreturnsanobject’stype(whichisanobjectitself).
Likeitsidentity,anobject’stypeisalsounchangeable.1
Thevalueofsomeobjectscanchange. Objectswhosevaluecanchangearesaidtobemutable;objectswhosevalueis
unchangeableoncetheyarecreatedarecalledimmutable. (Thevalueofanimmutablecontainerobjectthatcontains
areferencetoamutableobjectcanchangewhenthelatter’svalueischanged;howeverthecontainerisstillconsidered
immutable,becausethecollectionofobjectsitcontainscannotbechanged. So,immutabilityisnotstrictlythesame
ashavinganunchangeablevalue, itismoresubtle.) Anobject’smutabilityisdeterminedbyitstype; forinstance,
numbers,stringsandtuplesareimmutable,whiledictionariesandlistsaremutable.
Objectsareneverexplicitlydestroyed;however,whentheybecomeunreachabletheymaybegarbage-collected. An
implementationisallowedtopostponegarbagecollectionoromititaltogether—itisamatterofimplementation
qualityhowgarbagecollectionisimplemented,aslongasnoobjectsarecollectedthatarestillreachable.
CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed
detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not
guaranteedtocollectgarbagecontainingcircularreferences. Seethedocumentationofthegcmoduleforinformation
oncontrollingthecollectionofcyclicgarbage. OtherimplementationsactdifferentlyandCPythonmaychange. Do
not depend on immediate finalization of objects when they become unreachable (so you should always close files
explicitly).
Notethattheuseoftheimplementation’stracingordebuggingfacilitiesmaykeepobjectsalivethatwouldnormally
becollectable. Alsonotethatcatchinganexceptionwithatry…exceptstatementmaykeepobjectsalive.
Some objects contain references to “external” resources such as open files or windows. It is understood that these
resourcesarefreedwhentheobjectisgarbage-collected,butsincegarbagecollectionisnotguaranteedtohappen,
such objects also provide an explicit way to release the external resource, usually a close() method. Programs
arestronglyrecommendedtoexplicitlyclosesuchobjects. Thetry…finallystatementandthewithstatement
provideconvenientwaystodothis.
Someobjectscontainreferencestootherobjects;thesearecalledcontainers. Examplesofcontainersaretuples,lists
and dictionaries. The references are part of a container’s value. In most cases, when we talk about the value of a
container,weimplythevalues,nottheidentitiesofthecontainedobjects;however,whenwetalkaboutthemutability
1Itispossibleinsomecasestochangeanobject’stype,undercertaincontrolledconditions.Itgenerallyisn’tagoodideathough,sinceitcan
leadtosomeverystrangebehaviourifitishandledincorrectly.
23

### 第32页

ofacontainer,onlytheidentitiesoftheimmediatelycontainedobjectsareimplied. So,ifanimmutablecontainer
(likeatuple)containsareferencetoamutableobject,itsvaluechangesifthatmutableobjectischanged.
Typesaffectalmostallaspectsofobjectbehavior. Eventheimportanceofobjectidentityisaffectedinsomesense:
forimmutabletypes,operationsthatcomputenewvaluesmayactuallyreturnareferencetoanyexistingobjectwith
thesametypeandvalue,whileformutableobjectsthisisnotallowed. Forexample,aftera = 1; b = 1,aandb
mayormaynotrefertothesameobjectwiththevalueone,dependingontheimplementation. Thisisbecauseint
isanimmutabletype,sothereferenceto1canbereused. Thisbehaviourdependsontheimplementationused,so
shouldnotbereliedupon,butissomethingtobeawareofwhenmakinguseofobjectidentitytests. However,after
c = []; d = [],canddareguaranteedtorefertotwodifferent,unique,newlycreatedemptylists. (Notethate
= f = []assignsthesameobjecttobotheandf.)
3.2 The standard type hierarchy
Below is a list of the types that are built into Python. Extension modules (written in C, Java, or other languages,
dependingontheimplementation)candefineadditionaltypes. FutureversionsofPythonmayaddtypestothetype
hierarchy (e.g., rational numbers, efficiently stored arrays of integers, etc.), although such additions will often be
providedviathestandardlibraryinstead.
Someofthetypedescriptionsbelowcontainaparagraphlisting‘specialattributes.’ Theseareattributesthatprovide
accesstotheimplementationandarenotintendedforgeneraluse. Theirdefinitionmaychangeinthefuture.
3.2.1 None
This type has a single value. There is a single object with this value. This object is accessed through the built-in
name None. It is used to signify the absence of a value in many situations, e.g., it is returned from functions that
don’texplicitlyreturnanything. Itstruthvalueisfalse.
3.2.2 NotImplemented
This type has a single value. There is a single object with this value. This object is accessed through the built-in
nameNotImplemented. Numericmethodsandrichcomparisonmethodsshouldreturnthisvalueiftheydonot
implementtheoperationfortheoperandsprovided. (Theinterpreterwillthentrythereflectedoperation, orsome
otherfallback,dependingontheoperator.) Itshouldnotbeevaluatedinabooleancontext.
Seeimplementing-the-arithmetic-operationsformoredetails.
Changedinversion3.9: EvaluatingNotImplementedinabooleancontextwasdeprecated.
Changedinversion3.14: EvaluatingNotImplementedinabooleancontextnowraisesaTypeError. Itpreviously
evaluatedtoTrueandemittedaDeprecationWarningsincePython3.9.
3.2.3 Ellipsis
Thistypehasasinglevalue. Thereisasingleobjectwiththisvalue. Thisobjectisaccessedthroughtheliteral...
orthebuilt-innameEllipsis. Itstruthvalueistrue.
3.2.4 numbers.Number
Thesearecreatedbynumericliteralsandreturnedasresultsbyarithmeticoperatorsandarithmeticbuilt-infunctions.
Numeric objects are immutable; once created their value never changes. Python numbers are of course strongly
relatedtomathematicalnumbers,butsubjecttothelimitationsofnumericalrepresentationincomputers.
Thestringrepresentationsofthenumericclasses,computedby__repr__()and__str__(),havethefollowing
properties:
• They are valid numeric literals which, when passed to their class constructor, produce an object having the
valueoftheoriginalnumeric.
• Therepresentationisinbase10,whenpossible.
• Leadingzeros,possiblyexceptingasinglezerobeforeadecimalpoint,arenotshown.
24 Chapter3. Datamodel

### 第33页

• Trailingzeros,possiblyexceptingasinglezeroafteradecimalpoint,arenotshown.
• Asignisshownonlywhenthenumberisnegative.
Pythondistinguishesbetweenintegers,floating-pointnumbers,andcomplexnumbers:
numbers.Integral
Theserepresentelementsfromthemathematicalsetofintegers(positiveandnegative).
(cid:174) Note
The rules for integer representation are intended to give the most meaningful interpretation of shift and mask
operationsinvolvingnegativeintegers.
Therearetwotypesofintegers:
Integers(int)
Theserepresentnumbersinanunlimitedrange,subjecttoavailable(virtual)memoryonly. Forthepurpose
ofshiftandmaskoperations, abinaryrepresentationisassumed, andnegativenumbersarerepresentedina
variantof2’scomplementwhichgivestheillusionofaninfinitestringofsignbitsextendingtotheleft.
Booleans(bool)
TheserepresentthetruthvaluesFalseandTrue. ThetwoobjectsrepresentingthevaluesFalseandTrueare
theonlyBooleanobjects. TheBooleantypeisasubtypeoftheintegertype,andBooleanvaluesbehavelike
thevalues0and1,respectively,inalmostallcontexts,theexceptionbeingthatwhenconvertedtoastring,the
strings"False"or"True"arereturned,respectively.
numbers.Real(float)
These represent machine-level double precision floating-point numbers. You are at the mercy of the underlying
machinearchitecture(andCorJavaimplementation)fortheacceptedrangeandhandlingofoverflow. Pythondoes
notsupportsingle-precisionfloating-pointnumbers;thesavingsinprocessorandmemoryusagethatareusuallythe
reasonforusingthesearedwarfedbytheoverheadofusingobjectsinPython,sothereisnoreasontocomplicatethe
languagewithtwokindsoffloating-pointnumbers.
numbers.Complex(complex)
These represent complex numbers as a pair of machine-level double precision floating-point numbers. The same
caveatsapplyasforfloating-pointnumbers. Therealandimaginarypartsofacomplexnumberzcanberetrieved
throughtheread-onlyattributesz.realandz.imag.
3.2.5 Sequences
Theserepresentfiniteorderedsetsindexedbynon-negativenumbers. Thebuilt-infunctionlen()returnsthenumber
ofitemsofasequence. Whenthelengthofasequenceisn,theindexsetcontainsthenumbers0,1,…,n-1. Item
iofsequenceaisselectedbya[i]. Somesequences,includingbuilt-insequences,interpretnegativesubscriptsby
addingthesequencelength. Forexample,a[-2]equalsa[n-2],thesecondtolastitemofsequenceawithlength
n.
Sequencesalsosupportslicing:a[i:j]selectsallitemswithindexksuchthati<=k<j. Whenusedasanexpression,
a slice is a sequence of the same type. The comment above about negative indexes also applies to negative slice
positions.
Somesequencesalsosupport“extendedslicing”withathird“step”parameter: a[i:j:k]selectsallitemsofawith
indexxwherex = i + n*k,n>=0andi<=x<j.
Sequencesaredistinguishedaccordingtotheirmutability:
3.2. Thestandardtypehierarchy 25

### 第34页

Immutablesequences
An object of an immutable sequence type cannot change once it is created. (If the object contains references to
otherobjects,theseotherobjectsmaybemutableandmaybechanged; however,thecollectionofobjectsdirectly
referencedbyanimmutableobjectcannotchange.)
Thefollowingtypesareimmutablesequences:
Strings
AstringisasequenceofvaluesthatrepresentUnicodecodepoints. AllthecodepointsintherangeU+0000
- U+10FFFFcanberepresentedinastring. Pythondoesn’thaveachartype;instead,everycodepointinthe
stringisrepresentedasastringobjectwithlength1. Thebuilt-infunctionord()convertsacodepointfrom
itsstringformtoanintegerintherange0 - 10FFFF;chr()convertsanintegerintherange0 - 10FFFF
tothecorrespondinglength1stringobject. str.encode()canbeusedtoconvertastrtobytesusingthe
giventextencoding,andbytes.decode()canbeusedtoachievetheopposite.
Tuples
TheitemsofatuplearearbitraryPythonobjects. Tuplesoftwoormoreitemsareformedbycomma-separated
listsofexpressions. Atupleofoneitem(a‘singleton’)canbeformedbyaffixingacommatoanexpression(an
expressionbyitselfdoesnotcreateatuple,sinceparenthesesmustbeusableforgroupingofexpressions). An
emptytuplecanbeformedbyanemptypairofparentheses.
Bytes
Abytesobjectisanimmutablearray. Theitemsare8-bitbytes,representedbyintegersintherange0<=x
<256. Bytesliterals(likeb'abc')andthebuilt-inbytes()constructorcanbeusedtocreatebytesobjects.
Also,bytesobjectscanbedecodedtostringsviathedecode()method.
Mutablesequences
Mutablesequencescanbechangedaftertheyarecreated. Thesubscriptionandslicingnotationscanbeusedasthe
targetofassignmentanddel(delete)statements.
(cid:174) Note
Thecollectionsandarraymoduleprovideadditionalexamplesofmutablesequencetypes.
Therearecurrentlytwointrinsicmutablesequencetypes:
Lists
TheitemsofalistarearbitraryPythonobjects. Listsareformedbyplacingacomma-separatedlistofexpres-
sionsinsquarebrackets. (Notethattherearenospecialcasesneededtoformlistsoflength0or1.)
ByteArrays
Abytearrayobjectisamutablearray. Theyarecreatedbythebuilt-inbytearray()constructor. Asidefrom
beingmutable(andhenceunhashable),bytearraysotherwiseprovidethesameinterfaceandfunctionalityas
immutablebytesobjects.
3.2.6 Set types
Theserepresentunordered, finitesetsofunique, immutableobjects. Assuch, theycannotbeindexedbyanysub-
script. However, they can be iterated over, and the built-in function len() returns the number of items in a set.
Commonusesforsetsarefastmembershiptesting,removingduplicatesfromasequence,andcomputingmathemat-
icaloperationssuchasintersection,union,difference,andsymmetricdifference.
Forsetelements,thesameimmutabilityrulesapplyasfordictionarykeys. Notethatnumerictypesobeythenormal
rulesfornumericcomparison: iftwonumberscompareequal(e.g.,1and1.0),onlyoneofthemcanbecontained
inaset.
Therearecurrentlytwointrinsicsettypes:
26 Chapter3. Datamodel

### 第35页

Sets
Theserepresentamutableset. Theyarecreatedbythebuilt-inset()constructorandcanbemodifiedafter-
wardsbyseveralmethods,suchasadd.
Frozensets
Theserepresentanimmutableset. Theyarecreatedbythebuilt-infrozenset()constructor. Asafrozenset
isimmutableandhashable,itcanbeusedagainasanelementofanotherset,orasadictionarykey.
3.2.7 Mappings
Theserepresentfinitesetsofobjectsindexedbyarbitraryindexsets. Thesubscriptnotationa[k]selectstheitem
indexedbykfromthemappinga;thiscanbeusedinexpressionsandasthetargetofassignmentsordelstatements.
Thebuilt-infunctionlen()returnsthenumberofitemsinamapping.
Thereiscurrentlyasingleintrinsicmappingtype:
Dictionaries
These represent finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable
askeysarevaluescontaininglistsordictionariesorothermutabletypesthatarecomparedbyvalueratherthanby
objectidentity,thereasonbeingthattheefficientimplementationofdictionariesrequiresakey’shashvaluetoremain
constant. Numerictypesusedforkeysobeythenormalrulesfornumericcomparison: iftwonumberscompareequal
(e.g.,1and1.0)thentheycanbeusedinterchangeablytoindexthesamedictionaryentry.
Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added se-
quentially over the dictionary. Replacing an existing key does not change the order, however removing a key and
re-insertingitwilladdittotheendinsteadofkeepingitsoldplace.
Dictionariesaremutable;theycanbecreatedbythe{}notation(seesectionDictionarydisplays).
The extension modules dbm.ndbm and dbm.gnu provide additional examples of mapping types, as does the
collectionsmodule.
Changedinversion3.7: DictionariesdidnotpreserveinsertionorderinversionsofPythonbefore3.6. InCPython
3.6,insertionorderwaspreserved,butitwasconsideredanimplementationdetailatthattimeratherthanalanguage
guarantee.
3.2.8 Callable types
Thesearethetypestowhichthefunctioncalloperation(seesectionCalls)canbeapplied:
User-definedfunctions
Auser-definedfunctionobjectiscreatedbyafunctiondefinition(seesectionFunctiondefinitions). Itshouldbecalled
withanargumentlistcontainingthesamenumberofitemsasthefunction’sformalparameterlist.
Specialread-onlyattributes
Attribute Meaning
A reference to the dictionary that holds the func-
function.__globals__ tion’s global variables – the global namespace of the
moduleinwhichthefunctionwasdefined.
Noneoratupleofcellsthatcontainbindingsforthe
function.__closure__ names specified in the co_freevars attribute of the
function’scode object.
Acellobjecthastheattributecell_contents. This
can be used to get the value of the cell, as well as set
thevalue.
3.2. Thestandardtypehierarchy 27

| Attribute | Meaning |
| --- | --- |
| function.__globals__ | A reference to the dictionary that holds the func-
tion’s global variables – the global namespace of the
moduleinwhichthefunctionwasdefined. |
| function.__closure__ | Noneoratupleofcellsthatcontainbindingsforthe
names specified in the co_freevars attribute of the
function’scode object.
Acellobjecthastheattributecell_contents. This
can be used to get the value of the cell, as well as set
thevalue. |

### 第36页

Specialwritableattributes
Mostoftheseattributescheckthetypeoftheassignedvalue:
Attribute Meaning
The function’s documentation string, or None if un-
function.__doc__ available.
The function’s name. See also: __name__
function.__name__ attributes.
The function’s qualified name. See also:
function.__qualname__ __qualname__ attributes.
Addedinversion3.3.
Thenameofthemodulethefunctionwasdefinedin,or
function.__module__ Noneifunavailable.
Atuplecontainingdefaultparametervaluesforthose
function.__defaults__ parametersthathavedefaults,orNoneifnoparameters
haveadefaultvalue.
The code object representing the compiled function
function.__code__ body.
Thenamespacesupportingarbitraryfunctionattributes.
function.__dict__ Seealso: __dict__ attributes.
Adictionarycontainingannotationsofparameters.
function.__annotations__ Thekeysofthedictionaryaretheparameternames,and
'return'forthereturnannotation, ifprovided. See
also: object.__annotations__.
Changed in version 3.14: Annotations are now lazily
evaluated. SeePEP649.
The annotate function for this function, or None
function.__annotate__ if the function has no annotations. See object.
__annotate__.
Addedinversion3.14.
A dictionary containing defaults for keyword-only
function.__kwdefaults__ parameters.
A tuple containing the type parameters of a generic
function.__type_params__ function.
Addedinversion3.12.
Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach
metadatatofunctions. Regularattributedot-notationisusedtogetandsetsuchattributes.
CPython implementation detail: CPython’s current implementation only supports function attributes on user-
definedfunctions. Functionattributesonbuilt-infunctionsmaybesupportedinthefuture.
Additionalinformationaboutafunction’sdefinitioncanberetrievedfromitscodeobject(accessibleviathe__code__
attribute).
Instancemethods
Aninstancemethodobjectcombinesaclass,aclassinstanceandanycallableobject(normallyauser-definedfunc-
tion).
Specialread-onlyattributes:
28 Chapter3. Datamodel

| Attribute | Meaning |
| --- | --- |
| function.__doc__ | The function’s documentation string, or None if un-
available. |
| function.__name__ | The function’s name. See also: __name__
attributes. |
| function.__qualname__ | The function’s qualified name. See also:
__qualname__ attributes.
Addedinversion3.3. |
| function.__module__ | Thenameofthemodulethefunctionwasdefinedin,or
Noneifunavailable. |
| function.__defaults__ | Atuplecontainingdefaultparametervaluesforthose
parametersthathavedefaults,orNoneifnoparameters
haveadefaultvalue. |
| function.__code__ | The code object representing the compiled function
body. |
| function.__dict__ | Thenamespacesupportingarbitraryfunctionattributes.
Seealso: __dict__ attributes. |
| function.__annotations__ | Adictionarycontainingannotationsofparameters.
Thekeysofthedictionaryaretheparameternames,and
'return'forthereturnannotation, ifprovided. See
also: object.__annotations__.
Changed in version 3.14: Annotations are now lazily
evaluated. SeePEP649. |
| function.__annotate__ | The annotate function for this function, or None
if the function has no annotations. See object.
__annotate__.
Addedinversion3.14. |
| function.__kwdefaults__ | A dictionary containing defaults for keyword-only
parameters. |
| function.__type_params__ | A tuple containing the type parameters of a generic
function.
Addedinversion3.12. |

### 第37页

Referstotheclassinstanceobjecttowhichthemethod
method.__self__ isbound
Referstotheoriginalfunctionobject
method.__func__
The method’s documentation (same as method.
method.__doc__ __func__.__doc__). Astringiftheoriginalfunc-
tionhadadocstring,elseNone.
The name of the method (same as method.
method.__name__ __func__.__name__)
Thenameofthemodulethemethodwasdefinedin,or
method.__module__ Noneifunavailable.
Methodsalsosupportaccessing(butnotsetting)thearbitraryfunctionattributesontheunderlyingfunctionobject.
User-defined method objects may be created when getting an attribute of a class (perhaps via an instance of that
class),ifthatattributeisauser-definedfunctionobjectoraclassmethodobject.
When an instance method object is created by retrieving a user-defined function object from a class via one of its
instances, its __self__ attribute is the instance, and the method object is said to be bound. The new method’s
__func__attributeistheoriginalfunctionobject.
When an instance method object is created by retrieving a classmethod object from a class or instance, its
__self__attributeistheclassitself,andits__func__attributeisthefunctionobjectunderlyingtheclassmethod.
Whenaninstancemethodobjectiscalled,theunderlyingfunction(__func__)iscalled,insertingtheclassinstance
(__self__)infrontoftheargumentlist. Forinstance,whenCisaclasswhichcontainsadefinitionforafunction
f(),andxisaninstanceofC,callingx.f(1)isequivalenttocallingC.f(x, 1).
Whenaninstancemethodobjectisderivedfromaclassmethodobject,the“classinstance”storedin__self__
willactuallybetheclassitself,sothatcallingeitherx.f(1)orC.f(1)isequivalenttocallingf(C,1)wherefis
theunderlyingfunction.
Itisimportanttonotethatuser-definedfunctionswhichareattributesofaclassinstancearenotconvertedtobound
methods;thisonlyhappenswhenthefunctionisanattributeoftheclass.
Generatorfunctions
Afunctionormethodwhichusestheyieldstatement(seesectionTheyieldstatement)iscalledageneratorfunction.
Suchafunction,whencalled,alwaysreturnsaniteratorobjectwhichcanbeusedtoexecutethebodyofthefunction:
calling the iterator’s iterator.__next__() method will cause the function to execute until it provides a value
usingtheyieldstatement. Whenthefunctionexecutesareturnstatementorfallsofftheend,aStopIteration
exceptionisraisedandtheiteratorwillhavereachedtheendofthesetofvaluestobereturned.
Coroutinefunctions
Afunctionormethodwhichisdefinedusingasync defiscalledacoroutinefunction. Suchafunction,whencalled,
returnsacoroutineobject. Itmaycontainawaitexpressions,aswellasasync withandasync forstatements.
SeealsotheCoroutineObjectssection.
Asynchronousgeneratorfunctions
A function or method which is defined using async def and which uses the yield statement is called a asyn-
chronous generator function. Such a function, when called, returns an asynchronous iterator object which can be
usedinanasync forstatementtoexecutethebodyofthefunction.
Callingtheasynchronousiterator’saiterator.__anext__methodwillreturnanawaitablewhichwhenawaited
will execute until it provides a value using the yield expression. When the function executes an empty return
3.2. Thestandardtypehierarchy 29

| method.__self__ | Referstotheclassinstanceobjecttowhichthemethod
isbound |
| --- | --- |
| method.__func__ | Referstotheoriginalfunctionobject |
| method.__doc__ | The method’s documentation (same as method.
__func__.__doc__). Astringiftheoriginalfunc-
tionhadadocstring,elseNone. |
| method.__name__ | The name of the method (same as method.
__func__.__name__) |
| method.__module__ | Thenameofthemodulethemethodwasdefinedin,or
Noneifunavailable. |

### 第38页

statementorfallsofftheend,aStopAsyncIterationexceptionisraisedandtheasynchronousiteratorwillhave
reachedtheendofthesetofvaluestobeyielded.
Built-infunctions
Abuilt-infunctionobjectisawrapperaroundaCfunction. Examplesofbuilt-infunctionsarelen()andmath.
sin()(mathisastandardbuilt-inmodule). ThenumberandtypeoftheargumentsaredeterminedbytheCfunction.
Specialread-onlyattributes:
• __doc__isthefunction’sdocumentationstring,orNoneifunavailable. Seefunction.__doc__.
• __name__isthefunction’sname. Seefunction.__name__.
• __self__issettoNone(butseethenextitem).
• __module__isthenameofthemodulethefunctionwasdefinedinorNoneifunavailable. Seefunction.
__module__.
Built-inmethods
Thisisreallyadifferentdisguiseofabuilt-infunction,thistimecontaininganobjectpassedtotheCfunctionasan
implicitextraargument. Anexampleofabuilt-inmethodisalist.append(),assumingalist isalistobject. In
thiscase,thespecialread-onlyattribute__self__issettotheobjectdenotedbyalist. (Theattributehasthesame
semanticsasitdoeswithother instance methods.)
Classes
Classes are callable. These objects normally act as factories for new instances of themselves, but variations are
possibleforclasstypesthatoverride__new__(). Theargumentsofthecallarepassedto__new__()and,inthe
typicalcase,to__init__()toinitializethenewinstance.
ClassInstances
Instancesofarbitraryclassescanbemadecallablebydefininga__call__()methodintheirclass.
3.2.9 Modules
ModulesareabasicorganizationalunitofPythoncode,andarecreatedbytheimportsystemasinvokedeitherbythe
importstatement,orbycallingfunctionssuchasimportlib.import_module()andbuilt-in__import__().
Amoduleobjecthasanamespaceimplementedbyadictionaryobject(thisisthedictionaryreferencedbythe
__globals__attributeoffunctionsdefinedinthemodule). Attributereferencesaretranslatedtolookupsinthis
dictionary,e.g.,m.xisequivalenttom.__dict__["x"]. Amoduleobjectdoesnotcontainthecodeobjectusedto
initializethemodule(sinceitisn’tneededoncetheinitializationisdone).
Attributeassignmentupdatesthemodule’snamespacedictionary,e.g.,m.x = 1isequivalenttom.__dict__["x"]
= 1.
Import-relatedattributesonmoduleobjects
Module objects have the following attributes that relate to the import system. When a module is created using the
machinery associated with the import system, these attributes are filled in based on the module’s spec, before the
loaderexecutesandloadsthemodule.
Tocreateamoduledynamicallyratherthanusingtheimportsystem,it’srecommendedtouseimportlib.util.
module_from_spec(),whichwillsetthevariousimport-controlledattributestoappropriatevalues. It’salsopos-
sibletousethetypes.ModuleTypeconstructortocreatemodulesdirectly,butthistechniqueismoreerror-prone,
asmostattributesmustbemanuallysetonthemoduleobjectafterithasbeencreatedwhenusingthisapproach.
30 Chapter3. Datamodel

### 第39页

(cid:1002) Caution
With the exception of __name__, it is strongly recommended that you rely on __spec__ and its attributes
instead of any of the other individual attributes listed in this subsection. Note that updating an attribute on
__spec__willnotupdatethecorrespondingattributeonthemoduleitself:
>>> import typing
>>> typing.__name__, typing.__spec__.name
('typing', 'typing')
>>> typing.__spec__.name = 'spelling'
>>> typing.__name__, typing.__spec__.name
('typing', 'spelling')
>>> typing.__name__ = 'keyboard_smashing'
>>> typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling')
module.__name__
Thenameusedtouniquelyidentifythemoduleintheimportsystem. Foradirectlyexecutedmodule,thiswill
besetto"__main__".
This attribute must be set to the fully qualified name of the module. It is expected to match the value of
module.__spec__.name.
module.__spec__
Arecordofthemodule’simport-system-relatedstate.
Settothemodule specthatwasusedwhenimportingthemodule. SeeModulespecsformoredetails.
Addedinversion3.4.
module.__package__
Thepackageamodulebelongsto.
If the module is top-level (that is, not a part of any specific package) then the attribute should be set to ''
(theemptystring). Otherwise, itshouldbesettothenameofthemodule’spackage(whichcanbeequalto
module.__name__ifthemoduleitselfisapackage). SeePEP366forfurtherdetails.
Thisattributeisusedinsteadof__name__tocalculateexplicitrelativeimportsformainmodules. Itdefaultsto
Noneformodulescreateddynamicallyusingthetypes.ModuleTypeconstructor;useimportlib.util.
module_from_spec()insteadtoensuretheattributeissettoastr.
Itisstronglyrecommendedthatyouusemodule.__spec__.parentinsteadofmodule.__package__.
__package__isnowonlyusedasafallbackif__spec__.parentisnotset,andthisfallbackpathisdep-
recated.
Changedinversion3.4:ThisattributenowdefaultstoNoneformodulescreateddynamicallyusingthetypes.
ModuleTypeconstructor. Previouslytheattributewasoptional.
Changed in version 3.6: The value of __package__ is expected to be the same as __spec__.parent.
__package__isnowonlyusedasafallbackduringimportresolutionif__spec__.parentisnotdefined.
Changed in version 3.10: ImportWarning is raised if an import resolution falls back to __package__
insteadof__spec__.parent.
Changed in version 3.12: Raise DeprecationWarning instead of ImportWarning when falling back to
__package__duringimportresolution.
Deprecatedsinceversion3.13,willberemovedinversion3.15: __package__willceasetobesetortaken
intoconsiderationbytheimportsystemorstandardlibrary.
module.__loader__
Theloaderobjectthattheimportmachineryusedtoloadthemodule.
3.2. Thestandardtypehierarchy 31

|  |
| --- |
| (cid:1002) Caution |
| With the exception of __name__, it is strongly recommended that you rely on __spec__ and its attributes
instead of any of the other individual attributes listed in this subsection. Note that updating an attribute on
__spec__willnotupdatethecorrespondingattributeonthemoduleitself:
>>> import typing
>>> typing.__name__, typing.__spec__.name
('typing', 'typing')
>>> typing.__spec__.name = 'spelling'
>>> typing.__name__, typing.__spec__.name
('typing', 'spelling')
>>> typing.__name__ = 'keyboard_smashing'
>>> typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling') |

### 第40页

Thisattributeismostlyusefulforintrospection,butcanbeusedforadditionalloader-specificfunctionality,for
examplegettingdataassociatedwithaloader.
__loader__defaultstoNoneformodulescreateddynamicallyusingthetypes.ModuleTypeconstructor;
useimportlib.util.module_from_spec()insteadtoensuretheattributeissettoaloaderobject.
Itisstronglyrecommendedthatyouusemodule.__spec__.loaderinsteadofmodule.__loader__.
Changedinversion3.4:ThisattributenowdefaultstoNoneformodulescreateddynamicallyusingthetypes.
ModuleTypeconstructor. Previouslytheattributewasoptional.
Deprecated since version 3.12, will be removed in version 3.16: Setting __loader__ on a module while
failingtoset__spec__.loaderisdeprecated. InPython3.16,__loader__willceasetobesetortaken
intoconsiderationbytheimportsystemorthestandardlibrary.
module.__path__
A (possibly empty) sequence of strings enumerating the locations where the package’s submodules will be
found. Non-packagemodulesshouldnothavea__path__attribute. See__path__attributesonmodulesfor
moredetails.
Itisstronglyrecommendedthatyouusemodule.__spec__.submodule_search_locationsinsteadof
module.__path__.
module.__file__
module.__cached__
__file__and__cached__arebothoptionalattributesthatmayormaynotbeset. Bothattributesshould
beastrwhentheyareavailable.
__file__indicatesthepathnameofthefilefromwhichthemodulewasloaded(ifloadedfromafile),orthe
pathnameofthesharedlibraryfileforextensionmodulesloadeddynamicallyfromasharedlibrary. Itmight
bemissingforcertaintypesofmodules,suchasCmodulesthatarestaticallylinkedintotheinterpreter,and
theimportsystemmayopttoleaveitunsetifithasnosemanticmeaning(forexample,amoduleloadedfrom
adatabase).
If__file__issetthenthe__cached__attributemightalsobeset,whichisthepathtoanycompiledversion
ofthecode(forexample,abyte-compiledfile). Thefiledoesnotneedtoexisttosetthisattribute; thepath
cansimplypointtowherethecompiledfilewouldexist(seePEP3147).
Note that __cached__ may be set even if __file__ is not set. However, that scenario is quite atypical.
Ultimately,theloaderiswhatmakesuseofthemodulespecprovidedbythefinder(fromwhich__file__
and __cached__ are derived). So if a loader can load from a cached module but otherwise does not load
fromafile,thatatypicalscenariomaybeappropriate.
Itisstronglyrecommendedthatyouusemodule.__spec__.cachedinsteadofmodule.__cached__.
Deprecated since version 3.13, will be removed in version 3.15: Setting __cached__ on a module while
failingtoset__spec__.cachedisdeprecated. InPython3.15,__cached__willceasetobesetortaken
intoconsiderationbytheimportsystemorstandardlibrary.
Otherwritableattributesonmoduleobjects
Aswellastheimport-relatedattributeslistedabove,moduleobjectsalsohavethefollowingwritableattributes:
module.__doc__
Themodule’sdocumentationstring,orNoneifunavailable. Seealso: __doc__ attributes.
module.__annotations__
Adictionarycontainingvariableannotationscollectedduringmodulebodyexecution. Forbestpracticeson
workingwith__annotations__,seeannotationlib.
Changedinversion3.14: Annotationsarenowlazilyevaluated. SeePEP649.
32 Chapter3. Datamodel

### 第41页

module.__annotate__
Theannotatefunctionforthismodule,orNoneifthemodulehasnoannotations. Seealso: __annotate__
attributes.
Addedinversion3.14.
Moduledictionaries
Moduleobjectsalsohavethefollowingspecialread-onlyattribute:
module.__dict__
Themodule’snamespaceasadictionaryobject. Uniquelyamongtheattributeslistedhere,__dict__cannot
beaccessedasaglobalvariablefromwithinamodule;itcanonlybeaccessedasanattributeonmoduleobjects.
CPythonimplementationdetail: BecauseofthewayCPythonclearsmoduledictionaries,themoduledic-
tionarywillbeclearedwhenthemodulefallsoutofscopeevenifthedictionarystillhaslivereferences. To
avoidthis,copythedictionaryorkeepthemodulearoundwhileusingitsdictionarydirectly.
3.2.10 Custom classes
Customclasstypesaretypicallycreatedbyclassdefinitions(seesectionClassdefinitions). Aclasshasanamespace
implementedbyadictionaryobject. Classattributereferencesaretranslatedtolookupsinthisdictionary,e.g.,C.x
istranslatedtoC.__dict__["x"](althoughthereareanumberofhookswhichallowforothermeansoflocating
attributes). Whentheattributenameisnotfoundthere,theattributesearchcontinuesinthebaseclasses. Thissearch
ofthebaseclassesusestheC3methodresolutionorderwhichbehavescorrectlyeveninthepresenceof‘diamond’
inheritance structures where there are multiple inheritance paths leading back to a common ancestor. Additional
detailsontheC3MROusedbyPythoncanbefoundatpython_2.3_mro.
Whenaclassattributereference(forclassC,say)wouldyieldaclassmethodobject,itistransformedintoaninstance
methodobjectwhose__self__attributeisC.Whenitwouldyieldastaticmethodobject,itistransformedinto
the object wrapped by the static method object. See section Implementing Descriptors for another way in which
attributesretrievedfromaclassmaydifferfromthoseactuallycontainedinits__dict__.
Classattributeassignmentsupdatetheclass’sdictionary,neverthedictionaryofabaseclass.
Aclassobjectcanbecalled(seeabove)toyieldaclassinstance(seebelow).
3.2. Thestandardtypehierarchy 33

### 第42页

Specialattributes
Attribute Meaning
Theclass’sname. Seealso: __name__ attributes.
type.__name__
Theclass’squalifiedname. Seealso: __qualname__
type.__qualname__ attributes.
Thenameofthemoduleinwhichtheclasswasdefined.
type.__module__
A mapping proxy providing a read-only view of
type.__dict__ the class’s namespace. See also: __dict__
attributes.
A tuple containing the class’s bases. In most
type.__bases__ cases, fora classdefined as class X(A, B, C), X.
__bases__willbeexactlyequalto(A, B, C).
Theclass’sdocumentationstring,orNoneifundefined.
type.__doc__ Notinheritedbysubclasses.
A dictionary containing variable annotations col-
type.__annotations__ lected during class body execution. See also:
__annotations__ attributes.
For best practices on working with
__annotations__, please see annotationlib.
Useannotationlib.get_annotations()instead
ofaccessingthisattributedirectly.
(cid:193) Warning
Accessing the __annotations__ attribute di-
rectly on a class object may return annota-
tions for the wrong class, specifically in cer-
tain cases where the class, its base class, or a
metaclass is defined under from __future__
import annotations. See749fordetails.
This attribute does not exist on certain builtin
classes. On user-defined classes without
__annotations__, it is an empty dictio-
nary.
Changed in version 3.14: Annotations are now lazily
evaluated. SeePEP649.
The annotate function for this class, or None if the
type.__annotate__() class has no annotations. See also: __annotate__
attributes.
Addedinversion3.14.
A tuple containing the type parameters of a generic
type.__type_params__ class.
Addedinversion3.12.
A tuple containing names of attributes of this class
type.__static_attributes__ whichareassignedthroughself.Xfromanyfunction
initsbody.
Addedinversion3.13.
The line number of the first line of the class defini-
type.__firstlineno__ tion, including decorators. Setting the __module__
attribute removes the __firstlineno__ item from
thetype’sdictionary.
Addedinversion3.13.
34 Chapter3. Datamodel

| Attribute | Meaning |
| --- | --- |
| type.__name__ | Theclass’sname. Seealso: __name__ attributes. |
| type.__qualname__ | Theclass’squalifiedname. Seealso: __qualname__
attributes. |
| type.__module__ | Thenameofthemoduleinwhichtheclasswasdefined. |
| type.__dict__ | A mapping proxy providing a read-only view of
the class’s namespace. See also: __dict__
attributes. |
| type.__bases__ | A tuple containing the class’s bases. In most
cases, fora classdefined as class X(A, B, C), X.
__bases__willbeexactlyequalto(A, B, C). |
| type.__doc__ | Theclass’sdocumentationstring,orNoneifundefined.
Notinheritedbysubclasses. |
| type.__annotations__ | A dictionary containing variable annotations col-
lected during class body execution. See also:
__annotations__ attributes.
For best practices on working with
__annotations__, please see annotationlib.
Useannotationlib.get_annotations()instead
ofaccessingthisattributedirectly.
(cid:193) Warning
Accessing the __annotations__ attribute di-
rectly on a class object may return annota-
tions for the wrong class, specifically in cer-
tain cases where the class, its base class, or a
metaclass is defined under from __future__
import annotations. See749fordetails.
This attribute does not exist on certain builtin
classes. On user-defined classes without
__annotations__, it is an empty dictio-
nary.
Changed in version 3.14: Annotations are now lazily
evaluated. SeePEP649. |
| type.__annotate__() | The annotate function for this class, or None if the
class has no annotations. See also: __annotate__
attributes.
Addedinversion3.14. |
| type.__type_params__ | A tuple containing the type parameters of a generic
class.
Addedinversion3.12. |
| type.__static_attributes__ | A tuple containing names of attributes of this class
whichareassignedthroughself.Xfromanyfunction
initsbody.
Addedinversion3.13. |
| type.__firstlineno__ | The line number of the first line of the class defini-
tion, including decorators. Setting the __module__
attribute removes the __firstlineno__ item from
thetype’sdictionary. |
| 34 | Addedinversion3.13.
Chapter3. Datamodel |


| (cid:193) Warning |
| --- |
| Accessing the __annotations__ attribute di-
rectly on a class object may return annota-
tions for the wrong class, specifically in cer-
tain cases where the class, its base class, or a
metaclass is defined under from __future__
import annotations. See749fordetails.
This attribute does not exist on certain builtin
classes. On user-defined classes without
__annotations__, it is an empty dictio-
nary. |

### 第43页

Specialmethods
Inadditiontothespecialattributesdescribedabove,allPythonclassesalsohavethefollowingtwomethodsavailable:
type.mro()
Thismethodcanbeoverriddenbyametaclasstocustomizethemethodresolutionorderforitsinstances. Itis
calledatclassinstantiation,anditsresultisstoredin__mro__.
type.__subclasses__()
Eachclasskeepsalistofweakreferencestoitsimmediatesubclasses. Thismethodreturnsalistofallthose
referencesstillalive. Thelistisindefinitionorder. Example:
>>> class A: pass
>>> class B(A): pass
>>> A.__subclasses__()
[<class 'B'>]
3.2.11 Class instances
Aclassinstanceiscreatedbycallingaclassobject(seeabove). Aclassinstancehasanamespaceimplementedasa
dictionarywhichisthefirstplaceinwhichattributereferencesaresearched. Whenanattributeisnotfoundthere,
andtheinstance’sclasshasanattributebythatname,thesearchcontinueswiththeclassattributes. Ifaclassattribute
is found that is a user-defined function object, it is transformed into an instance method object whose __self__
attribute is the instance. Static method and class method objects are also transformed; see above under “Classes”.
See section Implementing Descriptors for another way in which attributes of a class retrieved via its instances may
differfromtheobjectsactuallystoredintheclass’s__dict__. Ifnoclassattributeisfound,andtheobject’sclass
hasa__getattr__()method,thatiscalledtosatisfythelookup.
Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary. If the class has a
__setattr__()or__delattr__()method,thisiscalledinsteadofupdatingtheinstancedictionarydirectly.
Classinstancescanpretendtobenumbers,sequences,ormappingsiftheyhavemethodswithcertainspecialnames.
SeesectionSpecialmethodnames.
Specialattributes
object.__class__
Theclasstowhichaclassinstancebelongs.
object.__dict__
Adictionaryorothermappingobjectusedtostoreanobject’s(writable)attributes. Notallinstanceshavea
__dict__attribute;seethesectionon__slots__formoredetails.
3.2.12 I/O objects (also known as file objects)
A file object represents an open file. Various shortcuts are available to create file objects: the open() built-in
function, andalsoos.popen(), os.fdopen(), andthemakefile()methodofsocketobjects(andperhapsby
otherfunctionsormethodsprovidedbyextensionmodules).
Theobjectssys.stdin,sys.stdoutandsys.stderrareinitializedtofileobjectscorrespondingtotheinter-
preter’s standard input, output and error streams; they are all open in text mode and therefore follow the interface
definedbytheio.TextIOBaseabstractclass.
3.2.13 Internal types
A few types used internally by the interpreter are exposed to the user. Their definitions may change with future
versionsoftheinterpreter,buttheyarementionedhereforcompleteness.
3.2. Thestandardtypehierarchy 35

### 第44页

Codeobjects
Code objects represent byte-compiled executable Python code, or bytecode. The difference between a code object
andafunctionobjectisthatthefunctionobjectcontainsanexplicitreferencetothefunction’sglobals(themodule
inwhichitwasdefined),whileacodeobjectcontainsnocontext;alsothedefaultargumentvaluesarestoredinthe
functionobject,notinthecodeobject(becausetheyrepresentvaluescalculatedatrun-time). Unlikefunctionobjects,
codeobjectsareimmutableandcontainnoreferences(directlyorindirectly)tomutableobjects.
36 Chapter3. Datamodel

### 第45页

Specialread-onlyattributes
Thefunctionname
codeobject.co_name
Thefullyqualifiedfunctionname
codeobject.co_qualname Addedinversion3.11.
The total number of positional parameters (including
codeobject.co_argcount positional-onlyparametersandparameterswithdefault
values)thatthefunctionhas
The number of positional-only parameters (including
codeobject.co_posonlyargcount argumentswithdefaultvalues)thatthefunctionhas
Thenumberofkeyword-onlyparameters(includingar-
codeobject.co_kwonlyargcount gumentswithdefaultvalues)thatthefunctionhas
Thenumberoflocalvariablesusedbythefunction(in-
codeobject.co_nlocals cludingparameters)
Atuplecontainingthenamesofthelocalvariablesin
codeobject.co_varnames thefunction(startingwiththeparameternames)
A tuple containing the names of local variables that
codeobject.co_cellvars arereferencedfromatleastonenestedscopeinsidethe
function
A tuple containing the names of free (closure) vari-
codeobject.co_freevars ables that a nested scope references in an outer scope.
Seealsofunction.__closure__.
Note: referencestoglobalandbuiltinnamesarenotin-
cluded.
Astringrepresentingthesequenceofbytecodeinstruc-
codeobject.co_code tionsinthefunction
Atuplecontainingtheliteralsusedbythebytecodein
codeobject.co_consts thefunction
Atuplecontainingthenamesusedbythebytecodein
codeobject.co_names thefunction
Thenameofthefilefromwhichthecodewascompiled
codeobject.co_filename
Thelinenumberofthefirstlineofthefunction
codeobject.co_firstlineno
Astringencodingthemappingfrombytecodeoffsetsto
codeobject.co_lnotab line numbers. For details, see the source code of the
interpreter.
Deprecated since version 3.12: This attribute of code
objects is deprecated, and may be removed in Python
3.15.
Therequiredstacksizeofthecodeobject
codeobject.co_stacksize
Anintegerencodinganumberofflagsfortheinter-
codeobject.co_flags preter.
3.2. Thestandardtypehierarchy 37

| codeobject.co_name | Thefunctionname |
| --- | --- |
| codeobject.co_qualname | Thefullyqualifiedfunctionname
Addedinversion3.11. |
| codeobject.co_argcount | The total number of positional parameters (including
positional-onlyparametersandparameterswithdefault
values)thatthefunctionhas |
| codeobject.co_posonlyargcount | The number of positional-only parameters (including
argumentswithdefaultvalues)thatthefunctionhas |
| codeobject.co_kwonlyargcount | Thenumberofkeyword-onlyparameters(includingar-
gumentswithdefaultvalues)thatthefunctionhas |
| codeobject.co_nlocals | Thenumberoflocalvariablesusedbythefunction(in-
cludingparameters) |
| codeobject.co_varnames | Atuplecontainingthenamesofthelocalvariablesin
thefunction(startingwiththeparameternames) |
| codeobject.co_cellvars | A tuple containing the names of local variables that
arereferencedfromatleastonenestedscopeinsidethe
function |
| codeobject.co_freevars | A tuple containing the names of free (closure) vari-
ables that a nested scope references in an outer scope.
Seealsofunction.__closure__.
Note: referencestoglobalandbuiltinnamesarenotin-
cluded. |
| codeobject.co_code | Astringrepresentingthesequenceofbytecodeinstruc-
tionsinthefunction |
| codeobject.co_consts | Atuplecontainingtheliteralsusedbythebytecodein
thefunction |
| codeobject.co_names | Atuplecontainingthenamesusedbythebytecodein
thefunction |
| codeobject.co_filename | Thenameofthefilefromwhichthecodewascompiled |
| codeobject.co_firstlineno | Thelinenumberofthefirstlineofthefunction |
| codeobject.co_lnotab | Astringencodingthemappingfrombytecodeoffsetsto
line numbers. For details, see the source code of the
interpreter.
Deprecated since version 3.12: This attribute of code
objects is deprecated, and may be removed in Python
3.15. |
| codeobject.co_stacksize | Therequiredstacksizeofthecodeobject |
| codeobject.co_flags | Anintegerencodinganumberofflagsfortheinter-
preter. |

### 第46页

The following flag bits are defined for co_flags: bit 0x04 is set if the function uses the *arguments syntax to
acceptanarbitrarynumberofpositionalarguments;bit0x08issetifthefunctionusesthe**keywordssyntaxto
acceptarbitrarykeywordarguments; bit0x20issetifthefunctionisagenerator. Seeinspect-module-co-flagsfor
detailsonthesemanticsofeachflagsthatmightbepresent.
Futurefeaturedeclarations(forexample,from __future__ import division)alsousebitsinco_flagsto
indicatewhetheracodeobjectwascompiledwithaparticularfeatureenabled. Seecompiler_flag.
Otherbitsinco_flagsarereservedforinternaluse.
Ifacodeobjectrepresentsafunctionandhasadocstring,theCO_HAS_DOCSTRINGbitissetinco_flagsandthe
firstiteminco_constsisthedocstringofthefunction.
Methodsoncodeobjects
codeobject.co_positions()
Returnsaniterableoverthesourcecodepositionsofeachbytecodeinstructioninthecodeobject.
Theiteratorreturnstuplescontainingthe(start_line, end_line, start_column, end_column).
The i-th tuple corresponds to the position of the source code that compiled to the i-th code unit. Column
informationis0-indexedutf-8byteoffsetsonthegivensourceline.
Thispositionalinformationcanbemissing. Anon-exhaustivelistsofcaseswherethismayhappen:
• Runningtheinterpreterwith-Xno_debug_ranges.
• Loadingapycfilecompiledwhileusing-Xno_debug_ranges.
• Positiontuplescorrespondingtoartificialinstructions.
• Lineandcolumnnumbersthatcan’tberepresentedduetoimplementationspecificlimitations.
Whenthisoccurs,someorallofthetupleelementscanbeNone.
Addedinversion3.11.
(cid:174) Note
Thisfeaturerequiresstoringcolumnpositionsincodeobjectswhichmayresultinasmallincreaseofdisk
usageofcompiledPythonfilesorinterpretermemoryusage. Toavoidstoringtheextrainformationand/or
deactivateprintingtheextratracebackinformation,the-Xno_debug_rangescommandlineflagorthe
PYTHONNODEBUGRANGESenvironmentvariablecanbeused.
codeobject.co_lines()
Returns an iterator that yields information about successive ranges of bytecodes. Each item yielded is a
(start, end, lineno)tuple:
• start(anint)representstheoffset(inclusive)ofthestartofthebytecoderange
• end(anint)representstheoffset(exclusive)oftheendofthebytecoderange
• linenoisanintrepresentingthelinenumberofthebytecoderange,orNoneifthebytecodesinthe
givenrangehavenolinenumber
Theitemsyieldedwillhavethefollowingproperties:
• Thefirstrangeyieldedwillhaveastartof0.
• The(start, end)rangeswillbenon-decreasingandconsecutive. Thatis,foranypairoftuples,the
startofthesecondwillbeequaltotheendofthefirst.
• Norangewillbebackwards: end >= startforalltriples.
• Thelasttupleyieldedwillhaveendequaltothesizeofthebytecode.
38 Chapter3. Datamodel

### 第47页

Zero-widthranges,wherestart == end,areallowed. Zero-widthrangesareusedforlinesthatarepresent
inthesourcecode,buthavebeeneliminatedbythebytecodecompiler.
Addedinversion3.10.
(cid:181) Seealso
PEP626-Preciselinenumbersfordebuggingandothertools.
ThePEPthatintroducedtheco_lines()method.
codeobject.replace(**kwargs)
Returnacopyofthecodeobjectwithnewvaluesforthespecifiedfields.
Codeobjectsarealsosupportedbythegenericfunctioncopy.replace().
Addedinversion3.8.
Frameobjects
Frame objects represent execution frames. They may occur in traceback objects, and are also passed to registered
tracefunctions.
Specialread-onlyattributes
Pointstothepreviousstackframe(towardsthecaller),
frame.f_back orNoneifthisisthebottomstackframe
The code object being executed in this frame. Ac-
frame.f_code cessingthisattributeraisesanauditingeventobject.
__getattr__withargumentsobjand"f_code".
Themappingusedbytheframetolookuplocalvari-
frame.f_locals ables. Iftheframereferstoanoptimizedscope,thismay
returnawrite-throughproxyobject.
Changedinversion3.13: Returnaproxyforoptimized
scopes.
Thedictionaryusedbytheframetolookupglobalvari-
frame.f_globals ables
Thedictionaryusedbytheframetolookupbuilt-in(in-
frame.f_builtins trinsic)names
The“preciseinstruction”oftheframeobject(thisisan
frame.f_lasti indexintothebytecodestringofthecodeobject)
Thegeneratororcoroutineobjectthatownsthisframe,
frame.f_generator orNoneiftheframeisanormalfunction.
Addedinversion3.14.
3.2. Thestandardtypehierarchy 39

| (cid:181) Seealso |
| --- |
| PEP626-Preciselinenumbersfordebuggingandothertools.
ThePEPthatintroducedtheco_lines()method. |


| frame.f_back | Pointstothepreviousstackframe(towardsthecaller),
orNoneifthisisthebottomstackframe |
| --- | --- |
| frame.f_code | The code object being executed in this frame. Ac-
cessingthisattributeraisesanauditingeventobject.
__getattr__withargumentsobjand"f_code". |
| frame.f_locals | Themappingusedbytheframetolookuplocalvari-
ables. Iftheframereferstoanoptimizedscope,thismay
returnawrite-throughproxyobject.
Changedinversion3.13: Returnaproxyforoptimized
scopes. |
| frame.f_globals | Thedictionaryusedbytheframetolookupglobalvari-
ables |
| frame.f_builtins | Thedictionaryusedbytheframetolookupbuilt-in(in-
trinsic)names |
| frame.f_lasti | The“preciseinstruction”oftheframeobject(thisisan
indexintothebytecodestringofthecodeobject) |
| frame.f_generator | Thegeneratororcoroutineobjectthatownsthisframe,
orNoneiftheframeisanormalfunction.
Addedinversion3.14. |

### 第48页

Specialwritableattributes
IfnotNone,thisisafunctioncalledforvariousevents
frame.f_trace duringcodeexecution(thisisusedbydebuggers). Nor-
mallyaneventistriggeredforeachnewsourceline(see
f_trace_lines).
SetthisattributetoFalsetodisabletriggeringatracing
frame.f_trace_lines eventforeachsourceline.
Set this attribute to True to allow per-opcode events
frame.f_trace_opcodes to be requested. Note that this may lead to undefined
interpreter behaviour if exceptions raised by the trace
functionescapetothefunctionbeingtraced.
Thecurrentlinenumberoftheframe–writingtothis
frame.f_lineno from within a trace function jumps to the given line
(onlyforthebottom-mostframe). Adebuggercanim-
plementaJumpcommand(akaSetNextStatement)by
writingtothisattribute.
Frameobjectmethods
Frameobjectssupportonemethod:
frame.clear()
Thismethodclearsallreferencestolocalvariablesheldbytheframe. Also,iftheframebelongedtoagenerator,
thegeneratorisfinalized. Thishelpsbreakreferencecyclesinvolvingframeobjects(forexamplewhencatching
anexceptionandstoringitstracebackforlateruse).
RuntimeErrorisraisediftheframeiscurrentlyexecutingorsuspended.
Addedinversion3.4.
Changedinversion3.13: AttemptingtoclearasuspendedframeraisesRuntimeError(ashasalwaysbeen
thecaseforexecutingframes).
Tracebackobjects
Traceback objects represent the stack trace of an exception. A traceback object is implicitly created when an ex-
ceptionoccurs,andmayalsobeexplicitlycreatedbycallingtypes.TracebackType.
Changedinversion3.7: TracebackobjectscannowbeexplicitlyinstantiatedfromPythoncode.
For implicitly created tracebacks, when the search for an exception handler unwinds the execution stack, at each
unwoundlevelatracebackobjectisinsertedinfrontofthecurrenttraceback. Whenanexceptionhandlerisentered,
thestacktraceismadeavailabletotheprogram. (SeesectionThetrystatement.) Itisaccessibleasthethirditemof
thetuplereturnedbysys.exc_info(),andasthe__traceback__attributeofthecaughtexception.
When the program contains no suitable handler, the stack trace is written (nicely formatted) to the standard error
stream;iftheinterpreterisinteractive,itisalsomadeavailabletotheuserassys.last_traceback.
Forexplicitlycreatedtracebacks,itisuptothecreatorofthetracebacktodeterminehowthetb_nextattributes
shouldbelinkedtoformafullstacktrace.
Specialread-onlyattributes:
40 Chapter3. Datamodel

| frame.f_trace | IfnotNone,thisisafunctioncalledforvariousevents
duringcodeexecution(thisisusedbydebuggers). Nor-
mallyaneventistriggeredforeachnewsourceline(see
f_trace_lines). |
| --- | --- |
| frame.f_trace_lines | SetthisattributetoFalsetodisabletriggeringatracing
eventforeachsourceline. |
| frame.f_trace_opcodes | Set this attribute to True to allow per-opcode events
to be requested. Note that this may lead to undefined
interpreter behaviour if exceptions raised by the trace
functionescapetothefunctionbeingtraced. |
| frame.f_lineno | Thecurrentlinenumberoftheframe–writingtothis
from within a trace function jumps to the given line
(onlyforthebottom-mostframe). Adebuggercanim-
plementaJumpcommand(akaSetNextStatement)by
writingtothisattribute. |

### 第49页

Pointstotheexecutionframeofthecurrentlevel.
traceback.tb_frame Accessing this attribute raises an auditing event
object.__getattr__ with arguments obj and
"tb_frame".
Givesthelinenumberwheretheexceptionoccurred
traceback.tb_lineno
Indicatesthe“preciseinstruction”.
traceback.tb_lasti
The line number and last instruction in the traceback may differ from the line number of its frame object if the
exceptionoccurredinatrystatementwithnomatchingexceptclauseorwithafinallyclause.
traceback.tb_next
Thespecialwritableattributetb_nextisthenextlevelinthestacktrace(towardstheframewheretheex-
ceptionoccurred),orNoneifthereisnonextlevel.
Changedinversion3.7: Thisattributeisnowwritable
Sliceobjects
Slice objects are used to represent slices for __getitem__() methods. They are also created by the built-in
slice()function.
Special read-only attributes: start is the lower bound; stop is the upper bound; step is the step value; each is
Noneifomitted. Theseattributescanhaveanytype.
Sliceobjectssupportonemethod:
slice.indices(self,length)
This method takes a single integer argument length and computes information about the slice that the slice
objectwoulddescribeifappliedtoasequenceoflengthitems. Itreturnsatupleofthreeintegers;respectively
thesearethestartandstopindicesandthesteporstridelengthoftheslice. Missingorout-of-boundsindices
arehandledinamannerconsistentwithregularslices.
Staticmethodobjects
Staticmethodobjectsprovideawayofdefeatingthetransformationoffunctionobjectstomethodobjectsdescribed
above. Astaticmethodobjectisawrapperaroundanyotherobject,usuallyauser-definedmethodobject. Whena
staticmethodobjectisretrievedfromaclassoraclassinstance,theobjectactuallyreturnedisthewrappedobject,
whichisnotsubjecttoanyfurthertransformation. Staticmethodobjectsarealsocallable. Staticmethodobjectsare
createdbythebuilt-instaticmethod()constructor.
Classmethodobjects
Aclassmethodobject,likeastaticmethodobject,isawrapperaroundanotherobjectthataltersthewayinwhich
thatobjectisretrievedfromclassesandclassinstances. Thebehaviourofclassmethodobjectsuponsuchretrieval
is described above, under “instance methods”. Class method objects are created by the built-in classmethod()
constructor.
3.3 Special method names
Aclasscanimplementcertainoperationsthatareinvokedbyspecialsyntax(suchasarithmeticoperationsorsub-
scripting and slicing) by defining methods with special names. This is Python’s approach to operator overloading,
allowing classes to define their own behavior with respect to language operators. For instance, if a class defines a
methodnamed__getitem__(),andxisaninstanceofthisclass,thenx[i]isroughlyequivalenttotype(x).
__getitem__(x, i). Except where mentioned, attempts to execute an operation raise an exception when no
appropriatemethodisdefined(typicallyAttributeErrororTypeError).
3.3. Specialmethodnames 41

| traceback.tb_frame | Pointstotheexecutionframeofthecurrentlevel.
Accessing this attribute raises an auditing event
object.__getattr__ with arguments obj and
"tb_frame". |
| --- | --- |
| traceback.tb_lineno | Givesthelinenumberwheretheexceptionoccurred |
| traceback.tb_lasti | Indicatesthe“preciseinstruction”. |

### 第50页

SettingaspecialmethodtoNoneindicatesthatthecorrespondingoperationisnotavailable. Forexample,ifaclass
sets __iter__() to None, the class is not iterable, so calling iter() on its instances will raise a TypeError
(withoutfallingbackto__getitem__()).2
Whenimplementingaclassthatemulatesanybuilt-intype,itisimportantthattheemulationonlybeimplemented
tothedegreethatitmakessensefortheobjectbeingmodelled. Forexample,somesequencesmayworkwellwith
retrieval of individual elements, but extracting a slice may not make sense. (One example of this is the NodeList
interfaceintheW3C’sDocumentObjectModel.)
3.3.1 Basic customization
[ ]
object.__new__(cls ,... )
Called to create a new instance of class cls. __new__() is a static method (special-cased so you need not
declareitassuch)thattakestheclassofwhichaninstancewasrequestedasitsfirstargument. Theremaining
arguments are those passed to the object constructor expression (the call to the class). The return value of
__new__()shouldbethenewobjectinstance(usuallyaninstanceofcls).
Typicalimplementationscreateanewinstanceoftheclassbyinvokingthesuperclass’s__new__()method
usingsuper().__new__(cls[, ...])withappropriateargumentsandthenmodifyingthenewlycreated
instanceasnecessarybeforereturningit.
If__new__()isinvokedduringobjectconstructionanditreturnsaninstanceofcls,thenthenewinstance’s
__init__() method will be invoked like __init__(self[, ...]), where self is the new instance and
theremainingargumentsarethesameaswerepassedtotheobjectconstructor.
If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be
invoked.
__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize
instancecreation. Itisalsocommonlyoverriddenincustommetaclassesinordertocustomizeclasscreation.
[ ]
object.__init__(self ,... )
Calledaftertheinstancehasbeencreated(by__new__()),butbeforeitisreturnedtothecaller. Theargu-
mentsarethosepassedtotheclassconstructorexpression. Ifabaseclasshasan__init__()method,the
derivedclass’s__init__()method,ifany,mustexplicitlycallittoensureproperinitializationofthebase
classpartoftheinstance;forexample: super().__init__([args...]).
Because__new__()and__init__()worktogetherinconstructingobjects(__new__()tocreateit,and
__init__() to customize it), no non-None value may be returned by __init__(); doing so will cause a
TypeErrortoberaisedatruntime.
object.__del__(self)
Calledwhentheinstanceisabouttobedestroyed. Thisisalsocalledafinalizeror(improperly)adestructor.
Ifabaseclasshasa__del__()method,thederivedclass’s__del__()method,ifany,mustexplicitlycall
ittoensureproperdeletionofthebaseclasspartoftheinstance.
Itispossible(thoughnotrecommended!) forthe__del__()methodtopostponedestructionoftheinstance
bycreatinganewreferencetoit. Thisiscalledobjectresurrection. Itisimplementation-dependentwhether
__del__()iscalledasecondtimewhenaresurrectedobjectisabouttobedestroyed;thecurrentCPython
implementationonlycallsitonce.
Itisnotguaranteedthat__del__()methodsarecalledforobjectsthatstillexistwhentheinterpreterexits.
weakref.finalizeprovidesastraightforwardwaytoregisteracleanupfunctiontobecalledwhenanobject
isgarbagecollected.
(cid:174) Note
del xdoesn’tdirectlycallx.__del__()—theformerdecrementsthereferencecountforxbyone,and
thelatterisonlycalledwhenx’sreferencecountreacheszero.
2The__hash__(),__iter__(),__reversed__(),__contains__(),__class_getitem__()and__fspath__()methodshave
specialhandlingforthis.OtherswillstillraiseaTypeError,butmaydosobyrelyingonthebehaviorthatNoneisnotcallable.
42 Chapter3. Datamodel

### 第51页

CPythonimplementationdetail:Itispossibleforareferencecycletopreventthereferencecountofanobject
fromgoingtozero. Inthiscase,thecyclewillbelaterdetectedanddeletedbythecyclicgarbagecollector. A
commoncauseofreferencecyclesiswhenanexceptionhasbeencaughtinalocalvariable. Theframe’slocals
then reference the exception, which references its own traceback, which references the locals of all frames
caughtinthetraceback.
(cid:181) Seealso
Documentationforthegcmodule.
(cid:193) Warning
Duetotheprecariouscircumstancesunderwhich__del__()methodsareinvoked,exceptionsthatoccur
duringtheirexecutionareignored,andawarningisprintedtosys.stderrinstead. Inparticular:
• __del__() can be invoked when arbitrary code is being executed, including from any arbitrary
thread. If__del__()needstotakealockorinvokeanyotherblockingresource,itmaydeadlock
astheresourcemayalreadybetakenbythecodethatgetsinterruptedtoexecute__del__().
• __del__()canbeexecutedduringinterpretershutdown. Asaconsequence,theglobalvariables
itneedstoaccess(includingothermodules)mayalreadyhavebeendeletedorsettoNone. Python
guaranteesthatglobalswhosenamebeginswithasingleunderscorearedeletedfromtheirmodule
beforeotherglobalsaredeleted;ifnootherreferencestosuchglobalsexist,thismayhelpinassuring
thatimportedmodulesarestillavailableatthetimewhenthe__del__()methodiscalled.
object.__repr__(self)
Called by the repr() built-in function to compute the “official” string representation of an object. If at
all possible, this should look like a valid Python expression that could be used to recreate an object with
the same value (given an appropriate environment). If this is not possible, a string of the form <...some
useful description...>shouldbereturned. Thereturnvaluemustbeastringobject. Ifaclassdefines
__repr__()butnot__str__(),then__repr__()isalsousedwhenan“informal”stringrepresentation
ofinstancesofthatclassisrequired.
Thisistypicallyusedfordebugging,soitisimportantthattherepresentationisinformation-richandunam-
biguous. Adefaultimplementationisprovidedbytheobjectclassitself.
object.__str__(self)
Calledbystr(object),thedefault__format__()implementation,andthebuilt-infunctionprint(),to
computethe“informal”ornicelyprintablestringrepresentationofanobject. Thereturnvaluemustbeastr
object.
Thismethoddiffersfromobject.__repr__()inthatthereisnoexpectationthat__str__()returnavalid
Pythonexpression: amoreconvenientorconciserepresentationcanbeused.
Thedefaultimplementationdefinedbythebuilt-intypeobjectcallsobject.__repr__().
object.__bytes__(self)
Calledbybytestocomputeabyte-stringrepresentationofanobject. Thisshouldreturnabytesobject. The
objectclassitselfdoesnotprovidethismethod.
object.__format__(self,format_spec)
Calledbytheformat()built-infunction,andbyextension,evaluationofformattedstringliteralsandthestr.
format()method, toproducea“formatted”stringrepresentationofanobject. Theformat_spec argument
isastringthatcontainsadescriptionoftheformattingoptionsdesired. Theinterpretationoftheformat_spec
argumentisuptothetypeimplementing__format__(),howevermostclasseswilleitherdelegateformatting
tooneofthebuilt-intypes,oruseasimilarformattingoptionsyntax.
Seeformatspecforadescriptionofthestandardformattingsyntax.
Thereturnvaluemustbeastringobject.
3.3. Specialmethodnames 43

| (cid:181) Seealso |
| --- |
| Documentationforthegcmodule. |


| (cid:193) Warning |
| --- |
| Duetotheprecariouscircumstancesunderwhich__del__()methodsareinvoked,exceptionsthatoccur
duringtheirexecutionareignored,andawarningisprintedtosys.stderrinstead. Inparticular:
• __del__() can be invoked when arbitrary code is being executed, including from any arbitrary
thread. If__del__()needstotakealockorinvokeanyotherblockingresource,itmaydeadlock
astheresourcemayalreadybetakenbythecodethatgetsinterruptedtoexecute__del__().
• __del__()canbeexecutedduringinterpretershutdown. Asaconsequence,theglobalvariables
itneedstoaccess(includingothermodules)mayalreadyhavebeendeletedorsettoNone. Python
guaranteesthatglobalswhosenamebeginswithasingleunderscorearedeletedfromtheirmodule
beforeotherglobalsaredeleted;ifnootherreferencestosuchglobalsexist,thismayhelpinassuring
thatimportedmodulesarestillavailableatthetimewhenthe__del__()methodiscalled. |

### 第52页

Thedefaultimplementationbytheobjectclassshouldbegivenanemptyformat_specstring. Itdelegatesto
__str__().
Changed in version 3.4: The __format__ method of object itself raises a TypeError if passed any non-
emptystring.
Changed in version 3.7: object.__format__(x, '') is now equivalent to str(x) rather than
format(str(x), '').
object.__lt__(self,other)
object.__le__(self,other)
object.__eq__(self,other)
object.__ne__(self,other)
object.__gt__(self,other)
object.__ge__(self,other)
These are the so-called “rich comparison” methods. The correspondence between operator symbols and
methodnamesisasfollows: x<ycallsx.__lt__(y),x<=ycallsx.__le__(y),x==ycallsx.__eq__(y),
x!=ycallsx.__ne__(y),x>ycallsx.__gt__(y),andx>=ycallsx.__ge__(y).
ArichcomparisonmethodmayreturnthesingletonNotImplementedifitdoesnotimplementtheoperation
for a given pair of arguments. By convention, False and True are returned for a successful comparison.
However,thesemethodscanreturnanyvalue,soifthecomparisonoperatorisusedinaBooleancontext(e.g.,
intheconditionofanifstatement),Pythonwillcallbool()onthevaluetodetermineiftheresultistrueor
false.
By default, object implements __eq__() by using is, returning NotImplemented in the case of a
false comparison: True if x is y else NotImplemented. For __ne__(), by default it delegates to
__eq__() and inverts the result unless it is NotImplemented. There are no other implied relationships
amongthecomparisonoperatorsordefaultimplementations;forexample,thetruthof(x<y or x==y)does
notimplyx<=y. Toautomaticallygenerateorderingoperationsfromasinglerootoperation,seefunctools.
total_ordering().
Bydefault,theobjectclassprovidesimplementationsconsistentwithValuecomparisons: equalitycompares
according to object identity, and order comparisons raise TypeError. Each default method may generate
theseresultsdirectly,butmayalsoreturnNotImplemented.
See the paragraph on __hash__() for some important notes on creating hashable objects which support
customcomparisonoperationsandareusableasdictionarykeys.
Therearenoswapped-argumentversionsofthesemethods(tobeusedwhentheleftargumentdoesnotsup-
porttheoperationbuttherightargumentdoes);rather,__lt__()and__gt__()areeachother’sreflection,
__le__()and__ge__()areeachother’sreflection,and__eq__()and__ne__()aretheirownreflection.
If theoperandsareofdifferent types, andtherightoperand’s type isa director indirectsubclassoftheleft
operand’stype,thereflectedmethodoftherightoperandhaspriority,otherwisetheleftoperand’smethodhas
priority. Virtualsubclassingisnotconsidered.
WhennoappropriatemethodreturnsanyvalueotherthanNotImplemented,the==and!=operatorswill
fallbacktoisandis not,respectively.
object.__hash__(self)
Called by built-in function hash() and for operations on members of hashed collections including set,
frozenset, and dict. The __hash__() method should return an integer. The only required property
isthatobjectswhichcompareequalhavethesamehashvalue;itisadvisedtomixtogetherthehashvaluesof
thecomponentsoftheobjectthatalsoplayapartincomparisonofobjectsbypackingthemintoatupleand
hashingthetuple. Example:
def __hash__(self):
return hash((self.name, self.nick, self.color))
44 Chapter3. Datamodel

### 第53页

(cid:174) Note
hash() truncates the value returned from an object’s custom __hash__() method to the size of a
Py_ssize_t. This is typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds. If an object’s
__hash__() must interoperate on builds of different bit sizes, be sure to check the width on all sup-
portedbuilds. Aneasywaytodothisiswithpython -c "import sys; print(sys.hash_info.
width)".
If a class does not define an __eq__() method it should not define a __hash__() operation either; if it
defines__eq__()butnot__hash__(),itsinstanceswillnotbeusableasitemsinhashablecollections. Ifa
classdefinesmutableobjectsandimplementsan__eq__()method,itshouldnotimplement__hash__(),
sincetheimplementationofhashablecollectionsrequiresthatakey’shashvalueisimmutable(iftheobject’s
hashvaluechanges,itwillbeinthewronghashbucket).
User-definedclasseshave__eq__()and__hash__()methodsbydefault(inheritedfromtheobjectclass);
withthem,allobjectscompareunequal(exceptwiththemselves)andx.__hash__()returnsanappropriate
valuesuchthatx == yimpliesboththatx is yandhash(x) == hash(y).
Aclassthatoverrides__eq__()anddoesnotdefine__hash__()willhaveits__hash__()implicitlyset
toNone. Whenthe__hash__()methodofaclassisNone,instancesoftheclasswillraiseanappropriate
TypeError when a program attempts to retrieve their hash value, and will also be correctly identified as
unhashablewhencheckingisinstance(obj, collections.abc.Hashable).
Ifaclassthatoverrides__eq__()needstoretaintheimplementationof__hash__()fromaparentclass,
theinterpretermustbetoldthisexplicitlybysetting__hash__ = <ParentClass>.__hash__.
Ifaclassthatdoesnotoverride__eq__()wishestosuppresshashsupport, itshouldinclude__hash__ =
Noneintheclassdefinition. Aclasswhichdefinesitsown__hash__()thatexplicitlyraisesaTypeError
wouldbeincorrectlyidentifiedashashablebyanisinstance(obj, collections.abc.Hashable)call.
(cid:174) Note
By default, the __hash__() values of str and bytes objects are “salted” with an unpredictable random
value. AlthoughtheyremainconstantwithinanindividualPythonprocess,theyarenotpredictablebetween
repeatedinvocationsofPython.
This is intended to provide protection against a denial-of-service caused by carefully chosen inputs that
exploittheworstcaseperformanceofadictinsertion,O(n2)complexity. Seehttp://ocert.org/advisories/
ocert-2011-003.htmlfordetails.
Changing hash values affects the iteration order of sets. Python has never made guarantees about this
ordering(andittypicallyvariesbetween32-bitand64-bitbuilds).
SeealsoPYTHONHASHSEED.
Changedinversion3.3: Hashrandomizationisenabledbydefault.
object.__bool__(self)
Called to implement truth value testing and the built-in operation bool(); should return False or True.
Whenthismethodisnotdefined,__len__()iscalled,ifitisdefined,andtheobjectisconsideredtrueifits
resultisnonzero. Ifaclassdefinesneither__len__()nor__bool__()(whichistrueoftheobjectclass
itself),allitsinstancesareconsideredtrue.
3.3.2 Customizing attribute access
Thefollowingmethodscanbedefinedtocustomizethemeaningofattributeaccess(useof,assignmentto,ordeletion
ofx.name)forclassinstances.
object.__getattr__(self,name)
CalledwhenthedefaultattributeaccessfailswithanAttributeError(either__getattribute__()raises
3.3. Specialmethodnames 45

### 第54页

anAttributeErrorbecausenameisnotaninstanceattributeoranattributeintheclasstreeforself;or
__get__()ofanamepropertyraisesAttributeError). Thismethodshouldeitherreturnthe(computed)
attributevalueorraiseanAttributeErrorexception. Theobjectclassitselfdoesnotprovidethismethod.
Note that if the attribute is found through the normal mechanism, __getattr__() is not called. (This is
anintentionalasymmetrybetween__getattr__()and__setattr__().) Thisisdonebothforefficiency
reasonsandbecauseotherwise__getattr__()wouldhavenowaytoaccessotherattributesoftheinstance.
Notethatatleastforinstancevariables,youcantaketotalcontrolbynotinsertinganyvaluesintheinstance
attributedictionary(butinsteadinsertingtheminanotherobject). Seethe__getattribute__()method
belowforawaytoactuallygettotalcontroloverattributeaccess.
object.__getattribute__(self,name)
Called unconditionally to implement attribute accesses for instances of the class. If the class also de-
fines __getattr__(), the latter will not be called unless __getattribute__() either calls it explic-
itly or raises an AttributeError. This method should return the (computed) attribute value or raise an
AttributeErrorexception. Inordertoavoidinfiniterecursioninthismethod, itsimplementationshould
alwayscallthebaseclassmethodwiththesamenametoaccessanyattributesitneeds,forexample,object.
__getattribute__(self, name).
(cid:174) Note
Thismethodmaystillbebypassedwhenlookingupspecialmethodsastheresultofimplicitinvocationvia
languagesyntaxorbuilt-infunctions. SeeSpecialmethodlookup.
Forcertainsensitiveattributeaccesses,raisesanauditingeventobject.__getattr__withargumentsobj
andname.
object.__setattr__(self,name,value)
Calledwhenanattributeassignmentisattempted. Thisiscalledinsteadofthenormalmechanism(i.e. store
thevalueintheinstancedictionary). nameistheattributename,valueisthevaluetobeassignedtoit.
If__setattr__()wantstoassigntoaninstanceattribute,itshouldcallthebaseclassmethodwiththesame
name,forexample,object.__setattr__(self, name, value).
Forcertainsensitiveattributeassignments, raisesanauditingeventobject.__setattr__witharguments
obj,name,value.
object.__delattr__(self,name)
Like__setattr__()butforattributedeletioninsteadofassignment. Thisshouldonlybeimplementedif
del obj.nameismeaningfulfortheobject.
Forcertainsensitiveattributedeletions,raisesanauditingeventobject.__delattr__withargumentsobj
andname.
object.__dir__(self)
Calledwhendir()iscalledontheobject. Aniterablemustbereturned. dir()convertsthereturnediterable
toalistandsortsit.
Customizingmoduleattributeaccess
module.__getattr__()
module.__dir__()
Special names __getattr__ and __dir__ can be also used to customize access to module attributes. The
__getattr__ function at the module level should accept one argument which is the name of an attribute and
returnthecomputedvalueorraiseanAttributeError. Ifanattributeisnotfoundonamoduleobjectthroughthe
46 Chapter3. Datamodel

### 第55页

normal lookup, i.e. object.__getattribute__(), then __getattr__ is searched in the module __dict__
beforeraisinganAttributeError. Iffound,itiscalledwiththeattributenameandtheresultisreturned.
The__dir__functionshouldacceptnoarguments,andreturnaniterableofstringsthatrepresentsthenamesac-
cessibleonmodule. Ifpresent,thisfunctionoverridesthestandarddir()searchonamodule.
module.__class__
Fora morefinegrainedcustomizationofthemodulebehavior(settingattributes, properties, etc.), onecansetthe
__class__attributeofamoduleobjecttoasubclassoftypes.ModuleType. Forexample:
import sys
from types import ModuleType
class VerboseModule(ModuleType):
def __repr__(self):
return f'Verbose {self.__name__}'
def __setattr__(self, attr, value):
print(f'Setting {attr}...')
super().__setattr__(attr, value)
sys.modules[__name__].__class__ = VerboseModule
(cid:174) Note
Defining module __getattr__ and setting module __class__ only affect lookups made using the attribute
accesssyntax–directlyaccessingthemoduleglobals(whetherbycodewithinthemodule,orviaareferenceto
themodule’sglobalsdictionary)isunaffected.
Changedinversion3.5: __class__moduleattributeisnowwritable.
Addedinversion3.7: __getattr__and__dir__moduleattributes.
(cid:181) Seealso
PEP562-Module__getattr__and__dir__
Describesthe__getattr__and__dir__functionsonmodules.
ImplementingDescriptors
Thefollowingmethodsonlyapplywhenaninstanceoftheclasscontainingthemethod(aso-calleddescriptorclass)
appearsinanownerclass(thedescriptormustbeineithertheowner’sclassdictionaryorintheclassdictionaryfor
oneofitsparents). Intheexamplesbelow,“theattribute”referstotheattributewhosenameisthekeyoftheproperty
intheownerclass’__dict__. Theobjectclassitselfdoesnotimplementanyoftheseprotocols.
object.__get__(self,instance,owner=None)
Calledtogettheattributeoftheownerclass(classattributeaccess)orofaninstanceofthatclass(instance
attribute access). The optional owner argument is the owner class, while instance is the instance that the
attributewasaccessedthrough,orNonewhentheattributeisaccessedthroughtheowner.
ThismethodshouldreturnthecomputedattributevalueorraiseanAttributeErrorexception.
PEP252specifiesthat__get__()iscallablewithoneortwoarguments. Python’sownbuilt-indescriptors
support this specification; however, it is likely that some third-party tools have descriptors that require both
arguments. Python’sown__getattribute__()implementationalwayspassesinbothargumentswhether
theyarerequiredornot.
3.3. Specialmethodnames 47

| (cid:181) Seealso |
| --- |
| PEP562-Module__getattr__and__dir__
Describesthe__getattr__and__dir__functionsonmodules. |

### 第56页

object.__set__(self,instance,value)
Calledtosettheattributeonaninstanceinstanceoftheownerclasstoanewvalue,value.
Note,adding__set__()or__delete__()changesthekindofdescriptortoa“datadescriptor”. SeeIn-
vokingDescriptorsformoredetails.
object.__delete__(self,instance)
Calledtodeletetheattributeonaninstanceinstanceoftheownerclass.
Instancesofdescriptorsmayalsohavethe__objclass__attributepresent:
object.__objclass__
Theattribute__objclass__isinterpretedbytheinspectmoduleasspecifyingtheclasswherethisobject
was defined (setting this appropriately can assist in runtime introspection of dynamic class attributes). For
callables,itmayindicatethataninstanceofthegiventype(orasubclass)isexpectedorrequiredasthefirst
positionalargument(forexample, CPythonsetsthisattributeforunboundmethodsthatareimplementedin
C).
InvokingDescriptors
Ingeneral,adescriptorisanobjectattributewith“bindingbehavior”,onewhoseattributeaccesshasbeenoverridden
bymethodsinthedescriptorprotocol: __get__(),__set__(),and__delete__(). Ifanyofthosemethodsare
definedforanobject,itissaidtobeadescriptor.
Thedefaultbehaviorforattributeaccessistoget,set,ordeletetheattributefromanobject’sdictionary. Forinstance,
a.xhasalookupchainstartingwitha.__dict__['x'],thentype(a).__dict__['x'],andcontinuingthrough
thebaseclassesoftype(a)excludingmetaclasses.
However,ifthelooked-upvalueisanobjectdefiningoneofthedescriptormethods,thenPythonmayoverridethe
defaultbehaviorandinvokethedescriptormethodinstead. Wherethisoccursintheprecedencechaindependson
whichdescriptormethodsweredefinedandhowtheywerecalled.
Thestartingpointfordescriptorinvocationisabinding,a.x. Howtheargumentsareassembleddependsona:
DirectCall
Thesimplestandleastcommoncalliswhenusercodedirectlyinvokesadescriptormethod: x.__get__(a).
InstanceBinding
Ifbindingtoanobjectinstance,a.xistransformedintothecall: type(a).__dict__['x'].__get__(a,
type(a)).
ClassBinding
Ifbindingtoaclass,A.xistransformedintothecall: A.__dict__['x'].__get__(None, A).
SuperBinding
Adottedlookupsuchassuper(A, a).xsearchesa.__class__.__mro__forabaseclassBfollowingA
andthenreturnsB.__dict__['x'].__get__(a, A).Ifnotadescriptor,xisreturnedunchanged.
For instance bindings, the precedence of descriptor invocation depends on which descriptor methods are defined.
A descriptor can define any combination of __get__(), __set__() and __delete__(). If it does not define
__get__(),thenaccessingtheattributewillreturnthedescriptorobjectitselfunlessthereisavalueintheobject’s
instancedictionary. Ifthedescriptordefines__set__()and/or__delete__(),itisadatadescriptor;ifitdefines
neither,itisanon-datadescriptor. Normally,datadescriptorsdefineboth__get__()and__set__(),whilenon-
data descriptors have just the __get__() method. Data descriptors with __get__() and __set__() (and/or
__delete__())definedalwaysoverridearedefinitioninaninstancedictionary. Incontrast,non-datadescriptors
canbeoverriddenbyinstances.
Pythonmethods(includingthosedecoratedwith@staticmethodand@classmethod)areimplementedasnon-
data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to
acquirebehaviorsthatdifferfromotherinstancesofthesameclass.
Theproperty()functionisimplementedasadatadescriptor. Accordingly,instancescannotoverridethebehavior
ofaproperty.
48 Chapter3. Datamodel

### 第57页

__slots__
__slots__ allow us to explicitly declare data members (like properties) and deny the creation of __dict__ and
__weakref__(unlessexplicitlydeclaredin__slots__oravailableinaparent.)
Thespacesavedoverusing__dict__canbesignificant. Attributelookupspeedcanbesignificantlyimprovedas
well.
object.__slots__
Thisclassvariablecanbeassignedastring, iterable, orsequenceofstringswithvariablenamesusedbyin-
stances. __slots__reservesspaceforthedeclaredvariablesandpreventstheautomaticcreationof__dict__
and__weakref__foreachinstance.
Notesonusing__slots__:
• When inheriting from a class without __slots__, the __dict__ and __weakref__ attribute of the instances
willalwaysbeaccessible.
• Withouta__dict__variable,instancescannotbeassignednewvariablesnotlistedinthe__slots__definition.
Attempts to assign to an unlisted variable name raises AttributeError. If dynamic assignment of new
variablesisdesired,thenadd'__dict__'tothesequenceofstringsinthe__slots__declaration.
• Without a __weakref__ variable for each instance, classes defining __slots__ do not support weak
references to its instances. If weak reference support is needed, then add '__weakref__' to the se-
quenceofstringsinthe__slots__declaration.
• __slots__areimplementedattheclasslevelbycreatingdescriptorsforeachvariablename. Asaresult,class
attributescannotbeusedtosetdefaultvaluesforinstancevariablesdefinedby__slots__;otherwise,theclass
attributewouldoverwritethedescriptorassignment.
• Theactionofa__slots__declarationisnotlimitedtotheclasswhereitisdefined. __slots__declaredinparents
areavailableinchildclasses. However, instancesofachildsubclasswillgeta__dict__and__weakref__
unlessthesubclassalsodefines__slots__(whichshouldonlycontainnamesofanyadditionalslots).
• If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is
inaccessible(exceptbyretrievingitsdescriptordirectlyfromthebaseclass). Thisrendersthemeaningofthe
programundefined. Inthefuture,acheckmaybeaddedtopreventthis.
• TypeErrorwillberaisedifnonempty__slots__aredefinedforaclassderivedfroma"variable-length"
built-in typesuchasint,bytes,andtuple.
• Anynon-stringiterablemaybeassignedto__slots__.
• Ifadictionaryisusedtoassign__slots__,thedictionarykeyswillbeusedastheslotnames. Thevaluesof
thedictionarycanbeusedtoprovideper-attributedocstringsthatwillberecognisedbyinspect.getdoc()
anddisplayedintheoutputofhelp().
• __class__assignmentworksonlyifbothclasseshavethesame__slots__.
• Multipleinheritancewithmultipleslottedparentclassescanbeused,butonlyoneparentisallowedtohave
attributescreatedbyslots(theotherbasesmusthaveemptyslotlayouts)-violationsraiseTypeError.
• Ifaniterator isusedfor__slots__thenadescriptor iscreatedforeachoftheiterator’svalues. However,the
__slots__attributewillbeanemptyiterator.
3.3.3 Customizing class creation
Whenevera classinherits fromanother class, __init_subclass__() iscalled onthe parentclass. This way, it
ispossibletowriteclasseswhichchangethebehaviorofsubclasses. Thisiscloselyrelatedtoclassdecorators,but
whereclassdecoratorsonlyaffectthespecificclassthey’reappliedto,__init_subclass__solelyappliestofuture
subclassesoftheclassdefiningthemethod.
classmethod object.__init_subclass__(cls)
Thismethodiscalledwheneverthecontainingclassissubclassed. clsisthenthenewsubclass. Ifdefinedasa
normalinstancemethod,thismethodisimplicitlyconvertedtoaclassmethod.
3.3. Specialmethodnames 49

### 第58页

Keyword arguments which are given to a new class are passed to the parent class’s __init_subclass__.
For compatibility with other classes using __init_subclass__, one should take out the needed keyword
argumentsandpasstheothersovertothebaseclass,asin:
class Philosopher:
def __init_subclass__(cls, /, default_name, **kwargs):
super().__init_subclass__(**kwargs)
cls.default_name = default_name
class AustralianPhilosopher(Philosopher, default_name="Bruce"):
pass
The default implementation object.__init_subclass__ does nothing, but raises an error if it is called
withanyarguments.
(cid:174) Note
The metaclass hint metaclass is consumed by the rest of the type machinery, and is never passed to
__init_subclass__ implementations. The actual metaclass (rather than the explicit hint) can be ac-
cessedastype(cls).
Addedinversion3.6.
When a class is created, type.__new__() scans the class variables and makes callbacks to those with a
__set_name__()hook.
object.__set_name__(self,owner,name)
Automaticallycalledatthetimetheowningclassowneriscreated. Theobjecthasbeenassignedtonamein
thatclass:
class A:
x = C() # Automatically calls: x.__set_name__(A, 'x')
Iftheclassvariableisassignedaftertheclassiscreated,__set_name__()willnotbecalledautomatically.
Ifneeded,__set_name__()canbecalleddirectly:
class A:
pass
c = C()
A.x = c # The hook is not called
c.__set_name__(A, 'x') # Manually invoke the hook
SeeCreatingtheclassobjectformoredetails.
Addedinversion3.6.
Metaclasses
Bydefault,classesareconstructedusingtype(). Theclassbodyisexecutedinanewnamespaceandtheclassname
isboundlocallytotheresultoftype(name, bases, namespace).
Theclasscreationprocesscanbecustomizedbypassingthemetaclasskeywordargumentintheclassdefinition
line,orbyinheritingfromanexistingclassthatincludedsuchanargument. Inthefollowingexample,bothMyClass
andMySubclassareinstancesofMeta:
class Meta(type):
pass
(continuesonnextpage)
50 Chapter3. Datamodel

### 第59页

(continuedfrompreviouspage)
class MyClass(metaclass=Meta):
pass
class MySubclass(MyClass):
pass
Anyotherkeywordargumentsthatarespecifiedintheclassdefinitionarepassedthroughtoallmetaclassoperations
describedbelow.
Whenaclassdefinitionisexecuted,thefollowingstepsoccur:
• MROentriesareresolved;
• theappropriatemetaclassisdetermined;
• theclassnamespaceisprepared;
• theclassbodyisexecuted;
• theclassobjectiscreated.
ResolvingMROentries
object.__mro_entries__(self,bases)
Ifabasethatappearsinaclassdefinitionisnotaninstanceoftype,thenan__mro_entries__()method
issearchedonthebase. Ifan__mro_entries__()methodisfound,thebaseissubstitutedwiththeresult
ofacallto__mro_entries__()whencreatingtheclass. Themethodiscalledwiththeoriginalbasestuple
passed to the bases parameter, and must return a tuple of classes thatwill be used insteadof the base. The
returnedtuplemaybeempty: inthesecases,theoriginalbaseisignored.
(cid:181) Seealso
types.resolve_bases()
Dynamicallyresolvebasesthatarenotinstancesoftype.
types.get_original_bases()
Retrieveaclass’s“originalbases”priortomodificationsby__mro_entries__().
PEP560
Coresupportfortypingmoduleandgenerictypes.
Determiningtheappropriatemetaclass
Theappropriatemetaclassforaclassdefinitionisdeterminedasfollows:
• ifnobasesandnoexplicitmetaclassaregiven,thentype()isused;
• ifanexplicitmetaclassisgivenanditisnotaninstanceoftype(),thenitisuseddirectlyasthemetaclass;
• ifaninstanceoftype()isgivenastheexplicitmetaclass,orbasesaredefined,thenthemostderivedmetaclass
isused.
The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e.
type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these
candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail
withTypeError.
3.3. Specialmethodnames 51

| (cid:181) Seealso |
| --- |
| types.resolve_bases()
Dynamicallyresolvebasesthatarenotinstancesoftype.
types.get_original_bases()
Retrieveaclass’s“originalbases”priortomodificationsby__mro_entries__().
PEP560
Coresupportfortypingmoduleandgenerictypes. |

### 第60页

Preparingtheclassnamespace
Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has
a__prepare__attribute,itiscalledasnamespace = metaclass.__prepare__(name, bases, **kwds)
(wheretheadditionalkeywordarguments,ifany,comefromtheclassdefinition). The__prepare__methodshould
beimplementedasaclassmethod. Thenamespacereturnedby__prepare__ispassedinto__new__,butwhen
thefinalclassobjectiscreatedthenamespaceiscopiedintoanewdict.
Ifthemetaclasshasno__prepare__attribute,thentheclassnamespaceisinitialisedasanemptyorderedmapping.
(cid:181) Seealso
PEP3115-MetaclassesinPython3000
Introducedthe__prepare__namespacehook
Executingtheclassbody
Theclassbodyisexecuted(approximately)asexec(body, globals(), namespace). Thekeydifferencefrom
a normal call to exec() is that lexical scoping allows the class body (including any methods) to reference names
fromthecurrentandouterscopeswhentheclassdefinitionoccursinsideafunction.
However,evenwhentheclassdefinitionoccursinsidethefunction,methodsdefinedinsidetheclassstillcannotsee
namesdefinedattheclassscope. Classvariablesmustbeaccessedthroughthefirstparameterofinstanceorclass
methods,orthroughtheimplicitlexicallyscoped__class__referencedescribedinthenextsection.
Creatingtheclassobject
Once the class namespace has been populated by executing the class body, the class object is created by calling
metaclass(name, bases, namespace, **kwds)(theadditionalkeywordspassedherearethesameasthose
passedto__prepare__).
Thisclassobjectistheonethatwillbereferencedbythezero-argumentformofsuper(). __class__isanimplicit
closurereferencecreatedbythecompilerifanymethodsinaclassbodyrefertoeither__class__orsuper. This
allows the zero argument form of super() to correctly identify the class being defined based on lexical scoping,
whiletheclassorinstancethatwasusedtomakethecurrentcallisidentifiedbasedonthefirstargumentpassedto
themethod.
CPython implementation detail: In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a
__classcell__entryintheclassnamespace. Ifpresent,thismustbepropagateduptothetype.__new__call
inorderfortheclasstobeinitialisedcorrectly. FailingtodosowillresultinaRuntimeErrorinPython3.8.
Whenusingthedefaultmetaclasstype,oranymetaclassthatultimatelycallstype.__new__,thefollowingaddi-
tionalcustomizationstepsareinvokedaftercreatingtheclassobject:
1) The type.__new__ method collects all of the attributes in the class namespace that define a
__set_name__()method;
2) Those__set_name__methodsarecalledwiththeclassbeingdefinedandtheassignednameofthatparticular
attribute;
3) The__init_subclass__()hookiscalledontheimmediateparentofthenewclassinitsmethodresolution
order.
Aftertheclassobjectiscreated,itispassedtotheclassdecoratorsincludedintheclassdefinition(ifany)andthe
resultingobjectisboundinthelocalnamespaceasthedefinedclass.
Whenanewclassiscreatedbytype.__new__,theobjectprovidedasthenamespaceparameteriscopiedtoanew
orderedmappingandtheoriginalobjectisdiscarded. Thenewcopyiswrappedinaread-onlyproxy,whichbecomes
the__dict__attributeoftheclassobject.
(cid:181) Seealso
52 Chapter3. Datamodel

| (cid:181) Seealso |
| --- |
| PEP3115-MetaclassesinPython3000
Introducedthe__prepare__namespacehook |


| (cid:181) Seealso |
| --- |
|  |

### 第61页

PEP3135-Newsuper
Describestheimplicit__class__closurereference
Usesformetaclasses
The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, in-
terface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource
locking/synchronization.
3.3.4 Customizing instance and subclass checks
Thefollowingmethodsareusedtooverridethedefaultbehavioroftheisinstance()andissubclass()built-in
functions.
Inparticular,themetaclassabc.ABCMetaimplementsthesemethodsinordertoallowtheadditionofAbstractBase
Classes(ABCs)as“virtualbaseclasses”toanyclassortype(includingbuilt-intypes),includingotherABCs.
type.__instancecheck__(self,instance)
Returntrueifinstanceshouldbeconsidereda(directorindirect)instanceofclass. Ifdefined,calledtoimple-
mentisinstance(instance, class).
type.__subclasscheck__(self,subclass)
Returntrueifsubclassshouldbeconsidereda(directorindirect)subclassofclass. Ifdefined,calledtoimple-
mentissubclass(subclass, class).
Notethatthesemethodsarelookeduponthetype(metaclass)ofaclass. Theycannotbedefinedasclassmethodsin
theactualclass. Thisisconsistentwiththelookupofspecialmethodsthatarecalledoninstances,onlyinthiscase
theinstanceisitselfaclass.
(cid:181) Seealso
PEP3119-IntroducingAbstractBaseClasses
Includes the specification for customizing isinstance() and issubclass() behavior through
__instancecheck__()and__subclasscheck__(),withmotivationforthisfunctionalityinthecon-
textofaddingAbstractBaseClasses(seetheabcmodule)tothelanguage.
3.3.5 Emulating generic types
Whenusingtypeannotations,itisoftenusefultoparameterizeagenerictypeusingPython’ssquare-bracketsnotation.
Forexample,theannotationlist[int]mightbeusedtosignifyalistinwhichalltheelementsareoftypeint.
(cid:181) Seealso
PEP484-TypeHints
IntroducingPython’sframeworkfortypeannotations
GenericAliasTypes
Documentationforobjectsrepresentingparameterizedgenericclasses
Generics,user-definedgenericsandtyping.Generic
Documentationonhowtoimplementgenericclassesthatcanbeparameterizedatruntimeandunderstood
bystatictype-checkers.
Aclasscangenerallyonlybeparameterizedifitdefinesthespecialclassmethod__class_getitem__().
classmethod object.__class_getitem__(cls,key)
Returnanobjectrepresentingthespecializationofagenericclassbytypeargumentsfoundinkey.
3.3. Specialmethodnames 53

| (cid:181) Seealso |
| --- |
| PEP3119-IntroducingAbstractBaseClasses
Includes the specification for customizing isinstance() and issubclass() behavior through
__instancecheck__()and__subclasscheck__(),withmotivationforthisfunctionalityinthecon-
textofaddingAbstractBaseClasses(seetheabcmodule)tothelanguage. |


| (cid:181) Seealso |
| --- |
| PEP484-TypeHints
IntroducingPython’sframeworkfortypeannotations
GenericAliasTypes
Documentationforobjectsrepresentingparameterizedgenericclasses
Generics,user-definedgenericsandtyping.Generic
Documentationonhowtoimplementgenericclassesthatcanbeparameterizedatruntimeandunderstood
bystatictype-checkers. |

### 第62页

Whendefinedonaclass,__class_getitem__()isautomaticallyaclassmethod. Assuch,thereisnoneed
forittobedecoratedwith@classmethodwhenitisdefined.
Thepurposeof__class_getitem__
Thepurposeof__class_getitem__()istoallowruntimeparameterizationofstandard-librarygenericclassesin
ordertomoreeasilyapplytypehintstotheseclasses.
Toimplementcustomgenericclassesthatcanbeparameterizedatruntimeandunderstoodbystatictype-checkers,
usersshouldeitherinheritfromastandardlibraryclassthatalreadyimplements__class_getitem__(),orinherit
fromtyping.Generic,whichhasitsownimplementationof__class_getitem__().
Customimplementationsof__class_getitem__()onclassesdefinedoutsideofthestandardlibrarymaynotbe
understoodbythird-partytype-checkerssuchasmypy. Using__class_getitem__()onanyclassforpurposes
otherthantypehintingisdiscouraged.
__class_getitem__versus__getitem__
Usually,thesubscriptionofanobjectusingsquarebracketswillcallthe__getitem__()instancemethoddefinedon
theobject’sclass. However,iftheobjectbeingsubscribedisitselfaclass,theclassmethod__class_getitem__()
maybecalledinstead. __class_getitem__()shouldreturnaGenericAliasobjectifitisproperlydefined.
Presentedwiththeexpressionobj[x],thePythoninterpreterfollowssomethinglikethefollowingprocesstodecide
whether__getitem__()or__class_getitem__()shouldbecalled:
from inspect import isclass
def subscribe(obj, x):
"""Return the result of the expression 'obj[x]'"""
class_of_obj = type(obj)
# If the class of obj defines __getitem__,
# call class_of_obj.__getitem__(obj, x)
if hasattr(class_of_obj, '__getitem__'):
return class_of_obj.__getitem__(obj, x)
# Else, if obj is a class and defines __class_getitem__,
# call obj.__class_getitem__(x)
elif isclass(obj) and hasattr(obj, '__class_getitem__'):
return obj.__class_getitem__(x)
# Else, raise an exception
else:
raise TypeError(
f"'{class_of_obj.__name__}' object is not subscriptable"
)
InPython,allclassesarethemselvesinstancesofotherclasses. Theclassofaclassisknownasthatclass’smetaclass,
andmostclasseshavethetypeclassastheirmetaclass. typedoesnotdefine__getitem__(),meaningthatexpres-
sionssuchaslist[int],dict[str, float]andtuple[str, bytes]allresultin__class_getitem__()
beingcalled:
>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
(continuesonnextpage)
54 Chapter3. Datamodel

### 第63页

(continuedfrompreviouspage)
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>
However,ifaclasshasacustommetaclassthatdefines__getitem__(),subscribingtheclassmayresultindifferent
behaviour. Anexampleofthiscanbefoundintheenummodule:
>>> from enum import Enum
>>> class Menu(Enum):
... """A breakfast menu"""
... SPAM = 'spam'
... BACON = 'bacon'
...
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>
(cid:181) Seealso
PEP560-CoreSupportfortypingmoduleandgenerictypes
Introducing __class_getitem__(), and outlining when a subscription results in
__class_getitem__()beingcalledinsteadof__getitem__()
3.3.6 Emulating callable objects
[ ]
object.__call__(self ,args... )
Calledwhentheinstanceis“called”asafunction;ifthismethodisdefined,x(arg1, arg2, ...)roughly
translatestotype(x).__call__(x, arg1, ...). Theobjectclassitselfdoesnotprovidethismethod.
3.3.7 Emulating container types
Thefollowingmethodscanbedefinedtoimplementcontainerobjects. Noneofthemareprovidedbytheobject
class itself. Containers usually are sequences (such as lists or tuples) or mappings (like dictionaries), but can
represent other containers as well. The first set of methods is used either to emulate a sequence or to emulate a
mapping; thedifferenceisthatforasequence,theallowablekeysshouldbetheintegersk forwhich0 <= k < N
where N is the length of the sequence, or slice objects, which define a range of items. It is also recommended
that mappings provide the methods keys(), values(), items(), get(), clear(), setdefault(), pop(),
popitem(), copy(), and update() behaving similar to those for Python’s standard dictionary objects. The
collections.abcmoduleprovidesaMutableMappingabstractbaseclasstohelpcreatethosemethodsfroma
basesetof__getitem__(),__setitem__(),__delitem__(),andkeys().
Mutable sequences should provide methods append(), clear(), count(), extend(), index(), insert(),
pop(),remove(),andreverse(),likePythonstandardlistobjects. Finally,sequencetypesshouldimplement
addition (meaning concatenation) and multiplication (meaning repetition) by defining the methods __add__(),
__radd__(),__iadd__(),__mul__(),__rmul__()and__imul__()describedbelow;theyshouldnotdefine
othernumericaloperators.
Itisrecommendedthatbothmappingsandsequencesimplementthe__contains__()methodtoallowefficient
3.3. Specialmethodnames 55

| (cid:181) Seealso |
| --- |
| PEP560-CoreSupportfortypingmoduleandgenerictypes
Introducing __class_getitem__(), and outlining when a subscription results in
__class_getitem__()beingcalledinsteadof__getitem__() |

### 第64页

useoftheinoperator;formappings,inshouldsearchthemapping’skeys;forsequences,itshouldsearchthrough
the values. It is further recommended that both mappings and sequences implement the __iter__() method to
allowefficientiterationthroughthecontainer;formappings,__iter__()shoulditeratethroughtheobject’skeys;
forsequences,itshoulditeratethroughthevalues.
object.__len__(self)
Calledtoimplementthebuilt-infunctionlen(). Shouldreturnthelengthoftheobject,aninteger>=0. Also,
anobjectthatdoesn’tdefinea__bool__()methodandwhose__len__()methodreturnszeroisconsidered
tobefalseinaBooleancontext.
CPython implementation detail: In CPython, the length is required to be at most sys.maxsize. If the
lengthislargerthansys.maxsizesomefeatures(suchaslen())mayraiseOverflowError. Toprevent
raisingOverflowErrorbytruthvaluetesting,anobjectmustdefinea__bool__()method.
object.__length_hint__(self)
Calledtoimplementoperator.length_hint(). Shouldreturnanestimatedlengthfortheobject(which
maybegreaterorlessthantheactuallength). Thelengthmustbeaninteger>=0. Thereturnvaluemayalso
beNotImplemented,whichistreatedthesameasifthe__length_hint__methoddidn’texistatall. This
methodispurelyanoptimizationandisneverrequiredforcorrectness.
Addedinversion3.4.
(cid:174) Note
Slicingisdoneexclusivelywiththefollowingthreemethods. Acalllike
a[1:2] = b
istranslatedto
a[slice(1, 2, None)] = b
andsoforth. MissingsliceitemsarealwaysfilledinwithNone.
object.__getitem__(self,key)
Called to implement evaluation of self[key]. For sequence types, the accepted keys should be integers.
Optionally,theymaysupportsliceobjectsaswell. Negativeindexsupportisalsooptional. Ifkeyisofan
inappropriate type, TypeError may be raised; if key is a value outside the set of indexes for the sequence
(afteranyspecialinterpretationofnegativevalues),IndexErrorshouldberaised. Formappingtypes,ifkey
ismissing(notinthecontainer),KeyErrorshouldberaised.
(cid:174) Note
for loopsexpectthatanIndexErrorwillberaisedforillegalindexestoallowproperdetectionofthe
endofthesequence.
(cid:174) Note
When subscripting a class, the special class method __class_getitem__() may be called instead of
__getitem__(). See__class_getitem__versus__getitem__formoredetails.
object.__setitem__(self,key,value)
Called to implement assignment to self[key]. Same note as for __getitem__(). This should only be
implementedformappingsiftheobjectssupportchangestothevaluesforkeys,orifnewkeyscanbeadded,
orforsequencesifelementscanbereplaced. Thesameexceptionsshouldberaisedforimproperkeyvalues
asforthe__getitem__()method.
56 Chapter3. Datamodel

### 第65页

object.__delitem__(self,key)
Calledtoimplementdeletionofself[key]. Samenoteasfor__getitem__(). Thisshouldonlybeim-
plementedformappingsiftheobjectssupportremovalofkeys,orforsequencesifelementscanberemoved
fromthesequence. Thesameexceptionsshouldberaisedforimproperkeyvaluesasforthe__getitem__()
method.
object.__missing__(self,key)
Calledbydict.__getitem__()toimplementself[key]fordictsubclasseswhenkeyisnotinthedictio-
nary.
object.__iter__(self)
Thismethodiscalledwhenaniterator isrequiredforacontainer. Thismethodshouldreturnanewiterator
objectthatcaniterateoveralltheobjectsinthecontainer. Formappings,itshoulditerateoverthekeysofthe
container.
object.__reversed__(self)
Called(ifpresent)bythereversed()built-intoimplementreverseiteration. Itshouldreturnanewiterator
objectthatiteratesoveralltheobjectsinthecontainerinreverseorder.
Ifthe__reversed__()methodisnotprovided,thereversed()built-inwillfallbacktousingthesequence
protocol(__len__()and__getitem__()). Objectsthatsupportthesequenceprotocolshouldonlyprovide
__reversed__() if they can provide an implementation that is more efficient than the one provided by
reversed().
The membership test operators (in and not in) are normally implemented as an iteration through a container.
However, container objects can supply the following special method with a more efficient implementation, which
alsodoesnotrequiretheobjectbeiterable.
object.__contains__(self,item)
Called to implement membership test operators. Should return true if item is in self, false otherwise. For
mappingobjects,thisshouldconsiderthekeysofthemappingratherthanthevaluesorthekey-itempairs.
For objects that don’t define __contains__(), the membership test first tries iteration via __iter__(),
thentheoldsequenceiterationprotocolvia__getitem__(),seethissectioninthelanguagereference.
3.3.8 Emulating numeric types
Thefollowingmethodscanbedefinedtoemulatenumericobjects. Methodscorrespondingtooperationsthatarenot
supportedbytheparticularkindofnumberimplemented(e.g.,bitwiseoperationsfornon-integralnumbers)should
beleftundefined.
object.__add__(self,other)
object.__sub__(self,other)
object.__mul__(self,other)
object.__matmul__(self,other)
object.__truediv__(self,other)
object.__floordiv__(self,other)
object.__mod__(self,other)
object.__divmod__(self,other)
[ ]
object.__pow__(self,other ,modulo )
object.__lshift__(self,other)
object.__rshift__(self,other)
object.__and__(self,other)
object.__xor__(self,other)
object.__or__(self,other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(),
pow(),**,<<,>>,&,^,|). Forinstance,toevaluatetheexpressionx + y,wherexisaninstanceofaclass
thathasan__add__()method,type(x).__add__(x, y)iscalled. The__divmod__()methodshould
3.3. Specialmethodnames 57

### 第66页

betheequivalenttousing__floordiv__()and__mod__();itshouldnotberelatedto__truediv__().
Notethat__pow__()shouldbedefinedtoacceptanoptionalthirdargumentifthethree-argumentversionof
thebuilt-inpow()functionistobesupported.
If one of those methods does not support the operation with the supplied arguments, it should return
NotImplemented.
object.__radd__(self,other)
object.__rsub__(self,other)
object.__rmul__(self,other)
object.__rmatmul__(self,other)
object.__rtruediv__(self,other)
object.__rfloordiv__(self,other)
object.__rmod__(self,other)
object.__rdivmod__(self,other)
[ ]
object.__rpow__(self,other ,modulo )
object.__rlshift__(self,other)
object.__rrshift__(self,other)
object.__rand__(self,other)
object.__rxor__(self,other)
object.__ror__(self,other)
These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(),
pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the
operandsareofdifferenttypes,whentheleftoperanddoesnotsupportthecorrespondingoperation3,orthe
rightoperand’sclassisderivedfromtheleftoperand’sclass.4 Forinstance,toevaluatetheexpressionx - y,
whereyisaninstanceofaclassthathasan__rsub__()method,type(y).__rsub__(y, x)iscalledif
type(x).__sub__(x, y)returnsNotImplementedortype(y)isasubclassoftype(x).5
Notethat__rpow__()shouldbedefinedtoacceptanoptionalthirdargumentifthethree-argumentversion
ofthebuilt-inpow()functionistobesupported.
Changedinversion3.14: Three-argumentpow()nowtrycalling__rpow__()ifnecessary. Previouslyitwas
onlycalledintwo-argumentpow()andthebinarypoweroperator.
(cid:174) Note
Iftherightoperand’stypeisasubclassoftheleftoperand’stypeandthatsubclassprovidesadifferentim-
plementationofthereflectedmethodfortheoperation,thismethodwillbecalledbeforetheleftoperand’s
non-reflectedmethod. Thisbehaviorallowssubclassestooverridetheirancestors’operations.
object.__iadd__(self,other)
object.__isub__(self,other)
object.__imul__(self,other)
object.__imatmul__(self,other)
object.__itruediv__(self,other)
object.__ifloordiv__(self,other)
object.__imod__(self,other)
[ ]
object.__ipow__(self,other ,modulo )
3“Doesnotsupport”heremeansthattheclasshasnosuchmethod,orthemethodreturnsNotImplemented.DonotsetthemethodtoNone
ifyouwanttoforcefallbacktotherightoperand’sreflectedmethod—thatwillinsteadhavetheoppositeeffectofexplicitlyblockingsuchfallback.
4Foroperandsofthesametype,itisassumedthatifthenon-reflectedmethod(suchas__add__())failsthentheoperationisnotsupported,
whichiswhythereflectedmethodisnotcalled.
5Iftherightoperand’stypeisasubclassoftheleftoperand’stype,thereflectedmethodhavingprecedenceallowssubclassestooverridetheir
ancestors’operations.
58 Chapter3. Datamodel

### 第67页

object.__ilshift__(self,other)
object.__irshift__(self,other)
object.__iand__(self,other)
object.__ixor__(self,other)
object.__ior__(self,other)
Thesemethodsarecalledtoimplementtheaugmentedarithmeticassignments(+=,-=,*=,@=,/=,//=,%=,
**=,<<=,>>=,&=,^=,|=). Thesemethodsshouldattempttodotheoperationin-place(modifyingself)and
returntheresult(whichcouldbe,butdoesnothavetobe,self). Ifaspecificmethodisnotdefined,orifthat
methodreturnsNotImplemented,theaugmentedassignmentfallsbacktothenormalmethods. Forinstance,
ifx isaninstanceofaclasswithan__iadd__()method, x += yisequivalenttox = x.__iadd__(y)
. If__iadd__()doesnotexist,orifx.__iadd__(y)returnsNotImplemented,x.__add__(y)andy.
__radd__(x)areconsidered,aswiththeevaluationofx + y. Incertainsituations,augmentedassignment
canresultinunexpectederrors(seefaq-augmented-assignment-tuple-error),butthisbehaviorisinfactpartof
thedatamodel.
object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)
Calledtoimplementtheunaryarithmeticoperations(-,+,abs()and~).
object.__complex__(self)
object.__int__(self)
object.__float__(self)
Calledtoimplementthebuilt-infunctionscomplex(), int()andfloat(). Shouldreturnavalueofthe
appropriatetype.
object.__index__(self)
Called to implement operator.index(), and whenever Python needs to losslessly convert the numeric
objecttoanintegerobject(suchasinslicing,orinthebuilt-inbin(),hex()andoct()functions). Presence
ofthismethodindicatesthatthenumericobjectisanintegertype. Mustreturnaninteger.
If __int__(), __float__() and __complex__() are not defined then corresponding built-in functions
int(),float()andcomplex()fallbackto__index__().
[ ]
object.__round__(self ,ndigits )
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)
Called to implement the built-in function round() and math functions trunc(), floor() and ceil().
Unlessndigitsispassedto__round__()allthesemethodsshouldreturnthevalueoftheobjecttruncatedto
anIntegral(typicallyanint).
Changedinversion3.14: int()nolongerdelegatestothe__trunc__()method.
3.3.9 With Statement Context Managers
Acontextmanagerisanobjectthatdefinestheruntimecontexttobeestablishedwhenexecutingawithstatement.
Thecontextmanagerhandlestheentryinto,andtheexitfrom,thedesiredruntimecontextfortheexecutionofthe
block of code. Context managers are normally invoked using the with statement (described in section The with
statement),butcanalsobeusedbydirectlyinvokingtheirmethods.
Typicalusesofcontextmanagersincludesavingandrestoringvariouskindsofglobalstate,lockingandunlocking
resources,closingopenedfiles,etc.
Formoreinformationoncontextmanagers,seetypecontextmanager. Theobjectclassitselfdoesnotprovidethe
contextmanagermethods.
3.3. Specialmethodnames 59

### 第68页

object.__enter__(self)
Entertheruntimecontextrelatedtothisobject. Thewithstatementwillbindthismethod’sreturnvalueto
thetarget(s)specifiedintheasclauseofthestatement,ifany.
object.__exit__(self,exc_type,exc_value,traceback)
Exittheruntimecontextrelatedtothisobject. Theparametersdescribetheexceptionthatcausedthecontext
tobeexited. Ifthecontextwasexitedwithoutanexception,allthreeargumentswillbeNone.
Ifanexceptionissupplied,andthemethodwishestosuppresstheexception(i.e.,preventitfrombeingprop-
agated),itshouldreturnatruevalue. Otherwise,theexceptionwillbeprocessednormallyuponexitfromthis
method.
Notethat__exit__()methodsshouldnotreraisethepassed-inexception;thisisthecaller’sresponsibility.
(cid:181) Seealso
PEP343-The“with”statement
Thespecification,background,andexamplesforthePythonwithstatement.
3.3.10 Customizing positional arguments in class pattern matching
When using a class name in a pattern, positional arguments in the pattern are not allowed by default, i.e. case
MyClass(x, y)istypicallyinvalidwithoutspecialsupportinMyClass. Tobeabletousethatkindofpattern,the
classneedstodefinea__match_args__attribute.
object.__match_args__
Thisclassvariablecanbeassignedatupleofstrings. Whenthisclassisusedinaclasspatternwithpositional
arguments,eachpositionalargumentwillbeconvertedintoakeywordargument,usingthecorrespondingvalue
in__match_args__asthekeyword. Theabsenceofthisattributeisequivalenttosettingitto().
For example, if MyClass.__match_args__ is ("left", "center", "right") that means that case
MyClass(x, y) is equivalent to case MyClass(left=x, center=y). Note that the number of arguments
inthepatternmustbesmallerthanorequaltothenumberofelementsin__match_args__;ifitislarger,thepattern
matchattemptwillraiseaTypeError.
Addedinversion3.10.
(cid:181) Seealso
PEP634-StructuralPatternMatching
ThespecificationforthePythonmatchstatement.
3.3.11 Emulating buffer types
ThebufferprotocolprovidesawayforPythonobjectstoexposeefficientaccesstoalow-levelmemoryarray. This
protocol is implemented by builtin types such as bytes and memoryview, and third-party libraries may define
additionalbuffertypes.
WhilebuffertypesareusuallyimplementedinC,itisalsopossibletoimplementtheprotocolinPython.
object.__buffer__(self,flags)
Calledwhenabufferisrequestedfromself(forexample,bythememoryviewconstructor). Theflagsargument
isanintegerrepresentingthekindofbufferrequested,affectingforexamplewhetherthereturnedbufferisread-
onlyorwritable. inspect.BufferFlagsprovidesaconvenientwaytointerprettheflags. Themethodmust
returnamemoryviewobject.
object.__release_buffer__(self,buffer)
Calledwhenabufferisnolongerneeded. Thebufferargumentisamemoryviewobjectthatwaspreviously
returnedby__buffer__(). Themethodmustreleaseanyresourcesassociatedwiththebuffer. Thismethod
60 Chapter3. Datamodel

| (cid:181) Seealso |
| --- |
| PEP343-The“with”statement
Thespecification,background,andexamplesforthePythonwithstatement. |


| (cid:181) Seealso |
| --- |
| PEP634-StructuralPatternMatching
ThespecificationforthePythonmatchstatement. |

### 第69页

shouldreturnNone. Bufferobjectsthatdonotneedtoperformanycleanuparenotrequiredtoimplementthis
method.
Addedinversion3.12.
(cid:181) Seealso
PEP688-MakingthebufferprotocolaccessibleinPython
IntroducesthePython__buffer__and__release_buffer__methods.
collections.abc.Buffer
ABCforbuffertypes.
3.3.12 Annotations
Functions,classes,andmodulesmaycontainannotations,whichareawaytoassociateinformation(usuallytypehints)
withasymbol.
object.__annotations__
Thisattributecontainstheannotationsforanobject. Itislazilyevaluated,soaccessingtheattributemayexecute
arbitrarycodeandraiseexceptions. Ifevaluationissuccessful,theattributeissettoadictionarymappingfrom
variablenamestoannotations.
Changedinversion3.14: Annotationsarenowlazilyevaluated.
object.__annotate__(format)
Anannotatefunction. Returnsanewdictionaryobjectmappingattribute/parameternamestotheirannotation
values.
Takesaformatparameterspecifyingtheformatinwhichannotationsvaluesshouldbeprovided. Itmustbe
amemberoftheannotationlib.Formatenum,oranintegerwithavaluecorrespondingtoamemberof
theenum.
Ifanannotatefunctiondoesn’tsupporttherequestedformat,itmustraiseNotImplementedError. Annotate
functions must always support VALUE format; they must not raise NotImplementedError() when called
withthisformat.
WhencalledwithVALUEformat,anannotatefunctionmayraiseNameError;itmustnotraiseNameError
whencalledrequestinganyotherformat.
If an object does not have any annotations, __annotate__ should preferably be set to None (it can’t be
deleted),ratherthansettoafunctionthatreturnsanemptydict.
Addedinversion3.14.
(cid:181) Seealso
PEP649—Deferredevaluationofannotationusingdescriptors
Introduceslazyevaluationofannotationsandthe__annotate__function.
3.3.13 Special method lookup
Forcustomclasses, implicitinvocationsofspecialmethodsareonlyguaranteedtoworkcorrectlyifdefinedonan
object’stype,notintheobject’sinstancedictionary. Thatbehaviouristhereasonwhythefollowingcoderaisesan
exception:
>>> class C:
... pass
...
>>> c = C()
(continuesonnextpage)
3.3. Specialmethodnames 61

| (cid:181) Seealso |
| --- |
| PEP688-MakingthebufferprotocolaccessibleinPython
IntroducesthePython__buffer__and__release_buffer__methods.
collections.abc.Buffer
ABCforbuffertypes. |


| (cid:181) Seealso |
| --- |
| PEP649—Deferredevaluationofannotationusingdescriptors
Introduceslazyevaluationofannotationsandthe__annotate__function. |

### 第70页

(continuedfrompreviouspage)
>>> c.__len__ = lambda: 5
>>> len(c)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()
Therationalebehindthisbehaviourlieswithanumberofspecialmethodssuchas__hash__()and__repr__()
thatareimplementedbyallobjects, includingtypeobjects. Iftheimplicitlookupofthesemethodsusedthecon-
ventionallookupprocess,theywouldfailwheninvokedonthetypeobjectitself:
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument
Incorrectly attempting to invoke an unbound method of a class in this way is sometimes referred to as ‘metaclass
confusion’,andisavoidedbybypassingtheinstancewhenlookingupspecialmethods:
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True
Inadditiontobypassinganyinstanceattributesintheinterestofcorrectness,implicitspecialmethodlookupgenerally
alsobypassesthe__getattribute__()methodevenoftheobject’smetaclass:
>>> class Meta(type):
... def __getattribute__(*args):
... print("Metaclass getattribute invoked")
... return type.__getattribute__(*args)
...
>>> class C(object, metaclass=Meta):
... def __len__(self):
... return 10
... def __getattribute__(*args):
... print("Class getattribute invoked")
... return object.__getattribute__(*args)
...
>>> c = C()
>>> c.__len__() # Explicit lookup via instance
Class getattribute invoked
10
>>> type(c).__len__(c) # Explicit lookup via type
Metaclass getattribute invoked
10
>>> len(c) # Implicit lookup
10
Bypassingthe__getattribute__()machineryinthisfashionprovidessignificantscopeforspeedoptimisations
withintheinterpreter,atthecostofsomeflexibilityinthehandlingofspecialmethods(thespecialmethodmustbe
setontheclassobjectitselfinordertobeconsistentlyinvokedbytheinterpreter).
62 Chapter3. Datamodel

### 第71页

3.4 Coroutines
3.4.1 Awaitable Objects
Anawaitableobjectgenerallyimplementsan__await__()method. Coroutineobjectsreturnedfromasync def
functionsareawaitable.
(cid:174) Note
Thegeneratoriteratorobjectsreturnedfromgeneratorsdecoratedwithtypes.coroutine()arealsoawaitable,
buttheydonotimplement__await__().
object.__await__(self)
Must return an iterator. Should be used to implement awaitable objects. For instance, asyncio.Future
implementsthismethodtobecompatiblewiththeawaitexpression. Theobjectclassitselfisnotawaitable
anddoesnotprovidethismethod.
(cid:174) Note
Thelanguagedoesn’tplaceanyrestrictiononthetypeorvalueoftheobjectsyieldedbytheiteratorreturned
by__await__, asthisisspecifictotheimplementationoftheasynchronousexecutionframework(e.g.
asyncio)thatwillbemanagingtheawaitableobject.
Addedinversion3.5.
(cid:181) Seealso
PEP492foradditionalinformationaboutawaitableobjects.
3.4.2 Coroutine Objects
Coroutine objects are awaitable objects. A coroutine’s execution can be controlled by calling __await__() and
iteratingovertheresult. Whenthecoroutinehasfinishedexecutingandreturns,theiteratorraisesStopIteration,
andtheexception’svalueattributeholdsthereturnvalue. Ifthecoroutineraisesanexception,itispropagatedby
theiterator. CoroutinesshouldnotdirectlyraiseunhandledStopIterationexceptions.
Coroutines also have the methods listed below, which are analogous to those of generators (see Generator-iterator
methods). However,unlikegenerators,coroutinesdonotdirectlysupportiteration.
Changedinversion3.5.2: ItisaRuntimeErrortoawaitonacoroutinemorethanonce.
coroutine.send(value)
Starts or resumes execution of the coroutine. If value is None, this is equivalent to advancing the iterator
returnedby__await__(). IfvalueisnotNone,thismethoddelegatestothesend()methodoftheiterator
that caused the coroutine to suspend. The result (return value, StopIteration, or other exception) is the
sameaswheniteratingoverthe__await__()returnvalue,describedabove.
coroutine.throw(value)
[ [ ]]
coroutine.throw(type ,value ,traceback )
Raisesthespecifiedexceptioninthecoroutine. Thismethoddelegatestothethrow()methodoftheiterator
thatcausedthecoroutinetosuspend,ifithassuchamethod. Otherwise,theexceptionisraisedatthesuspen-
sionpoint. Theresult(returnvalue,StopIteration,orotherexception)isthesameaswheniteratingover
the__await__()returnvalue,describedabove. Iftheexceptionisnotcaughtinthecoroutine,itpropagates
backtothecaller.
Changedinversion3.12: Thesecondsignature(type[,value[,traceback]])isdeprecatedandmayberemoved
inafutureversionofPython.
3.4. Coroutines 63

| (cid:181) Seealso |
| --- |
| PEP492foradditionalinformationaboutawaitableobjects. |

### 第72页

coroutine.close()
Causesthecoroutinetocleanitselfupandexit. Ifthecoroutineissuspended,thismethodfirstdelegatestothe
close()methodoftheiteratorthatcausedthecoroutinetosuspend,ifithassuchamethod. Thenitraises
GeneratorExit at the suspension point, causing the coroutine to immediately clean itself up. Finally, the
coroutineismarkedashavingfinishedexecuting,evenifitwasneverstarted.
Coroutineobjectsareautomaticallyclosedusingtheaboveprocesswhentheyareabouttobedestroyed.
3.4.3 Asynchronous Iterators
Anasynchronousiteratorcancallasynchronouscodeinits__anext__method.
Asynchronousiteratorscanbeusedinanasync forstatement.
Theobjectclassitselfdoesnotprovidethesemethods.
object.__aiter__(self)
Mustreturnanasynchronousiteratorobject.
object.__anext__(self)
Mustreturnanawaitableresultinginanextvalueoftheiterator. ShouldraiseaStopAsyncIterationerror
whentheiterationisover.
Anexampleofanasynchronousiterableobject:
class Reader:
async def readline(self):
...
def __aiter__(self):
return self
async def __anext__(self):
val = await self.readline()
if val == b'':
raise StopAsyncIteration
return val
Addedinversion3.5.
Changed in version 3.7: Prior to Python 3.7, __aiter__() could return an awaitable that would resolve to an
asynchronousiterator.
StartingwithPython3.7,__aiter__()mustreturnanasynchronousiteratorobject. Returninganythingelsewill
resultinaTypeErrorerror.
3.4.4 Asynchronous Context Managers
An asynchronous context manager is a context manager that is able to suspend execution in its __aenter__ and
__aexit__methods.
Asynchronouscontextmanagerscanbeusedinanasync withstatement.
Theobjectclassitselfdoesnotprovidethesemethods.
object.__aenter__(self)
Semanticallysimilarto__enter__(),theonlydifferencebeingthatitmustreturnanawaitable.
object.__aexit__(self,exc_type,exc_value,traceback)
Semanticallysimilarto__exit__(),theonlydifferencebeingthatitmustreturnanawaitable.
Anexampleofanasynchronouscontextmanagerclass:
64 Chapter3. Datamodel

### 第73页

class AsyncContextManager:
async def __aenter__(self):
await log('entering context')
async def __aexit__(self, exc_type, exc, tb):
await log('exiting context')
Addedinversion3.5.
3.4. Coroutines 65

### 第74页

66 Chapter3. Datamodel

### 第75页

CHAPTER
FOUR
EXECUTION MODEL
4.1 Structure of a program
APythonprogramisconstructedfromcodeblocks. AblockisapieceofPythonprogramtextthatisexecutedasa
unit. Thefollowingareblocks: amodule,afunctionbody,andaclassdefinition. Eachcommandtypedinteractively
isablock. Ascriptfile(afilegivenasstandardinputtotheinterpreterorspecifiedasacommandlineargumentto
theinterpreter)isacodeblock. Ascriptcommand(acommandspecifiedontheinterpretercommandlinewiththe
-coption)isacodeblock. Amodulerunasatoplevelscript(asmodule__main__)fromthecommandlineusing
a-margumentisalsoacodeblock. Thestringargumentpassedtothebuilt-infunctionseval()andexec()isa
codeblock.
Acodeblockisexecutedinanexecutionframe. Aframecontainssomeadministrativeinformation(usedfordebug-
ging)anddetermineswhereandhowexecutioncontinuesafterthecodeblock’sexecutionhascompleted.
4.2 Naming and binding
4.2.1 Binding of names
Namesrefertoobjects. Namesareintroducedbynamebindingoperations.
Thefollowingconstructsbindnames:
• formalparameterstofunctions,
• classdefinitions,
• functiondefinitions,
• assignmentexpressions,
• targetsthatareidentifiersifoccurringinanassignment:
– forloopheader,
– afterasinawithstatement,exceptclause,except*clause,orintheas-patterninstructuralpattern
matching,
– inacapturepatterninstructuralpatternmatching
• importstatements.
• typestatements.
• typeparameterlists.
Theimportstatementoftheformfrom ... import *bindsallnamesdefinedintheimportedmodule,except
thosebeginningwithanunderscore. Thisformmayonlybeusedatthemodulelevel.
Atargetoccurringinadelstatementisalsoconsideredboundforthispurpose(thoughtheactualsemanticsareto
unbindthename).
Eachassignmentorimportstatementoccurswithinablockdefinedbyaclassorfunctiondefinitionoratthemodule
level(thetop-levelcodeblock).
67

### 第76页

Ifanameisboundinablock,itisalocalvariableofthatblock,unlessdeclaredasnonlocalorglobal. Ifaname
isboundatthemodulelevel,itisaglobalvariable. (Thevariablesofthemodulecodeblockarelocalandglobal.) If
avariableisusedinacodeblockbutnotdefinedthere,itisafreevariable.
Eachoccurrenceofanameintheprogramtextreferstothebindingofthatnameestablishedbythefollowingname
resolutionrules.
4.2.2 Resolution of names
Ascopedefinesthevisibilityofanamewithinablock. Ifalocalvariableisdefinedinablock,itsscopeincludesthat
block. Ifthedefinitionoccursinafunctionblock,thescopeextendstoanyblockscontainedwithinthedefiningone,
unlessacontainedblockintroducesadifferentbindingforthename.
When a name is used in a code block, it is resolved using the nearest enclosing scope. The set of all such scopes
visibletoacodeblockiscalledtheblock’senvironment.
When a name is not found at all, a NameError exception is raised. If the current scope is a function scope, and
the name refers to a local variable that has not yet been bound to a value at the point where the name is used, an
UnboundLocalErrorexceptionisraised. UnboundLocalErrorisasubclassofNameError.
Ifanamebindingoperationoccursanywherewithinacodeblock,allusesofthenamewithintheblockaretreated
asreferencestothecurrentblock. Thiscanleadtoerrorswhenanameisusedwithinablockbeforeitisbound. This
ruleissubtle. Pythonlacksdeclarationsandallowsnamebindingoperationstooccuranywherewithinacodeblock.
The local variables of a code block can be determined by scanning the entire text of the block for name binding
operations. SeetheFAQentryonUnboundLocalErrorforexamples.
Iftheglobalstatementoccurswithinablock,allusesofthenamesspecifiedinthestatementrefertothebindings
ofthosenamesinthetop-levelnamespace. Namesareresolvedinthetop-levelnamespacebysearchingtheglobal
namespace,i.e. thenamespaceofthemodulecontainingthecodeblock,andthebuiltinsnamespace,thenamespace
of the module builtins. The global namespace is searched first. If the names are not found there, the builtins
namespaceissearchednext. Ifthenamesarealsonotfoundinthebuiltinsnamespace,newvariablesarecreatedin
theglobalnamespace. Theglobalstatementmustprecedeallusesofthelistednames.
Theglobalstatementhasthesamescopeasanamebindingoperationinthesameblock. Ifthenearestenclosing
scopeforafreevariablecontainsaglobalstatement,thefreevariableistreatedasaglobal.
Thenonlocalstatementcausescorrespondingnamestorefertopreviouslyboundvariablesinthenearestenclosing
functionscope. SyntaxErrorisraisedatcompiletimeifthegivennamedoesnotexistinanyenclosingfunction
scope. Typeparameterscannotbereboundwiththenonlocalstatement.
Thenamespaceforamoduleisautomaticallycreatedthefirsttimeamoduleisimported. Themainmodulefora
scriptisalwayscalled__main__.
Classdefinitionblocksandargumentstoexec()andeval()arespecialinthecontextofnameresolution. Aclass
definitionisanexecutablestatementthatmayuseanddefinenames. Thesereferencesfollowthenormalrulesforname
resolution with an exception that unbound local variables are looked up in the global namespace. The namespace
of the class definition becomes the attribute dictionary of the class. The scope of names defined in a class block
islimitedtotheclassblock; itdoesnotextendtothecodeblocksofmethods. Thisincludescomprehensionsand
generatorexpressions, butitdoesnotincludeannotationscopes, whichhaveaccesstotheirenclosingclassscopes.
Thismeansthatthefollowingwillfail:
class A:
a = 42
b = list(a + i for i in range(10))
However,thefollowingwillsucceed:
class A:
type Alias = Nested
class Nested: pass
print(A.Alias.__value__) # <type 'A.Nested'>
68 Chapter4. Executionmodel

### 第77页

4.2.3 Annotation scopes
Annotations,typeparameterlistsandtypestatementsintroduceannotationscopes,whichbehavemostlylikefunction
scopes,butwithsomeexceptionsdiscussedbelow.
Annotationscopesareusedinthefollowingcontexts:
• Functionannotations.
• Variableannotations.
• Typeparameterlistsforgenerictypealiases.
• Typeparameterlistsforgenericfunctions. Agenericfunction’sannotationsareexecutedwithintheannotation
scope,butitsdefaultsanddecoratorsarenot.
• Typeparameterlistsforgenericclasses. Agenericclass’sbaseclassesandkeywordargumentsareexecuted
withintheannotationscope,butitsdecoratorsarenot.
• Thebounds,constraints,anddefaultvaluesfortypeparameters(lazilyevaluated).
• Thevalueoftypealiases(lazilyevaluated).
Annotationscopesdifferfromfunctionscopesinthefollowingways:
• Annotation scopes have access to their enclosing class namespace. If an annotation scope is immediately
withinaclassscope,orwithinanotherannotationscopethatisimmediatelywithinaclassscope,thecodein
theannotationscopecanusenamesdefinedintheclassscopeasifitwereexecuteddirectlywithintheclass
body. Thiscontrastswithregularfunctionsdefinedwithinclasses,whichcannotaccessnamesdefinedinthe
classscope.
• Expressions in annotation scopes cannot contain yield, yield from, await, or := expressions. (These
expressionsareallowedinotherscopescontainedwithintheannotationscope.)
• Names defined in annotation scopes cannot be rebound with nonlocal statements in inner scopes. This
includes only type parameters, as no other syntactic elements that can appear within annotation scopes can
introducenewnames.
• While annotation scopes have an internal name, that name is not reflected in the qualified name of objects
definedwithinthescope. Instead,the__qualname__ofsuchobjectsisasiftheobjectweredefinedinthe
enclosingscope.
Addedinversion3.12: AnnotationscopeswereintroducedinPython3.12aspartofPEP695.
Changedinversion3.13: Annotationscopesarealsousedfortypeparameterdefaults,asintroducedbyPEP696.
Changedinversion3.14: Annotationscopesarenowalsousedforannotations, asspecifiedinPEP649andPEP
749.
4.2.4 Lazy evaluation
Mostannotationscopesarelazilyevaluated. Thisincludesannotations,thevaluesoftypealiasescreatedthroughthe
typestatement,andthebounds,constraints,anddefaultvaluesoftypevariablescreatedthroughthetypeparameter
syntax. This means that they are not evaluated when the type alias or type variable is created, or when the object
carryingannotationsiscreated. Instead,theyareonlyevaluatedwhennecessary,forexamplewhenthe__value__
attributeonatypealiasisaccessed.
Example:
>>> type Alias = 1/0
>>> Alias.__value__
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
>>> def func[T: 1/0](): pass
>>> T = func.__type_params__[0]
(continuesonnextpage)
4.2. Namingandbinding 69

### 第78页

(continuedfrompreviouspage)
>>> T.__bound__
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
Heretheexceptionisraisedonlywhenthe__value__attributeofthetypealiasorthe__bound__attributeofthe
typevariableisaccessed.
Thisbehaviorisprimarilyusefulforreferencestotypesthathavenotyetbeendefinedwhenthetypealiasortype
variableiscreated. Forexample,lazyevaluationenablescreationofmutuallyrecursivetypealiases:
from typing import Literal
type SimpleExpr = int | Parenthesized
type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]
Lazily evaluated values are evaluated in annotation scope, which means that names that appear inside the lazily
evaluatedvaluearelookedupasiftheywereusedintheimmediatelyenclosingscope.
Addedinversion3.12.
4.2.5 Builtins and restricted execution
CPythonimplementationdetail: Usersshouldnottouch__builtins__; itisstrictlyanimplementationdetail.
Users wanting to override values in the builtins namespace should import the builtins module and modify its
attributesappropriately.
The builtins namespace associated with the execution of a code block is actually found by looking up the name
__builtins__ in its global namespace; this should be a dictionary or a module (in the latter case the module’s
dictionaryisused). Bydefault,wheninthe__main__module,__builtins__isthebuilt-inmodulebuiltins;
wheninanyothermodule,__builtins__isanaliasforthedictionaryofthebuiltinsmoduleitself.
4.2.6 Interaction with dynamic features
Nameresolutionoffreevariablesoccursatruntime, notatcompiletime. Thismeansthatthefollowingcodewill
print42:
i = 10
def f():
print(i)
i = 42
f()
Theeval()andexec()functionsdonothaveaccesstothefullenvironmentforresolvingnames. Namesmaybe
resolved in the local and global namespaces of the caller. Free variables are not resolved in the nearest enclosing
namespace,butintheglobalnamespace.1 Theexec()andeval()functionshaveoptionalargumentstooverride
theglobalandlocalnamespace. Ifonlyonenamespaceisspecified,itisusedforboth.
4.3 Exceptions
Exceptionsareameansofbreakingoutofthenormalflowofcontrolofacodeblockinordertohandleerrorsor
otherexceptionalconditions. Anexceptionisraised atthepointwheretheerrorisdetected;itmaybehandled by
thesurroundingcodeblockorbyanycodeblockthatdirectlyorindirectlyinvokedthecodeblockwheretheerror
occurred.
1Thislimitationoccursbecausethecodethatisexecutedbytheseoperationsisnotavailableatthetimethemoduleiscompiled.
70 Chapter4. Executionmodel

### 第79页

The Python interpreter raises an exception when it detects a run-time error (such as division by zero). A Python
programcanalsoexplicitlyraiseanexceptionwiththeraisestatement. Exceptionhandlersarespecifiedwiththe
try…exceptstatement. Thefinallyclauseofsuchastatementcanbeusedtospecifycleanupcodewhichdoes
nothandletheexception,butisexecutedwhetheranexceptionoccurredornotintheprecedingcode.
Pythonusesthe“termination”modeloferrorhandling:anexceptionhandlercanfindoutwhathappenedandcontinue
executionatanouterlevel,butitcannotrepairthecauseoftheerrorandretrythefailingoperation(exceptbyre-
enteringtheoffendingpieceofcodefromthetop).
Whenanexceptionisnothandledatall,theinterpreterterminatesexecutionoftheprogram,orreturnstoitsinter-
activemainloop. Ineithercase,itprintsastacktraceback,exceptwhentheexceptionisSystemExit.
Exceptionsareidentifiedbyclassinstances. Theexceptclauseisselecteddependingontheclassoftheinstance:
itmustreferencetheclassoftheinstanceoranon-virtualbaseclass thereof. Theinstancecanbereceivedbythe
handlerandcancarryadditionalinformationabouttheexceptionalcondition.
(cid:174) Note
Exception messages are not part of the Python API. Their contents may change from one version of Python
tothenextwithoutwarningandshouldnotbereliedonbycodewhichwillrunundermultipleversionsofthe
interpreter.
SeealsothedescriptionofthetrystatementinsectionThetrystatementandraisestatementinsectionTheraise
statement.
4.3. Exceptions 71

### 第80页

72 Chapter4. Executionmodel

### 第81页

CHAPTER
FIVE
THE IMPORT SYSTEM
Pythoncodeinonemodulegainsaccesstothecodeinanothermodulebytheprocessofimportingit. Theimport
statementisthemostcommonwayofinvokingtheimportmachinery,butitisnottheonlyway. Functionssuchas
importlib.import_module()andbuilt-in__import__()canalsobeusedtoinvoketheimportmachinery.
The import statement combines two operations; it searches for the named module, then it binds the results of
thatsearchtoanameinthelocalscope. Thesearchoperationoftheimportstatementisdefinedasacalltothe
__import__()function,withtheappropriatearguments. Thereturnvalueof__import__()isusedtoperform
thenamebindingoperationoftheimportstatement. Seetheimportstatementfortheexactdetailsofthatname
bindingoperation.
A direct call to __import__() performs only the module search and, if found, the module creation operation.
Whilecertainside-effectsmayoccur,suchastheimportingofparentpackages,andtheupdatingofvariouscaches
(includingsys.modules),onlytheimportstatementperformsanamebindingoperation.
Whenanimportstatementisexecuted,thestandardbuiltin__import__()functioniscalled. Othermechanisms
forinvokingtheimportsystem(suchasimportlib.import_module())maychoosetobypass__import__()
andusetheirownsolutionstoimplementimportsemantics.
Whenamoduleisfirstimported,Pythonsearchesforthemoduleandiffound,itcreatesamoduleobject1,initializing
it. Ifthenamedmodulecannotbefound,aModuleNotFoundErrorisraised. Pythonimplementsvariousstrategies
tosearchforthenamedmodulewhentheimportmachineryisinvoked. Thesestrategiescanbemodifiedandextended
byusingvarioushooksdescribedinthesectionsbelow.
Changed in version 3.3: The import system has been updated to fully implement the second phase of PEP 302.
Thereisnolongeranyimplicitimportmachinery-thefullimportsystemisexposedthroughsys.meta_path. In
addition,nativenamespacepackagesupporthasbeenimplemented(seePEP420).
5.1 importlib
The importlib module provides a rich API for interacting with the import system. For example importlib.
import_module()providesarecommended, simplerAPIthanbuilt-in__import__()forinvokingtheimport
machinery. Refertotheimportliblibrarydocumentationforadditionaldetail.
5.2 Packages
Python has only one type of module object, and all modules are of this type, regardless of whether the module is
implementedinPython, C, orsomethingelse. Tohelporganizemodulesandprovidea naminghierarchy, Python
hasaconceptofpackages.
Youcanthinkofpackagesasthedirectoriesonafilesystemandmodulesasfileswithindirectories,butdon’ttake
thisanalogytooliterallysincepackagesandmodulesneednotoriginatefromthefilesystem. Forthepurposesof
thisdocumentation,we’llusethisconvenientanalogyofdirectoriesandfiles. Likefilesystemdirectories,packages
areorganizedhierarchically,andpackagesmaythemselvescontainsubpackages,aswellasregularmodules.
1Seetypes.ModuleType.
73

### 第82页

It’simportanttokeepinmindthatallpackagesaremodules,butnotallmodulesarepackages. Orputanotherway,
packagesarejustaspecialkindofmodule. Specifically,anymodulethatcontainsa__path__attributeisconsidered
apackage.
Allmoduleshaveaname. Subpackagenamesareseparatedfromtheirparentpackagenamebyadot,akintoPython’s
standardattributeaccesssyntax. Thusyoumighthaveapackagecalledemail,whichinturnhasasubpackagecalled
email.mimeandamodulewithinthatsubpackagecalledemail.mime.text.
5.2.1 Regular packages
Pythondefinestwotypesofpackages,regularpackagesandnamespacepackages. Regularpackagesaretraditional
packagesastheyexistedinPython3.2andearlier. Aregularpackageistypicallyimplementedasadirectorycon-
tainingan__init__.pyfile. Whenaregularpackageisimported,this__init__.pyfileisimplicitlyexecuted,
andtheobjectsitdefinesareboundtonamesinthepackage’snamespace. The__init__.pyfilecancontainthe
samePythoncodethatanyothermodulecancontain,andPythonwilladdsomeadditionalattributestothemodule
whenitisimported.
Forexample,thefollowingfilesystemlayoutdefinesatoplevelparentpackagewiththreesubpackages:
parent/
__init__.py
one/
__init__.py
two/
__init__.py
three/
__init__.py
Importingparent.onewillimplicitlyexecuteparent/__init__.pyandparent/one/__init__.py. Subse-
quentimportsofparent.twoorparent.threewillexecuteparent/two/__init__.pyandparent/three/
__init__.pyrespectively.
5.2.2 Namespace packages
Anamespacepackageisacompositeofvariousportions,whereeachportioncontributesasubpackagetotheparent
package. Portionsmayresideindifferentlocationsonthefilesystem. Portionsmayalsobefoundinzipfiles,onthe
network, or anywhere else that Python searches during import. Namespace packages may or may not correspond
directlytoobjectsonthefilesystem;theymaybevirtualmodulesthathavenoconcreterepresentation.
Namespacepackagesdonotuseanordinarylistfortheir__path__attribute. Theyinsteaduseacustomiterabletype
whichwillautomaticallyperformanewsearchforpackageportionsonthenextimportattemptwithinthatpackage
ifthepathoftheirparentpackage(orsys.pathforatoplevelpackage)changes.
Withnamespacepackages,thereisnoparent/__init__.pyfile. Infact,theremaybemultipleparentdirectories
found during import search, where each one is provided by a different portion. Thus parent/one may not be
physically located next to parent/two. In this case, Python will create a namespace package for the top-level
parentpackagewheneveritoroneofitssubpackagesisimported.
SeealsoPEP420forthenamespacepackagespecification.
5.3 Searching
Tobeginthesearch,Pythonneedsthefullyqualified nameofthemodule(orpackage,butforthepurposesofthis
discussion,thedifferenceisimmaterial)beingimported. Thisnamemaycomefromvariousargumentstotheimport
statement,orfromtheparameterstotheimportlib.import_module()or__import__()functions.
Thisnamewillbeusedinvariousphasesoftheimportsearch, anditmaybethedottedpathtoasubmodule, e.g.
foo.bar.baz. Inthiscase,Pythonfirsttriestoimportfoo,thenfoo.bar,andfinallyfoo.bar.baz. Ifanyof
theintermediateimportsfail,aModuleNotFoundErrorisraised.
74 Chapter5. Theimportsystem

### 第83页

5.3.1 The module cache
Thefirstplacecheckedduringimportsearchissys.modules. Thismappingservesasacacheofallmodulesthat
have been previously imported, including the intermediate paths. So if foo.bar.baz was previously imported,
sys.modules will contain entries for foo, foo.bar, and foo.bar.baz. Each key will have as its value the
correspondingmoduleobject.
Duringimport,themodulenameislookedupinsys.modulesandifpresent,theassociatedvalueisthemodule
satisfyingtheimport,andtheprocesscompletes. However,ifthevalueisNone,thenaModuleNotFoundErroris
raised. Ifthemodulenameismissing,Pythonwillcontinuesearchingforthemodule.
sys.modulesiswritable. Deletingakeymaynotdestroytheassociatedmodule(asothermodulesmayholdrefer-
encestoit),butitwillinvalidatethecacheentryforthenamedmodule,causingPythontosearchanewforthenamed
moduleuponitsnextimport. ThekeycanalsobeassignedtoNone,forcingthenextimportofthemoduletoresult
inaModuleNotFoundError.
Bewarethough,asifyoukeepareferencetothemoduleobject,invalidateitscacheentryinsys.modules,andthen
re-import the named module, the two module objects will not be the same. By contrast, importlib.reload()
willreusethesamemoduleobject,andsimplyreinitialisethemodulecontentsbyrerunningthemodule’scode.
5.3.2 Finders and loaders
Ifthenamedmoduleisnotfoundinsys.modules,thenPython’simportprotocolisinvokedtofindandloadthe
module. Thisprotocolconsistsoftwoconceptualobjects,findersandloaders. Afinder’sjobistodeterminewhether
itcanfindthenamedmoduleusingwhateverstrategyitknowsabout. Objectsthatimplementbothoftheseinterfaces
arereferredtoasimporters-theyreturnthemselveswhentheyfindthattheycanloadtherequestedmodule.
Pythonincludesanumberofdefaultfindersandimporters. Thefirstoneknowshowtolocatebuilt-inmodules,and
the second knows how to locate frozen modules. A third default finder searches an import path for modules. The
importpathisalistoflocationsthatmaynamefilesystempathsorzipfiles. Itcanalsobeextendedtosearchforany
locatableresource,suchasthoseidentifiedbyURLs.
Theimportmachineryisextensible,sonewfinderscanbeaddedtoextendtherangeandscopeofmodulesearching.
Findersdonotactuallyloadmodules. Iftheycanfindthenamedmodule,theyreturnamodulespec,anencapsulation
ofthemodule’simport-relatedinformation,whichtheimportmachinerythenuseswhenloadingthemodule.
Thefollowingsectionsdescribetheprotocolforfindersandloadersinmoredetail,includinghowyoucancreateand
registernewonestoextendtheimportmachinery.
Changedinversion3.4: InpreviousversionsofPython,findersreturnedloadersdirectly,whereasnowtheyreturn
modulespecswhichcontainloaders. Loadersarestillusedduringimportbuthavefewerresponsibilities.
5.3.3 Import hooks
Theimportmachineryisdesignedtobeextensible;theprimarymechanismforthisaretheimporthooks. Thereare
twotypesofimporthooks: metahooksandimportpathhooks.
Metahooksarecalledatthestartofimportprocessing,beforeanyotherimportprocessinghasoccurred,otherthan
sys.modulescachelookup. Thisallowsmetahookstooverridesys.pathprocessing,frozenmodules,oreven
built-inmodules. Metahooksareregisteredbyaddingnewfinderobjectstosys.meta_path,asdescribedbelow.
Importpathhooksarecalledaspartofsys.path(orpackage.__path__)processing, atthepointwheretheir
associatedpathitemisencountered. Importpathhooksareregisteredbyaddingnewcallablestosys.path_hooks
asdescribedbelow.
5.3.4 The meta path
When the named module is not found in sys.modules, Python next searches sys.meta_path, which contains
alistofmetapathfinderobjects. Thesefindersarequeriedinordertoseeiftheyknowhowtohandlethenamed
module. Metapathfindersmustimplementamethodcalledfind_spec()whichtakesthreearguments: aname,
animportpath, and(optionally)atargetmodule. Themetapathfindercanuseanystrategyitwantstodetermine
whetheritcanhandlethenamedmoduleornot.
5.3. Searching 75

### 第84页

Ifthemetapathfinderknowshowtohandlethenamedmodule,itreturnsaspecobject. Ifitcannothandlethenamed
module, it returns None. If sys.meta_path processing reaches the end of its list without returning a spec, then
a ModuleNotFoundError is raised. Any other exceptions raised are simply propagated up, aborting the import
process.
Thefind_spec()methodofmetapathfindersiscalledwithtwoorthreearguments. Thefirstisthefullyqualified
nameof the module being imported, for example foo.bar.baz. The second argument is the path entriesto use
forthemodulesearch. Fortop-levelmodules,thesecondargumentisNone,butforsubmodulesorsubpackages,the
second argument is the value of the parent package’s __path__ attribute. If the appropriate __path__ attribute
cannotbeaccessed,aModuleNotFoundErrorisraised. Thethirdargumentisanexistingmoduleobjectthatwill
bethetargetofloadinglater. Theimportsystempassesinatargetmoduleonlyduringreload.
The meta path may be traversed multiple times for a single import request. For example, assuming none of the
modules involved has already been cached, importing foo.bar.baz will first perform a top level import, calling
mpf.find_spec("foo", None, None) on each meta path finder (mpf). After foo has been imported, foo.
bar will be imported by traversing the meta path a second time, calling mpf.find_spec("foo.bar", foo.
__path__, None). Oncefoo.barhasbeenimported,thefinaltraversalwillcallmpf.find_spec("foo.bar.
baz", foo.bar.__path__, None).
Somemetapathfindersonlysupporttoplevelimports. TheseimporterswillalwaysreturnNonewhenanythingother
thanNoneispassedasthesecondargument.
Python’sdefaultsys.meta_pathhasthreemetapathfinders,onethatknowshowtoimportbuilt-inmodules,one
thatknowshowtoimportfrozenmodules,andonethatknowshowtoimportmodulesfromanimportpath(i.e. the
pathbasedfinder).
Changedinversion3.4: Thefind_spec()methodofmetapathfindersreplacedfind_module(),whichisnow
deprecated. Whileitwillcontinuetoworkwithoutchange,theimportmachinerywilltryitonlyifthefinderdoes
notimplementfind_spec().
Changedinversion3.10: Useoffind_module()bytheimportsystemnowraisesImportWarning.
Changedinversion3.12: find_module()hasbeenremoved. Usefind_spec()instead.
5.4 Loading
Ifandwhenamodulespecisfound,theimportmachinerywilluseit(andtheloaderitcontains)whenloadingthe
module. Hereisanapproximationofwhathappensduringtheloadingportionofimport:
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
# It is assumed 'exec_module' will also be defined on the loader.
module = spec.loader.create_module(spec)
if module is None:
module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)
if spec.loader is None:
# unsupported
raise ImportError
if spec.origin is None and spec.submodule_search_locations is not None:
# namespace package
sys.modules[spec.name] = module
elif not hasattr(spec.loader, 'exec_module'):
module = spec.loader.load_module(spec.name)
else:
sys.modules[spec.name] = module
try:
spec.loader.exec_module(module)
(continuesonnextpage)
76 Chapter5. Theimportsystem

### 第85页

(continuedfrompreviouspage)
except BaseException:
try:
del sys.modules[spec.name]
except KeyError:
pass
raise
return sys.modules[spec.name]
Notethefollowingdetails:
• Ifthereisanexistingmoduleobjectwiththegivennameinsys.modules,importwillhavealreadyreturned
it.
• Themodulewillexistinsys.modulesbeforetheloaderexecutesthemodulecode. Thisiscrucialbecause
the module code may (directly or indirectly) import itself; adding it to sys.modules beforehand prevents
unboundedrecursionintheworstcaseandmultipleloadinginthebest.
• Ifloadingfails, thefailingmodule–andonlythefailingmodule–getsremovedfromsys.modules. Any
modulealreadyinthesys.modulescache,andanymodulethatwassuccessfullyloadedasaside-effect,must
remaininthecache. Thiscontrastswithreloadingwhereeventhefailingmoduleisleftinsys.modules.
• After the module is created but before execution, the import machinery sets the import-related module at-
tributes(“_init_module_attrs”inthepseudo-codeexampleabove),assummarizedinalatersection.
• Moduleexecutionisthekeymomentofloadinginwhichthemodule’snamespacegetspopulated. Execution
isentirelydelegatedtotheloader,whichgetstodecidewhatgetspopulatedandhow.
• Themodulecreatedduringloadingandpassedtoexec_module()maynotbetheonereturnedattheendof
import2.
Changed in version 3.4: The import system has taken over the boilerplate responsibilities of loaders. These were
previouslyperformedbytheimportlib.abc.Loader.load_module()method.
5.4.1 Loaders
Module loaders provide the critical function of loading: module execution. The import machinery calls the
importlib.abc.Loader.exec_module()methodwithasingleargument, themoduleobjecttoexecute. Any
valuereturnedfromexec_module()isignored.
Loadersmustsatisfythefollowingrequirements:
• If the module is a Python module (as opposed to a built-in module or a dynamically loaded extension), the
loadershouldexecutethemodule’scodeinthemodule’sglobalnamespace(module.__dict__).
• Iftheloadercannotexecutethemodule,itshouldraiseanImportError,althoughanyotherexceptionraised
duringexec_module()willbepropagated.
In many cases, the finder and loader can be the same object; in such cases the find_spec() method would just
returnaspecwiththeloadersettoself.
Module loaders may opt in to creating the module object during loading by implementing a create_module()
method. It takes one argument, the module spec, and returns the new module object to use during loading.
create_module() does not need to set any attributes on the module object. If the method returns None, the
importmachinerywillcreatethenewmoduleitself.
Addedinversion3.4: Thecreate_module()methodofloaders.
Changedinversion3.4: Theload_module()methodwasreplacedbyexec_module()andtheimportmachinery
assumedalltheboilerplateresponsibilitiesofloading.
2Theimportlibimplementationavoidsusingthereturnvaluedirectly. Instead,itgetsthemoduleobjectbylookingthemodulenameup
insys.modules. Theindirecteffectofthisisthatanimportedmodulemayreplaceitselfinsys.modules. Thisisimplementation-specific
behaviorthatisnotguaranteedtoworkinotherPythonimplementations.
5.4. Loading 77

### 第86页

Forcompatibilitywithexistingloaders,theimportmachinerywillusetheload_module()methodofloadersifit
existsandtheloaderdoesnotalsoimplementexec_module(). However,load_module()hasbeendeprecated
andloadersshouldimplementexec_module()instead.
Theload_module()methodmustimplementalltheboilerplateloadingfunctionalitydescribedaboveinaddition
toexecutingthemodule. Allthesameconstraintsapply,withsomeadditionalclarification:
• Ifthereisanexistingmoduleobjectwiththegivennameinsys.modules,theloadermustusethatexisting
module. (Otherwise,importlib.reload()willnotworkcorrectly.) Ifthenamedmoduledoesnotexistin
sys.modules,theloadermustcreateanewmoduleobjectandaddittosys.modules.
• Themodulemust existinsys.modulesbeforetheloaderexecutesthemodulecode,topreventunbounded
recursionormultipleloading.
• Ifloadingfails,theloadermustremoveanymodulesithasinsertedintosys.modules,butitmustremove
onlythefailingmodule(s),andonlyiftheloaderitselfhasloadedthemodule(s)explicitly.
Changed in version 3.5: A DeprecationWarning is raised when exec_module() is defined but
create_module()isnot.
Changedinversion3.6: AnImportErrorisraisedwhenexec_module()isdefinedbutcreate_module()is
not.
Changedinversion3.10: Useofload_module()willraiseImportWarning.
5.4.2 Submodules
Whenasubmoduleisloadedusinganymechanism(e.g. importlibAPIs,theimportorimport-fromstatements,
or built-in __import__()) a binding is placed in the parent module’s namespace to the submodule object. For
example,ifpackagespamhasasubmodulefoo,afterimportingspam.foo,spamwillhaveanattributefoowhich
isboundtothesubmodule. Let’ssayyouhavethefollowingdirectorystructure:
spam/
__init__.py
foo.py
andspam/__init__.pyhasthefollowinglineinit:
from .foo import Foo
thenexecutingthefollowingputsnamebindingsforfooandFoointhespammodule:
>>> import spam
>>> spam.foo
<module 'spam.foo' from '/tmp/imports/spam/foo.py'>
>>> spam.Foo
<class 'spam.foo.Foo'>
Given Python’s familiar name binding rules this might seem surprising, but it’s actually a fundamental feature of
theimportsystem. Theinvariantholdingisthatifyouhavesys.modules['spam']andsys.modules['spam.
foo'](asyouwouldaftertheaboveimport),thelattermustappearasthefooattributeoftheformer.
5.4.3 Module specs
The import machinery uses a variety of information about each module during import, especially before loading.
Mostoftheinformationiscommontoallmodules. Thepurposeofamodule’sspecistoencapsulatethisimport-
relatedinformationonaper-modulebasis.
Usingaspecduringimportallowsstatetobetransferredbetweenimportsystemcomponents,e.g. betweenthefinder
that creates the module spec and the loader that executes it. Most importantly, it allows the import machinery to
performtheboilerplateoperationsofloading,whereaswithoutamodulespectheloaderhadthatresponsibility.
78 Chapter5. Theimportsystem

### 第87页

Themodule’sspecisexposedasmodule.__spec__. Setting__spec__appropriatelyappliesequallytomodules
initializedduringinterpreterstartup. Theoneexceptionis__main__,where__spec__issettoNoneinsomecases.
SeeModuleSpecfordetailsonthecontentsofthemodulespec.
Addedinversion3.4.
5.4.4 __path__ attributes on modules
The__path__attributeshouldbea(possiblyempty)sequenceofstringsenumeratingthelocationswherethepack-
age’ssubmoduleswillbefound. Bydefinition,ifamodulehasa__path__attribute,itisapackage.
Apackage’s__path__attributeisusedduringimportsofitssubpackages. Withintheimportmachinery,itfunctions
much the same as sys.path, i.e. providing a list of locations to search for modules during import. However,
__path__istypicallymuchmoreconstrainedthansys.path.
Thesamerulesusedforsys.pathalsoapplytoapackage’s__path__. sys.path_hooks(describedbelow)are
consultedwhentraversingapackage’s__path__.
A package’s __init__.py file may set or alter the package’s __path__ attribute, and this was typically the way
namespace packages were implemented prior to PEP 420. With the adoption of PEP 420, namespace packages
nolongerneedtosupply__init__.pyfilescontainingonly__path__manipulationcode;theimportmachinery
automaticallysets__path__correctlyforthenamespacepackage.
5.4.5 Module reprs
Bydefault,allmoduleshaveausablerepr,howeverdependingontheattributessetabove,andinthemodule’sspec,
youcanmoreexplicitlycontrolthereprofmoduleobjects.
Ifthemodulehasaspec(__spec__),theimportmachinerywilltrytogenerateareprfromit. Ifthatfailsorthereis
nospec,theimportsystemwillcraftadefaultreprusingwhateverinformationisavailableonthemodule. Itwilltryto
usethemodule.__name__,module.__file__,andmodule.__loader__asinputintotherepr,withdefaults
forwhateverinformationismissing.
Herearetheexactrulesused:
• Ifthemodulehasa__spec__attribute,theinformationinthespecisusedtogeneratetherepr. The“name”,
“loader”,“origin”,and“has_location”attributesareconsulted.
• Ifthemodulehasa__file__attribute,thisisusedaspartofthemodule’srepr.
• Ifthemodulehasno__file__butdoeshavea__loader__thatisnotNone,thentheloader’sreprisused
aspartofthemodule’srepr.
• Otherwise,justusethemodule’s__name__intherepr.
Changedinversion3.12:Useofmodule_repr(),havingbeendeprecatedsincePython3.4,wasremovedinPython
3.12andisnolongercalledduringtheresolutionofamodule’srepr.
5.4.6 Cached bytecode invalidation
Before Python loads cached bytecode from a .pyc file, it checks whether the cache is up-to-date with the source
.pyfile. Bydefault,Pythondoesthisbystoringthesource’slast-modifiedtimestampandsizeinthecachefilewhen
writingit. Atruntime,theimportsystemthenvalidatesthecachefilebycheckingthestoredmetadatainthecache
fileagainstthesource’smetadata.
Pythonalsosupports“hash-based”cachefiles,whichstoreahashofthesourcefile’scontentsratherthanitsmetadata.
Therearetwovariantsofhash-based.pycfiles: checkedandunchecked. Forcheckedhash-based.pycfiles,Python
validatesthecachefilebyhashingthesourcefileandcomparingtheresultinghashwiththehashinthecachefile. If
acheckedhash-basedcachefileisfoundtobeinvalid,Pythonregeneratesitandwritesanewcheckedhash-based
cachefile. Foruncheckedhash-based.pycfiles,Pythonsimplyassumesthecachefileisvalidifitexists. Hash-based
.pycfilesvalidationbehaviormaybeoverriddenwiththe--check-hash-based-pycsflag.
Changedinversion3.7: Addedhash-based.pycfiles. Previously,Pythononlysupportedtimestamp-basedinvali-
dationofbytecodecaches.
5.4. Loading 79

### 第88页

5.5 The Path Based Finder
Asmentionedpreviously,Pythoncomeswithseveraldefaultmetapathfinders. Oneofthese,calledthepathbased
finder(PathFinder),searchesanimportpath,whichcontainsalistofpathentries. Eachpathentrynamesalocation
tosearchformodules.
Thepathbasedfinderitselfdoesn’tknowhowtoimportanything. Instead, ittraversestheindividualpathentries,
associatingeachofthemwithapathentryfinderthatknowshowtohandlethatparticularkindofpath.
The default set of path entry finders implement all the semantics for finding modules on the file system, handling
specialfiletypessuchasPythonsourcecode(.pyfiles),Pythonbytecode(.pycfiles)andsharedlibraries(e.g. .so
files). Whensupportedbythezipimportmoduleinthestandardlibrary,thedefaultpathentryfindersalsohandle
loadingallofthesefiletypes(otherthansharedlibraries)fromzipfiles.
Path entries need not be limited to file system locations. They can refer to URLs, database queries, or any other
locationthatcanbespecifiedasastring.
The path based finder provides additional hooks and protocols so that you can extend and customize the types of
searchablepathentries. Forexample,ifyouwantedtosupportpathentriesasnetworkURLs,youcouldwriteahook
thatimplementsHTTPsemanticstofindmodulesontheweb. Thishook(acallable)wouldreturnapathentryfinder
supportingtheprotocoldescribedbelow,whichwasthenusedtogetaloaderforthemodulefromtheweb.
Awordofwarning: thissectionandthepreviousbothusethetermfinder,distinguishingbetweenthembyusingthe
termsmetapathfinderandpathentryfinder. Thesetwotypesoffindersareverysimilar,supportsimilarprotocols,
andfunctioninsimilarwaysduringtheimportprocess,butit’simportanttokeepinmindthattheyaresubtlydifferent.
Inparticular, metapathfindersoperateatthebeginningoftheimportprocess, askeyedoffthesys.meta_path
traversal.
Bycontrast,pathentryfindersareinasenseanimplementationdetailofthepathbasedfinder,andinfact,ifthepath
basedfinderweretoberemovedfromsys.meta_path,noneofthepathentryfindersemanticswouldbeinvoked.
5.5.1 Path entry finders
ThepathbasedfinderisresponsibleforfindingandloadingPythonmodulesandpackageswhoselocationisspecified
withastringpathentry. Mostpathentriesnamelocationsinthefilesystem,buttheyneednotbelimitedtothis.
Asametapathfinder,thepathbasedfinderimplementsthefind_spec()protocolpreviouslydescribed,however
itexposesadditionalhooksthatcanbeusedtocustomizehowmodulesarefoundandloadedfromtheimportpath.
Three variables are used by the path based finder, sys.path, sys.path_hooks and sys.
path_importer_cache. The __path__ attributes on package objects are also used. These provide additional
waysthattheimportmachinerycanbecustomized.
sys.pathcontainsalistofstringsprovidingsearchlocationsformodulesandpackages. Itisinitializedfromthe
PYTHONPATHenvironmentvariableandvariousotherinstallation-andimplementation-specificdefaults. Entriesin
sys.pathcannamedirectoriesonthefilesystem,zipfiles,andpotentiallyother“locations”(seethesitemodule)
thatshouldbesearchedformodules,suchasURLs,ordatabasequeries. Onlystringsshouldbepresentonsys.path;
allotherdatatypesareignored.
The path based finder is a meta path finder, so the import machinery begins the import path search by calling the
pathbasedfinder’sfind_spec()methodasdescribedpreviously. Whenthepathargumenttofind_spec()is
given,itwillbealistofstringpathstotraverse-typicallyapackage’s__path__attributeforanimportwithinthat
package. IfthepathargumentisNone,thisindicatesatoplevelimportandsys.pathisused.
The path based finder iterates over every entry in the search path, and for each of these, looks for an appropriate
pathentryfinder (PathEntryFinder)forthepathentry. Becausethiscanbeanexpensiveoperation(e.g. there
may be stat() call overheads for this search), the path based finder maintains a cache mapping path entries to
pathentryfinders. Thiscacheismaintainedinsys.path_importer_cache(despitethename,thiscacheactually
storesfinderobjectsratherthanbeinglimitedtoimporterobjects). Inthisway,theexpensivesearchforaparticular
path entry location’s path entry finder need only be done once. User code is free to remove cache entries from
sys.path_importer_cacheforcingthepathbasedfindertoperformthepathentrysearchagain.
Ifthepathentryisnotpresentinthecache,thepathbasedfinderiteratesovereverycallableinsys.path_hooks.
Eachofthepathentryhooksinthislistiscalledwithasingleargument,thepathentrytobesearched. Thiscallable
80 Chapter5. Theimportsystem

### 第89页

mayeitherreturnapathentryfinderthatcanhandlethepathentry,oritmayraiseImportError. AnImportError
isusedbythepathbasedfindertosignalthatthehookcannotfindapathentryfinderforthatpathentry. Theexception
isignoredandimportpathiterationcontinues. Thehookshouldexpecteitherastringorbytesobject;theencoding
ofbytesobjectsisuptothehook(e.g. itmaybeafilesystemencoding,UTF-8,orsomethingelse),andifthehook
cannotdecodetheargument,itshouldraiseImportError.
If sys.path_hooks iteration ends with no path entry finder being returned, then the path based finder’s
find_spec() method will store None in sys.path_importer_cache (to indicate that there is no finder for
thispathentry)andreturnNone,indicatingthatthismetapathfindercouldnotfindthemodule.
Ifapathentryfinder isreturnedbyoneofthepathentryhookcallablesonsys.path_hooks,thenthefollowing
protocolisusedtoaskthefinderforamodulespec,whichisthenusedwhenloadingthemodule.
Thecurrentworkingdirectory–denotedbyanemptystring–ishandledslightlydifferentlyfromotherentrieson
sys.path. First,ifthecurrentworkingdirectorycannotbedeterminedorisfoundnottoexist,novalueisstored
insys.path_importer_cache. Second,thevalueforthecurrentworkingdirectoryislookedupfreshforeach
modulelookup. Third,thepathusedforsys.path_importer_cacheandreturnedbyimportlib.machinery.
PathFinder.find_spec()willbetheactualcurrentworkingdirectoryandnottheemptystring.
5.5.2 Path entry finder protocol
Inordertosupportimportsofmodulesandinitializedpackagesandalsotocontributeportionstonamespacepackages,
pathentryfindersmustimplementthefind_spec()method.
find_spec()takestwoarguments: thefullyqualifiednameofthemodulebeingimported,andthe(optional)target
module. find_spec()returnsafullypopulatedspecforthemodule. Thisspecwillalwayshave“loader”set(with
oneexception).
To indicate to the import machinery that the spec represents a namespace portion, the path entry finder sets
submodule_search_locationstoalistcontainingtheportion.
Changedinversion3.4: find_spec()replacedfind_loader()andfind_module(),bothofwhicharenow
deprecated,butwillbeusediffind_spec()isnotdefined.
Olderpathentryfindersmayimplementoneofthesetwodeprecatedmethodsinsteadoffind_spec(). Themeth-
ods are still respected for the sake of backward compatibility. However, if find_spec() is implemented on the
pathentryfinder,thelegacymethodsareignored.
find_loader() takes one argument, the fully qualified name of the module being imported. find_loader()
returnsa2-tuplewherethefirstitemistheloaderandtheseconditemisanamespaceportion.
Forbackwardscompatibilitywithotherimplementationsoftheimportprotocol,manypathentryfindersalsosup-
port the same, traditional find_module() method that meta path finders support. However path entry finder
find_module() methods are never called with a path argument (they are expected to record the appropriate
pathinformationfromtheinitialcalltothepathhook).
The find_module() method on path entry finders is deprecated, as it does not allow the path entry finder to
contributeportionstonamespacepackages. Ifbothfind_loader()andfind_module()existonapathentry
finder,theimportsystemwillalwayscallfind_loader()inpreferencetofind_module().
Changed in version 3.10: Calls to find_module() and find_loader() by the import system will raise
ImportWarning.
Changedinversion3.12: find_module()andfind_loader()havebeenremoved.
5.6 Replacing the standard import system
The most reliable mechanism for replacing the entire import system is to delete the default contents of sys.
meta_path,replacingthementirelywithacustommetapathhook.
IfitisacceptabletoonlyalterthebehaviourofimportstatementswithoutaffectingotherAPIsthataccesstheimport
system,thenreplacingthebuiltin__import__()functionmaybesufficient. Thistechniquemayalsobeemployed
atthemoduleleveltoonlyalterthebehaviourofimportstatementswithinthatmodule.
5.6. Replacingthestandardimportsystem 81

### 第90页

To selectively prevent the import of some modules from a hook early on the meta path (rather than disabling the
standardimportsystementirely),itissufficienttoraiseModuleNotFoundErrordirectlyfromfind_spec()in-
steadofreturningNone. Thelatterindicatesthatthemetapathsearchshouldcontinue,whileraisinganexception
terminatesitimmediately.
5.7 Package Relative Imports
Relativeimportsuseleadingdots. Asingleleadingdotindicatesarelativeimport,startingwiththecurrentpackage.
Twoormoreleadingdotsindicatearelativeimporttotheparent(s)ofthecurrentpackage,onelevelperdotafter
thefirst. Forexample,giventhefollowingpackagelayout:
package/
__init__.py
subpackage1/
__init__.py
moduleX.py
moduleY.py
subpackage2/
__init__.py
moduleZ.py
moduleA.py
Ineithersubpackage1/moduleX.pyorsubpackage1/__init__.py,thefollowingarevalidrelativeimports:
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
Absoluteimportsmayuseeithertheimport <>orfrom <> import <>syntax, butrelativeimportsmayonly
usethesecondform;thereasonforthisisthat:
import XXX.YYY.ZZZ
shouldexposeXXX.YYY.ZZZasausableexpression,but.moduleYisnotavalidexpression.
5.8 Special considerations for __main__
The __main__ module is a special case relative to Python’s import system. As noted elsewhere, the __main__
module is directly initialized at interpreter startup, much like sys and builtins. However, unlike those two, it
doesn’tstrictlyqualifyasabuilt-inmodule. Thisisbecausethemannerinwhich__main__isinitializeddependson
theflagsandotheroptionswithwhichtheinterpreterisinvoked.
5.8.1 __main__.__spec__
Dependingonhow__main__isinitialized,__main__.__spec__getssetappropriatelyortoNone.
When Python is started with the -m option, __spec__ is set to the module spec of the corresponding module or
package. __spec__isalsopopulatedwhenthe__main__moduleisloadedaspartofexecutingadirectory,zipfile
orothersys.pathentry.
Intheremainingcases__main__.__spec__issettoNone,asthecodeusedtopopulatethe__main__doesnot
corresponddirectlywithanimportablemodule:
• interactiveprompt
• -coption
82 Chapter5. Theimportsystem

### 第91页

• runningfromstdin
• runningdirectlyfromasourceorbytecodefile
Notethat__main__.__spec__isalwaysNoneinthelastcase,evenifthefilecouldtechnicallybeimporteddirectly
asamoduleinstead. Usethe-mswitchifvalidmodulemetadataisdesiredin__main__.
Note also that even when __main__ corresponds with an importable module and __main__.__spec__ is set
accordingly,they’restillconsidereddistinct modules. Thisisduetothefactthatblocksguardedbyif __name__
== "__main__": checks only execute when the module is used to populate the __main__ namespace, and not
duringnormalimport.
5.9 References
TheimportmachineryhasevolvedconsiderablysincePython’searlydays. Theoriginalspecificationforpackagesis
stillavailabletoread,althoughsomedetailshavechangedsincethewritingofthatdocument.
Theoriginalspecificationforsys.meta_pathwasPEP302,withsubsequentextensioninPEP420.
PEP420introducednamespacepackagesforPython3.3. PEP420alsointroducedthefind_loader()protocol
asanalternativetofind_module().
PEP366describestheadditionofthe__package__attributeforexplicitrelativeimportsinmainmodules.
PEP328introducedabsoluteandexplicitrelativeimportsandinitiallyproposed__name__forsemanticsPEP366
wouldeventuallyspecifyfor__package__.
PEP338definesexecutingmodulesasscripts.
PEP451addstheencapsulationofper-moduleimportstateinspecobjects. Italsooff-loadsmostoftheboilerplate
responsibilitiesofloadersbackontotheimportmachinery. ThesechangesallowthedeprecationofseveralAPIsin
theimportsystemandalsoadditionofnewmethodstofindersandloaders.
5.9. References 83

### 第92页

84 Chapter5. Theimportsystem

### 第93页

CHAPTER
SIX
EXPRESSIONS
ThischapterexplainsthemeaningoftheelementsofexpressionsinPython.
SyntaxNotes: Inthisandthefollowingchapters,extendedBNFnotationwillbeusedtodescribesyntax,notlexical
analysis. When(onealternativeof)asyntaxrulehastheform
name: othername
andnosemanticsaregiven,thesemanticsofthisformofnamearethesameasforothername.
6.1 Arithmetic conversions
When a description of an arithmetic operator below uses the phrase “the numeric arguments are converted to a
commonrealtype”,thismeansthattheoperatorimplementationforbuilt-intypesworksasfollows:
• Ifbothargumentsarecomplexnumbers,noconversionisperformed;
• ifeitherargumentisacomplexorafloating-pointnumber,theotherisconvertedtoafloating-pointnumber;
• otherwise,bothmustbeintegersandnoconversionisnecessary.
Someadditionalrulesapplyforcertainoperators(e.g., astringasaleftargumenttothe‘%’operator). Extensions
mustdefinetheirownconversionbehavior.
6.2 Atoms
Atomsarethemostbasicelementsofexpressions. Thesimplestatomsareidentifiersorliterals. Formsenclosedin
parentheses,bracketsorbracesarealsocategorizedsyntacticallyasatoms. Thesyntaxforatomsis:
atom: identifier | literal | enclosure
enclosure: parenth_form | list_display | dict_display | set_display
| generator_expression | yield_atom
6.2.1 Identifiers (Names)
Anidentifieroccurringasanatomisaname. SeesectionNames(identifiersandkeywords)forlexicaldefinitionand
sectionNamingandbindingfordocumentationofnamingandbinding.
When the name is bound to an object, evaluation of the atom yields that object. When a name is not bound, an
attempttoevaluateitraisesaNameErrorexception.
Privatenamemangling
Whenanidentifierthattextuallyoccursinaclassdefinitionbeginswithtwoormoreunderscorecharactersanddoes
notendintwoormoreunderscores,itisconsideredaprivatenameofthatclass.
85

### 第94页

(cid:181) Seealso
Theclassspecifications.
Moreprecisely,privatenamesaretransformedtoalongerformbeforecodeisgeneratedforthem. Ifthetransformed
nameislongerthan255characters,implementation-definedtruncationmayhappen.
The transformation is independent of the syntactical context in which the identifier is used but only the following
privateidentifiersaremangled:
• Anynameusedasthenameofavariablethatisassignedorreadoranynameofanattributebeingaccessed.
The__name__attributeofnestedfunctions,classes,andtypealiasesishowevernotmangled.
• Thenameofimportedmodules,e.g.,__spaminimport __spam. Ifthemoduleispartofapackage(i.e.,
itsnamecontainsadot),thenameisnotmangled,e.g.,the__fooinimport __foo.barisnotmangled.
• Thenameofanimportedmember,e.g.,__finfrom spam import __f.
Thetransformationruleisdefinedasfollows:
• Theclassname,withleadingunderscoresremovedandasingleleadingunderscoreinserted,isinsertedinfront
oftheidentifier,e.g.,theidentifier__spamoccurringinaclassnamedFoo,_Fooor__Fooistransformedto
_Foo__spam.
• Iftheclassnameconsistsonlyofunderscores, thetransformationistheidentity, e.g., theidentifier__spam
occurringinaclassnamed_or__isleftasis.
6.2.2 Literals
Pythonsupportsstringandbytesliteralsandvariousnumericliterals:
literal: strings | NUMBER
Evaluationofaliteralyieldsanobjectofthegiventype(string,bytes,integer,floating-pointnumber,complexnum-
ber) with the given value. The value may be approximated in the case of floating-point and imaginary (complex)
literals. SeesectionLiteralsfordetails. SeesectionStringliteralconcatenationfordetailsonstrings.
All literals correspond to immutable data types, and hence the object’s identity is less important than its value.
Multiple evaluations of literals with the same value (either the same occurrence in the program text or a different
occurrence)mayobtainthesameobjectoradifferentobjectwiththesamevalue.
Stringliteralconcatenation
Multipleadjacentstringorbytesliterals(delimitedbywhitespace),possiblyusingdifferentquotingconventions,are
allowed,andtheirmeaningisthesameastheirconcatenation:
>>> "hello" 'world'
"helloworld"
Formally:
strings: ( STRING | fstring)+ | tstring+
Thisfeatureisdefinedatthesyntacticallevel,soitonlyworkswithliterals. Toconcatenatestringexpressionsatrun
time,the‘+’operatormaybeused:
>>> greeting = "Hello"
>>> space = " "
>>> name = "Blaise"
>>> print(greeting + space + name) # not: print(greeting space name)
Hello Blaise
86 Chapter6. Expressions

|  |
| --- |
| (cid:181) Seealso |
| Theclassspecifications. |

### 第95页

Literalconcatenationcanfreelymixrawstrings,triple-quotedstrings,andformattedstringliterals. Forexample:
>>> "Hello" r', ' f"{name}!"
"Hello, Blaise!"
Thisfeaturecanbeusedtoreducethenumberofbackslashesneeded,tosplitlongstringsconvenientlyacrosslong
lines,oreventoaddcommentstopartsofstrings. Forexample:
re.compile("[A-Za-z_]" # letter or underscore
"[A-Za-z0-9_]*" # letter, digit or underscore
)
However, bytes literals may only be combined with other byte literals; not with string literals of any kind. Also,
templatestringliteralsmayonlybecombinedwithothertemplatestringliterals:
>>> t"Hello" t"{name}!"
Template(strings=('Hello', '!'), interpolations=(...))
6.2.3 Parenthesized forms
Aparenthesizedformisanoptionalexpressionlistenclosedinparentheses:
parenth_form: "(" [starred_expression] ")"
Aparenthesizedexpressionlistyieldswhateverthatexpressionlistyields: ifthelistcontainsatleastonecomma,it
yieldsatuple;otherwise,ityieldsthesingleexpressionthatmakesuptheexpressionlist.
Anemptypairofparenthesesyieldsanemptytupleobject. Sincetuplesareimmutable,thesamerulesasforliterals
apply(i.e.,twooccurrencesoftheemptytuplemayormaynotyieldthesameobject).
Notethattuplesarenotformedbytheparentheses,butratherbyuseofthecomma. Theexceptionistheemptytuple,
for which parentheses are required — allowing unparenthesized “nothing” in expressions would cause ambiguities
andallowcommontypostopassuncaught.
6.2.4 Displays for lists, sets and dictionaries
For constructing a list, a set or a dictionary Python provides special syntax called “displays”, each of them in two
flavors:
• eitherthecontainercontentsarelistedexplicitly,or
• theyarecomputedviaasetofloopingandfilteringinstructions,calledacomprehension.
Commonsyntaxelementsforcomprehensionsare:
comprehension: assignment_expression comp_for
comp_for: ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter: comp_for | comp_if
comp_if: "if" or_test [comp_iter]
Thecomprehensionconsistsofasingleexpressionfollowedbyatleastoneforclauseandzeroormorefororif
clauses. Inthiscase,theelementsofthenewcontainerarethosethatwouldbeproducedbyconsideringeachofthe
fororifclausesablock,nestingfromlefttoright,andevaluatingtheexpressiontoproduceanelementeachtime
theinnermostblockisreached.
However,asidefromtheiterableexpressionintheleftmostforclause,thecomprehensionisexecutedinaseparate
implicitlynestedscope. Thisensuresthatnamesassignedtointhetargetlistdon’t“leak”intotheenclosingscope.
Theiterableexpressionintheleftmostforclauseisevaluateddirectlyintheenclosingscopeandthenpassedasan
argumenttotheimplicitlynestedscope. Subsequentforclausesandanyfilterconditionintheleftmostforclause
cannotbeevaluatedintheenclosingscopeastheymaydependonthevaluesobtainedfromtheleftmostiterable. For
example: [x*y for x in range(10) for y in range(x, x+10)].
6.2. Atoms 87

### 第96页

Toensurethecomprehensionalwaysresultsinacontaineroftheappropriatetype,yieldandyield fromexpres-
sionsareprohibitedintheimplicitlynestedscope.
Since Python 3.6, in an async def function, an async for clause may be used to iterate over a asynchronous
iterator. Acomprehensioninanasync deffunctionmayconsistofeitherafororasync forclausefollowing
theleadingexpression,maycontainadditionalfororasync forclauses,andmayalsouseawaitexpressions.
Ifacomprehensioncontainsasync forclauses, orifitcontainsawaitexpressionsorotherasynchronouscom-
prehensionsanywhereexcepttheiterableexpressionintheleftmostforclause,itiscalledanasynchronouscompre-
hension. Anasynchronouscomprehensionmaysuspendtheexecutionofthecoroutinefunctioninwhichitappears.
SeealsoPEP530.
Addedinversion3.6: Asynchronouscomprehensionswereintroduced.
Changedinversion3.8: yieldandyield fromprohibitedintheimplicitlynestedscope.
Changed in version 3.11: Asynchronous comprehensions are now allowed inside comprehensions in asynchronous
functions. Outercomprehensionsimplicitlybecomeasynchronous.
6.2.5 List displays
Alistdisplayisapossiblyemptyseriesofexpressionsenclosedinsquarebrackets:
list_display: "[" [flexible_expression_list | comprehension] "]"
Alistdisplayyieldsanewlistobject,thecontentsbeingspecifiedbyeitheralistofexpressionsoracomprehension.
Whenacomma-separatedlistofexpressionsissupplied,itselementsareevaluatedfromlefttorightandplacedinto
thelistobjectinthatorder. Whenacomprehensionissupplied, thelistisconstructedfromtheelementsresulting
fromthecomprehension.
6.2.6 Set displays
Asetdisplayisdenotedbycurlybracesanddistinguishablefromdictionarydisplaysbythelackofcolonsseparating
keysandvalues:
set_display: "{" (flexible_expression_list | comprehension) "}"
Asetdisplayyieldsanewmutablesetobject,thecontentsbeingspecifiedbyeitherasequenceofexpressionsora
comprehension. Whenacomma-separatedlistofexpressionsissupplied,itselementsareevaluatedfromlefttoright
andaddedtothesetobject. Whenacomprehensionissupplied, thesetisconstructedfromtheelementsresulting
fromthecomprehension.
Anemptysetcannotbeconstructedwith{};thisliteralconstructsanemptydictionary.
6.2.7 Dictionary displays
Adictionarydisplayisapossiblyemptyseriesofdictitems(key/valuepairs)enclosedincurlybraces:
dict_display: "{" [dict_item_list | dict_comprehension] "}"
dict_item_list: dict_item ("," dict_item)* [","]
dict_item: expression ":" expression | "**" or_expr
dict_comprehension: expression ":" expression comp_for
Adictionarydisplayyieldsanewdictionaryobject.
Ifacomma-separatedsequenceofdictitemsisgiven,theyareevaluatedfromlefttorighttodefinetheentriesofthe
dictionary: eachkeyobjectisusedasakeyintothedictionarytostorethecorrespondingvalue. Thismeansthatyou
canspecifythesamekeymultipletimesinthedictitemlist,andthefinaldictionary’svalueforthatkeywillbethe
lastonegiven.
Adoubleasterisk**denotesdictionaryunpacking. Itsoperandmustbeamapping. Eachmappingitemisaddedto
thenewdictionary. Latervaluesreplacevaluesalreadysetbyearlierdictitemsandearlierdictionaryunpackings.
Addedinversion3.5: Unpackingintodictionarydisplays,originallyproposedbyPEP448.
88 Chapter6. Expressions

### 第97页

A dict comprehension, in contrast to list and set comprehensions, needs two expressions separated with a colon
followedbytheusual“for”and“if”clauses. Whenthecomprehensionisrun,theresultingkeyandvalueelements
areinsertedinthenewdictionaryintheordertheyareproduced.
RestrictionsonthetypesofthekeyvaluesarelistedearlierinsectionThestandardtypehierarchy. (Tosummarize,the
keytypeshouldbehashable,whichexcludesallmutableobjects.) Clashesbetweenduplicatekeysarenotdetected;
thelastvalue(textuallyrightmostinthedisplay)storedforagivenkeyvalueprevails.
Changedinversion3.8: PriortoPython3.8,indictcomprehensions,theevaluationorderofkeyandvaluewasnot
well-defined. InCPython,thevaluewasevaluatedbeforethekey. Startingwith3.8,thekeyisevaluatedbeforethe
value,asproposedbyPEP572.
6.2.8 Generator expressions
Ageneratorexpressionisacompactgeneratornotationinparentheses:
generator_expression: "(" expression comp_for ")"
Ageneratorexpressionyieldsanewgeneratorobject. Itssyntaxisthesameasforcomprehensions,exceptthatitis
enclosedinparenthesesinsteadofbracketsorcurlybraces.
Variablesusedinthegeneratorexpressionareevaluatedlazilywhenthe__next__()methodiscalledforthegen-
eratorobject(inthesamefashionasnormalgenerators). However,theiterableexpressionintheleftmostforclause
is immediately evaluated, and the iterator is immediately created for that iterable, so that an error produced while
creatingtheiteratorwillbeemittedatthepointwherethegeneratorexpressionisdefined, ratherthanatthepoint
wherethefirstvalueisretrieved. Subsequentforclausesandanyfilterconditionintheleftmostforclausecannotbe
evaluatedintheenclosingscopeastheymaydependonthevaluesobtainedfromtheleftmostiterable. Forexample:
(x*y for x in range(10) for y in range(x, x+10)).
Theparenthesescanbeomittedoncallswithonlyoneargument. SeesectionCallsfordetails.
Toavoidinterferingwiththeexpectedoperationofthegeneratorexpressionitself,yieldandyield fromexpres-
sionsareprohibitedintheimplicitlydefinedgenerator.
If a generator expression contains either async for clauses or await expressions it is called an asynchronous
generatorexpression. Anasynchronousgeneratorexpressionreturnsanewasynchronousgeneratorobject,whichis
anasynchronousiterator(seeAsynchronousIterators).
Addedinversion3.6: Asynchronousgeneratorexpressionswereintroduced.
Changedinversion3.7: PriortoPython3.7,asynchronousgeneratorexpressionscouldonlyappearinasync def
coroutines. Startingwith3.7,anyfunctioncanuseasynchronousgeneratorexpressions.
Changedinversion3.8: yieldandyield fromprohibitedintheimplicitlynestedscope.
6.2.9 Yield expressions
yield_atom: "(" yield_expression ")"
yield_from: "yield" "from" expression
yield_expression: "yield" yield_list | yield_from
Theyieldexpressionisusedwhendefiningageneratorfunctionoranasynchronousgeneratorfunctionandthuscan
onlybeusedinthebodyofafunctiondefinition. Usingayieldexpressioninafunction’sbodycausesthatfunction
to be a generator function, and using it in an async def function’s body causes that coroutine function to be an
asynchronousgeneratorfunction. Forexample:
def gen(): # defines a generator function
yield 123
async def agen(): # defines an asynchronous generator function
yield 123
6.2. Atoms 89

### 第98页

Duetotheirsideeffectsonthecontainingscope,yieldexpressionsarenotpermittedaspartoftheimplicitlydefined
scopesusedtoimplementcomprehensionsandgeneratorexpressions.
Changedinversion3.8: Yieldexpressionsprohibitedintheimplicitlynestedscopesusedtoimplementcomprehen-
sionsandgeneratorexpressions.
Generatorfunctionsaredescribedbelow,whileasynchronousgeneratorfunctionsaredescribedseparatelyinsection
Asynchronousgeneratorfunctions.
When a generator function is called, it returns an iterator known as a generator. That generator then controls the
executionofthegeneratorfunction. Theexecutionstartswhenoneofthegenerator’smethodsiscalled. Atthattime,
theexecutionproceedstothefirstyieldexpression,whereitissuspendedagain,returningthevalueofyield_list
tothegenerator’scaller,orNoneifyield_listisomitted. Bysuspended,wemeanthatalllocalstateisretained,
includingthecurrentbindingsoflocalvariables,theinstructionpointer,theinternalevaluationstack,andthestate
ofanyexceptionhandling. Whentheexecutionisresumedbycallingoneofthegenerator’smethods,thefunction
canproceedexactlyasiftheyieldexpressionwerejustanotherexternalcall. Thevalueoftheyieldexpressionafter
resumingdependsonthemethodwhichresumedtheexecution. If__next__()isused(typicallyviaeitherafor
orthenext()builtin)thentheresultisNone. Otherwise,ifsend()isused,thentheresultwillbethevaluepassed
intothatmethod.
Allofthismakesgeneratorfunctionsquitesimilartocoroutines;theyyieldmultipletimes,theyhavemorethanone
entry point and their execution can be suspended. The only difference is that a generator function cannot control
wheretheexecutionshouldcontinueafterityields;thecontrolisalwaystransferredtothegenerator’scaller.
Yield expressions are allowed anywhere in a try construct. If the generator is not resumed before it is finalized
(byreachingazeroreferencecountorbybeinggarbagecollected),thegenerator-iterator’sclose()methodwillbe
called,allowinganypendingfinallyclausestoexecute.
Whenyield from <expr>isused,thesuppliedexpressionmustbeaniterable. Thevaluesproducedbyiterating
thatiterablearepasseddirectlytothecallerofthecurrentgenerator’smethods. Anyvaluespassedinwithsend()
andanyexceptionspassedinwiththrow()arepassedtotheunderlyingiteratorifithastheappropriatemethods.
Ifthisisnotthecase,thensend()willraiseAttributeErrororTypeError,whilethrow()willjustraisethe
passedinexceptionimmediately.
Whentheunderlyingiteratoriscomplete,thevalueattributeoftheraisedStopIterationinstancebecomesthe
valueoftheyieldexpression. ItcanbeeithersetexplicitlywhenraisingStopIteration, orautomaticallywhen
thesubiteratorisagenerator(byreturningavaluefromthesubgenerator).
Changedinversion3.3: Addedyield from <expr>todelegatecontrolflowtoasubiterator.
Theparenthesesmaybeomittedwhentheyieldexpressionisthesoleexpressionontherighthandsideofanassign-
mentstatement.
(cid:181) Seealso
PEP255-SimpleGenerators
TheproposalforaddinggeneratorsandtheyieldstatementtoPython.
PEP342-CoroutinesviaEnhancedGenerators
TheproposaltoenhancetheAPIandsyntaxofgenerators,makingthemusableassimplecoroutines.
PEP380-SyntaxforDelegatingtoaSubgenerator
Theproposaltointroducetheyield_fromsyntax,makingdelegationtosubgeneratorseasy.
PEP525-AsynchronousGenerators
TheproposalthatexpandedonPEP492byaddinggeneratorcapabilitiestocoroutinefunctions.
Generator-iteratormethods
Thissubsectiondescribesthemethodsofageneratoriterator. Theycanbeusedtocontroltheexecutionofagenerator
function.
90 Chapter6. Expressions

| (cid:181) Seealso |
| --- |
| PEP255-SimpleGenerators
TheproposalforaddinggeneratorsandtheyieldstatementtoPython.
PEP342-CoroutinesviaEnhancedGenerators
TheproposaltoenhancetheAPIandsyntaxofgenerators,makingthemusableassimplecoroutines.
PEP380-SyntaxforDelegatingtoaSubgenerator
Theproposaltointroducetheyield_fromsyntax,makingdelegationtosubgeneratorseasy.
PEP525-AsynchronousGenerators
TheproposalthatexpandedonPEP492byaddinggeneratorcapabilitiestocoroutinefunctions. |

### 第99页

NotethatcallinganyofthegeneratormethodsbelowwhenthegeneratorisalreadyexecutingraisesaValueError
exception.
generator.__next__()
Startstheexecutionofageneratorfunctionorresumesitatthelastexecutedyieldexpression. Whenagenerator
functionisresumedwitha__next__()method,thecurrentyieldexpressionalwaysevaluatestoNone. The
executionthencontinuestothenextyieldexpression,wherethegeneratorissuspendedagain,andthevalueof
theyield_listisreturnedto__next__()’scaller. Ifthegeneratorexitswithoutyieldinganothervalue,a
StopIterationexceptionisraised.
Thismethodisnormallycalledimplicitly,e.g. byaforloop,orbythebuilt-innext()function.
generator.send(value)
Resumestheexecutionand“sends”avalueintothegeneratorfunction. Thevalueargumentbecomestheresult
ofthecurrentyieldexpression. Thesend()methodreturnsthenextvalueyieldedbythegenerator,orraises
StopIteration if the generator exits without yielding another value. When send() is called to start the
generator,itmustbecalledwithNoneastheargument,becausethereisnoyieldexpressionthatcouldreceive
thevalue.
generator.throw(value)
[ [ ]]
generator.throw(type ,value ,traceback )
Raises an exception at the point where the generator was paused, and returns the next value yielded by the
generator function. If the generator exits without yielding another value, a StopIteration exception is
raised. Ifthegeneratorfunctiondoesnotcatchthepassed-inexception,orraisesadifferentexception,then
thatexceptionpropagatestothecaller.
Intypicaluse,thisiscalledwithasingleexceptioninstancesimilartothewaytheraisekeywordisused.
Forbackwardscompatibility,however,thesecondsignatureissupported,followingaconventionfromolder
versionsofPython. Thetypeargumentshouldbeanexceptionclass,andvalueshouldbeanexceptioninstance.
Ifthevalueisnotprovided,thetypeconstructoriscalledtogetaninstance. Iftracebackisprovided,itisset
ontheexception,otherwiseanyexisting__traceback__attributestoredinvaluemaybecleared.
Changedinversion3.12: Thesecondsignature(type[,value[,traceback]])isdeprecatedandmayberemoved
inafutureversionofPython.
generator.close()
RaisesaGeneratorExitexceptionatthepointwherethegeneratorfunctionwaspaused(equivalenttocalling
throw(GeneratorExit)). Theexceptionisraisedbytheyieldexpressionwherethegeneratorwaspaused.
Ifthegeneratorfunctioncatchestheexceptionandreturnsavalue,thisvalueisreturnedfromclose(). If
thegeneratorfunctionisalreadyclosed,orraisesGeneratorExit(bynotcatchingtheexception),close()
returns None. If the generator yields a value, a RuntimeError is raised. If the generator raises any other
exception,itispropagatedtothecaller. Ifthegeneratorhasalreadyexitedduetoanexceptionornormalexit,
close()returnsNoneandhasnoothereffect.
Changedinversion3.13: Ifageneratorreturnsavalueuponbeingclosed,thevalueisreturnedbyclose().
Examples
Hereisasimpleexamplethatdemonstratesthebehaviorofgeneratorsandgeneratorfunctions:
>>> def echo(value=None):
... print("Execution starts when 'next()' is called for the first time.")
... try:
... while True:
... try:
... value = (yield value)
... except Exception as e:
... value = e
... finally:
... print("Don't forget to clean up when 'close()' is called.")
(continuesonnextpage)
6.2. Atoms 91

### 第100页

(continuedfrompreviouspage)
...
>>> generator = echo(1)
>>> print(next(generator))
Execution starts when 'next()' is called for the first time.
1
>>> print(next(generator))
None
>>> print(generator.send(2))
2
>>> generator.throw(TypeError, "spam")
TypeError('spam',)
>>> generator.close()
Don't forget to clean up when 'close()' is called.
Forexamplesusingyield from,seepep-380in“What’sNewinPython.”
Asynchronousgeneratorfunctions
Thepresenceofayieldexpressioninafunctionormethoddefinedusingasync deffurtherdefinesthefunctionas
anasynchronousgeneratorfunction.
Whenanasynchronousgeneratorfunctioniscalled, itreturnsanasynchronousiteratorknownasanasynchronous
generatorobject. Thatobjectthencontrolstheexecutionofthegeneratorfunction. Anasynchronousgeneratorobject
istypicallyusedinanasync forstatementinacoroutinefunctionanalogouslytohowageneratorobjectwouldbe
usedinaforstatement.
Callingoneoftheasynchronousgenerator’smethodsreturnsanawaitableobject,andtheexecutionstartswhenthis
objectisawaitedon. Atthattime,theexecutionproceedstothefirstyieldexpression,whereitissuspendedagain,
returningthevalueofyield_listtotheawaitingcoroutine. Aswithagenerator,suspensionmeansthatalllocal
stateisretained,includingthecurrentbindingsoflocalvariables,theinstructionpointer,theinternalevaluationstack,
andthestateofanyexceptionhandling. Whentheexecutionisresumedbyawaitingonthenextobjectreturnedby
theasynchronousgenerator’smethods,thefunctioncanproceedexactlyasiftheyieldexpressionwerejustanother
externalcall. Thevalueoftheyieldexpressionafterresumingdependsonthemethodwhichresumedtheexecution.
If__anext__()isusedthentheresultisNone. Otherwise,ifasend()isused,thentheresultwillbethevalue
passedintothatmethod.
If an asynchronousgeneratorhappensto exit earlyby break, thecallertaskbeingcancelled, orotherexceptions,
thegenerator’sasynccleanupcodewillrunandpossiblyraiseexceptionsoraccesscontextvariablesinanunexpected
context–perhapsafterthelifetimeoftasksitdepends,orduringtheeventloopshutdownwhentheasync-generator
garbage collection hook is called. To prevent this, the caller must explicitly close the async generator by calling
aclose()methodtofinalizethegeneratorandultimatelydetachitfromtheeventloop.
Inanasynchronousgeneratorfunction,yieldexpressionsareallowedanywhereinatry construct. However,ifan
asynchronousgeneratorisnotresumedbeforeitisfinalized(byreachingazeroreferencecountorbybeinggarbage
collected), then a yield expression within a try construct could result in a failure to execute pending finally
clauses. Inthiscase,itistheresponsibilityoftheeventlooporschedulerrunningtheasynchronousgeneratortocall
the asynchronous generator-iterator’s aclose() method and run the resulting coroutine object, thus allowing any
pendingfinallyclausestoexecute.
Totakecareoffinalizationuponeventlooptermination,aneventloopshoulddefineafinalizerfunctionwhichtakes
anasynchronousgenerator-iteratorandpresumablycallsaclose()andexecutesthecoroutine. Thisfinalizermaybe
registeredbycallingsys.set_asyncgen_hooks(). Whenfirstiteratedover,anasynchronousgenerator-iterator
willstoretheregisteredfinalizertobecalleduponfinalization. Forareferenceexampleofafinalizermethodseethe
implementationofasyncio.Loop.shutdown_asyncgensinLib/asyncio/base_events.py.
Theexpressionyield from <expr>isasyntaxerrorwhenusedinanasynchronousgeneratorfunction.
92 Chapter6. Expressions

### 第101页

Asynchronousgenerator-iteratormethods
Thissubsectiondescribesthemethodsofanasynchronousgeneratoriterator,whichareusedtocontroltheexecution
ofageneratorfunction.
async agen.__anext__()
Returnsanawaitablewhichwhenrunstartstoexecutetheasynchronousgeneratororresumesitatthelastexe-
cutedyieldexpression. Whenanasynchronousgeneratorfunctionisresumedwithan__anext__()method,
the current yield expression always evaluates to None in the returned awaitable, which when run will con-
tinuetothenextyieldexpression. Thevalueoftheyield_listoftheyieldexpressionisthevalueofthe
StopIterationexceptionraisedbythecompletingcoroutine. Iftheasynchronousgeneratorexitswithout
yielding another value, the awaitable instead raises a StopAsyncIteration exception, signalling that the
asynchronousiterationhascompleted.
Thismethodisnormallycalledimplicitlybyaasync forloop.
async agen.asend(value)
Returns an awaitable which when run resumes the execution of the asynchronous generator. As with the
send()methodforagenerator,this“sends”avalueintotheasynchronousgeneratorfunction,andthevalue
argumentbecomestheresultofthecurrentyieldexpression. Theawaitablereturnedbytheasend()method
will return the next value yielded by the generator as the value of the raised StopIteration, or raises
StopAsyncIterationiftheasynchronousgeneratorexitswithoutyieldinganothervalue. Whenasend()
iscalledtostarttheasynchronousgenerator,itmustbecalledwithNoneastheargument,becausethereisno
yieldexpressionthatcouldreceivethevalue.
async agen.athrow(value)
[ [ ]]
async agen.athrow(type ,value ,traceback )
Returnsanawaitablethatraisesanexceptionoftypetypeatthepointwheretheasynchronousgeneratorwas
paused,andreturnsthenextvalueyieldedbythegeneratorfunctionasthevalueoftheraisedStopIteration
exception. If the asynchronous generator exits without yielding another value, a StopAsyncIteration
exceptionisraisedbytheawaitable. Ifthegeneratorfunctiondoesnotcatchthepassed-inexception,orraises
adifferentexception,thenwhentheawaitableisrunthatexceptionpropagatestothecalleroftheawaitable.
Changedinversion3.12: Thesecondsignature(type[,value[,traceback]])isdeprecatedandmayberemoved
inafutureversionofPython.
async agen.aclose()
Returns an awaitable that when run will throw a GeneratorExit into the asynchronous generator func-
tion at the point where it was paused. If the asynchronous generator function then exits gracefully, is al-
ready closed, or raises GeneratorExit (by not catching the exception), then the returned awaitable will
raiseaStopIterationexception. Anyfurtherawaitablesreturnedbysubsequentcallstotheasynchronous
generator will raise a StopAsyncIteration exception. If the asynchronous generator yields a value, a
RuntimeError is raised by the awaitable. If the asynchronous generator raises any other exception, it is
propagatedtothecalleroftheawaitable. Iftheasynchronousgeneratorhasalreadyexitedduetoanexception
ornormalexit,thenfurthercallstoaclose()willreturnanawaitablethatdoesnothing.
6.3 Primaries
Primariesrepresentthemosttightlyboundoperationsofthelanguage. Theirsyntaxis:
primary: atom | attributeref | subscription | slicing | call
6.3.1 Attribute references
Anattributereferenceisaprimaryfollowedbyaperiodandaname:
attributeref: primary "." identifier
The primary must evaluate to an object of a type that supports attribute references, which most objects do. This
objectisthenaskedtoproducetheattributewhosenameistheidentifier. Thetypeandvalueproducedisdetermined
bytheobject. Multipleevaluationsofthesameattributereferencemayyielddifferentobjects.
6.3. Primaries 93

### 第102页

This production can be customized by overriding the __getattribute__() method or the __getattr__()
method. The__getattribute__()methodiscalledfirstandeitherreturnsavalueorraisesAttributeError
iftheattributeisnotavailable.
IfanAttributeErrorisraisedandtheobjecthasa__getattr__()method,thatmethodiscalledasafallback.
6.3.2 Subscriptions
The subscription of an instance of a container class will generally select an element from the container. The sub-
scriptionofagenericclasswillgenerallyreturnaGenericAliasobject.
subscription: primary "[" flexible_expression_list "]"
Whenanobjectissubscripted,theinterpreterwillevaluatetheprimaryandtheexpressionlist.
Theprimarymustevaluatetoanobjectthatsupportssubscription. Anobjectmaysupportsubscriptionthroughdefin-
ingoneorbothof__getitem__()and__class_getitem__(). Whentheprimaryissubscripted,theevaluated
resultoftheexpressionlistwillbepassedtooneofthesemethods. Formoredetailsonwhen__class_getitem__
iscalledinsteadof__getitem__,see__class_getitem__versus__getitem__.
If the expression list contains at least one comma, or if any of the expressions are starred, the expression list will
evaluate to a tuple containing the items of the expression list. Otherwise, the expression list will evaluate to the
valueofthelist’ssolemember.
Changedinversion3.11: Expressionsinanexpressionlistmaybestarred. SeePEP646.
Forbuilt-inobjects,therearetwotypesofobjectsthatsupportsubscriptionvia__getitem__():
1. Mappings. Iftheprimaryisamapping,theexpressionlistmustevaluatetoanobjectwhosevalueisoneofthe
keysofthemapping,andthesubscriptionselectsthevalueinthemappingthatcorrespondstothatkey. An
exampleofabuiltinmappingclassisthedictclass.
2. Sequences. Iftheprimaryisasequence,theexpressionlistmustevaluatetoanintoraslice(asdiscussed
inthefollowingsection). Examplesofbuiltinsequenceclassesincludethestr,listandtupleclasses.
The formal syntax makes no special provision for negative indices in sequences. However, built-in sequences all
providea__getitem__()methodthatinterpretsnegativeindicesbyaddingthelengthofthesequencetotheindex
sothat, forexample, x[-1]selectsthelastitemofx. Theresultingvaluemustbeanonnegativeintegerlessthan
thenumberofitemsinthesequence,andthesubscriptionselectstheitemwhoseindexisthatvalue(countingfrom
zero). Sincethesupportfornegativeindicesandslicingoccursintheobject’s__getitem__()method,subclasses
overridingthismethodwillneedtoexplicitlyaddthatsupport.
Astringisaspecialkindofsequencewhoseitemsarecharacters. Acharacterisnotaseparatedatatypebuta
stringofexactlyonecharacter.
6.3.3 Slicings
Aslicingselectsarangeofitemsinasequenceobject(e.g.,astring,tupleorlist). Slicingsmaybeusedasexpressions
orastargetsinassignmentordelstatements. Thesyntaxforaslicing:
slicing: primary "[" slice_list "]"
slice_list: slice_item ("," slice_item)* [","]
slice_item: expression | proper_slice
proper_slice: [lower_bound] ":" [upper_bound] [ ":" [stride] ]
lower_bound: expression
upper_bound: expression
stride: expression
Thereisambiguityintheformalsyntaxhere: anythingthatlookslikeanexpressionlistalsolookslikeaslicelist,so
anysubscriptioncanbeinterpretedasaslicing. Ratherthanfurthercomplicatingthesyntax,thisisdisambiguated
bydefiningthatinthiscasetheinterpretationasasubscriptiontakespriorityovertheinterpretationasaslicing(this
isthecaseiftheslicelistcontainsnoproperslice).
The semantics for a slicing are as follows. The primary is indexed (using the same __getitem__() method as
normalsubscription)withakeythatisconstructedfromtheslicelist,asfollows. Iftheslicelistcontainsatleastone
94 Chapter6. Expressions

### 第103页

comma,thekeyisatuplecontainingtheconversionofthesliceitems;otherwise,theconversionofthelonesliceitem
isthekey. Theconversionofasliceitemthatisanexpressionisthatexpression. Theconversionofapropersliceis
asliceobject(seesectionThestandardtypehierarchy)whosestart,stopandstepattributesarethevaluesofthe
expressionsgivenaslowerbound,upperboundandstride,respectively,substitutingNoneformissingexpressions.
6.3.4 Calls
Acallcallsacallableobject(e.g.,afunction)withapossiblyemptyseriesofarguments:
call: primary "(" [argument_list [","] | comprehension] ")"
argument_list: positional_arguments ["," starred_and_keywords]
["," keywords_arguments]
| starred_and_keywords ["," keywords_arguments]
| keywords_arguments
positional_arguments: positional_item ("," positional_item)*
positional_item: assignment_expression | "*" expression
starred_and_keywords: ("*" expression | keyword_item)
("," "*" expression | "," keyword_item)*
keywords_arguments: (keyword_item | "**" expression)
("," keyword_item | "," "**" expression)*
keyword_item: identifier "=" expression
An optional trailing comma may be present after the positional and keyword arguments but does not affect the
semantics.
Theprimarymustevaluatetoacallableobject(user-definedfunctions,built-infunctions,methodsofbuilt-inobjects,
classobjects,methodsofclassinstances,andallobjectshavinga__call__()methodarecallable). Allargument
expressionsareevaluatedbeforethecallisattempted. PleaserefertosectionFunctiondefinitionsforthesyntaxof
formalparameterlists.
Ifkeywordargumentsarepresent,theyarefirstconvertedtopositionalarguments,asfollows. First,alistofunfilled
slotsiscreatedfortheformalparameters. IfthereareNpositionalarguments, theyareplacedinthefirstNslots.
Next,foreachkeywordargument,theidentifierisusedtodeterminethecorrespondingslot(iftheidentifieristhe
sameasthefirstformalparametername,thefirstslotisused,andsoon). Iftheslotisalreadyfilled,aTypeError
exceptionisraised. Otherwise,theargumentisplacedintheslot,fillingit(eveniftheexpressionisNone,itfillsthe
slot). Whenallargumentshavebeenprocessed,theslotsthatarestillunfilledarefilledwiththecorrespondingdefault
valuefromthefunctiondefinition. (Defaultvaluesarecalculated,once,whenthefunctionisdefined;thus,amutable
objectsuchasalistordictionaryusedasdefaultvaluewillbesharedbyallcallsthatdon’tspecifyanargumentvalue
forthecorrespondingslot;thisshouldusuallybeavoided.) Ifthereareanyunfilledslotsforwhichnodefaultvalueis
specified,aTypeErrorexceptionisraised. Otherwise,thelistoffilledslotsisusedastheargumentlistforthecall.
CPythonimplementationdetail: Animplementationmayprovidebuilt-infunctionswhosepositionalparameters
donothavenames,eveniftheyare‘named’forthepurposeofdocumentation,andwhichthereforecannotbesupplied
bykeyword. InCPython,thisisthecaseforfunctionsimplementedinCthatusePyArg_ParseTuple()toparse
theirarguments.
Iftherearemorepositionalargumentsthanthereareformalparameterslots,aTypeErrorexceptionisraised,unless
aformalparameterusingthesyntax*identifierispresent; inthiscase, thatformalparameterreceivesatuple
containingtheexcesspositionalarguments(oranemptytupleiftherewerenoexcesspositionalarguments).
Ifanykeywordargumentdoesnotcorrespondtoaformalparametername,aTypeErrorexceptionisraised,unlessa
formalparameterusingthesyntax**identifierispresent;inthiscase,thatformalparameterreceivesadictionary
containing the excess keyword arguments (using the keywords as keys and the argument values as corresponding
values),ora(new)emptydictionaryiftherewerenoexcesskeywordarguments.
Ifthesyntax*expressionappearsinthefunctioncall,expressionmustevaluatetoaniterable. Elementsfrom
theseiterablesaretreatedasiftheywereadditionalpositionalarguments. Forthecallf(x1, x2, *y, x3, x4),
ifyevaluatestoasequencey1,…,yM,thisisequivalenttoacallwithM+4positionalargumentsx1,x2,y1,…,yM,
x3,x4.
Aconsequenceofthisisthatalthoughthe*expressionsyntaxmayappearafterexplicitkeywordarguments,itis
processedbeforethekeywordarguments(andany**expressionarguments–seebelow). So:
6.3. Primaries 95

### 第104页

>>> def f(a, b):
... print(a, b)
...
>>> f(b=1, *(2,))
2 1
>>> f(a=1, *(2,))
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: f() got multiple values for keyword argument 'a'
>>> f(1, *(2,))
1 2
Itisunusualforbothkeywordargumentsandthe*expressionsyntaxtobeusedinthesamecall,soinpractice
thisconfusiondoesnotoftenarise.
Ifthesyntax**expressionappearsinthefunctioncall, expressionmustevaluatetoamapping, thecontents
ofwhicharetreatedasadditionalkeywordarguments. Ifaparametermatchingakeyhasalreadybeengivenavalue
(byanexplicitkeywordargument,orfromanotherunpacking),aTypeErrorexceptionisraised.
When**expressionisused,eachkeyinthismappingmustbeastring. Eachvaluefromthemappingisassigned
tothefirstformalparametereligibleforkeywordassignmentwhosenameisequaltothekey. Akeyneednotbea
Pythonidentifier(e.g. "max-temp °F"isacceptable,althoughitwillnotmatchanyformalparameterthatcouldbe
declared). Ifthereisnomatchtoaformalparameterthekey-valuepairiscollectedbythe**parameter,ifthereis
one,orifthereisnot,aTypeErrorexceptionisraised.
Formalparametersusingthesyntax*identifieror**identifiercannotbeusedaspositionalargumentslots
oraskeywordargumentnames.
Changedinversion3.5: Functioncallsacceptanynumberof*and**unpackings,positionalargumentsmayfollow
iterable unpackings (*), and keyword arguments may follow dictionary unpackings (**). Originally proposed by
PEP448.
Acallalwaysreturnssomevalue,possiblyNone,unlessitraisesanexception. Howthisvalueiscomputeddepends
onthetypeofthecallableobject.
Ifitis—
auser-definedfunction:
Thecodeblockforthefunctionisexecuted,passingittheargumentlist. Thefirstthingthecodeblockwilldo
isbindtheformalparameterstothearguments;thisisdescribedinsectionFunctiondefinitions. Whenthecode
blockexecutesareturnstatement, thisspecifiesthereturnvalueofthefunctioncall. Ifexecutionreaches
theendofthecodeblockwithoutexecutingareturnstatement,thereturnvalueisNone.
abuilt-infunctionormethod:
Theresultisuptotheinterpreter;seebuilt-in-funcsforthedescriptionsofbuilt-infunctionsandmethods.
aclassobject:
Anewinstanceofthatclassisreturned.
aclassinstancemethod:
Thecorrespondinguser-definedfunctioniscalled,withanargumentlistthatisonelongerthantheargument
listofthecall: theinstancebecomesthefirstargument.
aclassinstance:
Theclassmustdefinea__call__()method;theeffectisthenthesameasifthatmethodwascalled.
6.4 Await expression
Suspendtheexecutionofcoroutineonanawaitableobject. Canonlybeusedinsideacoroutinefunction.
await_expr: "await" primary
Addedinversion3.5.
96 Chapter6. Expressions

### 第105页

6.5 The power operator
Thepoweroperatorbindsmoretightlythanunaryoperatorsonitsleft;itbindslesstightlythanunaryoperatorson
itsright. Thesyntaxis:
power: (await_expr | primary) ["**" u_expr]
Thus, inanunparenthesizedsequenceofpowerandunaryoperators, theoperatorsareevaluatedfromrighttoleft
(thisdoesnotconstraintheevaluationorderfortheoperands): -1**2resultsin-1.
Thepoweroperatorhasthesamesemanticsasthebuilt-inpow()function,whencalledwithtwoarguments: ityields
itsleftargumentraisedtothepowerofitsrightargument. Thenumericargumentsarefirstconvertedtoacommon
type,andtheresultisofthattype.
Forintoperands,theresulthasthesametypeastheoperandsunlessthesecondargumentisnegative;inthatcase,all
argumentsareconvertedtofloatandafloatresultisdelivered. Forexample,10**2returns100,but10**-2returns
0.01.
Raising0.0toanegativepowerresultsinaZeroDivisionError. Raisinganegativenumbertoafractionalpower
resultsinacomplexnumber. (InearlierversionsitraisedaValueError.)
Thisoperationcanbecustomizedusingthespecial__pow__()and__rpow__()methods.
6.6 Unary arithmetic and bitwise operations
Allunaryarithmeticandbitwiseoperationshavethesamepriority:
u_expr: power | "-" u_expr | "+" u_expr | "~" u_expr
Theunary-(minus)operatoryieldsthenegationofitsnumericargument;theoperationcanbeoverriddenwiththe
__neg__()specialmethod.
The unary + (plus) operator yields its numeric argument unchanged; the operation can be overridden with the
__pos__()specialmethod.
The unary ~ (invert) operator yields the bitwise inversion of its integer argument. The bitwise inversion of x is
definedas-(x+1). Itonlyappliestointegralnumbersortocustomobjectsthatoverridethe__invert__()special
method.
Inallthreecases,iftheargumentdoesnothavethepropertype,aTypeErrorexceptionisraised.
6.7 Binary arithmetic operations
The binary arithmetic operations have the conventional priority levels. Note that some of these operations also
applytocertainnon-numerictypes. Apartfromthepoweroperator,thereareonlytwolevels,oneformultiplicative
operatorsandoneforadditiveoperators:
m_expr: u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
m_expr "//" u_expr | m_expr "/" u_expr |
m_expr "%" u_expr
a_expr: m_expr | a_expr "+" m_expr | a_expr "-" m_expr
The*(multiplication)operatoryieldstheproductofitsarguments. Theargumentsmusteitherbothbenumbers,or
oneargumentmustbeanintegerandtheothermustbeasequence. Intheformercase,thenumbersareconverted
toacommonrealtypeandthenmultipliedtogether. Inthelattercase,sequencerepetitionisperformed;anegative
repetitionfactoryieldsanemptysequence.
Thisoperationcanbecustomizedusingthespecial__mul__()and__rmul__()methods.
Changedinversion3.14: Ifonlyoneoperandisacomplexnumber,theotheroperandisconvertedtoafloating-point
number.
The@(at)operatorisintendedtobeusedformatrixmultiplication. NobuiltinPythontypesimplementthisoperator.
6.5. Thepoweroperator 97

### 第106页

Thisoperationcanbecustomizedusingthespecial__matmul__()and__rmatmul__()methods.
Addedinversion3.5.
The/(division)and//(floordivision)operatorsyieldthequotientoftheirarguments. Thenumericargumentsare
first converted to a common type. Division of integers yields a float, while floor division of integers results in an
integer; the result is that of mathematical division with the ‘floor’ function applied to the result. Division by zero
raisestheZeroDivisionErrorexception.
Thedivisionoperationcanbecustomizedusingthespecial__truediv__()and__rtruediv__()methods. The
floordivisionoperationcanbecustomizedusingthespecial__floordiv__()and__rfloordiv__()methods.
The%(modulo)operatoryieldstheremainderfromthedivisionofthefirstargumentbythesecond. Thenumeric
argumentsarefirstconvertedtoacommontype. AzerorightargumentraisestheZeroDivisionErrorexception.
Theargumentsmaybefloating-pointnumbers,e.g.,3.14%0.7equals0.34(since3.14equals4*0.7 + 0.34.)
Themodulooperatoralwaysyieldsaresultwiththesamesignasitssecondoperand(orzero);theabsolutevalueof
theresultisstrictlysmallerthantheabsolutevalueofthesecondoperand1.
Thefloordivisionandmodulooperatorsareconnectedbythefollowingidentity: x == (x//y)*y + (x%y). Floor
divisionandmoduloarealsoconnectedwiththebuilt-infunctiondivmod():divmod(x, y) == (x//y, x%y).2.
Inadditiontoperformingthemodulooperationonnumbers, the%operatorisalsooverloadedbystringobjectsto
performold-stylestringformatting(alsoknownasinterpolation). Thesyntaxforstringformattingisdescribedinthe
PythonLibraryReference,sectionold-string-formatting.
Themodulooperationcanbecustomizedusingthespecial__mod__()and__rmod__()methods.
Thefloordivisionoperator,themodulooperator,andthedivmod()functionarenotdefinedforcomplexnumbers.
Instead,converttoafloating-pointnumberusingtheabs()functionifappropriate.
The+(addition)operatoryieldsthesumofitsarguments. Theargumentsmusteitherbothbenumbersorbothbe
sequencesofthesametype. Intheformercase,thenumbersareconvertedtoacommonrealtypeandthenadded
together. Inthelattercase,thesequencesareconcatenated.
Thisoperationcanbecustomizedusingthespecial__add__()and__radd__()methods.
Changedinversion3.14: Ifonlyoneoperandisacomplexnumber,theotheroperandisconvertedtoafloating-point
number.
The-(subtraction)operatoryieldsthedifferenceofitsarguments. Thenumericargumentsarefirstconvertedtoa
commonrealtype.
Thisoperationcanbecustomizedusingthespecial__sub__()and__rsub__()methods.
Changedinversion3.14: Ifonlyoneoperandisacomplexnumber,theotheroperandisconvertedtoafloating-point
number.
6.8 Shifting operations
Theshiftingoperationshavelowerprioritythanthearithmeticoperations:
shift_expr: a_expr | shift_expr ("<<" | ">>") a_expr
Theseoperatorsacceptintegersasarguments. Theyshiftthefirstargumenttotheleftorrightbythenumberofbits
givenbythesecondargument.
Theleftshiftoperationcanbecustomizedusingthespecial__lshift__()and__rlshift__()methods. The
rightshiftoperationcanbecustomizedusingthespecial__rshift__()and__rrshift__()methods.
1Whileabs(x%y) < abs(y)istruemathematically,forfloatsitmaynotbetruenumericallyduetoroundoff.Forexample,andassuming
aplatformonwhichaPythonfloatisanIEEE754double-precisionnumber,inorderthat-1e-100 % 1e100havethesamesignas1e100,
thecomputedresultis-1e-100 + 1e100,whichisnumericallyexactlyequalto1e100. Thefunctionmath.fmod()returnsaresultwhose
signmatchesthesignofthefirstargumentinstead,andsoreturns-1e-100inthiscase. Whichapproachismoreappropriatedependsonthe
application.
2Ifxisveryclosetoanexactintegermultipleofy,it’spossibleforx//ytobeonelargerthan(x-x%y)//yduetorounding.Insuchcases,
Pythonreturnsthelatterresult,inordertopreservethatdivmod(x,y)[0] * y + x % ybeveryclosetox.
98 Chapter6. Expressions

### 第107页

Arightshiftbynbitsisdefinedasfloordivisionbypow(2,n). Aleftshiftbynbitsisdefinedasmultiplicationwith
pow(2,n).
6.9 Binary bitwise operations
Eachofthethreebitwiseoperationshasadifferentprioritylevel:
and_expr: shift_expr | and_expr "&" shift_expr
xor_expr: and_expr | xor_expr "^" and_expr
or_expr: xor_expr | or_expr "|" xor_expr
The&operatoryieldsthebitwiseANDofitsarguments,whichmustbeintegersoroneofthemmustbeacustom
objectoverriding__and__()or__rand__()specialmethods.
The^operatoryieldsthebitwiseXOR(exclusiveOR)ofitsarguments,whichmustbeintegersoroneofthemmust
beacustomobjectoverriding__xor__()or__rxor__()specialmethods.
The|operatoryieldsthebitwise(inclusive)ORofitsarguments,whichmustbeintegersoroneofthemmustbea
customobjectoverriding__or__()or__ror__()specialmethods.
6.10 Comparisons
Unlike C, all comparison operations in Python have the same priority, which is lower than that of any arithmetic,
shiftingorbitwiseoperation. AlsounlikeC,expressionslikea < b < chavetheinterpretationthatisconventional
inmathematics:
comparison: or_expr (comp_operator or_expr)*
comp_operator: "<" | ">" | "==" | ">=" | "<=" | "!="
| "is" ["not"] | ["not"] "in"
Comparisonsyieldbooleanvalues:TrueorFalse. Customrichcomparisonmethodsmayreturnnon-booleanvalues.
InthiscasePythonwillcallbool()onsuchvalueinbooleancontexts.
Comparisonscanbechainedarbitrarily,e.g.,x < y <= zisequivalenttox < y and y <= z,exceptthatyis
evaluatedonlyonce(butinbothcaseszisnotevaluatedatallwhenx < yisfoundtobefalse).
Formally,ifa, b, c,…, y, zareexpressionsandop1, op2,…, opN arecomparisonoperators,thena op1 b op2
c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z, except that each expression is
evaluatedatmostonce.
Note that a op1 b op2 c doesn’t imply any kind of comparison between a and c, so that, e.g., x < y > z is
perfectlylegal(thoughperhapsnotpretty).
6.10.1 Value comparisons
Theoperators<,>,==,>=,<=,and!=comparethevaluesoftwoobjects. Theobjectsdonotneedtohavethesame
type.
ChapterObjects,valuesandtypesstatesthatobjectshaveavalue(inadditiontotypeandidentity). Thevalueofan
objectisaratherabstractnotioninPython: Forexample,thereisnocanonicalaccessmethodforanobject’svalue.
Also,thereisnorequirementthatthevalueofanobjectshouldbeconstructedinaparticularway,e.g. comprised
ofallitsdataattributes. Comparisonoperatorsimplementaparticularnotionofwhatthevalueofanobjectis. One
canthinkofthemasdefiningthevalueofanobjectindirectly,bymeansoftheircomparisonimplementation.
Because all types are (direct or indirect) subtypes of object, they inherit the default comparison behavior from
object. Typescancustomizetheircomparisonbehaviorbyimplementingrichcomparisonmethodslike__lt__(),
describedinBasiccustomization.
Thedefaultbehaviorforequalitycomparison(==and!=)isbasedontheidentityoftheobjects. Hence, equality
comparisonofinstanceswiththesameidentityresultsinequality,andequalitycomparisonofinstanceswithdifferent
identitiesresultsininequality. Amotivationforthisdefaultbehavioristhedesirethatallobjectsshouldbereflexive
(i.e. x is yimpliesx == y).
6.9. Binarybitwiseoperations 99

### 第108页

Adefaultordercomparison(<,>,<=,and>=)isnotprovided;anattemptraisesTypeError. Amotivationforthis
defaultbehavioristhelackofasimilarinvariantasforequality.
Thebehaviorofthedefaultequalitycomparison,thatinstanceswithdifferentidentitiesarealwaysunequal,maybe
incontrasttowhattypeswillneedthathaveasensibledefinitionofobjectvalueandvalue-basedequality. Suchtypes
willneedtocustomizetheircomparisonbehavior,andinfact,anumberofbuilt-intypeshavedonethat.
Thefollowinglistdescribesthecomparisonbehaviorofthemostimportantbuilt-intypes.
• Numbersofbuilt-innumerictypes(typesnumeric)andofthestandardlibrarytypesfractions.Fraction
anddecimal.Decimalcanbecomparedwithinandacrosstheirtypes,withtherestrictionthatcomplexnum-
bersdonotsupportordercomparison. Withinthelimitsofthetypesinvolved,theycomparemathematically
(algorithmically)correctwithoutlossofprecision.
Thenot-a-numbervaluesfloat('NaN')anddecimal.Decimal('NaN')arespecial. Anyorderedcom-
parison of a number to a not-a-number value is false. A counter-intuitive implication is that not-a-number
valuesarenotequaltothemselves. Forexample,ifx = float('NaN'),3 < x,x < 3andx == xareall
false,whilex != xistrue. ThisbehavioriscompliantwithIEEE754.
• NoneandNotImplementedaresingletons. PEP8advisesthatcomparisonsforsingletonsshouldalwaysbe
donewithisoris not,nevertheequalityoperators.
• Binarysequences(instancesofbytesorbytearray)canbecomparedwithinandacrosstheirtypes. They
comparelexicographicallyusingthenumericvaluesoftheirelements.
• Strings(instancesofstr)comparelexicographicallyusingthenumericalUnicodecodepoints(theresultof
thebuilt-infunctionord())oftheircharacters.3
Stringsandbinarysequencescannotbedirectlycompared.
• Sequences(instancesoftuple,list,orrange)canbecomparedonlywithineachoftheirtypes,withthe
restriction that ranges do not support order comparison. Equality comparison across these types results in
inequality,andorderingcomparisonacrossthesetypesraisesTypeError.
Sequences compare lexicographically using comparison of corresponding elements. The built-in containers
typically assume identical objects are equal to themselves. That lets them bypass equality tests for identical
objectstoimproveperformanceandtomaintaintheirinternalinvariants.
Lexicographicalcomparisonbetweenbuilt-incollectionsworksasfollows:
– For two collections to compare equal, they must be of the same type, have the same length, and each
pair of corresponding elements must compare equal (for example, [1,2] == (1,2) is false because
thetypeisnotthesame).
– Collectionsthatsupportordercomparisonareorderedthesameastheirfirstunequalelements(forex-
ample, [1,2,x] <= [1,2,y] has the same value as x <= y). If a corresponding element does not
exist,theshortercollectionisorderedfirst(forexample,[1,2] < [1,2,3]istrue).
• Mappings(instancesofdict)compareequalifandonlyiftheyhaveequal(key, value)pairs. Equality
comparisonofthekeysandvaluesenforcesreflexivity.
Ordercomparisons(<,>,<=,and>=)raiseTypeError.
• Sets(instancesofsetorfrozenset)canbecomparedwithinandacrosstheirtypes.
Theydefineordercomparisonoperatorstomeansubsetandsupersettests. Thoserelationsdonotdefinetotal
orderings(forexample,thetwosets{1,2}and{2,3}arenotequal,norsubsetsofoneanother,norsupersets
ofoneanother). Accordingly,setsarenotappropriateargumentsforfunctionswhichdependontotalordering
(forexample,min(),max(),andsorted()produceundefinedresultsgivenalistofsetsasinputs).
3TheUnicodestandarddistinguishesbetweencodepoints(e.g.U+0041)andabstractcharacters(e.g.“LATINCAPITALLETTERA”).While
mostabstractcharactersinUnicodeareonlyrepresentedusingonecodepoint,thereisanumberofabstractcharactersthatcaninadditionbe
representedusingasequenceofmorethanonecodepoint.Forexample,theabstractcharacter“LATINCAPITALLETTERCWITHCEDILLA”
canberepresentedasasingleprecomposedcharacteratcodepositionU+00C7,orasasequenceofabasecharacteratcodepositionU+0043
(LATINCAPITALLETTERC),followedbyacombiningcharacteratcodepositionU+0327(COMBININGCEDILLA).
ThecomparisonoperatorsonstringscompareatthelevelofUnicodecodepoints. Thismaybecounter-intuitivetohumans. Forexample,
"\u00C7" == "\u0043\u0327"isFalse,eventhoughbothstringsrepresentthesameabstractcharacter“LATINCAPITALLETTERC
WITHCEDILLA”.
Tocomparestringsatthelevelofabstractcharacters(thatis,inawayintuitivetohumans),useunicodedata.normalize().
100 Chapter6. Expressions

### 第109页

Comparisonofsetsenforcesreflexivityofitselements.
• Mostotherbuilt-intypeshavenocomparisonmethodsimplemented, sotheyinheritthedefaultcomparison
behavior.
User-definedclassesthatcustomizetheircomparisonbehaviorshouldfollowsomeconsistencyrules,ifpossible:
• Equalitycomparisonshouldbereflexive. Inotherwords,identicalobjectsshouldcompareequal:
x is yimpliesx == y
• Comparisonshouldbesymmetric. Inotherwords,thefollowingexpressionsshouldhavethesameresult:
x == yandy == x
x != yandy != x
x < yandy > x
x <= yandy >= x
• Comparisonshouldbetransitive. Thefollowing(non-exhaustive)examplesillustratethat:
x > y and y > zimpliesx > z
x < y and y <= zimpliesx < z
• Inverse comparison should result in the boolean negation. In other words, the following expressions should
havethesameresult:
x == yandnot x != y
x < yandnot x >= y(fortotalordering)
x > yandnot x <= y(fortotalordering)
Thelasttwoexpressionsapplytototallyorderedcollections(e.g. tosequences,butnottosetsormappings).
Seealsothetotal_ordering()decorator.
• Thehash()resultshouldbeconsistentwithequality. Objectsthatareequalshouldeitherhavethesamehash
value,orbemarkedasunhashable.
Pythondoesnotenforcetheseconsistencyrules. Infact,thenot-a-numbervaluesareanexamplefornotfollowing
theserules.
6.10.2 Membership test operations
Theoperatorsinandnot intestformembership. x in sevaluatestoTrueifx isamemberofs, andFalse
otherwise. x not in sreturnsthenegationofx in s. Allbuilt-insequencesandsettypessupportthisaswell
asdictionary,forwhichintestswhetherthedictionaryhasagivenkey. Forcontainertypessuchaslist,tuple,set,
frozenset,dict,orcollections.deque,theexpressionx in yisequivalenttoany(x is e or x == e for e in
y).
Forthestringandbytestypes,x in yisTrueifandonlyifxisasubstringofy. Anequivalenttestisy.find(x)
!= -1. Emptystringsarealwaysconsideredtobeasubstringofanyotherstring,so"" in "abc"willreturnTrue.
For user-defined classes which define the __contains__() method, x in y returns True if y.
__contains__(x)returnsatruevalue,andFalseotherwise.
Foruser-definedclasseswhichdonotdefine__contains__()butdodefine__iter__(),x in yisTrueifsome
valuez,forwhichtheexpressionx is z or x == zistrue,isproducedwhileiteratingovery. Ifanexceptionis
raisedduringtheiteration,itisasifinraisedthatexception.
Lastly, theold-styleiterationprotocolistried: ifaclassdefines__getitem__(), x in yisTrueifandonlyif
thereisanon-negativeintegerindexisuchthatx is y[i] or x == y[i],andnolowerintegerindexraisesthe
IndexErrorexception. (Ifanyotherexceptionisraised,itisasifinraisedthatexception).
Theoperatornot inisdefinedtohavetheinversetruthvalueofin.
6.10. Comparisons 101

### 第110页

6.10.3 Identity comparisons
Theoperatorsisandis nottestforanobject’sidentity: x is yistrueifandonlyifxandyarethesameobject.
AnObject’sidentityisdeterminedusingtheid()function. x is not yyieldstheinversetruthvalue.4
6.11 Boolean operations
or_test: and_test | or_test "or" and_test
and_test: not_test | and_test "and" not_test
not_test: comparison | "not" not_test
InthecontextofBooleanoperations,andalsowhenexpressionsareusedbycontrolflowstatements,thefollowing
valuesareinterpretedasfalse: False,None,numericzeroofalltypes,andemptystringsandcontainers(including
strings,tuples,lists,dictionaries,setsandfrozensets). Allothervaluesareinterpretedastrue. User-definedobjects
cancustomizetheirtruthvaluebyprovidinga__bool__()method.
TheoperatornotyieldsTrueifitsargumentisfalse,Falseotherwise.
Theexpressionx and yfirstevaluatesx;ifxisfalse,itsvalueisreturned;otherwise,yisevaluatedandtheresulting
valueisreturned.
Theexpressionx or yfirstevaluatesx;ifxistrue,itsvalueisreturned;otherwise,yisevaluatedandtheresulting
valueisreturned.
Notethatneitherand noror restrictthevalueandtypetheyreturntoFalseandTrue,butratherreturnthelast
evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced by a default value if it
isempty,theexpressions or 'foo'yieldsthedesiredvalue. Becausenothastocreateanewvalue,itreturnsa
booleanvalueregardlessofthetypeofitsargument(forexample,not 'foo'producesFalseratherthan''.)
6.12 Assignment expressions
assignment_expression: [identifier ":="] expression
Anassignmentexpression(sometimesalsocalleda“namedexpression”or“walrus”)assignsanexpressiontoan
identifier,whilealsoreturningthevalueoftheexpression.
Onecommonusecaseiswhenhandlingmatchedregularexpressions:
if matching := pattern.search(data):
do_something(matching)
Or,whenprocessingafilestreaminchunks:
while chunk := file.read(9000):
process(chunk)
Assignment expressions must be surrounded by parentheses when used as expression statements and when used
as sub-expressions in slicing, conditional, lambda, keyword-argument, and comprehension-if expressions and in
assert, with, and assignment statements. In all other places where they can be used, parentheses are not re-
quired,includinginifandwhilestatements.
Addedinversion3.8: SeePEP572formoredetailsaboutassignmentexpressions.
6.13 Conditional expressions
conditional_expression: or_test ["if" or_test "else" expression]
expression: conditional_expression | lambda_expr
4Duetoautomaticgarbage-collection,freelists,andthedynamicnatureofdescriptors,youmaynoticeseeminglyunusualbehaviourincertain
usesoftheisoperator,likethoseinvolvingcomparisonsbetweeninstancemethods,orconstants.Checktheirdocumentationformoreinfo.
102 Chapter6. Expressions

### 第111页

Conditionalexpressions(sometimescalleda“ternaryoperator”)havethelowestpriorityofallPythonoperations.
The expression x if C else y first evaluates the condition, C rather than x. If C is true, x is evaluated and its
valueisreturned;otherwise,yisevaluatedanditsvalueisreturned.
SeePEP308formoredetailsaboutconditionalexpressions.
6.14 Lambdas
lambda_expr: "lambda" [parameter_list] ":" expression
Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. The expression
lambda parameters: expressionyieldsafunctionobject. Theunnamedobjectbehaveslikeafunctionobject
definedwith:
def <lambda>(parameters):
return expression
SeesectionFunctiondefinitionsforthesyntaxofparameterlists. Notethatfunctionscreatedwithlambdaexpressions
cannotcontainstatementsorannotations.
6.15 Expression lists
starred_expression: "*" or_expr | expression
flexible_expression: assignment_expression | starred_expression
flexible_expression_list: flexible_expression ("," flexible_expression)* [","]
starred_expression_list: starred_expression ("," starred_expression)* [","]
expression_list: expression ("," expression)* [","]
yield_list: expression_list | starred_expression "," [starred_expression_
Exceptwhenpartofalistorsetdisplay,anexpressionlistcontainingatleastonecommayieldsatuple. Thelength
ofthetupleisthenumberofexpressionsinthelist. Theexpressionsareevaluatedfromlefttoright.
Anasterisk*denotesiterableunpacking. Itsoperandmustbeaniterable. Theiterableisexpandedintoasequence
ofitems,whichareincludedinthenewtuple,list,orset,atthesiteoftheunpacking.
Addedinversion3.5: Iterableunpackinginexpressionlists,originallyproposedbyPEP448.
Addedinversion3.11: Anyiteminanexpressionlistmaybestarred. SeePEP646.
Atrailingcommaisrequiredonlytocreateaone-itemtuple, suchas1,; itisoptionalinallothercases. Asingle
expressionwithoutatrailingcommadoesn’tcreateatuple,butratheryieldsthevalueofthatexpression. (Tocreate
anemptytuple,useanemptypairofparentheses: ().)
6.16 Evaluation order
Python evaluates expressions from left to right. Notice that while evaluating an assignment, the right-hand side is
evaluatedbeforetheleft-handside.
Inthefollowinglines,expressionswillbeevaluatedinthearithmeticorderoftheirsuffixes:
expr1, expr2, expr3, expr4
(expr1, expr2, expr3, expr4)
{expr1: expr2, expr3: expr4}
expr1 + expr2 * (expr3 - expr4)
expr1(expr2, expr3, *expr4, **expr5)
expr3, expr4 = expr1, expr2
6.14. Lambdas 103

### 第112页

6.17 Operator precedence
ThefollowingtablesummarizestheoperatorprecedenceinPython,fromhighestprecedence(mostbinding)tolowest
precedence (least binding). Operators in the same box have the same precedence. Unless the syntax is explicitly
given,operatorsarebinary. Operatorsinthesameboxgrouplefttoright(exceptforexponentiationandconditional
expressions,whichgroupfromrighttoleft).
Notethatcomparisons, membershiptests, andidentitytests, allhavethesameprecedenceandhavealeft-to-right
chainingfeatureasdescribedintheComparisonssection.
Operator Description
(expressions...), Binding or parenthesized expression, list display,
[expressions...], {key: value...}, dictionarydisplay,setdisplay
{expressions...}
x[index], x[index:index], x(arguments...), x. Subscription,slicing,call,attributereference
attribute
await x Awaitexpression
** Exponentiation5
+x,-x,~x Positive,negative,bitwiseNOT
*,@,/,//,% Multiplication, matrix multiplication, division,
floordivision,remainder6
+,- Additionandsubtraction
<<,>> Shifts
& BitwiseAND
^ BitwiseXOR
| BitwiseOR
in,not in,is,is not,<,<=,>,>=,!=,== Comparisons, including membership tests and
identitytests
not x BooleanNOT
and BooleanAND
or BooleanOR
if –else Conditionalexpression
lambda Lambdaexpression
:= Assignmentexpression
5Thepoweroperator**bindslesstightlythananarithmeticorbitwiseunaryoperatoronitsright,thatis,2**-1is0.5.
6The%operatorisalsousedforstringformatting;thesameprecedenceapplies.
104 Chapter6. Expressions

| Operator | Description |
| --- | --- |
| (expressions...),
[expressions...], {key: value...},
{expressions...} | Binding or parenthesized expression, list display,
dictionarydisplay,setdisplay |
| x[index], x[index:index], x(arguments...), x.
attribute | Subscription,slicing,call,attributereference |
| await x | Awaitexpression |
| ** | Exponentiation5 |
| +x,-x,~x | Positive,negative,bitwiseNOT |
| *,@,/,//,% | Multiplication, matrix multiplication, division,
floordivision,remainder6 |
| +,- | Additionandsubtraction |
| <<,>> | Shifts |
| & | BitwiseAND |
| ^ | BitwiseXOR |
| | | BitwiseOR |
| in,not in,is,is not,<,<=,>,>=,!=,== | Comparisons, including membership tests and
identitytests |
| not x | BooleanNOT |
| and | BooleanAND |
| or | BooleanOR |
| if –else | Conditionalexpression |
| lambda | Lambdaexpression |
| := | Assignmentexpression |

### 第113页

CHAPTER
SEVEN
SIMPLE STATEMENTS
Asimplestatementiscomprisedwithinasinglelogicalline. Severalsimplestatementsmayoccuronasingleline
separatedbysemicolons. Thesyntaxforsimplestatementsis:
simple_stmt: expression_stmt
| assert_stmt
| assignment_stmt
| augmented_assignment_stmt
| annotated_assignment_stmt
| pass_stmt
| del_stmt
| return_stmt
| yield_stmt
| raise_stmt
| break_stmt
| continue_stmt
| import_stmt
| future_stmt
| global_stmt
| nonlocal_stmt
| type_stmt
7.1 Expression statements
Expressionstatementsareused(mostlyinteractively)tocomputeandwriteavalue,or(usually)tocallaprocedure
(afunctionthatreturnsnomeaningfulresult;inPython,proceduresreturnthevalueNone). Otherusesofexpression
statementsareallowedandoccasionallyuseful. Thesyntaxforanexpressionstatementis:
expression_stmt: starred_expression
Anexpressionstatementevaluatestheexpressionlist(whichmaybeasingleexpression).
Ininteractivemode,ifthevalueisnotNone,itisconvertedtoastringusingthebuilt-inrepr()functionandthe
resultingstringiswrittentostandardoutputonalinebyitself(exceptiftheresultisNone,sothatprocedurecalls
donotcauseanyoutput.)
7.2 Assignment statements
Assignmentstatementsareusedto(re)bindnamestovaluesandtomodifyattributesoritemsofmutableobjects:
assignment_stmt: (target_list "=")+ (starred_expression | yield_expression)
target_list: target ("," target)* [","]
target: identifier
| "(" [target_list] ")"
| "[" [target_list] "]"
| attributeref
105

### 第114页

| subscription
| slicing
| "*" target
(SeesectionPrimariesforthesyntaxdefinitionsforattributeref,subscription,andslicing.)
Anassignmentstatementevaluatestheexpressionlist(rememberthatthiscanbeasingleexpressionoracomma-
separatedlist,thelatteryieldingatuple)andassignsthesingleresultingobjecttoeachofthetargetlists,fromleftto
right.
Assignmentisdefinedrecursivelydependingontheformofthetarget(list). Whenatargetispartofamutableobject
(anattributereference,subscriptionorslicing),themutableobjectmustultimatelyperformtheassignmentanddecide
aboutitsvalidity,andmayraiseanexceptioniftheassignmentisunacceptable. Therulesobservedbyvarioustypes
andtheexceptionsraisedaregivenwiththedefinitionoftheobjecttypes(seesectionThestandardtypehierarchy).
Assignmentofanobjecttoatargetlist,optionallyenclosedinparenthesesorsquarebrackets,isrecursivelydefined
asfollows.
• Ifthetargetlistisasingletargetwithnotrailingcomma,optionallyinparentheses,theobjectisassignedto
thattarget.
• Else:
– Ifthetargetlistcontainsonetargetprefixedwithanasterisk,calleda“starred”target: Theobjectmust
beaniterablewithatleastasmanyitemsastherearetargetsinthetargetlist,minusone. Thefirstitems
oftheiterableareassigned,fromlefttoright,tothetargetsbeforethestarredtarget. Thefinalitemsof
theiterableareassignedtothetargetsafterthestarredtarget. Alistoftheremainingitemsintheiterable
isthenassignedtothestarredtarget(thelistcanbeempty).
– Else: Theobjectmustbeaniterablewiththesamenumberofitemsastherearetargetsinthetargetlist,
andtheitemsareassigned,fromlefttoright,tothecorrespondingtargets.
Assignmentofanobjecttoasingletargetisrecursivelydefinedasfollows.
• Ifthetargetisanidentifier(name):
– Ifthenamedoesnotoccurinaglobalornonlocalstatementinthecurrentcodeblock: thenameis
boundtotheobjectinthecurrentlocalnamespace.
– Otherwise: thenameisboundtotheobjectintheglobalnamespaceortheouternamespacedetermined
bynonlocal,respectively.
The name is rebound if it was already bound. This may cause the reference count for the object previously
boundtothenametoreachzero,causingtheobjecttobedeallocatedanditsdestructor(ifithasone)tobe
called.
• If the target is an attribute reference: The primary expression in the reference is evaluated. It should yield
an object with assignable attributes; if this is not the case, TypeError is raised. That object is then asked
toassigntheassignedobjecttothegivenattribute;ifitcannotperformtheassignment,itraisesanexception
(usuallybutnotnecessarilyAttributeError).
Note:Iftheobjectisaclassinstanceandtheattributereferenceoccursonbothsidesoftheassignmentoperator,
theright-handsideexpression,a.xcanaccesseitheraninstanceattributeor(ifnoinstanceattributeexists)a
classattribute. Theleft-handsidetargeta.xisalwayssetasaninstanceattribute,creatingitifnecessary. Thus,
the two occurrences of a.x do not necessarily refer to the same attribute: if the right-hand side expression
referstoaclassattribute,theleft-handsidecreatesanewinstanceattributeasthetargetoftheassignment:
class Cls:
x = 3 # class variable
inst = Cls()
inst.x = inst.x + 1 # writes inst.x as 4 leaving Cls.x as 3
This description does not necessarily apply to descriptor attributes, such as properties created with
property().
106 Chapter7. Simplestatements

### 第115页

• If the target is a subscription: The primary expression in the reference is evaluated. It should yield either
a mutable sequence object (such as a list) or a mapping object (such as a dictionary). Next, the subscript
expressionisevaluated.
Iftheprimaryisamutablesequenceobject(suchasalist),thesubscriptmustyieldaninteger. Ifitisnegative,
thesequence’slengthisaddedtoit. Theresultingvaluemustbeanonnegativeintegerlessthanthesequence’s
length,andthesequenceisaskedtoassigntheassignedobjecttoitsitemwiththatindex. Iftheindexisout
ofrange,IndexErrorisraised(assignmenttoasubscriptedsequencecannotaddnewitemstoalist).
Iftheprimaryisamappingobject(suchasadictionary),thesubscriptmusthaveatypecompatiblewiththe
mapping’skeytype,andthemappingisthenaskedtocreateakey/valuepairwhichmapsthesubscripttothe
assigned object. This can either replace an existing key/value pair with the same key value, or insert a new
key/valuepair(ifnokeywiththesamevalueexisted).
Foruser-definedobjects,the__setitem__()methodiscalledwithappropriatearguments.
• Ifthetargetisaslicing:Theprimaryexpressioninthereferenceisevaluated. Itshouldyieldamutablesequence
object(suchasalist). Theassignedobjectshouldbeasequenceobjectofthesametype. Next,thelowerand
upperboundexpressionsareevaluated, insofartheyarepresent; defaultsarezeroandthesequence’slength.
Theboundsshouldevaluatetointegers. Ifeitherboundisnegative,thesequence’slengthisaddedtoit. The
resulting bounds are clipped to lie between zero and the sequence’s length, inclusive. Finally, the sequence
object is asked to replace the slice with the items of the assigned sequence. The length of the slice may be
differentfromthelengthoftheassignedsequence,thuschangingthelengthofthetargetsequence,ifthetarget
sequenceallowsit.
CPythonimplementationdetail: Inthecurrentimplementation,thesyntaxfortargetsistakentobethesameas
forexpressions,andinvalidsyntaxisrejectedduringthecodegenerationphase,causinglessdetailederrormessages.
Althoughthedefinitionofassignmentimpliesthatoverlapsbetweentheleft-handsideandtheright-handsideare‘si-
multaneous’(forexamplea, b = b, aswapstwovariables),overlapswithinthecollectionofassigned-tovariables
occurleft-to-right,sometimesresultinginconfusion. Forinstance,thefollowingprogramprints[0, 2]:
x = [0, 1]
i = 0
i, x[i] = 1, 2 # i is updated, then x[i] is updated
print(x)
(cid:181) Seealso
PEP3132-ExtendedIterableUnpacking
Thespecificationforthe*targetfeature.
7.2.1 Augmented assignment statements
Augmentedassignmentisthecombination,inasinglestatement,ofabinaryoperationandanassignmentstatement:
augmented_assignment_stmt: augtarget augop (expression_list | yield_expression)
augtarget: identifier | attributeref | subscription | slicing
augop: "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
| ">>=" | "<<=" | "&=" | "^=" | "|="
(SeesectionPrimariesforthesyntaxdefinitionsofthelastthreesymbols.)
Anaugmentedassignmentevaluatesthetarget(which,unlikenormalassignmentstatements,cannotbeanunpacking)
and the expression list, performs the binary operation specific to the type of assignment on the two operands, and
assignstheresulttotheoriginaltarget. Thetargetisonlyevaluatedonce.
An augmented assignment statement like x += 1 can be rewritten as x = x + 1 to achieve a similar, but not
exactlyequaleffect. Intheaugmentedversion,xisonlyevaluatedonce. Also,whenpossible,theactualoperationis
performedin-place,meaningthatratherthancreatinganewobjectandassigningthattothetarget,theoldobjectis
modifiedinstead.
7.2. Assignmentstatements 107

| (cid:181) Seealso |
| --- |
| PEP3132-ExtendedIterableUnpacking
Thespecificationforthe*targetfeature. |

### 第116页

Unlikenormalassignments,augmentedassignmentsevaluatetheleft-handsidebeforeevaluatingtheright-handside.
Forexample, a[i] += f(x)firstlooks-upa[i], thenitevaluatesf(x)andperformstheaddition, andlastly, it
writestheresultbacktoa[i].
With the exception of assigning to tuples and multiple targets in a single statement, the assignment done by aug-
mentedassignmentstatementsishandledthesamewayasnormalassignments. Similarly,withtheexceptionofthe
possiblein-placebehavior,thebinaryoperationperformedbyaugmentedassignmentisthesameasthenormalbinary
operations.
Fortargetswhichareattributereferences,thesamecaveataboutclassandinstanceattributesappliesasforregular
assignments.
7.2.2 Annotated assignment statements
Annotationassignmentisthecombination,inasinglestatement,ofavariableorattributeannotationandanoptional
assignmentstatement:
annotated_assignment_stmt: augtarget ":" expression
["=" (starred_expression | yield_expression)]
ThedifferencefromnormalAssignmentstatementsisthatonlyasingletargetisallowed.
Theassignmenttargetisconsidered“simple”ifitconsistsofasinglenamethatisnotenclosedinparentheses. For
simpleassignmenttargets,ifinclassormodulescope,theannotationsaregatheredinalazilyevaluatedannotation
scope. Theannotationscanbeevaluatedusingthe__annotations__attributeofaclassormodule,orusingthe
facilitiesintheannotationlibmodule.
Iftheassignmenttargetisnotsimple(anattribute,subscriptnode,orparenthesizedname),theannotationisnever
evaluated.
Ifanameisannotatedinafunctionscope,thenthisnameislocalforthatscope. Annotationsareneverevaluated
andstoredinfunctionscopes.
Iftherighthandsideispresent,anannotatedassignmentperformstheactualassignmentasiftherewasnoannotation
present. Iftherighthandsideisnotpresentforanexpressiontarget,thentheinterpreterevaluatesthetargetexcept
forthelast__setitem__()or__setattr__()call.
(cid:181) Seealso
PEP526-SyntaxforVariableAnnotations
Theproposalthataddedsyntaxforannotatingthetypesofvariables(includingclassvariablesandinstance
variables),insteadofexpressingthemthroughcomments.
PEP484-Typehints
Theproposalthataddedthetypingmoduletoprovideastandardsyntaxfortypeannotationsthatcanbe
usedinstaticanalysistoolsandIDEs.
Changed in version 3.8: Now annotated assignments allow the same expressions in the right hand side as regular
assignments. Previously,someexpressions(likeun-parenthesizedtupleexpressions)causedasyntaxerror.
Changed in version 3.14: Annotations are now lazily evaluated in a separate annotation scope. If the assignment
targetisnotsimple,annotationsareneverevaluated.
7.3 The assert statement
Assertstatementsareaconvenientwaytoinsertdebuggingassertionsintoaprogram:
assert_stmt: "assert" expression ["," expression]
Thesimpleform,assert expression,isequivalentto
108 Chapter7. Simplestatements

| (cid:181) Seealso |
| --- |
| PEP526-SyntaxforVariableAnnotations
Theproposalthataddedsyntaxforannotatingthetypesofvariables(includingclassvariablesandinstance
variables),insteadofexpressingthemthroughcomments.
PEP484-Typehints
Theproposalthataddedthetypingmoduletoprovideastandardsyntaxfortypeannotationsthatcanbe
usedinstaticanalysistoolsandIDEs. |

### 第117页

if __debug__:
if not expression: raise AssertionError
Theextendedform,assert expression1, expression2,isequivalentto
if __debug__:
if not expression1: raise AssertionError(expression2)
Theseequivalencesassumethat__debug__andAssertionErrorrefertothebuilt-invariableswiththosenames.
Inthecurrentimplementation,thebuilt-invariable__debug__isTrueundernormalcircumstances,Falsewhen
optimization is requested (command line option -O). The current code generator emits no code for an assert
statementwhenoptimizationisrequestedatcompiletime. Notethatitisunnecessarytoincludethesourcecodefor
theexpressionthatfailedintheerrormessage;itwillbedisplayedaspartofthestacktrace.
Assignmentsto__debug__areillegal. Thevalueforthebuilt-invariableisdeterminedwhentheinterpreterstarts.
7.4 The pass statement
pass_stmt: "pass"
passisanulloperation—whenitisexecuted,nothinghappens. Itisusefulasaplaceholderwhenastatementis
requiredsyntactically,butnocodeneedstobeexecuted,forexample:
def f(arg): pass # a function that does nothing (yet)
class C: pass # a class with no methods (yet)
7.5 The del statement
del_stmt: "del" target_list
Deletionisrecursivelydefinedverysimilartothewayassignmentisdefined. Ratherthanspellingitoutinfulldetails,
herearesomehints.
Deletionofatargetlistrecursivelydeleteseachtarget,fromlefttoright.
Deletionofanameremovesthebindingofthatnamefromthelocalorglobalnamespace,dependingonwhetherthe
nameoccursinaglobalstatementinthesamecodeblock. TryingtodeleteanunboundnameraisesaNameError
exception.
Deletion of attribute references, subscriptions and slicings is passed to the primary object involved; deletion of a
slicingisingeneralequivalenttoassignmentofanemptysliceoftherighttype(buteventhisisdeterminedbythe
slicedobject).
Changed in version 3.2: Previously it was illegal to delete a name from the local namespace if it occurs as a free
variableinanestedblock.
7.6 The return statement
return_stmt: "return" [expression_list]
returnmayonlyoccursyntacticallynestedinafunctiondefinition,notwithinanestedclassdefinition.
Ifanexpressionlistispresent,itisevaluated,elseNoneissubstituted.
returnleavesthecurrentfunctioncallwiththeexpressionlist(orNone)asreturnvalue.
Whenreturnpassescontroloutofatrystatementwithafinallyclause,thatfinallyclauseisexecutedbefore
reallyleavingthefunction.
7.4. The statement 109

### 第118页

Inageneratorfunction,thereturnstatementindicatesthatthegeneratorisdoneandwillcauseStopIteration
to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the
StopIteration.valueattribute.
In an asynchronous generator function, an empty return statement indicates that the asynchronous generator is
doneandwillcauseStopAsyncIterationtoberaised. Anon-emptyreturnstatementisasyntaxerrorinan
asynchronousgeneratorfunction.
7.7 The yield statement
yield_stmt: yield_expression
Ayield statementissemanticallyequivalenttoayieldexpression. Theyieldstatementcanbeusedtoomitthe
parentheses that would otherwise be required in the equivalent yield expression statement. For example, the yield
statements
yield <expr>
yield from <expr>
areequivalenttotheyieldexpressionstatements
(yield <expr>)
(yield from <expr>)
Yieldexpressionsandstatementsareonlyusedwhendefiningageneratorfunction,andareonlyusedinthebodyof
thegeneratorfunction. Usingyieldinafunctiondefinitionissufficienttocausethatdefinitiontocreateagenerator
functioninsteadofanormalfunction.
Forfulldetailsofyieldsemantics,refertotheYieldexpressionssection.
7.8 The raise statement
raise_stmt: "raise" [expression ["from" expression]]
Ifnoexpressionsarepresent,raisere-raisestheexceptionthatiscurrentlybeinghandled,whichisalsoknownas
theactiveexception. Ifthereisn’tcurrentlyanactiveexception,aRuntimeErrorexceptionisraisedindicatingthat
thisisanerror.
Otherwise,raiseevaluatesthefirstexpressionastheexceptionobject. Itmustbeeitherasubclassoraninstance
ofBaseException. Ifitisaclass,theexceptioninstancewillbeobtainedwhenneededbyinstantiatingtheclass
withnoarguments.
Thetypeoftheexceptionistheexceptioninstance’sclass,thevalueistheinstanceitself.
A traceback object is normally created automatically when an exception is raised and attached to it as the
__traceback__ attribute. You can create an exception and set your own traceback in one step using the
with_traceback() exception method (which returns the same exception instance, with its traceback set to its
argument),likeso:
raise Exception("foo occurred").with_traceback(tracebackobj)
The from clause is used for exception chaining: if given, the second expression must be another exception class
or instance. If the second expression is an exception instance, it will be attached to the raised exception as the
__cause__attribute(whichiswritable). Iftheexpressionisanexceptionclass, theclasswillbeinstantiatedand
theresultingexceptioninstancewillbeattachedtotheraisedexceptionasthe__cause__attribute. Iftheraised
exceptionisnothandled,bothexceptionswillbeprinted:
>>> try:
... print(1 / 0)
(continuesonnextpage)
110 Chapter7. Simplestatements

### 第119页

(continuedfrompreviouspage)
... except Exception as exc:
... raise RuntimeError("Something bad happened") from exc
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
print(1 / 0)
~~^~~
ZeroDivisionError: division by zero
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
raise RuntimeError("Something bad happened") from exc
RuntimeError: Something bad happened
Asimilarmechanismworksimplicitlyifanewexceptionisraisedwhenanexceptionisalreadybeinghandled. An
exceptionmaybehandledwhenanexceptorfinallyclause,orawithstatement,isused. Thepreviousexception
isthenattachedasthenewexception’s__context__attribute:
>>> try:
... print(1 / 0)
... except:
... raise RuntimeError("Something bad happened")
...
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
print(1 / 0)
~~^~~
ZeroDivisionError: division by zero
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
raise RuntimeError("Something bad happened")
RuntimeError: Something bad happened
ExceptionchainingcanbeexplicitlysuppressedbyspecifyingNoneinthefromclause:
>>> try:
... print(1 / 0)
... except:
... raise RuntimeError("Something bad happened") from None
...
Traceback (most recent call last):
File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened
AdditionalinformationonexceptionscanbefoundinsectionExceptions,andinformationabouthandlingexceptions
isinsectionThetrystatement.
Changedinversion3.3: NoneisnowpermittedasYinraise X from Y.
Addedthe__suppress_context__attributetosuppressautomaticdisplayoftheexceptioncontext.
Changed in version 3.11: If the traceback of the active exception is modified in an except clause, a subsequent
raisestatementre-raisestheexceptionwiththemodifiedtraceback. Previously,theexceptionwasre-raisedwith
thetracebackithadwhenitwascaught.
7.8. The statement 111

### 第120页

7.9 The break statement
break_stmt: "break"
breakmayonlyoccursyntacticallynestedinafororwhileloop,butnotnestedinafunctionorclassdefinition
withinthatloop.
Itterminatesthenearestenclosingloop,skippingtheoptionalelseclauseiftheloophasone.
Ifaforloopisterminatedbybreak,theloopcontroltargetkeepsitscurrentvalue.
Whenbreakpassescontroloutofatrystatementwithafinallyclause,thatfinallyclauseisexecutedbefore
reallyleavingtheloop.
7.10 The continue statement
continue_stmt: "continue"
continuemayonlyoccursyntacticallynestedinafororwhileloop,butnotnestedinafunctionorclassdefinition
withinthatloop. Itcontinueswiththenextcycleofthenearestenclosingloop.
Whencontinuepassescontroloutofatry statementwithafinally clause, thatfinallyclauseisexecuted
beforereallystartingthenextloopcycle.
7.11 The import statement
import_stmt: "import" module ["as" identifier] ("," module ["as" identifier])*
| "from" relative_module "import" identifier ["as" identifier]
("," identifier ["as" identifier])*
| "from" relative_module "import" "(" identifier ["as" identifier]
("," identifier ["as" identifier])* [","] ")"
| "from" relative_module "import" "*"
module: (identifier ".")* identifier
relative_module: "."* module | "."+
Thebasicimportstatement(nofromclause)isexecutedintwosteps:
1. findamodule,loadingandinitializingitifnecessary
2. defineanameornamesinthelocalnamespaceforthescopewheretheimportstatementoccurs.
When the statement contains multiple clauses (separated by commas) the two steps are carried out separately for
eachclause,justasthoughtheclauseshadbeenseparatedoutintoindividualimportstatements.
Thedetailsofthefirststep,findingandloadingmodules,aredescribedingreaterdetailinthesectionontheimport
system,whichalsodescribesthevarioustypesofpackagesandmodulesthatcanbeimported,aswellasallthehooks
thatcanbeusedtocustomizetheimportsystem. Notethatfailuresinthisstepmayindicateeitherthatthemodule
couldnotbelocated,orthatanerroroccurredwhileinitializingthemodule,whichincludesexecutionofthemodule’s
code.
If the requested module is retrieved successfully, it will be made available in the local namespace in one of three
ways:
• Ifthemodulenameisfollowedbyas,thenthenamefollowingasisbounddirectlytotheimportedmodule.
• Ifnoothernameisspecified,andthemodulebeingimportedisatoplevelmodule,themodule’snameisbound
inthelocalnamespaceasareferencetotheimportedmodule
• Ifthemodulebeingimportedisnot atoplevelmodule,thenthenameofthetoplevelpackagethatcontains
themoduleisboundinthelocalnamespaceasareferencetothetoplevelpackage. Theimportedmodulemust
beaccessedusingitsfullqualifiednameratherthandirectly
Thefromformusesaslightlymorecomplexprocess:
112 Chapter7. Simplestatements

### 第121页

1. findthemodulespecifiedinthefromclause,loadingandinitializingitifnecessary;
2. foreachoftheidentifiersspecifiedintheimportclauses:
1. checkiftheimportedmodulehasanattributebythatname
2. ifnot,attempttoimportasubmodulewiththatnameandthenchecktheimportedmoduleagainforthat
attribute
3. iftheattributeisnotfound,ImportErrorisraised.
4. otherwise,areferencetothatvalueisstoredinthelocalnamespace,usingthenameintheasclauseifit
ispresent,otherwiseusingtheattributename
Examples:
import foo # foo imported and bound locally
import foo.bar.baz # foo, foo.bar, and foo.bar.baz imported, foo bound␣
,→locally
import foo.bar.baz as fbb # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz␣
,→bound as fbb
from foo.bar import baz # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz␣
,→bound as baz
from foo import attr # foo imported and foo.attr bound as attr
If the list of identifiers is replaced by a star ('*'), all public names defined in the module are bound in the local
namespaceforthescopewheretheimportstatementoccurs.
The public names defined by a module are determined by checking the module’s namespace for a variable named
__all__; if defined, it must be a sequence of strings which are names defined or imported by that module. The
namesgivenin__all__areallconsideredpublicandarerequiredtoexist. If__all__isnotdefined,thesetof
publicnamesincludesallnamesfoundinthemodule’snamespacewhichdonotbeginwithanunderscorecharacter
('_'). __all__shouldcontaintheentirepublicAPI.Itisintendedtoavoidaccidentallyexportingitemsthatare
notpartoftheAPI(suchaslibrarymoduleswhichwereimportedandusedwithinthemodule).
Thewildcardformofimport—from module import *—isonlyallowedatthemodulelevel. Attemptingto
useitinclassorfunctiondefinitionswillraiseaSyntaxError.
Whenspecifyingwhatmoduletoimportyoudonothavetospecifytheabsolutenameofthemodule. Whenamodule
orpackageiscontainedwithinanotherpackageitispossibletomakearelativeimportwithinthesametoppackage
withouthavingtomentionthepackagename. Byusingleadingdotsinthespecifiedmoduleorpackageafterfrom
youcanspecifyhowhightotraverseupthecurrentpackagehierarchywithoutspecifyingexactnames. Oneleading
dotmeansthecurrentpackagewherethemodulemakingtheimportexists. Twodotsmeansuponepackagelevel.
Threedotsisuptwolevels,etc. Soifyouexecutefrom . import modfromamoduleinthepkgpackagethenyou
willendupimportingpkg.mod. Ifyouexecutefrom ..subpkg2 import modfromwithinpkg.subpkg1you
willimportpkg.subpkg2.mod. ThespecificationforrelativeimportsiscontainedinthePackageRelativeImports
section.
importlib.import_module()isprovidedtosupportapplicationsthatdeterminedynamicallythemodulestobe
loaded.
Raises an auditing event import with arguments module, filename, sys.path, sys.meta_path, sys.
path_hooks.
7.11.1 Future statements
Afuturestatementisadirectivetothecompilerthataparticularmoduleshouldbecompiledusingsyntaxorsemantics
thatwillbeavailableinaspecifiedfuturereleaseofPythonwherethefeaturebecomesstandard.
ThefuturestatementisintendedtoeasemigrationtofutureversionsofPythonthatintroduceincompatiblechangesto
thelanguage. Itallowsuseofthenewfeaturesonaper-modulebasisbeforethereleaseinwhichthefeaturebecomes
standard.
future_stmt: "from" "__future__" "import" feature ["as" identifier]
7.11. The statement 113

### 第122页

("," feature ["as" identifier])*
| "from" "__future__" "import" "(" feature ["as" identifier]
("," feature ["as" identifier])* [","] ")"
feature: identifier
Afuturestatementmustappearnearthetopofthemodule. Theonlylinesthatcanappearbeforeafuturestatement
are:
• themoduledocstring(ifany),
• comments,
• blanklines,and
• otherfuturestatements.
Theonlyfeaturethatrequiresusingthefuturestatementisannotations(seePEP563).
All historical features enabled by the future statement are still recognized by Python 3. The list includes
absolute_import, division, generators, generator_stop, unicode_literals, print_function,
nested_scopesandwith_statement. Theyareallredundantbecausetheyarealwaysenabled, andonlykept
forbackwardscompatibility.
Afuturestatementisrecognizedandtreatedspeciallyatcompiletime: Changestothesemanticsofcoreconstructs
areoftenimplementedbygeneratingdifferentcode. Itmayevenbethecasethatanewfeatureintroducesnewincom-
patiblesyntax(suchasanewreservedword),inwhichcasethecompilermayneedtoparsethemoduledifferently.
Suchdecisionscannotbepushedoffuntilruntime.
Foranygivenrelease,thecompilerknowswhichfeaturenameshavebeendefined,andraisesacompile-timeerror
ifafuturestatementcontainsafeaturenotknowntoit.
Thedirectruntimesemanticsarethesameasforanyimportstatement: thereisastandardmodule__future__,
describedlater,anditwillbeimportedintheusualwayatthetimethefuturestatementisexecuted.
Theinterestingruntimesemanticsdependonthespecificfeatureenabledbythefuturestatement.
Notethatthereisnothingspecialaboutthestatement:
import __future__ [as name]
Thatisnotafuturestatement;it’sanordinaryimportstatementwithnospecialsemanticsorsyntaxrestrictions.
Code compiled by calls to the built-in functions exec() and compile() that occur in a module M containing a
futurestatementwill,bydefault,usethenewsyntaxorsemanticsassociatedwiththefuturestatement. Thiscanbe
controlledbyoptionalargumentstocompile()—seethedocumentationofthatfunctionfordetails.
Afuturestatementtypedataninteractiveinterpreterpromptwilltakeeffectfortherestoftheinterpretersession.
If an interpreter is started with the -i option, is passed a script name to execute, and the script includes a future
statement,itwillbeineffectintheinteractivesessionstartedafterthescriptisexecuted.
(cid:181) Seealso
PEP236-Backtothe__future__
Theoriginalproposalforthe__future__mechanism.
7.12 The global statement
global_stmt: "global" identifier ("," identifier)*
Theglobalstatementcausesthelistedidentifierstobeinterpretedasglobals. Itwouldbeimpossibletoassigntoa
globalvariablewithoutglobal,althoughfreevariablesmayrefertoglobalswithoutbeingdeclaredglobal.
Theglobalstatementappliestotheentirescopeofafunctionorclassbody. ASyntaxErrorisraisedifavariable
isusedorassignedtopriortoitsglobaldeclarationinthescope.
114 Chapter7. Simplestatements

| (cid:181) Seealso |
| --- |
| PEP236-Backtothe__future__
Theoriginalproposalforthe__future__mechanism. |

### 第123页

Programmer’s note: global is a directive to the parser. It applies only to code parsed at the same time as the
global statement. In particular, a global statementcontainedina stringorcodeobjectsuppliedto thebuilt-in
exec() function does not affect the code block containing the function call, and code contained in such a string
isunaffectedbyglobalstatementsinthecodecontainingthefunctioncall. Thesameappliestotheeval()and
compile()functions.
7.13 The nonlocal statement
nonlocal_stmt: "nonlocal" identifier ("," identifier)*
Whenthedefinitionofafunctionorclassisnested(enclosed)withinthedefinitionsofotherfunctions,itsnonlocal
scopesarethelocalscopesoftheenclosingfunctions. Thenonlocalstatementcausesthelistedidentifierstorefer
tonamespreviouslyboundinnonlocalscopes. Itallowsencapsulatedcodetorebindsuchnonlocalidentifiers. Ifa
nameisboundinmorethanonenonlocalscope,thenearestbindingisused. Ifanameisnotboundinanynonlocal
scope,orifthereisnononlocalscope,aSyntaxErrorisraised.
The nonlocal statement applies to the entire scope of a function or class body. A SyntaxError is raised if a
variableisusedorassignedtopriortoitsnonlocaldeclarationinthescope.
(cid:181) Seealso
PEP3104-AccesstoNamesinOuterScopes
Thespecificationforthenonlocalstatement.
Programmer’snote: nonlocalisadirectivetotheparserandappliesonlytocodeparsedalongwithit. Seethe
notefortheglobalstatement.
7.14 The type statement
type_stmt: 'type' identifier [type_params] "=" expression
Thetypestatementdeclaresatypealias,whichisaninstanceoftyping.TypeAliasType.
Forexample,thefollowingstatementcreatesatypealias:
type Point = tuple[float, float]
Thiscodeisroughlyequivalentto:
annotation-def VALUE_OF_Point():
return tuple[float, float]
Point = typing.TypeAliasType("Point", VALUE_OF_Point())
annotation-defindicatesanannotationscope,whichbehavesmostlylikeafunction,butwithseveralsmalldif-
ferences.
Thevalueofthetypealiasisevaluatedintheannotationscope. Itisnotevaluatedwhenthetypealiasiscreated,but
onlywhenthevalueisaccessedthroughthetypealias’s__value__attribute(seeLazyevaluation). Thisallowsthe
typealiastorefertonamesthatarenotyetdefined.
Typealiasesmaybemadegenericbyaddingatypeparameterlistafterthename. SeeGenerictypealiasesformore.
typeisasoftkeyword.
Addedinversion3.12.
(cid:181) Seealso
7.13. The statement 115

| (cid:181) Seealso |
| --- |
| PEP3104-AccesstoNamesinOuterScopes
Thespecificationforthenonlocalstatement. |


| (cid:181) Seealso |
| --- |
|  |

### 第124页

PEP695-TypeParameterSyntax
Introducedthetypestatementandsyntaxforgenericclassesandfunctions.
116 Chapter7. Simplestatements

### 第125页

CHAPTER
EIGHT
COMPOUND STATEMENTS
Compoundstatementscontain(groupsof)otherstatements;theyaffectorcontroltheexecutionofthoseotherstate-
mentsinsomeway. Ingeneral, compoundstatementsspanmultiplelines, althoughinsimpleincarnationsawhole
compoundstatementmaybecontainedinoneline.
Theif,whileandforstatementsimplementtraditionalcontrolflowconstructs. tryspecifiesexceptionhandlers
and/orcleanupcodeforagroupofstatements, whilethewithstatementallowstheexecutionofinitializationand
finalizationcodearoundablockofcode. Functionandclassdefinitionsarealsosyntacticallycompoundstatements.
Acompoundstatementconsistsofoneormore‘clauses.’ Aclauseconsistsofaheaderanda‘suite.’ Theclauseheaders
ofaparticularcompoundstatementareallatthesameindentationlevel. Eachclauseheaderbeginswithauniquely
identifyingkeywordandendswithacolon. Asuiteisagroupofstatementscontrolledbyaclause. Asuitecanbeone
ormoresemicolon-separatedsimplestatementsonthesamelineastheheader,followingtheheader’scolon,oritcan
beoneormoreindentedstatementsonsubsequentlines. Onlythelatterformofasuitecancontainnestedcompound
statements;thefollowingisillegal,mostlybecauseitwouldn’tbecleartowhichif clauseafollowingelseclause
wouldbelong:
if test1: if test2: print(x)
Alsonotethatthesemicolonbindstighterthanthecoloninthiscontext,sothatinthefollowingexample,eitherall
ornoneoftheprint()callsareexecuted:
if x < y < z: print(x); print(y); print(z)
Summarizing:
compound_stmt: if_stmt
| while_stmt
| for_stmt
| try_stmt
| with_stmt
| match_stmt
| funcdef
| classdef
| async_with_stmt
| async_for_stmt
| async_funcdef
suite: stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
statement: stmt_list NEWLINE | compound_stmt
stmt_list: simple_stmt (";" simple_stmt)* [";"]
NotethatstatementsalwaysendinaNEWLINEpossiblyfollowedbyaDEDENT.Alsonotethatoptionalcontinuation
clausesalwaysbeginwithakeywordthatcannotstartastatement,thustherearenoambiguities(the‘danglingelse’
problemissolvedinPythonbyrequiringnestedif statementstobeindented).
Theformattingofthegrammarrulesinthefollowingsectionsplaceseachclauseonaseparatelineforclarity.
117

### 第126页

8.1 The if statement
Theif statementisusedforconditionalexecution:
if_stmt: "if" assignment_expression ":" suite
("elif" assignment_expression ":" suite)*
["else" ":" suite]
Itselectsexactlyoneofthesuitesbyevaluatingtheexpressionsonebyoneuntiloneisfoundtobetrue(seesection
Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if
statementisexecutedorevaluated). Ifallexpressionsarefalse,thesuiteoftheelseclause,ifpresent,isexecuted.
8.2 The while statement
Thewhilestatementisusedforrepeatedexecutionaslongasanexpressionistrue:
while_stmt: "while" assignment_expression ":" suite
["else" ":" suite]
Thisrepeatedlyteststheexpressionand,ifitistrue,executesthefirstsuite;iftheexpressionisfalse(whichmaybe
thefirsttimeitistested)thesuiteoftheelseclause,ifpresent,isexecutedandtheloopterminates.
A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A
continuestatementexecutedinthefirstsuiteskipstherestofthesuiteandgoesbacktotestingtheexpression.
8.3 The for statement
Theforstatementisusedtoiterateovertheelementsofasequence(suchasastring,tupleorlist)orotheriterable
object:
for_stmt: "for" target_list "in" starred_expression_list ":" suite
["else" ":" suite]
The starred_expression_list expression is evaluated once; it should yield an iterable object. An iterator is
createdforthatiterable. Thefirstitemprovidedbytheiteratoristhenassignedtothetargetlistusingthestandard
rules for assignments (see Assignment statements), and the suite is executed. This repeats for each item provided
by the iterator. When the iterator is exhausted, the suite in the else clause, if present, is executed, and the loop
terminates.
A break statement executed in the first suite terminates the loop without executing the else clause’s suite. A
continuestatementexecutedinthefirstsuiteskipstherestofthesuiteandcontinueswiththenextitem,orwith
theelseclauseifthereisnonextitem.
Thefor-loopmakesassignmentstothevariablesinthetargetlist. Thisoverwritesallpreviousassignmentstothose
variablesincludingthosemadeinthesuiteofthefor-loop:
for i in range(10):
print(i)
i = 5 # this will not affect the for-loop
# because i will be overwritten with the next
# index in the range
Names in the target list are not deleted when the loop is finished, but if the sequence is empty, they will not have
beenassignedtoatallbytheloop. Hint: thebuilt-intyperange()representsimmutablearithmeticsequencesof
integers. Forinstance,iteratingrange(3)successivelyyields0,1,andthen2.
Changedinversion3.11: Starredelementsarenowallowedintheexpressionlist.
118 Chapter8. Compoundstatements

### 第127页

8.4 The try statement
Thetrystatementspecifiesexceptionhandlersand/orcleanupcodeforagroupofstatements:
try_stmt: try1_stmt | try2_stmt | try3_stmt
try1_stmt: "try" ":" suite
("except" [expression ["as" identifier]] ":" suite)+
["else" ":" suite]
["finally" ":" suite]
try2_stmt: "try" ":" suite
("except" "*" expression ["as" identifier] ":" suite)+
["else" ":" suite]
["finally" ":" suite]
try3_stmt: "try" ":" suite
"finally" ":" suite
AdditionalinformationonexceptionscanbefoundinsectionExceptions,andinformationonusingtheraisestate-
menttogenerateexceptionsmaybefoundinsectionTheraisestatement.
Changedinversion3.14: Supportforoptionallydroppinggroupingparentheseswhenusingmultipleexceptiontypes.
SeePEP758.
8.4.1 except clause
The except clause(s) specify one or more exception handlers. When no exception occurs in the try clause, no
exceptionhandlerisexecuted. Whenanexceptionoccursinthetrysuite,asearchforanexceptionhandlerisstarted.
Thissearchinspectstheexceptclausesinturnuntiloneisfoundthatmatchestheexception. Anexpression-less
exceptclause,ifpresent,mustbelast;itmatchesanyexception.
Foranexceptclausewithanexpression,theexpressionmustevaluatetoanexceptiontypeoratupleofexception
types. Parentheses can be dropped if multiple exception types are provided and the as clause is not used. The
raisedexceptionmatchesanexceptclausewhoseexpressionevaluatestotheclassoranon-virtualbaseclassofthe
exceptionobject,ortoatuplethatcontainssuchaclass.
Ifnoexceptclausematchestheexception,thesearchforanexceptionhandlercontinuesinthesurroundingcode
andontheinvocationstack.1
Iftheevaluationofanexpressionintheheaderofanexceptclauseraisesanexception, theoriginalsearchfora
handleriscanceledandasearchstartsforthenewexceptioninthesurroundingcodeandonthecallstack(itistreated
asiftheentiretrystatementraisedtheexception).
Whenamatchingexceptclauseisfound,theexceptionisassignedtothetargetspecifiedaftertheaskeywordinthat
exceptclause,ifpresent,andtheexceptclause’ssuiteisexecuted. Allexceptclausesmusthaveanexecutable
block. Whentheendofthisblockisreached, executioncontinuesnormallyaftertheentiretry statement. (This
means that if two nested handlers exist for the same exception, and the exception occurs in the try clause of the
innerhandler,theouterhandlerwillnothandletheexception.)
Whenanexceptionhasbeenassignedusingas target,itisclearedattheendoftheexceptclause. Thisisasif
except E as N:
foo
wastranslatedto
except E as N:
try:
foo
finally:
del N
1Theexceptionispropagatedtotheinvocationstackunlessthereisafinallyclausewhichhappenstoraiseanotherexception. Thatnew
exceptioncausestheoldonetobelost.
8.4. The statement 119

### 第128页

This means the exception must be assigned to a different name to be able to refer to it after the except clause.
Exceptions are cleared because with the traceback attached to them, they form a reference cycle with the stack
frame,keepingalllocalsinthatframealiveuntilthenextgarbagecollectionoccurs.
Before an except clause’s suite is executed, the exception is stored in the sys module, where it can be accessed
fromwithinthebodyoftheexceptclausebycallingsys.exception(). Whenleavinganexceptionhandler,the
exceptionstoredinthesysmoduleisresettoitspreviousvalue:
>>> print(sys.exception())
None
>>> try:
... raise TypeError
... except:
... print(repr(sys.exception()))
... try:
... raise ValueError
... except:
... print(repr(sys.exception()))
... print(repr(sys.exception()))
...
TypeError()
ValueError()
TypeError()
>>> print(sys.exception())
None
8.4.2 except* clause
Theexcept*clause(s)areusedforhandlingExceptionGroups. Theexceptiontypeformatchingisinterpreted
asinthecaseofexcept,butinthecaseofexceptiongroupswecanhavepartialmatcheswhenthetypematches
someoftheexceptionsinthegroup. Thismeansthatmultipleexcept*clausescanexecute,eachhandlingpartof
theexceptiongroup. Eachclauseexecutesatmostonceandhandlesanexceptiongroupofallmatchingexceptions.
Eachexceptioninthegroupishandledbyatmostoneexcept*clause,thefirstthatmatchesit.
>>> try:
... raise ExceptionGroup("eg",
... [ValueError(1), TypeError(2), OSError(3), OSError(4)])
... except* TypeError as e:
... print(f'caught {type(e)} with nested {e.exceptions}')
... except* OSError as e:
... print(f'caught {type(e)} with nested {e.exceptions}')
...
caught <class 'ExceptionGroup'> with nested (TypeError(2),)
caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
+ Exception Group Traceback (most recent call last):
| File "<stdin>", line 2, in <module>
| ExceptionGroup: eg
+-+---------------- 1 ----------------
| ValueError: 1
+------------------------------------
Any remaining exceptions that were not handled by any except* clause are re-raised at the end, along with all
exceptionsthatwereraisedfromwithintheexcept*clauses. Ifthislistcontainsmorethanoneexceptiontoreraise,
theyarecombinedintoanexceptiongroup.
Iftheraisedexceptionisnotanexceptiongroupanditstypematchesoneoftheexcept*clauses,itiscaughtand
wrappedbyanexceptiongroupwithanemptymessagestring.
120 Chapter8. Compoundstatements

### 第129页

>>> try:
... raise BlockingIOError
... except* BlockingIOError as e:
... print(repr(e))
...
ExceptionGroup('', (BlockingIOError()))
Anexcept*clausemusthaveamatchingexpression;itcannotbeexcept*:. Furthermore,thisexpressioncannot
containexceptiongrouptypes,becausethatwouldhaveambiguoussemantics.
Itisnotpossibletomixexceptandexcept*inthesametry. Thebreak,continue,andreturnstatements
cannotappearinanexcept*clause.
8.4.3 else clause
Theoptionalelseclauseisexecutedifthecontrolflowleavesthetrysuite,noexceptionwasraised,andnoreturn,
continue, or break statement was executed. Exceptions in the else clause are not handled by the preceding
exceptclauses.
8.4.4 finally clause
Iffinallyispresent,itspecifiesa‘cleanup’handler. Thetryclauseisexecuted,includinganyexceptandelse
clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved. The
finallyclauseisexecuted. Ifthereisasavedexceptionitisre-raisedattheendofthefinallyclause. Ifthe
finally clause raises another exception, the saved exception is set as the context of the new exception. If the
finallyclauseexecutesareturn,breakorcontinuestatement,thesavedexceptionisdiscarded. Forexample,
thisfunctionreturns42.
def f():
try:
1/0
finally:
return 42
Theexceptioninformationisnotavailabletotheprogramduringexecutionofthefinallyclause.
Whenareturn,breakorcontinuestatementisexecutedinthetry suiteofatry…finallystatement,the
finallyclauseisalsoexecuted‘onthewayout.’
The return value of a function is determined by the last return statement executed. Since the finally clause
always executes, a return statement executed in the finally clause will always be the last one executed. The
followingfunctionreturns‘finally’.
def foo():
try:
return 'try'
finally:
return 'finally'
Changed in version 3.8: Prior to Python 3.8, a continue statement was illegal in the finally clause due to a
problemwiththeimplementation.
Changedinversion3.14: ThecompileremitsaSyntaxWarningwhenareturn,breakorcontinueappearsin
afinallyblock(seePEP765).
8.4. The statement 121

### 第130页

8.5 The with statement
The with statement is used to wrap the execution of a block with methods defined by a context manager (see
section With Statement Context Managers). This allows common try…except…finally usage patterns to be
encapsulatedforconvenientreuse.
with_stmt: "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents ) ":"
with_stmt_contents: with_item ("," with_item)*
with_item: expression ["as" target]
Theexecutionofthewithstatementwithone“item”proceedsasfollows:
1. Thecontextexpression(theexpressiongiveninthewith_item)isevaluatedtoobtainacontextmanager.
2. Thecontextmanager’s__enter__()isloadedforlateruse.
3. Thecontextmanager’s__exit__()isloadedforlateruse.
4. Thecontextmanager’s__enter__()methodisinvoked.
5. Ifatargetwasincludedinthewithstatement,thereturnvaluefrom__enter__()isassignedtoit.
(cid:174) Note
The with statement guarantees that if the __enter__() method returns without an error, then
__exit__() will always be called. Thus, if an error occurs during the assignment to the target list, it
willbetreatedthesameasanerroroccurringwithinthesuitewouldbe. Seestep7below.
6. Thesuiteisexecuted.
7. Thecontextmanager’s__exit__()methodisinvoked. Ifanexceptioncausedthesuitetobeexited,itstype,
value,andtracebackarepassedasargumentsto__exit__(). Otherwise,threeNoneargumentsaresupplied.
Ifthesuitewasexitedduetoanexception,andthereturnvaluefromthe__exit__()methodwasfalse,the
exceptionisreraised. Ifthereturnvaluewastrue,theexceptionissuppressed,andexecutioncontinueswith
thestatementfollowingthewithstatement.
Ifthesuitewasexitedforanyreasonotherthananexception,thereturnvaluefrom__exit__()isignored,
andexecutionproceedsatthenormallocationforthekindofexitthatwastaken.
Thefollowingcode:
with EXPRESSION as TARGET:
SUITE
issemanticallyequivalentto:
manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False
try:
TARGET = value
SUITE
except:
hit_except = True
if not exit(manager, *sys.exc_info()):
raise
finally:
(continuesonnextpage)
122 Chapter8. Compoundstatements

### 第131页

(continuedfrompreviouspage)
if not hit_except:
exit(manager, None, None, None)
Withmorethanoneitem,thecontextmanagersareprocessedasifmultiplewithstatementswerenested:
with A() as a, B() as b:
SUITE
issemanticallyequivalentto:
with A() as a:
with B() as b:
SUITE
You can also write multi-item context managers in multiple lines if the items are surrounded by parentheses. For
example:
with (
A() as a,
B() as b,
):
SUITE
Changedinversion3.1: Supportformultiplecontextexpressions.
Changedinversion3.10: Supportforusinggroupingparenthesestobreakthestatementinmultiplelines.
(cid:181) Seealso
PEP343-The“with”statement
Thespecification,background,andexamplesforthePythonwithstatement.
8.6 The match statement
Addedinversion3.10.
Thematchstatementisusedforpatternmatching. Syntax:
match_stmt: 'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
subject_expr: `!star_named_expression` "," `!star_named_expressions`?
| `!named_expression`
case_block: 'case' patterns [guard] ":" `!block`
(cid:174) Note
Thissectionusessinglequotestodenotesoftkeywords.
Patternmatchingtakesapatternasinput(followingcase)andasubjectvalue(followingmatch). Thepattern(which
maycontainsubpatterns)ismatchedagainstthesubjectvalue. Theoutcomesare:
• Amatchsuccessorfailure(alsotermedapatternsuccessorfailure).
• Possiblebindingofmatchedvaluestoaname. Theprerequisitesforthisarefurtherdiscussedbelow.
Thematchandcasekeywordsaresoftkeywords.
8.6. The statement 123

| (cid:181) Seealso |
| --- |
| PEP343-The“with”statement
Thespecification,background,andexamplesforthePythonwithstatement. |

### 第132页

(cid:181) Seealso
• PEP634–StructuralPatternMatching: Specification
• PEP636–StructuralPatternMatching: Tutorial
8.6.1 Overview
Here’sanoverviewofthelogicalflowofamatchstatement:
1. The subject expression subject_expr is evaluated and a resulting subject value obtained. If the subject
expressioncontainsacomma,atupleisconstructedusingthestandardrules.
2. Each pattern in a case_block is attempted to match with the subject value. The specific rules for success
orfailurearedescribedbelow. Thematchattemptcanalsobindsomeorallofthestandalonenameswithin
thepattern. Theprecisepatternbindingrulesvaryperpatterntypeandarespecifiedbelow. Namebindings
made during a successful pattern match outlive the executed block and can be used after the match
statement.
(cid:174) Note
Duringfailedpatternmatches,somesubpatternsmaysucceed. Donotrelyonbindingsbeingmadefora
failedmatch. Conversely, donotrelyonvariablesremainingunchangedafterafailedmatch. Theexact
behavior is dependent on implementation and may vary. This is an intentional decision made to allow
differentimplementationstoaddoptimizations.
3. Ifthepatternsucceeds,thecorrespondingguard(ifpresent)isevaluated. Inthiscaseallnamebindingsare
guaranteedtohavehappened.
• Iftheguardevaluatesastrueorismissing,theblockinsidecase_blockisexecuted.
• Otherwise,thenextcase_blockisattemptedasdescribedabove.
• Iftherearenofurthercaseblocks,thematchstatementiscompleted.
(cid:174) Note
Users should generally never rely on a pattern being evaluated. Depending on implementation, the interpreter
maycachevaluesoruseotheroptimizationswhichskiprepeatedevaluations.
Asamplematchstatement:
>>> flag = False
>>> match (100, 200):
... case (100, 300): # Mismatch: 200 != 300
... print('Case 1')
... case (100, 200) if flag: # Successful match, but guard fails
... print('Case 2')
... case (100, y): # Matches and binds y to 200
... print(f'Case 3, y: {y}')
... case _: # Pattern not attempted
... print('Case 4, I match anything!')
...
Case 3, y: 200
Inthiscase,if flagisaguard. Readmoreaboutthatinthenextsection.
124 Chapter8. Compoundstatements

| (cid:181) Seealso |
| --- |
| • PEP634–StructuralPatternMatching: Specification
• PEP636–StructuralPatternMatching: Tutorial |

### 第133页

8.6.2 Guards
guard: "if" `!named_expression`
Aguard(whichispartofthecase)mustsucceedforcodeinsidethecaseblocktoexecute. Ittakestheform: if
followedbyanexpression.
Thelogicalflowofacaseblockwithaguardfollows:
1. Checkthatthepatterninthecaseblocksucceeded. Ifthepatternfailed,theguardisnotevaluatedandthe
nextcaseblockischecked.
2. Ifthepatternsucceeded,evaluatetheguard.
• Iftheguardconditionevaluatesastrue,thecaseblockisselected.
• Iftheguardconditionevaluatesasfalse,thecaseblockisnotselected.
• Iftheguardraisesanexceptionduringevaluation,theexceptionbubblesup.
Guardsareallowedtohavesideeffectsastheyareexpressions. Guardevaluationmustproceedfromthefirsttothe
lastcaseblock,oneatatime,skippingcaseblockswhosepattern(s)don’tallsucceed. (I.e.,guardevaluationmust
happeninorder.) Guardevaluationmuststoponceacaseblockisselected.
8.6.3 Irrefutable Case Blocks
Anirrefutablecaseblockisamatch-allcaseblock. Amatchstatementmayhaveatmostoneirrefutablecaseblock,
anditmustbelast.
Acaseblockisconsideredirrefutableifithasnoguardanditspatternisirrefutable. Apatternisconsideredirrefutable
ifwecanprovefromitssyntaxalonethatitwillalwayssucceed. Onlythefollowingpatternsareirrefutable:
• ASPatternswhoseleft-handsideisirrefutable
• ORPatternscontainingatleastoneirrefutablepattern
• CapturePatterns
• WildcardPatterns
• parenthesizedirrefutablepatterns
8.6.4 Patterns
(cid:174) Note
ThissectionusesgrammarnotationsbeyondstandardEBNF:
• thenotationSEP.RULE+isshorthandforRULE (SEP RULE)*
• thenotation!RULEisshorthandforanegativelookaheadassertion
Thetop-levelsyntaxforpatternsis:
patterns: open_sequence_pattern | pattern
pattern: as_pattern | or_pattern
closed_pattern: | literal_pattern
| capture_pattern
| wildcard_pattern
| value_pattern
| group_pattern
| sequence_pattern
| mapping_pattern
| class_pattern
8.6. The statement 125

### 第134页

Thedescriptionsbelowwillincludeadescription“insimpleterms”ofwhatapatterndoesforillustrationpurposes
(creditstoRaymondHettingerforadocumentthatinspiredmostofthedescriptions). Notethatthesedescriptions
are purely for illustration purposes and may not reflect the underlying implementation. Furthermore, they do not
coverallvalidforms.
ORPatterns
AnORpatternistwoormorepatternsseparatedbyverticalbars|. Syntax:
or_pattern: "|".closed_pattern+
Onlythefinalsubpatternmaybeirrefutable,andeachsubpatternmustbindthesamesetofnamestoavoidambiguity.
AnORpatternmatcheseachofitssubpatternsinturntothesubjectvalue, untilonesucceeds. TheORpatternis
thenconsideredsuccessful. Otherwise,ifnoneofthesubpatternssucceed,theORpatternfails.
Insimpleterms,P1 | P2 | ...willtrytomatchP1,ifitfailsitwilltrytomatchP2,succeedingimmediatelyif
anysucceeds,failingotherwise.
ASPatterns
AnASpatternmatchesanORpatternontheleftoftheaskeywordagainstasubject. Syntax:
as_pattern: or_pattern "as" capture_pattern
IftheORpatternfails,theASpatternfails. Otherwise,theASpatternbindsthesubjecttothenameontherightof
theaskeywordandsucceeds. capture_patterncannotbea_.
InsimpletermsP as NAMEwillmatchwithP,andonsuccessitwillsetNAME = <subject>.
LiteralPatterns
AliteralpatterncorrespondstomostliteralsinPython. Syntax:
literal_pattern: signed_number
| signed_number "+" NUMBER
| signed_number "-" NUMBER
| strings
| "None"
| "True"
| "False"
signed_number: ["-"] NUMBER
The rule strings and the token NUMBER are defined in the standard Python grammar. Triple-quoted strings are
supported. Rawstringsandbytestringsaresupported. f-stringsandt-stringsarenotsupported.
Theformssigned_number '+' NUMBERandsigned_number '-' NUMBERareforexpressingcomplexnum-
bers;theyrequirearealnumberontheleftandanimaginarynumberontheright. E.g. 3 + 4j.
In simple terms, LITERAL will succeed only if <subject> == LITERAL. For the singletons None, True and
False,theisoperatorisused.
CapturePatterns
Acapturepatternbindsthesubjectvaluetoaname. Syntax:
capture_pattern: !'_' NAME
A single underscore _ is not a capture pattern (this is what !'_' expresses). It is instead treated as a
wildcard_pattern.
Inagivenpattern,agivennamecanonlybeboundonce. E.g. case x, x: ... isinvalidwhilecase [x] | x:
... isallowed.
126 Chapter8. Compoundstatements

### 第135页

Capturepatternsalwayssucceed. Thebindingfollowsscopingrulesestablishedbytheassignmentexpressionoperator
inPEP572;thenamebecomesalocalvariableintheclosestcontainingfunctionscopeunlessthere’sanapplicable
globalornonlocalstatement.
InsimpletermsNAMEwillalwayssucceedanditwillsetNAME = <subject>.
WildcardPatterns
Awildcardpatternalwayssucceeds(matchesanything)andbindsnoname. Syntax:
wildcard_pattern: '_'
_isasoftkeywordwithinanypattern,butonlywithinpatterns. Itisanidentifier,asusual,evenwithinmatchsubject
expressions,guards,andcaseblocks.
Insimpleterms,_willalwayssucceed.
ValuePatterns
AvaluepatternrepresentsanamedvalueinPython. Syntax:
value_pattern: attr
attr: name_or_attr "." NAME
name_or_attr: attr | NAME
ThedottednameinthepatternislookedupusingstandardPythonnameresolutionrules. Thepatternsucceedsifthe
valuefoundcomparesequaltothesubjectvalue(usingthe==equalityoperator).
InsimpletermsNAME1.NAME2willsucceedonlyif<subject> == NAME1.NAME2
(cid:174) Note
Ifthesamevalueoccursmultipletimesinthesamematchstatement, theinterpretermaycachethefirstvalue
foundandreuseitratherthanrepeatthesamelookup. Thiscacheisstrictlytiedtoagivenexecutionofagiven
matchstatement.
GroupPatterns
Agrouppatternallowsuserstoaddparenthesesaroundpatternstoemphasizetheintendedgrouping. Otherwise,it
hasnoadditionalsyntax. Syntax:
group_pattern: "(" pattern ")"
Insimpleterms(P)hasthesameeffectasP.
SequencePatterns
Asequencepatterncontainsseveralsubpatternstobematchedagainstsequenceelements. Thesyntaxissimilarto
theunpackingofalistortuple.
sequence_pattern: "[" [maybe_sequence_pattern] "]"
| "(" [open_sequence_pattern] ")"
open_sequence_pattern: maybe_star_pattern "," [maybe_sequence_pattern]
maybe_sequence_pattern: ",".maybe_star_pattern+ ","?
maybe_star_pattern: star_pattern | pattern
star_pattern: "*" (capture_pattern | wildcard_pattern)
Thereisnodifferenceifparenthesesorsquarebracketsareusedforsequencepatterns(i.e. (...)vs[...]).
8.6. The statement 127

### 第136页

(cid:174) Note
Asinglepatternenclosedinparentheseswithoutatrailingcomma(e.g. (3 | 4))isagrouppattern. Whilea
singlepatternenclosedinsquarebrackets(e.g. [3 | 4])isstillasequencepattern.
At most one star subpattern may be in a sequence pattern. The star subpattern may occur in any position. If no
star subpatternis present, thesequence patternisa fixed-lengthsequencepattern; otherwiseit isa variable-length
sequencepattern.
Thefollowingisthelogicalflowformatchingasequencepatternagainstasubjectvalue:
1. Ifthesubjectvalueisnotasequence2,thesequencepatternfails.
2. Ifthesubjectvalueisaninstanceofstr,bytesorbytearraythesequencepatternfails.
3. Thesubsequentstepsdependonwhetherthesequencepatternisfixedorvariable-length.
Ifthesequencepatternisfixed-length:
1. Ifthelengthofthesubjectsequenceisnotequaltothenumberofsubpatterns,thesequencepatternfails
2. Subpatterns in the sequence pattern are matched to their corresponding items in the subject sequence
fromlefttoright. Matchingstopsassoonasasubpatternfails. Ifallsubpatternssucceedinmatching
theircorrespondingitem,thesequencepatternsucceeds.
Otherwise,ifthesequencepatternisvariable-length:
1. Ifthelengthofthesubjectsequenceislessthanthenumberofnon-starsubpatterns,thesequencepattern
fails.
2. Theleadingnon-starsubpatternsarematchedtotheircorrespondingitemsasforfixed-lengthsequences.
3. Ifthepreviousstepsucceeds,thestarsubpatternmatchesalistformedoftheremainingsubjectitems,
excludingtheremainingitemscorrespondingtonon-starsubpatternsfollowingthestarsubpattern.
4. Remainingnon-starsubpatternsarematchedtotheircorrespondingsubjectitems,asforafixed-length
sequence.
(cid:174) Note
Thelengthofthesubjectsequenceisobtainedvialen()(i.e. viathe__len__()protocol). Thislength
maybecachedbytheinterpreterinasimilarmannerasvaluepatterns.
Insimpleterms[P1, P2, P3,…, P<N>]matchesonlyifallthefollowinghappens:
• check<subject>isasequence
• len(subject) == <N>
2Inpatternmatching,asequenceisdefinedasoneofthefollowing:
• aclassthatinheritsfromcollections.abc.Sequence
• aPythonclassthathasbeenregisteredascollections.abc.Sequence
• abuiltinclassthathasits(CPython)Py_TPFLAGS_SEQUENCEbitset
• aclassthatinheritsfromanyoftheabove
Thefollowingstandardlibraryclassesaresequences:
• array.array
• collections.deque
• list
• memoryview
• range
• tuple
(cid:174) Note
Subjectvaluesoftypestr,bytes,andbytearraydonotmatchsequencepatterns.
128 Chapter8. Compoundstatements

### 第137页

• P1matches<subject>[0](notethatthismatchcanalsobindnames)
• P2matches<subject>[1](notethatthismatchcanalsobindnames)
• …andsoonforthecorrespondingpattern/element.
MappingPatterns
Amappingpatterncontainsoneormorekey-valuepatterns. Thesyntaxissimilartotheconstructionofadictionary.
Syntax:
mapping_pattern: "{" [items_pattern] "}"
items_pattern: ",".key_value_pattern+ ","?
key_value_pattern: (literal_pattern | value_pattern) ":" pattern
| double_star_pattern
double_star_pattern: "**" capture_pattern
Atmostonedoublestarpatternmaybeinamappingpattern. Thedoublestarpatternmustbethelastsubpatternin
themappingpattern.
Duplicatekeysinmappingpatternsaredisallowed. DuplicateliteralkeyswillraiseaSyntaxError. Twokeysthat
otherwisehavethesamevaluewillraiseaValueErroratruntime.
Thefollowingisthelogicalflowformatchingamappingpatternagainstasubjectvalue:
1. Ifthesubjectvalueisnotamapping3,themappingpatternfails.
2. Ifeverykeygiveninthemappingpatternispresentinthesubjectmapping,andthepatternforeachkeymatches
thecorrespondingitemofthesubjectmapping,themappingpatternsucceeds.
3. Ifduplicatekeysaredetectedinthemappingpattern,thepatternisconsideredinvalid. ASyntaxErroris
raisedforduplicateliteralvalues;oraValueErrorfornamedkeysofthesamevalue.
(cid:174) Note
Key-value pairs are matched using the two-argument form of the mapping subject’s get() method. Matched
key-value pairs must already be present in the mapping, and not created on-the-fly via __missing__() or
__getitem__().
Insimpleterms{KEY1: P1, KEY2: P2, ... }matchesonlyifallthefollowinghappens:
• check<subject>isamapping
• KEY1 in <subject>
• P1matches<subject>[KEY1]
• …andsoonforthecorrespondingKEY/patternpair.
ClassPatterns
Aclasspatternrepresentsaclassanditspositionalandkeywordarguments(ifany). Syntax:
class_pattern: name_or_attr "(" [pattern_arguments ","?] ")"
pattern_arguments: positional_patterns ["," keyword_patterns]
| keyword_patterns
positional_patterns: ",".pattern+
keyword_patterns: ",".keyword_pattern+
3Inpatternmatching,amappingisdefinedasoneofthefollowing:
• aclassthatinheritsfromcollections.abc.Mapping
• aPythonclassthathasbeenregisteredascollections.abc.Mapping
• abuiltinclassthathasits(CPython)Py_TPFLAGS_MAPPINGbitset
• aclassthatinheritsfromanyoftheabove
Thestandardlibraryclassesdictandtypes.MappingProxyTypearemappings.
8.6. The statement 129

### 第138页

keyword_pattern: NAME "=" pattern
Thesamekeywordshouldnotberepeatedinclasspatterns.
Thefollowingisthelogicalflowformatchingaclasspatternagainstasubjectvalue:
1. Ifname_or_attrisnotaninstanceofthebuiltintype,raiseTypeError.
2. Ifthesubjectvalueisnotaninstanceofname_or_attr(testedviaisinstance()),theclasspatternfails.
3. Ifnopatternargumentsarepresent,thepatternsucceeds. Otherwise,thesubsequentstepsdependonwhether
keywordorpositionalargumentpatternsarepresent.
Foranumberofbuilt-intypes(specifiedbelow),asinglepositionalsubpatternisacceptedwhichwillmatch
theentiresubject;forthesetypeskeywordpatternsalsoworkasforothertypes.
Ifonlykeywordpatternsarepresent,theyareprocessedasfollows,onebyone:
I.Thekeywordislookedupasanattributeonthesubject.
• IfthisraisesanexceptionotherthanAttributeError,theexceptionbubblesup.
• IfthisraisesAttributeError,theclasspatternhasfailed.
• Else,thesubpatternassociatedwiththekeywordpatternismatchedagainstthesubject’sattributevalue.
Ifthisfails,theclasspatternfails;ifthissucceeds,thematchproceedstothenextkeyword.
II.Ifallkeywordpatternssucceed,theclasspatternsucceeds.
If any positional patterns are present, they are converted to keyword patterns using the __match_args__
attributeontheclassname_or_attrbeforematching:
I.Theequivalentofgetattr(cls, "__match_args__", ())iscalled.
• Ifthisraisesanexception,theexceptionbubblesup.
• Ifthereturnedvalueisnotatuple,theconversionfailsandTypeErrorisraised.
• If there are more positional patterns than len(cls.__match_args__), TypeError is
raised.
• Otherwise,positionalpatterniisconvertedtoakeywordpatternusing__match_args__[i]
asthekeyword. __match_args__[i]mustbeastring;ifnotTypeErrorisraised.
• Ifthereareduplicatekeywords,TypeErrorisraised.
(cid:181) Seealso
Customizingpositionalargumentsinclasspatternmatching
II.Onceallpositionalpatternshavebeenconvertedtokeywordpatterns,
thematchproceedsasiftherewereonlykeywordpatterns.
Forthefollowingbuilt-intypesthehandlingofpositionalsubpatternsisdifferent:
• bool
• bytearray
• bytes
• dict
• float
• frozenset
• int
• list
• set
130 Chapter8. Compoundstatements

| (cid:181) Seealso |
| --- |
| Customizingpositionalargumentsinclasspatternmatching |

### 第139页

• str
• tuple
Theseclassesacceptasinglepositionalargument, andthepatternthereismatchedagainstthewholeobject
ratherthananattribute. Forexampleint(0|1)matchesthevalue0,butnotthevalue0.0.
InsimpletermsCLS(P1, attr=P2)matchesonlyifthefollowinghappens:
• isinstance(<subject>, CLS)
• convertP1toakeywordpatternusingCLS.__match_args__
• Foreachkeywordargumentattr=P2:
– hasattr(<subject>, "attr")
– P2matches<subject>.attr
• …andsoonforthecorrespondingkeywordargument/patternpair.
(cid:181) Seealso
• PEP634–StructuralPatternMatching: Specification
• PEP636–StructuralPatternMatching: Tutorial
8.7 Function definitions
Afunctiondefinitiondefinesauser-definedfunctionobject(seesectionThestandardtypehierarchy):
funcdef: [decorators] "def" funcname [type_params] "(" [parameter_lis
["->" expression] ":" suite
decorators: decorator+
decorator: "@" assignment_expression NEWLINE
parameter_list: defparameter ("," defparameter)* "," "/" ["," [parameter_lis
| parameter_list_no_posonly
parameter_list_no_posonly: defparameter ("," defparameter)* ["," [parameter_list_starar
| parameter_list_starargs
parameter_list_starargs: "*" [star_parameter] ("," defparameter)* ["," [parameter_sta
| "*" ("," defparameter)+ ["," [parameter_star_kwargs]]
| parameter_star_kwargs
parameter_star_kwargs: "**" parameter [","]
parameter: identifier [":" expression]
star_parameter: identifier [":" ["*"] expression]
defparameter: parameter ["=" expression]
funcname: identifier
Afunctiondefinitionisanexecutablestatement. Itsexecutionbindsthefunctionnameinthecurrentlocalnamespace
toafunctionobject(awrapperaroundtheexecutablecodeforthefunction). Thisfunctionobjectcontainsareference
tothecurrentglobalnamespaceastheglobalnamespacetobeusedwhenthefunctioniscalled.
Thefunctiondefinitiondoesnotexecutethefunctionbody;thisgetsexecutedonlywhenthefunctioniscalled.4
Afunctiondefinitionmaybewrappedbyoneormoredecorator expressions. Decoratorexpressionsareevaluated
whenthefunctionisdefined,inthescopethatcontainsthefunctiondefinition. Theresultmustbeacallable,which
isinvokedwiththefunctionobjectastheonlyargument. Thereturnedvalueisboundtothefunctionnameinstead
ofthefunctionobject. Multipledecoratorsareappliedinnestedfashion. Forexample,thefollowingcode
4Astringliteralappearingasthefirststatementinthefunctionbodyistransformedintothefunction’s__doc__attributeandthereforethe
function’sdocstring.
8.7. Functiondefinitions 131

| (cid:181) Seealso |
| --- |
| • PEP634–StructuralPatternMatching: Specification
• PEP636–StructuralPatternMatching: Tutorial |

### 第140页

@f1(arg)
@f2
def func(): pass
isroughlyequivalentto
def func(): pass
func = f1(arg)(f2(func))
exceptthattheoriginalfunctionisnottemporarilyboundtothenamefunc.
Changed in version 3.9: Functions may be decorated with any valid assignment_expression. Previously, the
grammarwasmuchmorerestrictive;seePEP614fordetails.
Alistoftypeparametersmaybegiveninsquarebracketsbetweenthefunction’snameandtheopeningparenthesisfor
itsparameterlist. Thisindicatestostatictypecheckersthatthefunctionisgeneric. Atruntime,thetypeparameters
canberetrievedfromthefunction’s__type_params__attribute. SeeGenericfunctionsformore.
Changedinversion3.12: TypeparameterlistsarenewinPython3.12.
Whenoneormoreparametershavetheformparameter=expression,thefunctionissaidtohave“defaultparameter
values.” Foraparameterwithadefaultvalue,thecorrespondingargumentmaybeomittedfromacall,inwhichcase
theparameter’sdefaultvalueissubstituted. Ifaparameterhasadefaultvalue,allfollowingparametersupuntilthe
“*”mustalsohaveadefaultvalue—thisisasyntacticrestrictionthatisnotexpressedbythegrammar.
Defaultparametervaluesareevaluatedfromlefttorightwhenthefunctiondefinitionisexecuted. Thismeans
thattheexpressionisevaluatedonce,whenthefunctionisdefined,andthatthesame“pre-computed”valueisused
foreachcall. Thisisespeciallyimportanttounderstandwhenadefaultparametervalueisamutableobject,suchas
alistoradictionary: ifthefunctionmodifiestheobject(e.g. byappendinganitemtoalist),thedefaultparameter
valueisineffectmodified. Thisisgenerallynotwhatwasintended. AwayaroundthisistouseNoneasthedefault,
andexplicitlytestforitinthebodyofthefunction,e.g.:
def whats_on_the_telly(penguin=None):
if penguin is None:
penguin = []
penguin.append("property of the zoo")
return penguin
FunctioncallsemanticsaredescribedinmoredetailinsectionCalls. Afunctioncallalwaysassignsvaluestoallpa-
rametersmentionedintheparameterlist,eitherfrompositionalarguments,fromkeywordarguments,orfromdefault
values. Iftheform“*identifier”ispresent,itisinitializedtoatuplereceivinganyexcesspositionalparameters,
defaultingtotheemptytuple. If theform“**identifier”ispresent, itisinitializedtoaneworderedmapping
receiving any excess keyword arguments, defaulting to a new empty mapping of the same type. Parameters after
“*”or“*identifier”arekeyword-onlyparametersandmayonlybepassedbykeywordarguments. Parameters
before“/”arepositional-onlyparametersandmayonlybepassedbypositionalarguments.
Changedinversion3.8: The/functionparametersyntaxmaybeusedtoindicatepositional-onlyparameters. See
PEP570fordetails.
Parametersmayhaveanannotationoftheform“: expression”followingtheparametername. Anyparameter
mayhaveanannotation,eventhoseoftheform*identifieror**identifier. (Asaspecialcase,parameters
oftheform*identifiermayhaveanannotation“: *expression”.) Functionsmayhave“return”annotation
of the form “-> expression” after the parameter list. These annotations can be any valid Python expression.
Thepresenceofannotationsdoesnotchangethesemanticsofafunction. SeeAnnotationsformoreinformationon
annotations.
Changedinversion3.11: Parametersoftheform“*identifier”mayhaveanannotation“: *expression”. See
PEP646.
Itisalsopossibletocreateanonymousfunctions(functionsnotboundtoaname),forimmediateuseinexpressions.
Thisuseslambdaexpressions,describedinsectionLambdas. Notethatthelambdaexpressionismerelyashorthand
for a simplified function definition; a function defined in a “def” statement can be passed around or assigned to
132 Chapter8. Compoundstatements

### 第141页

anothernamejustlikeafunctiondefinedbyalambdaexpression. The“def”formisactuallymorepowerfulsinceit
allowstheexecutionofmultiplestatementsandannotations.
Programmer’s note: Functions are first-class objects. A “def” statement executed inside a function definition
definesalocalfunctionthatcanbereturnedorpassedaround. Freevariablesusedinthenestedfunctioncanaccess
thelocalvariablesofthefunctioncontainingthedef. SeesectionNamingandbindingfordetails.
(cid:181) Seealso
PEP3107-FunctionAnnotations
Theoriginalspecificationforfunctionannotations.
PEP484-TypeHints
Definitionofastandardmeaningforannotations: typehints.
PEP526-SyntaxforVariableAnnotations
Abilitytotypehintvariabledeclarations,includingclassvariablesandinstancevariables.
PEP563-PostponedEvaluationofAnnotations
Support for forward references within annotations by preserving annotations in a string form at runtime
insteadofeagerevaluation.
PEP318-DecoratorsforFunctionsandMethods
Functionandmethoddecoratorswereintroduced. ClassdecoratorswereintroducedinPEP3129.
8.8 Class definitions
Aclassdefinitiondefinesaclassobject(seesectionThestandardtypehierarchy):
classdef: [decorators] "class" classname [type_params] [inheritance] ":" suite
inheritance: "(" [argument_list] ")"
classname: identifier
Aclassdefinitionisanexecutablestatement. Theinheritancelistusuallygivesalistofbaseclasses(seeMetaclasses
formoreadvanceduses),soeachiteminthelistshouldevaluatetoaclassobjectwhichallowssubclassing. Classes
withoutaninheritancelistinherit,bydefault,fromthebaseclassobject;hence,
class Foo:
pass
isequivalentto
class Foo(object):
pass
The class’s suite is then executed in a new execution frame (see Naming and binding), using a newly created local
namespace and theoriginal global namespace. (Usually, the suite containsmostly function definitions.) Whenthe
class’ssuitefinishesexecution,itsexecutionframeisdiscardedbutitslocalnamespaceissaved.5 Aclassobjectis
thencreatedusingtheinheritancelistforthebaseclassesandthesavedlocalnamespacefortheattributedictionary.
Theclassnameisboundtothisclassobjectintheoriginallocalnamespace.
Theorderinwhichattributesaredefinedintheclassbodyispreservedinthenewclass’s__dict__. Notethatthis
isreliableonlyrightaftertheclassiscreatedandonlyforclassesthatweredefinedusingthedefinitionsyntax.
Classcreationcanbecustomizedheavilyusingmetaclasses.
Classescanalsobedecorated: justlikewhendecoratingfunctions,
5Astringliteralappearingasthefirststatementintheclassbodyistransformedintothenamespace’s__doc__itemandthereforetheclass’s
docstring.
8.8. Classdefinitions 133

| (cid:181) Seealso |
| --- |
| PEP3107-FunctionAnnotations
Theoriginalspecificationforfunctionannotations.
PEP484-TypeHints
Definitionofastandardmeaningforannotations: typehints.
PEP526-SyntaxforVariableAnnotations
Abilitytotypehintvariabledeclarations,includingclassvariablesandinstancevariables.
PEP563-PostponedEvaluationofAnnotations
Support for forward references within annotations by preserving annotations in a string form at runtime
insteadofeagerevaluation.
PEP318-DecoratorsforFunctionsandMethods
Functionandmethoddecoratorswereintroduced. ClassdecoratorswereintroducedinPEP3129. |

### 第142页

@f1(arg)
@f2
class Foo: pass
isroughlyequivalentto
class Foo: pass
Foo = f1(arg)(f2(Foo))
Theevaluationrulesforthedecoratorexpressionsarethesameasforfunctiondecorators. Theresultisthenbound
totheclassname.
Changed in version 3.9: Classes may be decorated with any valid assignment_expression. Previously, the
grammarwasmuchmorerestrictive;seePEP614fordetails.
A list of type parameters may be given in square brackets immediately after the class’s name. This indicates to
static type checkers that the class is generic. At runtime, the type parameters can be retrieved from the class’s
__type_params__attribute. SeeGenericclassesformore.
Changedinversion3.12: TypeparameterlistsarenewinPython3.12.
Programmer’snote: Variablesdefinedintheclassdefinitionareclassattributes;theyaresharedbyinstances. In-
stanceattributescanbesetinamethodwithself.name = value. Bothclassandinstanceattributesareaccessible
throughthenotation“self.name”, andaninstanceattributehidesaclassattributewiththesamenamewhenac-
cessedinthisway. Classattributescanbeusedasdefaultsforinstanceattributes,butusingmutablevaluestherecan
leadtounexpectedresults. Descriptorscanbeusedtocreateinstancevariableswithdifferentimplementationdetails.
(cid:181) Seealso
PEP3115-MetaclassesinPython3000
Theproposalthatchangedthedeclarationofmetaclassestothecurrentsyntax,andthesemanticsforhow
classeswithmetaclassesareconstructed.
PEP3129-ClassDecorators
Theproposalthataddedclassdecorators. FunctionandmethoddecoratorswereintroducedinPEP318.
8.9 Coroutines
Addedinversion3.5.
8.9.1 Coroutine function definition
async_funcdef: [decorators] "async" "def" funcname "(" [parameter_list] ")"
["->" expression] ":" suite
ExecutionofPythoncoroutinescanbesuspendedandresumedatmanypoints(seecoroutine). awaitexpressions,
async forandasync withcanonlybeusedinthebodyofacoroutinefunction.
Functions defined with async def syntax are always coroutine functions, even if they do not contain await or
asynckeywords.
ItisaSyntaxErrortouseayield fromexpressioninsidethebodyofacoroutinefunction.
Anexampleofacoroutinefunction:
async def func(param1, param2):
do_stuff()
await some_coroutine()
Changedinversion3.7: awaitandasyncarenowkeywords;previouslytheywereonlytreatedassuchinsidethe
bodyofacoroutinefunction.
134 Chapter8. Compoundstatements

| (cid:181) Seealso |
| --- |
| PEP3115-MetaclassesinPython3000
Theproposalthatchangedthedeclarationofmetaclassestothecurrentsyntax,andthesemanticsforhow
classeswithmetaclassesareconstructed.
PEP3129-ClassDecorators
Theproposalthataddedclassdecorators. FunctionandmethoddecoratorswereintroducedinPEP318. |

### 第143页

8.9.2 The async for statement
async_for_stmt: "async" for_stmt
Anasynchronousiterableprovidesan__aiter__methodthatdirectlyreturnsanasynchronousiterator,whichcan
callasynchronouscodeinits__anext__method.
Theasync forstatementallowsconvenientiterationoverasynchronousiterables.
Thefollowingcode:
async for TARGET in ITER:
SUITE
else:
SUITE2
Issemanticallyequivalentto:
iter = (ITER)
iter = type(iter).__aiter__(iter)
running = True
while running:
try:
TARGET = await type(iter).__anext__(iter)
except StopAsyncIteration:
running = False
else:
SUITE
else:
SUITE2
Seealso__aiter__()and__anext__()fordetails.
ItisaSyntaxErrortouseanasync forstatementoutsidethebodyofacoroutinefunction.
8.9.3 The async with statement
async_with_stmt: "async" with_stmt
Anasynchronouscontextmanagerisacontextmanagerthatisabletosuspendexecutioninitsenterandexitmethods.
Thefollowingcode:
async with EXPRESSION as TARGET:
SUITE
issemanticallyequivalentto:
manager = (EXPRESSION)
aenter = type(manager).__aenter__
aexit = type(manager).__aexit__
value = await aenter(manager)
hit_except = False
try:
TARGET = value
SUITE
except:
hit_except = True
if not await aexit(manager, *sys.exc_info()):
(continuesonnextpage)
8.9. Coroutines 135

### 第144页

(continuedfrompreviouspage)
raise
finally:
if not hit_except:
await aexit(manager, None, None, None)
Seealso__aenter__()and__aexit__()fordetails.
ItisaSyntaxErrortouseanasync withstatementoutsidethebodyofacoroutinefunction.
(cid:181) Seealso
PEP492-Coroutineswithasyncandawaitsyntax
TheproposalthatmadecoroutinesaproperstandaloneconceptinPython,andaddedsupportingsyntax.
8.10 Type parameter lists
Addedinversion3.12.
Changedinversion3.13: Supportfordefaultvalueswasadded(seePEP696).
type_params: "[" type_param ("," type_param)* "]"
type_param: typevar | typevartuple | paramspec
typevar: identifier (":" expression)? ("=" expression)?
typevartuple: "*" identifier ("=" expression)?
paramspec: "**" identifier ("=" expression)?
Functions(includingcoroutines),classesandtypealiasesmaycontainatypeparameterlist:
def max[T](args: list[T]) -> T:
...
async def amax[T](args: list[T]) -> T:
...
class Bag[T]:
def __iter__(self) -> Iterator[T]:
...
def add(self, arg: T) -> None:
...
type ListOrSet[T] = list[T] | set[T]
Semantically,thisindicatesthatthefunction,class,ortypealiasisgenericoveratypevariable. Thisinformationis
primarilyusedbystatictypecheckers,andatruntime,genericobjectsbehavemuchliketheirnon-genericcounter-
parts.
Typeparametersaredeclaredinsquarebrackets([])immediatelyafterthenameofthefunction,class,ortypealias.
Thetypeparametersareaccessiblewithinthescopeofthegenericobject,butnotelsewhere. Thus,afteradeclaration
def func[T](): pass,thenameTisnotavailableinthemodulescope. Below,thesemanticsofgenericobjects
aredescribedwithmoreprecision. Thescopeoftypeparametersismodeledwithaspecialfunction(technically,an
annotationscope)thatwrapsthecreationofthegenericobject.
Genericfunctions,classes,andtypealiaseshavea__type_params__attributelistingtheirtypeparameters.
Typeparameterscomeinthreekinds:
• typing.TypeVar,introducedbyaplainname(e.g.,T).Semantically,thisrepresentsasingletypetoatype
checker.
136 Chapter8. Compoundstatements

| (cid:181) Seealso |
| --- |
| PEP492-Coroutineswithasyncandawaitsyntax
TheproposalthatmadecoroutinesaproperstandaloneconceptinPython,andaddedsupportingsyntax. |

### 第145页

• typing.TypeVarTuple,introducedbyanameprefixedwithasingleasterisk(e.g.,*Ts). Semantically,this
standsforatupleofanynumberoftypes.
• typing.ParamSpec,introducedbyanameprefixedwithtwoasterisks(e.g.,**P).Semantically,thisstands
fortheparametersofacallable.
typing.TypeVar declarations can define bounds and constraints with a colon (:) followed by an expression. A
single expression after the colon indicates a bound (e.g. T: int). Semantically, this means that the typing.
TypeVarcanonlyrepresenttypesthatareasubtypeofthisbound. Aparenthesizedtupleofexpressionsafterthe
colonindicatesasetofconstraints(e.g. T: (str, bytes)). Eachmemberofthetupleshouldbeatype(again,
thisisnotenforcedatruntime). Constrainedtypevariablescanonlytakeononeofthetypesinthelistofconstraints.
Fortyping.TypeVarsdeclaredusingthetypeparameterlistsyntax,theboundandconstraintsarenotevaluated
whenthegenericobjectiscreated,butonlywhenthevalueisexplicitlyaccessedthroughtheattributes__bound__
and__constraints__. Toaccomplishthis,theboundsorconstraintsareevaluatedinaseparateannotationscope.
typing.TypeVarTuplesandtyping.ParamSpecscannothaveboundsorconstraints.
All three flavors of type parameters can also have a default value, which is used when the type parameter is not
explicitlyprovided. Thisisaddedbyappendingasingleequalssign(=)followedbyanexpression. Likethebounds
andconstraintsoftypevariables,thedefaultvalueisnotevaluatedwhentheobjectiscreated,butonlywhenthetype
parameter’s__default__attributeisaccessed. Tothisend,thedefaultvalueisevaluatedinaseparateannotation
scope. Ifnodefaultvalueisspecifiedforatypeparameter,the__default__attributeissettothespecialsentinel
objecttyping.NoDefault.
Thefollowingexampleindicatesthefullsetofallowedtypeparameterdeclarations:
def overly_generic[
SimpleTypeVar,
TypeVarWithDefault = int,
TypeVarWithBound: int,
TypeVarWithConstraints: (str, bytes),
*SimpleTypeVarTuple = (int, float),
**SimpleParamSpec = (str, bytearray),
](
a: SimpleTypeVar,
b: TypeVarWithDefault,
c: TypeVarWithBound,
d: Callable[SimpleParamSpec, TypeVarWithConstraints],
*e: SimpleTypeVarTuple,
): ...
8.10.1 Generic functions
Genericfunctionsaredeclaredasfollows:
def func[T](arg: T): ...
Thissyntaxisequivalentto:
annotation-def TYPE_PARAMS_OF_func():
T = typing.TypeVar("T")
def func(arg: T): ...
func.__type_params__ = (T,)
return func
func = TYPE_PARAMS_OF_func()
Hereannotation-defindicatesanannotationscope, whichisnotactuallyboundtoanynameatruntime. (One
otherlibertyistakeninthetranslation: thesyntaxdoesnotgothroughattributeaccessonthetypingmodule,but
createsaninstanceoftyping.TypeVardirectly.)
8.10. Typeparameterlists 137

### 第146页

Theannotationsofgenericfunctionsareevaluatedwithintheannotationscopeusedfordeclaringthetypeparameters,
butthefunction’sdefaultsanddecoratorsarenot.
Thefollowingexampleillustratesthescopingrulesforthesecases,aswellasforadditionalflavorsoftypeparameters:
@decorator
def func[T: int, *Ts, **P](*args: *Ts, arg: Callable[P, T] = some_default):
...
ExceptforthelazyevaluationoftheTypeVarbound,thisisequivalentto:
DEFAULT_OF_arg = some_default
annotation-def TYPE_PARAMS_OF_func():
annotation-def BOUND_OF_T():
return int
# In reality, BOUND_OF_T() is evaluated only on demand.
T = typing.TypeVar("T", bound=BOUND_OF_T())
Ts = typing.TypeVarTuple("Ts")
P = typing.ParamSpec("P")
def func(*args: *Ts, arg: Callable[P, T] = DEFAULT_OF_arg):
...
func.__type_params__ = (T, Ts, P)
return func
func = decorator(TYPE_PARAMS_OF_func())
ThecapitalizednameslikeDEFAULT_OF_argarenotactuallyboundatruntime.
8.10.2 Generic classes
Genericclassesaredeclaredasfollows:
class Bag[T]: ...
Thissyntaxisequivalentto:
annotation-def TYPE_PARAMS_OF_Bag():
T = typing.TypeVar("T")
class Bag(typing.Generic[T]):
__type_params__ = (T,)
...
return Bag
Bag = TYPE_PARAMS_OF_Bag()
Here again annotation-def (not a real keyword) indicates an annotation scope, and the name
TYPE_PARAMS_OF_Bagisnotactuallyboundatruntime.
Generic classes implicitly inherit from typing.Generic. The base classes and keyword arguments of generic
classesareevaluatedwithinthetypescopeforthetypeparameters,anddecoratorsareevaluatedoutsidethatscope.
Thisisillustratedbythisexample:
@decorator
class Bag(Base[T], arg=T): ...
Thisisequivalentto:
138 Chapter8. Compoundstatements

### 第147页

annotation-def TYPE_PARAMS_OF_Bag():
T = typing.TypeVar("T")
class Bag(Base[T], typing.Generic[T], arg=T):
__type_params__ = (T,)
...
return Bag
Bag = decorator(TYPE_PARAMS_OF_Bag())
8.10.3 Generic type aliases
Thetypestatementcanalsobeusedtocreateagenerictypealias:
type ListOrSet[T] = list[T] | set[T]
Exceptforthelazyevaluationofthevalue,thisisequivalentto:
annotation-def TYPE_PARAMS_OF_ListOrSet():
T = typing.TypeVar("T")
annotation-def VALUE_OF_ListOrSet():
return list[T] | set[T]
# In reality, the value is lazily evaluated
return typing.TypeAliasType("ListOrSet", VALUE_OF_ListOrSet(), type_params=(T,
,→))
ListOrSet = TYPE_PARAMS_OF_ListOrSet()
Here, annotation-def (not a real keyword) indicates an annotation scope. The capitalized names like
TYPE_PARAMS_OF_ListOrSetarenotactuallyboundatruntime.
8.11 Annotations
Changedinversion3.14: Annotationsarenowlazilyevaluatedbydefault.
Variablesandfunctionparametersmaycarryannotations,createdbyaddingacolonafterthename,followedbyan
expression:
x: annotation = 1
def f(param: annotation): ...
Functionsmayalsocarryareturnannotationfollowinganarrow:
def f() -> annotation: ...
Annotationsareconventionallyusedfortypehints,butthisisnotenforcedbythelanguage,andingeneralannotations
maycontainarbitraryexpressions. Thepresenceofannotationsdoesnotchangetheruntimesemanticsofthecode,
exceptifsomemechanismisusedthatintrospectsandusestheannotations(suchasdataclassesorfunctools.
singledispatch()).
Bydefault,annotationsarelazilyevaluatedinanannotationscope. Thismeansthattheyarenotevaluatedwhenthe
codecontainingtheannotationisevaluated. Instead,theinterpretersavesinformationthatcanbeusedtoevaluate
theannotationlaterifrequested. Theannotationlibmoduleprovidestoolsforevaluatingannotations.
Ifthefuturestatementfrom __future__ import annotationsispresent,allannotationsareinsteadstoredas
strings:
>>> from __future__ import annotations
>>> def f(param: annotation): ...
>>> f.__annotations__
{'param': 'annotation'}
8.11. Annotations 139

### 第148页

This future statement will be deprecated and removed in a future version of Python, but not before Python
3.13 reaches its end of life (see PEP 749). When it is used, introspection tools like annotationlib.
get_annotations()andtyping.get_type_hints()arelesslikelytobeabletoresolveannotationsatrun-
time.
140 Chapter8. Compoundstatements

### 第149页

CHAPTER
NINE
TOP-LEVEL COMPONENTS
ThePythoninterpretercangetitsinputfromanumberofsources: fromascriptpassedtoitasstandardinputoras
programargument,typedininteractively,fromamodulesourcefile,etc. Thischaptergivesthesyntaxusedinthese
cases.
9.1 Complete Python programs
Whilealanguagespecificationneednotprescribehowthelanguageinterpreterisinvoked,itisusefultohaveanotion
ofacompletePythonprogram. AcompletePythonprogramisexecutedinaminimallyinitializedenvironment: all
built-inandstandardmodulesareavailable,butnonehavebeeninitialized,exceptforsys(varioussystemservices),
builtins (built-in functions, exceptions and None) and __main__. The latter is used to provide the local and
globalnamespaceforexecutionofthecompleteprogram.
ThesyntaxforacompletePythonprogramisthatforfileinput,describedinthenextsection.
Theinterpretermayalsobeinvokedininteractivemode;inthiscase,itdoesnotreadandexecuteacompleteprogram
butreadsandexecutesonestatement(possiblycompound)atatime. Theinitialenvironmentisidenticaltothatofa
completeprogram;eachstatementisexecutedinthenamespaceof__main__.
Acompleteprogramcanbepassedtotheinterpreterinthreeforms: withthe-cstringcommandlineoption,asa
filepassedasthefirstcommandlineargument,orasstandardinput. Ifthefileorstandardinputisattydevice,the
interpreterentersinteractivemode;otherwise,itexecutesthefileasacompleteprogram.
9.2 File input
Allinputreadfromnon-interactivefileshasthesameform:
file_input: (NEWLINE | statement)* ENDMARKER
Thissyntaxisusedinthefollowingsituations:
• whenparsingacompletePythonprogram(fromafileorfromastring);
• whenparsingamodule;
• whenparsingastringpassedtotheexec()function;
9.3 Interactive input
Inputininteractivemodeisparsedusingthefollowinggrammar:
interactive_input: [stmt_list] NEWLINE | compound_stmt NEWLINE | ENDMARKER
Notethata(top-level)compoundstatementmustbefollowedbyablanklineininteractivemode;thisisneededto
helptheparserdetecttheendoftheinput.
141

### 第150页

9.4 Expression input
eval()isusedforexpressioninput. Itignoresleadingwhitespace. Thestringargumenttoeval()musthavethe
followingform:
eval_input: expression_list NEWLINE* ENDMARKER
142 Chapter9. Top-levelcomponents

### 第151页

CHAPTER
TEN
FULL GRAMMAR SPECIFICATION
ThisisthefullPythongrammar,deriveddirectlyfromthegrammarusedtogeneratetheCPythonparser(seeGram-
mar/python.gram). Theversionhereomitsdetailsrelatedtocodegenerationanderrorrecovery.
Thenotationusedhereisthesameasintheprecedingdocs,andisdescribedinthenotationsection,exceptforan
extracomplication:
• ~(“cut”): committothecurrentalternativeandfailtheruleevenifthisfailstoparse
# PEG grammar for Python
# ========================= START OF THE GRAMMAR =========================
# General grammatical elements and rules:
#
# * Strings with double quotes (") denote SOFT KEYWORDS
# * Strings with single quotes (') denote KEYWORDS
# * Upper case names (NAME) denote tokens in the Grammar/Tokens file
# * Rule names starting with "invalid_" are used for specialized syntax errors
# - These rules are NOT used in the first pass of the parser.
# - Only if the first pass fails to parse, a second pass including the invalid
# rules will be executed.
# - If the parser fails in the second phase with a generic syntax error, the
# location of the generic failure of the first pass will be used (this avoids
# reporting incorrect locations due to the invalid rules).
# - The order of the alternatives involving invalid rules matter
# (like any rule in PEG).
#
# Grammar Syntax (see PEP 617 for more information):
#
# rule_name: expression
# Optionally, a type can be included right after the rule name, which
# specifies the return type of the C or Python function corresponding to the
# rule:
# rule_name[return_type]: expression
# If the return type is omitted, then a void * is returned in C and an Any in
# Python.
# e1 e2
# Match e1, then match e2.
# e1 | e2
# Match e1 or e2.
# The first alternative can also appear on the line after the rule name for
# formatting purposes. In that case, a | must be used before the first
# alternative, like so:
# rule_name[return_type]:
(continuesonnextpage)
143

### 第152页

(continuedfrompreviouspage)
# | first_alt
# | second_alt
# ( e )
# Match e (allows also to use other operators in the group like '(e)*')
# [ e ] or e?
# Optionally match e.
# e*
# Match zero or more occurrences of e.
# e+
# Match one or more occurrences of e.
# s.e+
# Match one or more occurrences of e, separated by s. The generated parse tree
# does not include the separator. This is otherwise identical to (e (s e)*).
# &e
# Succeed if e can be parsed, without consuming any input.
# !e
# Fail if e can be parsed, without consuming any input.
# ~
# Commit to the current alternative, even if it fails to parse.
# &&e
# Eager parse e. The parser will not backtrack and will immediately
# fail with SyntaxError if e cannot be parsed.
#
# STARTING RULES
# ==============
file: [statements] ENDMARKER
interactive: statement_newline
eval: expressions NEWLINE* ENDMARKER
func_type: '(' [type_expressions] ')' '->' expression NEWLINE* ENDMARKER
# GENERAL STATEMENTS
# ==================
statements: statement+
statement:
| compound_stmt
| simple_stmts
single_compound_stmt:
| compound_stmt
statement_newline:
| single_compound_stmt NEWLINE
| simple_stmts
| NEWLINE
| ENDMARKER
simple_stmts:
| simple_stmt !';' NEWLINE # Not needed, there for speedup
| ';'.simple_stmt+ [';'] NEWLINE
# NOTE: assignment MUST precede expression, else parsing a simple assignment
# will throw a SyntaxError.
(continuesonnextpage)
144 Chapter10. FullGrammarspecification

### 第153页

(continuedfrompreviouspage)
simple_stmt:
| assignment
| type_alias
| star_expressions
| return_stmt
| import_stmt
| raise_stmt
| pass_stmt
| del_stmt
| yield_stmt
| assert_stmt
| break_stmt
| continue_stmt
| global_stmt
| nonlocal_stmt
compound_stmt:
| function_def
| if_stmt
| class_def
| with_stmt
| for_stmt
| try_stmt
| while_stmt
| match_stmt
# SIMPLE STATEMENTS
# =================
# NOTE: annotated_rhs may start with 'yield'; yield_expr must start with 'yield'
assignment:
| NAME ':' expression ['=' annotated_rhs ]
| ('(' single_target ')'
| single_subscript_attribute_target) ':' expression ['=' annotated_rhs ]
| (star_targets '=' )+ annotated_rhs !'=' [TYPE_COMMENT]
| single_target augassign ~ annotated_rhs
annotated_rhs: yield_expr | star_expressions
augassign:
| '+='
| '-='
| '*='
| '@='
| '/='
| '%='
| '&='
| '|='
| '^='
| '<<='
| '>>='
| '**='
| '//='
return_stmt:
| 'return' [star_expressions]
(continuesonnextpage)
145

### 第154页

(continuedfrompreviouspage)
raise_stmt:
| 'raise' expression ['from' expression ]
| 'raise'
pass_stmt:
| 'pass'
break_stmt:
| 'break'
continue_stmt:
| 'continue'
global_stmt: 'global' ','.NAME+
nonlocal_stmt: 'nonlocal' ','.NAME+
del_stmt:
| 'del' del_targets &(';' | NEWLINE)
yield_stmt: yield_expr
assert_stmt: 'assert' expression [',' expression ]
import_stmt:
| import_name
| import_from
# Import statements
# -----------------
import_name: 'import' dotted_as_names
# note below: the ('.' | '...') is necessary because '...' is tokenized as ELLIPSIS
import_from:
| 'from' ('.' | '...')* dotted_name 'import' import_from_targets
| 'from' ('.' | '...')+ 'import' import_from_targets
import_from_targets:
| '(' import_from_as_names [','] ')'
| import_from_as_names !','
| '*'
import_from_as_names:
| ','.import_from_as_name+
import_from_as_name:
| NAME ['as' NAME ]
dotted_as_names:
| ','.dotted_as_name+
dotted_as_name:
| dotted_name ['as' NAME ]
dotted_name:
| dotted_name '.' NAME
| NAME
# COMPOUND STATEMENTS
(continuesonnextpage)
146 Chapter10. FullGrammarspecification

### 第155页

(continuedfrompreviouspage)
# ===================
# Common elements
# ---------------
block:
| NEWLINE INDENT statements DEDENT
| simple_stmts
decorators: ('@' named_expression NEWLINE )+
# Class definitions
# -----------------
class_def:
| decorators class_def_raw
| class_def_raw
class_def_raw:
| 'class' NAME [type_params] ['(' [arguments] ')' ] ':' block
# Function definitions
# --------------------
function_def:
| decorators function_def_raw
| function_def_raw
function_def_raw:
| 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':' [func_type_
,→comment] block
| 'async' 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':'␣
,→[func_type_comment] block
# Function parameters
# -------------------
params:
| parameters
parameters:
| slash_no_default param_no_default* param_with_default* [star_etc]
| slash_with_default param_with_default* [star_etc]
| param_no_default+ param_with_default* [star_etc]
| param_with_default+ [star_etc]
| star_etc
# Some duplication here because we can't write (',' | &')'),
# which is because we don't support empty alternatives (yet).
slash_no_default:
| param_no_default+ '/' ','
| param_no_default+ '/' &')'
slash_with_default:
| param_no_default* param_with_default+ '/' ','
| param_no_default* param_with_default+ '/' &')'
(continuesonnextpage)
147

### 第156页

(continuedfrompreviouspage)
star_etc:
| '*' param_no_default param_maybe_default* [kwds]
| '*' param_no_default_star_annotation param_maybe_default* [kwds]
| '*' ',' param_maybe_default+ [kwds]
| kwds
kwds:
| '**' param_no_default
# One parameter. This *includes* a following comma and type comment.
#
# There are three styles:
# - No default
# - With default
# - Maybe with default
#
# There are two alternative forms of each, to deal with type comments:
# - Ends in a comma followed by an optional type comment
# - No comma, optional type comment, must be followed by close paren
# The latter form is for a final parameter without trailing comma.
#
param_no_default:
| param ',' TYPE_COMMENT?
| param TYPE_COMMENT? &')'
param_no_default_star_annotation:
| param_star_annotation ',' TYPE_COMMENT?
| param_star_annotation TYPE_COMMENT? &')'
param_with_default:
| param default ',' TYPE_COMMENT?
| param default TYPE_COMMENT? &')'
param_maybe_default:
| param default? ',' TYPE_COMMENT?
| param default? TYPE_COMMENT? &')'
param: NAME annotation?
param_star_annotation: NAME star_annotation
annotation: ':' expression
star_annotation: ':' star_expression
default: '=' expression | invalid_default
# If statement
# ------------
if_stmt:
| 'if' named_expression ':' block elif_stmt
| 'if' named_expression ':' block [else_block]
elif_stmt:
| 'elif' named_expression ':' block elif_stmt
| 'elif' named_expression ':' block [else_block]
else_block:
| 'else' ':' block
# While statement
# ---------------
(continuesonnextpage)
148 Chapter10. FullGrammarspecification

### 第157页

(continuedfrompreviouspage)
while_stmt:
| 'while' named_expression ':' block [else_block]
# For statement
# -------------
for_stmt:
| 'for' star_targets 'in' ~ star_expressions ':' [TYPE_COMMENT] block [else_
,→block]
| 'async' 'for' star_targets 'in' ~ star_expressions ':' [TYPE_COMMENT] block␣
,→[else_block]
# With statement
# --------------
with_stmt:
| 'with' '(' ','.with_item+ ','? ')' ':' [TYPE_COMMENT] block
| 'with' ','.with_item+ ':' [TYPE_COMMENT] block
| 'async' 'with' '(' ','.with_item+ ','? ')' ':' block
| 'async' 'with' ','.with_item+ ':' [TYPE_COMMENT] block
with_item:
| expression 'as' star_target &(',' | ')' | ':')
| expression
# Try statement
# -------------
try_stmt:
| 'try' ':' block finally_block
| 'try' ':' block except_block+ [else_block] [finally_block]
| 'try' ':' block except_star_block+ [else_block] [finally_block]
# Except statement
# ----------------
except_block:
| 'except' expression ':' block
| 'except' expression 'as' NAME ':' block
| 'except' expressions ':' block
| 'except' ':' block
except_star_block:
| 'except' '*' expression ':' block
| 'except' '*' expression 'as' NAME ':' block
| 'except' '*' expressions ':' block
finally_block:
| 'finally' ':' block
# Match statement
# ---------------
match_stmt:
| "match" subject_expr ':' NEWLINE INDENT case_block+ DEDENT
subject_expr:
(continuesonnextpage)
149

### 第158页

(continuedfrompreviouspage)
| star_named_expression ',' star_named_expressions?
| named_expression
case_block:
| "case" patterns guard? ':' block
guard: 'if' named_expression
patterns:
| open_sequence_pattern
| pattern
pattern:
| as_pattern
| or_pattern
as_pattern:
| or_pattern 'as' pattern_capture_target
or_pattern:
| '|'.closed_pattern+
closed_pattern:
| literal_pattern
| capture_pattern
| wildcard_pattern
| value_pattern
| group_pattern
| sequence_pattern
| mapping_pattern
| class_pattern
# Literal patterns are used for equality and identity constraints
literal_pattern:
| signed_number !('+' | '-')
| complex_number
| strings
| 'None'
| 'True'
| 'False'
# Literal expressions are used to restrict permitted mapping pattern keys
literal_expr:
| signed_number !('+' | '-')
| complex_number
| strings
| 'None'
| 'True'
| 'False'
complex_number:
| signed_real_number '+' imaginary_number
| signed_real_number '-' imaginary_number
signed_number:
| NUMBER
(continuesonnextpage)
150 Chapter10. FullGrammarspecification

### 第159页

(continuedfrompreviouspage)
| '-' NUMBER
signed_real_number:
| real_number
| '-' real_number
real_number:
| NUMBER
imaginary_number:
| NUMBER
capture_pattern:
| pattern_capture_target
pattern_capture_target:
| !"_" NAME !('.' | '(' | '=')
wildcard_pattern:
| "_"
value_pattern:
| attr !('.' | '(' | '=')
attr:
| name_or_attr '.' NAME
name_or_attr:
| attr
| NAME
group_pattern:
| '(' pattern ')'
sequence_pattern:
| '[' maybe_sequence_pattern? ']'
| '(' open_sequence_pattern? ')'
open_sequence_pattern:
| maybe_star_pattern ',' maybe_sequence_pattern?
maybe_sequence_pattern:
| ','.maybe_star_pattern+ ','?
maybe_star_pattern:
| star_pattern
| pattern
star_pattern:
| '*' pattern_capture_target
| '*' wildcard_pattern
mapping_pattern:
| '{' '}'
| '{' double_star_pattern ','? '}'
| '{' items_pattern ',' double_star_pattern ','? '}'
(continuesonnextpage)
151

### 第160页

(continuedfrompreviouspage)
| '{' items_pattern ','? '}'
items_pattern:
| ','.key_value_pattern+
key_value_pattern:
| (literal_expr | attr) ':' pattern
double_star_pattern:
| '**' pattern_capture_target
class_pattern:
| name_or_attr '(' ')'
| name_or_attr '(' positional_patterns ','? ')'
| name_or_attr '(' keyword_patterns ','? ')'
| name_or_attr '(' positional_patterns ',' keyword_patterns ','? ')'
positional_patterns:
| ','.pattern+
keyword_patterns:
| ','.keyword_pattern+
keyword_pattern:
| NAME '=' pattern
# Type statement
# ---------------
type_alias:
| "type" NAME [type_params] '=' expression
# Type parameter declaration
# --------------------------
type_params:
| '[' type_param_seq ']'
type_param_seq: ','.type_param+ [',']
type_param:
| NAME [type_param_bound] [type_param_default]
| '*' NAME [type_param_starred_default]
| '**' NAME [type_param_default]
type_param_bound: ':' expression
type_param_default: '=' expression
type_param_starred_default: '=' star_expression
# EXPRESSIONS
# -----------
expressions:
| expression (',' expression )+ [',']
| expression ','
| expression
(continuesonnextpage)
152 Chapter10. FullGrammarspecification

### 第161页

(continuedfrompreviouspage)
expression:
| disjunction 'if' disjunction 'else' expression
| disjunction
| lambdef
yield_expr:
| 'yield' 'from' expression
| 'yield' [star_expressions]
star_expressions:
| star_expression (',' star_expression )+ [',']
| star_expression ','
| star_expression
star_expression:
| '*' bitwise_or
| expression
star_named_expressions: ','.star_named_expression+ [',']
star_named_expression:
| '*' bitwise_or
| named_expression
assignment_expression:
| NAME ':=' ~ expression
named_expression:
| assignment_expression
| expression !':='
disjunction:
| conjunction ('or' conjunction )+
| conjunction
conjunction:
| inversion ('and' inversion )+
| inversion
inversion:
| 'not' inversion
| comparison
# Comparison operators
# --------------------
comparison:
| bitwise_or compare_op_bitwise_or_pair+
| bitwise_or
compare_op_bitwise_or_pair:
| eq_bitwise_or
| noteq_bitwise_or
| lte_bitwise_or
| lt_bitwise_or
(continuesonnextpage)
153

### 第162页

(continuedfrompreviouspage)
| gte_bitwise_or
| gt_bitwise_or
| notin_bitwise_or
| in_bitwise_or
| isnot_bitwise_or
| is_bitwise_or
eq_bitwise_or: '==' bitwise_or
noteq_bitwise_or:
| ('!=' ) bitwise_or
lte_bitwise_or: '<=' bitwise_or
lt_bitwise_or: '<' bitwise_or
gte_bitwise_or: '>=' bitwise_or
gt_bitwise_or: '>' bitwise_or
notin_bitwise_or: 'not' 'in' bitwise_or
in_bitwise_or: 'in' bitwise_or
isnot_bitwise_or: 'is' 'not' bitwise_or
is_bitwise_or: 'is' bitwise_or
# Bitwise operators
# -----------------
bitwise_or:
| bitwise_or '|' bitwise_xor
| bitwise_xor
bitwise_xor:
| bitwise_xor '^' bitwise_and
| bitwise_and
bitwise_and:
| bitwise_and '&' shift_expr
| shift_expr
shift_expr:
| shift_expr '<<' sum
| shift_expr '>>' sum
| sum
# Arithmetic operators
# --------------------
sum:
| sum '+' term
| sum '-' term
| term
term:
| term '*' factor
| term '/' factor
| term '//' factor
| term '%' factor
| term '@' factor
| factor
factor:
(continuesonnextpage)
154 Chapter10. FullGrammarspecification

### 第163页

(continuedfrompreviouspage)
| '+' factor
| '-' factor
| '~' factor
| power
power:
| await_primary '**' factor
| await_primary
# Primary elements
# ----------------
# Primary elements are things like "obj.something.something", "obj[something]",
,→"obj(something)", "obj" ...
await_primary:
| 'await' primary
| primary
primary:
| primary '.' NAME
| primary genexp
| primary '(' [arguments] ')'
| primary '[' slices ']'
| atom
slices:
| slice !','
| ','.(slice | starred_expression)+ [',']
slice:
| [expression] ':' [expression] [':' [expression] ]
| named_expression
atom:
| NAME
| 'True'
| 'False'
| 'None'
| strings
| NUMBER
| (tuple | group | genexp)
| (list | listcomp)
| (dict | set | dictcomp | setcomp)
| '...'
group:
| '(' (yield_expr | named_expression) ')'
# Lambda functions
# ----------------
lambdef:
| 'lambda' [lambda_params] ':' expression
lambda_params:
(continuesonnextpage)
155

### 第164页

(continuedfrompreviouspage)
| lambda_parameters
# lambda_parameters etc. duplicates parameters but without annotations
# or type comments, and if there's no comma after a parameter, we expect
# a colon, not a close parenthesis. (For more, see parameters above.)
#
lambda_parameters:
| lambda_slash_no_default lambda_param_no_default* lambda_param_with_default*␣
,→[lambda_star_etc]
| lambda_slash_with_default lambda_param_with_default* [lambda_star_etc]
| lambda_param_no_default+ lambda_param_with_default* [lambda_star_etc]
| lambda_param_with_default+ [lambda_star_etc]
| lambda_star_etc
lambda_slash_no_default:
| lambda_param_no_default+ '/' ','
| lambda_param_no_default+ '/' &':'
lambda_slash_with_default:
| lambda_param_no_default* lambda_param_with_default+ '/' ','
| lambda_param_no_default* lambda_param_with_default+ '/' &':'
lambda_star_etc:
| '*' lambda_param_no_default lambda_param_maybe_default* [lambda_kwds]
| '*' ',' lambda_param_maybe_default+ [lambda_kwds]
| lambda_kwds
lambda_kwds:
| '**' lambda_param_no_default
lambda_param_no_default:
| lambda_param ','
| lambda_param &':'
lambda_param_with_default:
| lambda_param default ','
| lambda_param default &':'
lambda_param_maybe_default:
| lambda_param default? ','
| lambda_param default? &':'
lambda_param: NAME
# LITERALS
# ========
fstring_middle:
| fstring_replacement_field
| FSTRING_MIDDLE
fstring_replacement_field:
| '{' annotated_rhs '='? [fstring_conversion] [fstring_full_format_spec] '}'
fstring_conversion:
| "!" NAME
fstring_full_format_spec:
| ':' fstring_format_spec*
fstring_format_spec:
| FSTRING_MIDDLE
| fstring_replacement_field
(continuesonnextpage)
156 Chapter10. FullGrammarspecification

### 第165页

(continuedfrompreviouspage)
fstring:
| FSTRING_START fstring_middle* FSTRING_END
tstring_format_spec_replacement_field:
| '{' annotated_rhs '='? [fstring_conversion] [tstring_full_format_spec] '}'
tstring_format_spec:
| TSTRING_MIDDLE
| tstring_format_spec_replacement_field
tstring_full_format_spec:
| ':' tstring_format_spec*
tstring_replacement_field:
| '{' annotated_rhs '='? [fstring_conversion] [tstring_full_format_spec] '}'
tstring_middle:
| tstring_replacement_field
| TSTRING_MIDDLE
tstring:
| TSTRING_START tstring_middle* TSTRING_END
string: STRING
strings:
| (fstring|string)+
| tstring+
list:
| '[' [star_named_expressions] ']'
tuple:
| '(' [star_named_expression ',' [star_named_expressions] ] ')'
set: '{' star_named_expressions '}'
# Dicts
# -----
dict:
| '{' [double_starred_kvpairs] '}'
double_starred_kvpairs: ','.double_starred_kvpair+ [',']
double_starred_kvpair:
| '**' bitwise_or
| kvpair
kvpair: expression ':' expression
# Comprehensions & Generators
# ---------------------------
for_if_clauses:
| for_if_clause+
for_if_clause:
| 'async' 'for' star_targets 'in' ~ disjunction ('if' disjunction )*
| 'for' star_targets 'in' ~ disjunction ('if' disjunction )*
listcomp:
(continuesonnextpage)
157

### 第166页

(continuedfrompreviouspage)
| '[' named_expression for_if_clauses ']'
setcomp:
| '{' named_expression for_if_clauses '}'
genexp:
| '(' ( assignment_expression | expression !':=') for_if_clauses ')'
dictcomp:
| '{' kvpair for_if_clauses '}'
# FUNCTION CALL ARGUMENTS
# =======================
arguments:
| args [','] &')'
args:
| ','.(starred_expression | ( assignment_expression | expression !':=') !'=')+␣
,→[',' kwargs ]
| kwargs
kwargs:
| ','.kwarg_or_starred+ ',' ','.kwarg_or_double_starred+
| ','.kwarg_or_starred+
| ','.kwarg_or_double_starred+
starred_expression:
| '*' expression
kwarg_or_starred:
| NAME '=' expression
| starred_expression
kwarg_or_double_starred:
| NAME '=' expression
| '**' expression
# ASSIGNMENT TARGETS
# ==================
# Generic targets
# ---------------
# NOTE: star_targets may contain *bitwise_or, targets may not.
star_targets:
| star_target !','
| star_target (',' star_target )* [',']
star_targets_list_seq: ','.star_target+ [',']
star_targets_tuple_seq:
| star_target (',' star_target )+ [',']
| star_target ','
star_target:
(continuesonnextpage)
158 Chapter10. FullGrammarspecification

### 第167页

(continuedfrompreviouspage)
| '*' (!'*' star_target)
| target_with_star_atom
target_with_star_atom:
| t_primary '.' NAME !t_lookahead
| t_primary '[' slices ']' !t_lookahead
| star_atom
star_atom:
| NAME
| '(' target_with_star_atom ')'
| '(' [star_targets_tuple_seq] ')'
| '[' [star_targets_list_seq] ']'
single_target:
| single_subscript_attribute_target
| NAME
| '(' single_target ')'
single_subscript_attribute_target:
| t_primary '.' NAME !t_lookahead
| t_primary '[' slices ']' !t_lookahead
t_primary:
| t_primary '.' NAME &t_lookahead
| t_primary '[' slices ']' &t_lookahead
| t_primary genexp &t_lookahead
| t_primary '(' [arguments] ')' &t_lookahead
| atom &t_lookahead
t_lookahead: '(' | '[' | '.'
# Targets for del statements
# --------------------------
del_targets: ','.del_target+ [',']
del_target:
| t_primary '.' NAME !t_lookahead
| t_primary '[' slices ']' !t_lookahead
| del_t_atom
del_t_atom:
| NAME
| '(' del_target ')'
| '(' [del_targets] ')'
| '[' [del_targets] ']'
# TYPING ELEMENTS
# ---------------
# type_expressions allow */** but ignore them
type_expressions:
| ','.expression+ ',' '*' expression ',' '**' expression
| ','.expression+ ',' '*' expression
| ','.expression+ ',' '**' expression
(continuesonnextpage)
159

### 第168页

(continuedfrompreviouspage)
| '*' expression ',' '**' expression
| '*' expression
| '**' expression
| ','.expression+
func_type_comment:
| NEWLINE TYPE_COMMENT &(NEWLINE INDENT) # Must be followed by indented block
| TYPE_COMMENT
# ========================= END OF THE GRAMMAR ===========================
# ========================= START OF INVALID RULES =======================
160 Chapter10. FullGrammarspecification

### 第169页

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
161

### 第170页

and5arebothpositionalargumentsinthefollowingcalls:
complex(3, 5)
complex(*(3, 5))
Arguments are assigned to the named local variables in a function body. See the Calls section for the rules
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
awaitableobject. async for resolvestheawaitablesreturnedbyanasynchronousiterator’s__anext__()
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
162 AppendixA. Glossary

### 第171页

ItispossibletogiveanobjectanattributewhosenameisnotanidentifierasdefinedbyNames(identifiersand
keywords),forexampleusingsetattr(),iftheobjectallowsit. Suchanattributewillnotbeaccessibleusing
adottedexpression,andwouldinsteadneedtoberetrievedwithgetattr().
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
163

### 第172页

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
mentedwiththeasync def statement. SeealsoPEP492.
coroutinefunction
Afunctionwhichreturnsacoroutineobject. Acoroutinefunctionmaybedefinedwiththeasync defstate-
164 AppendixA. Glossary

### 第173页

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
For more information about descriptors’ methods, see Implementing Descriptors or the Descriptor How To
Guide.
dictionary
Anassociativearray,wherearbitrarykeysaremappedtovalues. Thekeyscanbeanyobjectwith__hash__()
and__eq__()methods. CalledahashinPerl.
dictionarycomprehension
A compact way to process all or part of the elements in an iterable and return a dictionary with the re-
sults. results = {n: n ** 2 for n in range(10)}generatesadictionarycontainingkeynmapped
tovaluen ** 2. SeeDisplaysforlists,setsanddictionaries.
dictionaryview
Theobjectsreturnedfromdict.keys(),dict.values(),anddict.items()arecalleddictionaryviews.
Theyprovideadynamicviewonthedictionary’sentries,whichmeansthatwhenthedictionarychanges,the
view reflects these changes. To force the dictionary view to become a full list use list(dictview). See
dict-views.
docstring
Astringliteralwhichappearsasthefirstexpressioninaclass,functionormodule. Whileignoredwhenthe
165

### 第174页

suiteisexecuted,itisrecognizedbythecompilerandputintothe__doc__attributeoftheenclosingclass,
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
characterizedbythepresenceofmanytry andexceptstatements. ThetechniquecontrastswiththeLBYL
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
166 AppendixA. Glossary

### 第175页

Seealsothelocaleencoding.
finder
Anobjectthattriestofindtheloaderforamodulethatisbeingimported.
Therearetwotypesoffinder: metapathfindersforusewithsys.meta_path,andpathentryfindersforuse
withsys.path_hooks.
SeeFindersandloadersandimportlibformuchmoredetail.
floordivision
Mathematicaldivisionthatroundsdowntonearestinteger. Thefloordivisionoperatoris//. Forexample,the
expression11 // 4evaluatesto2incontrasttothe2.75returnedbyfloattruedivision. Notethat(-11)
// 4is-3becausethatis-2.75roundeddownward. SeePEP238.
freethreading
AthreadingmodelwheremultiplethreadscanrunPythonbytecodesimultaneouslywithinthesameinterpreter.
ThisisincontrasttotheglobalinterpreterlockwhichallowsonlyonethreadtoexecutePythonbytecodeata
time. SeePEP703.
freevariable
Formally,asdefinedinthelanguageexecutionmodel,afreevariableisanyvariableusedinanamespacewhich
isnotalocalvariableinthatnamespace. Seeclosurevariableforanexample. Pragmatically,duetothenameof
thecodeobject.co_freevarsattribute,thetermisalsosometimesusedasasynonymforclosurevariable.
function
Aseriesofstatementswhichreturnssomevaluetoacaller. Itcanalsobepassedzeroormoreargumentswhich
maybeusedintheexecutionofthebody. Seealsoparameter,method,andtheFunctiondefinitionssection.
functionannotation
Anannotationofafunctionparameterorreturnvalue.
Function annotations are usually used for type hints: for example, this function is expected to take two int
argumentsandisalsoexpectedtohaveanintreturnvalue:
def sum_two_numbers(a: int, b: int) -> int:
return a + b
FunctionannotationsyntaxisexplainedinsectionFunctiondefinitions.
SeevariableannotationandPEP484,whichdescribethisfunctionality. Alsoseeannotations-howtoforbest
practicesonworkingwithannotations.
__future__
Afuturestatement, from __future__ import <feature>, directsthecompilertocompilethecurrent
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
167

### 第176页

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
determineitsvalidity. SeeCachedbytecodeinvalidation.
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
168 AppendixA. Glossary

### 第177页

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
169

### 第178页

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
stylecontrastswiththeEAFPapproachandischaracterizedbythepresenceofmanyif statements.
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
• Findersandloaders
170 AppendixA. Glossary

### 第179页

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
MoreinformationcanbefoundinMetaclasses.
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
SeealsoModulespecs.
MRO
Seemethodresolutionorder.
mutable
Mutableobjectscanchangetheirvaluebutkeeptheirid(). Seealsoimmutable.
171

### 第180页

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
Formoreinformation,seePEP420andNamespacepackages.
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
172 AppendixA. Glossary

### 第181页

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
theinspect.Parameterclass,theFunctiondefinitionssection,andPEP362.
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
173

### 第182页

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
174 AppendixA. Glossary

### 第183页

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
Displaysforlists,setsanddictionaries.
singledispatch
Aformofgenericfunctiondispatchwheretheimplementationischosenbasedonthetypeofasingleargument.
slice
Anobjectusuallycontainingaportionofasequence. Asliceiscreatedusingthesubscriptnotation,[]with
colons between numbers when several are given, such as in variable_name[1:3:5]. The bracket (sub-
script)notationusessliceobjectsinternally.
softdeprecated
AsoftdeprecatedAPIshouldnotbeusedinnewcode,butitissafeforalreadyexistingcodetouseit. The
APIremainsdocumentedandtested,butwillnotbeenhancedfurther.
175

### 第184页

Softdeprecation,unlikenormaldeprecation,doesnotplanonremovingtheAPIandwillnotemitwarnings.
SeePEP387: SoftDeprecation.
specialmethod
AmethodthatiscalledimplicitlybyPythontoexecuteacertainoperationonatype,suchasaddition. Such
methodshavenamesstartingandendingwithdoubleunderscores. SpecialmethodsaredocumentedinSpecial
methodnames.
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
176 AppendixA. Glossary

### 第185页

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
177

### 第186页

Variableannotationsareusuallyusedfortypehints: forexamplethisvariableisexpectedtotakeintvalues:
count: int = 0
VariableannotationsyntaxisexplainedinsectionAnnotatedassignmentstatements.
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
178 AppendixA. Glossary

### 第187页

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
179

### 第188页

180 AppendixB. Aboutthisdocumentation

### 第189页

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
181

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

### 第190页

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
182 AppendixC. HistoryandLicense

### 第191页

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
C.2. TermsandconditionsforaccessingorotherwiseusingPython 183

### 第192页

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
184 AppendixC. HistoryandLicense

### 第193页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 185

### 第194页

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
186 AppendixC. HistoryandLicense

### 第195页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 187

### 第196页

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
188 AppendixC. HistoryandLicense

### 第197页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 189

### 第198页

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
190 AppendixC. HistoryandLicense

### 第199页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 191

### 第200页

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
192 AppendixC. HistoryandLicense

### 第201页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 193

### 第202页

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
194 AppendixC. HistoryandLicense

### 第203页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 195

### 第204页

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
196 AppendixC. HistoryandLicense

### 第205页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 197

### 第206页

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
198 AppendixC. HistoryandLicense

### 第207页

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
C.3. LicensesandAcknowledgementsforIncorporatedSoftware 199

### 第208页

200 AppendixC. HistoryandLicense

### 第209页

APPENDIX
D
COPYRIGHT
Pythonandthisdocumentationis:
Copyright©2001PythonSoftwareFoundation. Allrightsreserved.
Copyright©2000BeOpen.com. Allrightsreserved.
Copyright©1995-2000CorporationforNationalResearchInitiatives. Allrightsreserved.
Copyright©1991-1995StichtingMathematischCentrum. Allrightsreserved.
SeeHistoryandLicenseforcompletelicenseandpermissionsinformation.
201

### 第210页

202 AppendixD. Copyright

### 第211页

INDEX
Non-alphabetical
in expression lists,103
...,161 in function calls,95
ellipsis literal,24,161
operator,97
**
'''
string literal,12 function definition,132
{}(curlybrackets) in dictionary displays,88
dictionary expression,88 in function calls,96
in formatted string literal,16
operator,97
set expression,88 **=
. (dot) augmented assignment,107
attribute reference,93 *=
in numeric literal,19 augmented assignment,107
! (exclamation)
+(plus)
in formatted string literal,16 binary operator,98
-(minus) unary operator,97
binary operator,98 +=
unary operator,97 augmented assignment,107
'(singlequote)
,(comma),87
string literal,12 argument list,95
! patterns,125 expression list,88,103,108,133
"(doublequote) identifier list,114,115
string literal,12 import statement,112
in dictionary displays,88
"""
string literal,12 in target list,106
#(hash) parameter list,131
comment,7
slicing,94
source encoding declaration,7 with statement,122
%(percent)
/(slash)
operator,98 function definition,132
operator,98
%=
augmented assignment,107 //
&(ampersand)
operator,98
operator,99 //=
augmented assignment,107
&=
augmented assignment,107 /=
()(parentheses) augmented assignment,107
call,95 0b
class definition,133 integer literal,18
function definition,131 0o
generator expression,89 integer literal,18
in assignment target list,106 0x
tuple display,87 integer literal,18
*(asterisk) : (colon)
function definition,132 annotated variable,108
import statement,113 compound statement,118,119,122,123,131,
133
in assignment target list,106
203

### 第212页

function annotations,132 escape sequence,13
in dictionary expressions,88 \n
in formatted string literal,16 escape sequence,13
lambda expression,103 \r
slicing,94 escape sequence,13
:=(colonequals),102 \t
;(semicolon),117 escape sequence,13
<(less) \U
operator,99 escape sequence,13
<< \u
operator,98 escape sequence,13
<<= \v
augmented assignment,107 escape sequence,13
<= \x
operator,99 escape sequence,13
!= ^(caret)
operator,99 operator,99
-= ^=
augmented assignment,107 augmented assignment,107
=(equals) _(underscore)
assignment statement,105 in numeric literal,18,19
class definition,50 _, identifiers,11
for help in debugging using string __, identifiers,11
literals,16 __abs__()(objectmethod),59
function definition,132 __add__()(objectmethod),57
in function calls,95 __aenter__()(objectmethod),64
== __aexit__()(objectmethod),64
operator,99 __aiter__()(objectmethod),64
-> __all__(moduleattribute),113
function annotations,132 __all__(optionalmoduleattribute),113
>(greater) __and__()(objectmethod),57
operator,99 __anext__()(agenmethod),93
>= __anext__()(objectmethod),64
operator,99 __annotate__(classattribute),34
>> __annotate__(functionattribute),28
operator,98 __annotate__(moduleattribute),30,32
>>= __annotate__()(objectmethod),61
augmented assignment,107 __annotate__()(typemethod),34
>>>,161 __annotations__(classattribute),34
@(at) __annotations__(functionattribute),28
class definition,133 __annotations__(moduleattribute),30,32
function definition,131 __annotations__(objectattribute),61
operator,97 __annotations__(typeattribute),34
[](squarebrackets) __await__()(objectmethod),63
in assignment target list,106 __bases__(classattribute),34
list expression,88 __bases__(typeattribute),34
subscription,94 __bool__()(objectmethod),45,56
\(backslash) __buffer__()(objectmethod),60
escape sequence,13 __bytes__()(objectmethod),43
\\ __cached__(moduleattribute),30,32
escape sequence,13 __call__()(objectmethod),55,96
\a __cause__(exceptionattribute),110
escape sequence,13 __ceil__()(objectmethod),59
\b __class__(instanceattribute),35
escape sequence,13 __class__(methodcell),52
\f __class__(moduleattribute),46,47
escape sequence,13 __class__(objectattribute),35
\N __class_getitem__()(objectclassmethod),53
204 Index

### 第213页

__classcell__(classnamespaceentry),52 __index__()(objectmethod),59
__closure__(functionattribute),27 __init__()(objectmethod),42
__code__(functionattribute),28 __init_subclass__()(objectclassmethod),49
__complex__()(objectmethod),59 __instancecheck__()(typemethod),53
__contains__()(objectmethod),57 __int__()(objectmethod),59
__context__(exceptionattribute),110 __invert__()(objectmethod),59
__debug__,109 __ior__()(objectmethod),58
__defaults__(functionattribute),28 __ipow__()(objectmethod),58
__del__()(objectmethod),42 __irshift__()(objectmethod),58
__delattr__()(objectmethod),46 __isub__()(objectmethod),58
__delete__()(objectmethod),48 __iter__()(objectmethod),57
__delitem__()(objectmethod),56 __itruediv__()(objectmethod),58
__dict__(classattribute),34 __ixor__()(objectmethod),58
__dict__(functionattribute),28 __kwdefaults__(functionattribute),28
__dict__(instanceattribute),35 __le__()(objectmethod),44
__dict__(moduleattribute),33 __len__()(mappingobjectmethod),45
__dict__(objectattribute),35 __len__()(objectmethod),56
__dict__(typeattribute),34 __length_hint__()(objectmethod),56
__dir__(moduleattribute),46 __loader__(moduleattribute),30,31
__dir__()(modulemethod),46 __lshift__()(objectmethod),57
__dir__()(objectmethod),46 __lt__()(objectmethod),44
__divmod__()(objectmethod),57 __main__
__doc__(classattribute),34 module,68,141
__doc__(functionattribute),28 __matmul__()(objectmethod),57
__doc__(methodattribute),28,29 __missing__()(objectmethod),57
__doc__(moduleattribute),30,32 __mod__()(objectmethod),57
__doc__(typeattribute),34 __module__(classattribute),34
__enter__()(objectmethod),59 __module__(functionattribute),28
__eq__()(objectmethod),44 __module__(methodattribute),28,29
__exit__()(objectmethod),60 __module__(typeattribute),34
__file__(moduleattribute),30,32 __mro__(typeattribute),34
__firstlineno__(classattribute),34 __mro_entries__()(objectmethod),51
__firstlineno__(typeattribute),34 __mul__()(objectmethod),57
__float__()(objectmethod),59 __name__(classattribute),34
__floor__()(objectmethod),59 __name__(functionattribute),28
__floordiv__()(objectmethod),57 __name__(methodattribute),28,29
__format__()(objectmethod),43 __name__(moduleattribute),30,31
__func__(methodattribute),28,29 __name__(typeattribute),34
__future__,167 __ne__()(objectmethod),44
future statement,113 __neg__()(objectmethod),59
__ge__()(objectmethod),44 __new__()(objectmethod),42
__get__()(objectmethod),47 __next__()(generatormethod),91
__getattr__(moduleattribute),46 __objclass__(objectattribute),48
__getattr__()(modulemethod),46 __or__()(objectmethod),57
__getattr__()(objectmethod),45 __package__(moduleattribute),30,31
__getattribute__()(objectmethod),46 __path__(moduleattribute),30,32
__getitem__()(mappingobjectmethod),41 __pos__()(objectmethod),59
__getitem__()(objectmethod),56 __pow__()(objectmethod),57
__globals__(functionattribute),27 __prepare__(metaclassmethod),52
__gt__()(objectmethod),44 __qualname__(functionattribute),28
__hash__()(objectmethod),44 __qualname__(typeattribute),34
__iadd__()(objectmethod),58 __radd__()(objectmethod),58
__iand__()(objectmethod),58 __rand__()(objectmethod),58
__ifloordiv__()(objectmethod),58 __rdivmod__()(objectmethod),58
__ilshift__()(objectmethod),58 __release_buffer__()(objectmethod),60
__imatmul__()(objectmethod),58 __repr__()(objectmethod),43
__imod__()(objectmethod),58 __reversed__()(objectmethod),57
__imul__()(objectmethod),58 __rfloordiv__()(objectmethod),58
Index 205

### 第214页

__rlshift__()(objectmethod),58 function,27
__rmatmul__()(objectmethod),58 function definition,132
__rmod__()(objectmethod),58 arithmetic
__rmul__()(objectmethod),58 conversion,85
__ror__()(objectmethod),58 operation,binary,97
__round__()(objectmethod),59 operation,unary,97
__rpow__()(objectmethod),58 array
__rrshift__()(objectmethod),58 module,26
__rshift__()(objectmethod),57 as
__rsub__()(objectmethod),58 except clause,119
__rtruediv__()(objectmethod),58 import statement,112
__rxor__()(objectmethod),58 keyword,112,119,122,123
__self__(methodattribute),28,29 match statement,123
__set__()(objectmethod),47 with statement,122
__set_name__()(objectmethod),50 AS pattern, OR pattern, capture pattern,
__setattr__()(objectmethod),46 wildcard pattern,125
__setitem__()(objectmethod),56 ASCII,12
__slots__,175 asend()(agenmethod),93
__spec__(moduleattribute),30,31 assert
__static_attributes__(classattribute),34 statement,108
__static_attributes__(typeattribute),34 AssertionError
__str__()(objectmethod),43 exception,109
__sub__()(objectmethod),57 assertions
__subclasscheck__()(typemethod),53 debugging,108
__subclasses__()(typemethod),35 assignment
__traceback__(exceptionattribute),110 annotated,108
__truediv__()(objectmethod),57 attribute,105,106
__trunc__()(objectmethod),59 augmented,107
__type_params__(classattribute),34 classattribute,33
__type_params__(functionattribute),28 class instanceattribute,35
__type_params__(typeattribute),34 expression,102
__xor__()(objectmethod),57 slicing,107
|(verticalbar) statement,26,105
operator,99 subscription,106
|= targetlist,106
augmented assignment,107 assignment expression,102
~(tilde) async
operator,97 keyword,134
async def
A
statement,134
abs async for
built-in function,59 in comprehensions,87
abstract base class,161 statement,134
aclose()(agenmethod),93 async with
addition,98 statement,135
and asynchronous context manager,162
bitwise,99 asynchronous generator,162
operator,102 asynchronous iterator,29
annotate function,161 function,29
annotated asynchronous generator iterator,162
assignment,108 asynchronous iterable,162
annotation,161 asynchronous iterator,162
annotations asynchronous-generator
function,132 object,92
anonymous athrow()(agenmethod),93
function,103 atom,85
argument,161 attached thread state,162
call semantics,95 attribute,24,162
206 Index

### 第215页

assignment,105,106 divmod,57,58
assignment,class,33 eval,114,142
assignment,class instance,35 exec,114
class,33 float,59
class instance,35 hash,44
deletion,109 id,23
genericspecial,24 int,59
reference,93 len,2527,56
special,24 object,30,96
AttributeError open,35
exception,93 ord,26
augmented pow,57,58
assignment,107 print,43
await range,118
in comprehensions,88 repr,105
keyword,96,134 round,59
awaitable,163 slice,41
type,23,50
B
built-in method
b' call,96
bytes literal,15 object,30,96
b" builtins
bytes literal,15 module,141
backslash character,8 byte,26
BDFL,163 bytearray,26
binary bytecode,36,163
arithmeticoperation,97 bytes,26
bitwiseoperation,99 built-in function,43
binary file,163 bytes literal,12
binary literal,18 bytes-like object,163
binding
C
globalname,114
name,67,105,112,131,133 C,13
bitwise language,24,25,30,99
and,99 call,95
operation,binary,99 built-in function,96
operation,unary,97 built-in method,96
or,99 class instance,96
xor,99 class object,33,96
blank line,8 function,27,96
block,67 instance,55,96
code,67 method,96
BNF,4,85 procedure,105
Boolean user-definedfunction,96
object,25 callable,163
operation,102 object,27,95
borrowed reference,163 callback,163
break case
statement,112,118,121 keyword,123
built-in match,123
method,30 case block,125
built-in function C-contiguous,164
abs,59 chaining
bytes,43 comparisons,99
call,96 exception,110
chr,26 character,26,94
compile,114 chr
complex,59 built-in function,26
Index 207

### 第216页

class,163 co_varnames(codeobjectattribute),37
attribute,33 code
attributeassignment,33 block,67
body,52 code object,36
constructor,42 collections
definition,109,133 module,26
instance,35 comma,87
name,133 trailing,103
object,33,96,133 command line,141
statement,133 comment,7
class instance comparison,99
attribute,35 comparisons,44
attributeassignment,35 chaining,99
call,96 compile
object,33,35,96 built-in function,114
class object complex
call,33,96 built-in function,59
class variable,163 number,25
clause,117 object,25
clear()(framemethod),40 complex literal,18
close()(coroutinemethod),64 complex number,164
close()(generatormethod),91 compound
closure variable,164 statement,117
co_argcount(codeobjectattribute),36 comprehensions,87
co_argcount(codeobjectattribute),37 dictionary,88
co_cellvars(codeobjectattribute),36 list,88
co_cellvars(codeobjectattribute),37 set,88
co_code(codeobjectattribute),36 Conditional
co_code(codeobjectattribute),37 expression,102
co_consts(codeobjectattribute),36 conditional
co_consts(codeobjectattribute),37 expression,102
co_filename(codeobjectattribute),36 constant,12
co_filename(codeobjectattribute),37 constructor
co_firstlineno(codeobjectattribute),36 class,42
co_firstlineno(codeobjectattribute),37 container,23,33
co_flags(codeobjectattribute),36 context,164
co_flags(codeobjectattribute),37 context management protocol,164
co_freevars(codeobjectattribute),36 context manager,59,164
co_freevars(codeobjectattribute),37 context variable,164
co_kwonlyargcount(codeobjectattribute),36 contiguous,164
co_kwonlyargcount(codeobjectattribute),37 continue
co_lines()(codeobjectmethod),38 statement,112,118,121
co_lnotab(codeobjectattribute),36 conversion
co_lnotab(codeobjectattribute),37 arithmetic,85
co_name(codeobjectattribute),36 string,43,105
co_name(codeobjectattribute),37 coroutine,62,90,164
co_names(codeobjectattribute),36 function,29
co_names(codeobjectattribute),37 coroutine function,164
co_nlocals(codeobjectattribute),36 CPython,165
co_nlocals(codeobjectattribute),37 current context,165
co_positions()(codeobjectmethod),38 cyclic isolate,165
co_posonlyargcount(codeobjectattribute),36
D
co_posonlyargcount(codeobjectattribute),37
co_qualname(codeobjectattribute),36 dangling
co_qualname(codeobjectattribute),37 else,117
co_stacksize(codeobjectattribute),36 data,23
co_stacksize(codeobjectattribute),37 type,24
co_varnames(codeobjectattribute),36 type,immutable,86
208 Index

### 第217页

dbm.gnu encoding declarations(sourcefile),7
module,27 environment,68
dbm.ndbm environment variable
module,27 PYTHON_GIL,168
debugging PYTHONHASHSEED,45
assertions,108 PYTHONNODEBUGRANGES,38
decimal literal,18 PYTHONPATH,80
decorator,165 error handling,70
DEDENT token,9,117 errors,70
def escape sequence,13
statement,131 eval
default built-in function,114,142
parametervalue,132 evaluate function,166
definition evaluation
class,109,133 order,103
function,109,131 exc_info(inmodulesys),40
del except
statement,42,109 keyword,119
deletion except_star
attribute,109 keyword,120
target,109 exception,70,110
targetlist,109 AssertionError,109
delimiters,21 AttributeError,93
descriptor,165 chaining,110
destructor,42,106 GeneratorExit,91,93
dictionary,165 handler,40
comprehensions,88 ImportError,112
display,88 NameError,85
object,27,33,44,88,94,107 raising,110
dictionary comprehension,165 StopAsyncIteration,93
dictionary view,165 StopIteration,91,110
display TypeError,97
dictionary,88 ValueError,98
list,88 ZeroDivisionError,98
set,88 exception handler,70
division,98 exclusive
divmod or,99
built-in function,57,58 exec
docstring,133,165 built-in function,114
documentation string,38 execution
duck-typing,166 frame,67,133
dunder,166 restricted,70
stack,40
E
execution model,67
e expression,85,166
in numeric literal,19 assignment,102
EAFP,166 Conditional,102
elif conditional,102
keyword,118 generator,89
Ellipsis lambda,103,132
object,24 list,103,105
else statement,105
conditional expression,102 yield,89
dangling,117 extension
keyword,112,118,119,121 module,24
empty extension module,166
list,88
tuple,26,87
Index 209

### 第218页

F
fstring,16
f-string,16
f'
formatted string literal,16
function,167
annotations,132
f"
formatted string literal,16
anonymous,103
f-string,166
argument,27
f-strings,166
call,27,96
f_back(frameattribute),39
call,user-defined,96
f_builtins(frameattribute),39
definition,109,131
f_code(frameattribute),39
generator,89,110
f_generator(frameattribute),39
name,131
f_globals(frameattribute),39
object,27,30,96,131
f_lasti(frameattribute),39
user-defined,27
f_lineno(frameattribute),39,40 function annotation,167
f_locals(frameattribute),39 future
f_trace(frameattribute),39,40
statement,113
f_trace_lines(frameattribute),39,40
G
f_trace_opcodes(frameattribute),39,40
False,25 garbage collection,23,167
file object,166 generator,167
file-like object,166 expression,89
filesystem encoding and error handler,166 function,29,89,110
finalizer,42 iterator,29,110
finally object,38,89,90
keyword,109,112,119,121 generator expression,168
find_spec generator iterator,168
finder,75 GeneratorExit
finder,75,167 exception,91,93
find_spec,75 generic
float specialattribute,24
built-in function,59 generic function,168
floating-point generic type,168
number,25 GIL,168
object,25 global
floating-point literal,18 namebinding,114
floor division,167 namespace,27
for statement,109,114
in comprehensions,87 global interpreter lock,168
statement,112,118 grammar,4
form grouping,8
lambda,103 guard,125
format()(built-infunction)
H
__str__()(objectmethod),43
formatted string literal,16 handle an exception,70
Fortran contiguous,164 handler
frame exception,40
execution,67,133 hash
object,39 built-in function,44
free hash character,7
variable,67 hash-based pyc,168
free threading,167 hashable,89,168
free variable,167 hexadecimal literal,18
from hierarchy
import statement,67,112 type,24
keyword,89,112 hooks
yield from expression,90 import,75
frozenset meta,75
object,27 path,75
210 Index

### 第219页

I
interpreted,169
interpreter,141
id
built-in function,23 interpreter shutdown,169
identifier,10,85
inversion,97
invocation,27
identity
test,101 io
identity of an object,23
module,35
IDLE,169 irrefutable case block,125
is
if
conditional expression,102
operator,101
in comprehensions,87 is not
keyword,123
operator,101
statement,118 item
imaginary literal,18
sequence,94
immortal,169
string,94
immutable,169 item selection,25
datatype,86
iterable,169
object,26,86,89
unpacking,103
immutable object,23
iterator,170
immutable sequence J
object,26
immutable types j
subclassing,42 in numeric literal,20
import Java
hooks,75 language,25
statement,30,112
K
import hooks,75
import machinery,73 key,88
import path,169 key function,170
importer,169 key/value pair,88
ImportError keyword,11
exception,112 as,112,119,122,123
importing,169 async,134
in await,96,134
keyword,118 case,123
operator,101 elif,118
inclusive else,112,118,119,121
or,99 except,119
INDENT token,9 except_star,120
indentation,8 finally,109,112,119,121
index operation,25 from,89,112
indices()(slicemethod),41 if,123
inheritance,133 in,118
input,142 yield,89
instance keyword argument,170
call,55,96
L
class,35
object,33,35,96 lambda,170
int expression,103,132
built-in function,59 form,103
integer,26 language
object,25 C,24,25,30,99
representation,25 Java,25
integer literal,18 last_traceback(inmodulesys),40
interactive,169 LBYL,170
interactive mode,141 leading whitespace,8
internal type,35 len
interpolated string literal,16 built-in function,2527,56
Index 211

### 第220页

lexical analysis,7 builtins,141
lexical analyzer,170 collections,26
lexical definitions,5 dbm.gnu,27
line continuation,8 dbm.ndbm,27
line joining,7,8 extension,24
line structure,7 importing,112
list,170 io,35
assignment,target,106 namespace,30
comprehensions,88 object,30,93
deletiontarget,109 sys,120,141
display,88 module spec,75,171
empty,88 modulo,98
expression,103,105 MRO,171
object,26,88,93,94,107 mro()(typemethod),35
target,106,118 multiplication,97
list comprehension,170 mutable,171
literal,12,86 object,26,105,106
loader,75,170 mutable object,23
locale encoding,171 mutable sequence
logical line,7 object,26
loop
N
statement,112,118
loop control name,10,67,85
target,112 binding,67,105,112,131,133
binding,global,114
M
class,133
magic function,131
method,171 mangling,85
magic method,171 rebinding,105
makefile()(socketmethod),35 unbinding,109
mangling named expression,102
name,85 named tuple,172
mapping,171 NameError
object,27,35,94,107 exception,85
match NameError(built-inexception),68
case,123 names
statement,123 private,85
matrix multiplication,97 namespace,67,172
membership global,27
test,101 module,30
meta package,74
hooks,75 namespace package,172
meta hooks,75 negation,97
meta path finder,171 nested scope,172
metaclass,50,171 new-style class,172
metaclass hint,51 NEWLINE token,7,117
method,171 None
built-in,30 object,24,105
call,96 nonlocal
magic,171 statement,115
object,28,30,96 not
special,176 operator,102
user-defined,28 not in
method resolution order,171 operator,101
minus,97 notation,4
module,171 NotImplemented
__main__,68,141 object,24
array,26 null
212 Index

### 第221页

operation,109 power,97
number,18 shifting,98
complex,25 unaryarithmetic,97
floating-point,25 unarybitwise,97
numeric operator
object,24,35 -(minus),97,98
numeric literal,18 %(percent),98
&(ampersand),99
O
*(asterisk),97
object,23,172 **,97
asynchronous-generator,92 +(plus),97,98
Boolean,25 /(slash),98
built-in function,30,96 //,98
built-in method,30,96 <(less),99
callable,27,95 <<,98
class,33,96,133 <=,99
class instance,33,35,96 !=,99
code,36 ==,99
complex,25 >(greater),99
dictionary,27,33,44,88,94,107 >=,99
Ellipsis,24 >>,98
floating-point,25 @(at),97
frame,39 ^(caret),99
frozenset,27 |(verticalbar),99
function,27,30,96,131 ~(tilde),97
generator,38,89,90 and,102
immutable,26,86,89 in,101
immutable sequence,26 is,101
instance,33,35,96 is not,101
integer,25 not,102
list,26,88,93,94,107 not in,101
mapping,27,35,94,107 or,102
method,28,30,96 overloading,41
module,30,93 precedence,104
mutable,26,105,106 ternary,102
mutable sequence,26 operators,21
None,24,105 optimized scope,172
NotImplemented,24 or
numeric,24,35 bitwise,99
sequence,25,35,94,101,107,118 exclusive,99
set,27,88 inclusive,99
set type,26 operator,102
slice,56 ord
string,94 built-in function,26
traceback,40,110,120 order
tuple,26,94,103 evaluation,103
user-defined function,27,96,131 output,105
user-defined method,28 standard,105
object.__match_args__(built-invariable),60 overloading
object.__slots__(built-invariable),49 operator,41
octal literal,18
P
open
built-in function,35 package,73,172
operation namespace,74
binaryarithmetic,97 portion,74
binarybitwise,99 regular,74
Boolean,102 parameter,173
null,109 call semantics,95
Index 213

### 第222页

function definition,131 PEP 380,90
value,default,132 PEP 411,174
parenthesized form,87 PEP 414,13
parser,7 PEP 420,73,74,79,83,172,174
pass PEP 443,168
statement,109 PEP 448,88,96,103
path PEP 451,83
hooks,75 PEP 483,168
path based finder,80,173 PEP 484,53,108,133,161,167,168,177,178
path entry,173 PEP 492,63,90,136,162165
path entry finder,173 PEP 498,18,166
path entry hook,173 PEP 519,173
path hooks,75 PEP 525,90,162
path-like object,173 PEP 526,108,133,161,178
pattern matching,123 PEP 530,88
PEP,173 PEP 560,51,55
physical line,7,8,13 PEP 562,47
plus,97 PEP 563,114,133
popen()(inmoduleos),35 PEP 570,132
portion,174 PEP 572,89,102,127
package,74 PEP 585,168
positional argument,174 PEP 614,132,134
pow PEP 617,4
built-in function,57,58 PEP 626,39
power PEP 634,60,124,131
operation,97 PEP 636,124,131
precedence PEP 646,94,103,132
operator,104 PEP 649,28,32,34,61,69,161
primary,93 PEP 683,169
print PEP 688,61
built-in function,43 PEP 695,69,116
print()(built-infunction) PEP 696,69,136
__str__()(objectmethod),43 PEP 703,167,168
private PEP 749,69,140
names,85 PEP 749#pep749-metaclasses,34
procedure PEP 758,119
call,105 PEP 765,121
program,141 PEP 3104,115
provisional API,174 PEP 3107,133
provisional package,174 PEP 3115,52,134
Python 3000,174 PEP 3116,177
Python Enhancement Proposals PEP 3119,53
PEP 1,174 PEP 3120,7
PEP 8,100 PEP 3129,133,134
PEP 236,114 PEP 3131,10
PEP 238,167 PEP 3132,107
PEP 252,47 PEP 3135,53
PEP 255,90 PEP 3147,32
PEP 278,177 PEP 3155,174
PEP 302,73,83,171 PYTHON_GIL,168
PEP 308,103 PYTHONHASHSEED,45
PEP 318,133,134 Pythonic,174
PEP 328,83 PYTHONNODEBUGRANGES,38
PEP 338,83 PYTHONPATH,80
PEP 342,90
Q
PEP 343,60,123,164
PEP 362,162,173 qualified name,174
PEP 366,31,83
214 Index

### 第223页

R
singleton
tuple,26
r'
raw string literal,16
slice,94,175
built-in function,41
r"
raw string literal,16
object,56
slicing,25,26,94
raise
statement,110
assignment,107
raise an exception,70 soft deprecated,175
soft keyword,11
raising
exception,110 source character set,7
space,8
range
built-in function,118 special
attribute,24
rebinding
name,105
attribute,generic,24
method,176
reference
attribute,93 special method,176
reference count,175 stack
reference counting,23
execution,40
trace,40
regular
package,74 standard
regular package,175
output,105
Standard C,13
relative
import,113 standard input,141
REPL,175 standard library,176
replace()(codeobjectmethod),39
start(sliceobjectattribute),41,94
statement,176
repr
built-in function,105
assert,108
repr()(built-infunction)
assignment,26,105
__repr__()(objectmethod),43 assignment, annotated,108
assignment, augmented,107
representation
integer,25 async def,134
reserved word,11 async for,134
async with,135
restricted
execution,70
break,112,118,121
class,133
return
statement,109,121
compound,117
continue,112,118,121
round
built-in function,59
def,131
del,42,109
S expression,105
for,112,118
scope,67,68
future,113
send()(coroutinemethod),63
global,109,114
send()(generatormethod),91
if,118
sequence,175
import,30,112
item,94
loop,112,118
object,25,35,94,101,107,118
match,123
set
nonlocal,115
comprehensions,88
pass,109
display,88
raise,110
object,27,88
return,109,121
set comprehension,175
simple,105
set type
try,40,119
object,26
type,115
shifting
while,112,118
operation,98
with,59,122
simple
yield,110
statement,105
statement grouping,8
single dispatch,175
Index 215

### 第224页

static type checker,176 tb_next(tracebackattribute),41
stderr(inmodulesys),35 termination model,71
stdin(inmodulesys),35 ternary
stdio,35 operator,102
stdlib,176 test
stdout(inmodulesys),35 identity,101
step(sliceobjectattribute),41,94 membership,101
stop(sliceobjectattribute),41,94 text encoding,176
StopAsyncIteration text file,176
exception,93 thread state,176
StopIteration throw()(coroutinemethod),63
exception,91,110 throw()(generatormethod),91
string token,7,177
__format__()(objectmethod),43 trace
__str__()(objectmethod),43 stack,40
conversion,43,105 traceback
formatted literal,16 object,40,110,120
immutable sequences,26 trailing
interpolated literal,16 comma,103
item,94 triple-quoted string,177
object,94 triple-quoted string,12
string literal,12 True,25
strong reference,176 try
subclassing statement,40,119
immutable types,42 tuple
subscription,2527,94 empty,26,87
assignment,106 object,26,94,103
subtraction,98 singleton,26
suite,117 type,24,177
syntax,4 built-in function,23,50
sys data,24
module,120,141 hierarchy,24
sys.exc_info,40 immutabledata,86
sys.exception,40 statement,115
sys.last_traceback,40 type alias,177
sys.meta_path,75 type hint,177
sys.modules,75 type of an object,23
sys.path,80 type parameters,136
sys.path_hooks,80 TypeError
sys.path_importer_cache,80 exception,97
sys.stderr,35 types, internal,35
sys.stdin,35
U
sys.stdout,35
SystemExit(built-inexception),71 u'
string literal,12
T
u"
t-string,176 string literal,12
t-strings,176 unary
tab,8 arithmeticoperation,97
target,106 bitwiseoperation,97
deletion,109 unbinding
list,106,118 name,109
listassignment,106 UnboundLocalError,68
list,deletion,109 Unicode,26
loop control,112 universal newlines,177
tb_frame(tracebackattribute),40,41 UNIX,141
tb_lasti(tracebackattribute),40,41 unpacking
tb_lineno(tracebackattribute),40,41 dictionary,88
216 Index

### 第225页

in function calls,95
iterable,103
unreachable object,23
unrecognized escape sequence,15
user-defined
function,27
functioncall,96
method,28
user-defined function
object,27,96,131
user-defined method
object,28
V
value,88
defaultparameter,132
value of an object,23
ValueError
exception,98
values
writing,105
variable
free,67
variable annotation,177
virtual environment,178
virtual machine,178
W
walrus operator,102,178
while
statement,112,118
Windows,141
with
statement,59,122
writing
values,105
X
xor
bitwise,99
Y
yield
examples,91
expression,89
keyword,89
statement,110
Z
Zen of Python,178
ZeroDivisionError
exception,98
Index 217

