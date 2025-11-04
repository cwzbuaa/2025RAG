### 第1页

Functional Programming HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Introduction 2
1.1 Formalprovability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Modularity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Easeofdebuggingandtesting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Composability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Iterators 4
2.1 DataTypesThatSupportIterators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3 Generatorexpressionsandlistcomprehensions 6
4 Generators 7
4.1 Passingvaluesintoagenerator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5 Built-infunctions 10
6 Theitertoolsmodule 11
6.1 Creatingnewiterators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
6.2 Callingfunctionsonelements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
6.3 Selectingelements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
6.4 Combinatoricfunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
6.5 Groupingelements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
7 Thefunctoolsmodule 15
7.1 Theoperatormodule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
8 Smallfunctionsandthelambdaexpression 17
9 RevisionHistoryandAcknowledgements 18
10 References 18
10.1 General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
10.2 Python-specific . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
10.3 Pythondocumentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Index 20
1

### 第2页

Author
A.M.Kuchling
Release
0.32
In this document, we’ll take a tour of Python’s features suitable for implementing programs in a functional style.
Afteranintroductiontotheconceptsoffunctionalprogramming,we’lllookatlanguagefeaturessuchasiteratorsand
generatorsandrelevantlibrarymodulessuchasitertoolsandfunctools.
1 Introduction
Thissectionexplainsthebasicconceptoffunctionalprogramming;ifyou’rejustinterestedinlearningaboutPython
languagefeatures,skiptothenextsectiononIterators.
Programminglanguagessupportdecomposingproblemsinseveraldifferentways:
• Mostprogramminglanguagesareprocedural: programsarelistsofinstructionsthattellthecomputerwhat
todowiththeprogram’sinput. C,Pascal,andevenUnixshellsareprocedurallanguages.
• Indeclarativelanguages,youwriteaspecificationthatdescribestheproblemtobesolved,andthelanguage
implementationfiguresouthowtoperformthecomputationefficiently. SQListhedeclarativelanguageyou’re
mostlikelytobefamiliarwith;aSQLquerydescribesthedatasetyouwanttoretrieve,andtheSQLengine
decideswhethertoscantablesoruseindexes,whichsubclausesshouldbeperformedfirst,etc.
• Object-orientedprogramsmanipulatecollectionsofobjects. Objectshaveinternalstateandsupportmethods
thatqueryormodifythisinternalstateinsomeway. SmalltalkandJavaareobject-orientedlanguages. C++
andPythonarelanguagesthatsupportobject-orientedprogramming,butdon’tforcetheuseofobject-oriented
features.
• Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs
andproduceoutputs,anddon’thaveanyinternalstatethataffectstheoutputproducedforagiveninput. Well-
knownfunctionallanguagesincludetheMLfamily(StandardML,OCaml,andothervariants)andHaskell.
Thedesignersofsomecomputerlanguageschoosetoemphasizeoneparticularapproachtoprogramming. Thisoften
makesitdifficulttowriteprogramsthatuseadifferentapproach. Otherlanguagesaremulti-paradigmlanguagesthat
supportseveraldifferentapproaches. Lisp,C++,andPythonaremulti-paradigm;youcanwriteprogramsorlibraries
that are largely procedural, object-oriented, or functional in all of these languages. In a large program, different
sectionsmightbewrittenusingdifferentapproaches;theGUImightbeobject-orientedwhiletheprocessinglogicis
proceduralorfunctional,forexample.
Inafunctionalprogram,inputflowsthroughasetoffunctions. Eachfunctionoperatesonitsinputandproducessome
output. Functionalstylediscouragesfunctionswithsideeffectsthatmodifyinternalstateormakeotherchangesthat
aren’t visible in the function’s return value. Functions that have no side effects at all are called purely functional.
Avoidingsideeffectsmeansnotusingdatastructuresthatgetupdatedasaprogramruns;everyfunction’soutputmust
onlydependonitsinput.
Somelanguagesareverystrictaboutpurityanddon’tevenhaveassignmentstatementssuchasa=3orc = a + b,
butit’sdifficulttoavoidallsideeffects,suchasprintingtothescreenorwritingtoadiskfile. Anotherexampleisa
calltotheprint()ortime.sleep()function,neitherofwhichreturnsausefulvalue. Botharecalledonlyfor
theirsideeffectsofsendingsometexttothescreenorpausingexecutionforasecond.
Pythonprogramswritteninfunctionalstyleusuallywon’tgototheextremeofavoidingallI/Oorallassignments;
instead,they’llprovideafunctional-appearinginterfacebutwillusenon-functionalfeaturesinternally. Forexample,
the implementation of a function will still use assignments to local variables, but won’t modify global variables or
haveothersideeffects.
Functionalprogrammingcanbeconsideredtheoppositeofobject-orientedprogramming. Objectsarelittlecapsules
containingsomeinternalstatealongwithacollectionofmethodcallsthatletyoumodifythisstate, andprograms
consistofmakingtherightsetofstatechanges. Functionalprogrammingwantstoavoidstatechangesasmuchas
possibleandworkswithdataflowingbetweenfunctions. InPythonyoumightcombinethetwoapproachesbywriting
functionsthattakeandreturninstancesrepresentingobjectsinyourapplication(e-mailmessages,transactions,etc.).
2

### 第3页

Functionaldesignmayseemlikeanoddconstrainttoworkunder. Whyshouldyouavoidobjectsandsideeffects?
Therearetheoreticalandpracticaladvantagestothefunctionalstyle:
• Formalprovability.
• Modularity.
• Composability.
• Easeofdebuggingandtesting.
1.1 Formal provability
Atheoreticalbenefitisthatit’seasiertoconstructamathematicalproofthatafunctionalprogramiscorrect.
Foralongtimeresearchershavebeeninterestedinfindingwaystomathematicallyproveprogramscorrect. Thisis
differentfromtestingaprogramonnumerousinputsandconcludingthatitsoutputisusuallycorrect, orreadinga
program’ssourcecodeandconcludingthatthecodelooksright;thegoalisinsteadarigorousproofthataprogram
producestherightresultforallpossibleinputs.
Thetechniqueusedtoproveprogramscorrectistowritedowninvariants,propertiesoftheinputdataandofthe
program’svariablesthatarealwaystrue. Foreachlineofcode,youthenshowthatifinvariantsXandYaretruebefore
thelineisexecuted,theslightlydifferentinvariantsX’andY’aretrueafterthelineisexecuted. Thiscontinuesuntil
youreachtheendoftheprogram,atwhichpointtheinvariantsshouldmatchthedesiredconditionsontheprogram’s
output.
Functionalprogramming’savoidanceofassignmentsarosebecauseassignmentsaredifficulttohandlewiththistech-
nique;assignmentscanbreakinvariantsthatweretruebeforetheassignmentwithoutproducinganynewinvariants
thatcanbepropagatedonward.
Unfortunately, proving programs correct is largely impractical and not relevant to Python software. Even trivial
programsrequireproofsthatareseveralpageslong;theproofofcorrectnessforamoderatelycomplicatedprogram
wouldbeenormous,andfewornoneoftheprogramsyouusedaily(thePythoninterpreter,yourXMLparser,your
webbrowser)couldbeprovencorrect. Evenifyouwrotedownorgeneratedaproof,therewouldthenbethequestion
ofverifyingtheproof;maybethere’sanerrorinit,andyouwronglybelieveyou’veprovedtheprogramcorrect.
1.2 Modularity
Amorepracticalbenefitoffunctionalprogrammingisthatitforcesyoutobreakapartyourproblemintosmallpieces.
Programsaremoremodularasaresult. It’seasiertospecifyandwriteasmallfunctionthatdoesonethingthana
largefunctionthatperformsacomplicatedtransformation. Smallfunctionsarealsoeasiertoreadandtocheckfor
errors.
1.3 Ease of debugging and testing
Testinganddebuggingafunctional-styleprogramiseasier.
Debuggingissimplifiedbecausefunctionsaregenerallysmallandclearlyspecified. Whenaprogramdoesn’twork,
eachfunctionisaninterfacepointwhereyoucancheckthatthedataarecorrect. Youcanlookattheintermediate
inputsandoutputstoquicklyisolatethefunctionthat’sresponsibleforabug.
Testingiseasierbecauseeachfunctionisapotentialsubjectforaunittest. Functionsdon’tdependonsystemstate
thatneedstobereplicatedbeforerunningatest;insteadyouonlyhavetosynthesizetherightinputandthencheck
thattheoutputmatchesexpectations.
1.4 Composability
Asyouworkonafunctional-styleprogram,you’llwriteanumberoffunctionswithvaryinginputsandoutputs. Some
ofthesefunctionswillbeunavoidablyspecializedtoaparticularapplication,butotherswillbeusefulinawidevariety
ofprograms. Forexample,afunctionthattakesadirectorypathandreturnsalltheXMLfilesinthedirectory,ora
functionthattakesafilenameandreturnsitscontents,canbeappliedtomanydifferentsituations.
Over time you’ll form a personal library of utilities. Often you’ll assemble new programs by arranging existing
functionsinanewconfigurationandwritingafewfunctionsspecializedforthecurrenttask.
3

### 第4页

2 Iterators
I’llstartbylookingataPythonlanguagefeaturethat’sanimportantfoundationforwritingfunctional-styleprograms:
iterators.
Aniteratorisanobjectrepresentingastreamofdata;thisobjectreturnsthedataoneelementatatime. APython
iteratormustsupportamethodcalled__next__()thattakesnoargumentsandalwaysreturnsthenextelementof
thestream. Iftherearenomoreelementsinthestream,__next__()mustraisetheStopIterationexception.
Iteratorsdon’thavetobefinite,though;it’sperfectlyreasonabletowriteaniteratorthatproducesaninfinitestream
ofdata.
The built-in iter() function takes an arbitrary object and tries to return an iterator that will return the object’s
contents or elements, raising TypeError if the object doesn’t support iteration. Several of Python’s built-in data
typessupportiteration,themostcommonbeinglistsanddictionaries. Anobjectiscallediterableifyoucangetan
iteratorforit.
Youcanexperimentwiththeiterationinterfacemanually:
>>> L = [1, 2, 3]
>>> it = iter(L)
>>> it
<...iterator object at ...>
>>> it.__next__() # same as next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>>
Python expects iterable objects in several different contexts, the most important being the for statement. In the
statementfor X in Y,Ymustbeaniteratororsomeobjectforwhichiter()cancreateaniterator. Thesetwo
statementsareequivalent:
for i in iter(obj):
print(i)
for i in obj:
print(i)
Iteratorscanbematerializedaslistsortuplesbyusingthelist()ortuple()constructorfunctions:
>>> L = [1, 2, 3]
>>> iterator = iter(L)
>>> t = tuple(iterator)
>>> t
(1, 2, 3)
Sequenceunpackingalsosupportsiterators: ifyouknowaniteratorwillreturnNelements, youcanunpackthem
intoanN-tuple:
>>> L = [1, 2, 3]
>>> iterator = iter(L)
>>> a, b, c = iterator
>>> a, b, c
(1, 2, 3)
4

### 第5页

Built-infunctionssuchasmax()andmin()cantakeasingleiteratorargumentandwillreturnthelargestorsmallest
element. The"in" and"not in" operatorsalsosupportiterators: X in iterator istrue ifX isfoundinthe
streamreturnedbytheiterator. You’llrunintoobviousproblemsiftheiteratorisinfinite;max(),min()willnever
return,andiftheelementXneverappearsinthestream,the"in"and"not in"operatorswon’treturneither.
Note that you can only go forward in an iterator; there’s no way to get the previous element, reset the iterator, or
makeacopyofit. Iteratorobjectscanoptionallyprovidetheseadditionalcapabilities,buttheiteratorprotocolonly
specifiesthe__next__()method. Functionsmaythereforeconsumealloftheiterator’soutput,andifyouneedto
dosomethingdifferentwiththesamestream,you’llhavetocreateanewiterator.
2.1 Data Types That Support Iterators
We’ve already seen how lists and tuples support iterators. In fact, any Python sequence type, such as strings, will
automaticallysupportcreationofaniterator.
Callingiter()onadictionaryreturnsaniteratorthatwillloopoverthedictionary’skeys:
>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
... 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
>>> for key in m:
... print(key, m[key])
Jan 1
Feb 2
Mar 3
Apr 4
May 5
Jun 6
Jul 7
Aug 8
Sep 9
Oct 10
Nov 11
Dec 12
NotethatstartingwithPython3.7,dictionaryiterationorderisguaranteedtobethesameastheinsertionorder. In
earlierversions,thebehaviourwasunspecifiedandcouldvarybetweenimplementations.
Applyingiter()toadictionaryalwaysloopsoverthekeys,butdictionarieshavemethodsthatreturnotheriterators.
Ifyouwanttoiterateovervaluesorkey/valuepairs,youcanexplicitlycallthevalues()oritems()methodsto
getanappropriateiterator.
Thedict()constructorcanacceptaniteratorthatreturnsafinitestreamof(key, value)tuples:
>>> L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
>>> dict(iter(L))
{'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}
Filesalsosupportiterationbycallingthereadline()methoduntiltherearenomorelinesinthefile. Thismeans
youcanreadeachlineofafilelikethis:
for line in file:
# do something for each line
...
Setscantaketheircontentsfromaniterableandletyouiterateovertheset’selements:
>>> S = {2, 3, 5, 7, 11, 13}
>>> for i in S:
... print(i)
2
(continuesonnextpage)
5

### 第6页

(continuedfrompreviouspage)
3
5
7
11
13
3 Generator expressions and list comprehensions
Twocommonoperationsonaniterator’soutputare1)performingsomeoperationforeveryelement,2)selectinga
subsetofelementsthatmeetsomecondition. Forexample,givenalistofstrings,youmightwanttostripofftrailing
whitespacefromeachlineorextractallthestringscontainingagivensubstring.
List comprehensions and generator expressions (short form: “listcomps” and “genexps”) are a concise notation for
suchoperations,borrowedfromthefunctionalprogramminglanguageHaskell(https://www.haskell.org/). Youcan
stripallthewhitespacefromastreamofstringswiththefollowingcode:
>>> line_list = [' line 1\n', 'line 2 \n', ' \n', '']
>>> # Generator expression -- returns iterator
>>> stripped_iter = (line.strip() for line in line_list)
>>> # List comprehension -- returns list
>>> stripped_list = [line.strip() for line in line_list]
Youcanselectonlycertainelementsbyaddingan"if"condition:
>>> stripped_list = [line.strip() for line in line_list
... if line != ""]
Withalistcomprehension,yougetbackaPythonlist;stripped_listisalistcontainingtheresultinglines,notan
iterator. Generatorexpressionsreturnaniteratorthatcomputesthevaluesasnecessary,notneedingtomaterialize
allthevaluesatonce. Thismeansthatlistcomprehensionsaren’tusefulifyou’reworkingwithiteratorsthatreturn
aninfinitestreamoraverylargeamountofdata. Generatorexpressionsarepreferableinthesesituations.
Generatorexpressionsaresurroundedbyparentheses(“()”)andlistcomprehensionsaresurroundedbysquarebrack-
ets(“[]”). Generatorexpressionshavetheform:
( expression for expr in sequence1
if condition1
for expr2 in sequence2
if condition2
for expr3 in sequence3
...
if condition3
for exprN in sequenceN
if conditionN )
Again,foralistcomprehensiononlytheoutsidebracketsaredifferent(squarebracketsinsteadofparentheses).
Theelementsofthegeneratedoutputwillbethesuccessivevaluesofexpression. Theifclausesarealloptional;
ifpresent,expressionisonlyevaluatedandaddedtotheresultwhenconditionistrue.
Generatorexpressionsalwayshavetobewritteninsideparentheses,buttheparenthesessignallingafunctioncallalso
count. Ifyouwanttocreateaniteratorthatwillbeimmediatelypassedtoafunctionyoucanwrite:
obj_total = sum(obj.count for obj in list_all_objects())
Thefor...inclausescontainthesequencestobeiteratedover. Thesequencesdonothavetobethesamelength,
becausetheyareiteratedoverfromlefttoright, notinparallel. Foreachelementinsequence1, sequence2is
6

### 第7页

loopedoverfromthebeginning. sequence3isthenloopedoverforeachresultingpairofelementsfromsequence1
andsequence2.
Toputitanotherway,alistcomprehensionorgeneratorexpressionisequivalenttothefollowingPythoncode:
for expr1 in sequence1:
if not (condition1):
continue # Skip this element
for expr2 in sequence2:
if not (condition2):
continue # Skip this element
...
for exprN in sequenceN:
if not (conditionN):
continue # Skip this element
# Output the value of
# the expression.
Thismeansthatwhentherearemultiplefor...inclausesbutnoifclauses,thelengthoftheresultingoutputwill
be equal to the product of the lengths of all the sequences. If you have two lists of length 3, the output list is 9
elementslong:
>>> seq1 = 'abc'
>>> seq2 = (1, 2, 3)
>>> [(x, y) for x in seq1 for y in seq2]
[('a', 1), ('a', 2), ('a', 3),
('b', 1), ('b', 2), ('b', 3),
('c', 1), ('c', 2), ('c', 3)]
ToavoidintroducinganambiguityintoPython’sgrammar,ifexpressioniscreatingatuple,itmustbesurrounded
withparentheses. Thefirstlistcomprehensionbelowisasyntaxerror,whilethesecondoneiscorrect:
# Syntax error
[x, y for x in seq1 for y in seq2]
# Correct
[(x, y) for x in seq1 for y in seq2]
4 Generators
Generatorsareaspecialclassoffunctionsthatsimplifythetaskofwritingiterators. Regularfunctionscomputea
valueandreturnit,butgeneratorsreturnaniteratorthatreturnsastreamofvalues.
You’redoubtlessfamiliarwithhowregularfunctioncallsworkinPythonorC.Whenyoucallafunction, itgetsa
privatenamespacewhereitslocalvariablesarecreated. Whenthefunctionreachesareturnstatement,thelocal
variablesaredestroyedandthevalueisreturnedtothecaller. Alatercalltothesamefunctioncreatesanewprivate
namespaceandafreshsetoflocalvariables. But,whatifthelocalvariablesweren’tthrownawayonexitingafunction?
Whatifyoucouldlaterresumethefunctionwhereitleftoff? Thisiswhatgeneratorsprovide;theycanbethought
ofasresumablefunctions.
Here’sthesimplestexampleofageneratorfunction:
>>> def generate_ints(N):
... for i in range(N):
... yield i
Any function containing a yield keyword is a generator function; this is detected by Python’s bytecode compiler
whichcompilesthefunctionspeciallyasaresult.
7

### 第8页

Whenyoucallageneratorfunction,itdoesn’treturnasinglevalue;insteaditreturnsageneratorobjectthatsupports
theiteratorprotocol. Onexecutingtheyieldexpression,thegeneratoroutputsthevalueofi,similartoareturn
statement. Thebigdifferencebetweenyieldandareturnstatementisthatonreachingayieldthegenerator’s
stateofexecutionissuspendedandlocalvariablesarepreserved. Onthenextcalltothegenerator’s__next__()
method,thefunctionwillresumeexecuting.
Here’sasampleusageofthegenerate_ints()generator:
>>> gen = generate_ints(3)
>>> gen
<generator object generate_ints at ...>
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
Traceback (most recent call last):
File "stdin", line 1, in <module>
File "stdin", line 2, in generate_ints
StopIteration
Youcouldequallywritefor i in generate_ints(5),ora, b, c = generate_ints(3).
Insideageneratorfunction,return valuecausesStopIteration(value)toberaisedfromthe__next__()
method. Oncethishappens,orthebottomofthefunctionisreached,theprocessionofvaluesendsandthegenerator
cannotyieldanyfurthervalues.
Youcouldachievetheeffectofgeneratorsmanuallybywritingyourownclassandstoringallthelocalvariablesofthe
generatorasinstancevariables. Forexample,returningalistofintegerscouldbedonebysettingself.countto0,
andhavingthe__next__()methodincrementself.countandreturnit. However,foramoderatelycomplicated
generator,writingacorrespondingclasscanbemuchmessier.
ThetestsuiteincludedwithPython’slibrary,Lib/test/test_generators.py,containsanumberofmoreinterestingex-
amples. Here’sonegeneratorthatimplementsanin-ordertraversalofatreeusinggeneratorsrecursively.
# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
if t:
for x in inorder(t.left):
yield x
yield t.label
for x in inorder(t.right):
yield x
Twootherexamplesintest_generators.pyproducesolutionsfortheN-Queensproblem(placingNqueenson
anNxNchessboardsothatnoqueenthreatensanother)andtheKnight’sTour(findingaroutethattakesaknightto
everysquareofanNxNchessboardwithoutvisitinganysquaretwice).
4.1 Passing values into a generator
InPython2.4andearlier,generatorsonlyproducedoutput. Onceagenerator’scodewasinvokedtocreateaniterator,
there was no way to pass any new information into the function when its execution is resumed. You could hack
together this ability by making the generator look at a global variable or by passing in some mutable object that
callersthenmodify,buttheseapproachesaremessy.
InPython2.5there’sasimplewaytopassvaluesintoagenerator. yieldbecameanexpression,returningavalue
thatcanbeassignedtoavariableorotherwiseoperatedon:
8

### 第9页

val = (yield i)
I recommend that you always put parentheses around a yield expression when you’re doing something with the
returnedvalue,asintheaboveexample. Theparenthesesaren’talwaysnecessary,butit’seasiertoalwaysaddthem
insteadofhavingtorememberwhenthey’reneeded.
(PEP342explainstheexactrules,whicharethatayield-expressionmustalwaysbeparenthesizedexceptwhenit
occursatthetop-levelexpressionontheright-handsideofanassignment. Thismeansyoucanwriteval = yield
ibuthavetouseparentheseswhenthere’sanoperation,asinval = (yield i) + 12.)
Valuesaresentintoageneratorbycallingitssend(value)method. Thismethodresumesthegenerator’scodeand
theyieldexpressionreturnsthespecifiedvalue. Iftheregular__next__()methodiscalled,theyieldreturns
None.
Here’sasimplecounterthatincrementsby1andallowschangingthevalueoftheinternalcounter.
def counter(maximum):
i = 0
while i < maximum:
val = (yield i)
# If value provided, change counter
if val is not None:
i = val
else:
i += 1
Andhere’sanexampleofchangingthecounter:
>>> it = counter(10)
>>> next(it)
0
>>> next(it)
1
>>> it.send(8)
8
>>> next(it)
9
>>> next(it)
Traceback (most recent call last):
File "t.py", line 15, in <module>
it.next()
StopIteration
Because yield will often be returning None, you should always check for this case. Don’t just use its value in
expressions unless you’re sure that the send() method will be the only method used to resume your generator
function.
Inadditiontosend(),therearetwoothermethodsongenerators:
• throw(value)isusedtoraiseanexceptioninsidethegenerator; theexceptionisraisedbytheyieldex-
pressionwherethegenerator’sexecutionispaused.
• close() sends a GeneratorExit exception to the generator to terminate the iteration. On receiving this
exception,thegenerator’scodemusteitherraiseGeneratorExitorStopIteration;catchingtheexception
anddoinganythingelseisillegalandwilltriggeraRuntimeError. close()willalsobecalledbyPython’s
garbagecollectorwhenthegeneratorisgarbage-collected.
If you need to run cleanup code when a GeneratorExit occurs, I suggest using a try: ... finally:
suiteinsteadofcatchingGeneratorExit.
Thecumulativeeffectofthesechangesistoturngeneratorsfromone-wayproducersofinformationintobothpro-
ducersandconsumers.
9

### 第10页

Generatorsalsobecomecoroutines,amoregeneralizedformofsubroutines. Subroutinesareenteredatonepoint
andexitedatanotherpoint(thetopofthefunction,andareturnstatement),butcoroutinescanbeentered,exited,
andresumedatmanydifferentpoints(theyieldstatements).
5 Built-in functions
Let’slookinmoredetailatbuilt-infunctionsoftenusedwithiterators.
TwoofPython’sbuilt-infunctions,map()andfilter()duplicatethefeaturesofgeneratorexpressions:
map(f, iterA, iterB, ...)returnsaniteratoroverthesequence
f(iterA[0], iterB[0]), f(iterA[1], iterB[1]), f(iterA[2], iterB[2]), ....
>>> def upper(s):
... return s.upper()
>>> list(map(upper, ['sentence', 'fragment']))
['SENTENCE', 'FRAGMENT']
>>> [upper(s) for s in ['sentence', 'fragment']]
['SENTENCE', 'FRAGMENT']
Youcanofcourseachievethesameeffectwithalistcomprehension.
filter(predicate, iter)returnsaniteratoroverallthesequenceelementsthatmeetacertaincondition,andis
similarlyduplicatedbylistcomprehensions. Apredicateisafunctionthatreturnsthetruthvalueofsomecondition;
forusewithfilter(),thepredicatemusttakeasinglevalue.
>>> def is_even(x):
... return (x % 2) == 0
>>> list(filter(is_even, range(10)))
[0, 2, 4, 6, 8]
Thiscanalsobewrittenasalistcomprehension:
>>> list(x for x in range(10) if is_even(x))
[0, 2, 4, 6, 8]
enumerate(iter, start=0)countsofftheelementsintheiterablereturning2-tuplescontainingthecount(from
start)andeachelement.
>>> for item in enumerate(['subject', 'verb', 'object']):
... print(item)
(0, 'subject')
(1, 'verb')
(2, 'object')
enumerate()isoftenusedwhenloopingthroughalistandrecordingtheindexesatwhichcertainconditionsare
met:
f = open('data.txt', 'r')
for i, line in enumerate(f):
if line.strip() == '':
print('Blank line at line #%i' % i)
sorted(iterable, key=None, reverse=False)collectsalltheelementsoftheiterableintoalist,sortsthe
list,andreturnsthesortedresult. Thekeyandreverseargumentsarepassedthroughtotheconstructedlist’ssort()
method.
10

### 第11页

>>> import random
>>> # Generate 8 random numbers between [0, 10000)
>>> rand_list = random.sample(range(10000), 8)
>>> rand_list
[769, 7953, 9828, 6431, 8442, 9878, 6213, 2207]
>>> sorted(rand_list)
[769, 2207, 6213, 6431, 7953, 8442, 9828, 9878]
>>> sorted(rand_list, reverse=True)
[9878, 9828, 8442, 7953, 6431, 6213, 2207, 769]
(Foramoredetaileddiscussionofsorting,seethesortinghowto.)
Theany(iter)andall(iter)built-inslookatthetruthvaluesofaniterable’scontents. any()returnsTrueif
anyelementintheiterableisatruevalue,andall()returnsTrueifalloftheelementsaretruevalues:
>>> any([0, 1, 0])
True
>>> any([0, 0, 0])
False
>>> any([1, 1, 1])
True
>>> all([0, 1, 0])
False
>>> all([0, 0, 0])
False
>>> all([1, 1, 1])
True
zip(iterA, iterB, ...)takesoneelementfromeachiterableandreturnstheminatuple:
zip(['a', 'b', 'c'], (1, 2, 3)) =>
('a', 1), ('b', 2), ('c', 3)
Itdoesn’tconstructanin-memorylistandexhaustalltheinputiteratorsbeforereturning;insteadtuplesareconstructed
andreturnedonlyifthey’rerequested. (Thetechnicaltermforthisbehaviourislazyevaluation.)
This iterator is intended to be used with iterables that are all of the same length. If the iterables are of different
lengths,theresultingstreamwillbethesamelengthastheshortestiterable.
zip(['a', 'b'], (1, 2, 3)) =>
('a', 1), ('b', 2)
Youshouldavoiddoingthis,though,becauseanelementmaybetakenfromthelongeriteratorsanddiscarded. This
meansyoucan’tgoontousetheiteratorsfurtherbecauseyouriskskippingadiscardedelement.
6 The itertools module
Theitertoolsmodulecontainsanumberofcommonlyusediteratorsaswellasfunctionsforcombiningseveral
iterators. Thissectionwillintroducethemodule’scontentsbyshowingsmallexamples.
Themodule’sfunctionsfallintoafewbroadclasses:
• Functionsthatcreateanewiteratorbasedonanexistingiterator.
• Functionsfortreatinganiterator’selementsasfunctionarguments.
• Functionsforselectingportionsofaniterator’soutput.
• Afunctionforgroupinganiterator’soutput.
11

### 第12页

6.1 Creating new iterators
itertools.count(start, step)returnsaninfinitestreamofevenlyspacedvalues. Youcanoptionallysupply
thestartingnumber,whichdefaultsto0,andtheintervalbetweennumbers,whichdefaultsto1:
itertools.count() =>
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
itertools.count(10) =>
10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...
itertools.count(10, 5) =>
10, 15, 20, 25, 30, 35, 40, 45, 50, 55, ...
itertools.cycle(iter)savesacopyofthecontentsofaprovidediterableandreturnsanewiteratorthatreturns
itselementsfromfirsttolast. Thenewiteratorwillrepeattheseelementsinfinitely.
itertools.cycle([1, 2, 3, 4, 5]) =>
1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
itertools.repeat(elem, [n])returnstheprovidedelementntimes, orreturnstheelementendlesslyifnis
notprovided.
itertools.repeat('abc') =>
abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...
itertools.repeat('abc', 5) =>
abc, abc, abc, abc, abc
itertools.chain(iterA, iterB, ...) takes an arbitrary number of iterables as input, and returns all the
elements of the first iterator, then all the elements of the second, and so on, until all of the iterables have been
exhausted.
itertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>
a, b, c, 1, 2, 3
itertools.islice(iter, [start], stop, [step])returnsastreamthat’sasliceoftheiterator. Witha
singlestopargument,itwillreturnthefirststopelements. Ifyousupplyastartingindex,you’llgetstop-startelements,
andifyousupplyavalueforstep,elementswillbeskippedaccordingly. UnlikePython’sstringandlistslicing,you
can’tusenegativevaluesforstart,stop,orstep.
itertools.islice(range(10), 8) =>
0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
2, 4, 6
itertools.tee(iter, [n])replicatesaniterator;itreturnsnindependentiteratorsthatwillallreturnthecon-
tentsofthesourceiterator. Ifyoudon’tsupplyavalueforn,thedefaultis2. Replicatingiteratorsrequiressaving
someofthecontentsofthesourceiterator,sothiscanconsumesignificantmemoryiftheiteratorislargeandone
ofthenewiteratorsisconsumedmorethantheothers.
itertools.tee( itertools.count() ) =>
iterA, iterB
where iterA ->
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
and iterB ->
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
12

### 第13页

6.2 Calling functions on elements
The operator module contains a set of functions corresponding to Python’s operators. Some examples
are operator.add(a, b) (adds two values), operator.ne(a, b) (same as a != b), and operator.
attrgetter('id')(returnsacallablethatfetchesthe.idattribute).
itertools.starmap(func, iter)assumesthattheiterablewillreturnastreamoftuples,andcallsfuncusing
thesetuplesasthearguments:
itertools.starmap(os.path.join,
[('/bin', 'python'), ('/usr', 'bin', 'java'),
('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')])
=>
/bin/python, /usr/bin/java, /usr/bin/perl, /usr/bin/ruby
6.3 Selecting elements
Anothergroupoffunctionschoosesasubsetofaniterator’selementsbasedonapredicate.
itertools.filterfalse(predicate, iter)istheoppositeoffilter(),returningallelementsforwhich
thepredicatereturnsfalse:
itertools.filterfalse(is_even, itertools.count()) =>
1, 3, 5, 7, 9, 11, 13, 15, ...
itertools.takewhile(predicate, iter)returnselementsforaslongasthepredicatereturnstrue. Oncethe
predicatereturnsfalse,theiteratorwillsignaltheendofitsresults.
def less_than_10(x):
return x < 10
itertools.takewhile(less_than_10, itertools.count()) =>
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
itertools.takewhile(is_even, itertools.count()) =>
0
itertools.dropwhile(predicate, iter)discardselementswhilethepredicatereturnstrue,andthenreturns
therestoftheiterable’sresults.
itertools.dropwhile(less_than_10, itertools.count()) =>
10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...
itertools.dropwhile(is_even, itertools.count()) =>
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
itertools.compress(data, selectors)takestwoiteratorsandreturnsonlythoseelementsofdataforwhich
thecorrespondingelementofselectorsistrue,stoppingwhenevereitheroneisexhausted:
itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True]) =>
1, 2, 5
6.4 Combinatoric functions
The itertools.combinations(iterable, r) returns an iterator giving all possible r-tuple combinations of
theelementscontainediniterable.
itertools.combinations([1, 2, 3, 4, 5], 2) =>
(1, 2), (1, 3), (1, 4), (1, 5),
(continuesonnextpage)
13

### 第14页

(continuedfrompreviouspage)
(2, 3), (2, 4), (2, 5),
(3, 4), (3, 5),
(4, 5)
itertools.combinations([1, 2, 3, 4, 5], 3) =>
(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5),
(2, 3, 4), (2, 3, 5), (2, 4, 5),
(3, 4, 5)
Theelementswithineachtupleremaininthesameorderasiterablereturnedthem. Forexample, thenumber1is
alwaysbefore2, 3, 4, or5intheexamplesabove. Asimilarfunction, itertools.permutations(iterable,
r=None),removesthisconstraintontheorder,returningallpossiblearrangementsoflengthr:
itertools.permutations([1, 2, 3, 4, 5], 2) =>
(1, 2), (1, 3), (1, 4), (1, 5),
(2, 1), (2, 3), (2, 4), (2, 5),
(3, 1), (3, 2), (3, 4), (3, 5),
(4, 1), (4, 2), (4, 3), (4, 5),
(5, 1), (5, 2), (5, 3), (5, 4)
itertools.permutations([1, 2, 3, 4, 5]) =>
(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5),
...
(5, 4, 3, 2, 1)
Ifyoudon’tsupplyavalueforrthelengthoftheiterableisused,meaningthatalltheelementsarepermuted.
Notethatthesefunctionsproduceallofthepossiblecombinationsbypositionanddon’trequirethatthecontentsof
iterableareunique:
itertools.permutations('aba', 3) =>
('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'),
('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')
Theidenticaltuple('a', 'a', 'b')occurstwice,butthetwo‘a’stringscamefromdifferentpositions.
The itertools.combinations_with_replacement(iterable, r) function relaxes a different constraint:
elementscanberepeatedwithinasingletuple. Conceptuallyanelementisselectedforthefirstpositionofeachtuple
andthenisreplacedbeforethesecondelementisselected.
itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2) =>
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
(2, 2), (2, 3), (2, 4), (2, 5),
(3, 3), (3, 4), (3, 5),
(4, 4), (4, 5),
(5, 5)
6.5 Grouping elements
The last function I’ll discuss, itertools.groupby(iter, key_func=None), is the most complicated.
key_func(elem) is a function that can compute a key value for each element returned by the iterable. If you
don’tsupplyakeyfunction,thekeyissimplyeachelementitself.
groupby() collects all the consecutive elements from the underlying iterable that have the same key value, and
returnsastreamof2-tuplescontainingakeyvalueandaniteratorfortheelementswiththatkey.
city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
('Anchorage', 'AK'), ('Nome', 'AK'),
(continuesonnextpage)
14

### 第15页

(continuedfrompreviouspage)
('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
...
]
def get_state(city_state):
return city_state[1]
itertools.groupby(city_list, get_state) =>
('AL', iterator-1),
('AK', iterator-2),
('AZ', iterator-3), ...
where
iterator-1 =>
('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
iterator-2 =>
('Anchorage', 'AK'), ('Nome', 'AK')
iterator-3 =>
('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')
groupby()assumesthattheunderlyingiterable’scontentswillalreadybesortedbasedonthekey. Notethatthe
returnediteratorsalsousetheunderlyingiterable,soyouhavetoconsumetheresultsofiterator-1beforerequesting
iterator-2anditscorrespondingkey.
7 The functools module
Thefunctoolsmodulecontainssomehigher-orderfunctions. Ahigher-orderfunctiontakesoneormorefunc-
tions as input and returns a new function. The most useful tool in this module is the functools.partial()
function.
Forprogramswritteninafunctionalstyle,you’llsometimeswanttoconstructvariantsofexistingfunctionsthathave
someoftheparametersfilledin. ConsideraPythonfunctionf(a, b, c);youmaywishtocreateanewfunction
g(b, c) that’s equivalent to f(1, b, c); you’re filling in a value for one of f()’s parameters. This is called
“partialfunctionapplication”.
The constructor for partial() takes the arguments (function, arg1, arg2, ..., kwarg1=value1,
kwarg2=value2). The resulting object is callable, so you can just call it to invoke function with the filled-in
arguments.
Here’sasmallbutrealisticexample:
import functools
def log(message, subsystem):
"""Write the contents of 'message' to the specified subsystem."""
print('%s: %s' % (subsystem, message))
...
server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')
functools.reduce(func, iter, [initial_value]) cumulatively performs an operation on all the iter-
able’selementsand,therefore,can’tbeappliedtoinfiniteiterables. funcmustbeafunctionthattakestwoelements
and returns a single value. functools.reduce() takes the first two elements A and B returned by the iterator
andcalculatesfunc(A, B).Itthenrequeststhethirdelement, C,calculatesfunc(func(A, B), C),combines
this result with the fourth element returned, and continues until the iterable is exhausted. If the iterable returns
no values at all, a TypeError exception is raised. If the initial value is supplied, it’s used as a starting point and
func(initial_value, A)isthefirstcalculation.
15

### 第16页

>>> import operator, functools
>>> functools.reduce(operator.concat, ['A', 'BB', 'C'])
'ABBC'
>>> functools.reduce(operator.concat, [])
Traceback (most recent call last):
...
TypeError: reduce() of empty sequence with no initial value
>>> functools.reduce(operator.mul, [1, 2, 3], 1)
6
>>> functools.reduce(operator.mul, [], 1)
1
Ifyouuseoperator.add()withfunctools.reduce(),you’lladdupalltheelementsoftheiterable. Thiscase
issocommonthatthere’saspecialbuilt-incalledsum()tocomputeit:
>>> import functools, operator
>>> functools.reduce(operator.add, [1, 2, 3, 4], 0)
10
>>> sum([1, 2, 3, 4])
10
>>> sum([])
0
Formanyusesoffunctools.reduce(),though,itcanbeclearertojustwritetheobviousforloop:
import functools
# Instead of:
product = functools.reduce(operator.mul, [1, 2, 3], 1)
# You can write:
product = 1
for i in [1, 2, 3]:
product *= i
Arelatedfunctionisitertools.accumulate(iterable, func=operator.add). Itperformsthesamecal-
culation,butinsteadofreturningonlythefinalresult,accumulate()returnsaniteratorthatalsoyieldseachpartial
result:
itertools.accumulate([1, 2, 3, 4, 5]) =>
1, 3, 6, 10, 15
itertools.accumulate([1, 2, 3, 4, 5], operator.mul) =>
1, 2, 6, 24, 120
7.1 The operator module
The operator module was mentioned earlier. It contains a set of functions corresponding to Python’s operators.
These functions are often useful in functional-style code because they save you from writing trivial functions that
performasingleoperation.
Someofthefunctionsinthismoduleare:
• Mathoperations: add(),sub(),mul(),floordiv(),abs(),…
• Logicaloperations: not_(),truth().
• Bitwiseoperations: and_(),or_(),invert().
• Comparisons: eq(),ne(),lt(),le(),gt(),andge().
• Objectidentity: is_(),is_not().
16

### 第17页

Consulttheoperatormodule’sdocumentationforacompletelist.
8 Small functions and the lambda expression
When writing functional-style programs, you’ll often need little functions that act as predicates or that combine
elementsinsomeway.
Ifthere’saPythonbuilt-inoramodulefunctionthat’ssuitable,youdon’tneedtodefineanewfunctionatall:
stripped_lines = [line.strip() for line in lines]
existing_files = filter(os.path.exists, file_list)
Ifthefunctionyouneeddoesn’texist,youneedtowriteit. Onewaytowritesmallfunctionsistousethelambda
expression. lambda takes a number ofparameters andan expressioncombining theseparameters, and createsan
anonymousfunctionthatreturnsthevalueoftheexpression:
adder = lambda x, y: x+y
print_assign = lambda name, value: name + '=' + str(value)
Analternativeistojustusethedefstatementanddefineafunctionintheusualway:
def adder(x, y):
return x + y
def print_assign(name, value):
return name + '=' + str(value)
Whichalternativeispreferable? That’sastylequestion;myusualcourseistoavoidusinglambda.
One reason for my preference is that lambda is quite limited in the functions it can define. The result has to be
computableasasingleexpression, whichmeansyoucan’thavemultiwayif... elif... elsecomparisonsor
try... exceptstatements. Ifyoutrytodotoomuchinalambdastatement,you’llendupwithanoverlycom-
plicatedexpressionthat’shardtoread. Quick,what’sthefollowingcodedoing?
import functools
total = functools.reduce(lambda a, b: (0, a[1] + b[1]), items)[1]
Youcanfigureitout,butittakestimetodisentangletheexpressiontofigureoutwhat’sgoingon. Usingashortnested
defstatementsmakesthingsalittlebitbetter:
import functools
def combine(a, b):
return 0, a[1] + b[1]
total = functools.reduce(combine, items)[1]
ButitwouldbebestofallifIhadsimplyusedaforloop:
total = 0
for a, b in items:
total += b
Orthesum()built-inandageneratorexpression:
total = sum(b for a, b in items)
Manyusesoffunctools.reduce()areclearerwhenwrittenasforloops.
FredrikLundhoncesuggestedthefollowingsetofrulesforrefactoringusesoflambda:
17

### 第18页

1. Writealambdafunction.
2. Writeacommentexplainingwhattheheckthatlambdadoes.
3. Studythecommentforawhile,andthinkofanamethatcapturestheessenceofthecomment.
4. Convertthelambdatoadefstatement,usingthatname.
5. Removethecomment.
Ireallyliketheserules,butyou’refreetodisagreeaboutwhetherthislambda-freestyleisbetter.
9 Revision History and Acknowledgements
Theauthorwouldliketothankthefollowingpeopleforofferingsuggestions,correctionsandassistancewithvarious
draftsofthisarticle: IanBicking,NickCoghlan,NickEfford,RaymondHettinger,JimJewett,MikeKrell,Leandro
Lameiro,JussiSalmela,CollinWinter,BlakeWinton.
Version0.1: postedJune302006.
Version0.11: postedJuly12006. Typofixes.
Version0.2: postedJuly102006. Mergedgenexpandlistcompsectionsintoone. Typofixes.
Version0.21: Addedmorereferencessuggestedonthetutormailinglist.
Version0.30:AddsasectiononthefunctionalmodulewrittenbyCollinWinter;addsshortsectionontheoperator
module;afewotheredits.
10 References
10.1 General
Structure and Interpretation of Computer Programs, by Harold Abelson and Gerald Jay Sussman with Julie
Sussman. The book can be found at https://mitpress.mit.edu/sicp. In this classic textbook of computer science,
chapters2and3discusstheuseofsequencesandstreamstoorganizethedataflowinsideaprogram. Thebookuses
Schemeforitsexamples,butmanyofthedesignapproachesdescribedinthesechaptersareapplicabletofunctional-
stylePythoncode.
https://defmacro.org/2006/06/19/fp.html:AgeneralintroductiontofunctionalprogrammingthatusesJavaexamples
andhasalengthyhistoricalintroduction.
https://en.wikipedia.org/wiki/Functional_programming: General Wikipedia entry describing functional program-
ming.
https://en.wikipedia.org/wiki/Coroutine: Entryforcoroutines.
https://en.wikipedia.org/wiki/Partial_application: Entryfortheconceptofpartialfunctionapplication.
https://en.wikipedia.org/wiki/Currying: Entryfortheconceptofcurrying.
10.2 Python-specific
https://gnosis.cx/TPiP/: ThefirstchapterofDavidMertz’sbookTextProcessinginPythondiscussesfunctionalpro-
grammingfortextprocessing,inthesectiontitled“UtilizingHigher-OrderFunctionsinTextProcessing”.
Mertzalsowrotea3-partseriesofarticlesonfunctionalprogrammingforIBM’sDeveloperWorkssite; seepart1,
part2,andpart3,
10.3 Python documentation
Documentationfortheitertoolsmodule.
Documentationforthefunctoolsmodule.
Documentationfortheoperatormodule.
18

### 第19页

PEP289: “GeneratorExpressions”
PEP342: “CoroutinesviaEnhancedGenerators”describesthenewgeneratorfeaturesinPython2.5.
19

### 第20页

Index
P
Python Enhancement Proposals
PEP 289,19
PEP 342,9,19
20

