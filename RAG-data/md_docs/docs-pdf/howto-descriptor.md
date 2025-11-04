### 第1页

Descriptor Guide
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Primer 3
1.1 Simpleexample: Adescriptorthatreturnsaconstant . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Dynamiclookups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Managedattributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Customizednames. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Closingthoughts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 CompletePracticalExample 6
2.1 Validatorclass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Customvalidators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Practicalapplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 TechnicalTutorial 9
3.1 Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 Definitionandintroduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.3 Descriptorprotocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4 Overviewofdescriptorinvocation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.5 Invocationfromaninstance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.6 Invocationfromaclass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.7 Invocationfromsuper . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.8 Summaryofinvocationlogic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.9 Automaticnamenotification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.10 ORMexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4 PurePythonEquivalents 13
4.1 Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4.2 Functionsandmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.3 Kindsofmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.4 Staticmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.5 Classmethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.6 Memberobjectsand__slots__ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Author
RaymondHettinger
Contact
<pythonatrcndotcom>
1

### 第2页

Contents
• DescriptorGuide
– Primer
∗ Simpleexample: Adescriptorthatreturnsaconstant
∗ Dynamiclookups
∗ Managedattributes
∗ Customizednames
∗ Closingthoughts
– CompletePracticalExample
∗ Validatorclass
∗ Customvalidators
∗ Practicalapplication
– TechnicalTutorial
∗ Abstract
∗ Definitionandintroduction
∗ Descriptorprotocol
∗ Overviewofdescriptorinvocation
∗ Invocationfromaninstance
∗ Invocationfromaclass
∗ Invocationfromsuper
∗ Summaryofinvocationlogic
∗ Automaticnamenotification
∗ ORMexample
– PurePythonEquivalents
∗ Properties
∗ Functionsandmethods
∗ Kindsofmethods
∗ Staticmethods
∗ Classmethods
∗ Memberobjectsand__slots__
Descriptorsletobjectscustomizeattributelookup,storage,anddeletion.
Thisguidehasfourmajorsections:
1) The“primer”givesabasicoverview,movinggentlyfromsimpleexamples,addingonefeatureatatime. Start
hereifyou’renewtodescriptors.
2) Thesecondsectionshowsacomplete,practicaldescriptorexample. Ifyoualreadyknowthebasics,startthere.
3) Thethirdsectionprovidesamoretechnicaltutorialthatgoesintothedetailedmechanicsofhowdescriptors
work. Mostpeopledon’tneedthislevelofdetail.
2

| Contents |  |
| --- | --- |
|  | Contents |
|  |  |

### 第3页

4) ThelastsectionhaspurePythonequivalentsforbuilt-indescriptorsthatarewritteninC.Readthisifyou’re
curious about how functions turn into bound methods or about the implementation of common tools like
classmethod(),staticmethod(),property(),and__slots__.
1 Primer
Inthisprimer,westartwiththemostbasicpossibleexampleandthenwe’lladdnewcapabilitiesonebyone.
1.1 Simple example: A descriptor that returns a constant
TheTenclassisadescriptorwhose__get__()methodalwaysreturnstheconstant10:
class Ten:
def __get__(self, obj, objtype=None):
return 10
Tousethedescriptor,itmustbestoredasaclassvariableinanotherclass:
class A:
x = 5 # Regular class attribute
y = Ten() # Descriptor instance
Aninteractivesessionshowsthedifferencebetweennormalattributelookupanddescriptorlookup:
>>> a = A() # Make an instance of class A
>>> a.x # Normal attribute lookup
5
>>> a.y # Descriptor lookup
10
Inthea.xattributelookup,thedotoperatorfinds'x': 5intheclassdictionary. Inthea.ylookup,thedotoperator
findsadescriptorinstance,recognizedbyits__get__method. Callingthatmethodreturns10.
Notethatthevalue10isnotstoredineithertheclassdictionaryortheinstancedictionary. Instead,thevalue10is
computedondemand.
Thisexampleshowshowasimpledescriptorworks,butitisn’tveryuseful. Forretrievingconstants,normalattribute
lookupwouldbebetter.
Inthenextsection,we’llcreatesomethingmoreuseful,adynamiclookup.
1.2 Dynamic lookups
Interestingdescriptorstypicallyruncomputationsinsteadofreturningconstants:
import os
class DirectorySize:
def __get__(self, obj, objtype=None):
return len(os.listdir(obj.dirname))
class Directory:
size = DirectorySize() # Descriptor instance
def __init__(self, dirname):
self.dirname = dirname # Regular instance attribute
Aninteractivesessionshowsthatthelookupisdynamic—itcomputesdifferent,updatedanswerseachtime:
3

### 第4页

>>> s = Directory('songs')
>>> g = Directory('games')
>>> s.size # The songs directory has twenty files
20
>>> g.size # The games directory has three files
3
>>> os.remove('games/chess') # Delete a game
>>> g.size # File count is automatically updated
2
Besidesshowinghowdescriptorscanruncomputations,thisexamplealsorevealsthepurposeoftheparametersto
__get__(). Theselfparameterissize,aninstanceofDirectorySize. Theobjparameteriseithergors,aninstanceof
Directory. Itistheobjparameterthatletsthe__get__()methodlearnthetargetdirectory. Theobjtypeparameter
istheclassDirectory.
1.3 Managed attributes
Apopularusefordescriptorsismanagingaccesstoinstancedata. Thedescriptorisassignedtoapublicattributein
theclassdictionarywhiletheactualdataisstoredasaprivateattributeintheinstancedictionary. Thedescriptor’s
__get__()and__set__()methodsaretriggeredwhenthepublicattributeisaccessed.
Inthefollowingexample, ageisthepublicattributeand_ageistheprivateattribute. Whenthepublicattributeis
accessed,thedescriptorlogsthelookuporupdate:
import logging
logging.basicConfig(level=logging.INFO)
class LoggedAgeAccess:
def __get__(self, obj, objtype=None):
value = obj._age
logging.info('Accessing %r giving %r', 'age', value)
return value
def __set__(self, obj, value):
logging.info('Updating %r to %r', 'age', value)
obj._age = value
class Person:
age = LoggedAgeAccess() # Descriptor instance
def __init__(self, name, age):
self.name = name # Regular instance attribute
self.age = age # Calls __set__()
def birthday(self):
self.age += 1 # Calls both __get__() and __set__()
Aninteractivesessionshowsthatallaccesstothemanagedattributeageislogged,butthattheregularattributename
isnotlogged:
>>> mary = Person('Mary M', 30) # The initial age update is logged
INFO:root:Updating 'age' to 30
>>> dave = Person('David D', 40)
INFO:root:Updating 'age' to 40
(continuesonnextpage)
4

### 第5页

(continuedfrompreviouspage)
>>> vars(mary) # The actual data is in a private attribute
{'name': 'Mary M', '_age': 30}
>>> vars(dave)
{'name': 'David D', '_age': 40}
>>> mary.age # Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
30
>>> mary.birthday() # Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31
>>> dave.name # Regular attribute lookup isn't logged
'David D'
>>> dave.age # Only the managed attribute is logged
INFO:root:Accessing 'age' giving 40
40
One major issue with this example is that the private name _age is hardwired in the LoggedAgeAccess class. That
meansthateachinstancecanonlyhaveoneloggedattributeandthatitsnameisunchangeable. Inthenextexample,
we’llfixthatproblem.
1.4 Customized names
Whenaclassusesdescriptors,itcaninformeachdescriptoraboutwhichvariablenamewasused.
Inthisexample,thePersonclasshastwodescriptorinstances,nameandage. WhenthePersonclassisdefined,
it makes a callback to __set_name__() in LoggedAccess so that the field names can be recorded, giving each
descriptoritsownpublic_nameandprivate_name:
import logging
logging.basicConfig(level=logging.INFO)
class LoggedAccess:
def __set_name__(self, owner, name):
self.public_name = name
self.private_name = '_' + name
def __get__(self, obj, objtype=None):
value = getattr(obj, self.private_name)
logging.info('Accessing %r giving %r', self.public_name, value)
return value
def __set__(self, obj, value):
logging.info('Updating %r to %r', self.public_name, value)
setattr(obj, self.private_name, value)
class Person:
name = LoggedAccess() # First descriptor instance
age = LoggedAccess() # Second descriptor instance
def __init__(self, name, age):
self.name = name # Calls the first descriptor
self.age = age # Calls the second descriptor
(continuesonnextpage)
5

### 第6页

(continuedfrompreviouspage)
def birthday(self):
self.age += 1
AninteractivesessionshowsthatthePersonclasshascalled__set_name__()sothatthefieldnameswouldbe
recorded. Herewecallvars()tolookupthedescriptorwithouttriggeringit:
>>> vars(vars(Person)['name'])
{'public_name': 'name', 'private_name': '_name'}
>>> vars(vars(Person)['age'])
{'public_name': 'age', 'private_name': '_age'}
Thenewclassnowlogsaccesstobothnameandage:
>>> pete = Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10
>>> kate = Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20
ThetwoPersoninstancescontainonlytheprivatenames:
>>> vars(pete)
{'_name': 'Peter P', '_age': 10}
>>> vars(kate)
{'_name': 'Catherine C', '_age': 20}
1.5 Closing thoughts
Adescriptoriswhatwecallanyobjectthatdefines__get__(),__set__(),or__delete__().
Optionally,descriptorscanhavea__set_name__()method. Thisisonlyusedincaseswhereadescriptorneedsto
knoweithertheclasswhereitwascreatedorthenameofclassvariableitwasassignedto. (Thismethod,ifpresent,
iscalledeveniftheclassisnotadescriptor.)
Descriptors get invoked by the dot operator during attribute lookup. If a descriptor is accessed indirectly with
vars(some_class)[descriptor_name],thedescriptorinstanceisreturnedwithoutinvokingit.
Descriptorsonlyworkwhenusedasclassvariables. Whenputininstances,theyhavenoeffect.
Themainmotivationfordescriptorsistoprovideahookallowingobjectsstoredinclassvariablestocontrolwhat
happensduringattributelookup.
Traditionally, thecallingclasscontrolswhathappensduringlookup. Descriptorsinvertthatrelationshipandallow
thedatabeinglooked-uptohaveasayinthematter.
Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like
classmethod(),staticmethod(),property(),andfunctools.cached_property()areallimplemented
asdescriptors.
2 Complete Practical Example
Inthisexample,wecreateapracticalandpowerfultoolforlocatingnotoriouslyhardtofinddatacorruptionbugs.
6

### 第7页

2.1 Validator class
Avalidatorisadescriptorformanagedattributeaccess. Priortostoringanydata,itverifiesthatthenewvaluemeets
varioustypeandrangerestrictions. Ifthoserestrictionsaren’tmet,itraisesanexceptiontopreventdatacorruption
atitssource.
ThisValidatorclassisbothanabstractbaseclassandamanagedattributedescriptor:
from abc import ABC, abstractmethod
class Validator(ABC):
def __set_name__(self, owner, name):
self.private_name = '_' + name
def __get__(self, obj, objtype=None):
return getattr(obj, self.private_name)
def __set__(self, obj, value):
self.validate(value)
setattr(obj, self.private_name, value)
@abstractmethod
def validate(self, value):
pass
CustomvalidatorsneedtoinheritfromValidatorandmustsupplyavalidate()methodtotestvariousrestric-
tionsasneeded.
2.2 Custom validators
Herearethreepracticaldatavalidationutilities:
1) OneOfverifiesthatavalueisoneofarestrictedsetofoptions.
2) Numberverifiesthatavalueiseitheranintorfloat. Optionally,itverifiesthatavalueisbetweenagiven
minimumormaximum.
3) Stringverifiesthatavalueisastr. Optionally, itvalidatesagivenminimumormaximumlength. Itcan
validateauser-definedpredicateaswell.
class OneOf(Validator):
def __init__(self, *options):
self.options = set(options)
def validate(self, value):
if value not in self.options:
raise ValueError(
f'Expected {value!r} to be one of {self.options!r}'
)
class Number(Validator):
def __init__(self, minvalue=None, maxvalue=None):
self.minvalue = minvalue
self.maxvalue = maxvalue
def validate(self, value):
if not isinstance(value, (int, float)):
(continuesonnextpage)
7

### 第8页

(continuedfrompreviouspage)
raise TypeError(f'Expected {value!r} to be an int or float')
if self.minvalue is not None and value < self.minvalue:
raise ValueError(
f'Expected {value!r} to be at least {self.minvalue!r}'
)
if self.maxvalue is not None and value > self.maxvalue:
raise ValueError(
f'Expected {value!r} to be no more than {self.maxvalue!r}'
)
class String(Validator):
def __init__(self, minsize=None, maxsize=None, predicate=None):
self.minsize = minsize
self.maxsize = maxsize
self.predicate = predicate
def validate(self, value):
if not isinstance(value, str):
raise TypeError(f'Expected {value!r} to be a str')
if self.minsize is not None and len(value) < self.minsize:
raise ValueError(
f'Expected {value!r} to be no smaller than {self.minsize!r}'
)
if self.maxsize is not None and len(value) > self.maxsize:
raise ValueError(
f'Expected {value!r} to be no bigger than {self.maxsize!r}'
)
if self.predicate is not None and not self.predicate(value):
raise ValueError(
f'Expected {self.predicate} to be true for {value!r}'
)
2.3 Practical application
Here’showthedatavalidatorscanbeusedinarealclass:
class Component:
name = String(minsize=3, maxsize=10, predicate=str.isupper)
kind = OneOf('wood', 'metal', 'plastic')
quantity = Number(minvalue=0)
def __init__(self, name, kind, quantity):
self.name = name
self.kind = kind
self.quantity = quantity
Thedescriptorspreventinvalidinstancesfrombeingcreated:
>>> Component('Widget', 'metal', 5) # Blocked: 'Widget' is not all uppercase
Traceback (most recent call last):
...
ValueError: Expected <method 'isupper' of 'str' objects> to be true for 'Widget'
>>> Component('WIDGET', 'metle', 5) # Blocked: 'metle' is misspelled
(continuesonnextpage)
8

### 第9页

(continuedfrompreviouspage)
Traceback (most recent call last):
...
ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}
>>> Component('WIDGET', 'metal', -5) # Blocked: -5 is negative
Traceback (most recent call last):
...
ValueError: Expected -5 to be at least 0
>>> Component('WIDGET', 'metal', 'V') # Blocked: 'V' isn't a number
Traceback (most recent call last):
...
TypeError: Expected 'V' to be an int or float
>>> c = Component('WIDGET', 'metal', 5) # Allowed: The inputs are valid
3 Technical Tutorial
Whatfollowsisamoretechnicaltutorialforthemechanicsanddetailsofhowdescriptorswork.
3.1 Abstract
Definesdescriptors,summarizestheprotocol,andshowshowdescriptorsarecalled. Providesanexampleshowing
howobjectrelationalmappingswork.
Learning about descriptors not only provides access to a larger toolset, it creates a deeper understanding of how
Pythonworks.
3.2 Definition and introduction
Ingeneral,adescriptorisanattributevaluethathasoneofthemethodsinthedescriptorprotocol. Thosemethods
are__get__(),__set__(),and__delete__(). Ifanyofthosemethodsaredefinedforanattribute,itissaidto
beadescriptor.
Thedefaultbehaviorforattributeaccessistoget,set,ordeletetheattributefromanobject’sdictionary. Forinstance,
a.xhasalookupchainstartingwitha.__dict__['x'],thentype(a).__dict__['x'],andcontinuingthrough
themethodresolutionorderoftype(a). Ifthelooked-upvalueisanobjectdefiningoneofthedescriptormethods,
thenPythonmayoverridethedefaultbehaviorandinvokethedescriptormethodinstead. Wherethisoccursinthe
precedencechaindependsonwhichdescriptormethodsweredefined.
Descriptors are a powerful, general purpose protocol. They are the mechanism behind properties, methods, static
methods,classmethods,andsuper(). TheyareusedthroughoutPythonitself. Descriptorssimplifytheunderlying
CcodeandofferaflexiblesetofnewtoolsforeverydayPythonprograms.
3.3 Descriptor protocol
descr.__get__(self, obj, type=None)
descr.__set__(self, obj, value)
descr.__delete__(self, obj)
Thatisallthereistoit. Defineanyofthesemethodsandanobjectisconsideredadescriptorandcanoverridedefault
behavioruponbeinglookedupasanattribute.
Ifanobjectdefines__set__()or__delete__(),itisconsideredadatadescriptor. Descriptorsthatonlydefine
__get__()arecallednon-datadescriptors(theyareoftenusedformethodsbutotherusesarepossible).
Dataandnon-datadescriptorsdifferinhowoverridesarecalculatedwithrespecttoentriesinaninstance’sdictionary.
Ifaninstance’sdictionaryhasanentrywiththesamenameasadatadescriptor,thedatadescriptortakesprecedence.
9

### 第10页

If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes
precedence.
To make a read-only data descriptor, define both __get__() and __set__() with the __set__() raising an
AttributeErrorwhencalled. Definingthe__set__()methodwithanexceptionraisingplaceholderisenough
tomakeitadatadescriptor.
3.4 Overview of descriptor invocation
Adescriptorcanbecalleddirectlywithdesc.__get__(obj)ordesc.__get__(None, cls).
Butitismorecommonforadescriptortobeinvokedautomaticallyfromattributeaccess.
Theexpressionobj.xlooksuptheattributexinthechainofnamespacesforobj. Ifthesearchfindsadescriptor
outsideoftheinstance__dict__,its__get__()methodisinvokedaccordingtotheprecedenceruleslistedbelow.
Thedetailsofinvocationdependonwhetherobjisanobject,class,orinstanceofsuper.
3.5 Invocation from an instance
Instancelookupscansthroughachainofnamespacesgivingdatadescriptorsthehighestpriority,followedbyinstance
variables,thennon-datadescriptors,thenclassvariables,andlastly__getattr__()ifitisprovided.
Ifadescriptorisfoundfora.x,thenitisinvokedwith: desc.__get__(a, type(a)).
Thelogicforadottedlookupisinobject.__getattribute__(). HereisapurePythonequivalent:
def find_name_in_mro(cls, name, default):
"Emulate _PyType_Lookup() in Objects/typeobject.c"
for base in cls.__mro__:
if name in vars(base):
return vars(base)[name]
return default
def object_getattribute(obj, name):
"Emulate PyObject_GenericGetAttr() in Objects/object.c"
null = object()
objtype = type(obj)
cls_var = find_name_in_mro(objtype, name, null)
descr_get = getattr(type(cls_var), '__get__', null)
if descr_get is not null:
if (hasattr(type(cls_var), '__set__')
or hasattr(type(cls_var), '__delete__')):
return descr_get(cls_var, obj, objtype) # data descriptor
if hasattr(obj, '__dict__') and name in vars(obj):
return vars(obj)[name] # instance variable
if descr_get is not null:
return descr_get(cls_var, obj, objtype) # non-data descriptor
if cls_var is not null:
return cls_var # class variable
raise AttributeError(name)
Note, there is no __getattr__() hook in the __getattribute__() code. That is why calling
__getattribute__()directlyorwithsuper().__getattribute__willbypass__getattr__()entirely.
Instead,itisthedotoperatorandthegetattr()functionthatareresponsibleforinvoking__getattr__()when-
ever__getattribute__()raisesanAttributeError. Theirlogicisencapsulatedinahelperfunction:
def getattr_hook(obj, name):
"Emulate slot_tp_getattr_hook() in Objects/typeobject.c"
try:
(continuesonnextpage)
10

### 第11页

(continuedfrompreviouspage)
return obj.__getattribute__(name)
except AttributeError:
if not hasattr(type(obj), '__getattr__'):
raise
return type(obj).__getattr__(obj, name) # __getattr__
3.6 Invocation from a class
The logic for a dotted lookup such as A.x is in type.__getattribute__(). The steps are similar to those
forobject.__getattribute__()buttheinstancedictionarylookupisreplacedbyasearchthroughtheclass’s
methodresolutionorder.
Ifadescriptorisfound,itisinvokedwithdesc.__get__(None, A).
ThefullCimplementationcanbefoundintype_getattro()and_PyType_Lookup()inObjects/typeobject.c.
3.7 Invocation from super
Thelogicforsuper’sdottedlookupisinthe__getattribute__()methodforobjectreturnedbysuper().
Adottedlookupsuchassuper(A, obj).msearchesobj.__class__.__mro__forthebaseclassBimmediately
followingAandthenreturnsB.__dict__['m'].__get__(obj, A).Ifnotadescriptor,misreturnedunchanged.
ThefullCimplementationcanbefoundinsuper_getattro()inObjects/typeobject.c. ApurePythonequivalent
canbefoundinGuido’sTutorial.
3.8 Summary of invocation logic
The mechanism for descriptors is embedded in the __getattribute__() methods for object, type, and
super().
Theimportantpointstorememberare:
• Descriptorsareinvokedbythe__getattribute__()method.
• Classesinheritthismachineryfromobject,type,orsuper().
• Overriding__getattribute__()preventsautomaticdescriptorcallsbecauseallthedescriptorlogicisin
thatmethod.
• object.__getattribute__() and type.__getattribute__() make different calls to __get__().
Thefirstincludestheinstanceandmayincludetheclass. ThesecondputsinNonefortheinstanceandalways
includestheclass.
• Datadescriptorsalwaysoverrideinstancedictionaries.
• Non-datadescriptorsmaybeoverriddenbyinstancedictionaries.
3.9 Automatic name notification
Sometimesitisdesirableforadescriptortoknowwhatclassvariablenameitwasassignedto. Whenanewclassis
created,thetypemetaclassscansthedictionaryofthenewclass. Ifanyoftheentriesaredescriptorsandifthey
define__set_name__(),thatmethodiscalledwithtwoarguments. Theowneristheclasswherethedescriptoris
used,andthenameistheclassvariablethedescriptorwasassignedto.
Theimplementationdetailsareintype_new()andset_names()inObjects/typeobject.c.
Sincetheupdatelogicisintype.__new__(),notificationsonlytakeplaceatthetimeofclasscreation. Ifdescriptors
areaddedtotheclassafterwards,__set_name__()willneedtobecalledmanually.
11

### 第12页

3.10 ORM example
The following code is a simplified skeleton showing how data descriptors could be used to implement an object
relationalmapping.
The essential idea is that the data is stored in an external database. The Python instances only hold keys to the
database’stables. Descriptorstakecareoflookupsorupdates:
class Field:
def __set_name__(self, owner, name):
self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'
def __get__(self, obj, objtype=None):
return conn.execute(self.fetch, [obj.key]).fetchone()[0]
def __set__(self, obj, value):
conn.execute(self.store, [value, obj.key])
conn.commit()
WecanusetheFieldclasstodefinemodelsthatdescribetheschemaforeachtableinadatabase:
class Movie:
table = 'Movies' # Table name
key = 'title' # Primary key
director = Field()
year = Field()
def __init__(self, key):
self.key = key
class Song:
table = 'Music'
key = 'title'
artist = Field()
year = Field()
genre = Field()
def __init__(self, key):
self.key = key
Tousethemodels,firstconnecttothedatabase:
>>> import sqlite3
>>> conn = sqlite3.connect('entertainment.db')
Aninteractivesessionshowshowdataisretrievedfromthedatabaseandhowitcanbeupdated:
>>> Movie('Star Wars').director
'George Lucas'
>>> jaws = Movie('Jaws')
>>> f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'
>>> Song('Country Roads').artist
'John Denver'
>>> Movie('Star Wars').director = 'J.J. Abrams'
(continuesonnextpage)
12

### 第13页

(continuedfrompreviouspage)
>>> Movie('Star Wars').director
'J.J. Abrams'
4 Pure Python Equivalents
Thedescriptorprotocolissimpleandoffersexcitingpossibilities. Severalusecasesaresocommonthattheyhave
beenprepackagedintobuilt-intools. Properties, boundmethods, staticmethods, classmethods, and__slots__are
allbasedonthedescriptorprotocol.
4.1 Properties
Callingproperty()isasuccinctwayofbuildingadatadescriptorthattriggersafunctioncalluponaccesstoan
attribute. Itssignatureis:
property(fget=None, fset=None, fdel=None, doc=None) -> property
Thedocumentationshowsatypicalusetodefineamanagedattributex:
class C:
def getx(self): return self.__x
def setx(self, value): self.__x = value
def delx(self): del self.__x
x = property(getx, setx, delx, "I'm the 'x' property.")
Toseehowproperty()isimplementedintermsofthedescriptorprotocol,hereisapurePythonequivalentthat
implementsmostofthecorefunctionality:
class Property:
"Emulate PyProperty_Type() in Objects/descrobject.c"
def __init__(self, fget=None, fset=None, fdel=None, doc=None):
self.fget = fget
self.fset = fset
self.fdel = fdel
if doc is None and fget is not None:
doc = fget.__doc__
self.__doc__ = doc
def __set_name__(self, owner, name):
self.__name__ = name
def __get__(self, obj, objtype=None):
if obj is None:
return self
if self.fget is None:
raise AttributeError
return self.fget(obj)
def __set__(self, obj, value):
if self.fset is None:
raise AttributeError
self.fset(obj, value)
def __delete__(self, obj):
if self.fdel is None:
raise AttributeError
(continuesonnextpage)
13

### 第14页

(continuedfrompreviouspage)
self.fdel(obj)
def getter(self, fget):
return type(self)(fget, self.fset, self.fdel, self.__doc__)
def setter(self, fset):
return type(self)(self.fget, fset, self.fdel, self.__doc__)
def deleter(self, fdel):
return type(self)(self.fget, self.fset, fdel, self.__doc__)
Theproperty()builtinhelpswheneverauserinterfacehasgrantedattributeaccessandthensubsequentchanges
requiretheinterventionofamethod.
Forinstance,aspreadsheetclassmaygrantaccesstoacellvaluethroughCell('b10').value. Subsequentim-
provementstotheprogramrequirethecelltoberecalculatedoneveryaccess; however, theprogrammerdoesnot
wanttoaffectexistingclientcodeaccessingtheattributedirectly. Thesolutionistowrapaccesstothevalueattribute
inapropertydatadescriptor:
class Cell:
...
@property
def value(self):
"Recalculate the cell before returning value"
self.recalc()
return self._value
Eitherthebuilt-inproperty()orourProperty()equivalentwouldworkinthisexample.
4.2 Functions and methods
Python’sobjectorientedfeaturesarebuiltuponafunctionbasedenvironment. Usingnon-datadescriptors,thetwo
aremergedseamlessly.
Functionsstoredinclassdictionariesgetturnedintomethodswheninvoked. Methodsonlydifferfromregularfunc-
tionsinthattheobjectinstanceisprependedtotheotherarguments. Byconvention,theinstanceiscalledself but
couldbecalledthisoranyothervariablename.
Methodscanbecreatedmanuallywithtypes.MethodTypewhichisroughlyequivalentto:
class MethodType:
"Emulate PyMethod_Type in Objects/classobject.c"
def __init__(self, func, obj):
self.__func__ = func
self.__self__ = obj
def __call__(self, *args, **kwargs):
func = self.__func__
obj = self.__self__
return func(obj, *args, **kwargs)
def __getattribute__(self, name):
"Emulate method_getset() in Objects/classobject.c"
if name == '__doc__':
return self.__func__.__doc__
return object.__getattribute__(self, name)
(continuesonnextpage)
14

### 第15页

(continuedfrompreviouspage)
def __getattr__(self, name):
"Emulate method_getattro() in Objects/classobject.c"
return getattr(self.__func__, name)
def __get__(self, obj, objtype=None):
"Emulate method_descr_get() in Objects/classobject.c"
return self
To support automatic creation of methods, functions include the __get__() method for binding methods during
attributeaccess. Thismeansthatfunctionsarenon-datadescriptorsthatreturnboundmethodsduringdottedlookup
fromaninstance. Here’showitworks:
class Function:
...
def __get__(self, obj, objtype=None):
"Simulate func_descr_get() in Objects/funcobject.c"
if obj is None:
return self
return MethodType(self, obj)
Runningthefollowingclassintheinterpretershowshowthefunctiondescriptorworksinpractice:
class D:
def f(self):
return self
class D2:
pass
Thefunctionhasaqualifiednameattributetosupportintrospection:
>>> D.f.__qualname__
'D.f'
Accessingthefunctionthroughtheclassdictionarydoesnotinvoke__get__(). Instead,itjustreturnstheunderlying
functionobject:
>>> D.__dict__['f']
<function D.f at 0x00C45070>
Dottedaccessfromaclasscalls__get__()whichjustreturnstheunderlyingfunctionunchanged:
>>> D.f
<function D.f at 0x00C45070>
Theinterestingbehavioroccursduringdottedaccessfromaninstance. Thedottedlookupcalls__get__()which
returnsaboundmethodobject:
>>> d = D()
>>> d.f
<bound method D.f of <__main__.D object at 0x00B18C90>>
Internally,theboundmethodstorestheunderlyingfunctionandtheboundinstance:
>>> d.f.__func__
<function D.f at 0x00C45070>
(continuesonnextpage)
15

### 第16页

(continuedfrompreviouspage)
>>> d.f.__self__
<__main__.D object at 0x00B18C90>
Ifyouhaveeverwonderedwhereselfcomesfrominregularmethodsorwhereclscomesfrominclassmethods,this
isit!
4.3 Kinds of methods
Non-datadescriptorsprovideasimplemechanismforvariationsontheusualpatternsofbindingfunctionsintometh-
ods.
Torecap,functionshavea__get__()methodsothattheycanbeconvertedtoamethodwhenaccessedasattributes.
The non-data descriptor transforms an obj.f(*args) call into f(obj, *args). Calling cls.f(*args) be-
comesf(*args).
Thischartsummarizesthebindinganditstwomostusefulvariants:
Transformation Calledfromanobject Calledfromaclass
function f(obj,*args) f(*args)
staticmethod f(*args) f(*args)
classmethod f(type(obj),*args) f(cls,*args)
4.4 Static methods
Staticmethodsreturntheunderlyingfunctionwithoutchanges. Callingeitherc.forC.fistheequivalentofadirect
lookup into object.__getattribute__(c, "f") or object.__getattribute__(C, "f"). As a result,
thefunctionbecomesidenticallyaccessiblefromeitheranobjectoraclass.
Goodcandidatesforstaticmethodsaremethodsthatdonotreferencetheselfvariable.
For instance, a statistics package may include a container class for experimental data. The class provides normal
methodsforcomputingtheaverage,mean,median,andotherdescriptivestatisticsthatdependonthedata. However,
theremaybeusefulfunctionswhichareconceptuallyrelatedbutdonotdependonthedata. Forinstance,erf(x)is
handyconversionroutinethatcomesupinstatisticalworkbutdoesnotdirectlydependonaparticulardataset. Itcan
becalledeitherfromanobjectortheclass: s.erf(1.5) --> 0.9332orSample.erf(1.5) --> 0.9332.
Sincestaticmethodsreturntheunderlyingfunctionwithnochanges,theexamplecallsareunexciting:
class E:
@staticmethod
def f(x):
return x * 10
>>> E.f(3)
30
>>> E().f(3)
30
Usingthenon-datadescriptorprotocol,apurePythonversionofstaticmethod()wouldlooklikethis:
import functools
class StaticMethod:
"Emulate PyStaticMethod_Type() in Objects/funcobject.c"
def __init__(self, f):
(continuesonnextpage)
16

| Transformation | Calledfromanobject | Calledfromaclass |
| --- | --- | --- |
| function | f(obj,*args) | f(*args) |
| staticmethod | f(*args) | f(*args) |
| classmethod | f(type(obj),*args) | f(cls,*args) |

### 第17页

(continuedfrompreviouspage)
self.f = f
functools.update_wrapper(self, f)
def __get__(self, obj, objtype=None):
return self.f
def __call__(self, *args, **kwds):
return self.f(*args, **kwds)
@property
def __annotations__(self):
return self.f.__annotations__
Thefunctools.update_wrapper()calladdsa__wrapped__attributethatreferstotheunderlyingfunction.
Also it carries forward the attributes necessary to make the wrapper look like the wrapped function, including
__name__,__qualname__,and__doc__.
4.5 Class methods
Unlikestaticmethods,classmethodsprependtheclassreferencetotheargumentlistbeforecallingthefunction. This
formatisthesameforwhetherthecallerisanobjectoraclass:
class F:
@classmethod
def f(cls, x):
return cls.__name__, x
>>> F.f(3)
('F', 3)
>>> F().f(3)
('F', 3)
Thisbehaviorisusefulwheneverthemethodonlyneedstohaveaclassreferenceanddoesnotrelyondatastoredin
aspecificinstance. Oneuseforclassmethodsistocreatealternateclassconstructors. Forexample,theclassmethod
dict.fromkeys()createsanewdictionaryfromalistofkeys. ThepurePythonequivalentis:
class Dict(dict):
@classmethod
def fromkeys(cls, iterable, value=None):
"Emulate dict_fromkeys() in Objects/dictobject.c"
d = cls()
for key in iterable:
d[key] = value
return d
Nowanewdictionaryofuniquekeyscanbeconstructedlikethis:
>>> d = Dict.fromkeys('abracadabra')
>>> type(d) is Dict
True
>>> d
{'a': None, 'b': None, 'r': None, 'c': None, 'd': None}
Usingthenon-datadescriptorprotocol,apurePythonversionofclassmethod()wouldlooklikethis:
import functools
(continuesonnextpage)
17

### 第18页

(continuedfrompreviouspage)
class ClassMethod:
"Emulate PyClassMethod_Type() in Objects/funcobject.c"
def __init__(self, f):
self.f = f
functools.update_wrapper(self, f)
def __get__(self, obj, cls=None):
if cls is None:
cls = type(obj)
return MethodType(self.f, cls)
The functools.update_wrapper() call in ClassMethod adds a __wrapped__ attribute that refers to the
underlying function. Also it carries forward the attributes necessary to make the wrapper look like the wrapped
function: __name__,__qualname__,__doc__,and__annotations__.
4.6 Member objects and __slots__
Whenaclassdefines__slots__,itreplacesinstancedictionarieswithafixed-lengtharrayofslotvalues. Froma
userpointofviewthathasseveraleffects:
1. Providesimmediatedetectionofbugsduetomisspelledattributeassignments. Onlyattributenamesspecifiedin
__slots__areallowed:
class Vehicle:
__slots__ = ('id_number', 'make', 'model')
>>> auto = Vehicle()
>>> auto.id_nubmer = 'VYE483814LQEX'
Traceback (most recent call last):
...
AttributeError: 'Vehicle' object has no attribute 'id_nubmer'
2. Helpscreateimmutableobjectswheredescriptorsmanageaccesstoprivateattributesstoredin__slots__:
class Immutable:
__slots__ = ('_dept', '_name') # Replace the instance dictionary
def __init__(self, dept, name):
self._dept = dept # Store to private attribute
self._name = name # Store to private attribute
@property # Read-only descriptor
def dept(self):
return self._dept
@property
def name(self): # Read-only descriptor
return self._name
>>> mark = Immutable('Botany', 'Mark Watney')
>>> mark.dept
'Botany'
>>> mark.dept = 'Space Pirate'
Traceback (most recent call last):
...
(continuesonnextpage)
18

### 第19页

(continuedfrompreviouspage)
AttributeError: property 'dept' of 'Immutable' object has no setter
>>> mark.location = 'Mars'
Traceback (most recent call last):
...
AttributeError: 'Immutable' object has no attribute 'location'
3. Savesmemory. Ona64-bitLinuxbuild,aninstancewithtwoattributestakes48byteswith__slots__and152
bytes without. This flyweight design pattern likely only matters when a large number of instances are going to be
created.
4. Improvesspeed. Readinginstancevariablesis35%fasterwith__slots__(asmeasuredwithPython3.10onan
AppleM1processor).
5. Blockstoolslikefunctools.cached_property()whichrequireaninstancedictionarytofunctioncorrectly:
from functools import cached_property
class CP:
__slots__ = () # Eliminates the instance dict
@cached_property # Requires an instance dict
def pi(self):
return 4 * sum((-1.0)**n / (2.0*n + 1.0)
for n in reversed(range(100_000)))
>>> CP().pi
Traceback (most recent call last):
...
TypeError: No '__dict__' attribute on 'CP' instance to cache 'pi' property.
Itisnotpossibletocreateanexactdrop-inpurePythonversionof__slots__becauseitrequiresdirectaccessto
Cstructuresandcontroloverobjectmemoryallocation. However,wecanbuildamostlyfaithfulsimulationwhere
theactualCstructureforslotsisemulatedbyaprivate_slotvalueslist. Readsandwritestothatprivatestructure
aremanagedbymemberdescriptors:
null = object()
class Member:
def __init__(self, name, clsname, offset):
'Emulate PyMemberDef in Include/structmember.h'
# Also see descr_new() in Objects/descrobject.c
self.name = name
self.clsname = clsname
self.offset = offset
def __get__(self, obj, objtype=None):
'Emulate member_get() in Objects/descrobject.c'
# Also see PyMember_GetOne() in Python/structmember.c
if obj is None:
return self
value = obj._slotvalues[self.offset]
if value is null:
raise AttributeError(self.name)
return value
def __set__(self, obj, value):
(continuesonnextpage)
19

### 第20页

(continuedfrompreviouspage)
'Emulate member_set() in Objects/descrobject.c'
obj._slotvalues[self.offset] = value
def __delete__(self, obj):
'Emulate member_delete() in Objects/descrobject.c'
value = obj._slotvalues[self.offset]
if value is null:
raise AttributeError(self.name)
obj._slotvalues[self.offset] = null
def __repr__(self):
'Emulate member_repr() in Objects/descrobject.c'
return f'<Member {self.name!r} of {self.clsname!r}>'
Thetype.__new__()methodtakescareofaddingmemberobjectstoclassvariables:
class Type(type):
'Simulate how the type metaclass adds member objects for slots'
def __new__(mcls, clsname, bases, mapping, **kwargs):
'Emulate type_new() in Objects/typeobject.c'
# type_new() calls PyTypeReady() which calls add_methods()
slot_names = mapping.get('slot_names', [])
for offset, name in enumerate(slot_names):
mapping[name] = Member(name, clsname, offset)
return type.__new__(mcls, clsname, bases, mapping, **kwargs)
Theobject.__new__()methodtakescareofcreatinginstancesthathaveslotsinsteadofaninstancedictionary.
HereisaroughsimulationinpurePython:
class Object:
'Simulate how object.__new__() allocates memory for __slots__'
def __new__(cls, *args, **kwargs):
'Emulate object_new() in Objects/typeobject.c'
inst = super().__new__(cls)
if hasattr(cls, 'slot_names'):
empty_slots = [null] * len(cls.slot_names)
object.__setattr__(inst, '_slotvalues', empty_slots)
return inst
def __setattr__(self, name, value):
'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
cls = type(self)
if hasattr(cls, 'slot_names') and name not in cls.slot_names:
raise AttributeError(
f'{cls.__name__!r} object has no attribute {name!r}'
)
super().__setattr__(name, value)
def __delattr__(self, name):
'Emulate _PyObject_GenericSetAttrWithDict() Objects/object.c'
cls = type(self)
if hasattr(cls, 'slot_names') and name not in cls.slot_names:
raise AttributeError(
f'{cls.__name__!r} object has no attribute {name!r}'
)
(continuesonnextpage)
20

### 第21页

(continuedfrompreviouspage)
super().__delattr__(name)
Tousethesimulationinarealclass,justinheritfromObjectandsetthemetaclasstoType:
class H(Object, metaclass=Type):
'Instance variables stored in slots'
slot_names = ['x', 'y']
def __init__(self, x, y):
self.x = x
self.y = y
Atthispoint,themetaclasshasloadedmemberobjectsforxandy:
>>> from pprint import pp
>>> pp(dict(vars(H)))
{'__module__': '__main__',
'__doc__': 'Instance variables stored in slots',
'slot_names': ['x', 'y'],
'__init__': <function H.__init__ at 0x7fb5d302f9d0>,
'x': <Member 'x' of 'H'>,
'y': <Member 'y' of 'H'>}
Wheninstancesarecreated,theyhaveaslot_valueslistwheretheattributesarestored:
>>> h = H(10, 20)
>>> vars(h)
{'_slotvalues': [10, 20]}
>>> h.x = 55
>>> vars(h)
{'_slotvalues': [55, 20]}
Misspelledorunassignedattributeswillraiseanexception:
>>> h.xz
Traceback (most recent call last):
...
AttributeError: 'H' object has no attribute 'xz'
21

