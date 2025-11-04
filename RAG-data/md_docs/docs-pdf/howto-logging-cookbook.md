### 第1页

Logging Cookbook
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Usinglogginginmultiplemodules 3
2 Loggingfrommultiplethreads 4
3 Multiplehandlersandformatters 5
4 Loggingtomultipledestinations 6
5 Customhandlingoflevels 7
6 Configurationserverexample 10
7 Dealingwithhandlersthatblock 11
8 Sendingandreceivingloggingeventsacrossanetwork 12
8.1 Runningaloggingsocketlistenerinproduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
9 Addingcontextualinformationtoyourloggingoutput 15
9.1 UsingLoggerAdapterstoimpartcontextualinformation . . . . . . . . . . . . . . . . . . . . . . . 16
9.2 UsingFilterstoimpartcontextualinformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
10 Useofcontextvars 18
11 Impartingcontextualinformationinhandlers 22
12 Loggingtoasinglefilefrommultipleprocesses 22
12.1 Usingconcurrent.futures.ProcessPoolExecutor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12.2 DeployingWebapplicationsusingGunicornanduWSGI . . . . . . . . . . . . . . . . . . . . . . . 27
13 Usingfilerotation 27
14 Useofalternativeformattingstyles 28
15 CustomizingLogRecord 30
16 SubclassingQueueHandlerandQueueListener-aZeroMQexample 31
16.1 SubclassQueueHandler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
16.2 SubclassQueueListener . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1

### 第2页

17 SubclassingQueueHandlerandQueueListener-apynngexample 32
17.1 SubclassQueueListener . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
17.2 SubclassQueueHandler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
18 Anexampledictionary-basedconfiguration 35
19 Usingarotatorandnamertocustomizelogrotationprocessing 36
20 Amoreelaboratemultiprocessingexample 37
21 InsertingaBOMintomessagessenttoaSysLogHandler 41
22 Implementingstructuredlogging 42
23 CustomizinghandlerswithdictConfig() 43
24 Usingparticularformattingstylesthroughoutyourapplication 45
24.1 UsingLogRecordfactories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
24.2 Usingcustommessageobjects. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
25 ConfiguringfilterswithdictConfig() 47
26 Customizedexceptionformatting 48
27 Speakingloggingmessages 49
28 Bufferingloggingmessagesandoutputtingthemconditionally 49
29 Sendingloggingmessagestoemail,withbuffering 52
30 FormattingtimesusingUTC(GMT)viaconfiguration 53
31 Usingacontextmanagerforselectivelogging 54
32 ACLIapplicationstartertemplate 56
33 AQtGUIforlogging 58
34 LoggingtosyslogwithRFC5424support 63
35 Howtotreataloggerlikeanoutputstream 64
36 Howtouniformlyhandlenewlinesinloggingoutput 66
37 Patternstoavoid 68
37.1 Openingthesamelogfilemultipletimes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
37.2 Usingloggersasattributesinaclassorpassingthemasparameters . . . . . . . . . . . . . . . . . 68
37.3 AddinghandlersotherthanNullHandlertoaloggerinalibrary . . . . . . . . . . . . . . . . . . 68
37.4 Creatingalotofloggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
38 Otherresources 69
Index 70
Author
VinaySajip<vinay_sajipatred-dovedotcom>
This page contains a number of recipes related to logging, which have been found useful in the past. For links to
tutorialandreferenceinformation,pleaseseeOtherresources.
2

### 第3页

1 Using logging in multiple modules
Multiplecallstologging.getLogger('someLogger')returnareferencetothesameloggerobject. Thisistrue
notonlywithinthesamemodule,butalsoacrossmodulesaslongasitisinthesamePythoninterpreterprocess. Itis
trueforreferencestothesameobject;additionally,applicationcodecandefineandconfigureaparentloggerinone
moduleandcreate(butnotconfigure)achildloggerinaseparatemodule,andallloggercallstothechildwillpass
uptotheparent. Hereisamainmodule:
import logging
import auxiliary_module
# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s
,→')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')
Hereistheauxiliarymodule:
import logging
# create logger
module_logger = logging.getLogger('spam_application.auxiliary')
class Auxiliary:
def __init__(self):
self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
self.logger.info('creating an instance of Auxiliary')
def do_something(self):
self.logger.info('doing something')
a = 1 + 1
self.logger.info('done doing something')
def some_function():
module_logger.info('received a call to "some_function"')
3

### 第4页

Theoutputlookslikethis:
2005-03-23 23:47:11,663 - spam_application - INFO -
creating an instance of auxiliary_module.Auxiliary
2005-03-23 23:47:11,665 - spam_application.auxiliary.Auxiliary - INFO -
creating an instance of Auxiliary
2005-03-23 23:47:11,665 - spam_application - INFO -
created an instance of auxiliary_module.Auxiliary
2005-03-23 23:47:11,668 - spam_application - INFO -
calling auxiliary_module.Auxiliary.do_something
2005-03-23 23:47:11,668 - spam_application.auxiliary.Auxiliary - INFO -
doing something
2005-03-23 23:47:11,669 - spam_application.auxiliary.Auxiliary - INFO -
done doing something
2005-03-23 23:47:11,670 - spam_application - INFO -
finished auxiliary_module.Auxiliary.do_something
2005-03-23 23:47:11,671 - spam_application - INFO -
calling auxiliary_module.some_function()
2005-03-23 23:47:11,672 - spam_application.auxiliary - INFO -
received a call to 'some_function'
2005-03-23 23:47:11,673 - spam_application - INFO -
done with auxiliary_module.some_function()
2 Logging from multiple threads
Loggingfrommultiplethreadsrequiresnospecialeffort. Thefollowingexampleshowsloggingfromthemain(initial)
threadandanotherthread:
import logging
import threading
import time
def worker(arg):
while not arg['stop']:
logging.debug('Hi from myfunc')
time.sleep(0.5)
def main():
logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d
,→%(threadName)s %(message)s')
info = {'stop': False}
thread = threading.Thread(target=worker, args=(info,))
thread.start()
while True:
try:
logging.debug('Hello from main')
time.sleep(0.75)
except KeyboardInterrupt:
info['stop'] = True
break
thread.join()
if __name__ == '__main__':
main()
Whenrun,thescriptshouldprintsomethinglikethefollowing:
4

### 第5页

0 Thread-1 Hi from myfunc
3 MainThread Hello from main
505 Thread-1 Hi from myfunc
755 MainThread Hello from main
1007 Thread-1 Hi from myfunc
1507 MainThread Hello from main
1508 Thread-1 Hi from myfunc
2010 Thread-1 Hi from myfunc
2258 MainThread Hello from main
2512 Thread-1 Hi from myfunc
3009 MainThread Hello from main
3013 Thread-1 Hi from myfunc
3515 Thread-1 Hi from myfunc
3761 MainThread Hello from main
4017 Thread-1 Hi from myfunc
4513 MainThread Hello from main
4518 Thread-1 Hi from myfunc
Thisshowstheloggingoutputinterspersedasonemightexpect. Thisapproachworksformorethreadsthanshown
here,ofcourse.
3 Multiple handlers and formatters
LoggersareplainPythonobjects. TheaddHandler()methodhasnominimumormaximumquotaforthenumber
ofhandlersyoumayadd. Sometimesitwillbebeneficialforanapplicationtologallmessagesofallseveritiestoa
textfilewhilesimultaneouslyloggingerrorsorabovetotheconsole. Tosetthisup,simplyconfiguretheappropriate
handlers. The logging calls in the application code will remain unchanged. Here is a slight modification to the
previoussimplemodule-basedconfigurationexample:
import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s
,→')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
Notice that the ‘application’ code does not care about multiple handlers. All that changed was the addition and
configurationofanewhandlernamedfh.
5

### 第6页

Theabilitytocreatenewhandlerswithhigher-orlower-severityfilterscanbeveryhelpfulwhenwritingandtest-
inganapplication. Insteadofusingmanyprintstatementsfordebugging,uselogger.debug: Unliketheprint
statements,whichyouwillhavetodeleteorcommentoutlater,thelogger.debugstatementscanremainintactinthe
sourcecodeandremaindormantuntilyouneedthemagain. Atthattime,theonlychangethatneedstohappenisto
modifytheseverityleveloftheloggerand/orhandlertodebug.
4 Logging to multiple destinations
Let’ssayyouwanttologtoconsoleandfilewithdifferentmessageformatsandindifferingcircumstances. Sayyou
wanttologmessageswithlevelsofDEBUGandhighertofile,andthosemessagesatlevelINFOandhighertothe
console. Let’salsoassumethatthefileshouldcontaintimestamps,buttheconsolemessagesshouldnot. Here’show
youcanachievethis:
import logging
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
datefmt='%m-%d %H:%M',
filename='/tmp/myapp.log',
filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')
# Now, define a couple of other loggers which might represent areas in your
# application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
Whenyourunthis,ontheconsoleyouwillsee
root : INFO Jackdaws love my big sphinx of quartz.
myapp.area1 : INFO How quickly daft jumping zebras vex.
myapp.area2 : WARNING Jail zesty vixen who grabbed pay from quack.
myapp.area2 : ERROR The five boxing wizards jump quickly.
andinthefileyouwillseesomethinglike
10-22 22:19 root INFO Jackdaws love my big sphinx of quartz.
10-22 22:19 myapp.area1 DEBUG Quick zephyrs blow, vexing daft Jim.
10-22 22:19 myapp.area1 INFO How quickly daft jumping zebras vex.
(continuesonnextpage)
6

### 第7页

(continuedfrompreviouspage)
10-22 22:19 myapp.area2 WARNING Jail zesty vixen who grabbed pay from quack.
10-22 22:19 myapp.area2 ERROR The five boxing wizards jump quickly.
Asyoucansee,theDEBUGmessageonlyshowsupinthefile. Theothermessagesaresenttobothdestinations.
Thisexampleusesconsoleandfilehandlers,butyoucanuseanynumberandcombinationofhandlersyouchoose.
Notethattheabovechoiceoflogfilename/tmp/myapp.logimpliesuseofastandardlocationfortemporaryfiles
onPOSIXsystems. OnWindows,youmayneedtochooseadifferentdirectorynameforthelog-justensurethat
thedirectoryexistsandthatyouhavethepermissionstocreateandupdatefilesinit.
5 Custom handling of levels
Sometimes,youmightwanttodosomethingslightlydifferentfromthestandardhandlingoflevelsinhandlers,where
alllevelsaboveathresholdgetprocessedbyahandler. Todothis,youneedtousefilters. Let’slookatascenario
whereyouwanttoarrangethingsasfollows:
• SendmessagesofseverityINFOandWARNINGtosys.stdout
• SendmessagesofseverityERRORandabovetosys.stderr
• SendmessagesofseverityDEBUGandabovetofileapp.log
SupposeyouconfigureloggingwiththefollowingJSON:
{
"version": 1,
"disable_existing_loggers": false,
"formatters": {
"simple": {
"format": "%(levelname)-8s - %(message)s"
}
},
"handlers": {
"stdout": {
"class": "logging.StreamHandler",
"level": "INFO",
"formatter": "simple",
"stream": "ext://sys.stdout"
},
"stderr": {
"class": "logging.StreamHandler",
"level": "ERROR",
"formatter": "simple",
"stream": "ext://sys.stderr"
},
"file": {
"class": "logging.FileHandler",
"formatter": "simple",
"filename": "app.log",
"mode": "w"
}
},
"root": {
"level": "DEBUG",
"handlers": [
"stderr",
"stdout",
"file"
(continuesonnextpage)
7

### 第8页

(continuedfrompreviouspage)
]
}
}
Thisconfigurationdoesalmostwhatwewant,exceptthatsys.stdoutwouldshowmessagesofseverityERRORand
onlyeventsofthisseverityandhigherwillbetrackedaswellasINFOandWARNINGmessages. Topreventthis,we
cansetupafilterwhichexcludesthosemessagesandaddittotherelevanthandler. Thiscanbeconfiguredbyadding
afilterssectionparalleltoformattersandhandlers:
{
"filters": {
"warnings_and_below": {
"()" : "__main__.filter_maker",
"level": "WARNING"
}
}
}
andchangingthesectiononthestdouthandlertoaddit:
{
"stdout": {
"class": "logging.StreamHandler",
"level": "INFO",
"formatter": "simple",
"stream": "ext://sys.stdout",
"filters": ["warnings_and_below"]
}
}
Afilterisjustafunction,sowecandefinethefilter_maker(afactoryfunction)asfollows:
def filter_maker(level):
level = getattr(logging, level)
def filter(record):
return record.levelno <= level
return filter
This converts the string argument passed in to a numeric level, and returns a function which only returns True if
the level of the passed in record is at or below the specified level. Note that in this example I have defined the
filter_makerinatestscriptmain.pythatIrunfromthecommandline,soitsmodulewillbe__main__-hence
the__main__.filter_makerinthefilterconfiguration. Youwillneedtochangethatifyoudefineitinadifferent
module.
Withthefilteradded,wecanrunmain.py,whichinfullis:
import json
import logging
import logging.config
CONFIG = '''
{
"version": 1,
"disable_existing_loggers": false,
"formatters": {
(continuesonnextpage)
8

### 第9页

(continuedfrompreviouspage)
"simple": {
"format": "%(levelname)-8s - %(message)s"
}
},
"filters": {
"warnings_and_below": {
"()" : "__main__.filter_maker",
"level": "WARNING"
}
},
"handlers": {
"stdout": {
"class": "logging.StreamHandler",
"level": "INFO",
"formatter": "simple",
"stream": "ext://sys.stdout",
"filters": ["warnings_and_below"]
},
"stderr": {
"class": "logging.StreamHandler",
"level": "ERROR",
"formatter": "simple",
"stream": "ext://sys.stderr"
},
"file": {
"class": "logging.FileHandler",
"formatter": "simple",
"filename": "app.log",
"mode": "w"
}
},
"root": {
"level": "DEBUG",
"handlers": [
"stderr",
"stdout",
"file"
]
}
}
'''
def filter_maker(level):
level = getattr(logging, level)
def filter(record):
return record.levelno <= level
return filter
logging.config.dictConfig(json.loads(CONFIG))
logging.debug('A DEBUG message')
logging.info('An INFO message')
logging.warning('A WARNING message')
logging.error('An ERROR message')
logging.critical('A CRITICAL message')
9

### 第10页

Andafterrunningitlikethis:
python main.py 2>stderr.log >stdout.log
Wecanseetheresultsareasexpected:
$ more *.log
::::::::::::::
app.log
::::::::::::::
DEBUG - A DEBUG message
INFO - An INFO message
WARNING - A WARNING message
ERROR - An ERROR message
CRITICAL - A CRITICAL message
::::::::::::::
stderr.log
::::::::::::::
ERROR - An ERROR message
CRITICAL - A CRITICAL message
::::::::::::::
stdout.log
::::::::::::::
INFO - An INFO message
WARNING - A WARNING message
6 Configuration server example
Hereisanexampleofamoduleusingtheloggingconfigurationserver:
import logging
import logging.config
import time
import os
# read initial config file
logging.config.fileConfig('logging.conf')
# create and start listener on port 9999
t = logging.config.listen(9999)
t.start()
logger = logging.getLogger('simpleExample')
try:
# loop through logging calls to see the difference
# new configurations make, until Ctrl+C is pressed
while True:
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
time.sleep(5)
except KeyboardInterrupt:
# cleanup
logging.config.stopListening()
(continuesonnextpage)
10

### 第11页

(continuedfrompreviouspage)
t.join()
Andhereisascriptthattakesafilenameandsendsthatfiletotheserver,properlyprecededwiththebinary-encoded
length,asthenewloggingconfiguration:
#!/usr/bin/env python
import socket, sys, struct
with open(sys.argv[1], 'rb') as f:
data_to_send = f.read()
HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting...')
s.connect((HOST, PORT))
print('sending config...')
s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)
s.close()
print('complete')
7 Dealing with handlers that block
Sometimesyouhavetogetyourlogginghandlerstodotheirworkwithoutblockingthethreadyou’reloggingfrom.
Thisiscommoninwebapplications,thoughofcourseitalsooccursinotherscenarios.
A common culprit which demonstrates sluggish behaviour is the SMTPHandler: sending emails can take a long
time, for a number of reasons outside the developer’s control (for example, a poorly performing mail or network
infrastructure). But almost any network-based handler can block: Even a SocketHandler operation may do a
DNS query under the hood which is too slow (and this query can be deep in the socket library code, below the
Pythonlayer,andoutsideyourcontrol).
Onesolutionistouseatwo-partapproach. Forthefirstpart,attachonlyaQueueHandlertothoseloggerswhichare
accessedfromperformance-criticalthreads. Theysimplywritetotheirqueue,whichcanbesizedtoalargeenough
capacityorinitializedwithnoupperboundtotheirsize. Thewritetothequeuewilltypicallybeacceptedquickly,
thoughyouwillprobablyneedtocatchthequeue.Fullexceptionasaprecautioninyourcode. Ifyouarealibrary
developerwhohasperformance-criticalthreadsintheircode,besuretodocumentthis(togetherwithasuggestion
toattachonlyQueueHandlerstoyourloggers)forthebenefitofotherdeveloperswhowilluseyourcode.
ThesecondpartofthesolutionisQueueListener,whichhasbeendesignedasthecounterparttoQueueHandler.
AQueueListenerisverysimple: it’spassedaqueueandsomehandlers,anditfiresupaninternalthreadwhich
listenstoitsqueueforLogRecordssentfromQueueHandlers(oranyothersourceofLogRecords,forthatmatter).
TheLogRecordsareremovedfromthequeueandpassedtothehandlersforprocessing.
TheadvantageofhavingaseparateQueueListenerclassisthatyoucanusethesameinstancetoservicemultiple
QueueHandlers. Thisismoreresource-friendlythan,say,havingthreadedversionsoftheexistinghandlerclasses,
whichwouldeatuponethreadperhandlerfornoparticularbenefit.
Anexampleofusingthesetwoclassesfollows(importsomitted):
que = queue.Queue(-1) # no limit on size
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
listener = QueueListener(que, handler)
root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(threadName)s: %(message)s')
(continuesonnextpage)
11

### 第12页

(continuedfrompreviouspage)
handler.setFormatter(formatter)
listener.start()
# The log output will display the thread which generated
# the event (the main thread) rather than the internal
# thread which monitors the internal queue. This is what
# you want to happen.
root.warning('Look out!')
listener.stop()
which,whenrun,willproduce:
MainThread: Look out!
(cid:174) Note
Althoughtheearlierdiscussionwasn’tspecificallytalkingaboutasynccode,butratheraboutslowlogginghandlers,
it should be noted that when logging from async code, network and even file handlers could lead to problems
(blockingtheeventloop)becausesomeloggingisdonefromasynciointernals. Itmightbebest,ifanyasync
codeisusedinanapplication,tousetheaboveapproachforlogging,sothatanyblockingcoderunsonlyinthe
QueueListenerthread.
Changedinversion3.5: PriortoPython3.5,theQueueListeneralwayspassedeverymessagereceivedfromthe
queuetoeveryhandleritwasinitializedwith. (Thiswasbecauseitwasassumedthatlevelfilteringwasalldoneon
theotherside, wherethequeueisfilled.) From3.5onwards, thisbehaviourcanbechangedbypassingakeyword
argumentrespect_handler_level=Truetothelistener’sconstructor. Whenthisisdone,thelistenercompares
thelevelofeachmessagewiththehandler’slevel,andonlypassesamessagetoahandlerifit’sappropriatetodoso.
Changedinversion3.14: TheQueueListenercanbestarted(andstopped)viathewithstatement. Forexample:
with QueueListener(que, handler) as listener:
# The queue listener automatically starts
# when the 'with' block is entered.
pass
# The queue listener automatically stops once
# the 'with' block is exited.
8 Sending and receiving logging events across a network
Let’ssayyouwanttosendloggingeventsacrossanetwork,andhandlethematthereceivingend. Asimplewayof
doingthisisattachingaSocketHandlerinstancetotherootloggeratthesendingend:
import logging, logging.handlers
rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost',
logging.handlers.DEFAULT_TCP_LOGGING_PORT)
# don't bother with a formatter, since a socket handler sends the event as
# an unformatted pickle
rootLogger.addHandler(socketHandler)
# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')
# Now, define a couple of other loggers which might represent areas in your
(continuesonnextpage)
12

### 第13页

(continuedfrompreviouspage)
# application:
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
Atthereceivingend,youcansetupareceiverusingthesocketservermodule. Hereisabasicworkingexample:
import pickle
import logging
import logging.handlers
import socketserver
import struct
class LogRecordStreamHandler(socketserver.StreamRequestHandler):
"""Handler for a streaming logging request.
This basically logs the record using whatever logging policy is
configured locally.
"""
def handle(self):
"""
Handle multiple requests - each expected to be a 4-byte length,
followed by the LogRecord in pickle format. Logs the record
according to whatever policy is configured locally.
"""
while True:
chunk = self.connection.recv(4)
if len(chunk) < 4:
break
slen = struct.unpack('>L', chunk)[0]
chunk = self.connection.recv(slen)
while len(chunk) < slen:
chunk = chunk + self.connection.recv(slen - len(chunk))
obj = self.unPickle(chunk)
record = logging.makeLogRecord(obj)
self.handleLogRecord(record)
def unPickle(self, data):
return pickle.loads(data)
def handleLogRecord(self, record):
# if a name is specified, we use the named logger rather than the one
# implied by the record.
if self.server.logname is not None:
name = self.server.logname
else:
name = record.name
logger = logging.getLogger(name)
# N.B. EVERY record gets logged. This is because Logger.handle
(continuesonnextpage)
13

### 第14页

(continuedfrompreviouspage)
# is normally called AFTER logger-level filtering. If you want
# to do filtering, do it at the client end to save wasting
# cycles and network bandwidth!
logger.handle(record)
class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
"""
Simple TCP socket-based logging receiver suitable for testing.
"""
allow_reuse_address = True
def __init__(self, host='localhost',
port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
handler=LogRecordStreamHandler):
socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
self.abort = 0
self.timeout = 1
self.logname = None
def serve_until_stopped(self):
import select
abort = 0
while not abort:
rd, wr, ex = select.select([self.socket.fileno()],
[], [],
self.timeout)
if rd:
self.handle_request()
abort = self.abort
def main():
logging.basicConfig(
format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
tcpserver = LogRecordSocketReceiver()
print('About to start TCP server...')
tcpserver.serve_until_stopped()
if __name__ == '__main__':
main()
Firstruntheserver,andthentheclient. Ontheclientside,nothingisprintedontheconsole;ontheserverside,you
shouldseesomethinglike:
About to start TCP server...
59 root INFO Jackdaws love my big sphinx of quartz.
59 myapp.area1 DEBUG Quick zephyrs blow, vexing daft Jim.
69 myapp.area1 INFO How quickly daft jumping zebras vex.
69 myapp.area2 WARNING Jail zesty vixen who grabbed pay from quack.
69 myapp.area2 ERROR The five boxing wizards jump quickly.
Notethattherearesomesecurityissueswithpickleinsomescenarios. Iftheseaffectyou,youcanuseanalternative
serializationschemebyoverridingthemakePickle()methodandimplementingyouralternativethere,aswellas
adaptingtheabovescripttouseyouralternativeserialization.
14

### 第15页

8.1 Running a logging socket listener in production
Torunalogginglistenerinproduction,youmayneedtouseaprocess-managementtoolsuchasSupervisor. Hereis
aGistwhichprovidesthebare-bonesfilestoruntheabovefunctionalityusingSupervisor. Itconsistsofthefollowing
files:
File Purpose
prepare.sh ABashscripttopreparetheenvironmentfortesting
supervisor. TheSupervisorconfigurationfile,whichhasentriesforthelistenerandamulti-processweb
conf application
ensure_app.sh ABashscripttoensurethatSupervisorisrunningwiththeaboveconfiguration
log_listener. Thesocketlistenerprogramwhichreceiveslogeventsandrecordsthemtoafile
py
main.py Asimplewebapplicationwhichperformsloggingviaasocketconnectedtothelistener
webapp.json AJSONconfigurationfileforthewebapplication
client.py APythonscripttoexercisethewebapplication
ThewebapplicationusesGunicorn,whichisapopularwebapplicationserverthatstartsmultipleworkerprocesses
tohandlerequests. Thisexamplesetupshowshowtheworkerscanwritetothesamelogfilewithoutconflictingwith
oneanother—theyallgothroughthesocketlistener.
Totestthesefiles,dothefollowinginaPOSIXenvironment:
1. DownloadtheGistasaZIParchiveusingtheDownloadZIPbutton.
2. Unziptheabovefilesfromthearchiveintoascratchdirectory.
3. Inthescratchdirectory,runbash prepare.shtogetthingsready. Thiscreatesarunsubdirectorytocontain
Supervisor-relatedandlogfiles,andavenvsubdirectorytocontainavirtualenvironmentintowhichbottle,
gunicornandsupervisorareinstalled.
4. Runbash ensure_app.shtoensurethatSupervisorisrunningwiththeaboveconfiguration.
5. Runvenv/bin/python client.pytoexercisethewebapplication,whichwillleadtorecordsbeingwritten
tothelog.
6. Inspect the log files in the run subdirectory. You should see the most recent log lines in files matching the
pattern app.log*. They won’t be in any particular order, since they have been handled concurrently by
differentworkerprocessesinanon-deterministicway.
7. You can shut down the listener and the web application by running venv/bin/supervisorctl -c
supervisor.conf shutdown.
Youmayneedtotweaktheconfigurationfilesintheunlikelyeventthattheconfiguredportsclashwithsomething
elseinyourtestenvironment.
The default configuration uses a TCP socket on port 9020. You can use a Unix Domain socket instead of a TCP
socketbydoingthefollowing:
1. In listener.json, add a socket key with the path to the domain socket you want to use. If this key is
present, the listener listens on the corresponding domain socket and not on a TCP socket (the port key is
ignored).
2. Inwebapp.json,changethesockethandlerconfigurationdictionarysothatthehostvalueisthepathtothe
domainsocket,andsettheportvaluetonull.
9 Adding contextual information to your logging output
Sometimes you want logging output to contain contextual information in addition to the parameters passed to the
loggingcall. Forexample, inanetworkedapplication, itmaybedesirableto logclient-specificinformationinthe
log(e.g. remoteclient’susername,orIPaddress). Althoughyoucouldusetheextraparametertoachievethis,it’s
notalwaysconvenienttopasstheinformationinthisway. WhileitmightbetemptingtocreateLoggerinstances
15

| File | Purpose |
| --- | --- |
| prepare.sh | ABashscripttopreparetheenvironmentfortesting |
| supervisor.
conf | TheSupervisorconfigurationfile,whichhasentriesforthelistenerandamulti-processweb
application |
| ensure_app.sh | ABashscripttoensurethatSupervisorisrunningwiththeaboveconfiguration |
| log_listener.
py | Thesocketlistenerprogramwhichreceiveslogeventsandrecordsthemtoafile |
| main.py | Asimplewebapplicationwhichperformsloggingviaasocketconnectedtothelistener |
| webapp.json | AJSONconfigurationfileforthewebapplication |
| client.py | APythonscripttoexercisethewebapplication |

### 第16页

on a per-connection basis, this is not a good idea because these instances are not garbage collected. While this is
notaprobleminpractice,whenthenumberofLoggerinstancesisdependentonthelevelofgranularityyouwant
touseinlogginganapplication,itcouldbehardtomanageifthenumberofLoggerinstancesbecomeseffectively
unbounded.
9.1 Using LoggerAdapters to impart contextual information
Aneasywayinwhichyoucanpasscontextualinformationtobeoutputalongwithloggingeventinformationistouse
theLoggerAdapterclass. ThisclassisdesignedtolooklikeaLogger,sothatyoucancalldebug(),info(),
warning(),error(),exception(),critical()andlog(). Thesemethodshavethesamesignaturesastheir
counterpartsinLogger,soyoucanusethetwotypesofinstancesinterchangeably.
WhenyoucreateaninstanceofLoggerAdapter,youpassitaLoggerinstanceandadict-likeobjectwhichcontains
your contextual information. When you call one of the logging methods on an instance of LoggerAdapter, it
delegatesthecalltotheunderlyinginstanceofLoggerpassedtoitsconstructor,andarrangestopassthecontextual
informationinthedelegatedcall. Here’sasnippetfromthecodeofLoggerAdapter:
def debug(self, msg, /, *args, **kwargs):
"""
Delegate a debug call to the underlying logger, after adding
contextual information from this adapter instance.
"""
msg, kwargs = self.process(msg, kwargs)
self.logger.debug(msg, *args, **kwargs)
Theprocess() methodof LoggerAdapter iswherethecontextualinformationisaddedto theloggingoutput.
It’spassedthemessageandkeywordargumentsoftheloggingcall,anditpassesback(potentially)modifiedversions
ofthesetouseinthecalltotheunderlyinglogger. Thedefaultimplementationofthismethodleavesthemessage
alone,butinsertsan‘extra’keyinthekeywordargumentwhosevalueisthedict-likeobjectpassedtotheconstructor.
Ofcourse,ifyouhadpassedan‘extra’keywordargumentinthecalltotheadapter,itwillbesilentlyoverwritten.
The advantage of using ‘extra’ is that the values in the dict-like object are merged into the LogRecord instance’s
__dict__,allowingyoutousecustomizedstringswithyourFormatterinstanceswhichknowaboutthekeysofthe
dict-likeobject. Ifyouneedadifferentmethod,e.g. ifyouwanttoprependorappendthecontextualinformationto
themessagestring,youjustneedtosubclassLoggerAdapterandoverrideprocess()todowhatyouneed. Here
isasimpleexample:
class CustomAdapter(logging.LoggerAdapter):
"""
This example adapter expects the passed in dict-like object to have a
'connid' key, whose value in brackets is prepended to the log message.
"""
def process(self, msg, kwargs):
return '[%s] %s' % (self.extra['connid'], msg), kwargs
whichyoucanuselikethis:
logger = logging.getLogger(__name__)
adapter = CustomAdapter(logger, {'connid': some_conn_id})
Thenanyeventsthatyoulogtotheadapterwillhavethevalueofsome_conn_idprependedtothelogmessages.
Usingobjectsotherthandictstopasscontextualinformation
Youdon’tneedtopassanactualdicttoaLoggerAdapter-youcouldpassaninstanceofaclasswhichimplements
__getitem__and__iter__sothatitlookslikeadicttologging. Thiswouldbeusefulifyouwanttogenerate
valuesdynamically(whereasthevaluesinadictwouldbeconstant).
16

### 第17页

9.2 Using Filters to impart contextual information
Youcanalsoaddcontextualinformationtologoutputusingauser-definedFilter. Filterinstancesareallowed
tomodifytheLogRecordspassedtothem,includingaddingadditionalattributeswhichcanthenbeoutputusinga
suitableformatstring,orifneededacustomFormatter.
Forexampleinawebapplication,therequestbeingprocessed(oratleast,theinterestingpartsofit)canbestored
inathreadlocal(threading.local)variable,andthenaccessedfromaFiltertoadd,say,informationfromthe
request-say,theremoteIPaddressandremoteuser’susername-totheLogRecord,usingtheattributenames‘ip’
and‘user’asintheLoggerAdapterexampleabove. Inthatcase,thesameformatstringcanbeusedtogetsimilar
outputtothatshownabove. Here’sanexamplescript:
import logging
from random import choice
class ContextFilter(logging.Filter):
"""
This is a filter which injects contextual information into the log.
Rather than use actual contextual information, we just use random
data in this demo.
"""
USERS = ['jim', 'fred', 'sheila']
IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']
def filter(self, record):
record.ip = choice(ContextFilter.IPS)
record.user = choice(ContextFilter.USERS)
return True
if __name__ == '__main__':
levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.
,→CRITICAL)
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)-15s %(name)-5s %(levelname)-8s IP:
,→%(ip)-15s User: %(user)-8s %(message)s')
a1 = logging.getLogger('a.b.c')
a2 = logging.getLogger('d.e.f')
f = ContextFilter()
a1.addFilter(f)
a2.addFilter(f)
a1.debug('A debug message')
a1.info('An info message with %s', 'some parameters')
for x in range(10):
lvl = choice(levels)
lvlname = logging.getLevelName(lvl)
a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')
which,whenrun,producessomethinglike:
2010-09-06 22:38:15,292 a.b.c DEBUG IP: 123.231.231.123 User: fred A debug␣
,→message
2010-09-06 22:38:15,300 a.b.c INFO IP: 192.168.0.1 User: sheila An info␣
,→message with some parameters
2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 127.0.0.1 User: sheila A␣
,→message at CRITICAL level with 2 parameters
(continuesonnextpage)
17

### 第18页

(continuedfrompreviouspage)
2010-09-06 22:38:15,300 d.e.f ERROR IP: 127.0.0.1 User: jim A␣
,→message at ERROR level with 2 parameters
2010-09-06 22:38:15,300 d.e.f DEBUG IP: 127.0.0.1 User: sheila A␣
,→message at DEBUG level with 2 parameters
2010-09-06 22:38:15,300 d.e.f ERROR IP: 123.231.231.123 User: fred A␣
,→message at ERROR level with 2 parameters
2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 192.168.0.1 User: jim A␣
,→message at CRITICAL level with 2 parameters
2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 127.0.0.1 User: sheila A␣
,→message at CRITICAL level with 2 parameters
2010-09-06 22:38:15,300 d.e.f DEBUG IP: 192.168.0.1 User: jim A␣
,→message at DEBUG level with 2 parameters
2010-09-06 22:38:15,301 d.e.f ERROR IP: 127.0.0.1 User: sheila A␣
,→message at ERROR level with 2 parameters
2010-09-06 22:38:15,301 d.e.f DEBUG IP: 123.231.231.123 User: fred A␣
,→message at DEBUG level with 2 parameters
2010-09-06 22:38:15,301 d.e.f INFO IP: 123.231.231.123 User: fred A␣
,→message at INFO level with 2 parameters
10 Use of contextvars
SincePython3.7,thecontextvarsmodulehasprovidedcontext-localstoragewhichworksforboththreading
andasyncioprocessingneeds. Thistypeofstoragemaythusbegenerallypreferabletothread-locals. Thefollowing
exampleshowshow, inamulti-threadedenvironment, logscanpopulatedwithcontextualinformationsuchas, for
example,requestattributeshandledbywebapplications.
For the purposes of illustration, say that you have different web applications, each independent of the other but
runninginthesamePythonprocessandusingalibrarycommontothem. Howcaneachoftheseapplicationshave
theirownlog, whereallloggingmessagesfromthelibrary(andotherrequestprocessingcode)aredirectedtothe
appropriateapplication’slogfile,whileincludinginthelogadditionalcontextualinformationsuchasclientIP,HTTP
requestmethodandclientusername?
Let’sassumethatthelibrarycanbesimulatedbythefollowingcode:
# webapplib.py
import logging
import time
logger = logging.getLogger(__name__)
def useful():
# Just a representative event logged from the library
logger.debug('Hello from webapplib!')
# Just sleep for a bit so other threads get to run
time.sleep(0.01)
Wecansimulatethemultiplewebapplicationsbymeansoftwosimpleclasses,RequestandWebApp. Thesesimulate
howrealthreadedwebapplicationswork-eachrequestishandledbyathread:
# main.py
import argparse
from contextvars import ContextVar
import logging
import os
from random import choice
import threading
(continuesonnextpage)
18

### 第19页

(continuedfrompreviouspage)
import webapplib
logger = logging.getLogger(__name__)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
class Request:
"""
A simple dummy request class which just holds dummy HTTP request method,
client IP address and client username
"""
def __init__(self, method, ip, user):
self.method = method
self.ip = ip
self.user = user
# A dummy set of requests which will be used in the simulation - we'll just pick
# from this list randomly. Note that all GET requests are from 192.168.2.XXX
# addresses, whereas POST requests are from 192.16.3.XXX addresses. Three users
# are represented in the sample requests.
REQUESTS = [
Request('GET', '192.168.2.20', 'jim'),
Request('POST', '192.168.3.20', 'fred'),
Request('GET', '192.168.2.21', 'sheila'),
Request('POST', '192.168.3.21', 'jim'),
Request('GET', '192.168.2.22', 'fred'),
Request('POST', '192.168.3.22', 'sheila'),
]
# Note that the format string includes references to request context information
# such as HTTP method, client IP and username
formatter = logging.Formatter('%(threadName)-11s %(appName)s %(name)-9s %(user)-6s
,→%(ip)s %(method)-4s %(message)s')
# Create our context variables. These will be filled at the start of request
# processing, and used in the logging that happens during that processing
ctx_request = ContextVar('request')
ctx_appname = ContextVar('appname')
class InjectingFilter(logging.Filter):
"""
A filter which injects context-specific information into logs and ensures
that only information for a specific webapp is included in its log
"""
def __init__(self, app):
self.app = app
def filter(self, record):
request = ctx_request.get()
record.method = request.method
record.ip = request.ip
record.user = request.user
record.appName = appName = ctx_appname.get()
(continuesonnextpage)
19

### 第20页

(continuedfrompreviouspage)
return appName == self.app.name
class WebApp:
"""
A dummy web application class which has its own handler and filter for a
webapp-specific log.
"""
def __init__(self, name):
self.name = name
handler = logging.FileHandler(name + '.log', 'w')
f = InjectingFilter(self)
handler.setFormatter(formatter)
handler.addFilter(f)
root.addHandler(handler)
self.num_requests = 0
def process_request(self, request):
"""
This is the dummy method for processing a request. It's called on a
different thread for every request. We store the context information into
the context vars before doing anything else.
"""
ctx_request.set(request)
ctx_appname.set(self.name)
self.num_requests += 1
logger.debug('Request processing started')
webapplib.useful()
logger.debug('Request processing finished')
def main():
fn = os.path.splitext(os.path.basename(__file__))[0]
adhf = argparse.ArgumentDefaultsHelpFormatter
ap = argparse.ArgumentParser(formatter_class=adhf, prog=fn,
description='Simulate a couple of web '
'applications handling some '
'requests, showing how request '
'context can be used to '
'populate logs')
aa = ap.add_argument
aa('--count', '-c', type=int, default=100, help='How many requests to simulate
,→')
options = ap.parse_args()
# Create the dummy webapps and put them in a list which we can use to select
# from randomly
app1 = WebApp('app1')
app2 = WebApp('app2')
apps = [app1, app2]
threads = []
# Add a common handler which will capture all events
handler = logging.FileHandler('app.log', 'w')
handler.setFormatter(formatter)
root.addHandler(handler)
# Generate calls to process requests
for i in range(options.count):
(continuesonnextpage)
20

### 第21页

(continuedfrompreviouspage)
try:
# Pick an app at random and a request for it to process
app = choice(apps)
request = choice(REQUESTS)
# Process the request in its own thread
t = threading.Thread(target=app.process_request, args=(request,))
threads.append(t)
t.start()
except KeyboardInterrupt:
break
# Wait for the threads to terminate
for t in threads:
t.join()
for app in apps:
print('%s processed %s requests' % (app.name, app.num_requests))
if __name__ == '__main__':
main()
Ifyouruntheabove,youshouldfindthatroughlyhalftherequestsgointoapp1.logandtherestintoapp2.log,
andthealltherequestsareloggedtoapp.log. Eachwebapp-specificlogwillcontainonlylogentriesforonlythat
webapp, andtherequestinformationwillbedisplayedconsistentlyinthelog(i.e. theinformationineachdummy
requestwillalwaysappeartogetherinalogline). Thisisillustratedbythefollowingshelloutput:
~/logging-contextual-webapp$ python main.py
app1 processed 51 requests
app2 processed 49 requests
~/logging-contextual-webapp$ wc -l *.log
153 app1.log
147 app2.log
300 app.log
600 total
~/logging-contextual-webapp$ head -3 app1.log
Thread-3 (process_request) app1 __main__ jim 192.168.3.21 POST Request␣
,→processing started
Thread-3 (process_request) app1 webapplib jim 192.168.3.21 POST Hello from␣
,→webapplib!
Thread-5 (process_request) app1 __main__ jim 192.168.3.21 POST Request␣
,→processing started
~/logging-contextual-webapp$ head -3 app2.log
Thread-1 (process_request) app2 __main__ sheila 192.168.2.21 GET Request␣
,→processing started
Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET Hello from␣
,→webapplib!
Thread-2 (process_request) app2 __main__ jim 192.168.2.20 GET Request␣
,→processing started
~/logging-contextual-webapp$ head app.log
Thread-1 (process_request) app2 __main__ sheila 192.168.2.21 GET Request␣
,→processing started
Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET Hello from␣
,→webapplib!
Thread-2 (process_request) app2 __main__ jim 192.168.2.20 GET Request␣
,→processing started
Thread-3 (process_request) app1 __main__ jim 192.168.3.21 POST Request␣
(continuesonnextpage)
21

### 第22页

(continuedfrompreviouspage)
,→processing started
Thread-2 (process_request) app2 webapplib jim 192.168.2.20 GET Hello from␣
,→webapplib!
Thread-3 (process_request) app1 webapplib jim 192.168.3.21 POST Hello from␣
,→webapplib!
Thread-4 (process_request) app2 __main__ fred 192.168.2.22 GET Request␣
,→processing started
Thread-5 (process_request) app1 __main__ jim 192.168.3.21 POST Request␣
,→processing started
Thread-4 (process_request) app2 webapplib fred 192.168.2.22 GET Hello from␣
,→webapplib!
Thread-6 (process_request) app1 __main__ jim 192.168.3.21 POST Request␣
,→processing started
~/logging-contextual-webapp$ grep app1 app1.log | wc -l
153
~/logging-contextual-webapp$ grep app2 app2.log | wc -l
147
~/logging-contextual-webapp$ grep app1 app.log | wc -l
153
~/logging-contextual-webapp$ grep app2 app.log | wc -l
147
11 Imparting contextual information in handlers
Each Handler has its own chain of filters. If you want to add contextual information to a LogRecord without
leakingittootherhandlers,youcanuseafilterthatreturnsanewLogRecordinsteadofmodifyingitin-place,as
showninthefollowingscript:
import copy
import logging
def filter(record: logging.LogRecord):
record = copy.copy(record)
record.user = 'jim'
return record
if __name__ == '__main__':
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s from %(user)-8s')
handler.setFormatter(formatter)
handler.addFilter(filter)
logger.addHandler(handler)
logger.info('A log message')
12 Logging to a single file from multiple processes
Althoughloggingisthread-safe, andloggingtoasinglefilefrommultiplethreadsinasingleprocessis supported,
loggingtoasinglefilefrommultipleprocessesisnotsupported,becausethereisnostandardwaytoserializeaccessto
asinglefileacrossmultipleprocessesinPython. Ifyouneedtologtoasinglefilefrommultipleprocesses,oneway
ofdoingthisistohavealltheprocesseslogtoaSocketHandler,andhaveaseparateprocesswhichimplements
asocketserverwhichreadsfromthesocketandlogstofile. (Ifyouprefer, youcandedicateonethreadinoneof
22

### 第23页

theexistingprocessestoperformthisfunction.) Thissectiondocumentsthisapproachinmoredetailandincludesa
workingsocketreceiverwhichcanbeusedasastartingpointforyoutoadaptinyourownapplications.
You could also write your own handler which uses the Lock class from the multiprocessing module to se-
rialize access to the file from your processes. The stdlib FileHandler and subclasses do not make use of
multiprocessing.
Alternatively,youcanuseaQueueandaQueueHandlertosendallloggingeventstooneoftheprocessesinyour
multi-processapplication. Thefollowingexamplescriptdemonstrateshowyoucandothis;intheexampleaseparate
listenerprocesslistensforeventssentbyotherprocessesandlogsthemaccordingtoitsownloggingconfiguration.
Although the example only demonstrates one way of doing it (for example, you may want to use a listener thread
ratherthanaseparatelistenerprocess–theimplementationwouldbeanalogous)itdoesallowforcompletelydifferent
loggingconfigurationsforthelistenerandtheotherprocessesinyourapplication, andcanbeusedasthebasisfor
codemeetingyourownspecificrequirements:
# You'll need these imports in your own code
import logging
import logging.handlers
import multiprocessing
# Next two import lines for this demo only
from random import choice, random
import time
#
# Because you'll want to define the logging configurations for listener and␣
,→workers, the
# listener and worker process functions take a configurer parameter which is a␣
,→callable
# for configuring logging for that process. These functions are also passed the␣
,→queue,
# which they use for communication.
#
# In practice, you can configure the listener however you want, but note that in␣
,→this
# simple example, the listener does not apply level or filter logic to received␣
,→records.
# In practice, you would probably want to do this logic in the worker processes,␣
,→to avoid
# sending events which would be filtered out between processes.
#
# The size of the rotated files is made small so you can see the results easily.
def listener_configurer():
root = logging.getLogger()
h = logging.handlers.RotatingFileHandler('mptest.log', 'a', 300, 10)
f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s
,→%(message)s')
h.setFormatter(f)
root.addHandler(h)
# This is the listener process top-level loop: wait for logging events
# (LogRecords)on the queue and handle them, quit when you get a None for a
# LogRecord.
def listener_process(queue, configurer):
configurer()
while True:
try:
record = queue.get()
if record is None: # We send this as a sentinel to tell the listener␣
(continuesonnextpage)
23

### 第24页

(continuedfrompreviouspage)
,→to quit.
break
logger = logging.getLogger(record.name)
logger.handle(record) # No level or filter logic applied - just do it!
except Exception:
import sys, traceback
print('Whoops! Problem:', file=sys.stderr)
traceback.print_exc(file=sys.stderr)
# Arrays used for random selections in this demo
LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING,
logging.ERROR, logging.CRITICAL]
LOGGERS = ['a.b.c', 'd.e.f']
MESSAGES = [
'Random message #1',
'Random message #2',
'Random message #3',
]
# The worker configuration is done at the start of the worker process run.
# Note that on Windows you can't rely on fork semantics, so each process
# will run the logging configuration code when it starts.
def worker_configurer(queue):
h = logging.handlers.QueueHandler(queue) # Just the one handler needed
root = logging.getLogger()
root.addHandler(h)
# send all messages, for demo; no other level or filter logic applied.
root.setLevel(logging.DEBUG)
# This is the worker process top-level loop, which just logs ten events with
# random intervening delays before terminating.
# The print messages are just so you know it's doing something!
def worker_process(queue, configurer):
configurer(queue)
name = multiprocessing.current_process().name
print('Worker started: %s' % name)
for i in range(10):
time.sleep(random())
logger = logging.getLogger(choice(LOGGERS))
level = choice(LEVELS)
message = choice(MESSAGES)
logger.log(level, message)
print('Worker finished: %s' % name)
# Here's where the demo gets orchestrated. Create the queue, create and start
# the listener, create ten workers and start them, wait for them to finish,
# then send a None to the queue to tell the listener to finish.
def main():
queue = multiprocessing.Queue(-1)
listener = multiprocessing.Process(target=listener_process,
args=(queue, listener_configurer))
listener.start()
workers = []
(continuesonnextpage)
24

### 第25页

(continuedfrompreviouspage)
for i in range(10):
worker = multiprocessing.Process(target=worker_process,
args=(queue, worker_configurer))
workers.append(worker)
worker.start()
for w in workers:
w.join()
queue.put_nowait(None)
listener.join()
if __name__ == '__main__':
main()
Avariantoftheabovescriptkeepsthelogginginthemainprocess,inaseparatethread:
import logging
import logging.config
import logging.handlers
from multiprocessing import Process, Queue
import random
import threading
import time
def logger_thread(q):
while True:
record = q.get()
if record is None:
break
logger = logging.getLogger(record.name)
logger.handle(record)
def worker_process(q):
qh = logging.handlers.QueueHandler(q)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(qh)
levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
logging.CRITICAL]
loggers = ['foo', 'foo.bar', 'foo.bar.baz',
'spam', 'spam.ham', 'spam.ham.eggs']
for i in range(100):
lvl = random.choice(levels)
logger = logging.getLogger(random.choice(loggers))
logger.log(lvl, 'Message no. %d', i)
if __name__ == '__main__':
q = Queue()
d = {
'version': 1,
'formatters': {
'detailed': {
'class': 'logging.Formatter',
'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-
,→10s %(message)s'
}
(continuesonnextpage)
25

### 第26页

(continuedfrompreviouspage)
},
'handlers': {
'console': {
'class': 'logging.StreamHandler',
'level': 'INFO',
},
'file': {
'class': 'logging.FileHandler',
'filename': 'mplog.log',
'mode': 'w',
'formatter': 'detailed',
},
'foofile': {
'class': 'logging.FileHandler',
'filename': 'mplog-foo.log',
'mode': 'w',
'formatter': 'detailed',
},
'errors': {
'class': 'logging.FileHandler',
'filename': 'mplog-errors.log',
'mode': 'w',
'level': 'ERROR',
'formatter': 'detailed',
},
},
'loggers': {
'foo': {
'handlers': ['foofile']
}
},
'root': {
'level': 'DEBUG',
'handlers': ['console', 'file', 'errors']
},
}
workers = []
for i in range(5):
wp = Process(target=worker_process, name='worker %d' % (i + 1), args=(q,))
workers.append(wp)
wp.start()
logging.config.dictConfig(d)
lp = threading.Thread(target=logger_thread, args=(q,))
lp.start()
# At this point, the main process could do some useful work of its own
# Once it's done that, it can wait for the workers to terminate...
for wp in workers:
wp.join()
# And now tell the logging thread to finish up, too
q.put(None)
lp.join()
This variant shows how you can e.g. apply configuration for particular loggers - e.g. the foo logger has a special
handler which stores all events in the foo subsystem in a file mplog-foo.log. This will be used by the logging
machineryinthemainprocess(eventhoughtheloggingeventsaregeneratedintheworkerprocesses)todirectthe
messagestotheappropriatedestinations.
26

### 第27页

12.1 Using concurrent.futures.ProcessPoolExecutor
Ifyouwanttouseconcurrent.futures.ProcessPoolExecutortostartyourworkerprocesses,youneedto
createthequeueslightlydifferently. Insteadof
queue = multiprocessing.Queue(-1)
youshoulduse
queue = multiprocessing.Manager().Queue(-1) # also works with the examples above
andyoucanthenreplacetheworkercreationfromthis:
workers = []
for i in range(10):
worker = multiprocessing.Process(target=worker_process,
args=(queue, worker_configurer))
workers.append(worker)
worker.start()
for w in workers:
w.join()
tothis(rememberingtofirstimportconcurrent.futures):
with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
for i in range(10):
executor.submit(worker_process, queue, worker_configurer)
12.2 Deploying Web applications using Gunicorn and uWSGI
When deploying Web applications using Gunicorn or uWSGI (or similar), multiple worker processes are created
tohandleclientrequests. Insuchenvironments,avoidcreatingfile-basedhandlersdirectlyinyourwebapplication.
Instead,useaSocketHandlertologfromthewebapplicationtoalistenerinaseparateprocess. Thiscanbeset
upusingaprocessmanagementtoolsuchasSupervisor-seeRunningaloggingsocketlistenerinproductionformore
details.
13 Using file rotation
Sometimes you want to let a log file grow to a certain size, then open a new file and log to that. You may want
to keep a certain number of these files, and when that many files have been created, rotate the files so that the
numberoffilesandthesizeofthefilesbothremainbounded. Forthisusagepattern,theloggingpackageprovidesa
RotatingFileHandler:
import glob
import logging
import logging.handlers
LOG_FILENAME = 'logging_rotatingfile_example.out'
# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
LOG_FILENAME, maxBytes=20, backupCount=5)
my_logger.addHandler(handler)
(continuesonnextpage)
27

### 第28页

(continuedfrompreviouspage)
# Log some messages
for i in range(20):
my_logger.debug('i = %d' % i)
# See what files are created
logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in logfiles:
print(filename)
Theresultshouldbe6separatefiles,eachwithpartoftheloghistoryfortheapplication:
logging_rotatingfile_example.out
logging_rotatingfile_example.out.1
logging_rotatingfile_example.out.2
logging_rotatingfile_example.out.3
logging_rotatingfile_example.out.4
logging_rotatingfile_example.out.5
Themostcurrentfileisalwayslogging_rotatingfile_example.out,andeachtimeitreachesthesizelimitit
isrenamedwiththesuffix.1. Eachoftheexistingbackupfilesisrenamedtoincrementthesuffix(.1becomes.2,
etc.) andthe.6fileiserased.
Obviouslythisexamplesetstheloglengthmuchtoosmallasanextremeexample. YouwouldwanttosetmaxBytes
toanappropriatevalue.
14 Use of alternative formatting styles
WhenloggingwasaddedtothePythonstandardlibrary,theonlywayofformattingmessageswithvariablecontent
was to use the %-formatting method. Since then, Python has gained two new formatting approaches: string.
Template(addedinPython2.4)andstr.format()(addedinPython2.6).
Logging(asof3.2)providesimprovedsupportforthesetwoadditionalformattingstyles. TheFormatterclassbeen
enhancedtotakeanadditional,optionalkeywordparameternamedstyle. Thisdefaultsto'%',butotherpossible
valuesare'{'and'$',whichcorrespondtotheothertwoformattingstyles. Backwardscompatibilityismaintained
bydefault(asyouwouldexpect),butbyexplicitlyspecifyingastyleparameter,yougettheabilitytospecifyformat
strings which work with str.format() or string.Template. Here’s an example console session to show the
possibilities:
>>> import logging
>>> root = logging.getLogger()
>>> root.setLevel(logging.DEBUG)
>>> handler = logging.StreamHandler()
>>> bf = logging.Formatter('{asctime} {name} {levelname:8s} {message}',
... style='{')
>>> handler.setFormatter(bf)
>>> root.addHandler(handler)
>>> logger = logging.getLogger('foo.bar')
>>> logger.debug('This is a DEBUG message')
2010-10-28 15:11:55,341 foo.bar DEBUG This is a DEBUG message
>>> logger.critical('This is a CRITICAL message')
2010-10-28 15:12:11,526 foo.bar CRITICAL This is a CRITICAL message
>>> df = logging.Formatter('$asctime $name ${levelname} $message',
... style='$')
>>> handler.setFormatter(df)
>>> logger.debug('This is a DEBUG message')
(continuesonnextpage)
28

### 第29页

(continuedfrompreviouspage)
2010-10-28 15:13:06,924 foo.bar DEBUG This is a DEBUG message
>>> logger.critical('This is a CRITICAL message')
2010-10-28 15:13:11,494 foo.bar CRITICAL This is a CRITICAL message
>>>
Notethattheformattingofloggingmessagesforfinaloutputtologsiscompletelyindependentofhowanindividual
loggingmessageisconstructed. Thatcanstilluse%-formatting,asshownhere:
>>> logger.error('This is an%s %s %s', 'other,', 'ERROR,', 'message')
2010-10-28 15:19:29,833 foo.bar ERROR This is another, ERROR, message
>>>
Logging calls (logger.debug(), logger.info() etc.) only take positional parameters for the actual logging
message itself, with keyword parameters used only for determining options for how to handle the actual logging
call(e.g. theexc_infokeywordparametertoindicatethattracebackinformationshouldbelogged,ortheextra
keywordparametertoindicateadditionalcontextualinformationtobeaddedtothelog). Soyoucannotdirectlymake
loggingcallsusingstr.format()orstring.Templatesyntax,becauseinternallytheloggingpackageuses%-
formattingtomergetheformatstringandthevariablearguments. Therewouldbenochangingthiswhilepreserving
backwardcompatibility,sinceallloggingcallswhichareoutthereinexistingcodewillbeusing%-formatstrings.
There is, however, a way that you can use {}- and $- formatting to construct your individual log messages. Recall
thatforamessageyoucanuseanarbitraryobjectasamessageformatstring,andthattheloggingpackagewillcall
str()onthatobjecttogettheactualformatstring. Considerthefollowingtwoclasses:
class BraceMessage:
def __init__(self, fmt, /, *args, **kwargs):
self.fmt = fmt
self.args = args
self.kwargs = kwargs
def __str__(self):
return self.fmt.format(*self.args, **self.kwargs)
class DollarMessage:
def __init__(self, fmt, /, **kwargs):
self.fmt = fmt
self.kwargs = kwargs
def __str__(self):
from string import Template
return Template(self.fmt).substitute(**self.kwargs)
Either of these can be used in place of a format string, to allow {}- or $-formatting to be used to build the actual
“message”partwhichappearsintheformattedlogoutputinplaceof“%(message)s”or“{message}”or“$message”.
It’salittleunwieldytousetheclassnameswheneveryouwanttologsomething,butit’squitepalatableifyouusean
aliassuchas__(doubleunderscore—nottobeconfusedwith_,thesingleunderscoreusedasasynonym/aliasfor
gettext.gettext()oritsbrethren).
TheaboveclassesarenotincludedinPython,thoughthey’reeasyenoughtocopyandpasteintoyourowncode. They
canbeusedasfollows(assumingthatthey’redeclaredinamodulecalledwherever):
>>> from wherever import BraceMessage as __
>>> print(__('Message with {0} {name}', 2, name='placeholders'))
Message with 2 placeholders
>>> class Point: pass
...
>>> p = Point()
>>> p.x = 0.5
(continuesonnextpage)
29

### 第30页

(continuedfrompreviouspage)
>>> p.y = 0.5
>>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})',
... point=p))
Message with coordinates: (0.50, 0.50)
>>> from wherever import DollarMessage as __
>>> print(__('Message with $num $what', num=2, what='placeholders'))
Message with 2 placeholders
>>>
While the above examples use print() to show how the formatting works, you would of course use logger.
debug()orsimilartoactuallylogusingthisapproach.
Onethingtonoteisthatyoupaynosignificantperformancepenaltywiththisapproach: theactualformattinghappens
notwhenyoumaketheloggingcall,butwhen(andif)theloggedmessageisactuallyabouttobeoutputtoalogbya
handler. Sotheonlyslightlyunusualthingwhichmighttripyouupisthattheparenthesesgoaroundtheformatstring
andthearguments,notjusttheformatstring. That’sbecausethe__notationisjustsyntaxsugarforaconstructorcall
tooneoftheXXXMessageclasses.
Ifyouprefer,youcanuseaLoggerAdaptertoachieveasimilareffecttotheabove,asinthefollowingexample:
import logging
class Message:
def __init__(self, fmt, args):
self.fmt = fmt
self.args = args
def __str__(self):
return self.fmt.format(*self.args)
class StyleAdapter(logging.LoggerAdapter):
def log(self, level, msg, /, *args, stacklevel=1, **kwargs):
if self.isEnabledFor(level):
msg, kwargs = self.process(msg, kwargs)
self.logger.log(level, Message(msg, args), **kwargs,
stacklevel=stacklevel+1)
logger = StyleAdapter(logging.getLogger(__name__))
def main():
logger.debug('Hello, {}', 'world!')
if __name__ == '__main__':
logging.basicConfig(level=logging.DEBUG)
main()
TheabovescriptshouldlogthemessageHello, world!whenrunwithPython3.8orlater.
15 Customizing LogRecord
EveryloggingeventisrepresentedbyaLogRecordinstance. Whenaneventisloggedandnotfilteredoutbyalogger’s
level,aLogRecordiscreated,populatedwithinformationabouttheeventandthenpassedtothehandlersforthat
logger (and its ancestors, up to and including the logger where further propagation up the hierarchy is disabled).
BeforePython3.2,therewereonlytwoplaceswherethiscreationwasdone:
• Logger.makeRecord(),whichiscalledinthenormalprocessoflogginganevent. ThisinvokedLogRecord
directlytocreateaninstance.
30

### 第31页

• makeLogRecord(), which is called with a dictionary containing attributes to be added to the LogRecord.
Thisistypicallyinvokedwhenasuitabledictionaryhasbeenreceivedoverthenetwork(e.g. inpickleform
viaaSocketHandler,orinJSONformviaanHTTPHandler).
This has usually meant that if you need to do anything special with a LogRecord, you’ve had to do one of the
following.
• Create your own Logger subclass, which overrides Logger.makeRecord(), and set it using
setLoggerClass()beforeanyloggersthatyoucareaboutareinstantiated.
• Add a Filter to a logger or handler, which does the necessary special manipulation you need when its
filter()methodiscalled.
The first approach would be a little unwieldy in the scenario where (say) several different libraries wanted to do
differentthings. EachwouldattempttosetitsownLoggersubclass,andtheonewhichdidthislastwouldwin.
Thesecondapproachworksreasonablywellformanycases,butdoesnotallowyoutoe.g. useaspecializedsubclass
ofLogRecord. Librarydeveloperscansetasuitablefilterontheirloggers,buttheywouldhavetoremembertodo
thiseverytimetheyintroducedanewlogger(whichtheywoulddosimplybyaddingnewpackagesormodulesand
doing
logger = logging.getLogger(__name__)
at module level). It’s probably one too many things to think about. Developers could also add the filter to a
NullHandlerattachedtotheirtop-levellogger,butthiswouldnotbeinvokedifanapplicationdeveloperattached
ahandlertoalower-levellibrarylogger—sooutputfromthathandlerwouldnotreflecttheintentionsofthelibrary
developer.
InPython3.2andlater,LogRecordcreationisdonethroughafactory,whichyoucanspecify. Thefactoryisjust
a callable you can set with setLogRecordFactory(), and interrogate with getLogRecordFactory(). The
factoryisinvokedwiththesamesignatureastheLogRecordconstructor,asLogRecordisthedefaultsettingfor
thefactory.
ThisapproachallowsacustomfactorytocontrolallaspectsofLogRecordcreation. Forexample,youcouldreturn
asubclass,orjustaddsomeadditionalattributestotherecordoncecreated,usingapatternsimilartothis:
old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
record = old_factory(*args, **kwargs)
record.custom_attribute = 0xdecafbad
return record
logging.setLogRecordFactory(record_factory)
This pattern allows different libraries to chain factories together, and as long as they don’t overwrite each other’s
attributesorunintentionallyoverwritetheattributesprovidedasstandard,thereshouldbenosurprises. However,it
shouldbeborneinmindthateachlinkinthechainaddsrun-timeoverheadtoallloggingoperations,andthetechnique
shouldonlybeusedwhentheuseofaFilterdoesnotprovidethedesiredresult.
16 Subclassing QueueHandler and QueueListener- a ZeroMQ ex-
ample
16.1 Subclass QueueHandler
YoucanuseaQueueHandlersubclasstosendmessagestootherkindsofqueues,forexampleaZeroMQ‘publish’
socket. Intheexamplebelow,thesocketiscreatedseparatelyandpassedtothehandler(asits‘queue’):
import zmq # using pyzmq, the Python binding for ZeroMQ
import json # for serializing records portably
(continuesonnextpage)
31

### 第32页

(continuedfrompreviouspage)
ctx = zmq.Context()
sock = zmq.Socket(ctx, zmq.PUB) # or zmq.PUSH, or other suitable value
sock.bind('tcp://*:5556') # or wherever
class ZeroMQSocketHandler(QueueHandler):
def enqueue(self, record):
self.queue.send_json(record.__dict__)
handler = ZeroMQSocketHandler(sock)
Ofcoursethereareotherwaysoforganizingthis,forexamplepassinginthedataneededbythehandlertocreatethe
socket:
class ZeroMQSocketHandler(QueueHandler):
def __init__(self, uri, socktype=zmq.PUB, ctx=None):
self.ctx = ctx or zmq.Context()
socket = zmq.Socket(self.ctx, socktype)
socket.bind(uri)
super().__init__(socket)
def enqueue(self, record):
self.queue.send_json(record.__dict__)
def close(self):
self.queue.close()
16.2 Subclass QueueListener
YoucanalsosubclassQueueListenertogetmessagesfromotherkindsofqueues,forexampleaZeroMQ‘sub-
scribe’socket. Here’sanexample:
class ZeroMQSocketListener(QueueListener):
def __init__(self, uri, /, *handlers, **kwargs):
self.ctx = kwargs.get('ctx') or zmq.Context()
socket = zmq.Socket(self.ctx, zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, '') # subscribe to everything
socket.connect(uri)
super().__init__(socket, *handlers, **kwargs)
def dequeue(self):
msg = self.queue.recv_json()
return logging.makeLogRecord(msg)
17 Subclassing QueueHandler and QueueListener- a pynng exam-
ple
In a similar way to the above section, we can implement a listener and handler using pynng, which is a Python
bindingtoNNG,billedasaspiritualsuccessortoZeroMQ.Thefollowingsnippetsillustrate–youcantestthemin
anenvironmentwhichhaspynnginstalled. Justforvariety,wepresentthelistenerfirst.
32

### 第33页

17.1 Subclass QueueListener
# listener.py
import json
import logging
import logging.handlers
import pynng
DEFAULT_ADDR = "tcp://localhost:13232"
interrupted = False
class NNGSocketListener(logging.handlers.QueueListener):
def __init__(self, uri, /, *handlers, **kwargs):
# Have a timeout for interruptability, and open a
# subscriber socket
socket = pynng.Sub0(listen=uri, recv_timeout=500)
# The b'' subscription matches all topics
topics = kwargs.pop('topics', None) or b''
socket.subscribe(topics)
# We treat the socket as a queue
super().__init__(socket, *handlers, **kwargs)
def dequeue(self, block):
data = None
# Keep looping while not interrupted and no data received over the
# socket
while not interrupted:
try:
data = self.queue.recv(block=block)
break
except pynng.Timeout:
pass
except pynng.Closed: # sometimes happens when you hit Ctrl-C
break
if data is None:
return None
# Get the logging event sent from a publisher
event = json.loads(data.decode('utf-8'))
return logging.makeLogRecord(event)
def enqueue_sentinel(self):
# Not used in this implementation, as the socket isn't really a
# queue
pass
logging.getLogger('pynng').propagate = False
listener = NNGSocketListener(DEFAULT_ADDR, logging.StreamHandler(), topics=b'')
listener.start()
print('Press Ctrl-C to stop.')
try:
while True:
pass
except KeyboardInterrupt:
interrupted = True
(continuesonnextpage)
33

### 第34页

(continuedfrompreviouspage)
finally:
listener.stop()
17.2 Subclass QueueHandler
# sender.py
import json
import logging
import logging.handlers
import time
import random
import pynng
DEFAULT_ADDR = "tcp://localhost:13232"
class NNGSocketHandler(logging.handlers.QueueHandler):
def __init__(self, uri):
socket = pynng.Pub0(dial=uri, send_timeout=500)
super().__init__(socket)
def enqueue(self, record):
# Send the record as UTF-8 encoded JSON
d = dict(record.__dict__)
data = json.dumps(d)
self.queue.send(data.encode('utf-8'))
def close(self):
self.queue.close()
logging.getLogger('pynng').propagate = False
handler = NNGSocketHandler(DEFAULT_ADDR)
# Make sure the process ID is in the output
logging.basicConfig(level=logging.DEBUG,
handlers=[logging.StreamHandler(), handler],
format='%(levelname)-8s %(name)10s %(process)6s %(message)s')
levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
logging.CRITICAL)
logger_names = ('myapp', 'myapp.lib1', 'myapp.lib2')
msgno = 1
while True:
# Just randomly select some loggers and levels and log away
level = random.choice(levels)
logger = logging.getLogger(random.choice(logger_names))
logger.log(level, 'Message no. %5d' % msgno)
msgno += 1
delay = random.random() * 2 + 0.5
time.sleep(delay)
Youcanruntheabovetwosnippetsinseparatecommandshells. Ifwerunthelistenerinoneshellandrunthesender
intwoseparateshells,weshouldseesomethinglikethefollowing. Inthefirstsendershell:
$ python sender.py
DEBUG myapp 613 Message no. 1
WARNING myapp.lib2 613 Message no. 2
(continuesonnextpage)
34

### 第35页

(continuedfrompreviouspage)
CRITICAL myapp.lib2 613 Message no. 3
WARNING myapp.lib2 613 Message no. 4
CRITICAL myapp.lib1 613 Message no. 5
DEBUG myapp 613 Message no. 6
CRITICAL myapp.lib1 613 Message no. 7
INFO myapp.lib1 613 Message no. 8
(and so on)
Inthesecondsendershell:
$ python sender.py
INFO myapp.lib2 657 Message no. 1
CRITICAL myapp.lib2 657 Message no. 2
CRITICAL myapp 657 Message no. 3
CRITICAL myapp.lib1 657 Message no. 4
INFO myapp.lib1 657 Message no. 5
WARNING myapp.lib2 657 Message no. 6
CRITICAL myapp 657 Message no. 7
DEBUG myapp.lib1 657 Message no. 8
(and so on)
Inthelistenershell:
$ python listener.py
Press Ctrl-C to stop.
DEBUG myapp 613 Message no. 1
WARNING myapp.lib2 613 Message no. 2
INFO myapp.lib2 657 Message no. 1
CRITICAL myapp.lib2 613 Message no. 3
CRITICAL myapp.lib2 657 Message no. 2
CRITICAL myapp 657 Message no. 3
WARNING myapp.lib2 613 Message no. 4
CRITICAL myapp.lib1 613 Message no. 5
CRITICAL myapp.lib1 657 Message no. 4
INFO myapp.lib1 657 Message no. 5
DEBUG myapp 613 Message no. 6
WARNING myapp.lib2 657 Message no. 6
CRITICAL myapp 657 Message no. 7
CRITICAL myapp.lib1 613 Message no. 7
INFO myapp.lib1 613 Message no. 8
DEBUG myapp.lib1 657 Message no. 8
(and so on)
Asyoucansee,theloggingfromthetwosenderprocessesisinterleavedinthelistener’soutput.
18 An example dictionary-based configuration
Belowisanexampleofaloggingconfigurationdictionary-it’stakenfromthedocumentationontheDjangoproject.
ThisdictionaryispassedtodictConfig()toputtheconfigurationintoeffect:
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
'verbose': {
'format': '{levelname} {asctime} {module} {process:d} {thread:d}
(continuesonnextpage)
35

### 第36页

(continuedfrompreviouspage)
,→{message}',
'style': '{',
},
'simple': {
'format': '{levelname} {message}',
'style': '{',
},
},
'filters': {
'special': {
'()': 'project.logging.SpecialFilter',
'foo': 'bar',
},
},
'handlers': {
'console': {
'level': 'INFO',
'class': 'logging.StreamHandler',
'formatter': 'simple',
},
'mail_admins': {
'level': 'ERROR',
'class': 'django.utils.log.AdminEmailHandler',
'filters': ['special']
}
},
'loggers': {
'django': {
'handlers': ['console'],
'propagate': True,
},
'django.request': {
'handlers': ['mail_admins'],
'level': 'ERROR',
'propagate': False,
},
'myproject.custom': {
'handlers': ['console', 'mail_admins'],
'level': 'INFO',
'filters': ['special']
}
}
}
Formoreinformationaboutthisconfiguration,youcanseetherelevantsectionoftheDjangodocumentation.
19 Using a rotator and namer to customize log rotation processing
Anexampleofhowyoucandefineanamerandrotatorisgiveninthefollowingrunnablescript,whichshowsgzip
compressionofthelogfile:
import gzip
import logging
import logging.handlers
import os
import shutil
(continuesonnextpage)
36

### 第37页

(continuedfrompreviouspage)
def namer(name):
return name + ".gz"
def rotator(source, dest):
with open(source, 'rb') as f_in:
with gzip.open(dest, 'wb') as f_out:
shutil.copyfileobj(f_in, f_out)
os.remove(source)
rh = logging.handlers.RotatingFileHandler('rotated.log', maxBytes=128,␣
,→backupCount=5)
rh.rotator = rotator
rh.namer = namer
root = logging.getLogger()
root.setLevel(logging.INFO)
root.addHandler(rh)
f = logging.Formatter('%(asctime)s %(message)s')
rh.setFormatter(f)
for i in range(1000):
root.info(f'Message no. {i + 1}')
Afterrunningthis,youwillseesixnewfiles,fiveofwhicharecompressed:
$ ls rotated.log*
rotated.log rotated.log.2.gz rotated.log.4.gz
rotated.log.1.gz rotated.log.3.gz rotated.log.5.gz
$ zcat rotated.log.1.gz
2023-01-20 02:28:17,767 Message no. 996
2023-01-20 02:28:17,767 Message no. 997
2023-01-20 02:28:17,767 Message no. 998
20 A more elaborate multiprocessing example
Thefollowingworkingexampleshowshowloggingcanbeusedwithmultiprocessingusingconfigurationfiles. The
configurationsarefairlysimple,butservetoillustratehowmorecomplexonescouldbeimplementedinarealmul-
tiprocessingscenario.
Intheexample,themainprocessspawnsalistenerprocessandsomeworkerprocesses. Eachofthemainprocess,
thelistenerandtheworkershavethreeseparateconfigurations(theworkersallsharethesameconfiguration). We
can see logging in the main process, how the workers log to a QueueHandler and how the listener implements a
QueueListenerandamorecomplexloggingconfiguration,andarrangestodispatcheventsreceivedviathequeueto
thehandlersspecifiedintheconfiguration. Notethattheseconfigurationsarepurelyillustrative,butyoushouldbe
abletoadaptthisexampletoyourownscenario.
Here’sthescript-thedocstringsandthecommentshopefullyexplainhowitworks:
import logging
import logging.config
import logging.handlers
from multiprocessing import Process, Queue, Event, current_process
import os
import random
import time
(continuesonnextpage)
37

### 第38页

(continuedfrompreviouspage)
class MyHandler:
"""
A simple handler for logging events. It runs in the listener process and
dispatches events to loggers based on the name in the received record,
which then get dispatched, by the logging system, to the handlers
configured for those loggers.
"""
def handle(self, record):
if record.name == "root":
logger = logging.getLogger()
else:
logger = logging.getLogger(record.name)
if logger.isEnabledFor(record.levelno):
# The process name is transformed just to show that it's the listener
# doing the logging to files and console
record.processName = '%s (for %s)' % (current_process().name, record.
,→processName)
logger.handle(record)
def listener_process(q, stop_event, config):
"""
This could be done in the main process, but is just done in a separate
process for illustrative purposes.
This initialises logging according to the specified configuration,
starts the listener and waits for the main process to signal completion
via the event. The listener is then stopped, and the process exits.
"""
logging.config.dictConfig(config)
listener = logging.handlers.QueueListener(q, MyHandler())
listener.start()
if os.name == 'posix':
# On POSIX, the setup logger will have been configured in the
# parent process, but should have been disabled following the
# dictConfig call.
# On Windows, since fork isn't used, the setup logger won't
# exist in the child, so it would be created and the message
# would appear - hence the "if posix" clause.
logger = logging.getLogger('setup')
logger.critical('Should not appear, because of disabled logger ...')
stop_event.wait()
listener.stop()
def worker_process(config):
"""
A number of these are spawned for the purpose of illustration. In
practice, they could be a heterogeneous bunch of processes rather than
ones which are identical to each other.
This initialises logging according to the specified configuration,
and logs a hundred messages with random levels to randomly selected
loggers.
(continuesonnextpage)
38

### 第39页

(continuedfrompreviouspage)
A small sleep is added to allow other processes a chance to run. This
is not strictly needed, but it mixes the output from the different
processes a bit more than if it's left out.
"""
logging.config.dictConfig(config)
levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
logging.CRITICAL]
loggers = ['foo', 'foo.bar', 'foo.bar.baz',
'spam', 'spam.ham', 'spam.ham.eggs']
if os.name == 'posix':
# On POSIX, the setup logger will have been configured in the
# parent process, but should have been disabled following the
# dictConfig call.
# On Windows, since fork isn't used, the setup logger won't
# exist in the child, so it would be created and the message
# would appear - hence the "if posix" clause.
logger = logging.getLogger('setup')
logger.critical('Should not appear, because of disabled logger ...')
for i in range(100):
lvl = random.choice(levels)
logger = logging.getLogger(random.choice(loggers))
logger.log(lvl, 'Message no. %d', i)
time.sleep(0.01)
def main():
q = Queue()
# The main process gets a simple configuration which prints to the console.
config_initial = {
'version': 1,
'handlers': {
'console': {
'class': 'logging.StreamHandler',
'level': 'INFO'
}
},
'root': {
'handlers': ['console'],
'level': 'DEBUG'
}
}
# The worker process configuration is just a QueueHandler attached to the
# root logger, which allows all messages to be sent to the queue.
# We disable existing loggers to disable the "setup" logger used in the
# parent process. This is needed on POSIX because the logger will
# be there in the child following a fork().
config_worker = {
'version': 1,
'disable_existing_loggers': True,
'handlers': {
'queue': {
'class': 'logging.handlers.QueueHandler',
'queue': q
}
},
'root': {
'handlers': ['queue'],
(continuesonnextpage)
39

### 第40页

(continuedfrompreviouspage)
'level': 'DEBUG'
}
}
# The listener process configuration shows that the full flexibility of
# logging configuration is available to dispatch events to handlers however
# you want.
# We disable existing loggers to disable the "setup" logger used in the
# parent process. This is needed on POSIX because the logger will
# be there in the child following a fork().
config_listener = {
'version': 1,
'disable_existing_loggers': True,
'formatters': {
'detailed': {
'class': 'logging.Formatter',
'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-
,→10s %(message)s'
},
'simple': {
'class': 'logging.Formatter',
'format': '%(name)-15s %(levelname)-8s %(processName)-10s
,→%(message)s'
}
},
'handlers': {
'console': {
'class': 'logging.StreamHandler',
'formatter': 'simple',
'level': 'INFO'
},
'file': {
'class': 'logging.FileHandler',
'filename': 'mplog.log',
'mode': 'w',
'formatter': 'detailed'
},
'foofile': {
'class': 'logging.FileHandler',
'filename': 'mplog-foo.log',
'mode': 'w',
'formatter': 'detailed'
},
'errors': {
'class': 'logging.FileHandler',
'filename': 'mplog-errors.log',
'mode': 'w',
'formatter': 'detailed',
'level': 'ERROR'
}
},
'loggers': {
'foo': {
'handlers': ['foofile']
}
},
'root': {
(continuesonnextpage)
40

### 第41页

(continuedfrompreviouspage)
'handlers': ['console', 'file', 'errors'],
'level': 'DEBUG'
}
}
# Log some initial events, just to show that logging in the parent works
# normally.
logging.config.dictConfig(config_initial)
logger = logging.getLogger('setup')
logger.info('About to create workers ...')
workers = []
for i in range(5):
wp = Process(target=worker_process, name='worker %d' % (i + 1),
args=(config_worker,))
workers.append(wp)
wp.start()
logger.info('Started worker: %s', wp.name)
logger.info('About to create listener ...')
stop_event = Event()
lp = Process(target=listener_process, name='listener',
args=(q, stop_event, config_listener))
lp.start()
logger.info('Started listener')
# We now hang around for the workers to finish their work.
for wp in workers:
wp.join()
# Workers all done, listening can now stop.
# Logging in the parent still works normally.
logger.info('Telling listener to stop ...')
stop_event.set()
lp.join()
logger.info('All done.')
if __name__ == '__main__':
main()
21 Inserting a BOM into messages sent to a SysLogHandler
RFC5424requiresthataUnicodemessagebesenttoasyslogdaemonasasetofbyteswhichhavethefollowing
structure: anoptionalpure-ASCIIcomponent,followedbyaUTF-8ByteOrderMark(BOM),followedbyUnicode
encodedusingUTF-8. (Seetherelevantsectionofthespecification.)
In Python 3.1, code was added to SysLogHandler to insert a BOM into the message, but unfortunately, it was
implementedincorrectly,withtheBOMappearingatthebeginningofthemessageandhencenotallowinganypure-
ASCIIcomponenttoappearbeforeit.
Asthisbehaviourisbroken,theincorrectBOMinsertioncodeisbeingremovedfromPython3.2.4andlater. How-
ever,itisnotbeingreplaced,andifyouwanttoproduceRFC5424-compliantmessageswhichincludeaBOM,an
optionalpure-ASCIIsequencebeforeitandarbitraryUnicodeafterit, encodedusingUTF-8, thenyouneedtodo
thefollowing:
1. AttachaFormatterinstancetoyourSysLogHandlerinstance,withaformatstringsuchas:
'ASCII section\ufeffUnicode section'
TheUnicodecodepointU+FEFF,whenencodedusingUTF-8,willbeencodedasaUTF-8BOM–thebyte-
stringb'\xef\xbb\xbf'.
41

### 第42页

2. Replace the ASCII section with whatever placeholders you like, but make sure that the data that appears in
thereaftersubstitutionisalwaysASCII(thatway,itwillremainunchangedafterUTF-8encoding).
3. ReplacetheUnicodesectionwithwhateverplaceholdersyoulike;ifthedatawhichappearsthereaftersubsti-
tutioncontainscharactersoutsidetheASCIIrange,that’sfine–itwillbeencodedusingUTF-8.
TheformattedmessagewillbeencodedusingUTF-8encodingbySysLogHandler. Ifyoufollowtheaboverules,
you should be able to produce RFC 5424-compliant messages. If you don’t, logging may not complain, but your
messageswillnotbeRFC5424-compliant,andyoursyslogdaemonmaycomplain.
22 Implementing structured logging
Althoughmostloggingmessagesareintendedforreadingbyhumans,andthusnotreadilymachine-parseable,there
mightbecircumstanceswhereyouwanttooutputmessagesinastructuredformatwhichiscapableofbeingparsed
by a program (without needing complex regular expressions to parse the log message). This is straightforward to
achieveusingtheloggingpackage. Thereareanumberofwaysinwhichthiscouldbeachieved,butthefollowingis
asimpleapproachwhichusesJSONtoserialisetheeventinamachine-parseablemanner:
import json
import logging
class StructuredMessage:
def __init__(self, message, /, **kwargs):
self.message = message
self.kwargs = kwargs
def __str__(self):
return '%s >>> %s' % (self.message, json.dumps(self.kwargs))
_ = StructuredMessage # optional, to improve readability
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(_('message 1', foo='bar', bar='baz', num=123, fnum=123.456))
Iftheabovescriptisrun,itprints:
message 1 >>> {"fnum": 123.456, "num": 123, "bar": "baz", "foo": "bar"}
NotethattheorderofitemsmightbedifferentaccordingtotheversionofPythonused.
Ifyouneedmorespecialisedprocessing,youcanuseacustomJSONencoder,asinthefollowingcompleteexample:
import json
import logging
class Encoder(json.JSONEncoder):
def default(self, o):
if isinstance(o, set):
return tuple(o)
elif isinstance(o, str):
return o.encode('unicode_escape').decode('ascii')
return super().default(o)
class StructuredMessage:
def __init__(self, message, /, **kwargs):
self.message = message
self.kwargs = kwargs
(continuesonnextpage)
42

### 第43页

(continuedfrompreviouspage)
def __str__(self):
s = Encoder().encode(self.kwargs)
return '%s >>> %s' % (self.message, s)
_ = StructuredMessage # optional, to improve readability
def main():
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.info(_('message 1', set_value={1, 2, 3}, snowman='\u2603'))
if __name__ == '__main__':
main()
Whentheabovescriptisrun,itprints:
message 1 >>> {"snowman": "\u2603", "set_value": [1, 2, 3]}
NotethattheorderofitemsmightbedifferentaccordingtotheversionofPythonused.
23 Customizing handlers with dictConfig()
Therearetimeswhenyouwanttocustomizelogginghandlersinparticularways,andifyouusedictConfig()you
may be able to do this without subclassing. As an example, consider that you may want to set the ownership of a
logfile. OnPOSIX,thisiseasilydoneusingshutil.chown(),butthefilehandlersinthestdlibdon’tofferbuilt-in
support. Youcancustomizehandlercreationusingaplainfunctionsuchas:
def owned_file_handler(filename, mode='a', encoding=None, owner=None):
if owner:
if not os.path.exists(filename):
open(filename, 'a').close()
shutil.chown(filename, *owner)
return logging.FileHandler(filename, mode, encoding)
You can then specify, in a logging configuration passed to dictConfig(), that a logging handler be created by
callingthisfunction:
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
'default': {
'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
},
},
'handlers': {
'file':{
# The values below are popped from this dictionary and
# used to create the handler, set the handler's level and
# its formatter.
'()': owned_file_handler,
'level':'DEBUG',
'formatter': 'default',
# The values below are passed to the handler creator callable
# as keyword arguments.
'owner': ['pulse', 'pulse'],
'filename': 'chowntest.log',
(continuesonnextpage)
43

### 第44页

(continuedfrompreviouspage)
'mode': 'w',
'encoding': 'utf-8',
},
},
'root': {
'handlers': ['file'],
'level': 'DEBUG',
},
}
In this example I am setting the ownership using the pulse user and group, just for the purposes of illustration.
Puttingittogetherintoaworkingscript,chowntest.py:
import logging, logging.config, os, shutil
def owned_file_handler(filename, mode='a', encoding=None, owner=None):
if owner:
if not os.path.exists(filename):
open(filename, 'a').close()
shutil.chown(filename, *owner)
return logging.FileHandler(filename, mode, encoding)
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
'default': {
'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
},
},
'handlers': {
'file':{
# The values below are popped from this dictionary and
# used to create the handler, set the handler's level and
# its formatter.
'()': owned_file_handler,
'level':'DEBUG',
'formatter': 'default',
# The values below are passed to the handler creator callable
# as keyword arguments.
'owner': ['pulse', 'pulse'],
'filename': 'chowntest.log',
'mode': 'w',
'encoding': 'utf-8',
},
},
'root': {
'handlers': ['file'],
'level': 'DEBUG',
},
}
logging.config.dictConfig(LOGGING)
logger = logging.getLogger('mylogger')
logger.debug('A debug message')
Torunthis,youwillprobablyneedtorunasroot:
44

### 第45页

$ sudo python3.3 chowntest.py
$ cat chowntest.log
2013-11-05 09:34:51,128 DEBUG mylogger A debug message
$ ls -l chowntest.log
-rw-r--r-- 1 pulse pulse 55 2013-11-05 09:34 chowntest.log
NotethatthisexampleusesPython3.3becausethat’swhereshutil.chown()makesanappearance. Thisapproach
shouldworkwithanyPythonversionthatsupportsdictConfig()-namely,Python2.7,3.2orlater. Withpre-3.3
versions,youwouldneedtoimplementtheactualownershipchangeusinge.g. os.chown().
Inpractice,thehandler-creatingfunctionmaybeinautilitymodulesomewhereinyourproject. Insteadoftheline
intheconfiguration:
'()': owned_file_handler,
youcouldusee.g.:
'()': 'ext://project.util.owned_file_handler',
where project.util can be replaced with the actual name of the package where the function resides. In the
aboveworkingscript,using'ext://__main__.owned_file_handler'shouldwork. Here,theactualcallable
isresolvedbydictConfig()fromtheext:// specification.
This example hopefully also points the way to how you could implement other types of file change - e.g. setting
specificPOSIXpermissionbits-inthesameway,usingos.chmod().
Ofcourse,theapproachcouldalsobeextendedtotypesofhandlerotherthanaFileHandler-forexample,one
oftherotatingfilehandlers,oradifferenttypeofhandleraltogether.
24 Using particular formatting styles throughout your application
InPython3.2,theFormattergainedastylekeywordparameterwhich,whiledefaultingto%forbackwardcom-
patibility, allowed the specification of { or $ to support the formatting approaches supported by str.format()
andstring.Template. Notethatthisgovernstheformattingofloggingmessagesforfinaloutputtologs,andis
completelyorthogonaltohowanindividualloggingmessageisconstructed.
Loggingcalls(debug(), info() etc.) onlytakepositionalparametersfortheactualloggingmessageitself, with
keywordparametersusedonlyfordeterminingoptionsforhowtohandletheloggingcall(e.g. theexc_infokeyword
parameter to indicate that traceback information should be logged, or the extra keyword parameter to indicate
additional contextual information to be added to the log). So you cannot directly make logging calls using str.
format()orstring.Templatesyntax, becauseinternallytheloggingpackageuses%-formattingtomergethe
formatstringandthevariablearguments. Therewouldbenochangingthiswhilepreservingbackwardcompatibility,
sinceallloggingcallswhichareoutthereinexistingcodewillbeusing%-formatstrings.
Therehavebeensuggestionstoassociateformatstyleswithspecificloggers,butthatapproachalsorunsintobackward
compatibilityproblemsbecauseanyexistingcodecouldbeusingagivenloggernameandusing%-formatting.
Forloggingtoworkinteroperablybetweenanythird-partylibrariesandyourcode,decisionsaboutformattingneed
tobemadeattheleveloftheindividualloggingcall. Thisopensupacoupleofwaysinwhichalternativeformatting
stylescanbeaccommodated.
24.1 Using LogRecord factories
InPython3.2,alongwiththeFormatterchangesmentionedabove,theloggingpackagegainedtheabilitytoallow
userstosettheirownLogRecordsubclasses,usingthesetLogRecordFactory()function. Youcanusethistoset
yourownsubclassofLogRecord,whichdoestheRightThingbyoverridingthegetMessage()method. Thebase
class implementation of this method is where the msg % args formatting happens, and where you can substitute
youralternateformatting;however,youshouldbecarefultosupportallformattingstylesandallow%-formattingas
thedefault, toensureinteroperabilitywithothercode. Careshouldalsobetakentocallstr(self.msg), justas
thebaseimplementationdoes.
45

### 第46页

RefertothereferencedocumentationonsetLogRecordFactory()andLogRecordformoreinformation.
24.2 Using custom message objects
Thereisanother,perhapssimplerwaythatyoucanuse{}-and$-formattingtoconstructyourindividuallogmessages.
You may recall (from arbitrary-object-messages) that when logging you can use an arbitrary object as a message
formatstring,andthattheloggingpackagewillcallstr()onthatobjecttogettheactualformatstring. Consider
thefollowingtwoclasses:
class BraceMessage:
def __init__(self, fmt, /, *args, **kwargs):
self.fmt = fmt
self.args = args
self.kwargs = kwargs
def __str__(self):
return self.fmt.format(*self.args, **self.kwargs)
class DollarMessage:
def __init__(self, fmt, /, **kwargs):
self.fmt = fmt
self.kwargs = kwargs
def __str__(self):
from string import Template
return Template(self.fmt).substitute(**self.kwargs)
Either of these can be used in place of a format string, to allow {}- or $-formatting to be used to build the actual
“message”partwhichappearsintheformattedlogoutputinplaceof“%(message)s”or“{message}”or“$message”.
If you find it a little unwieldy to use the class names whenever you want to log something, you can make it more
palatableifyouuseanaliassuchasMor_forthemessage(orperhaps__,ifyouareusing_forlocalization).
Examplesofthisapproacharegivenbelow. Firstly,formattingwithstr.format():
>>> __ = BraceMessage
>>> print(__('Message with {0} {1}', 2, 'placeholders'))
Message with 2 placeholders
>>> class Point: pass
...
>>> p = Point()
>>> p.x = 0.5
>>> p.y = 0.5
>>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})', point=p))
Message with coordinates: (0.50, 0.50)
Secondly,formattingwithstring.Template:
>>> __ = DollarMessage
>>> print(__('Message with $num $what', num=2, what='placeholders'))
Message with 2 placeholders
>>>
Onethingtonoteisthatyoupaynosignificantperformancepenaltywiththisapproach: theactualformattinghappens
notwhenyoumaketheloggingcall,butwhen(andif)theloggedmessageisactuallyabouttobeoutputtoalogbya
handler. Sotheonlyslightlyunusualthingwhichmighttripyouupisthattheparenthesesgoaroundtheformatstring
andthearguments,notjusttheformatstring. That’sbecausethe__notationisjustsyntaxsugarforaconstructorcall
tooneoftheXXXMessageclassesshownabove.
46

### 第47页

25 Configuring filters with dictConfig()
YoucanconfigurefiltersusingdictConfig(), thoughitmightnotbeobviousatfirstglancehowtodoit(hence
thisrecipe). SinceFilteristheonlyfilterclassincludedinthestandardlibrary,anditisunlikelytocatertomany
requirements (it’s only there as a base class), you will typically need to define your own Filter subclass with an
overriddenfilter()method. Todothis,specifythe()keyintheconfigurationdictionaryforthefilter,specifying
acallablewhichwillbeusedtocreatethefilter(aclassisthemostobvious,butyoucanprovideanycallablewhich
returnsaFilterinstance). Hereisacompleteexample:
import logging
import logging.config
import sys
class MyFilter(logging.Filter):
def __init__(self, param=None):
self.param = param
def filter(self, record):
if self.param is None:
allow = True
else:
allow = self.param not in record.msg
if allow:
record.msg = 'changed: ' + record.msg
return allow
LOGGING = {
'version': 1,
'filters': {
'myfilter': {
'()': MyFilter,
'param': 'noshow',
}
},
'handlers': {
'console': {
'class': 'logging.StreamHandler',
'filters': ['myfilter']
}
},
'root': {
'level': 'DEBUG',
'handlers': ['console']
},
}
if __name__ == '__main__':
logging.config.dictConfig(LOGGING)
logging.debug('hello')
logging.debug('hello - noshow')
Thisexampleshowshowyoucanpassconfigurationdatatothecallablewhichconstructstheinstance,intheformof
keywordparameters. Whenrun,theabovescriptwillprint:
changed: hello
whichshowsthatthefilterisworkingasconfigured.
Acoupleofextrapointstonote:
47

### 第48页

• Ifyoucan’trefertothecallabledirectlyintheconfiguration(e.g. ifitlivesinadifferentmodule,andyoucan’t
import it directly where the configuration dictionary is), you can use the form ext://... as described in
logging-config-dict-externalobj. Forexample,youcouldhaveusedthetext'ext://__main__.MyFilter'
insteadofMyFilterintheaboveexample.
• Aswellasforfilters,thistechniquecanalsobeusedtoconfigurecustomhandlersandformatters. Seelogging-
config-dict-userdefformoreinformationonhowloggingsupportsusinguser-definedobjectsinitsconfigura-
tion,andseetheothercookbookrecipeCustomizinghandlerswithdictConfig()above.
26 Customized exception formatting
There might be times when you want to do customized exception formatting - for argument’s sake, let’s say you
wantexactlyonelineperloggedevent,evenwhenexceptioninformationispresent. Youcandothiswithacustom
formatterclass,asshowninthefollowingexample:
import logging
class OneLineExceptionFormatter(logging.Formatter):
def formatException(self, exc_info):
"""
Format an exception so that it prints on a single line.
"""
result = super().formatException(exc_info)
return repr(result) # or format into one line however you want to
def format(self, record):
s = super().format(record)
if record.exc_text:
s = s.replace('\n', '') + '|'
return s
def configure_logging():
fh = logging.FileHandler('output.txt', 'w')
f = OneLineExceptionFormatter('%(asctime)s|%(levelname)s|%(message)s|',
'%d/%m/%Y %H:%M:%S')
fh.setFormatter(f)
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(fh)
def main():
configure_logging()
logging.info('Sample message')
try:
x = 1 / 0
except ZeroDivisionError as e:
logging.exception('ZeroDivisionError: %s', e)
if __name__ == '__main__':
main()
Whenrun,thisproducesafilewithexactlytwolines:
28/01/2015 07:21:23|INFO|Sample message|
28/01/2015 07:21:23|ERROR|ZeroDivisionError: division by zero|'Traceback (most␣
,→recent call last):\n File "logtest7.py", line 30, in main\n x = 1 / 0\
,→nZeroDivisionError: division by zero'|
48

### 第49页

While the above treatment is simplistic, it points the way to how exception information can be formatted to your
liking. Thetracebackmodulemaybehelpfulformorespecializedneeds.
27 Speaking logging messages
Theremightbesituationswhenitisdesirabletohaveloggingmessagesrenderedinanaudibleratherthanavisible
format. Thisiseasytodoifyouhavetext-to-speech(TTS)functionalityavailableinyoursystem,evenifitdoesn’t
haveaPythonbinding. MostTTSsystemshaveacommandlineprogramyoucanrun,andthiscanbeinvokedfrom
a handler using subprocess. It’s assumed here that TTS command line programs won’t expect to interact with
usersortakealongtimetocomplete,andthatthefrequencyofloggedmessageswillbenotsohighastoswampthe
userwithmessages,andthatit’sacceptabletohavethemessagesspokenoneatatimeratherthanconcurrently,The
exampleimplementationbelowwaitsforonemessagetobespokenbeforethenextisprocessed,andthismightcause
otherhandlerstobekeptwaiting. Hereisashortexampleshowingtheapproach,whichassumesthattheespeak
TTSpackageisavailable:
import logging
import subprocess
import sys
class TTSHandler(logging.Handler):
def emit(self, record):
msg = self.format(record)
# Speak slowly in a female English voice
cmd = ['espeak', '-s150', '-ven+f3', msg]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
stderr=subprocess.STDOUT)
# wait for the program to finish
p.communicate()
def configure_logging():
h = TTSHandler()
root = logging.getLogger()
root.addHandler(h)
# the default formatter just returns the message
root.setLevel(logging.DEBUG)
def main():
logging.info('Hello')
logging.debug('Goodbye')
if __name__ == '__main__':
configure_logging()
sys.exit(main())
Whenrun,thisscriptshouldsay“Hello”andthen“Goodbye”inafemalevoice.
Theaboveapproachcan,ofcourse,beadaptedtootherTTSsystemsandevenothersystemsaltogetherwhichcan
processmessagesviaexternalprogramsrunfromacommandline.
28 Buffering logging messages and outputting them conditionally
There might be situations where you want to log messages in a temporary area and only output them if a certain
conditionoccurs. Forexample,youmaywanttostartloggingdebugeventsinafunction,andifthefunctioncompletes
without errors, you don’t want to clutter the log with the collected debug information, but if there is an error, you
wantallthedebuginformationtobeoutputaswellastheerror.
Hereisanexamplewhichshowshowyoucoulddothisusingadecoratorforyourfunctionswhereyouwantlogging
tobehavethisway. Itmakesuseofthelogging.handlers.MemoryHandler,whichallowsbufferingoflogged
49

### 第50页

eventsuntilsomeconditionoccurs,atwhichpointthebufferedeventsareflushed-passedtoanotherhandler(the
targethandler)forprocessing. Bydefault,theMemoryHandlerflushedwhenitsbuffergetsfilleduporanevent
whoselevelisgreaterthanorequaltoaspecifiedthresholdisseen. Youcanusethisrecipewithamorespecialised
subclassofMemoryHandlerifyouwantcustomflushingbehavior.
The example script has a simple function, foo, which just cycles through all the logging levels, writing to sys.
stderr to say what level it’s about to log at, and then actually logging a message at that level. You can pass a
parametertofoowhich,iftrue,willlogatERRORandCRITICALlevels-otherwise,itonlylogsatDEBUG,INFO
andWARNINGlevels.
Thescriptjustarrangestodecoratefoowithadecoratorwhichwilldotheconditionalloggingthat’srequired. The
decoratortakesaloggerasaparameterandattachesamemoryhandlerforthedurationofthecalltothedecorated
function. The decorator can be additionally parameterised using a target handler, a level at which flushing should
occur,andacapacityforthebuffer(numberofrecordsbuffered). ThesedefaulttoaStreamHandlerwhichwrites
tosys.stderr,logging.ERRORand100respectively.
Here’sthescript:
import logging
from logging.handlers import MemoryHandler
import sys
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
def log_if_errors(logger, target_handler=None, flush_level=None, capacity=None):
if target_handler is None:
target_handler = logging.StreamHandler()
if flush_level is None:
flush_level = logging.ERROR
if capacity is None:
capacity = 100
handler = MemoryHandler(capacity, flushLevel=flush_level, target=target_
,→handler)
def decorator(fn):
def wrapper(*args, **kwargs):
logger.addHandler(handler)
try:
return fn(*args, **kwargs)
except Exception:
logger.exception('call failed')
raise
finally:
super(MemoryHandler, handler).flush()
logger.removeHandler(handler)
return wrapper
return decorator
def write_line(s):
sys.stderr.write('%s\n' % s)
def foo(fail=False):
write_line('about to log at DEBUG ...')
logger.debug('Actually logged at DEBUG')
write_line('about to log at INFO ...')
logger.info('Actually logged at INFO')
write_line('about to log at WARNING ...')
(continuesonnextpage)
50

### 第51页

(continuedfrompreviouspage)
logger.warning('Actually logged at WARNING')
if fail:
write_line('about to log at ERROR ...')
logger.error('Actually logged at ERROR')
write_line('about to log at CRITICAL ...')
logger.critical('Actually logged at CRITICAL')
return fail
decorated_foo = log_if_errors(logger)(foo)
if __name__ == '__main__':
logger.setLevel(logging.DEBUG)
write_line('Calling undecorated foo with False')
assert not foo(False)
write_line('Calling undecorated foo with True')
assert foo(True)
write_line('Calling decorated foo with False')
assert not decorated_foo(False)
write_line('Calling decorated foo with True')
assert decorated_foo(True)
Whenthisscriptisrun,thefollowingoutputshouldbeobserved:
Calling undecorated foo with False
about to log at DEBUG ...
about to log at INFO ...
about to log at WARNING ...
Calling undecorated foo with True
about to log at DEBUG ...
about to log at INFO ...
about to log at WARNING ...
about to log at ERROR ...
about to log at CRITICAL ...
Calling decorated foo with False
about to log at DEBUG ...
about to log at INFO ...
about to log at WARNING ...
Calling decorated foo with True
about to log at DEBUG ...
about to log at INFO ...
about to log at WARNING ...
about to log at ERROR ...
Actually logged at DEBUG
Actually logged at INFO
Actually logged at WARNING
Actually logged at ERROR
about to log at CRITICAL ...
Actually logged at CRITICAL
Asyoucansee,actualloggingoutputonlyoccurswhenaneventisloggedwhoseseverityisERRORorgreater,but
inthatcase,anypreviouseventsatlowerseveritiesarealsologged.
Youcanofcourseusetheconventionalmeansofdecoration:
@log_if_errors(logger)
def foo(fail=False):
...
51

### 第52页

29 Sending logging messages to email, with buffering
To illustrate how you can send log messages via email, so that a set number of messages are sent per email, you
can subclass BufferingHandler. In the following example, which you can adapt to suit your specific needs, a
simpletestharnessisprovidedwhichallowsyoutorunthescriptwithcommandlineargumentsspecifyingwhatyou
typicallyneedtosendthingsviaSMTP.(Runthedownloadedscriptwiththe-hargumenttoseetherequiredand
optionalarguments.)
import logging
import logging.handlers
import smtplib
class BufferingSMTPHandler(logging.handlers.BufferingHandler):
def __init__(self, mailhost, port, username, password, fromaddr, toaddrs,
subject, capacity):
logging.handlers.BufferingHandler.__init__(self, capacity)
self.mailhost = mailhost
self.mailport = port
self.username = username
self.password = password
self.fromaddr = fromaddr
if isinstance(toaddrs, str):
toaddrs = [toaddrs]
self.toaddrs = toaddrs
self.subject = subject
self.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5s
,→%(message)s"))
def flush(self):
if len(self.buffer) > 0:
try:
smtp = smtplib.SMTP(self.mailhost, self.mailport)
smtp.starttls()
smtp.login(self.username, self.password)
msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (self.fromaddr,
,→ ','.join(self.toaddrs), self.subject)
for record in self.buffer:
s = self.format(record)
msg = msg + s + "\r\n"
smtp.sendmail(self.fromaddr, self.toaddrs, msg)
smtp.quit()
except Exception:
if logging.raiseExceptions:
raise
self.buffer = []
if __name__ == '__main__':
import argparse
ap = argparse.ArgumentParser()
aa = ap.add_argument
aa('host', metavar='HOST', help='SMTP server')
aa('--port', '-p', type=int, default=587, help='SMTP port')
aa('user', metavar='USER', help='SMTP username')
aa('password', metavar='PASSWORD', help='SMTP password')
aa('to', metavar='TO', help='Addressee for emails')
aa('sender', metavar='SENDER', help='Sender email address')
(continuesonnextpage)
52

### 第53页

(continuedfrompreviouspage)
aa('--subject', '-s',
default='Test Logging email from Python logging module (buffering)',
help='Subject of email')
options = ap.parse_args()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
h = BufferingSMTPHandler(options.host, options.port, options.user,
options.password, options.sender,
options.to, options.subject, 10)
logger.addHandler(h)
for i in range(102):
logger.info("Info index = %d", i)
h.flush()
h.close()
If you run this script and your SMTP server is correctly set up, you should find that it sends eleven emails to the
addresseeyouspecify. Thefirsttenemailswilleachhavetenlogmessages,andtheeleventhwillhavetwomessages.
Thatmakesup102messagesasspecifiedinthescript.
30 Formatting times using UTC (GMT) via configuration
SometimesyouwanttoformattimesusingUTC,whichcanbedoneusingaclasssuchasUTCFormatter,shown
below:
import logging
import time
class UTCFormatter(logging.Formatter):
converter = time.gmtime
andyoucanthenusetheUTCFormatterinyourcodeinsteadofFormatter. Ifyouwanttodothatviaconfigura-
tion,youcanusethedictConfig()APIwithanapproachillustratedbythefollowingcompleteexample:
import logging
import logging.config
import time
class UTCFormatter(logging.Formatter):
converter = time.gmtime
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
'utc': {
'()': UTCFormatter,
'format': '%(asctime)s %(message)s',
},
'local': {
'format': '%(asctime)s %(message)s',
}
},
'handlers': {
'console1': {
'class': 'logging.StreamHandler',
'formatter': 'utc',
(continuesonnextpage)
53

### 第54页

(continuedfrompreviouspage)
},
'console2': {
'class': 'logging.StreamHandler',
'formatter': 'local',
},
},
'root': {
'handlers': ['console1', 'console2'],
}
}
if __name__ == '__main__':
logging.config.dictConfig(LOGGING)
logging.warning('The local time is %s', time.asctime())
Whenthisscriptisrun,itshouldprintsomethinglike:
2015-10-17 12:53:29,501 The local time is Sat Oct 17 13:53:29 2015
2015-10-17 13:53:29,501 The local time is Sat Oct 17 13:53:29 2015
showinghowthetimeisformattedbothaslocaltimeandUTC,oneforeachhandler.
31 Using a context manager for selective logging
Therearetimeswhenitwouldbeusefultotemporarilychangetheloggingconfigurationandrevertitbackafterdoing
something. Forthis,acontextmanageristhemostobviouswayofsavingandrestoringtheloggingcontext. Here
isasimpleexampleofsuchacontextmanager, whichallowsyoutooptionallychangethelogginglevelandadda
logginghandlerpurelyinthescopeofthecontextmanager:
import logging
import sys
class LoggingContext:
def __init__(self, logger, level=None, handler=None, close=True):
self.logger = logger
self.level = level
self.handler = handler
self.close = close
def __enter__(self):
if self.level is not None:
self.old_level = self.logger.level
self.logger.setLevel(self.level)
if self.handler:
self.logger.addHandler(self.handler)
def __exit__(self, et, ev, tb):
if self.level is not None:
self.logger.setLevel(self.old_level)
if self.handler:
self.logger.removeHandler(self.handler)
if self.handler and self.close:
self.handler.close()
# implicit return of None => don't swallow exceptions
Ifyouspecifyalevelvalue,thelogger’slevelissettothatvalueinthescopeofthewithblockcoveredbythecontext
manager. Ifyouspecifyahandler,itisaddedtotheloggeronentrytotheblockandremovedonexitfromtheblock.
54

### 第55页

You can also ask the manager to close the handler for you on block exit - you could do this if you don’t need the
handleranymore.
Toillustratehowitworks,wecanaddthefollowingblockofcodetotheabove:
if __name__ == '__main__':
logger = logging.getLogger('foo')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)
logger.info('1. This should appear just once on stderr.')
logger.debug('2. This should not appear.')
with LoggingContext(logger, level=logging.DEBUG):
logger.debug('3. This should appear once on stderr.')
logger.debug('4. This should not appear.')
h = logging.StreamHandler(sys.stdout)
with LoggingContext(logger, level=logging.DEBUG, handler=h, close=True):
logger.debug('5. This should appear twice - once on stderr and once on␣
,→stdout.')
logger.info('6. This should appear just once on stderr.')
logger.debug('7. This should not appear.')
Weinitiallysetthelogger’sleveltoINFO,somessage#1appearsandmessage#2doesn’t. Wethenchangethelevel
toDEBUGtemporarilyinthefollowingwithblock, andsomessage#3appears. Aftertheblockexits, thelogger’s
levelisrestoredtoINFOandsomessage#4doesn’tappear. Inthenextwithblock,wesettheleveltoDEBUGagain
butalsoaddahandlerwritingtosys.stdout. Thus,message#5appearstwiceontheconsole(onceviastderr
andonceviastdout). Afterthewithstatement’scompletion,thestatusisasitwasbeforesomessage#6appears
(likemessage#1)whereasmessage#7doesn’t(justlikemessage#2).
Ifweruntheresultingscript,theresultisasfollows:
$ python logctx.py
1. This should appear just once on stderr.
3. This should appear once on stderr.
5. This should appear twice - once on stderr and once on stdout.
5. This should appear twice - once on stderr and once on stdout.
6. This should appear just once on stderr.
If we run it again, but pipe stderr to /dev/null, we see the following, which is the only message written to
stdout:
$ python logctx.py 2>/dev/null
5. This should appear twice - once on stderr and once on stdout.
Onceagain,butpipingstdoutto/dev/null,weget:
$ python logctx.py >/dev/null
1. This should appear just once on stderr.
3. This should appear once on stderr.
5. This should appear twice - once on stderr and once on stdout.
6. This should appear just once on stderr.
Inthiscase,themessage#5printedtostdoutdoesn’tappear,asexpected.
Ofcourse,theapproachdescribedherecanbegeneralised,forexampletoattachloggingfilterstemporarily. Note
thattheabovecodeworksinPython2aswellasPython3.
55

### 第56页

32 A CLI application starter template
Here’sanexamplewhichshowshowyoucan:
• Usealogginglevelbasedoncommand-linearguments
• Dispatchtomultiplesubcommandsinseparatefiles,allloggingatthesamelevelinaconsistentway
• Makeuseofsimple,minimalconfiguration
Suppose we have a command-line application whose job is to stop, start or restart some services. This could be
organisedforthepurposesofillustrationasafileapp.pythatisthemainscriptfortheapplication,withindividual
commands implemented in start.py, stop.py and restart.py. Suppose further that we want to control the
verbosityoftheapplicationviaacommand-lineargument,defaultingtologging.INFO.Here’sonewaythatapp.
pycouldbewritten:
import argparse
import importlib
import logging
import os
import sys
def main(args=None):
scriptname = os.path.basename(__file__)
parser = argparse.ArgumentParser(scriptname)
levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
parser.add_argument('--log-level', default='INFO', choices=levels)
subparsers = parser.add_subparsers(dest='command',
help='Available commands:')
start_cmd = subparsers.add_parser('start', help='Start a service')
start_cmd.add_argument('name', metavar='NAME',
help='Name of service to start')
stop_cmd = subparsers.add_parser('stop',
help='Stop one or more services')
stop_cmd.add_argument('names', metavar='NAME', nargs='+',
help='Name of service to stop')
restart_cmd = subparsers.add_parser('restart',
help='Restart one or more services')
restart_cmd.add_argument('names', metavar='NAME', nargs='+',
help='Name of service to restart')
options = parser.parse_args()
# the code to dispatch commands could all be in this file. For the purposes
# of illustration only, we implement each command in a separate module.
try:
mod = importlib.import_module(options.command)
cmd = getattr(mod, 'command')
except (ImportError, AttributeError):
print('Unable to find the code for command \'%s\'' % options.command)
return 1
# Could get fancy here and load configuration from file or dictionary
logging.basicConfig(level=options.log_level,
format='%(levelname)s %(name)s %(message)s')
cmd(options)
if __name__ == '__main__':
sys.exit(main())
Andthestart,stopandrestartcommandscanbeimplementedinseparatemodules,likesoforstarting:
56

### 第57页

# start.py
import logging
logger = logging.getLogger(__name__)
def command(options):
logger.debug('About to start %s', options.name)
# actually do the command processing here ...
logger.info('Started the \'%s\' service.', options.name)
andthusforstopping:
# stop.py
import logging
logger = logging.getLogger(__name__)
def command(options):
n = len(options.names)
if n == 1:
plural = ''
services = '\'%s\'' % options.names[0]
else:
plural = 's'
services = ', '.join('\'%s\'' % name for name in options.names)
i = services.rfind(', ')
services = services[:i] + ' and ' + services[i + 2:]
logger.debug('About to stop %s', services)
# actually do the command processing here ...
logger.info('Stopped the %s service%s.', services, plural)
andsimilarlyforrestarting:
# restart.py
import logging
logger = logging.getLogger(__name__)
def command(options):
n = len(options.names)
if n == 1:
plural = ''
services = '\'%s\'' % options.names[0]
else:
plural = 's'
services = ', '.join('\'%s\'' % name for name in options.names)
i = services.rfind(', ')
services = services[:i] + ' and ' + services[i + 2:]
logger.debug('About to restart %s', services)
# actually do the command processing here ...
logger.info('Restarted the %s service%s.', services, plural)
Ifwerunthisapplicationwiththedefaultloglevel,wegetoutputlikethis:
$ python app.py start foo
INFO start Started the 'foo' service.
(continuesonnextpage)
57

### 第58页

(continuedfrompreviouspage)
$ python app.py stop foo bar
INFO stop Stopped the 'foo' and 'bar' services.
$ python app.py restart foo bar baz
INFO restart Restarted the 'foo', 'bar' and 'baz' services.
Thefirstwordisthelogginglevel,andthesecondwordisthemoduleorpackagenameoftheplacewheretheevent
waslogged.
Ifwechangethelogginglevel,thenwecanchangetheinformationsenttothelog. Forexample,ifwewantmore
information:
$ python app.py --log-level DEBUG start foo
DEBUG start About to start foo
INFO start Started the 'foo' service.
$ python app.py --log-level DEBUG stop foo bar
DEBUG stop About to stop 'foo' and 'bar'
INFO stop Stopped the 'foo' and 'bar' services.
$ python app.py --log-level DEBUG restart foo bar baz
DEBUG restart About to restart 'foo', 'bar' and 'baz'
INFO restart Restarted the 'foo', 'bar' and 'baz' services.
Andifwewantless:
$ python app.py --log-level WARNING start foo
$ python app.py --log-level WARNING stop foo bar
$ python app.py --log-level WARNING restart foo bar baz
Inthiscase,thecommandsdon’tprintanythingtotheconsole,sincenothingatWARNINGleveloraboveisloggedby
them.
33 A Qt GUI for logging
AquestionthatcomesupfromtimetotimeisabouthowtologtoaGUIapplication. TheQtframeworkisapopular
cross-platformUIframeworkwithPythonbindingsusingPySide2orPyQt5libraries.
The following example shows how to log to a Qt GUI. This introduces a simple QtHandler class which takes a
callable,whichshouldbeaslotinthemainthreadthatdoesGUIupdates. Aworkerthreadisalsocreatedtoshow
howyoucanlogtotheGUIfromboththeUIitself(viaabuttonformanuallogging)aswellasaworkerthreaddoing
workinthebackground(here,justloggingmessagesatrandomlevelswithrandomshortdelaysinbetween).
TheworkerthreadisimplementedusingQt’sQThreadclassratherthanthethreadingmodule,astherearecir-
cumstanceswhereonehastouseQThread,whichoffersbetterintegrationwithotherQtcomponents.
The code should work with recent releases of any of PySide6, PyQt6, PySide2 or PyQt5. You should be able
toadapttheapproachtoearlierversionsofQt. Pleaserefertothecommentsinthecodesnippetformoredetailed
information.
import datetime
import logging
import random
import sys
import time
# Deal with minor differences between different Qt packages
try:
(continuesonnextpage)
58

### 第59页

(continuedfrompreviouspage)
from PySide6 import QtCore, QtGui, QtWidgets
Signal = QtCore.Signal
Slot = QtCore.Slot
except ImportError:
try:
from PyQt6 import QtCore, QtGui, QtWidgets
Signal = QtCore.pyqtSignal
Slot = QtCore.pyqtSlot
except ImportError:
try:
from PySide2 import QtCore, QtGui, QtWidgets
Signal = QtCore.Signal
Slot = QtCore.Slot
except ImportError:
from PyQt5 import QtCore, QtGui, QtWidgets
Signal = QtCore.pyqtSignal
Slot = QtCore.pyqtSlot
logger = logging.getLogger(__name__)
#
# Signals need to be contained in a QObject or subclass in order to be correctly
# initialized.
#
class Signaller(QtCore.QObject):
signal = Signal(str, logging.LogRecord)
#
# Output to a Qt GUI is only supposed to happen on the main thread. So, this
# handler is designed to take a slot function which is set up to run in the main
# thread. In this example, the function takes a string argument which is a
# formatted log message, and the log record which generated it. The formatted
# string is just a convenience - you could format a string for output any way
# you like in the slot function itself.
#
# You specify the slot function to do whatever GUI updates you want. The handler
# doesn't know or care about specific UI elements.
#
class QtHandler(logging.Handler):
def __init__(self, slotfunc, *args, **kwargs):
super().__init__(*args, **kwargs)
self.signaller = Signaller()
self.signaller.signal.connect(slotfunc)
def emit(self, record):
s = self.format(record)
self.signaller.signal.emit(s, record)
#
# This example uses QThreads, which means that the threads at the Python level
# are named something like "Dummy-1". The function below gets the Qt name of the
# current thread.
#
def ctname():
return QtCore.QThread.currentThread().objectName()
(continuesonnextpage)
59

### 第60页

(continuedfrompreviouspage)
#
# Used to generate random levels for logging.
#
LEVELS = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
logging.CRITICAL)
#
# This worker class represents work that is done in a thread separate to the
# main thread. The way the thread is kicked off to do work is via a button press
# that connects to a slot in the worker.
#
# Because the default threadName value in the LogRecord isn't much use, we add
# a qThreadName which contains the QThread name as computed above, and pass that
# value in an "extra" dictionary which is used to update the LogRecord with the
# QThread name.
#
# This example worker just outputs messages sequentially, interspersed with
# random delays of the order of a few seconds.
#
class Worker(QtCore.QObject):
@Slot()
def start(self):
extra = {'qThreadName': ctname() }
logger.debug('Started work', extra=extra)
i = 1
# Let the thread run until interrupted. This allows reasonably clean
# thread termination.
while not QtCore.QThread.currentThread().isInterruptionRequested():
delay = 0.5 + random.random() * 2
time.sleep(delay)
try:
if random.random() < 0.1:
raise ValueError('Exception raised: %d' % i)
else:
level = random.choice(LEVELS)
logger.log(level, 'Message after delay of %3.1f: %d', delay, i,
,→ extra=extra)
except ValueError as e:
logger.exception('Failed: %s', e, extra=extra)
i += 1
#
# Implement a simple UI for this cookbook example. This contains:
#
# * A read-only text edit window which holds formatted log messages
# * A button to start work and log stuff in a separate thread
# * A button to log something from the main thread
# * A button to clear the log window
#
class Window(QtWidgets.QWidget):
COLORS = {
logging.DEBUG: 'black',
logging.INFO: 'blue',
(continuesonnextpage)
60

### 第61页

(continuedfrompreviouspage)
logging.WARNING: 'orange',
logging.ERROR: 'red',
logging.CRITICAL: 'purple',
}
def __init__(self, app):
super().__init__()
self.app = app
self.textedit = te = QtWidgets.QPlainTextEdit(self)
# Set whatever the default monospace font is for the platform
f = QtGui.QFont('nosuchfont')
if hasattr(f, 'Monospace'):
f.setStyleHint(f.Monospace)
else:
f.setStyleHint(f.StyleHint.Monospace) # for Qt6
te.setFont(f)
te.setReadOnly(True)
PB = QtWidgets.QPushButton
self.work_button = PB('Start background work', self)
self.log_button = PB('Log a message at a random level', self)
self.clear_button = PB('Clear log window', self)
self.handler = h = QtHandler(self.update_status)
# Remember to use qThreadName rather than threadName in the format string.
fs = '%(asctime)s %(qThreadName)-12s %(levelname)-8s %(message)s'
formatter = logging.Formatter(fs)
h.setFormatter(formatter)
logger.addHandler(h)
# Set up to terminate the QThread when we exit
app.aboutToQuit.connect(self.force_quit)
# Lay out all the widgets
layout = QtWidgets.QVBoxLayout(self)
layout.addWidget(te)
layout.addWidget(self.work_button)
layout.addWidget(self.log_button)
layout.addWidget(self.clear_button)
self.setFixedSize(900, 400)
# Connect the non-worker slots and signals
self.log_button.clicked.connect(self.manual_update)
self.clear_button.clicked.connect(self.clear_display)
# Start a new worker thread and connect the slots for the worker
self.start_thread()
self.work_button.clicked.connect(self.worker.start)
# Once started, the button should be disabled
self.work_button.clicked.connect(lambda : self.work_button.
,→setEnabled(False))
def start_thread(self):
self.worker = Worker()
self.worker_thread = QtCore.QThread()
self.worker.setObjectName('Worker')
self.worker_thread.setObjectName('WorkerThread') # for qThreadName
self.worker.moveToThread(self.worker_thread)
# This will start an event loop in the worker thread
(continuesonnextpage)
61

### 第62页

(continuedfrompreviouspage)
self.worker_thread.start()
def kill_thread(self):
# Just tell the worker to stop, then tell it to quit and wait for that
# to happen
self.worker_thread.requestInterruption()
if self.worker_thread.isRunning():
self.worker_thread.quit()
self.worker_thread.wait()
else:
print('worker has already exited.')
def force_quit(self):
# For use when the window is closed
if self.worker_thread.isRunning():
self.kill_thread()
# The functions below update the UI and run in the main thread because
# that's where the slots are set up
@Slot(str, logging.LogRecord)
def update_status(self, status, record):
color = self.COLORS.get(record.levelno, 'black')
s = '<pre><font color="%s">%s</font></pre>' % (color, status)
self.textedit.appendHtml(s)
@Slot()
def manual_update(self):
# This function uses the formatted message passed in, but also uses
# information from the record to format the message in an appropriate
# color according to its severity (level).
level = random.choice(LEVELS)
extra = {'qThreadName': ctname() }
logger.log(level, 'Manually logged!', extra=extra)
@Slot()
def clear_display(self):
self.textedit.clear()
def main():
QtCore.QThread.currentThread().setObjectName('MainThread')
logging.getLogger().setLevel(logging.DEBUG)
app = QtWidgets.QApplication(sys.argv)
example = Window(app)
example.show()
if hasattr(app, 'exec'):
rc = app.exec()
else:
rc = app.exec_()
sys.exit(rc)
if __name__=='__main__':
main()
62

### 第63页

34 Logging to syslog with RFC5424 support
Although RFC 5424 dates from 2009, most syslog servers are configured by default to use the older RFC 3164,
whichhailsfrom2001. WhenloggingwasaddedtoPythonin2003, itsupportedtheearlier(andonlyexisting)
protocolatthetime. SinceRFC5424cameout,astherehasnotbeenwidespreaddeploymentofitinsyslogservers,
theSysLogHandlerfunctionalityhasnotbeenupdated.
RFC5424containssomeusefulfeaturessuchassupportforstructureddata,andifyouneedtobeabletologtoa
syslogserverwithsupportforit,youcandosowithasubclassedhandlerwhichlookssomethinglikethis:
import datetime
import logging.handlers
import re
import socket
import time
class SysLogHandler5424(logging.handlers.SysLogHandler):
tz_offset = re.compile(r'([+-]\d{2})(\d{2})$')
escaped = re.compile(r'([\]"\\])')
def __init__(self, *args, **kwargs):
self.msgid = kwargs.pop('msgid', None)
self.appname = kwargs.pop('appname', None)
super().__init__(*args, **kwargs)
def format(self, record):
version = 1
asctime = datetime.datetime.fromtimestamp(record.created).isoformat()
m = self.tz_offset.match(time.strftime('%z'))
has_offset = False
if m and time.timezone:
hrs, mins = m.groups()
if int(hrs) or int(mins):
has_offset = True
if not has_offset:
asctime += 'Z'
else:
asctime += f'{hrs}:{mins}'
try:
hostname = socket.gethostname()
except Exception:
hostname = '-'
appname = self.appname or '-'
procid = record.process
msgid = '-'
msg = super().format(record)
sdata = '-'
if hasattr(record, 'structured_data'):
sd = record.structured_data
# This should be a dict where the keys are SD-ID and the value is a
# dict mapping PARAM-NAME to PARAM-VALUE (refer to the RFC for what␣
,→these
# mean)
# There's no error checking here - it's purely for illustration, and␣
,→you
# can adapt this code for use in production environments
parts = []
(continuesonnextpage)
63

### 第64页

(continuedfrompreviouspage)
def replacer(m):
g = m.groups()
return '\\' + g[0]
for sdid, dv in sd.items():
part = f'[{sdid}'
for k, v in dv.items():
s = str(v)
s = self.escaped.sub(replacer, s)
part += f' {k}="{s}"'
part += ']'
parts.append(part)
sdata = ''.join(parts)
return f'{version} {asctime} {hostname} {appname} {procid} {msgid} {sdata}
,→{msg}'
You’llneedtobefamiliarwithRFC5424tofullyunderstandtheabovecode,anditmaybethatyouhaveslightly
differentneeds(e.g. forhowyoupassstructuraldatatothelog). Nevertheless,theaboveshouldbeadaptabletoyour
speciricneeds. Withtheabovehandler,you’dpassstructureddatausingsomethinglikethis:
sd = {
'foo@12345': {'bar': 'baz', 'baz': 'bozz', 'fizz': r'buzz'},
'foo@54321': {'rab': 'baz', 'zab': 'bozz', 'zzif': r'buzz'}
}
extra = {'structured_data': sd}
i = 1
logger.debug('Message %d', i, extra=extra)
35 How to treat a logger like an output stream
Sometimes, youneedtointerfacetoathird-partyAPIwhichexpectsafile-likeobjecttowriteto, butyouwantto
directtheAPI’soutputtoalogger. Youcandothisusingaclasswhichwrapsaloggerwithafile-likeAPI.Here’sa
shortscriptillustratingsuchaclass:
import logging
class LoggerWriter:
def __init__(self, logger, level):
self.logger = logger
self.level = level
def write(self, message):
if message != '\n': # avoid printing bare newlines, if you like
self.logger.log(self.level, message)
def flush(self):
# doesn't actually do anything, but might be expected of a file-like
# object - so optional depending on your situation
pass
def close(self):
# doesn't actually do anything, but might be expected of a file-like
# object - so optional depending on your situation. You might want
# to set a flag so that later calls to write raise an exception
(continuesonnextpage)
64

### 第65页

(continuedfrompreviouspage)
pass
def main():
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('demo')
info_fp = LoggerWriter(logger, logging.INFO)
debug_fp = LoggerWriter(logger, logging.DEBUG)
print('An INFO message', file=info_fp)
print('A DEBUG message', file=debug_fp)
if __name__ == "__main__":
main()
Whenthisscriptisrun,itprints
INFO:demo:An INFO message
DEBUG:demo:A DEBUG message
YoucouldalsouseLoggerWritertoredirectsys.stdoutandsys.stderrbydoingsomethinglikethis:
import sys
sys.stdout = LoggerWriter(logger, logging.INFO)
sys.stderr = LoggerWriter(logger, logging.WARNING)
Youshoulddothisafter configuringloggingforyourneeds. Intheaboveexample,thebasicConfig()calldoes
this(usingthesys.stderrvaluebeforeitisoverwrittenbyaLoggerWriterinstance). Then,you’dgetthiskind
ofresult:
>>> print('Foo')
INFO:demo:Foo
>>> print('Bar', file=sys.stderr)
WARNING:demo:Bar
>>>
Of course, the examples above show output according to the format used by basicConfig(), butyou can use a
differentformatterwhenyouconfigurelogging.
Notethatwiththeabovescheme,youaresomewhatatthemercyofbufferingandthesequenceofwritecallswhich
youareintercepting. Forexample,withthedefinitionofLoggerWriterabove,ifyouhavethesnippet
sys.stderr = LoggerWriter(logger, logging.WARNING)
1 / 0
thenrunningthescriptresultsin
WARNING:demo:Traceback (most recent call last):
WARNING:demo: File "/home/runner/cookbook-loggerwriter/test.py", line 53, in
,→<module>
WARNING:demo:
WARNING:demo:main()
WARNING:demo: File "/home/runner/cookbook-loggerwriter/test.py", line 49, in main
WARNING:demo:
WARNING:demo:1 / 0
WARNING:demo:ZeroDivisionError
(continuesonnextpage)
65

### 第66页

(continuedfrompreviouspage)
WARNING:demo::
WARNING:demo:division by zero
As you can see, this output isn’t ideal. That’s because the underlying code which writes to sys.stderr makes
multiple writes, each of which results in a separate logged line (for example, the last three lines above). To get
aroundthisproblem,youneedtobufferthingsandonlyoutputloglineswhennewlinesareseen. Let’suseaslightly
betterimplementationofLoggerWriter:
class BufferingLoggerWriter(LoggerWriter):
def __init__(self, logger, level):
super().__init__(logger, level)
self.buffer = ''
def write(self, message):
if '\n' not in message:
self.buffer += message
else:
parts = message.split('\n')
if self.buffer:
s = self.buffer + parts.pop(0)
self.logger.log(self.level, s)
self.buffer = parts.pop()
for part in parts:
self.logger.log(self.level, part)
This just buffers up stuff until a newline is seen, and then logs complete lines. With this approach, you get better
output:
WARNING:demo:Traceback (most recent call last):
WARNING:demo: File "/home/runner/cookbook-loggerwriter/main.py", line 55, in
,→<module>
WARNING:demo: main()
WARNING:demo: File "/home/runner/cookbook-loggerwriter/main.py", line 52, in main
WARNING:demo: 1/0
WARNING:demo:ZeroDivisionError: division by zero
36 How to uniformly handle newlines in logging output
Usually,messagesthatarelogged(saytoconsoleorfile)consistofasinglelineoftext. However,sometimesthereis
aneedtohandlemessageswithmultiplelines-whetherbecausealoggingformatstringcontainsnewlines,orlogged
data contains newlines. If you want to handle such messages uniformly, so that each line in the logged message
appearsuniformlyformattedasifitwasloggedseparately,youcandothisusingahandlermixin,asinthefollowing
snippet:
# Assume this is in a module mymixins.py
import copy
class MultilineMixin:
def emit(self, record):
s = record.getMessage()
if '\n' not in s:
super().emit(record)
else:
lines = s.splitlines()
rec = copy.copy(record)
rec.args = None
(continuesonnextpage)
66

### 第67页

(continuedfrompreviouspage)
for line in lines:
rec.msg = line
super().emit(rec)
Youcanusethemixinasinthefollowingscript:
import logging
from mymixins import MultilineMixin
logger = logging.getLogger(__name__)
class StreamHandler(MultilineMixin, logging.StreamHandler):
pass
if __name__ == '__main__':
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-9s
,→%(message)s',
handlers = [StreamHandler()])
logger.debug('Single line')
logger.debug('Multiple lines:\nfool me once ...')
logger.debug('Another single line')
logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')
Thescript,whenrun,printssomethinglike:
2025-07-02 13:54:47,234 DEBUG Single line
2025-07-02 13:54:47,234 DEBUG Multiple lines:
2025-07-02 13:54:47,234 DEBUG fool me once ...
2025-07-02 13:54:47,234 DEBUG Another single line
2025-07-02 13:54:47,234 DEBUG Multiple lines:
2025-07-02 13:54:47,234 DEBUG fool me ...
2025-07-02 13:54:47,234 DEBUG can't get fooled again
If,ontheotherhand,youareconcernedaboutloginjection,youcanuseaformatterwhichescapesnewlines,asper
thefollowingexample:
import logging
logger = logging.getLogger(__name__)
class EscapingFormatter(logging.Formatter):
def format(self, record):
s = super().format(record)
return s.replace('\n', r'\n')
if __name__ == '__main__':
h = logging.StreamHandler()
h.setFormatter(EscapingFormatter('%(asctime)s %(levelname)-9s %(message)s'))
logging.basicConfig(level=logging.DEBUG, handlers = [h])
logger.debug('Single line')
logger.debug('Multiple lines:\nfool me once ...')
logger.debug('Another single line')
logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')
You can, of course, use whatever escaping scheme makes the most sense for you. The script, when run, should
produceoutputlikethis:
67

### 第68页

2025-07-09 06:47:33,783 DEBUG Single line
2025-07-09 06:47:33,783 DEBUG Multiple lines:\nfool me once ...
2025-07-09 06:47:33,783 DEBUG Another single line
2025-07-09 06:47:33,783 DEBUG Multiple lines:\nfool me ...\ncan't get fooled␣
,→again
Escapingbehaviourcan’tbethestdlibdefault,asitwouldbreakbackwardscompatibility.
37 Patterns to avoid
Althoughtheprecedingsectionshavedescribedwaysofdoingthingsyoumightneedtodoordealwith,itisworth
mentioning some usage patterns which are unhelpful, and which should therefore be avoided in most cases. The
followingsectionsareinnoparticularorder.
37.1 Opening the same log file multiple times
OnWindows,youwillgenerallynotbeabletoopenthesamefilemultipletimesasthiswillleadtoa“fileisinuse
byanotherprocess”error. However,onPOSIXplatformsyou’llnotgetanyerrorsifyouopenthesamefilemultiple
times. Thiscouldbedoneaccidentally,forexampleby:
• Adding a file handler more than once which references the same file (e.g. by a copy/paste/forget-to-change
error).
• Openingtwofilesthatlookdifferent,astheyhavedifferentnames,butarethesamebecauseoneisasymbolic
linktotheother.
• Forking a process, following which both parent and child have a reference to the same file. This might be
throughuseofthemultiprocessingmodule,forexample.
Openingafilemultipletimesmightappeartoworkmostofthetime,butcanleadtoanumberofproblemsinpractice:
• Loggingoutputcanbegarbledbecausemultiplethreadsorprocessestrytowritetothesamefile. Although
loggingguardsagainstconcurrentuseofthesamehandlerinstancebymultiplethreads,thereisnosuchpro-
tectionifconcurrentwritesareattemptedbytwodifferentthreadsusingtwodifferenthandlerinstanceswhich
happentopointtothesamefile.
• Anattempttodeleteafile(e.g. duringfilerotation)silentlyfails,becausethereisanotherreferencepointingto
it. Thiscanleadtoconfusionandwasteddebuggingtime-logentriesendupinunexpectedplaces,orarelost
altogether. Orafilethatwassupposedtobemovedremainsinplace,andgrowsinsizeunexpectedlydespite
size-basedrotationbeingsupposedlyinplace.
UsethetechniquesoutlinedinLoggingtoasinglefilefrommultipleprocessestocircumventsuchissues.
37.2 Using loggers as attributes in a class or passing them as parameters
While there might be unusual cases where you’ll need to do this, in general there is no point because loggers are
singletons. Codecanalwaysaccessagivenloggerinstancebynameusinglogging.getLogger(name),sopassing
instancesaroundandholdingthemasinstanceattributesispointless. NotethatinotherlanguagessuchasJavaand
C#,loggersareoftenstaticclassattributes. However,thispatterndoesn’tmakesenseinPython,wherethemodule
(andnottheclass)istheunitofsoftwaredecomposition.
37.3 Adding handlers other than NullHandler to a logger in a library
Configuringloggingbyaddinghandlers,formattersandfiltersistheresponsibilityoftheapplicationdeveloper,not
thelibrarydeveloper. Ifyouaremaintainingalibrary,ensurethatyoudon’taddhandlerstoanyofyourloggersother
thanaNullHandlerinstance.
68

### 第69页

37.4 Creating a lot of loggers
Loggers are singletons that are never freed during a script execution, and so creating lots of loggers will use up
memorywhichcan’tthenbefreed. Ratherthancreatealoggerpere.g. fileprocessedornetworkconnectionmade,
usetheexistingmechanismsforpassingcontextualinformationintoyourlogsandrestricttheloggerscreatedtothose
describingareaswithinyourapplication(generallymodules,butoccasionallyslightlymorefine-grainedthanthat).
38 Other resources
(cid:181) Seealso
Modulelogging
APIreferencefortheloggingmodule.
Modulelogging.config
ConfigurationAPIfortheloggingmodule.
Modulelogging.handlers
Usefulhandlersincludedwiththeloggingmodule.
BasicTutorial
AdvancedTutorial
69

| (cid:181) Seealso |
| --- |
| Modulelogging
APIreferencefortheloggingmodule.
Modulelogging.config
ConfigurationAPIfortheloggingmodule.
Modulelogging.handlers
Usefulhandlersincludedwiththeloggingmodule.
BasicTutorial
AdvancedTutorial |

### 第70页

Index
R
RFC
RFC 3164,63
RFC 5424,41,42,63
RFC 5424 Section 6,41
70

