### 第1页

Enum HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Programmaticaccesstoenumerationmembersandtheirattributes 5
2 Duplicatingenummembersandvalues 5
3 Ensuringuniqueenumerationvalues 6
4 Usingautomaticvalues 6
5 Iteration 7
6 Comparisons 7
7 Allowedmembersandattributesofenumerations 8
8 RestrictedEnumsubclassing 9
9 Dataclasssupport 9
10 Pickling 10
11 FunctionalAPI 10
12 DerivedEnumerations 12
12.1 IntEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
12.2 StrEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
12.3 IntFlag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
12.4 Flag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
12.5 Others . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
13 Whentouse__new__()vs. __init__() 16
13.1 FinerPoints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
14 HowareEnumsandFlagsdifferent? 20
14.1 EnumClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
14.2 FlagClasses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
14.3 EnumMembers(akainstances) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
14.4 FlagMembers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
1

### 第2页

15 EnumCookbook 21
15.1 Omittingvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
15.2 OrderedEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
15.3 DuplicateFreeEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
15.4 MultiValueEnum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
15.5 Planet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
15.6 TimePeriod . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
16 SubclassingEnumType 26
AnEnumisasetofsymbolicnamesboundtouniquevalues. Theyaresimilartoglobalvariables, buttheyoffera
moreusefulrepr(),grouping,type-safety,andafewotherfeatures.
Theyaremostusefulwhenyouhaveavariablethatcantakeoneofalimitedselectionofvalues. Forexample,the
daysoftheweek:
>>> from enum import Enum
>>> class Weekday(Enum):
... MONDAY = 1
... TUESDAY = 2
... WEDNESDAY = 3
... THURSDAY = 4
... FRIDAY = 5
... SATURDAY = 6
... SUNDAY = 7
OrperhapstheRGBprimarycolors:
>>> from enum import Enum
>>> class Color(Enum):
... RED = 1
... GREEN = 2
... BLUE = 3
Asyoucansee,creatinganEnumisassimpleaswritingaclassthatinheritsfromEnumitself.
(cid:174) Note
CaseofEnumMembers
BecauseEnumsareusedtorepresentconstants,andtohelpavoidissueswithnameclashesbetweenmixin-class
methods/attributesandenumnames,westronglyrecommendusingUPPER_CASEnamesformembers,andwill
beusingthatstyleinourexamples.
Dependingonthenatureoftheenumamember’svaluemayormaynotbeimportant,buteitherwaythatvaluecan
beusedtogetthecorrespondingmember:
>>> Weekday(3)
<Weekday.WEDNESDAY: 3>
Asyoucansee,therepr()ofamembershowstheenumname,themembername,andthevalue. Thestr()ofa
membershowsonlytheenumnameandmembername:
>>> print(Weekday.THURSDAY)
Weekday.THURSDAY
Thetypeofanenumerationmemberistheenumitbelongsto:
2

### 第3页

>>> type(Weekday.MONDAY)
<enum 'Weekday'>
>>> isinstance(Weekday.FRIDAY, Weekday)
True
Enummembershaveanattributethatcontainsjusttheirname:
>>> print(Weekday.TUESDAY.name)
TUESDAY
Likewise,theyhaveanattributefortheirvalue:
>>> Weekday.WEDNESDAY.value
3
Unlikemanylanguagesthattreatenumerationssolelyasname/valuepairs,PythonEnumscanhavebehavioradded.
Forexample,datetime.datehastwomethodsforreturningtheweekday: weekday()andisoweekday(). The
differenceisthatoneofthemcountsfrom0-6andtheotherfrom1-7. Ratherthankeeptrackofthatourselveswe
canaddamethodtotheWeekdayenumtoextractthedayfromthedateinstanceandreturnthematchingenum
member:
@classmethod
def from_date(cls, date):
return cls(date.isoweekday())
ThecompleteWeekdayenumnowlookslikethis:
>>> class Weekday(Enum):
... MONDAY = 1
... TUESDAY = 2
... WEDNESDAY = 3
... THURSDAY = 4
... FRIDAY = 5
... SATURDAY = 6
... SUNDAY = 7
... #
... @classmethod
... def from_date(cls, date):
... return cls(date.isoweekday())
Nowwecanfindoutwhattodayis! Observe:
>>> from datetime import date
>>> Weekday.from_date(date.today())
<Weekday.TUESDAY: 2>
Ofcourse,ifyou’rereadingthisonsomeotherday,you’llseethatdayinstead.
ThisWeekdayenumisgreatifourvariableonlyneedsoneday,butwhatifweneedseveral? Maybewe’rewritinga
functiontoplotchoresduringaweek,anddon’twanttousealist–wecoulduseadifferenttypeofEnum:
>>> from enum import Flag
>>> class Weekday(Flag):
... MONDAY = 1
... TUESDAY = 2
... WEDNESDAY = 4
... THURSDAY = 8
... FRIDAY = 16
(continuesonnextpage)
3

### 第4页

(continuedfrompreviouspage)
... SATURDAY = 32
... SUNDAY = 64
We’vechangedtwothings: we’reinheritedfromFlag,andthevaluesareallpowersof2.
JustliketheoriginalWeekdayenumabove,wecanhaveasingleselection:
>>> first_week_day = Weekday.MONDAY
>>> first_week_day
<Weekday.MONDAY: 1>
ButFlagalsoallowsustocombineseveralmembersintoasinglevariable:
>>> weekend = Weekday.SATURDAY | Weekday.SUNDAY
>>> weekend
<Weekday.SATURDAY|SUNDAY: 96>
YoucaneveniterateoveraFlagvariable:
>>> for day in weekend:
... print(day)
Weekday.SATURDAY
Weekday.SUNDAY
Okay,let’sgetsomechoressetup:
>>> chores_for_ethan = {
... 'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
... 'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
... 'answer SO questions': Weekday.SATURDAY,
... }
Andafunctiontodisplaythechoresforagivenday:
>>> def show_chores(chores, day):
... for chore, days in chores.items():
... if day in days:
... print(chore)
...
>>> show_chores(chores_for_ethan, Weekday.SATURDAY)
answer SO questions
Incaseswheretheactualvaluesofthemembersdonotmatter,youcansaveyourselfsomeworkanduseauto()
forthevalues:
>>> from enum import auto
>>> class Weekday(Flag):
... MONDAY = auto()
... TUESDAY = auto()
... WEDNESDAY = auto()
... THURSDAY = auto()
... FRIDAY = auto()
... SATURDAY = auto()
... SUNDAY = auto()
... WEEKEND = SATURDAY | SUNDAY
4

### 第5页

1 Programmatic access to enumeration members and their at-
tributes
Sometimesit’susefultoaccessmembersinenumerationsprogrammatically(i.e. situationswhereColor.REDwon’t
dobecausetheexactcolorisnotknownatprogram-writingtime). Enumallowssuchaccess:
>>> Color(1)
<Color.RED: 1>
>>> Color(3)
<Color.BLUE: 3>
Ifyouwanttoaccessenummembersbyname,useitemaccess:
>>> Color['RED']
<Color.RED: 1>
>>> Color['GREEN']
<Color.GREEN: 2>
Ifyouhaveanenummemberandneeditsnameorvalue:
>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1
2 Duplicating enum members and values
Havingtwoenummemberswiththesamenameisinvalid:
>>> class Shape(Enum):
... SQUARE = 2
... SQUARE = 3
...
Traceback (most recent call last):
...
TypeError: 'SQUARE' already defined as 2
However,anenummembercanhaveothernamesassociatedwithit. GiventwoentriesAandBwiththesamevalue
(and A definedfirst), B is an alias forthe member A. By-value lookup ofthe value of A will return the member A.
By-namelookupofAwillreturnthememberA.By-namelookupofBwillalsoreturnthememberA:
>>> class Shape(Enum):
... SQUARE = 2
... DIAMOND = 1
... CIRCLE = 3
... ALIAS_FOR_SQUARE = 2
...
>>> Shape.SQUARE
<Shape.SQUARE: 2>
>>> Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
>>> Shape(2)
<Shape.SQUARE: 2>
5

### 第6页

(cid:174) Note
Attemptingtocreateamemberwiththesamenameasanalreadydefinedattribute(anothermember,amethod,
etc.) orattemptingtocreateanattributewiththesamenameasamemberisnotallowed.
3 Ensuring unique enumeration values
Bydefault,enumerationsallowmultiplenamesasaliasesforthesamevalue. Whenthisbehaviorisn’tdesired,you
canusetheunique()decorator:
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
... ONE = 1
... TWO = 2
... THREE = 3
... FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
4 Using automatic values
Iftheexactvalueisunimportantyoucanuseauto:
>>> from enum import Enum, auto
>>> class Color(Enum):
... RED = auto()
... BLUE = auto()
... GREEN = auto()
...
>>> [member.value for member in Color]
[1, 2, 3]
Thevaluesarechosenby_generate_next_value_(),whichcanbeoverridden:
>>> class AutoName(Enum):
... @staticmethod
... def _generate_next_value_(name, start, count, last_values):
... return name
...
>>> class Ordinal(AutoName):
... NORTH = auto()
... SOUTH = auto()
... EAST = auto()
... WEST = auto()
...
>>> [member.value for member in Ordinal]
['NORTH', 'SOUTH', 'EAST', 'WEST']
(cid:174) Note
The_generate_next_value_()methodmustbedefinedbeforeanymembers.
6

### 第7页

5 Iteration
Iteratingoverthemembersofanenumdoesnotprovidethealiases:
>>> list(Shape)
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
>>> list(Weekday)
[<Weekday.MONDAY: 1>, <Weekday.TUESDAY: 2>, <Weekday.WEDNESDAY: 4>, <Weekday.
,→THURSDAY: 8>, <Weekday.FRIDAY: 16>, <Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]
NotethatthealiasesShape.ALIAS_FOR_SQUAREandWeekday.WEEKENDaren’tshown.
The special attribute __members__ is a read-only ordered mapping of names to members. It includes all names
definedintheenumeration,includingthealiases:
>>> for name, member in Shape.__members__.items():
... name, member
...
('SQUARE', <Shape.SQUARE: 2>)
('DIAMOND', <Shape.DIAMOND: 1>)
('CIRCLE', <Shape.CIRCLE: 3>)
('ALIAS_FOR_SQUARE', <Shape.SQUARE: 2>)
The__members__attributecanbeusedfordetailedprogrammaticaccesstotheenumerationmembers. Forexam-
ple,findingallthealiases:
>>> [name for name, member in Shape.__members__.items() if member.name != name]
['ALIAS_FOR_SQUARE']
(cid:174) Note
Aliasesforflagsincludevalueswithmultipleflagsset,suchas3,andnoflagsset,i.e. 0.
6 Comparisons
Enumerationmembersarecomparedbyidentity:
>>> Color.RED is Color.RED
True
>>> Color.RED is Color.BLUE
False
>>> Color.RED is not Color.BLUE
True
Ordered comparisons between enumeration values are not supported. Enum members are not integers (but see
IntEnumbelow):
>>> Color.RED < Color.BLUE
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Color' and 'Color'
Equalitycomparisonsaredefinedthough:
>>> Color.BLUE == Color.RED
False
>>> Color.BLUE != Color.RED
(continuesonnextpage)
7

### 第8页

(continuedfrompreviouspage)
True
>>> Color.BLUE == Color.BLUE
True
Comparisonsagainstnon-enumerationvalueswillalwayscomparenotequal(again,IntEnumwasexplicitlydesigned
tobehavedifferently,seebelow):
>>> Color.BLUE == 2
False
(cid:193) Warning
It is possible to reload modules – if a reloaded module contains enums, they will be recreated, and the new
membersmaynotcompareidentical/equaltotheoriginalmembers.
7 Allowed members and attributes of enumerations
Mostoftheexamplesaboveuseintegersforenumerationvalues. Usingintegersisshortandhandy(andprovidedby
defaultbytheFunctionalAPI),butnotstrictlyenforced. Inthevastmajorityofuse-cases,onedoesn’tcarewhatthe
actualvalueofanenumerationis. Butifthevalueisimportant,enumerationscanhavearbitraryvalues.
EnumerationsarePythonclasses,andcanhavemethodsandspecialmethodsasusual. Ifwehavethisenumeration:
>>> class Mood(Enum):
... FUNKY = 1
... HAPPY = 3
...
... def describe(self):
... # self is the member here
... return self.name, self.value
...
... def __str__(self):
... return 'my custom str! {0}'.format(self.value)
...
... @classmethod
... def favorite_mood(cls):
... # cls here is the enumeration
... return cls.HAPPY
...
Then:
>>> Mood.favorite_mood()
<Mood.HAPPY: 3>
>>> Mood.HAPPY.describe()
('HAPPY', 3)
>>> str(Mood.FUNKY)
'my custom str! 1'
Therulesforwhatisallowedareasfollows: namesthatstartandendwithasingleunderscorearereservedbyenum
andcannotbeused; allotherattributesdefinedwithinanenumerationwillbecomemembersofthisenumeration,
withtheexceptionofspecialmethods(__str__(),__add__(),etc.),descriptors(methodsarealsodescriptors),
andvariablenameslistedin_ignore_.
Note: ifyourenumerationdefines__new__()and/or__init__(), anyvalue(s)giventotheenummemberwill
bepassedintothosemethods. SeePlanetforanexample.
8

### 第9页

(cid:174) Note
The__new__()method,ifdefined,isusedduringcreationoftheEnummembers;itisthenreplacedbyEnum’s
__new__()whichisusedafterclasscreationforlookupofexistingmembers. SeeWhentouse__new__()vs.
__init__()formoredetails.
8 Restricted Enum subclassing
AnewEnumclassmusthaveonebaseenumclass,uptooneconcretedatatype,andasmanyobject-basedmixin
classesasneeded. Theorderofthesebaseclassesis:
class EnumName([mix-in, ...,] [data-type,] base-enum):
pass
Also,subclassinganenumerationisallowedonlyiftheenumerationdoesnotdefineanymembers. Sothisisforbidden:
>>> class MoreColor(Color):
... PINK = 17
...
Traceback (most recent call last):
...
TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>
Butthisisallowed:
>>> class Foo(Enum):
... def some_behavior(self):
... pass
...
>>> class Bar(Foo):
... HAPPY = 1
... SAD = 2
...
Allowingsubclassingofenumsthatdefinememberswouldleadtoaviolationofsomeimportantinvariantsoftypes
and instances. On the other hand, it makes sense to allow sharing some common behavior between a group of
enumerations. (SeeOrderedEnumforanexample.)
9 Dataclass support
Wheninheritingfromadataclass,the__repr__()omitstheinheritedclass’name. Forexample:
>>> from dataclasses import dataclass, field
>>> @dataclass
... class CreatureDataMixin:
... size: str
... legs: int
... tail: bool = field(repr=False, default=True)
...
>>> class Creature(CreatureDataMixin, Enum):
... BEETLE = 'small', 6
... DOG = 'medium', 4
...
>>> Creature.DOG
<Creature.DOG: size='medium', legs=4>
9

### 第10页

Usethedataclass()argumentrepr=Falsetousethestandardrepr().
Changedinversion3.12: Onlythedataclassfieldsareshowninthevaluearea,notthedataclass’name.
(cid:174) Note
Addingdataclass()decoratortoEnumanditssubclassesisnotsupported. Itwillnotraiseanyerrors,butit
willproduceverystrangeresultsatruntime,suchasmembersbeingequaltoeachother:
>>> @dataclass # don't do this: it does not make any sense
... class Color(Enum):
... RED = 1
... BLUE = 2
...
>>> Color.RED is Color.BLUE
False
>>> Color.RED == Color.BLUE # problem is here: they should not be equal
True
10 Pickling
Enumerationscanbepickledandunpickled:
>>> from test.test_enum import Fruit
>>> from pickle import dumps, loads
>>> Fruit.TOMATO is loads(dumps(Fruit.TOMATO))
True
Theusualrestrictionsforpicklingapply: picklableenumsmustbedefinedinthetoplevelofamodule,sinceunpick-
lingrequiresthemtobeimportablefromthatmodule.
(cid:174) Note
Withpickleprotocolversion4itispossibletoeasilypickleenumsnestedinotherclasses.
Itispossibletomodifyhowenummembersarepickled/unpickledbydefining__reduce_ex__()intheenumera-
tionclass. Thedefaultmethodisby-value,butenumswithcomplicatedvaluesmaywanttouseby-name:
>>> import enum
>>> class MyEnum(enum.Enum):
... __reduce_ex__ = enum.pickle_by_enum_name
(cid:174) Note
Usingby-nameforflagsisnotrecommended,asunnamedaliaseswillnotunpickle.
11 Functional API
TheEnumclassiscallable,providingthefollowingfunctionalAPI:
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG')
>>> Animal
<enum 'Animal'>
(continuesonnextpage)
10

### 第11页

(continuedfrompreviouspage)
>>> Animal.ANT
<Animal.ANT: 1>
>>> list(Animal)
[<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]
ThesemanticsofthisAPIresemblenamedtuple. ThefirstargumentofthecalltoEnumisthenameoftheenu-
meration.
Thesecondargumentisthesourceofenumerationmembernames. Itcanbeawhitespace-separatedstringofnames,
asequenceofnames,asequenceof2-tupleswithkey/valuepairs,oramapping(e.g. dictionary)ofnamestovalues.
The last two options enable assigning arbitrary values to enumerations; the others auto-assign increasing integers
startingwith1(usethestartparametertospecifyadifferentstartingvalue). AnewclassderivedfromEnumis
returned. Inotherwords,theaboveassignmenttoAnimalisequivalentto:
>>> class Animal(Enum):
... ANT = 1
... BEE = 2
... CAT = 3
... DOG = 4
...
Thereasonfordefaultingto1asthestartingnumberandnot0isthat0isFalseinabooleansense,butbydefault
enummembersallevaluatetoTrue.
PicklingenumscreatedwiththefunctionalAPIcanbetrickyasframestackimplementationdetailsareusedtotry
and figure out which module the enumeration is being created in (e.g. it will fail if you use a utility function in
a separate module, and also may not work on IronPython or Jython). The solution is to specify the module name
explicitlyasfollows:
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG', module=__name__)
(cid:193) Warning
Ifmoduleisnotsupplied,andEnumcannotdeterminewhatitis,thenewEnummemberswillnotbeunpicklable;
tokeeperrorsclosertothesource,picklingwillbedisabled.
The new pickle protocol 4 also, in some circumstances, relies on __qualname__ being set to the location where
pickle will be able to find the class. For example, if the class was made available in class SomeData in the global
scope:
>>> Animal = Enum('Animal', 'ANT BEE CAT DOG', qualname='SomeData.Animal')
Thecompletesignatureis:
Enum(
value='NewEnumName',
names=<...>,
*,
module='...',
qualname='...',
type=<mixed-in class>,
start=1,
)
• value: Whatthenewenumclasswillrecordasitsname.
• names: Theenummembers. Thiscanbeawhitespace-orcomma-separatedstring(valueswillstartat1unless
otherwisespecified):
11

### 第12页

'RED GREEN BLUE' | 'RED,GREEN,BLUE' | 'RED, GREEN, BLUE'
oraniteratorofnames:
['RED', 'GREEN', 'BLUE']
oraniteratorof(name,value)pairs:
[('CYAN', 4), ('MAGENTA', 5), ('YELLOW', 6)]
oramapping:
{'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42}
• module: nameofmodulewherenewenumclasscanbefound.
• qualname: whereinmodulenewenumclasscanbefound.
• type: typetomixintonewenumclass.
• start: numbertostartcountingatifonlynamesarepassedin.
Changedinversion3.5: Thestartparameterwasadded.
12 Derived Enumerations
12.1 IntEnum
ThefirstvariationofEnumthatisprovidedisalsoasubclassofint. MembersofanIntEnumcanbecomparedto
integers;byextension,integerenumerationsofdifferenttypescanalsobecomparedtoeachother:
>>> from enum import IntEnum
>>> class Shape(IntEnum):
... CIRCLE = 1
... SQUARE = 2
...
>>> class Request(IntEnum):
... POST = 1
... GET = 2
...
>>> Shape == 1
False
>>> Shape.CIRCLE == 1
True
>>> Shape.CIRCLE == Request.POST
True
However,theystillcan’tbecomparedtostandardEnumenumerations:
>>> class Shape(IntEnum):
... CIRCLE = 1
... SQUARE = 2
...
>>> class Color(Enum):
... RED = 1
... GREEN = 2
...
>>> Shape.CIRCLE == Color.RED
False
12

### 第13页

IntEnumvaluesbehavelikeintegersinotherwaysyou’dexpect:
>>> int(Shape.CIRCLE)
1
>>> ['a', 'b', 'c'][Shape.CIRCLE]
'b'
>>> [i for i in range(Shape.SQUARE)]
[0, 1]
12.2 StrEnum
ThesecondvariationofEnumthatisprovidedisalsoasubclassofstr. MembersofaStrEnumcanbecompared
tostrings;byextension,stringenumerationsofdifferenttypescanalsobecomparedtoeachother.
Addedinversion3.11.
12.3 IntFlag
ThenextvariationofEnumprovided,IntFlag,isalsobasedonint. ThedifferencebeingIntFlagmemberscan
be combined using the bitwise operators (&, |, ^, ~) and the result is still an IntFlag member, if possible. Like
IntEnum,IntFlagmembersarealsointegersandcanbeusedwhereveranintisused.
(cid:174) Note
AnyoperationonanIntFlagmemberbesidesthebit-wiseoperationswilllosetheIntFlagmembership.
Bit-wise operations that result in invalid IntFlag values will lose the IntFlag membership. See
FlagBoundaryfordetails.
Addedinversion3.6.
Changedinversion3.11.
SampleIntFlagclass:
>>> from enum import IntFlag
>>> class Perm(IntFlag):
... R = 4
... W = 2
... X = 1
...
>>> Perm.R | Perm.W
<Perm.R|W: 6>
>>> Perm.R + Perm.W
6
>>> RW = Perm.R | Perm.W
>>> Perm.R in RW
True
Itisalsopossibletonamethecombinations:
>>> class Perm(IntFlag):
... R = 4
... W = 2
... X = 1
... RWX = 7
...
>>> Perm.RWX
<Perm.RWX: 7>
(continuesonnextpage)
13

### 第14页

(continuedfrompreviouspage)
>>> ~Perm.RWX
<Perm: 0>
>>> Perm(7)
<Perm.RWX: 7>
(cid:174) Note
Namedcombinationsareconsideredaliases. Aliasesdonotshowupduringiteration,butcanbereturnedfrom
by-valuelookups.
Changedinversion3.11.
Another important difference between IntFlag and Enum is that if no flags are set (the value is 0), its boolean
evaluationisFalse:
>>> Perm.R & Perm.X
<Perm: 0>
>>> bool(Perm.R & Perm.X)
False
Because IntFlag members are also subclasses of int they can be combined with them (but may lose IntFlag
membership:
>>> Perm.X | 4
<Perm.R|X: 5>
>>> Perm.X + 8
9
(cid:174) Note
Thenegationoperator,~,alwaysreturnsanIntFlagmemberwithapositivevalue:
>>> (~Perm.X).value == (Perm.R|Perm.W).value == 6
True
IntFlagmemberscanalsobeiteratedover:
>>> list(RW)
[<Perm.R: 4>, <Perm.W: 2>]
Addedinversion3.11.
12.4 Flag
The last variation is Flag. Like IntFlag, Flag members can be combined using the bitwise operators (&, |, ^,
~). UnlikeIntFlag,theycannotbecombinedwith,norcomparedagainst,anyotherFlagenumeration,norint.
WhileitispossibletospecifythevaluesdirectlyitisrecommendedtouseautoasthevalueandletFlagselectan
appropriatevalue.
Addedinversion3.6.
LikeIntFlag,ifacombinationofFlagmembersresultsinnoflagsbeingset,thebooleanevaluationisFalse:
>>> from enum import Flag, auto
>>> class Color(Flag):
(continuesonnextpage)
14

### 第15页

(continuedfrompreviouspage)
... RED = auto()
... BLUE = auto()
... GREEN = auto()
...
>>> Color.RED & Color.GREEN
<Color: 0>
>>> bool(Color.RED & Color.GREEN)
False
Individualflagsshouldhavevaluesthatarepowersoftwo(1,2,4,8,…),whilecombinationsofflagswillnot:
>>> class Color(Flag):
... RED = auto()
... BLUE = auto()
... GREEN = auto()
... WHITE = RED | BLUE | GREEN
...
>>> Color.WHITE
<Color.WHITE: 7>
Givinganametothe“noflagsset”conditiondoesnotchangeitsbooleanvalue:
>>> class Color(Flag):
... BLACK = 0
... RED = auto()
... BLUE = auto()
... GREEN = auto()
...
>>> Color.BLACK
<Color.BLACK: 0>
>>> bool(Color.BLACK)
False
Flagmemberscanalsobeiteratedover:
>>> purple = Color.RED | Color.BLUE
>>> list(purple)
[<Color.RED: 1>, <Color.BLUE: 2>]
Addedinversion3.11.
(cid:174) Note
Forthemajorityofnewcode,EnumandFlagarestronglyrecommended,sinceIntEnumandIntFlagbreak
some semantic promises of an enumeration (by being comparable to integers, and thus by transitivity to other
unrelatedenumerations). IntEnumandIntFlagshouldbeusedonlyincaseswhereEnumandFlagwillnotdo;
forexample,whenintegerconstantsarereplacedwithenumerations,orforinteroperabilitywithothersystems.
12.5 Others
WhileIntEnumispartoftheenummodule,itwouldbeverysimpletoimplementindependently:
class IntEnum(int, ReprEnum): # or Enum instead of ReprEnum
pass
Thisdemonstrateshowsimilarderivedenumerationscanbedefined;forexampleaFloatEnumthatmixesinfloat
insteadofint.
15

### 第16页

Somerules:
1. WhensubclassingEnum,mix-intypesmustappearbeforetheEnumclassitselfinthesequenceofbases,asin
theIntEnumexampleabove.
2. Mix-intypesmustbesubclassable. Forexample,boolandrangearenotsubclassableandwillthrowanerror
duringEnumcreationifusedasthemix-intype.
3. WhileEnumcanhavemembersofanytype,onceyoumixinanadditionaltype,allthemembersmusthave
valuesofthattype, e.g. intabove. Thisrestrictiondoesnotapplytomix-inswhichonlyaddmethodsand
don’tspecifyanothertype.
4. Whenanotherdatatypeismixedin,thevalueattributeisnotthesameastheenummemberitself,although
itisequivalentandwillcompareequal.
5. Adata typeisamixinthatdefines__new__(),oradataclass
6. %-styleformatting: %sand%rcalltheEnumclass’s__str__()and__repr__()respectively;othercodes
(suchas%ior%hforIntEnum)treattheenummemberasitsmixed-intype.
7. Formattedstringliterals,str.format(),andformat()willusetheenum’s__str__()method.
(cid:174) Note
BecauseIntEnum,IntFlag,andStrEnumaredesignedtobedrop-inreplacementsforexistingconstants,their
__str__()methodhasbeenresettotheirdatatypes’__str__()method.
13 When to use __new__() vs. __init__()
__new__()mustbeusedwheneveryouwanttocustomizetheactualvalueoftheEnummember. Anyothermodi-
ficationsmaygoineither__new__()or__init__(),with__init__()beingpreferred.
Forexample,ifyouwanttopassseveralitemstotheconstructor,butonlywantoneofthemtobethevalue:
>>> class Coordinate(bytes, Enum):
... """
... Coordinate with binary codes that can be indexed by the int code.
... """
... def __new__(cls, value, label, unit):
... obj = bytes.__new__(cls, [value])
... obj._value_ = value
... obj.label = label
... obj.unit = unit
... return obj
... PX = (0, 'P.X', 'km')
... PY = (1, 'P.Y', 'km')
... VX = (2, 'V.X', 'km/s')
... VY = (3, 'V.Y', 'km/s')
...
>>> print(Coordinate['PY'])
Coordinate.PY
>>> print(Coordinate(3))
Coordinate.VY
(cid:193) Warning
16

| (cid:193) Warning |
| --- |
|  |

### 第17页

Donot callsuper().__new__(),asthelookup-only__new__istheonethatisfound; instead,usethedata
typedirectly.
13.1 Finer Points
Supported__dunder__names
__members__isaread-onlyorderedmappingofmember_name:memberitems. Itisonlyavailableontheclass.
__new__(),ifspecified,mustcreateandreturntheenummembers;itisalsoaverygoodideatosetthemember’s
_value_appropriately. Onceallthemembersarecreateditisnolongerused.
Supported_sunder_names
• _name_–nameofthemember
• _value_–valueofthemember;canbesetin__new__
• _missing_()–alookupfunctionusedwhenavalueisnotfound;maybeoverridden
• _ignore_–alistofnames,eitherasalistorastr,thatwillnotbetransformedintomembers,andwill
beremovedfromthefinalclass
• _generate_next_value_()–usedtogetanappropriatevalueforanenummember;maybeoverridden
• _add_alias_()–addsanewnameasanaliastoanexistingmember.
• _add_value_alias_()–addsanewvalueasanaliastoanexistingmember. SeeMultiValueEnumforan
example.
(cid:174) Note
ForstandardEnumclassesthenextvaluechosenisthehighestvalueseenincrementedbyone.
ForFlagclassesthenextvaluechosenwillbethenexthighestpower-of-two.
Changedinversion3.13: Priorversionswouldusethelastseenvalueinsteadofthehighestvalue.
Addedinversion3.6: _missing_,_order_,_generate_next_value_
Addedinversion3.7: _ignore_
Addedinversion3.13: _add_alias_,_add_value_alias_
TohelpkeepPython2/Python3codeinsyncan_order_attributecanbeprovided. Itwillbecheckedagainstthe
actualorderoftheenumerationandraiseanerrorifthetwodonotmatch:
>>> class Color(Enum):
... _order_ = 'RED GREEN BLUE'
... RED = 1
... BLUE = 3
... GREEN = 2
...
Traceback (most recent call last):
...
TypeError: member order does not match _order_:
['RED', 'BLUE', 'GREEN']
['RED', 'GREEN', 'BLUE']
17

### 第18页

(cid:174) Note
InPython2codethe_order_attributeisnecessaryasdefinitionorderislostbeforeitcanberecorded.
_Private__names
Privatenamesarenotconvertedtoenummembers,butremainnormalattributes.
Changedinversion3.11.
Enummembertype
Enum members are instances of their enum class, and are normally accessed as EnumClass.member. In certain
situations,suchaswritingcustomenumbehavior,beingabletoaccessonememberdirectlyfromanotherisuseful,
and is supported; however, in order to avoid name clashes between member names and attributes/methods from
mixed-inclasses,upper-casenamesarestronglyrecommended.
Changedinversion3.5.
Creatingmembersthataremixedwithotherdatatypes
Whensubclassingotherdatatypes,suchasintorstr,withanEnum,allvaluesafterthe=arepassedtothatdata
type’sconstructor. Forexample:
>>> class MyEnum(IntEnum): # help(int) -> int(x, base=10) -> integer
... example = '11', 16 # so x='11' and base=16
...
>>> MyEnum.example.value # and hex(11) is...
17
BooleanvalueofEnumclassesandmembers
Enumclassesthataremixedwithnon-Enumtypes(suchasint,str,etc.) areevaluatedaccordingtothemixed-in
type’srules;otherwise,allmembersevaluateasTrue. Tomakeyourownenum’sbooleanevaluationdependonthe
member’svalueaddthefollowingtoyourclass:
def __bool__(self):
return bool(self.value)
PlainEnumclassesalwaysevaluateasTrue.
Enumclasseswithmethods
Ifyougiveyourenumsubclassextramethods,likethePlanet classbelow,thosemethodswillshowupinadir()
ofthemember,butnotoftheclass:
>>> dir(Planet)
['EARTH', 'JUPITER', 'MARS', 'MERCURY', 'NEPTUNE', 'SATURN', 'URANUS', 'VENUS', '__
,→class__', '__doc__', '__members__', '__module__']
>>> dir(Planet.EARTH)
['__class__', '__doc__', '__module__', 'mass', 'name', 'radius', 'surface_gravity',
,→ 'value']
CombiningmembersofFlag
IteratingoveracombinationofFlagmemberswillonlyreturnthemembersthatarecomprisedofasinglebit:
18

### 第19页

>>> class Color(Flag):
... RED = auto()
... GREEN = auto()
... BLUE = auto()
... MAGENTA = RED | BLUE
... YELLOW = RED | GREEN
... CYAN = GREEN | BLUE
...
>>> Color(3) # named combination
<Color.YELLOW: 3>
>>> Color(7) # not named combination
<Color.RED|GREEN|BLUE: 7>
FlagandIntFlagminutia
Usingthefollowingsnippetforourexamples:
>>> class Color(IntFlag):
... BLACK = 0
... RED = 1
... GREEN = 2
... BLUE = 4
... PURPLE = RED | BLUE
... WHITE = RED | GREEN | BLUE
...
thefollowingaretrue:
• single-bitflagsarecanonical
• multi-bitandzero-bitflagsarealiases
• onlycanonicalflagsarereturnedduringiteration:
>>> list(Color.WHITE)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]
• negatingaflagorflagsetreturnsanewflag/flagsetwiththecorrespondingpositiveintegervalue:
>>> Color.BLUE
<Color.BLUE: 4>
>>> ~Color.BLUE
<Color.RED|GREEN: 3>
• namesofpseudo-flagsareconstructedfromtheirmembers’names:
>>> (Color.RED | Color.GREEN).name
'RED|GREEN'
>>> class Perm(IntFlag):
... R = 4
... W = 2
... X = 1
...
>>> (Perm.R & Perm.W).name is None # effectively Perm(0)
True
• multi-bitflags,akaaliases,canbereturnedfromoperations:
19

### 第20页

>>> Color.RED | Color.BLUE
<Color.PURPLE: 5>
>>> Color(7) # or Color(-1)
<Color.WHITE: 7>
>>> Color(0)
<Color.BLACK: 0>
• membership/containmentchecking: zero-valuedflagsarealwaysconsideredtobecontained:
>>> Color.BLACK in Color.WHITE
True
otherwise,onlyifallbitsofoneflagareintheotherflagwillTruebereturned:
>>> Color.PURPLE in Color.WHITE
True
>>> Color.GREEN in Color.PURPLE
False
Thereisanewboundarymechanismthatcontrolshowout-of-range/invalidbitsarehandled: STRICT,CONFORM,
EJECT,andKEEP:
• STRICT–>raisesanexceptionwhenpresentedwithinvalidvalues
• CONFORM–>discardsanyinvalidbits
• EJECT–>loseFlagstatusandbecomeanormalintwiththegivenvalue
• KEEP–>keeptheextrabits
– keepsFlagstatusandextrabits
– extrabitsdonotshowupiniteration
– extrabitsdoshowupinrepr()andstr()
The default for Flag is STRICT, the default for IntFlag is EJECT, and the default for _convert_ is KEEP (see
ssl.OptionsforanexampleofwhenKEEPisneeded).
14 How are Enums and Flags different?
EnumshaveacustommetaclassthataffectsmanyaspectsofbothderivedEnumclassesandtheirinstances(members).
14.1 Enum Classes
TheEnumTypemetaclassisresponsibleforprovidingthe__contains__(),__dir__(),__iter__()andother
methods that allow one to do things with an Enum class that fail on a typical class, such as list(Color) or
some_enum_var in Color. EnumTypeisresponsibleforensuringthatvariousothermethodsonthefinalEnum
classarecorrect(suchas__new__(),__getnewargs__(),__str__()and__repr__()).
14.2 Flag Classes
Flagshaveanexpandedviewofaliasing: tobecanonical,thevalueofaflagneedstobeapower-of-twovalue,and
notaduplicatename. So,inadditiontotheEnumdefinitionofalias,aflagwithnovalue(a.k.a. 0)orwithmorethan
onepower-of-twovalue(e.g. 3)isconsideredanalias.
20

### 第21页

14.3 Enum Members (aka instances)
The most interesting thing about enum members is that they are singletons. EnumType creates them all while it
is creating the enum class itself, and then puts a custom __new__() in place to ensure that no new ones are ever
instantiatedbyreturningonlytheexistingmemberinstances.
14.4 Flag Members
FlagmemberscanbeiteratedoverjustliketheFlagclass,andonlythecanonicalmemberswillbereturned. For
example:
>>> list(Color)
[<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]
(NotethatBLACK,PURPLE,andWHITEdonotshowup.)
Invertingaflagmemberreturnsthecorrespondingpositivevalue,ratherthananegativevalue—forexample:
>>> ~Color.RED
<Color.GREEN|BLUE: 6>
Flagmembershavealengthcorrespondingtothenumberofpower-of-twovaluestheycontain. Forexample:
>>> len(Color.PURPLE)
2
15 Enum Cookbook
WhileEnum,IntEnum,StrEnum,Flag,andIntFlagareexpectedtocoverthemajorityofuse-cases,theycannot
coverthemall. Herearerecipesforsomedifferenttypesofenumerationsthatcanbeuseddirectly,orasexamples
forcreatingone’sown.
15.1 Omitting values
Inmanyuse-cases,onedoesn’tcarewhattheactualvalueofanenumerationis. Thereareseveralwaystodefinethis
typeofsimpleenumeration:
• useinstancesofautoforthevalue
• useinstancesofobjectasthevalue
• useadescriptivestringasthevalue
• useatupleasthevalueandacustom__new__()toreplacethetuplewithanintvalue
Using any of these methods signifies to the user that these values are not important, and also enables one to add,
remove,orreordermemberswithouthavingtorenumbertheremainingmembers.
Usingauto
Usingautowouldlooklike:
>>> class Color(Enum):
... RED = auto()
... BLUE = auto()
... GREEN = auto()
...
>>> Color.GREEN
<Color.GREEN: 3>
21

### 第22页

Usingobject
Usingobjectwouldlooklike:
>>> class Color(Enum):
... RED = object()
... GREEN = object()
... BLUE = object()
...
>>> Color.GREEN
<Color.GREEN: <object object at 0x...>>
Thisisalsoagoodexampleofwhyyoumightwanttowriteyourown__repr__():
>>> class Color(Enum):
... RED = object()
... GREEN = object()
... BLUE = object()
... def __repr__(self):
... return "<%s.%s>" % (self.__class__.__name__, self._name_)
...
>>> Color.GREEN
<Color.GREEN>
Usingadescriptivestring
Usingastringasthevaluewouldlooklike:
>>> class Color(Enum):
... RED = 'stop'
... GREEN = 'go'
... BLUE = 'too fast!'
...
>>> Color.GREEN
<Color.GREEN: 'go'>
Usingacustom__new__()
Usinganauto-numbering__new__()wouldlooklike:
>>> class AutoNumber(Enum):
... def __new__(cls):
... value = len(cls.__members__) + 1
... obj = object.__new__(cls)
... obj._value_ = value
... return obj
...
>>> class Color(AutoNumber):
... RED = ()
... GREEN = ()
... BLUE = ()
...
>>> Color.GREEN
<Color.GREEN: 2>
TomakeamoregeneralpurposeAutoNumber,add*argstothesignature:
22

### 第23页

>>> class AutoNumber(Enum):
... def __new__(cls, *args): # this is the only change from above
... value = len(cls.__members__) + 1
... obj = object.__new__(cls)
... obj._value_ = value
... return obj
...
ThenwhenyouinheritfromAutoNumberyoucanwriteyourown__init__tohandleanyextraarguments:
>>> class Swatch(AutoNumber):
... def __init__(self, pantone='unknown'):
... self.pantone = pantone
... AUBURN = '3497'
... SEA_GREEN = '1246'
... BLEACHED_CORAL = () # New color, no Pantone code yet!
...
>>> Swatch.SEA_GREEN
<Swatch.SEA_GREEN: 2>
>>> Swatch.SEA_GREEN.pantone
'1246'
>>> Swatch.BLEACHED_CORAL.pantone
'unknown'
(cid:174) Note
The__new__()method,ifdefined,isusedduringcreationoftheEnummembers;itisthenreplacedbyEnum’s
__new__()whichisusedafterclasscreationforlookupofexistingmembers.
(cid:193) Warning
Donot callsuper().__new__(),asthelookup-only__new__istheonethatisfound; instead,usethedata
typedirectly–e.g.:
obj = int.__new__(cls, value)
15.2 OrderedEnum
An ordered enumeration that is not based on IntEnum and so maintains the normal Enum invariants (such as not
beingcomparabletootherenumerations):
>>> class OrderedEnum(Enum):
... def __ge__(self, other):
... if self.__class__ is other.__class__:
... return self.value >= other.value
... return NotImplemented
... def __gt__(self, other):
... if self.__class__ is other.__class__:
... return self.value > other.value
... return NotImplemented
... def __le__(self, other):
... if self.__class__ is other.__class__:
... return self.value <= other.value
... return NotImplemented
(continuesonnextpage)
23

| (cid:193) Warning |
| --- |
| Donot callsuper().__new__(),asthelookup-only__new__istheonethatisfound; instead,usethedata
typedirectly–e.g.:
obj = int.__new__(cls, value) |

### 第24页

(continuedfrompreviouspage)
... def __lt__(self, other):
... if self.__class__ is other.__class__:
... return self.value < other.value
... return NotImplemented
...
>>> class Grade(OrderedEnum):
... A = 5
... B = 4
... C = 3
... D = 2
... F = 1
...
>>> Grade.C < Grade.A
True
15.3 DuplicateFreeEnum
Raisesanerrorifaduplicatemembervalueisfoundinsteadofcreatinganalias:
>>> class DuplicateFreeEnum(Enum):
... def __init__(self, *args):
... cls = self.__class__
... if any(self.value == e.value for e in cls):
... a = self.name
... e = cls(self.value).name
... raise ValueError(
... "aliases not allowed in DuplicateFreeEnum: %r --> %r"
... % (a, e))
...
>>> class Color(DuplicateFreeEnum):
... RED = 1
... GREEN = 2
... BLUE = 3
... GRENE = 2
...
Traceback (most recent call last):
...
ValueError: aliases not allowed in DuplicateFreeEnum: 'GRENE' --> 'GREEN'
(cid:174) Note
ThisisausefulexampleforsubclassingEnumtoaddorchangeotherbehaviorsaswellasdisallowingaliases. If
theonlydesiredchangeisdisallowingaliases,theunique()decoratorcanbeusedinstead.
15.4 MultiValueEnum
Supportshavingmorethanonevaluepermember:
>>> class MultiValueEnum(Enum):
... def __new__(cls, value, *values):
... self = object.__new__(cls)
... self._value_ = value
... for v in values:
... self._add_value_alias_(v)
... return self
(continuesonnextpage)
24

### 第25页

(continuedfrompreviouspage)
...
>>> class DType(MultiValueEnum):
... float32 = 'f', 8
... double64 = 'd', 9
...
>>> DType('f')
<DType.float32: 'f'>
>>> DType(9)
<DType.double64: 'd'>
15.5 Planet
If__new__()or__init__()isdefined,thevalueoftheenummemberwillbepassedtothosemethods:
>>> class Planet(Enum):
... MERCURY = (3.303e+23, 2.4397e6)
... VENUS = (4.869e+24, 6.0518e6)
... EARTH = (5.976e+24, 6.37814e6)
... MARS = (6.421e+23, 3.3972e6)
... JUPITER = (1.9e+27, 7.1492e7)
... SATURN = (5.688e+26, 6.0268e7)
... URANUS = (8.686e+25, 2.5559e7)
... NEPTUNE = (1.024e+26, 2.4746e7)
... def __init__(self, mass, radius):
... self.mass = mass # in kilograms
... self.radius = radius # in meters
... @property
... def surface_gravity(self):
... # universal gravitational constant (m3 kg-1 s-2)
... G = 6.67300E-11
... return G * self.mass / (self.radius * self.radius)
...
>>> Planet.EARTH.value
(5.976e+24, 6378140.0)
>>> Planet.EARTH.surface_gravity
9.802652743337129
15.6 TimePeriod
Anexampletoshowthe_ignore_attributeinuse:
>>> from datetime import timedelta
>>> class Period(timedelta, Enum):
... "different lengths of time"
... _ignore_ = 'Period i'
... Period = vars()
... for i in range(367):
... Period['day_%d' % i] = i
...
>>> list(Period)[:2]
[<Period.day_0: datetime.timedelta(0)>, <Period.day_1: datetime.timedelta(days=1)>]
>>> list(Period)[-2:]
[<Period.day_365: datetime.timedelta(days=365)>, <Period.day_366: datetime.
,→timedelta(days=366)>]
25

### 第26页

16 Subclassing EnumType
WhilemostenumneedscanbemetbycustomizingEnumsubclasses,eitherwithclassdecoratorsorcustomfunctions,
EnumTypecanbesubclassedtoprovideadifferentEnumexperience.
26

