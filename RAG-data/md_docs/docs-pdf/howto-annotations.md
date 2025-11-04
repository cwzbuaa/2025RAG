### 第1页

Annotations Best Practices
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 AccessingTheAnnotationsDictOfAnObjectInPython3.10AndNewer 1
2 AccessingTheAnnotationsDictOfAnObjectInPython3.9AndOlder 2
3 ManuallyUn-StringizingStringizedAnnotations 3
4 BestPracticesFor__annotations__InAnyPythonVersion 3
5 __annotations__Quirks 3
Index 5
author
LarryHastings
Abstract
This document is designed to encapsulate the best practices for working with annotations dicts. If you write
Pythoncodethatexamines__annotations__onPythonobjects, weencourageyoutofollowtheguidelines
describedbelow.
Thedocumentisorganizedintofoursections: bestpracticesforaccessingtheannotationsofanobjectinPython
versions3.10andnewer,bestpracticesforaccessingtheannotationsofanobjectinPythonversions3.9andolder,
otherbestpracticesfor__annotations__thatapplytoanyPythonversion,andquirksof__annotations__.
Note that this document is specifically about working with __annotations__, not uses for annotations. If
you’relookingforinformationonhowtouse“typehints”inyourcode,pleaseseethetypingmodule.
1 Accessing The Annotations Dict Of An Object In Python 3.10 And
Newer
Python3.10addsanewfunctiontothestandardlibrary: inspect.get_annotations(). InPythonversions3.10
through3.13,callingthisfunctionisthebestpracticeforaccessingtheannotationsdictofanyobjectthatsupports
annotations. Thisfunctioncanalso“un-stringize”stringizedannotationsforyou.
1

### 第2页

In Python 3.14, there is a new annotationlib module with functionality for working with annotations. This
includesaannotationlib.get_annotations()function,whichsupersedesinspect.get_annotations().
If for some reason inspect.get_annotations() isn’t viable for your use case, you may access the
__annotations__ data member manually. Best practice for this changed in Python 3.10 as well: as of Python
3.10, o.__annotations__ is guaranteed to always work on Python functions, classes, and modules. If you’re
certaintheobjectyou’reexaminingisoneofthesethreespecificobjects,youmaysimplyuseo.__annotations__
togetattheobject’sannotationsdict.
However, other types of callables–for example, callables created by functools.partial()–may not have an
__annotations__attributedefined. Whenaccessingthe__annotations__ofapossiblyunknownobject,best
practiceinPythonversions3.10andneweristocallgetattr()withthreearguments,forexamplegetattr(o,
'__annotations__', None).
BeforePython3.10,accessing__annotations__onaclassthatdefinesnoannotationsbutthathasaparentclass
withannotationswouldreturntheparent’s__annotations__. InPython3.10andnewer,thechildclass’sannota-
tionswillbeanemptydictinstead.
2 Accessing The Annotations Dict Of An Object In Python 3.9 And
Older
InPython3.9andolder,accessingtheannotationsdictofanobjectismuchmorecomplicatedthaninnewerversions.
TheproblemisadesignflawintheseolderversionsofPython,specificallytodowithclassannotations.
Bestpracticeforaccessingtheannotationsdictofotherobjects–functions,othercallables,andmodules–isthesameas
bestpracticefor3.10,assumingyouaren’tcallinginspect.get_annotations(): youshouldusethree-argument
getattr()toaccesstheobject’s__annotations__attribute.
Unfortunately,thisisn’tbestpracticeforclasses. Theproblemisthat,since__annotations__isoptionalonclasses,
andbecauseclassescaninheritattributesfromtheirbaseclasses, accessingthe__annotations__ attributeofa
classmayinadvertentlyreturntheannotationsdictofabaseclass. Asanexample:
class Base:
a: int = 3
b: str = 'abc'
class Derived(Base):
pass
print(Derived.__annotations__)
ThiswillprinttheannotationsdictfromBase,notDerived.
Yourcodewillhavetohaveaseparatecodepathiftheobjectyou’reexaminingisaclass(isinstance(o, type)).
In that case, best practice relies on an implementation detail of Python 3.9 and before: if a class has annotations
defined,theyarestoredintheclass’s__dict__dictionary. Sincetheclassmayormaynothaveannotationsdefined,
bestpracticeistocalltheget()methodontheclassdict.
Toputitalltogether,hereissomesamplecodethatsafelyaccessesthe__annotations__attributeonanarbitrary
objectinPython3.9andbefore:
if isinstance(o, type):
ann = o.__dict__.get('__annotations__', None)
else:
ann = getattr(o, '__annotations__', None)
Afterrunningthiscode,annshouldbeeitheradictionaryorNone. You’reencouragedtodouble-checkthetypeof
annusingisinstance()beforefurtherexamination.
Notethatsomeexoticormalformedtypeobjectsmaynothavea__dict__attribute,soforextrasafetyyoumay
alsowishtousegetattr()toaccess__dict__.
2

### 第3页

3 Manually Un-Stringizing Stringized Annotations
In situations where some annotations may be “stringized”, and you wish to evaluate those strings to produce the
Pythonvaluestheyrepresent,itreallyisbesttocallinspect.get_annotations()todothisworkforyou.
Ifyou’reusingPython3.9orolder,orifforsomereasonyoucan’tuseinspect.get_annotations(),you’llneed
toduplicateitslogic. You’reencouragedtoexaminetheimplementationofinspect.get_annotations()inthe
currentPythonversionandfollowasimilarapproach.
Inanutshell,ifyouwishtoevaluateastringizedannotationonanarbitraryobjecto:
• Ifoisamodule,useo.__dict__astheglobalswhencallingeval().
• Ifoisaclass,usesys.modules[o.__module__].__dict__astheglobals,anddict(vars(o))as
thelocals,whencallingeval().
• Ifoisawrappedcallableusingfunctools.update_wrapper(),functools.wraps(),orfunctools.
partial(),iterativelyunwrapitbyaccessingeithero.__wrapped__oro.funcasappropriate,untilyou
havefoundtherootunwrappedfunction.
• Ifoisacallable(butnotaclass),useo.__globals__astheglobalswhencallingeval().
However,notallstringvaluesusedasannotationscanbesuccessfullyturnedintoPythonvaluesbyeval(). String
valuescouldtheoreticallycontainanyvalidstring,andinpracticetherearevalidusecasesfortypehintsthatrequire
annotatingwithstringvaluesthatspecificallycan’tbeevaluated. Forexample:
• PEP604uniontypesusing|,beforesupportforthiswasaddedtoPython3.10.
• Definitionsthataren’tneededatruntime,onlyimportedwhentyping.TYPE_CHECKINGistrue.
Ifeval()attemptstoevaluatesuchvalues,itwillfailandraiseanexception. So,whendesigningalibraryAPIthat
workswithannotations,it’srecommendedtoonlyattempttoevaluatestringvalueswhenexplicitlyrequestedtoby
thecaller.
4 Best Practices For __annotations__ In Any Python Version
• Youshouldavoidassigningtothe__annotations__memberofobjectsdirectly. LetPythonmanagesetting
__annotations__.
• Ifyoudoassigndirectlytothe__annotations__memberofanobject,youshouldalwayssetittoadict
object.
• You should avoid accessing __annotations__ directly on any object. Instead, use annotationlib.
get_annotations()(Python3.14+)orinspect.get_annotations()(Python3.10+).
• Ifyoudodirectlyaccessthe__annotations__memberofanobject,youshouldensurethatit’sadictionary
beforeattemptingtoexamineitscontents.
• Youshouldavoidmodifying__annotations__dicts.
• Youshouldavoiddeletingthe__annotations__attributeofanobject.
5 __annotations__ Quirks
InallversionsofPython3,functionobjectslazy-createanannotationsdictifnoannotationsaredefinedonthatobject.
You can delete the __annotations__ attribute using del fn.__annotations__, but if you then access fn.
__annotations__theobjectwillcreateanewemptydictthatitwillstoreandreturnasitsannotations. Deleting
theannotationsonafunctionbeforeithaslazilycreateditsannotationsdictwillthrowanAttributeError;using
del fn.__annotations__twiceinarowisguaranteedtoalwaysthrowanAttributeError.
EverythingintheaboveparagraphalsoappliestoclassandmoduleobjectsinPython3.10andnewer.
InallversionsofPython3,youcanset__annotations__onafunctionobjecttoNone. However,subsequently
accessingtheannotationsonthatobjectusingfn.__annotations__willlazy-createanemptydictionaryasper
3

### 第4页

thefirstparagraphofthissection. Thisisnottrueofmodulesandclasses,inanyPythonversion;thoseobjectspermit
setting__annotations__toanyPythonvalue,andwillretainwhatevervalueisset.
IfPythonstringizesyourannotationsforyou(usingfrom __future__ import annotations),andyouspecify
astringasanannotation,thestringwillitselfbequoted. Ineffecttheannotationisquotedtwice. Forexample:
from __future__ import annotations
def foo(a: "str"): pass
print(foo.__annotations__)
Thisprints{'a': "'str'"}. Thisshouldn’treallybeconsidereda“quirk”;it’smentionedheresimplybecauseit
mightbesurprising.
Ifyouuseaclasswithacustommetaclassandaccess__annotations__ontheclass,youmayobserveunexpected
behavior;see749forsomeexamples. Youcanavoidthesequirksbyusingannotationlib.get_annotations()
on Python 3.14+ or inspect.get_annotations() on Python 3.10+. On earlier versions of Python, you
can avoid these bugs by accessing the annotations from the class’s __dict__ (for example, cls.__dict__.
get('__annotations__', None)).
In some versions of Python, instances of classes may have an __annotations__ attribute. However, this is not
supported functionality. If you need the annotations of an instance, you can use type() to access its class (for
example,annotationlib.get_annotations(type(myinstance))onPython3.14+).
4

### 第5页

Index
P
Python Enhancement Proposals
PEP 604,3
PEP 749#pep749-metaclasses,4
5

