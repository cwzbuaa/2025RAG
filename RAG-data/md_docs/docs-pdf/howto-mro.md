### 第1页

The Python 2.3 Method Resolution
Order
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Thebeginning 2
2 TheC3MethodResolutionOrder 3
3 Examples 4
4 BadMethodResolutionOrders 6
5 Theend 9
6 Resources 10
(cid:174) Note
This is a historical document, provided as an appendix to the official documentation. The Method Resolution
OrderdiscussedherewasintroducedinPython2.3,butitisstillusedinlaterversions–includingPython3.
ByMicheleSimionato.
Abstract
ThisdocumentisintendedforPythonprogrammerswhowanttounderstandtheC3MethodReso-
lutionOrderusedinPython2.3. Althoughitisnotintendedfornewbies,itisquitepedagogicalwith
many worked out examples. I am not aware of other publicly available documents with the same
scope,thereforeitshouldbeuseful.
Disclaimer:
IdonatethisdocumenttothePythonSoftwareFoundation,underthePython2.3license. Asusualinthese
circumstances,Iwarnthereaderthatwhatfollowsshouldbecorrect,butIdon’tgiveanywarranty. Use
itatyourownriskandperil!
Acknowledgments:
AllthepeopleofthePythonmailinglistwhosentmetheirsupport. PaulFoleywhopointedoutvarious
imprecisionsandmademetoaddthepartonlocalprecedenceordering. DavidGoodgerforhelpwiththe
1

### 第2页

formattinginreStructuredText. DavidMertzforhelpwiththeediting. Finally, GuidovanRossumwho
enthusiasticallyaddedthisdocumenttotheofficialPython2.3home-page.
1 The beginning
Felixquipotuitrerumcognoscerecausas–Virgilius
Everything started with a post by Samuele Pedroni to the Python development mailing list1. In his post, Samuele
showed that the Python 2.2 method resolution order is not monotonic and he proposed to replace it with the C3
methodresolutionorder. GuidoagreedwithhisargumentsandthereforenowPython2.3usesC3. TheC3method
itselfhasnothingtodowithPython,sinceitwasinventedbypeopleworkingonDylananditisdescribedinapaper
intendedforlispers2. Thepresentpapergivesa(hopefully)readablediscussionoftheC3algorithmforPythonistas
whowanttounderstandthereasonsforthechange.
Firstofall, letmepointoutthatwhatIamgoingtosayonlyappliestothenewstyleclassesintroducedinPython
2.2: classicclassesmaintaintheiroldmethodresolutionorder,depthfirstandthenlefttoright. Therefore,thereisno
breakingofoldcodeforclassicclasses;andevenifinprincipletherecouldbebreakingofcodeforPython2.2new
style classes, in practice the cases in which the C3 resolution order differs from the Python 2.2 method resolution
orderaresorarethatnorealbreakingofcodeisexpected. Therefore:
Don’tbescared!
Moreover,unlessyoumakestronguseofmultipleinheritanceandyouhavenon-trivialhierarchies,youdon’tneed
tounderstandtheC3algorithm,andyoucaneasilyskipthispaper. Ontheotherhand,ifyoureallywanttoknow
howmultipleinheritanceworks,thenthispaperisforyou. Thegoodnewsisthatthingsarenotascomplicatedas
youmightexpect.
Letmebeginwithsomebasicdefinitions.
1) GivenaclassCinacomplicatedmultipleinheritancehierarchy,itisanon-trivialtasktospecifytheorderin
whichmethodsareoverridden,i.e. tospecifytheorderoftheancestorsofC.
2) ThelistoftheancestorsofaclassC,includingtheclassitself,orderedfromthenearestancestortothefurthest,
iscalledtheclassprecedencelistorthelinearizationofC.
3) TheMethodResolutionOrder(MRO)isthesetofrulesthatconstructthelinearization. InthePythonliterature,
theidiom“theMROofC”isalsousedasasynonymousforthelinearizationoftheclassC.
4) Forinstance,inthecaseofsingleinheritancehierarchy,ifCisasubclassofC1,andC1isasubclassofC2,
thenthelinearizationofCissimplythelist[C,C1,C2]. However,withmultipleinheritancehierarchies,the
constructionofthelinearizationismorecumbersome,sinceitismoredifficulttoconstructalinearizationthat
respectslocalprecedenceorderingandmonotonicity.
5) Iwilldiscussthelocalprecedenceorderinglater,butIcangivethedefinitionofmonotonicityhere. AMRO
ismonotonicwhenthefollowingistrue: ifC1precedesC2inthelinearizationofC,thenC1precedesC2inthe
linearizationofanysubclass ofC. Otherwise, theinnocuousoperationofderivinga newclasscouldchange
theresolutionorderofmethods,potentiallyintroducingverysubtlebugs. Exampleswherethishappenswill
beshownlater.
6) Notallclassesadmitalinearization. Therearecases, incomplicatedhierarchies, whereitisnotpossibleto
deriveaclasssuchthatitslinearizationrespectsallthedesiredproperties.
HereIgiveanexampleofthissituation. Considerthehierarchy
>>> O = object
>>> class X(O): pass
>>> class Y(O): pass
>>> class A(X,Y): pass
>>> class B(Y,X): pass
1Thethreadonpython-devstartedbySamuelePedroni:https://mail.python.org/pipermail/python-dev/2002-October/029035.html
2ThepaperAMonotonicSuperclassLinearizationforDylan:https://doi.org/10.1145/236337.236343
2

### 第3页

whichcanberepresentedwiththefollowinginheritancegraph,whereIhavedenotedwithOtheobjectclass,which
isthebeginningofanyhierarchyfornewstyleclasses:
-----------
| |
| O |
| / \ |
- X Y /
| / | /
| / |/
A B
\ /
?
Inthiscase,itisnotpossibletoderiveanewclassCfromAandB,sinceXprecedesYinA,butYprecedesXinB,
thereforethemethodresolutionorderwouldbeambiguousinC.
Python2.3raisesanexceptioninthissituation(TypeError: MROconflictamongbasesY,X)forbiddingthenaive
programmerfromcreatingambiguoushierarchies. Python2.2insteaddoesnotraiseanexception,butchoosesanad
hocordering(CABXYOinthiscase).
2 The C3 Method Resolution Order
Let me introduce a few simple notations which will be useful for the following discussion. I will use the shortcut
notation:
C1 C2 ... CN
toindicatethelistofclasses[C1,C2,…,CN].
Theheadofthelistisitsfirstelement:
head = C1
whereasthetailistherestofthelist:
tail = C2 ... CN.
Ishallalsousethenotation:
C + (C1 C2 ... CN) = C C1 C2 ... CN
todenotethesumofthelists[C]+[C1,C2,…,CN].
NowIcanexplainhowtheMROworksinPython2.3.
ConsideraclassCinamultipleinheritancehierarchy,withCinheritingfromthebaseclassesB1,B2,…,BN.We
wanttocomputethelinearizationL[C]oftheclassC.Theruleisthefollowing:
thelinearizationofCisthesumofCplusthemergeofthelinearizationsoftheparentsandthelistofthe
parents.
Insymbolicnotation:
L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)
Inparticular,ifCistheobjectclass,whichhasnoparents,thelinearizationistrivial:
L[object] = object.
However,ingeneralonehastocomputethemergeaccordingtothefollowingprescription:
3

### 第4页

taketheheadofthefirstlist,i.eL[B1][0];ifthisheadisnotinthetailofanyoftheotherlists,thenaddit
tothelinearizationofCandremoveitfromthelistsinthemerge,otherwiselookattheheadofthenextlist
andtakeit,ifitisagoodhead. Thenrepeattheoperationuntilalltheclassareremovedoritisimpossible
tofindgoodheads. Inthiscase,itisimpossibletoconstructthemerge,Python2.3willrefusetocreatethe
classCandwillraiseanexception.
Thisprescriptionensuresthatthemergeoperationpreservestheordering,iftheorderingcanbepreserved. Onthe
otherhand,iftheordercannotbepreserved(asintheexampleofseriousorderdisagreementdiscussedabove)then
themergecannotbecomputed.
ThecomputationofthemergeistrivialifChasonlyoneparent(singleinheritance);inthiscase:
L[C(B)] = C + merge(L[B],B) = C + L[B]
However,inthecaseofmultipleinheritancethingsaremorecumbersomeandIdon’texpectyoucanunderstandthe
rulewithoutacoupleofexamples;-)
3 Examples
Firstexample. Considerthefollowinghierarchy:
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(D,E): pass
>>> class A(B,C): pass
Inthiscasetheinheritancegraphcanbedrawnas:
6
---
Level 3 | O | (more general)
/ --- \
/ | \ |
/ | \ |
/ | \ |
--- --- --- |
Level 2 3 | D | 4| E | | F | 5 |
--- --- --- |
\ \ _ / | |
\ / \ _ | |
\ / \ | |
--- --- |
Level 1 1 | B | | C | 2 |
--- --- |
\ / |
\ / \ /
---
Level 0 0 | A | (more specialized)
---
ThelinearizationsofO,D,EandFaretrivial:
L[O] = O
L[D] = D O
L[E] = E O
L[F] = F O
4

### 第5页

ThelinearizationofBcanbecomputedas:
L[B] = B + merge(DO, EO, DE)
WeseethatDisagoodhead,thereforewetakeitandwearereducedtocomputemerge(O,EO,E).NowOisnot
a good head, since it is in the tail of the sequence EO. In this case the rule says that we have to skip to the next
sequence. ThenweseethatEisagoodhead;wetakeitandwearereducedtocomputemerge(O,O)whichgives
O.Therefore:
L[B] = B D E O
Usingthesameprocedureonefinds:
L[C] = C + merge(DO,FO,DF)
= C + D + merge(O,FO,F)
= C + D + F + merge(O,O)
= C D F O
Nowwecancompute:
L[A] = A + merge(BDEO,CDFO,BC)
= A + B + merge(DEO,CDFO,C)
= A + B + C + merge(DEO,DFO)
= A + B + C + D + merge(EO,FO)
= A + B + C + D + E + merge(O,FO)
= A + B + C + D + E + F + merge(O,O)
= A B C D E F O
Inthisexample,thelinearizationisorderedinaprettynicewayaccordingtotheinheritancelevel,inthesensethat
lowerlevels(i.e. morespecializedclasses)havehigherprecedence(seetheinheritancegraph). However,thisisnot
thegeneralcase.
Ileaveasanexerciseforthereadertocomputethelinearizationformysecondexample:
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(E,D): pass
>>> class A(B,C): pass
TheonlydifferencewiththepreviousexampleisthechangeB(D,E)–>B(E,D);howeverevensuchalittlemodifi-
cationcompletelychangestheorderingofthehierarchy:
6
---
Level 3 | O |
/ --- \
/ | \
/ | \
/ | \
--- --- ---
Level 2 2 | E | 4 | D | | F | 5
--- --- ---
\ / \ /
\ / \ /
\ / \ /
--- ---
(continuesonnextpage)
5

### 第6页

(continuedfrompreviouspage)
Level 1 1 | B | | C | 3
--- ---
\ /
\ /
---
Level 0 0 | A |
---
NoticethattheclassE,whichisinthesecondlevelofthehierarchy,precedestheclassC,whichisinthefirstlevel
ofthehierarchy,i.e. EismorespecializedthanC,evenifitisinahigherlevel.
AlazyprogrammercanobtaintheMROdirectlyfromPython2.2,sinceinthiscaseitcoincideswiththePython2.3
linearization. Itisenoughtoinvokethemro()methodofclassA:
>>> A.mro()
[<class 'A'>, <class 'B'>, <class 'E'>,
<class 'C'>, <class 'D'>, <class 'F'>,
<class 'object'>]
Finally, let me consider the example discussed in the first section, involving a serious order disagreement. In this
case,itisstraightforwardtocomputethelinearizationsofO,X,Y,AandB:
L[O] = 0
L[X] = X O
L[Y] = Y O
L[A] = A X Y O
L[B] = B Y X O
However,itisimpossibletocomputethelinearizationforaclassCthatinheritsfromAandB:
L[C] = C + merge(AXYO, BYXO, AB)
= C + A + merge(XYO, BYXO, B)
= C + A + B + merge(XYO, YXO)
AtthispointwecannotmergethelistsXYOandYXO,sinceXisinthetailofYXOwhereasYisinthetailofXYO:
thereforetherearenogoodheadsandtheC3algorithmstops. Python2.3raisesanerrorandrefusestocreatethe
classC.
4 Bad Method Resolution Orders
AMROisbad whenitbreakssuchfundamentalpropertiesaslocalprecedenceorderingandmonotonicity. Inthis
section,IwillshowthatboththeMROforclassicclassesandtheMROfornewstyleclassesinPython2.2arebad.
Itiseasiertostartwiththelocalprecedenceordering. Considerthefollowingexample:
>>> F=type('Food',(),{'remember2buy':'spam'})
>>> E=type('Eggs',(F,),{'remember2buy':'eggs'})
>>> G=type('GoodFood',(F,E),{}) # under Python 2.3 this is an error!
withinheritancediagram
O
|
(buy spam) F
| \
| E (buy eggs)
| /
(continuesonnextpage)
6

### 第7页

(continuedfrompreviouspage)
G
(buy eggs or spam ?)
WeseethatclassGinheritsfromFandE,withFbeforeE:thereforewewouldexpecttheattributeG.remember2buy
tobeinheritedbyF.remember2buyandnotbyE.remember2buy: neverthelessPython2.2gives
>>> G.remember2buy
'eggs'
Thisisabreakingoflocalprecedenceorderingsincetheorderinthelocalprecedencelist,i.e. thelistoftheparents
ofG,isnotpreservedinthePython2.2linearizationofG:
L[G,P22]= G E F object # F *follows* E
OnecouldarguethatthereasonwhyFfollowsEinthePython2.2linearizationisthatFislessspecializedthanE,
sinceFisthesuperclassofE;neverthelessthebreakingoflocalprecedenceorderingisquitenon-intuitiveanderror
prone. Thisisparticularlytruesinceitisadifferentfromoldstyleclasses:
>>> class F: remember2buy='spam'
>>> class E(F): remember2buy='eggs'
>>> class G(F,E): pass
>>> G.remember2buy
'spam'
InthiscasetheMROisGFEFandthelocalprecedenceorderingispreserved.
Asageneralrule,hierarchiessuchasthepreviousoneshouldbeavoided,sinceitisunclearifFshouldoverrideE
orvice-versa. Python2.3solvestheambiguitybyraisinganexceptioninthecreationofclassG,effectivelystopping
theprogrammerfromgeneratingambiguoushierarchies. ThereasonforthatisthattheC3algorithmfailswhenthe
merge:
merge(FO,EFO,FE)
cannotbecomputed,becauseFisinthetailofEFOandEisinthetailofFE.
Therealsolutionistodesignanon-ambiguoushierarchy,i.e. toderiveGfromEandF(themorespecificfirst)and
notfromFandE;inthiscasetheMROisGEFwithoutanydoubt.
O
|
F (spam)
/ |
(eggs) E |
\ |
G
(eggs, no doubt)
Python2.3forcestheprogrammertowritegoodhierarchies(or,atleast,lesserror-proneones).
Onarelatednote,letmepointoutthatthePython2.3algorithmissmartenoughtorecognizeobviousmistakes,as
theduplicationofclassesinthelistofparents:
>>> class A(object): pass
>>> class C(A,A): pass # error
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: duplicate base class A
7

### 第8页

Python2.2(bothforclassicclassesandnewstyleclasses)inthissituation,wouldnotraiseanyexception.
Finally,Iwouldliketopointouttwolessonswehavelearnedfromthisexample:
1. despitethename,theMROdeterminestheresolutionorderofattributes,notonlyofmethods;
2. thedefaultfoodforPythonistasisspam! (butyoualreadyknewthat;-)
Havingdiscussedtheissueoflocalprecedenceordering,letmenowconsidertheissueofmonotonicity. Mygoalis
toshowthatneithertheMROforclassicclassesnorthatforPython2.2newstyleclassesismonotonic.
To prove that the MRO for classic classes is non-monotonic is rather trivial, it is enough to look at the diamond
diagram:
C
/ \
/ \
A B
\ /
\ /
D
Oneeasilydiscernstheinconsistency:
L[B,P21] = B C # B precedes C : B's methods win
L[D,P21] = D A C B C # B follows C : C's methods win!
Ontheotherhand,therearenoproblemswiththePython2.2and2.3MROs,theygiveboth:
L[D] = D A B C
Guido points out in his essay3 that the classic MRO is not so bad in practice, since one can typically avoids dia-
monds for classic classes. But all new style classes inherit from object, therefore diamonds are unavoidable and
inconsistenciesshowsupineverymultipleinheritancegraph.
TheMROofPython2.2makesbreakingmonotonicitydifficult,butnotimpossible. Thefollowingexample,originally
providedbySamuelePedroni,showsthattheMROofPython2.2isnon-monotonic:
>>> class A(object): pass
>>> class B(object): pass
>>> class C(object): pass
>>> class D(object): pass
>>> class E(object): pass
>>> class K1(A,B,C): pass
>>> class K2(D,B,E): pass
>>> class K3(D,A): pass
>>> class Z(K1,K2,K3): pass
HerearethelinearizationsaccordingtotheC3MRO(thereadershouldverifytheselinearizationsasanexerciseand
drawtheinheritancediagram;-)
L[A] = A O
L[B] = B O
L[C] = C O
L[D] = D O
L[E] = E O
L[K1]= K1 A B C O
L[K2]= K2 D B E O
L[K3]= K3 D A O
L[Z] = Z K1 K2 K3 D A B C E O
3GuidovanRossum’sessay,UnifyingtypesandclassesinPython2.2:https://web.archive.org/web/20140210194412/http://www.python.org/
download/releases/2.2.2/descrintro
8

### 第9页

Python2.2givesexactlythesamelinearizationsforA,B,C,D,E,K1,K2andK3,butadifferentlinearizationforZ:
L[Z,P22] = Z K1 K3 A K2 D B C E O
Itisclearthatthislinearizationiswrong,sinceAcomesbeforeDwhereasinthelinearizationofK3Acomesafter
D.Inotherwords,inK3methodsderivedbyDoverridemethodsderivedbyA,butinZ,whichstillisasubclassof
K3,methodsderivedbyAoverridemethodsderivedbyD!Thisisaviolationofmonotonicity. Moreover,thePython
2.2linearizationofZisalsoinconsistentwithlocalprecedenceordering,sincethelocalprecedencelistoftheclass
Zis[K1,K2,K3](K2precedesK3),whereasinthelinearizationofZK2followsK3. Theseproblemsexplainwhy
the2.2rulehasbeendismissedinfavoroftheC3rule.
5 The end
Thissectionisfortheimpatientreader,whoskippedalltheprevioussectionsandjumpedimmediatelytotheend. This
sectionisforthelazyprogrammertoo,whodidn’twanttoexerciseher/hisbrain. Finally,itisfortheprogrammerwith
somehubris,otherwises/hewouldnotbereadingapaperontheC3methodresolutionorderinmultipleinheritance
hierarchies;-)Thesethreevirtuestakenalltogether(andnotseparately)deserveaprize: theprizeisashortPython
2.2scriptthatallowsyoutocomputethe2.3MROwithoutrisktoyourbrain. Simplychangethelastlinetoplay
withthevariousexamplesIhavediscussedinthispaper.:
#<mro.py>
"""C3 algorithm by Samuele Pedroni (with readability enhanced by me)."""
class __metaclass__(type):
"All classes are metamagically modified to be nicely printed"
__repr__ = lambda cls: cls.__name__
class ex_2:
"Serious order disagreement" #From Guido
class O: pass
class X(O): pass
class Y(O): pass
class A(X,Y): pass
class B(Y,X): pass
try:
class Z(A,B): pass #creates Z(A,B) in Python 2.2
except TypeError:
pass # Z(A,B) cannot be created in Python 2.3
class ex_5:
"My first example"
class O: pass
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass
class ex_6:
"My second example"
class O: pass
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
(continuesonnextpage)
9

### 第10页

(continuedfrompreviouspage)
class B(E,D): pass
class A(B,C): pass
class ex_9:
"Difference between Python 2.2 MRO and C3" #From Samuele
class O: pass
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A): pass
class Z(K1,K2,K3): pass
def merge(seqs):
print '\n\nCPL[%s]=%s' % (seqs[0][0],seqs),
res = []; i=0
while 1:
nonemptyseqs=[seq for seq in seqs if seq]
if not nonemptyseqs: return res
i+=1; print '\n',i,'round: candidates...',
for seq in nonemptyseqs: # find merge candidates among seq heads
cand = seq[0]; print ' ',cand,
nothead=[s for s in nonemptyseqs if cand in s[1:]]
if nothead: cand=None #reject candidate
else: break
if not cand: raise "Inconsistent hierarchy"
res.append(cand)
for seq in nonemptyseqs: # remove cand
if seq[0] == cand: del seq[0]
def mro(C):
"Compute the class precedence list (mro) according to C3"
return merge([[C]]+map(mro,C.__bases__)+[list(C.__bases__)])
def print_mro(C):
print '\nMRO[%s]=%s' % (C,mro(C))
print '\nP22 MRO[%s]=%s' % (C,C.mro())
print_mro(ex_9.Z)
#</mro.py>
That’sallfolks,
enjoy!
6 Resources
10

