### 第1页

Sorting Techniques
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 SortingBasics 1
2 KeyFunctions 2
3 OperatorModuleFunctionsandPartialFunctionEvaluation 3
4 AscendingandDescending 3
5 SortStabilityandComplexSorts 3
6 Decorate-Sort-Undecorate 4
7 ComparisonFunctions 5
8 StrategiesForUnorderableTypesandValues 5
9 OddsandEnds 6
10 PartialSorts 6
Index 7
Author
AndrewDalkeandRaymondHettinger
Pythonlistshaveabuilt-inlist.sort()methodthatmodifiesthelistin-place. Thereisalsoasorted()built-in
functionthatbuildsanewsortedlistfromaniterable.
Inthisdocument,weexplorethevarioustechniquesforsortingdatausingPython.
1 Sorting Basics
Asimpleascendingsortisveryeasy: justcallthesorted()function. Itreturnsanewsortedlist:
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
1

### 第2页

You can also use the list.sort() method. It modifies the list in-place (and returns None to avoid confusion).
Usuallyit’slessconvenientthansorted()-butifyoudon’tneedtheoriginallist,it’sslightlymoreefficient.
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
Anotherdifferenceisthatthelist.sort()methodisonlydefinedforlists. Incontrast, thesorted()function
acceptsanyiterable.
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
2 Key Functions
The list.sort() method and the functions sorted(), min(), max(), heapq.nsmallest(), and heapq.
nlargest()haveakeyparametertospecifyafunction(orothercallable)tobecalledoneachlistelementpriorto
makingcomparisons.
Forexample,here’sacase-insensitivestringcomparisonusingstr.casefold():
>>> sorted("This is a test string from Andrew".split(), key=str.casefold)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
The value of the key parameter should be a function (or other callable) that takes a single argument and returns a
keytouseforsortingpurposes. Thistechniqueisfastbecausethekeyfunctioniscalledexactlyonceforeachinput
record.
Acommonpatternistosortcomplexobjectsusingsomeoftheobject’sindicesaskeys. Forexample:
>>> student_tuples = [
... ('john', 'A', 15),
... ('jane', 'B', 12),
... ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2]) # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Thesametechniqueworksforobjectswithnamedattributes. Forexample:
>>> class Student:
... def __init__(self, name, grade, age):
... self.name = name
... self.grade = grade
... self.age = age
... def __repr__(self):
... return repr((self.name, self.grade, self.age))
>>> student_objects = [
... Student('john', 'A', 15),
... Student('jane', 'B', 12),
... Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age) # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Objectswithnamedattributescanbemadebyaregularclassasshownabove,ortheycanbeinstancesofdataclass
oranamedtuple.
2

### 第3页

3 Operator Module Functions and Partial Function Evaluation
Thekeyfunctionpatternsshownaboveareverycommon,soPythonprovidesconveniencefunctionstomakeaccessor
functionseasierandfaster. Theoperatormodulehasitemgetter(),attrgetter(),andamethodcaller()
function.
Usingthosefunctions,theaboveexamplesbecomesimplerandfaster:
>>> from operator import itemgetter, attrgetter
>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Theoperatormodulefunctionsallowmultiplelevelsofsorting. Forexample,tosortbygradethenbyage:
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
The functools module provides another helpful tool for making key-functions. The partial() function can
reducethearityofamulti-argumentfunctionmakingitsuitableforuseasakey-function.
>>> from functools import partial
>>> from unicodedata import normalize
>>> names = 'Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise'.split()
>>> sorted(names, key=partial(normalize, 'NFD'))
['Abe', 'Åbjørn', 'Eloise', 'Élana', 'Nubia', 'Núñez', 'Zeke', 'Zoë']
>>> sorted(names, key=partial(normalize, 'NFC'))
['Abe', 'Eloise', 'Nubia', 'Núñez', 'Zeke', 'Zoë', 'Åbjørn', 'Élana']
4 Ascending and Descending
Bothlist.sort()andsorted()acceptareverseparameterwithabooleanvalue. Thisisusedtoflagdescending
sorts. Forexample,togetthestudentdatainreverseageorder:
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
5 Sort Stability and Complex Sorts
Sortsareguaranteedtobestable. Thatmeansthatwhenmultiplerecordshavethesamekey,theiroriginalorderis
preserved.
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
3

### 第4页

Notice how the two records for blue retain their original order so that ('blue', 1) is guaranteed to precede
('blue', 2).
This wonderful property lets you build complex sorts in a series of sorting steps. For example, to sort the student
databydescendinggradeandthenascendingage,dotheagesortfirstandthensortagainusinggrade:
>>> s = sorted(student_objects, key=attrgetter('age')) # sort on secondary key
>>> sorted(s, key=attrgetter('grade'), reverse=True) # now sort on primary␣
,→key, descending
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
Thiscanbeabstractedoutintoawrapperfunctionthatcantakealistandtuplesoffieldandordertosortthemon
multiplepasses.
>>> def multisort(xs, specs):
... for key, reverse in reversed(specs):
... xs.sort(key=attrgetter(key), reverse=reverse)
... return xs
>>> multisort(list(student_objects), (('grade', True), ('age', False)))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
TheTimsortalgorithmusedinPythondoesmultiplesortsefficientlybecauseitcantakeadvantageofanyordering
alreadypresentinadataset.
6 Decorate-Sort-Undecorate
ThisidiomiscalledDecorate-Sort-Undecorateafteritsthreesteps:
• First,theinitiallistisdecoratedwithnewvaluesthatcontrolthesortorder.
• Second,thedecoratedlistissorted.
• Finally,thedecorationsareremoved,creatingalistthatcontainsonlytheinitialvaluesintheneworder.
Forexample,tosortthestudentdatabygradeusingtheDSUapproach:
>>> decorated = [(student.grade, i, student) for i, student in enumerate(student_
,→objects)]
>>> decorated.sort()
>>> [student for grade, i, student in decorated] # undecorate
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
Thisidiomworksbecausetuplesarecomparedlexicographically;thefirstitemsarecompared;iftheyarethesame
thentheseconditemsarecompared,andsoon.
Itisnotstrictlynecessaryinallcasestoincludetheindexiinthedecoratedlist,butincludingitgivestwobenefits:
• Thesortisstable–iftwoitemshavethesamekey,theirorderwillbepreservedinthesortedlist.
• Theoriginalitemsdonothavetobecomparablebecausetheorderingofthedecoratedtupleswillbedetermined
byatmostthefirsttwoitems. Soforexampletheoriginallistcouldcontaincomplexnumberswhichcannot
besorteddirectly.
Another name for this idiom is Schwartzian transform, after Randal L. Schwartz, who popularized it among Perl
programmers.
NowthatPythonsortingprovideskey-functions,thistechniqueisnotoftenneeded.
4

### 第5页

7 Comparison Functions
Unlikekeyfunctionsthatreturnanabsolutevalueforsorting,acomparisonfunctioncomputestherelativeordering
fortwoinputs.
Forexample,abalancescalecomparestwosamplesgivingarelativeordering: lighter,equal,orheavier. Likewise,a
comparisonfunctionsuchascmp(a, b)willreturnanegativevalueforless-than,zeroiftheinputsareequal,ora
positivevalueforgreater-than.
It is common to encounter comparison functions when translating algorithms from other languages. Also, some
libraries provide comparison functions as part of their API. For example, locale.strcoll() is a comparison
function.
Toaccommodatethosesituations,Pythonprovidesfunctools.cmp_to_keytowrapthecomparisonfunctionto
makeitusableasakeyfunction:
sorted(words, key=cmp_to_key(strcoll)) # locale-aware sort order
8 Strategies For Unorderable Types and Values
Anumberoftypeandvalueissuescanarisewhensorting. Herearesomestrategiesthatcanhelp:
• Convertnon-comparableinputtypestostringspriortosorting:
>>> data = ['twelve', '11', 10]
>>> sorted(map(str, data))
['10', '11', 'twelve']
Thisisneededbecausemostcross-typecomparisonsraiseaTypeError.
• Removespecialvaluespriortosorting:
>>> from math import isnan
>>> from itertools import filterfalse
>>> data = [3.3, float('nan'), 1.1, 2.2]
>>> sorted(filterfalse(isnan, data))
[1.1, 2.2, 3.3]
ThisisneededbecausetheIEEE-754standardspecifiesthat,“EveryNaNshallcompareunorderedwitheverything,
includingitself.”
Likewise,Nonecanbestrippedfromdatasetsaswell:
>>> data = [3.3, None, 1.1, 2.2]
>>> sorted(x for x in data if x is not None)
[1.1, 2.2, 3.3]
ThisisneededbecauseNoneisnotcomparabletoothertypes.
• Convertmappingtypesintosorteditemlistsbeforesorting:
>>> data = [{'a': 1}, {'b': 2}]
>>> sorted(data, key=lambda d: sorted(d.items()))
[{'a': 1}, {'b': 2}]
Thisisneededbecausedict-to-dictcomparisonsraiseaTypeError.
• Convertsettypesintosortedlistsbeforesorting:
>>> data = [{'a', 'b', 'c'}, {'b', 'c', 'd'}]
>>> sorted(map(sorted, data))
[['a', 'b', 'c'], ['b', 'c', 'd']]
5

### 第6页

This is needed because the elements contained in set types do not have a deterministic order. For example,
list({'a', 'b'})mayproduceeither['a', 'b']or['b', 'a'].
9 Odds and Ends
• For locale aware sorting, use locale.strxfrm() for a key function or locale.strcoll() for a com-
parisonfunction. Thisisnecessarybecause“alphabetical”sortorderingscanvaryacrossculturesevenifthe
underlyingalphabetisthesame.
• Thereverseparameterstillmaintainssortstability(sothatrecordswithequalkeysretaintheoriginalorder).
Interestingly, that effect can be simulated without the parameter by using the builtin reversed() function
twice:
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> standard_way = sorted(data, key=itemgetter(0), reverse=True)
>>> double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
>>> assert standard_way == double_reversed
>>> standard_way
[('red', 1), ('red', 2), ('blue', 1), ('blue', 2)]
• Thesortroutinesuse<whenmakingcomparisonsbetweentwoobjects. So,itiseasytoaddastandardsort
ordertoaclassbydefiningan__lt__()method:
>>> Student.__lt__ = lambda self, other: self.age < other.age
>>> sorted(student_objects)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
However, note that < can fall back to using __gt__() if __lt__() is not implemented (see object.
__lt__() for details on the mechanics). To avoid surprises, PEP 8 recommends that all six comparison
methodsbeimplemented. Thetotal_ordering()decoratorisprovidedtomakethattaskeasier.
• Keyfunctionsneednotdependdirectlyontheobjectsbeingsorted. Akeyfunctioncanalsoaccessexternal
resources. Forinstance,ifthestudentgradesarestoredinadictionary,theycanbeusedtosortaseparatelist
ofstudentnames:
>>> students = ['dave', 'john', 'jane']
>>> newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
>>> sorted(students, key=newgrades.__getitem__)
['jane', 'dave', 'john']
10 Partial Sorts
Someapplicationsrequireonlysomeofthedatatobeordered. Thestandardlibraryprovidesseveraltoolsthatdo
lessworkthanafullsort:
• min()andmax()returnthesmallestandlargestvalues,respectively. Thesefunctionsmakeasinglepassover
theinputdataandrequirealmostnoauxiliarymemory.
• heapq.nsmallest()andheapq.nlargest()returnthensmallestandlargestvalues,respectively. These
functionsmakeasinglepassoverthedatakeepingonlynelementsinmemoryatatime. Forvaluesofnthat
aresmallrelativetothenumberofinputs,thesefunctionsmakefarfewercomparisonsthanafullsort.
• heapq.heappush()andheapq.heappop()createandmaintainapartiallysortedarrangementofdatathat
keepsthesmallestelementatposition0. Thesefunctionsaresuitableforimplementingpriorityqueueswhich
arecommonlyusedfortaskscheduling.
6

### 第7页

Index
P
Python Enhancement Proposals
PEP 8,6
7

