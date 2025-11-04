### 第1页

Logging HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 BasicLoggingTutorial 2
1.1 Whentouselogging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Asimpleexample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Loggingtoafile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Loggingvariabledata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Changingtheformatofdisplayedmessages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6 Displayingthedate/timeinmessages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.7 NextSteps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 AdvancedLoggingTutorial 5
2.1 LoggingFlow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Loggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 Handlers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.4 Formatters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.5 ConfiguringLogging. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.6 Whathappensifnoconfigurationisprovided . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.7 ConfiguringLoggingforaLibrary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3 LoggingLevels 13
3.1 CustomLevels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 UsefulHandlers 14
5 Exceptionsraisedduringlogging 15
6 Usingarbitraryobjectsasmessages 15
7 Optimization 15
8 Otherresources 16
Index 17
Author
VinaySajip<vinay_sajipatred-dovedotcom>
1

### 第2页

Thispagecontainstutorialinformation. Forlinkstoreferenceinformationandaloggingcookbook,pleaseseeOther
resources.
1 Basic Logging Tutorial
Loggingisameansoftrackingeventsthathappenwhensomesoftwareruns. Thesoftware’sdeveloperaddslogging
callstotheircodetoindicatethatcertaineventshaveoccurred. Aneventisdescribedbyadescriptivemessagewhich
canoptionallycontainvariabledata(i.e. datathatispotentiallydifferentforeachoccurrenceoftheevent). Events
also have an importance which the developer ascribes to the event; the importance can also be called the level or
severity.
1.1 When to use logging
Youcanaccessloggingfunctionalitybycreatingaloggervialogger = getLogger(__name__),andthencalling
the logger’s debug(), info(), warning(), error() and critical() methods. To determine when to use
logging, andtoseewhichloggermethodstousewhen, seethetablebelow. Itstates, foreachofasetofcommon
tasks,thebesttooltouseforthattask.
Taskyouwanttoperform Thebesttoolforthetask
Display console output for ordi- print()
nary usage of a command line
scriptorprogram
Report events that occur during Alogger’sinfo()(ordebug()methodforverydetailedoutputfordiagnos-
normal operation of a program ticpurposes)
(e.g. for status monitoring or
faultinvestigation)
Issueawarningregardingapar- warnings.warn() in library code if the issue is avoidable and the client
ticularruntimeevent applicationshouldbemodifiedtoeliminatethewarning
A logger’s warning() methodifthere isnothing theclientapplication can
doaboutthesituation,buttheeventshouldstillbenoted
Reportanerrorregardingapar- Raiseanexception
ticularruntimeevent
Report suppression of an error Alogger’serror(),exception()orcritical()methodasappropriate
withoutraisinganexception(e.g. forthespecificerrorandapplicationdomain
error handler in a long-running
serverprocess)
Theloggermethodsarenamedafterthelevelorseverityoftheeventstheyareusedtotrack. Thestandardlevelsand
theirapplicabilityaredescribedbelow(inincreasingorderofseverity):
Level Whenit’sused
DEBUG Detailedinformation,typicallyofinterestonlywhendiagnosingproblems.
INFO Confirmationthatthingsareworkingasexpected.
WARNING Anindicationthatsomethingunexpectedhappened,orindicativeofsomeprobleminthenear
future(e.g. ‘diskspacelow’). Thesoftwareisstillworkingasexpected.
ERROR Duetoamoreseriousproblem,thesoftwarehasnotbeenabletoperformsomefunction.
CRITICAL Aseriouserror,indicatingthattheprogramitselfmaybeunabletocontinuerunning.
Thedefaultlevelis WARNING,whichmeansthatonlyeventsofthisseverityandhigherwillbe tracked, unlessthe
loggingpackageisconfiguredtodootherwise.
Eventsthataretrackedcanbehandledindifferentways. Thesimplestwayofhandlingtrackedeventsistoprintthem
totheconsole. Anothercommonwayistowritethemtoadiskfile.
2

| Taskyouwanttoperform | Thebesttoolforthetask |
| --- | --- |
| Display console output for ordi-
nary usage of a command line
scriptorprogram | print() |
| Report events that occur during
normal operation of a program
(e.g. for status monitoring or
faultinvestigation) | Alogger’sinfo()(ordebug()methodforverydetailedoutputfordiagnos-
ticpurposes) |
| Issueawarningregardingapar-
ticularruntimeevent | warnings.warn() in library code if the issue is avoidable and the client
applicationshouldbemodifiedtoeliminatethewarning
A logger’s warning() methodifthere isnothing theclientapplication can
doaboutthesituation,buttheeventshouldstillbenoted |
| Reportanerrorregardingapar-
ticularruntimeevent | Raiseanexception |
| Report suppression of an error
withoutraisinganexception(e.g.
error handler in a long-running
serverprocess) | Alogger’serror(),exception()orcritical()methodasappropriate
forthespecificerrorandapplicationdomain |


| Level | Whenit’sused |
| --- | --- |
| DEBUG | Detailedinformation,typicallyofinterestonlywhendiagnosingproblems. |
| INFO | Confirmationthatthingsareworkingasexpected. |
| WARNING | Anindicationthatsomethingunexpectedhappened,orindicativeofsomeprobleminthenear
future(e.g. ‘diskspacelow’). Thesoftwareisstillworkingasexpected. |
| ERROR | Duetoamoreseriousproblem,thesoftwarehasnotbeenabletoperformsomefunction. |
| CRITICAL | Aseriouserror,indicatingthattheprogramitselfmaybeunabletocontinuerunning. |

### 第3页

1.2 A simple example
Averysimpleexampleis:
import logging
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
Ifyoutypetheselinesintoascriptandrunit,you’llsee:
WARNING:root:Watch out!
printed out on the console. The INFO message doesn’t appear because the default level is WARNING. The printed
messageincludestheindicationofthelevelandthedescriptionoftheeventprovidedintheloggingcall,i.e. ‘Watch
out!’. Theactualoutputcanbeformattedquiteflexiblyifyouneedthat; formattingoptionswillalsobeexplained
later.
Noticethatinthisexample,weusefunctionsdirectlyontheloggingmodule,likelogging.debug,ratherthan
creatingaloggerandcallingfunctionsonit. Thesefunctionsoperateontherootlogger, butcanbeusefulasthey
willcallbasicConfig()foryouifithasnotbeencalledyet,likeinthisexample. Inlargerprogramsyou’llusually
wanttocontroltheloggingconfigurationexplicitlyhowever-soforthatreasonaswellasothers,it’sbettertocreate
loggersandcalltheirmethods.
1.3 Logging to a file
A very common situation is that of recording logging events in a file, so let’s look at that next. Be sure to try the
followinginanewlystartedPythoninterpreter,anddon’tjustcontinuefromthesessiondescribedabove:
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
Changed in version 3.9: The encoding argument was added. In earlier Python versions, or if not specified, the
encodingusedisthedefaultvalueusedbyopen(). Whilenotshownintheaboveexample,anerrorsargumentcan
alsonowbepassed,whichdetermineshowencodingerrorsarehandled. Foravailablevaluesandthedefault,seethe
documentationforopen().
Andnowifweopenthefileandlookatwhatwehave,weshouldfindthelogmessages:
DEBUG:__main__:This message should go to the log file
INFO:__main__:So should this
WARNING:__main__:And this, too
ERROR:__main__:And non-ASCII stuff, too, like Øresund and Malmö
This example also shows how you can set the logging level which acts as the threshold for tracking. In this case,
becausewesetthethresholdtoDEBUG,allofthemessageswereprinted.
Ifyouwanttosetthelogginglevelfromacommand-lineoptionsuchas:
--log=INFO
andyouhavethevalueoftheparameterpassedfor--loginsomevariableloglevel,youcanuse:
getattr(logging, loglevel.upper())
togetthevaluewhichyou’llpasstobasicConfig()viathelevelargument. Youmaywanttoerrorcheckanyuser
inputvalue,perhapsasinthefollowingexample:
3

### 第4页

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level, ...)
The call to basicConfig() should come before any calls to a logger’s methods such as debug(), info(), etc.
Otherwise,thatloggingeventmaynotbehandledinthedesiredmanner.
If you run the above script several times, the messages from successive runs are appended to the file example.log.
Ifyouwanteachruntostartafresh,notrememberingthemessagesfromearlierruns,youcanspecifythefilemode
argument,bychangingthecallintheaboveexampleto:
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
Theoutputwillbethesameasbefore,butthelogfileisnolongerappendedto,sothemessagesfromearlierrunsare
lost.
1.4 Logging variable data
Tologvariabledata,useaformatstringfortheeventdescriptionmessageandappendthevariabledataasarguments.
Forexample:
import logging
logging.warning('%s before you %s', 'Look', 'leap!')
willdisplay:
WARNING:root:Look before you leap!
Asyoucansee,mergingofvariabledataintotheeventdescriptionmessageusestheold,%-styleofstringformatting.
Thisisforbackwardscompatibility: theloggingpackagepre-datesnewerformattingoptionssuchasstr.format()
andstring.Template. Thesenewerformattingoptionsaresupported,butexploringthemisoutsidethescopeof
thistutorial: seeformatting-stylesformoreinformation.
1.5 Changing the format of displayed messages
Tochangetheformatwhichisusedtodisplaymessages,youneedtospecifytheformatyouwanttouse:
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
whichwouldprint:
DEBUG:This message should appear on the console
INFO:So should this
WARNING:And this, too
Noticethatthe‘root’whichappearedinearlierexamples hasdisappeared. Fora fullsetofthingsthatcanappear
in format strings, you can refer to the documentation for logrecord-attributes, but for simple usage, you just need
thelevelname(severity),message(eventdescription,includingvariabledata)andperhapstodisplaywhentheevent
occurred. Thisisdescribedinthenextsection.
4

### 第5页

1.6 Displaying the date/time in messages
Todisplaythedateandtimeofanevent,youwouldplace‘%(asctime)s’inyourformatstring:
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
whichshouldprintsomethinglikethis:
2010-12-12 11:41:42,612 is when this event was logged.
Thedefaultformatfordate/timedisplay(shownabove)islikeISO8601orRFC3339. Ifyouneedmorecontrolover
theformattingofthedate/time,provideadatefmtargumenttobasicConfig,asinthisexample:
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p
,→')
logging.warning('is when this event was logged.')
whichwoulddisplaysomethinglikethis:
12/12/2010 11:46:36 AM is when this event was logged.
Theformatofthedatefmtargumentisthesameassupportedbytime.strftime().
1.7 Next Steps
Thatconcludesthebasictutorial. Itshouldbeenoughtogetyouupandrunningwithlogging. There’salotmorethat
theloggingpackageoffers,buttogetthebestoutofit,you’llneedtoinvestalittlemoreofyourtimeinreadingthe
followingsections. Ifyou’rereadyforthat,grabsomeofyourfavouritebeverageandcarryon.
Ifyourloggingneedsaresimple,thenusetheaboveexamplestoincorporateloggingintoyourownscripts,andifyou
runintoproblemsordon’tunderstandsomething,pleasepostaquestionintheHelpcategoryofthePythondiscussion
forumandyoushouldreceivehelpbeforetoolong.
Stillhere? Youcancarryonreadingthenextfewsections,whichprovideaslightlymoreadvanced/in-depthtutorial
thanthebasiconeabove. Afterthat,youcantakealookatthelogging-cookbook.
2 Advanced Logging Tutorial
Thelogginglibrarytakesamodularapproachandoffersseveralcategoriesofcomponents: loggers,handlers,filters,
andformatters.
• Loggersexposetheinterfacethatapplicationcodedirectlyuses.
• Handlerssendthelogrecords(createdbyloggers)totheappropriatedestination.
• Filtersprovideafinergrainedfacilityfordeterminingwhichlogrecordstooutput.
• Formattersspecifythelayoutoflogrecordsinthefinaloutput.
Logeventinformationispassedbetweenloggers,handlers,filtersandformattersinaLogRecordinstance.
LoggingisperformedbycallingmethodsoninstancesoftheLoggerclass(hereaftercalledloggers). Eachinstance
has a name, and they are conceptually arranged in a namespace hierarchy using dots (periods) as separators. For
example,aloggernamed‘scan’istheparentofloggers‘scan.text’,‘scan.html’and‘scan.pdf’. Loggernamescanbe
anythingyouwant,andindicatetheareaofanapplicationinwhichaloggedmessageoriginates.
Agoodconventiontousewhennamingloggersistouseamodule-levellogger,ineachmodulewhichuseslogging,
namedasfollows:
5

### 第6页

logger = logging.getLogger(__name__)
Thismeansthatloggernamestrackthepackage/modulehierarchy,andit’sintuitivelyobviouswhereeventsarelogged
justfromtheloggername.
The root of the hierarchy of loggers is called the root logger. That’s the logger used by the functions debug(),
info(),warning(),error()andcritical(),whichjustcallthesame-namedmethodoftherootlogger. The
functionsandthemethodshavethesamesignatures. Therootlogger’snameisprintedas‘root’intheloggedoutput.
It is, of course, possible to log messages to different destinations. Support is included in the package for writing
logmessagestofiles,HTTPGET/POSTlocations,emailviaSMTP,genericsockets,queues,orOS-specificlogging
mechanismssuchassyslogortheWindowsNTeventlog. Destinationsareservedbyhandlerclasses. Youcancreate
yourownlogdestinationclassifyouhavespecialrequirementsnotmetbyanyofthebuilt-inhandlerclasses.
By default, no destination is set for any logging messages. You can specify a destination (such as console or file)
by using basicConfig() as in the tutorial examples. If you call the functions debug(), info(), warning(),
error() and critical(), they will check to see if no destination is set; and if one is not set, they will set a
destination of the console (sys.stderr) and a default format for the displayed message before delegating to the
rootloggertodotheactualmessageoutput.
ThedefaultformatsetbybasicConfig()formessagesis:
severity:logger name:message
You can change this by passing a format string to basicConfig() with the format keyword argument. For all
optionsregardinghowaformatstringisconstructed,seeformatter-objects.
2.1 Logging Flow
Theflowoflogeventinformationinloggersandhandlersisillustratedinthefollowingdiagram.
6

### 第7页

2.2 Loggers
Loggerobjectshaveathreefoldjob. First,theyexposeseveralmethodstoapplicationcodesothatapplicationscan
logmessagesatruntime. Second,loggerobjectsdeterminewhichlogmessagestoactuponbaseduponseverity(the
defaultfilteringfacility)orfilterobjects. Third,loggerobjectspassalongrelevantlogmessagestoallinterestedlog
handlers.
Themostwidelyusedmethodsonloggerobjectsfallintotwocategories: configurationandmessagesending.
Thesearethemostcommonconfigurationmethods:
• Logger.setLevel()specifiesthelowest-severitylogmessagealoggerwillhandle,wheredebugisthelowest
built-in severitylevelandcriticalis thehighestbuilt-inseverity. Forexample, if theseveritylevelisINFO,
theloggerwillhandleonlyINFO,WARNING,ERROR,andCRITICALmessagesandwillignoreDEBUG
messages.
• Logger.addHandler()andLogger.removeHandler()addandremovehandlerobjectsfromthelogger
object. HandlersarecoveredinmoredetailinHandlers.
• Logger.addFilter()andLogger.removeFilter()addandremovefilterobjectsfromtheloggerob-
7

### 第8页

ject. Filtersarecoveredinmoredetailinfilter.
Youdon’tneedtoalwayscallthesemethodsoneveryloggeryoucreate. Seethelasttwoparagraphsinthissection.
Withtheloggerobjectconfigured,thefollowingmethodscreatelogmessages:
• Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), and Logger.
critical() all create log records with a message and a level that corresponds to their respective
method names. The message is actually a format string, which may contain the standard string substitution
syntax of %s, %d, %f, and so on. The rest of their arguments is a list of objects that correspond with the
substitutionfieldsinthemessage. Withregardto**kwargs,theloggingmethodscareonlyaboutakeyword
ofexc_infoanduseittodeterminewhethertologexceptioninformation.
• Logger.exception()createsalogmessagesimilartoLogger.error(). ThedifferenceisthatLogger.
exception()dumpsastacktracealongwithit. Callthismethodonlyfromanexceptionhandler.
• Logger.log()takesaloglevelasanexplicitargument. Thisisalittlemoreverboseforloggingmessages
thanusingtheloglevelconveniencemethodslistedabove,butthisishowtologatcustomloglevels.
getLogger() returns a reference to a logger instance with the specified name if it is provided, or root if not.
Thenamesareperiod-separatedhierarchicalstructures. MultiplecallstogetLogger()withthesamenamewill
return a reference to the same logger object. Loggers that are further down in the hierarchical list are children of
loggers higher up in the list. For example, given a logger with a name of foo, loggers with names of foo.bar,
foo.bar.baz,andfoo.bamarealldescendantsoffoo.
Loggers have a concept of effective level. If a level is not explicitly set on a logger, the level of its parent is used
insteadasitseffectivelevel. Iftheparenthasnoexplicitlevelset,itsparentisexamined,andsoon-allancestorsare
searcheduntilanexplicitlysetlevelisfound. Therootloggeralwayshasanexplicitlevelset(WARNINGbydefault).
Whendecidingwhethertoprocessanevent,theeffectiveleveloftheloggerisusedtodeterminewhethertheevent
ispassedtothelogger’shandlers.
Child loggers propagate messages up to the handlers associated with their ancestor loggers. Because of this, it is
unnecessary to define and configure handlers for all the loggers an application uses. It is sufficient to configure
handlersforatop-levelloggerandcreatechildloggersasneeded. (Youcan,however,turnoffpropagationbysetting
thepropagateattributeofaloggertoFalse.)
2.3 Handlers
Handlerobjectsareresponsiblefordispatchingtheappropriatelogmessages(basedonthelogmessages’severity)
tothehandler’sspecifieddestination. Loggerobjectscanaddzeroormorehandlerobjectstothemselveswithan
addHandler() method. As an example scenario, an application may want to send all log messages to a log file,
alllogmessagesoferrororhighertostdout,andallmessagesofcriticaltoanemailaddress. Thisscenariorequires
threeindividualhandlerswhereeachhandlerisresponsibleforsendingmessagesofaspecificseveritytoaspecific
location.
The standard library includes quite a few handler types (see Useful Handlers); the tutorials use mainly
StreamHandlerandFileHandlerinitsexamples.
Thereareveryfewmethodsina handlerforapplicationdeveloperstoconcernthemselveswith. Theonlyhandler
methodsthatseemrelevantforapplicationdeveloperswhoareusingthebuilt-inhandlerobjects(thatis,notcreating
customhandlers)arethefollowingconfigurationmethods:
• The setLevel() method, just as in logger objects, specifies the lowest severity that will be dispatched to
theappropriatedestination. WhyaretheretwosetLevel()methods? Thelevelsetintheloggerdetermines
whichseverityofmessagesitwillpasstoitshandlers. Thelevelsetineachhandlerdetermineswhichmessages
thathandlerwillsendon.
• setFormatter()selectsaFormatterobjectforthishandlertouse.
• addFilter()andremoveFilter()respectivelyconfigureanddeconfigurefilterobjectsonhandlers.
ApplicationcodeshouldnotdirectlyinstantiateanduseinstancesofHandler. Instead,theHandlerclassisabase
classthatdefinestheinterfacethatallhandlersshouldhaveandestablishessomedefaultbehaviorthatchildclasses
canuse(oroverride).
8

### 第9页

2.4 Formatters
Formatterobjectsconfigurethefinalorder,structure,andcontentsofthelogmessage. Unlikethebaselogging.
Handlerclass,applicationcodemayinstantiateformatterclasses,althoughyoucouldlikelysubclasstheformatter
ifyourapplicationneedsspecialbehavior. Theconstructortakesthreeoptionalarguments–amessageformatstring,
adateformatstringandastyleindicator.
logging.Formatter.__init__(fmt=None,datefmt=None,style=’%’)
Ifthereisnomessageformatstring,thedefaultistousetherawmessage. Ifthereisnodateformatstring,thedefault
dateformatis:
%Y-%m-%d %H:%M:%S
withthemillisecondstackedonattheend. Thestyleisoneof'%','{',or'$'. Ifoneoftheseisnotspecified,
then'%'willbeused.
Ifthestyleis'%',themessageformatstringuses%(<dictionary key>)sstyledstringsubstitution;thepossible
keysaredocumentedinlogrecord-attributes. Ifthestyleis'{',themessageformatstringisassumedtobecompatible
with str.format() (using keyword arguments), while if the style is '$' then the message format string should
conformtowhatisexpectedbystring.Template.substitute().
Changedinversion3.2: Addedthestyleparameter.
Thefollowingmessageformatstringwilllogthetimeinahuman-readableformat,theseverityofthemessage,and
thecontentsofthemessage,inthatorder:
'%(asctime)s - %(levelname)s - %(message)s'
Formattersuseauser-configurablefunctiontoconvertthecreationtimeofarecordtoatuple. Bydefault, time.
localtime()isused;tochangethisforaparticularformatterinstance,settheconverterattributeoftheinstance
toafunctionwiththesamesignatureastime.localtime()ortime.gmtime(). Tochangeitforallformatters,
forexampleifyouwantallloggingtimestobeshowninGMT,settheconverterattributeintheFormatterclass
(totime.gmtimeforGMTdisplay).
2.5 Configuring Logging
Programmerscanconfigurelogginginthreeways:
1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods
listedabove.
2. CreatingaloggingconfigfileandreadingitusingthefileConfig()function.
3. CreatingadictionaryofconfigurationinformationandpassingittothedictConfig()function.
Forthereferencedocumentationonthelasttwooptions,seelogging-config-api. Thefollowingexampleconfiguresa
verysimplelogger,aconsolehandler,andasimpleformatterusingPythoncode:
import logging
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s
,→')
(continuesonnextpage)
9

### 第10页

(continuedfrompreviouspage)
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
Runningthismodulefromthecommandlineproducesthefollowingoutput:
$ python simple_logging_module.py
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
2005-03-19 15:10:26,620 - simple_example - INFO - info message
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
2005-03-19 15:10:26,697 - simple_example - ERROR - error message
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
ThefollowingPythonmodulecreatesalogger,handler,andformatternearlyidenticaltothoseintheexamplelisted
above,withtheonlydifferencebeingthenamesoftheobjects:
import logging
import logging.config
logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('simpleExample')
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
Hereisthelogging.conffile:
[loggers]
keys=root,simpleExample
[handlers]
keys=consoleHandler
[formatters]
keys=simpleFormatter
[logger_root]
level=DEBUG
handlers=consoleHandler
[logger_simpleExample]
level=DEBUG
(continuesonnextpage)
10

### 第11页

(continuedfrompreviouspage)
handlers=consoleHandler
qualname=simpleExample
propagate=0
[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)
[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
Theoutputisnearlyidenticaltothatofthenon-config-file-basedexample:
$ python simple_logging_config.py
2005-03-19 15:38:55,977 - simpleExample - DEBUG - debug message
2005-03-19 15:38:55,979 - simpleExample - INFO - info message
2005-03-19 15:38:56,054 - simpleExample - WARNING - warn message
2005-03-19 15:38:56,055 - simpleExample - ERROR - error message
2005-03-19 15:38:56,130 - simpleExample - CRITICAL - critical message
YoucanseethattheconfigfileapproachhasafewadvantagesoverthePythoncodeapproach,mainlyseparationof
configurationandcodeandtheabilityofnoncoderstoeasilymodifytheloggingproperties.
(cid:193) Warning
The fileConfig() function takes a default parameter, disable_existing_loggers, which defaults to
True for reasons of backward compatibility. This may or may not be what you want, since it will cause any
non-rootloggersexistingbeforethefileConfig()calltobedisabledunlessthey(oranancestor)areexplic-
itlynamedintheconfiguration. Pleaserefertothereferencedocumentationformoreinformation,andspecify
Falseforthisparameterifyouwish.
The dictionary passed to dictConfig() can also specify a Boolean value with key
disable_existing_loggers, which if not specified explicitly in the dictionary also defaults to being
interpretedasTrue. Thisleadstothelogger-disablingbehaviourdescribedabove,whichmaynotbewhatyou
want-inwhichcase,providethekeyexplicitlywithavalueofFalse.
Note that the class names referenced in config files need to be either relative to the logging module, or absolute
valueswhichcanberesolvedusingnormalimportmechanisms. Thus,youcoulduseeitherWatchedFileHandler
(relativetotheloggingmodule)ormypackage.mymodule.MyHandler(foraclassdefinedinpackagemypackage
andmodulemymodule,wheremypackageisavailableonthePythonimportpath).
In Python 3.2, a new means of configuring logging has been introduced, using dictionaries to hold configuration
information. This provides a superset of the functionality of the config-file-based approach outlined above, and is
therecommendedconfigurationmethodfornewapplicationsanddeployments. BecauseaPythondictionaryisused
toholdconfigurationinformation,andsinceyoucanpopulatethatdictionaryusingdifferentmeans,youhavemore
optionsforconfiguration. Forexample, youcanusea configurationfileinJSON format, or, ifyouhaveaccessto
YAMLprocessingfunctionality,afileinYAMLformat,topopulatetheconfigurationdictionary. Or,ofcourse,you
canconstructthedictionaryinPythoncode,receiveitinpickledformoverasocket,orusewhateverapproachmakes
senseforyourapplication.
Here’sanexampleofthesameconfigurationasabove,inYAMLformatforthenewdictionary-basedapproach:
version: 1
formatters:
simple:
(continuesonnextpage)
11

### 第12页

(continuedfrompreviouspage)
format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
console:
class: logging.StreamHandler
level: DEBUG
formatter: simple
stream: ext://sys.stdout
loggers:
simpleExample:
level: DEBUG
handlers: [console]
propagate: no
root:
level: DEBUG
handlers: [console]
Formoreinformationaboutloggingusingadictionary,seelogging-config-api.
2.6 What happens if no configuration is provided
Ifnologgingconfigurationisprovided,itispossibletohaveasituationwherealoggingeventneedstobeoutput,but
nohandlerscanbefoundtooutputtheevent.
Theeventisoutputusinga‘handleroflastresort’, storedinlastResort. Thisinternalhandlerisnotassociated
withanylogger,andactslikeaStreamHandlerwhichwritestheeventdescriptionmessagetothecurrentvalueof
sys.stderr(thereforerespectinganyredirectionswhichmaybeineffect). Noformattingisdoneonthemessage
-justthebareeventdescriptionmessageisprinted. Thehandler’slevelissettoWARNING,soalleventsatthisand
greaterseveritieswillbeoutput.
Changedinversion3.2: ForversionsofPythonpriorto3.2,thebehaviourisasfollows:
• IfraiseExceptionsisFalse(productionmode),theeventissilentlydropped.
• IfraiseExceptionsisTrue(developmentmode),amessage‘NohandlerscouldbefoundforloggerX.Y.Z’
isprintedonce.
Toobtainthepre-3.2behaviour,lastResortcanbesettoNone.
2.7 Configuring Logging for a Library
When developing a library which uses logging, you should take care to document how the library uses logging -
forexample,thenamesofloggersused. Someconsiderationalsoneedstobegiventoitsloggingconfiguration. If
theusingapplicationdoesnotuselogging,andlibrarycodemakesloggingcalls,then(asdescribedintheprevious
section)eventsofseverityWARNINGandgreaterwillbeprintedtosys.stderr. Thisisregardedasthebestdefault
behaviour.
Ifforsomereasonyoudon’twantthesemessagesprintedintheabsenceofanyloggingconfiguration,youcanattach
ado-nothinghandlertothetop-levelloggerforyourlibrary. Thisavoidsthemessagebeingprinted,sinceahandler
willalwaysbefoundforthelibrary’sevents: itjustdoesn’tproduceanyoutput. Ifthelibraryuserconfigureslogging
forapplicationuse,presumablythatconfigurationwilladdsomehandlers,andiflevelsaresuitablyconfiguredthen
loggingcallsmadeinlibrarycodewillsendoutputtothosehandlers,asnormal.
A do-nothing handler is included in the logging package: NullHandler (since Python 3.1). An instance of this
handlercouldbeaddedtothetop-levelloggeroftheloggingnamespaceusedbythelibrary(if youwanttoprevent
yourlibrary’sloggedeventsbeingoutputtosys.stderrintheabsenceofloggingconfiguration). Ifallloggingby
alibraryfooisdoneusingloggerswithnamesmatching‘foo.x’,‘foo.x.y’,etc. thenthecode:
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())
12

### 第13页

shouldhavethedesiredeffect. Ifanorganisationproducesanumberoflibraries,thentheloggernamespecifiedcan
be‘orgname.foo’ratherthanjust‘foo’.
(cid:174) Note
Itisstronglyadvisedthatyoudonotlogtotherootloggerinyourlibrary. Instead,usealoggerwithauniqueand
easilyidentifiablename, suchasthe__name__foryourlibrary’stop-levelpackageormodule. Loggingtothe
rootloggerwillmakeitdifficultorimpossiblefortheapplicationdevelopertoconfiguretheloggingverbosityor
handlersofyourlibraryastheywish.
(cid:174) Note
ItisstronglyadvisedthatyoudonotaddanyhandlersotherthanNullHandlertoyourlibrary’sloggers. Thisis
becausetheconfigurationofhandlersistheprerogativeoftheapplicationdeveloperwhousesyourlibrary. The
applicationdeveloperknowstheirtargetaudienceandwhathandlersaremostappropriatefortheirapplication:
ifyouaddhandlers‘underthehood’,youmightwellinterferewiththeirabilitytocarryoutunittestsanddeliver
logswhichsuittheirrequirements.
3 Logging Levels
Thenumericvaluesoflogginglevelsaregiveninthefollowingtable. Theseareprimarilyofinterestifyouwantto
defineyourownlevels,andneedthemtohavespecificvaluesrelativetothepredefinedlevels. Ifyoudefinealevel
withthesamenumericvalue,itoverwritesthepredefinedvalue;thepredefinednameislost.
Level Numericvalue
CRITICAL 50
ERROR 40
WARNING 30
INFO 20
DEBUG 10
NOTSET 0
Levels can also be associated with loggers, being set either by the developer or through loading a saved logging
configuration. Whenaloggingmethodiscalledonalogger,theloggercomparesitsownlevelwiththelevelassociated
withthemethodcall. Ifthelogger’slevelishigherthanthemethodcall’s,nologgingmessageisactuallygenerated.
Thisisthebasicmechanismcontrollingtheverbosityofloggingoutput.
LoggingmessagesareencodedasinstancesoftheLogRecordclass. Whenaloggerdecidestoactuallyloganevent,
aLogRecordinstanceiscreatedfromtheloggingmessage.
Logging messages are subjected to a dispatch mechanism through the use of handlers, which are instances of
subclasses of the Handler class. Handlers are responsible for ensuring that a logged message (in the form of a
LogRecord) ends up in a particular location (or set of locations) which is useful for the target audience for that
message(suchasendusers,supportdeskstaff,systemadministrators,developers). HandlersarepassedLogRecord
instancesintendedforparticulardestinations. Eachloggercanhavezero,oneormorehandlersassociatedwithit(via
theaddHandler()methodofLogger). Inadditiontoanyhandlersdirectlyassociatedwithalogger,allhandlers
associatedwithallancestorsoftheloggerarecalledtodispatchthemessage(unlessthepropagateflagforaloggeris
settoafalsevalue,atwhichpointthepassingtoancestorhandlersstops).
Justasforloggers,handlerscanhavelevelsassociatedwiththem. Ahandler’slevelactsasafilterinthesameway
asalogger’sleveldoes. Ifahandlerdecidestoactuallydispatchanevent, theemit()methodisusedtosendthe
messagetoitsdestination. Mostuser-definedsubclassesofHandlerwillneedtooverridethisemit().
13

| Level | Numericvalue |
| --- | --- |
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |

### 第14页

3.1 Custom Levels
Definingyourownlevelsispossible,butshouldnotbenecessary,astheexistinglevelshavebeenchosenonthebasis
ofpracticalexperience. However,ifyouareconvincedthatyouneedcustomlevels,greatcareshouldbeexercised
when doing this, and it is possibly a very bad idea to define custom levels if you are developing a library. That’s
becauseifmultiplelibraryauthorsalldefinetheirowncustomlevels,thereisachancethattheloggingoutputfrom
such multiple libraries used together will be difficult for the using developer to control and/or interpret, because a
givennumericvaluemightmeandifferentthingsfordifferentlibraries.
4 Useful Handlers
InadditiontothebaseHandlerclass,manyusefulsubclassesareprovided:
1. StreamHandlerinstancessendmessagestostreams(file-likeobjects).
2. FileHandlerinstancessendmessagestodiskfiles.
3. BaseRotatingHandleristhebaseclassforhandlersthatrotatelogfilesatacertainpoint. Itisnotmeant
tobeinstantiateddirectly. Instead,useRotatingFileHandlerorTimedRotatingFileHandler.
4. RotatingFileHandlerinstancessendmessagestodiskfiles,withsupportformaximumlogfilesizesand
logfilerotation.
5. TimedRotatingFileHandler instances send messages to disk files, rotating the log file at certain timed
intervals.
6. SocketHandlerinstancessendmessagestoTCP/IPsockets. Since3.4,Unixdomainsocketsarealsosup-
ported.
7. DatagramHandlerinstancessendmessagestoUDPsockets. Since3.4,Unixdomainsocketsarealsosup-
ported.
8. SMTPHandlerinstancessendmessagestoadesignatedemailaddress.
9. SysLogHandlerinstancessendmessagestoaUnixsyslogdaemon,possiblyonaremotemachine.
10. NTEventLogHandlerinstancessendmessagestoaWindowsNT/2000/XPeventlog.
11. MemoryHandlerinstancessendmessagestoabufferinmemory,whichisflushedwheneverspecificcriteria
aremet.
12. HTTPHandlerinstancessendmessagestoanHTTPserverusingeitherGETorPOSTsemantics.
13. WatchedFileHandler instances watchthefiletheyareloggingto. If thefile changes, itisclosedandre-
openedusingthefilename. ThishandlerisonlyusefulonUnix-likesystems;Windowsdoesnotsupportthe
underlyingmechanismused.
14. QueueHandler instances send messages to a queue, such as those implemented in the queue or
multiprocessingmodules.
15. NullHandlerinstancesdonothingwitherrormessages. Theyareusedbylibrarydeveloperswhowanttouse
logging,butwanttoavoidthe‘NohandlerscouldbefoundforloggerXXX’messagewhichcanbedisplayedif
thelibraryuserhasnotconfiguredlogging. SeeConfiguringLoggingforaLibraryformoreinformation.
Addedinversion3.1: TheNullHandlerclass.
Addedinversion3.2: TheQueueHandlerclass.
TheNullHandler,StreamHandlerandFileHandlerclassesaredefinedinthecoreloggingpackage. Theother
handlersaredefinedinasub-module,logging.handlers. (Thereisalsoanothersub-module,logging.config,
forconfigurationfunctionality.)
LoggedmessagesareformattedforpresentationthroughinstancesoftheFormatterclass. Theyareinitializedwith
aformatstringsuitableforusewiththe%operatorandadictionary.
Forformattingmultiplemessagesinabatch, instancesofBufferingFormattercanbeused. Inadditiontothe
formatstring(whichisappliedtoeachmessageinthebatch),thereisprovisionforheaderandtrailerformatstrings.
14

### 第15页

Whenfilteringbasedonloggerleveland/orhandlerlevelisnotenough,instancesofFiltercanbeaddedtoboth
LoggerandHandlerinstances(throughtheiraddFilter()method). Beforedecidingtoprocessamessagefur-
ther,bothloggersandhandlersconsultalltheirfiltersforpermission. Ifanyfilterreturnsafalsevalue,themessage
isnotprocessedfurther.
ThebasicFilterfunctionalityallowsfilteringbyspecificloggername. Ifthisfeatureisused,messagessenttothe
namedloggeranditschildrenareallowedthroughthefilter,andallothersdropped.
5 Exceptions raised during logging
Theloggingpackageisdesignedtoswallowexceptionswhichoccurwhilelogginginproduction. Thisissothaterrors
whichoccurwhilehandlingloggingevents-suchasloggingmisconfiguration,networkorothersimilarerrors-do
notcausetheapplicationusingloggingtoterminateprematurely.
SystemExitandKeyboardInterruptexceptionsareneverswallowed. Otherexceptionswhichoccurduringthe
emit()methodofaHandlersubclassarepassedtoitshandleError()method.
The default implementation of handleError() in Handler checks to see if a module-level variable,
raiseExceptions,isset. Ifset,atracebackisprintedtosys.stderr. Ifnotset,theexceptionisswallowed.
(cid:174) Note
The default value of raiseExceptions is True. This is because during development, you typically want to
benotifiedofanyexceptionsthatoccur. It’sadvisedthatyousetraiseExceptionstoFalseforproduction
usage.
6 Using arbitrary objects as messages
In the preceding sections and examples, it has been assumed that the message passed when logging the event is a
string. However,thisisnottheonlypossibility. Youcanpassanarbitraryobjectasamessage,andits__str__()
methodwillbecalledwhentheloggingsystemneedstoconvertittoastringrepresentation. Infact,ifyouwantto,
youcanavoidcomputingastringrepresentationaltogether-forexample, theSocketHandleremitsaneventby
picklingitandsendingitoverthewire.
7 Optimization
Formattingofmessageargumentsisdeferreduntilitcannotbeavoided. However,computingtheargumentspassed
totheloggingmethodcanalsobeexpensive,andyoumaywanttoavoiddoingitiftheloggerwilljustthrowaway
your event. To decide what to do, you can call the isEnabledFor() method which takes a level argument and
returnstrueiftheeventwouldbecreatedbytheLoggerforthatlevelofcall. Youcanwritecodelikethis:
if logger.isEnabledFor(logging.DEBUG):
logger.debug('Message with %s, %s', expensive_func1(),
expensive_func2())
so that if the logger’s threshold is set above DEBUG, the calls to expensive_func1 and expensive_func2 are
nevermade.
(cid:174) Note
Insomecases, isEnabledFor()canitselfbemoreexpensivethanyou’dlike(e.g. fordeeplynestedloggers
whereanexplicitlevelisonlysethighupintheloggerhierarchy). Insuchcases(orifyouwanttoavoidcallinga
methodintightloops),youcancachetheresultofacalltoisEnabledFor()inalocalorinstancevariable,and
usethatinsteadofcallingthemethodeachtime. Suchacachedvaluewouldonlyneedtoberecomputedwhen
theloggingconfigurationchangesdynamicallywhiletheapplicationisrunning(whichisnotallthatcommon).
15

### 第16页

Thereareotheroptimizationswhichcanbemadeforspecificapplicationswhichneedmoreprecisecontroloverwhat
logginginformationiscollected. Here’salistofthingsyoucandotoavoidprocessingduringloggingwhichyoudon’t
need:
Whatyoudon’twanttocollect Howtoavoidcollectingit
Information about where calls Setlogging._srcfiletoNone. Thisavoidscallingsys._getframe(),
weremadefrom. whichmayhelptospeedupyourcodeinenvironmentslikePyPy(whichcan’t
speedupcodethatusessys._getframe()).
Threadinginformation. Setlogging.logThreadstoFalse.
Current process ID (os. Setlogging.logProcessestoFalse.
getpid())
Current process name when us- Setlogging.logMultiprocessingtoFalse.
ingmultiprocessingtoman-
agemultipleprocesses.
Current asyncio.Task name Setlogging.logAsyncioTaskstoFalse.
whenusingasyncio.
Alsonotethatthecoreloggingmoduleonlyincludesthebasichandlers. Ifyoudon’timportlogging.handlers
andlogging.config,theywon’ttakeupanymemory.
8 Other resources
(cid:181) Seealso
Modulelogging
APIreferencefortheloggingmodule.
Modulelogging.config
ConfigurationAPIfortheloggingmodule.
Modulelogging.handlers
Usefulhandlersincludedwiththeloggingmodule.
Aloggingcookbook
16

| Whatyoudon’twanttocollect | Howtoavoidcollectingit |
| --- | --- |
| Information about where calls
weremadefrom. | Setlogging._srcfiletoNone. Thisavoidscallingsys._getframe(),
whichmayhelptospeedupyourcodeinenvironmentslikePyPy(whichcan’t
speedupcodethatusessys._getframe()). |
| Threadinginformation. | Setlogging.logThreadstoFalse. |
| Current process ID (os.
getpid()) | Setlogging.logProcessestoFalse. |
| Current process name when us-
ingmultiprocessingtoman-
agemultipleprocesses. | Setlogging.logMultiprocessingtoFalse. |
| Current asyncio.Task name
whenusingasyncio. | Setlogging.logAsyncioTaskstoFalse. |


| (cid:181) Seealso |
| --- |
| Modulelogging
APIreferencefortheloggingmodule.
Modulelogging.config
ConfigurationAPIfortheloggingmodule.
Modulelogging.handlers
Usefulhandlersincludedwiththeloggingmodule.
Aloggingcookbook |

### 第17页

Index
Non-alphabetical
__init__()(logging.logging.Formattermethod),9
R
RFC
RFC 3339,5
17

