### 第1页

A Conceptual Overview of asyncio
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Aconceptualoverviewpart1: thehigh-level 2
1.1 EventLoop . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Asynchronousfunctionsandcoroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 await . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Aconceptualoverviewpart2: thenutsandbolts 6
2.1 Theinnerworkingsofcoroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Futures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Ahomemadeasyncio.sleep . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
ThisHOWTOarticleseekstohelpyoubuildasturdymentalmodelofhowasynciofundamentallyworks,helping
youunderstandthehowandwhybehindtherecommendedpatterns.
Youmightbecuriousaboutsomekeyasyncioconcepts. You’llbecomfortablyabletoanswerthesequestionsby
theendofthisarticle:
• What’shappeningbehindthesceneswhenanobjectisawaited?
• Howdoesasynciodifferentiatebetweenataskwhichdoesn’tneedCPU-time(suchasanetworkrequestor
fileread)asopposedtoataskthatdoes(suchascomputingn-factorial)?
• Howtowriteanasynchronousvariantofanoperation,suchasanasyncsleepordatabaserequest.
(cid:181) Seealso
• TheguidethatinspiredthisHOWTOarticle,byAlexanderNordin.
• Thisin-depthYouTubetutorialseriesonasynciocreatedbyPythoncoreteammember,ŁukaszLanga.
• 500 Lines or Less: A Web Crawler With asyncio Coroutines by A. Jesse Jiryu Davis and Guido van
Rossum.
1

| (cid:181) Seealso |
| --- |
| • TheguidethatinspiredthisHOWTOarticle,byAlexanderNordin.
• Thisin-depthYouTubetutorialseriesonasynciocreatedbyPythoncoreteammember,ŁukaszLanga.
• 500 Lines or Less: A Web Crawler With asyncio Coroutines by A. Jesse Jiryu Davis and Guido van
Rossum. |

### 第2页

1 A conceptual overview part 1: the high-level
Inpart1,we’llcoverthemain,high-levelbuildingblocksofasyncio: theeventloop,coroutinefunctions,coroutine
objects,tasksandawait.
1.1 Event Loop
Everythinginasynciohappensrelativetotheeventloop. It’sthestaroftheshow. It’slikeanorchestraconductor.
It’sbehindthescenesmanagingresources. Somepowerisexplicitlygrantedtoit,butalotofitsabilitytogetthings
donecomesfromtherespectandcooperationofitsworkerbees.
Inmoretechnicalterms,theeventloopcontainsacollectionofjobstoberun. Somejobsareaddeddirectlybyyou,
andsomeindirectlybyasyncio. Theeventlooptakesajobfromitsbacklogofworkandinvokesit(or“givesit
control”),similartocallingafunction,andthenthatjobruns. Onceitpausesorcompletes,itreturnscontroltothe
event loop. The event loop will then select another job from its pool and invoke it. You can roughly think of the
collectionofjobsasaqueue: jobsareaddedandthenprocessedoneatatime,generally(butnotalways)inorder.
Thisprocessrepeatsindefinitelywiththeeventloopcyclingendlesslyonwards. Iftherearenomorejobspending
execution,theeventloopissmartenoughtorestandavoidneedlesslywastingCPUcycles,andwillcomebackwhen
there’smoreworktobedone.
Effectiveexecutionreliesonjobssharingwellandcooperating; agreedyjobcouldhogcontrolandleavetheother
jobstostarve,renderingtheoveralleventloopapproachratheruseless.
import asyncio
# This creates an event loop and indefinitely cycles through
# its collection of jobs.
event_loop = asyncio.new_event_loop()
event_loop.run_forever()
1.2 Asynchronous functions and coroutines
Thisisabasic,boringPythonfunction:
def hello_printer():
print(
"Hi, I am a lowly, simple printer, though I have all I "
"need in life -- \nfresh paper and my dearly beloved octopus "
"partner in crime."
)
Callingaregularfunctioninvokesitslogicorbody:
>>> hello_printer()
Hi, I am a lowly, simple printer, though I have all I need in life --
fresh paper and my dearly beloved octopus partner in crime.
Theasyncdef,asopposedtojustaplaindef,makesthisanasynchronousfunction(or“coroutinefunction”). Calling
itcreatesandreturnsacoroutineobject.
async def loudmouth_penguin(magic_number: int):
print(
"I am a super special talking penguin. Far cooler than that printer. "
f"By the way, my lucky number is: {magic_number}."
)
Callingtheasyncfunction,loudmouth_penguin,doesnotexecutetheprintstatement;instead,itcreatesacoroutine
object:
2

### 第3页

>>> loudmouth_penguin(magic_number=3)
<coroutine object loudmouth_penguin at 0x104ed2740>
Theterms“coroutinefunction”and“coroutineobject”areoftenconflatedascoroutine. Thatcanbeconfusing! Inthis
article,coroutinespecificallyreferstoacoroutineobject,ormoreprecisely,aninstanceoftypes.CoroutineType
(nativecoroutine). Notethatcoroutinescanalsoexistasinstancesofcollections.abc.Coroutine–adistinc-
tionthatmattersfortypechecking.
Acoroutinerepresentsthefunction’sbodyorlogic. Acoroutinehastobeexplicitlystarted;again,merelycreatingthe
coroutinedoesnotstartit. Notably,thecoroutinecanbepausedandresumedatvariouspointswithinthefunction’s
body. Thatpausingandresumingabilityiswhatallowsforasynchronousbehavior!
Coroutinesandcoroutinefunctionswerebuiltbyleveragingthefunctionalityofgeneratorsandgeneratorfunctions.
Recall,ageneratorfunctionisafunctionthatyields,likethisone:
def get_random_number():
# This would be a bad random number generator!
print("Hi")
yield 1
print("Hello")
yield 7
print("Howdy")
yield 4
...
Similartoacoroutinefunction,callingageneratorfunctiondoesnotrunit. Instead,itcreatesageneratorobject:
>>> get_random_number()
<generator object get_random_number at 0x1048671c0>
Youcanproceedtothenextyieldofageneratorbyusingthebuilt-infunctionnext(). Inotherwords,thegenerator
runs,thenpauses. Forexample:
>>> generator = get_random_number()
>>> next(generator)
Hi
1
>>> next(generator)
Hello
7
1.3 Tasks
Roughlyspeaking,tasksarecoroutines(notcoroutinefunctions)tiedtoaneventloop. Ataskalsomaintainsalist
ofcallbackfunctionswhoseimportancewillbecomeclearinamomentwhenwediscussawait. Therecommended
waytocreatetasksisviaasyncio.create_task().
Creatingataskautomaticallyschedulesitforexecution(byaddingacallbacktorunitintheeventloop’sto-dolist,
thatis,collectionofjobs).
Sincethere’sonlyoneeventloop(ineachthread),asynciotakescareofassociatingthetaskwiththeeventloopfor
you. Assuch,there’snoneedtospecifytheeventloop.
coroutine = loudmouth_penguin(magic_number=5)
# This creates a Task object and schedules its execution via the event loop.
task = asyncio.create_task(coroutine)
Earlier, we manually created the event loop and set it to run forever. In practice, it’s recommended to use (and
commontosee)asyncio.run(),whichtakescareofmanagingtheeventloopandensuringtheprovidedcoroutine
finishesbeforeadvancing. Forexample,manyasyncprogramsfollowthissetup:
3

### 第4页

import asyncio
async def main():
# Perform all sorts of wacky, wild asynchronous things...
...
if __name__ == "__main__":
asyncio.run(main())
# The program will not reach the following print statement until the
# coroutine main() finishes.
print("coroutine main() is done!")
It’simportanttobeawarethatthetaskitselfisnotaddedtotheeventloop,onlyacallbacktothetaskis. Thismatters
if the task object you created is garbage collected before it’s called by the event loop. For example, consider this
program:
async def hello():
1
print("hello!")
2
3
async def main():
4
asyncio.create_task(hello())
5
# Other asynchronous instructions which run for a while
6
# and cede control to the event loop...
7
...
8
9
asyncio.run(main())
10
Becausethere’snoreferencetothetaskobjectcreatedonline5,itmightbegarbagecollectedbeforetheeventloop
invokes it. Later instructions in the coroutine main() hand control back to the event loop so it can invoke other
jobs. Whentheeventloopeventuallytriestorunthetask,itmightfailanddiscoverthetaskobjectdoesnotexist!
Thiscanalsohappenevenifacoroutinekeepsareferencetoataskbutcompletesbeforethattaskfinishes. When
thecoroutineexits,localvariablesgooutofscopeandmaybesubjecttogarbagecollection. Inpractice,asyncio
andPython’sgarbagecollectorworkprettyhardtoensurethissortofthingdoesn’thappen. Butthat’snoreasonto
bereckless!
1.4 await
awaitisaPythonkeywordthat’scommonlyusedinoneoftwodifferentways:
await task
await coroutine
Inacrucialway,thebehaviorofawaitdependsonthetypeofobjectbeingawaited.
Awaitingataskwillcedecontrolfromthecurrenttaskorcoroutinetotheeventloop. Intheprocessofrelinquishing
control,afewimportantthingshappen. We’llusethefollowingcodeexampletoillustrate:
async def plant_a_tree():
dig_the_hole_task = asyncio.create_task(dig_the_hole())
await dig_the_hole_task
# Other instructions associated with planting a tree.
...
Inthisexample,imaginetheeventloophaspassedcontroltothestartofthecoroutineplant_a_tree(). Asseen
above,thecoroutinecreatesataskandthenawaitsit. Theawait dig_the_hole_taskinstructionaddsacallback
(which will resume plant_a_tree()) to the dig_the_hole_task object’s list of callbacks. And then, the in-
structioncedescontroltotheeventloop. Sometimelater,theeventloopwillpasscontroltodig_the_hole_task
4

### 第5页

andthetaskwillfinishwhateveritneedstodo. Oncethetaskfinishes,itwilladditsvariouscallbackstotheevent
loop,inthiscase,acalltoresumeplant_a_tree().
Generally speaking, when the awaited task finishes (dig_the_hole_task), the original task or coroutine
(plant_a_tree())isaddedbacktotheeventloopsto-dolisttoberesumed.
This is a basic, yet reliable mental model. In practice, the control handoffs are slightly more complex, but not by
much. Inpart2,we’llwalkthroughthedetailsthatmakethispossible.
Unliketasks,awaitingacoroutinedoesnothandcontrolbacktotheeventloop! Wrappingacoroutineinatask
first,thenawaitingthatwouldcedecontrol. Thebehaviorofawait coroutineiseffectivelythesameasinvoking
aregular,synchronousPythonfunction. Considerthisprogram:
import asyncio
async def coro_a():
print("I am coro_a(). Hi!")
async def coro_b():
print("I am coro_b(). I sure hope no one hogs the event loop...")
async def main():
task_b = asyncio.create_task(coro_b())
num_repeats = 3
for _ in range(num_repeats):
await coro_a()
await task_b
asyncio.run(main())
Thefirststatementinthecoroutinemain()createstask_bandschedulesitforexecutionviatheeventloop. Then,
coro_a()isrepeatedlyawaited. Controlnevercedestotheeventloopwhichiswhyweseetheoutputofallthree
coro_a()invocationsbeforecoro_b()’soutput:
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_b(). I sure hope no one hogs the event loop...
If we change await coro_a() to await asyncio.create_task(coro_a()), the behavior changes. The
coroutine main() cedes control to the event loop with that statement. The event loop then proceeds through its
backlogofwork,callingtask_bandthenthetaskwhichwrapscoro_a()beforeresumingthecoroutinemain().
I am coro_b(). I sure hope no one hogs the event loop...
I am coro_a(). Hi!
I am coro_a(). Hi!
I am coro_a(). Hi!
Thisbehaviorofawait coroutinecantripalotofpeopleup! Thatexamplehighlightshowusingonlyawait
coroutinecouldunintentionallyhogcontrolfromothertasksandeffectivelystalltheeventloop. asyncio.run()
canhelpyoudetectsuchoccurencesviathedebug=Trueflagwhichaccordinglyenablesdebugmode. Amongother
things,itwillloganycoroutinesthatmonopolizeexecutionfor100msorlonger.
Thedesignintentionallytradesoffsomeconceptualclarityaroundusageofawaitforimprovedperformance. Each
timeataskisawaited,controlneedstobepassedallthewayupthecallstacktotheeventloop. Thatmightsound
minor, but in a large program with many await’s and a deep callstack that overhead can add up to a meaningful
performancedrag.
5

### 第6页

2 A conceptual overview part 2: the nuts and bolts
Part 2 goes into detail on the mechanisms asyncio uses to manage control flow. This is where the magic hap-
pens. You’llcomeawayfromthissectionknowingwhatawaitdoesbehindthescenesandhowtomakeyourown
asynchronousoperators.
2.1 The inner workings of coroutines
asyncioleveragesfourcomponentstopassaroundcontrol.
coroutine.send(arg)isthemethodusedtostartorresumeacoroutine. Ifthecoroutinewaspausedandisnow
beingresumed,theargumentargwillbesentinasthereturnvalueoftheyieldstatementwhichoriginallypaused
it. Ifthecoroutineisbeingusedforthefirsttime(asopposedtobeingresumed)argmustbeNone.
class Rock:
1
def __await__(self):
2
value_sent_in = yield 7
3
print(f"Rock.__await__ resuming with value: {value_sent_in}.")
4
return value_sent_in
5
6
async def main():
7
print("Beginning coroutine main().")
8
rock = Rock()
9
print("Awaiting rock...")
10
value_from_rock = await rock
11
print(f"Coroutine received value: {value_from_rock} from rock.")
12
return 23
13
14
coroutine = main()
15
intermediate_result = coroutine.send(None)
16
print(f"Coroutine paused and returned intermediate value: {intermediate_result}.")
17
18
print(f"Resuming coroutine and sending in value: 42.")
19
try:
20
coroutine.send(42)
21
except StopIteration as e:
22
returned_value = e.value
23
print(f"Coroutine main() finished and provided value: {returned_value}.")
24
yield,likeusual,pausesexecutionandreturnscontroltothecaller. Intheexampleabove,theyield,online3,is
calledby... = await rockonline11. Morebroadlyspeaking,awaitcallsthe__await__()methodofthe
givenobject. awaitalsodoesonemoreveryspecialthing: itpropagates(or“passesalong”)anyyieldsitreceives
upthecall-chain. Inthiscase,that’sbackto... = coroutine.send(None)online16.
Thecoroutineisresumedviathecoroutine.send(42)callonline21. Thecoroutinepicksbackupfromwhere
ityielded(orpaused)online3andexecutestheremainingstatementsinitsbody. Whenacoroutinefinishes, it
raisesaStopIterationexceptionwiththereturnvalueattachedinthevalueattribute.
Thatsnippetproducesthisoutput:
Beginning coroutine main().
Awaiting rock...
Coroutine paused and returned intermediate value: 7.
Resuming coroutine and sending in value: 42.
Rock.__await__ resuming with value: 42.
Coroutine received value: 42 from rock.
Coroutine main() finished and provided value: 23.
It’s worth pausing for a moment here and making sure you followed the various ways that control flow and values
werepassed. Alotofimportantideaswerecoveredandit’sworthensuringyourunderstandingisfirm.
6

### 第7页

The only way to yield (or effectively cede control) from a coroutine is to await an object that yields in its
__await__method. Thatmightsoundoddtoyou. Youmightbethinking:
1. What about a yield directly within the coroutine function? The coroutine function becomes an
asyncgeneratorfunction,adifferentbeastentirely.
2. Whataboutayieldfromwithinthecoroutinefunctiontoa(plain)generator? Thatcausestheerror:
SyntaxError: yield from not allowed in a coroutine. This was intentionally designed
for the sake of simplicity – mandating only one way of using coroutines. Initially yield was barred
as well, but was re-accepted to allow for async generators. Despite that, yield from and await
effectivelydothesamething.
2.2 Futures
Afutureisanobjectmeanttorepresentacomputation’sstatusandresult. Thetermisanodtotheideaofsomething
stilltocomeornotyethappened,andtheobjectisawaytokeepaneyeonthatsomething.
Afuturehasafewimportantattributes. Oneisitsstatewhichcanbeeither“pending”,“cancelled”or“done”. Another
isitsresult,whichissetwhenthestatetransitionstodone. Unlikeacoroutine,afuturedoesnotrepresenttheactual
computation to be done; instead, it represents the status and result of that computation, kind of like a status light
(red,yelloworgreen)orindicator.
asyncio.Task subclasses asyncio.Future in order to gain these various capabilities. The prior section said
tasks store a list of callbacks, which wasn’t entirely accurate. It’s actually the Future class that implements this
logic,whichTaskinherits.
Futuresmayalsobeuseddirectly(notviatasks). Tasksmarkthemselvesasdonewhentheircoroutineiscomplete.
Futuresaremuchmoreversatileandwillbemarkedasdonewhenyousayso. Inthisway,they’retheflexibleinterface
foryoutomakeyourownconditionsforwaitingandresuming.
2.3 A homemade asyncio.sleep
We’llgothroughanexampleofhowyoucouldleverageafuturetocreateyourownvariantofasynchronoussleep
(async_sleep)whichmimicsasyncio.sleep().
This snippet registers a few tasks with the event loop and then awaits a coroutine wrapped in a task:
async_sleep(3). Wewantthattasktofinishonlyafterthreesecondshaveelapsed,butwithoutpreventingother
tasksfromrunning.
async def other_work():
print("I like work. Work work.")
async def main():
# Add a few other tasks to the event loop, so there's something
# to do while asynchronously sleeping.
work_tasks = [
asyncio.create_task(other_work()),
asyncio.create_task(other_work()),
asyncio.create_task(other_work())
]
print(
"Beginning asynchronous sleep at time: "
f"{datetime.datetime.now().strftime("%H:%M:%S")}."
)
await asyncio.create_task(async_sleep(3))
print(
"Done asynchronous sleep at time: "
f"{datetime.datetime.now().strftime("%H:%M:%S")}."
)
# asyncio.gather effectively awaits each task in the collection.
await asyncio.gather(*work_tasks)
7

### 第8页

Below, we use a future to enable custom control over when that task will be marked as done. If future.
set_result()(themethodresponsibleformarkingthatfutureasdone)isnevercalled,thenthistaskwillnever
finish. We’vealsoenlistedthehelpofanothertask,whichwe’llseeinamoment,thatwillmonitorhowmuchtime
haselapsedand,accordingly,callfuture.set_result().
async def async_sleep(seconds: float):
future = asyncio.Future()
time_to_wake = time.time() + seconds
# Add the watcher-task to the event loop.
watcher_task = asyncio.create_task(_sleep_watcher(future, time_to_wake))
# Block until the future is marked as done.
await future
Below,we’llusearatherbareobject,YieldToEventLoop(),toyieldfrom__await__inordertocedecontrol
totheeventloop. Thisiseffectivelythesameascallingasyncio.sleep(0),butthisapproachoffersmoreclarity,
nottomentionit’ssomewhatcheatingtouseasyncio.sleepwhenshowcasinghowtoimplementit!
Asusual,theeventloopcyclesthroughitstasks,givingthemcontrolandreceivingcontrolbackwhentheypauseor
finish. Thewatcher_task,whichrunsthecoroutine_sleep_watcher(...),willbeinvokedonceperfullcycle
oftheeventloop. Oneachresumption,it’llcheckthetimeandifnotenoughhaselapsed,thenit’llpauseonceagain
andhandcontrolbacktotheeventloop. Eventually,enoughtimewillhaveelapsed,and_sleep_watcher(...)
willmarkthefutureasdone,andthenitselffinishtoobybreakingoutoftheinfinitewhileloop. Giventhishelper
taskisonlyinvokedoncepercycleoftheeventloop,you’dbecorrecttonotethatthisasynchronoussleepwillsleep
atleastthreeseconds,ratherthanexactlythreeseconds. Notethisisalsooftrueofasyncio.sleep.
class YieldToEventLoop:
def __await__(self):
yield
async def _sleep_watcher(future, time_to_wake):
while True:
if time.time() >= time_to_wake:
# This marks the future as done.
future.set_result(None)
break
else:
await YieldToEventLoop()
Hereisthefullprogram’soutput:
$ python custom-async-sleep.py
Beginning asynchronous sleep at time: 14:52:22.
I like work. Work work.
I like work. Work work.
I like work. Work work.
Done asynchronous sleep at time: 14:52:25.
You might feel this implementation of asynchronous sleep was unnecessarily convoluted. And, well, it was. The
examplewasmeanttoshowcasetheversatilityoffutureswithasimpleexamplethatcouldbemimickedformore
complexneeds. Forreference,youcouldimplementitwithoutfutures,likeso:
async def simpler_async_sleep(seconds):
time_to_wake = time.time() + seconds
while True:
if time.time() >= time_to_wake:
return
else:
await YieldToEventLoop()
8

### 第9页

But,that’sallfornow. Hopefullyyou’rereadytomoreconfidentlydiveintosomeasyncprogrammingorcheckout
advancedtopicsintherest of the documentation.
9

