### 第1页

Curses Programming with Python
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Whatiscurses? 1
1.1 ThePythoncursesmodule. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 Startingandendingacursesapplication 2
3 WindowsandPads 3
4 DisplayingText 4
4.1 AttributesandColor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
5 UserInput 6
6 ForMoreInformation 7
Author
A.M.Kuchling,EricS.Raymond
Release
2.04
Abstract
Thisdocumentdescribeshowtousethecursesextensionmoduletocontroltext-modedisplays.
1 What is curses?
Thecurseslibrarysuppliesaterminal-independentscreen-paintingandkeyboard-handlingfacilityfortext-basedter-
minals;suchterminalsincludeVT100s,theLinuxconsole,andthesimulatedterminalprovidedbyvariousprograms.
Displayterminalssupportvariouscontrolcodestoperformcommonoperationssuchasmovingthecursor,scrolling
thescreen,anderasingareas. Differentterminalsusewidelydifferingcodes,andoftenhavetheirownminorquirks.
Inaworldofgraphicaldisplays, onemightask“whybother”? It’struethatcharacter-celldisplayterminalsarean
obsolete technology, but there are niches in which being able to do fancy things with them are still valuable. One
nicheisonsmall-footprintorembeddedUnixesthatdon’trunanXserver. AnotheristoolssuchasOSinstallersand
kernelconfiguratorsthatmayhavetorunbeforeanygraphicalsupportisavailable.
1

### 第2页

The curses library provides fairly basic functionality, providing the programmer with an abstraction of a display
containingmultiplenon-overlappingwindowsoftext. Thecontentsofawindowcanbechangedinvariousways—
addingtext,erasingit,changingitsappearance—andthecurseslibrarywillfigureoutwhatcontrolcodesneedtobe
senttotheterminaltoproducetherightoutput. cursesdoesn’tprovidemanyuser-interfaceconceptssuchasbuttons,
checkboxes,ordialogs;ifyouneedsuchfeatures,considerauserinterfacelibrarysuchasUrwid.
ThecurseslibrarywasoriginallywrittenforBSDUnix;thelaterSystemVversionsofUnixfromAT&Taddedmany
enhancementsandnewfunctions. BSDcursesisnolongermaintained,havingbeenreplacedbyncurses,whichisan
open-sourceimplementationoftheAT&Tinterface. Ifyou’reusinganopen-sourceUnixsuchasLinuxorFreeBSD,
yoursystemalmostcertainlyusesncurses. SincemostcurrentcommercialUnixversionsarebasedonSystemVcode,
allthefunctionsdescribedherewillprobablybeavailable. Theolderversionsofcursescarriedbysomeproprietary
Unixesmaynotsupporteverything,though.
TheWindowsversionofPythondoesn’tincludethecursesmodule. AportedversioncalledUniCursesisavailable.
1.1 The Python curses module
The Python module is a fairly simple wrapper over the C functions provided by curses; if you’re already familiar
withcursesprogramminginC,it’sreallyeasytotransferthatknowledgetoPython. Thebiggestdifferenceisthat
thePythoninterfacemakesthingssimplerbymergingdifferentCfunctionssuchasaddstr(),mvaddstr(),and
mvwaddstr()intoasingleaddstr()method. You’llseethiscoveredinmoredetaillater.
ThisHOWTOisanintroductiontowritingtext-modeprogramswithcursesandPython. Itdoesn’tattempttobea
completeguidetothecursesAPI;forthat,seethePythonlibraryguide’ssectiononncurses,andtheCmanualpages
forncurses. Itwill,however,giveyouthebasicideas.
2 Starting and ending a curses application
Before doing anything, curses must be initialized. This is done by calling the initscr() function, which will
determinetheterminaltype,sendanyrequiredsetupcodestotheterminal,andcreatevariousinternaldatastructures.
Ifsuccessful,initscr()returnsawindowobjectrepresentingtheentirescreen;thisisusuallycalledstdscrafter
thenameofthecorrespondingCvariable.
import curses
stdscr = curses.initscr()
Usuallycursesapplicationsturnoffautomaticechoingofkeystothescreen,inordertobeabletoreadkeysandonly
displaythemundercertaincircumstances. Thisrequirescallingthenoecho()function.
curses.noecho()
Applicationswillalsocommonlyneedtoreacttokeysinstantly,withoutrequiringtheEnterkeytobepressed;this
iscalledcbreakmode,asopposedtotheusualbufferedinputmode.
curses.cbreak()
Terminals usually return special keys, such as the cursor keys or navigation keys such as Page Up and Home, as
a multibyte escape sequence. While you could write your application to expect such sequences and process them
accordingly,cursescandoitforyou,returningaspecialvaluesuchascurses.KEY_LEFT.Togetcursestodothe
job,you’llhavetoenablekeypadmode.
stdscr.keypad(True)
Terminatingacursesapplicationismucheasierthanstartingone. You’llneedtocall:
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
2

### 第3页

toreversethecurses-friendlyterminalsettings. Thencalltheendwin()functiontorestoretheterminaltoitsoriginal
operatingmode.
curses.endwin()
A common problem when debugging a curses application is to get your terminal messed up when the application
dieswithoutrestoringtheterminaltoitspreviousstate. InPythonthiscommonlyhappenswhenyourcodeisbuggy
andraisesanuncaughtexception. Keysarenolongerechoedtothescreenwhenyoutypethem,forexample,which
makesusingtheshelldifficult.
InPythonyoucanavoidthesecomplicationsandmakedebuggingmucheasierbyimportingthecurses.wrapper()
functionandusingitlikethis:
from curses import wrapper
def main(stdscr):
# Clear screen
stdscr.clear()
# This raises ZeroDivisionError when i == 10.
for i in range(0, 11):
v = i-10
stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
stdscr.refresh()
stdscr.getkey()
wrapper(main)
Thewrapper()functiontakesacallableobjectanddoestheinitializationsdescribedabove,alsoinitializingcolors
if color support is present. wrapper() then runs your provided callable. Once the callable returns, wrapper()
willrestoretheoriginalstateoftheterminal. Thecallableiscalledinsideatry…exceptthatcatchesexceptions,
restoresthestateoftheterminal,andthenre-raisestheexception. Thereforeyourterminalwon’tbeleftinafunny
stateonexceptionandyou’llbeabletoreadtheexception’smessageandtraceback.
3 Windows and Pads
Windows are the basic abstraction in curses. A window object represents a rectangular area of the screen, and
supportsmethodstodisplaytext,eraseit,allowtheusertoinputstrings,andsoforth.
The stdscr object returned by the initscr() function is a window object that covers the entire screen. Many
programsmayneedonlythissinglewindow,butyoumightwishtodividethescreenintosmallerwindows,inorder
toredraworclearthemseparately. Thenewwin()functioncreatesanewwindowofagivensize,returningthenew
windowobject.
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
Notethatthecoordinatesystemusedincursesisunusual. Coordinatesarealwayspassedintheordery,x, andthe
top-leftcornerofawindowiscoordinate(0,0). Thisbreaksthenormalconventionforhandlingcoordinateswhere
thexcoordinatecomesfirst. Thisisanunfortunatedifferencefrommostothercomputerapplications,butit’sbeen
partofcursessinceitwasfirstwritten,andit’stoolatetochangethingsnow.
Yourapplicationcandeterminethesizeofthescreenbyusingthecurses.LINESandcurses.COLSvariablesto
obtaintheyandxsizes. Legalcoordinateswillthenextendfrom(0,0)to(curses.LINES - 1, curses.COLS
- 1).
Whenyoucallamethodtodisplayorerasetext,theeffectdoesn’timmediatelyshowuponthedisplay. Insteadyou
mustcalltherefresh()methodofwindowobjectstoupdatethescreen.
3

### 第4页

Thisisbecausecurseswasoriginallywrittenwithslow300-baudterminalconnectionsinmind;withtheseterminals,
minimizingthetimerequiredtoredrawthescreenwasveryimportant. Insteadcursesaccumulateschangestothe
screen and displays them in the most efficient manner when you call refresh(). For example, if your program
displayssometextinawindowandthenclearsthewindow,there’snoneedtosendtheoriginaltextbecausethey’re
nevervisible.
Inpractice, explicitlytellingcursestoredrawawindowdoesn’treallycomplicateprogrammingwithcursesmuch.
Mostprogramsgointoaflurryofactivity,andthenpausewaitingforakeypressorsomeotheractiononthepartof
theuser. Allyouhavetodoistobesurethatthescreenhasbeenredrawnbeforepausingtowaitforuserinput,by
firstcallingstdscr.refresh()ortherefresh()methodofsomeotherrelevantwindow.
A pad is a special case of a window; it can be larger than the actual display screen, and only a portion of the pad
displayedatatime. Creatingapadrequiresthepad’sheightandwidth, whilerefreshingapadrequiresgivingthe
coordinatesoftheon-screenareawhereasubsectionofthepadwillbedisplayed.
pad = curses.newpad(100, 100)
# These loops fill the pad with letters; addch() is
# explained in the next section
for y in range(0, 99):
for x in range(0, 99):
pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
# Displays a section of the pad in the middle of the screen.
# (0,0) : coordinate of upper-left corner of pad area to display.
# (5,5) : coordinate of upper-left corner of window area to be filled
# with pad content.
# (20, 75) : coordinate of lower-right corner of window area to be
# : filled with pad content.
pad.refresh( 0,0, 5,5, 20,75)
The refresh() call displays a section of the pad in the rectangle extending from coordinate (5,5) to coordinate
(20,75) on the screen; the upper left corner of the displayed section is coordinate (0,0) on the pad. Beyond that
difference,padsareexactlylikeordinarywindowsandsupportthesamemethods.
If you have multiple windows and pads on screen there is a more efficient way to update the screen and prevent
annoyingscreenflickeraseachpartofthescreengetsupdated. refresh()actuallydoestwothings:
1) Callsthe noutrefresh() methodofeachwindowtoupdatean underlyingdatastructurerepresentingthe
desiredstateofthescreen.
2) Callsthefunctiondoupdate()functiontochangethephysicalscreentomatchthedesiredstaterecordedin
thedatastructure.
Instead you can call noutrefresh() on a number of windows to update the data structure, and then call
doupdate()toupdatethescreen.
4 Displaying Text
FromaCprogrammer’spointofview,cursesmaysometimeslooklikeatwistymazeoffunctions,allsubtlydifferent.
Forexample,addstr()displaysastringatthecurrentcursorlocationinthestdscrwindow,whilemvaddstr()
moves to a given y,x coordinate first before displaying the string. waddstr() is just like addstr(), but allows
specifyingawindowtouseinsteadofusingstdscrbydefault. mvwaddstr()allowsspecifyingbothawindowand
acoordinate.
FortunatelythePythoninterfacehidesallthesedetails. stdscrisawindowobjectlikeanyother,andmethodssuch
asaddstr()acceptmultipleargumentforms. Usuallytherearefourdifferentforms.
4

### 第5页

Form Description
strorch Displaythestringstrorcharacterchatthecurrentposition
strorch,attr Displaythestringstrorcharacterch,usingattributeattratthecurrentposition
y,x,strorch Movetopositiony,xwithinthewindow,anddisplaystrorch
y,x,strorch,attr Movetopositiony,xwithinthewindow,anddisplaystrorch,usingattributeattr
Attributesallowdisplayingtextinhighlightedformssuchasboldface,underline,reversecode,orincolor. They’llbe
explainedinmoredetailinthenextsubsection.
Theaddstr()methodtakesaPythonstringorbytestringasthevaluetobedisplayed. Thecontentsofbytestrings
aresenttotheterminalas-is. Stringsareencodedtobytesusingthevalueofthewindow’sencodingattribute;this
defaultstothedefaultsystemencodingasreturnedbylocale.getencoding().
The addch() methods take a character, which can be either a string of length 1, a bytestring of length 1, or an
integer.
Constants are provided for extension characters; these constants are integers greater than 255. For example,
ACS_PLMINUSisa+/-symbol,andACS_ULCORNERistheupperleftcornerofabox(handyfordrawingborders).
YoucanalsousetheappropriateUnicodecharacter.
Windows remember where the cursor was left after the last operation, so if you leave out the y,x coordinates, the
string or character will be displayed wherever the last operation left off. You can also move the cursor with the
move(y,x) method. Because some terminals always display a flashing cursor, you may want to ensure that the
cursorispositionedinsomelocationwhereitwon’tbedistracting;itcanbeconfusingtohavethecursorblinkingat
someapparentlyrandomlocation.
Ifyourapplicationdoesn’tneedablinkingcursoratall,youcancallcurs_set(False)tomakeitinvisible. For
compatibility with older curses versions, there’s a leaveok(bool) function that’s a synonym for curs_set().
Whenboolistrue,thecurseslibrarywillattempttosuppresstheflashingcursor,andyouwon’tneedtoworryabout
leavingitinoddlocations.
4.1 Attributes and Color
Characterscanbedisplayedindifferentways. Statuslinesinatext-basedapplicationarecommonlyshowninreverse
video,oratextviewermayneedtohighlightcertainwords. cursessupportsthisbyallowingyoutospecifyanattribute
foreachcellonthescreen.
Anattributeisaninteger,eachbitrepresentingadifferentattribute. Youcantrytodisplaytextwithmultipleattribute
bitsset,butcursesdoesn’tguaranteethatallthepossiblecombinationsareavailable,orthatthey’reallvisuallydistinct.
Thatdependsontheabilityoftheterminalbeingused,soit’ssafesttosticktothemostcommonlyavailableattributes,
listedhere.
Attribute Description
A_BLINK Blinkingtext
A_BOLD Extrabrightorboldtext
A_DIM Halfbrighttext
A_REVERSE Reverse-videotext
A_STANDOUT Thebesthighlightingmodeavailable
A_UNDERLINE Underlinedtext
So,todisplayareverse-videostatuslineonthetoplineofthescreen,youcouldcode:
stdscr.addstr(0, 0, "Current mode: Typing mode",
curses.A_REVERSE)
stdscr.refresh()
Thecurseslibraryalsosupportscoloronthoseterminalsthatprovideit. Themostcommonsuchterminalisprobably
theLinuxconsole,followedbycolorxterms.
5

| Form | Description |
| --- | --- |
| strorch | Displaythestringstrorcharacterchatthecurrentposition |
| strorch,attr | Displaythestringstrorcharacterch,usingattributeattratthecurrentposition |
| y,x,strorch | Movetopositiony,xwithinthewindow,anddisplaystrorch |
| y,x,strorch,attr | Movetopositiony,xwithinthewindow,anddisplaystrorch,usingattributeattr |


| Attribute | Description |
| --- | --- |
| A_BLINK | Blinkingtext |
| A_BOLD | Extrabrightorboldtext |
| A_DIM | Halfbrighttext |
| A_REVERSE | Reverse-videotext |
| A_STANDOUT | Thebesthighlightingmodeavailable |
| A_UNDERLINE | Underlinedtext |

### 第6页

Tousecolor,youmustcallthestart_color()functionsoonaftercallinginitscr(),toinitializethedefaultcolor
set (the curses.wrapper() function does this automatically). Once that’s done, the has_colors() function
returns TRUE if the terminal in use can actually display color. (Note: curses uses the American spelling ‘color’,
insteadoftheCanadian/Britishspelling‘colour’. Ifyou’reusedtotheBritishspelling,you’llhavetoresignyourself
tomisspellingitforthesakeofthesefunctions.)
Thecurseslibrarymaintainsafinitenumberofcolorpairs,containingaforeground(ortext)colorandabackground
color. Youcangettheattributevaluecorrespondingtoacolorpairwiththecolor_pair()function; thiscanbe
bitwise-OR’edwithotherattributessuchasA_REVERSE,butagain,suchcombinationsarenotguaranteedtowork
onallterminals.
Anexample,whichdisplaysalineoftextusingcolorpair1:
stdscr.addstr("Pretty text", curses.color_pair(1))
stdscr.refresh()
AsIsaidbefore,acolorpairconsistsofaforegroundandbackgroundcolor. Theinit_pair(n, f, b)function
changesthedefinitionofcolorpairn,toforegroundcolorfandbackgroundcolorb. Colorpair0ishard-wiredto
whiteonblack,andcannotbechanged.
Colorsarenumbered,andstart_color()initializes8basiccolorswhenitactivatescolormode. Theyare:0:black,
1:red,2:green,3:yellow,4:blue,5:magenta,6:cyan,and7:white. Thecursesmoduledefinesnamedconstantsfor
eachofthesecolors: curses.COLOR_BLACK,curses.COLOR_RED,andsoforth.
Let’sputallthistogether. Tochangecolor1toredtextonawhitebackground,youwouldcall:
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
Whenyouchangeacolorpair, anytextalreadydisplayedusingthatcolorpairwillchangetothenewcolors. You
canalsodisplaynewtextinthiscolorwith:
stdscr.addstr(0,0, "RED ALERT!", curses.color_pair(1))
VeryfancyterminalscanchangethedefinitionsoftheactualcolorstoagivenRGBvalue. Thisletsyouchangecolor
1,whichisusuallyred,topurpleorblueoranyothercoloryoulike. Unfortunately,theLinuxconsoledoesn’tsupport
this,soI’munabletotryitout,andcan’tprovideanyexamples. Youcancheckifyourterminalcandothisbycalling
can_change_color(),whichreturnsTrueifthecapabilityisthere. Ifyou’reluckyenoughtohavesuchatalented
terminal,consultyoursystem’smanpagesformoreinformation.
5 User Input
The C curses library offers only very simple input mechanisms. Python’s curses module adds a basic text-input
widget. (OtherlibrariessuchasUrwidhavemoreextensivecollectionsofwidgets.)
Therearetwomethodsforgettinginputfromawindow:
• getch()refreshesthescreenandthenwaitsfortheusertohitakey,displayingthekeyifecho()hasbeen
calledearlier. Youcanoptionallyspecifyacoordinatetowhichthecursorshouldbemovedbeforepausing.
• getkey()doesthesamethingbutconvertstheintegertoastring. Individualcharactersarereturnedas1-
characterstrings,andspecialkeyssuchasfunctionkeysreturnlongerstringscontainingakeynamesuchas
KEY_UPor^G.
It’spossibletonotwaitfortheuserusingthenodelay()windowmethod. Afternodelay(True),getch()and
getkey()forthewindowbecomenon-blocking. Tosignalthatnoinputisready,getch()returnscurses.ERR
(avalueof-1)andgetkey()raisesanexception. There’salsoahalfdelay()function,whichcanbeusedto(in
effect)setatimeroneachgetch();ifnoinputbecomesavailablewithinaspecifieddelay(measuredintenthsofa
second),cursesraisesanexception.
Thegetch()methodreturnsaninteger;ifit’sbetween0and255,itrepresentstheASCIIcodeofthekeypressed.
Values greater than 255 are special keys such as Page Up, Home, or the cursor keys. You can compare the value
returned to constants such as curses.KEY_PPAGE, curses.KEY_HOME, or curses.KEY_LEFT. The main loop
ofyourprogrammaylooksomethinglikethis:
6

### 第7页

while True:
c = stdscr.getch()
if c == ord('p'):
PrintDocument()
elif c == ord('q'):
break # Exit the while loop
elif c == curses.KEY_HOME:
x = y = 0
Thecurses.asciimodulesuppliesASCIIclassmembershipfunctionsthattakeeitherintegeror1-characterstring
arguments;thesemaybeusefulinwritingmorereadabletestsforsuchloops. Italsosuppliesconversionfunctionsthat
takeeitherintegeror1-character-stringargumentsandreturnthesametype. Forexample,curses.ascii.ctrl()
returnsthecontrolcharactercorrespondingtoitsargument.
There’salsoamethodtoretrieveanentirestring,getstr(). Itisn’tusedveryoften,becauseitsfunctionalityisquite
limited;theonlyeditingkeysavailablearethebackspacekeyandtheEnterkey,whichterminatesthestring. Itcan
optionallybelimitedtoafixednumberofcharacters.
curses.echo() # Enable echoing of characters
# Get a 15-character string, with the cursor on the top line
s = stdscr.getstr(0,0, 15)
Thecurses.textpadmodulesuppliesatextboxthatsupportsanEmacs-likesetofkeybindings. Variousmethods
oftheTextboxclasssupporteditingwithinputvalidationandgatheringtheeditresultseitherwithorwithouttrailing
spaces. Here’sanexample:
import curses
from curses.textpad import Textbox, rectangle
def main(stdscr):
stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")
editwin = curses.newwin(5,30, 2,1)
rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
stdscr.refresh()
box = Textbox(editwin)
# Let the user edit until Ctrl-G is struck.
box.edit()
# Get resulting contents
message = box.gather()
Seethelibrarydocumentationoncurses.textpadformoredetails.
6 For More Information
ThisHOWTOdoesn’tcoversomeadvancedtopics, suchasreadingthecontentsofthescreenorcapturingmouse
eventsfromanxterminstance,butthePythonlibrarypageforthecursesmoduleisnowreasonablycomplete. You
shouldbrowseitnext.
If you’re in doubt about the detailed behavior of the curses functions, consult the manual pages for your curses
implementation, whether it’s ncursesor a proprietaryUnix vendor’s. The manual pageswill document anyquirks,
andprovidecompletelistsofallthefunctions,attributes,andACS_*charactersavailabletoyou.
BecausethecursesAPIissolarge,somefunctionsaren’tsupportedinthePythoninterface. Oftenthisisn’tbecause
they’redifficulttoimplement,butbecausenoonehasneededthemyet. Also,Pythondoesn’tyetsupportthemenu
7

### 第8页

library associated with ncurses. Patches adding support for these would be welcome; see the Python Developer’s
GuidetolearnmoreaboutsubmittingpatchestoPython.
• WritingProgramswithNCURSES:alengthytutorialforCprogrammers.
• Thencursesmanpage
• ThencursesFAQ
• “Usecurses…don’tswear”: videoofaPyCon2013talkoncontrollingterminalsusingcursesorUrwid.
• “ConsoleApplicationswithUrwid”: videoofaPyConCA2012talkdemonstratingsomeapplicationswritten
usingUrwid.
8

