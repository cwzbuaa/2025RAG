### 第1页

Socket Programming HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Sockets 1
1.1 History. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 CreatingaSocket 2
2.1 IPC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3 UsingaSocket 3
3.1 BinaryData . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
4 Disconnecting 5
4.1 WhenSocketsDie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
5 Non-blockingSockets 5
Author
GordonMcMillan
Abstract
Socketsareusednearlyeverywhere,butareoneofthemostseverelymisunderstoodtechnologiesaround. Thisisa
10,000footoverviewofsockets. It’snotreallyatutorial-you’llstillhaveworktodoingettingthingsoperational.
It doesn’t cover the fine points (and there are a lot of them), but I hope it will give you enough background to
beginusingthemdecently.
1 Sockets
I’monlygoingtotalkaboutINET(i.e. IPv4)sockets,buttheyaccountforatleast99%ofthesocketsinuse. AndI’ll
onlytalkaboutSTREAM(i.e. TCP)sockets-unlessyoureallyknowwhatyou’redoing(inwhichcasethisHOWTO
isn’tforyou!),you’llgetbetterbehaviorandperformancefromaSTREAMsocketthananythingelse. Iwilltryto
clearupthemysteryofwhatasocketis,aswellassomehintsonhowtoworkwithblockingandnon-blockingsockets.
ButI’llstartbytalkingaboutblockingsockets. You’llneedtoknowhowtheyworkbeforedealingwithnon-blocking
sockets.
Part of the trouble with understanding these things is that “socket” can mean a number of subtly different things,
dependingoncontext. Sofirst,let’smakeadistinctionbetweena“client”socket-anendpointofaconversation,and
1

### 第2页

a“server”socket,whichismorelikeaswitchboardoperator. Theclientapplication(yourbrowser,forexample)uses
“client”socketsexclusively;thewebserverit’stalkingtousesboth“server”socketsand“client”sockets.
1.1 History
Of the various forms of IPC (Inter Process Communication), sockets are by far the most popular. On any given
platform,therearelikelytobeotherformsofIPCthatarefaster,butforcross-platformcommunication,socketsare
abouttheonlygameintown.
They were invented in Berkeley as part of the BSD flavor of Unix. They spread like wildfire with the internet.
Withgoodreason—thecombinationofsocketswithINETmakestalkingtoarbitrarymachinesaroundtheworld
unbelievablyeasy(atleastcomparedtootherschemes).
2 Creating a Socket
Roughlyspeaking,whenyouclickedonthelinkthatbroughtyoutothispage,yourbrowserdidsomethinglikethe
following:
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))
When the connect completes, the socket s can be used to send in a request for the text of the page. The same
socketwillreadthereply,andthenbedestroyed. That’sright,destroyed. Clientsocketsarenormallyonlyusedfor
oneexchange(orasmallsetofsequentialexchanges).
Whathappensinthewebserverisabitmorecomplex. First,thewebservercreatesa“serversocket”:
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)
A couple things to notice: we used socket.gethostname() so that the socket would be visible to the outside
world. Ifwehaduseds.bind(('localhost', 80))ors.bind(('127.0.0.1', 80))wewouldstillhave
a “server” socket, but one that was only visible within the same machine. s.bind(('', 80)) specifies that the
socketisreachablebyanyaddressthemachinehappenstohave.
A second thing to note: low number ports are usually reserved for “well known” services (HTTP, SNMP etc). If
you’replayingaround,useanicehighnumber(4digits).
Finally,theargumenttolistentellsthesocketlibrarythatwewantittoqueueupasmanyas5connectrequests(the
normalmax)beforerefusingoutsideconnections. Iftherestofthecodeiswrittenproperly,thatshouldbeplenty.
Nowthatwehavea“server”socket,listeningonport80,wecanenterthemainloopofthewebserver:
while True:
# accept connections from outside
(clientsocket, address) = serversocket.accept()
# now do something with the clientsocket
# in this case, we'll pretend this is a threaded server
ct = make_client_thread(clientsocket)
ct.start()
There’s actually 3 general ways in which this loop could work - dispatching a thread to handle clientsocket,
createanewprocesstohandleclientsocket,orrestructurethisapptousenon-blockingsockets,andmultiplex
betweenour“server”socketandanyactiveclientsocketsusingselect. Moreaboutthatlater. Theimportant
thingtounderstandnowisthis: thisisalla“server”socketdoes. Itdoesn’tsendanydata. Itdoesn’treceiveanydata.
2

### 第3页

It just produces “client” sockets. Each clientsocket is created in response to some other “client” socket doing
aconnect()tothehostandportwe’reboundto. Assoonaswe’vecreatedthatclientsocket, wegobackto
listeningformoreconnections. Thetwo“clients”arefreetochatitup-theyareusingsomedynamicallyallocated
portwhichwillberecycledwhentheconversationends.
2.1 IPC
IfyouneedfastIPCbetweentwoprocessesononemachine,youshouldlookintopipesorsharedmemory. Ifyou
dodecidetouseAF_INETsockets,bindthe“server”socketto'localhost'. Onmostplatforms,thiswilltakea
shortcutaroundacoupleoflayersofnetworkcodeandbequiteabitfaster.
(cid:181) Seealso
Themultiprocessingintegratescross-platformIPCintoahigher-levelAPI.
3 Using a Socket
Thefirstthingtonote,isthatthewebbrowser’s“client”socketandthewebserver’s“client”socketareidenticalbeasts.
Thatis,thisisa“peertopeer”conversation. Ortoputitanotherway,asthedesigner,youwillhavetodecidewhat
therulesofetiquetteareforaconversation. Normally,theconnectingsocketstartstheconversation,bysendingin
arequest,orperhapsasignon. Butthat’sadesigndecision-it’snotaruleofsockets.
Nowtherearetwosetsofverbstouseforcommunication. Youcanusesendandrecv,oryoucantransformyour
clientsocketintoafile-likebeastandusereadandwrite. ThelatteristhewayJavapresentsitssockets. I’mnot
goingtotalkaboutithere, excepttowarnyouthatyouneedtouse flushonsockets. Thesearebuffered“files”,
andacommonmistakeistowritesomething,andthenreadforareply. Withoutaflushinthere,youmaywait
foreverforthereply,becausetherequestmaystillbeinyouroutputbuffer.
Nowwecometothemajorstumblingblockofsockets-sendandrecvoperateonthenetworkbuffers. Theydo
notnecessarilyhandleallthebytesyouhandthem(orexpectfromthem),becausetheirmajorfocusishandlingthe
network buffers. In general, they return when the associated network buffers have been filled (send) or emptied
(recv). They then tell you how many bytes they handled. It is your responsibility to call them again until your
messagehasbeencompletelydealtwith.
Whenarecvreturns0bytes,itmeanstheothersidehasclosed(orisintheprocessofclosing)theconnection. You
willnotreceiveanymoredataonthisconnection. Ever. Youmaybeabletosenddatasuccessfully; I’lltalkmore
aboutthislater.
AprotocollikeHTTPusesasocketforonlyonetransfer. Theclientsendsarequest,thenreadsareply. That’sit.
Thesocketisdiscarded. Thismeansthataclientcandetecttheendofthereplybyreceiving0bytes.
Butifyouplantoreuseyoursocketforfurthertransfers,youneedtorealizethatthereisnoEOT(EndofTransfer)
onasocket. Irepeat: ifasocketsendorrecvreturnsafterhandling0bytes,theconnectionhasbeenbroken. If
theconnectionhasnotbeenbroken,youmaywaitonarecvforever,becausethesocketwillnottellyouthatthere’s
nothing more to read (for now). Now if you think about that a bit, you’ll come to realize a fundamental truth of
sockets: messages must either be fixed length (yuck), or be delimited (shrug), or indicate how long they are (much
better),orendbyshuttingdowntheconnection. Thechoiceisentirelyyours,(butsomewaysarerighterthanothers).
Assumingyoudon’twanttoendtheconnection,thesimplestsolutionisafixedlengthmessage:
class MySocket:
"""demonstration class only
- coded for clarity, not efficiency
"""
def __init__(self, sock=None):
if sock is None:
self.sock = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)
(continuesonnextpage)
3

| (cid:181) Seealso |
| --- |
| Themultiprocessingintegratescross-platformIPCintoahigher-levelAPI. |

### 第4页

(continuedfrompreviouspage)
else:
self.sock = sock
def connect(self, host, port):
self.sock.connect((host, port))
def mysend(self, msg):
totalsent = 0
while totalsent < MSGLEN:
sent = self.sock.send(msg[totalsent:])
if sent == 0:
raise RuntimeError("socket connection broken")
totalsent = totalsent + sent
def myreceive(self):
chunks = []
bytes_recd = 0
while bytes_recd < MSGLEN:
chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
if chunk == b'':
raise RuntimeError("socket connection broken")
chunks.append(chunk)
bytes_recd = bytes_recd + len(chunk)
return b''.join(chunks)
The sending code here is usable for almost any messaging scheme - in Python you send strings, and you can use
len()todetermineitslength(evenifithasembedded\0characters). It’smostlythereceivingcodethatgetsmore
complex. (AndinC,it’snotmuchworse,exceptyoucan’tusestrlenifthemessagehasembedded\0s.)
Theeasiestenhancementistomakethefirstcharacterofthemessageanindicatorofmessagetype,andhavethetype
determinethelength. Nowyouhavetworecvs-thefirsttoget(atleast)thatfirstcharactersoyoucanlookupthe
length,andthesecondinalooptogettherest. Ifyoudecidetogothedelimitedroute,you’llbereceivinginsome
arbitrarychunksize,(4096or8192isfrequentlyagoodmatchfornetworkbuffersizes),andscanningwhatyou’ve
receivedforadelimiter.
Onecomplicationtobeawareof: ifyourconversationalprotocolallowsmultiplemessagestobesentbacktoback
(without some kind of reply), and you pass recv an arbitrary chunk size, you may end up reading the start of a
followingmessage. You’llneedtoputthatasideandholdontoit,untilit’sneeded.
Prefixingthemessagewithitslength(say,as5numericcharacters)getsmorecomplex,because(believeitornot),
youmaynotgetall5charactersinonerecv. Inplayingaround,you’llgetawaywithit;butinhighnetworkloads,
yourcodewillveryquicklybreakunlessyouusetworecvloops-thefirsttodeterminethelength,thesecondtoget
thedatapartofthemessage. Nasty. Thisisalsowhenyou’lldiscoverthatsenddoesnotalwaysmanagetogetrid
ofeverythinginonepass. Anddespitehavingreadthis,youwilleventuallygetbitbyit!
Intheinterestsofspace,buildingyourcharacter,(andpreservingmycompetitiveposition),theseenhancementsare
leftasanexerciseforthereader. Letsmoveontocleaningup.
3.1 Binary Data
Itisperfectlypossibletosendbinarydataoverasocket. Themajorproblemisthatnotallmachinesusethesame
formatsforbinarydata. Forexample,networkbyteorderisbig-endian,withthemostsignificantbytefirst,soa16
bitintegerwiththevalue1wouldbethetwohexbytes00 01. However,mostcommonprocessors(x86/AMD64,
ARM,RISC-V),arelittle-endian,withtheleastsignificantbytefirst-thatsame1wouldbe01 00.
Socket libraries have calls for converting 16 and 32 bit integers - ntohl, htonl, ntohs, htons where “n”
meansnetworkand“h”meanshost,“s”meansshortand“l”meanslong. Wherenetworkorderishostorder,thesedo
nothing,butwherethemachineisbyte-reversed,theseswapthebytesaroundappropriately.
In these days of 64-bit machines, the ASCII representation of binary data is frequently smaller than the binary
4

### 第5页

representation. That’s because a surprising amount of the time, most integers have the value 0, or maybe 1. The
string"0"wouldbetwobytes,whileafull64-bitintegerwouldbe8. Ofcourse,thisdoesn’tfitwellwithfixed-length
messages. Decisions,decisions.
4 Disconnecting
Strictlyspeaking,you’resupposedtouseshutdownonasocketbeforeyoucloseit. Theshutdownisanadvisory
tothesocketattheotherend. Dependingontheargumentyoupassit,itcanmean“I’mnotgoingtosendanymore,
butI’llstilllisten”,or“I’mnotlistening,goodriddance!”. Mostsocketlibraries,however,aresousedtoprogrammers
neglectingtousethispieceofetiquettethatnormallyacloseisthesameasshutdown(); close(). Soinmost
situations,anexplicitshutdownisnotneeded.
One way to use shutdown effectively is in an HTTP-like exchange. The client sends a request and then does a
shutdown(1). Thistellstheserver“Thisclientisdonesending,butcanstillreceive.” Theservercandetect“EOF”
byareceiveof0bytes. Itcanassumeithasthecompleterequest. Theserversendsareply. Ifthesendcompletes
successfullythen,indeed,theclientwasstillreceiving.
Pythontakestheautomaticshutdownastepfurther, andsaysthatwhenasocketisgarbagecollected, itwillauto-
maticallydoacloseifit’sneeded. Butrelyingonthisisaverybadhabit. Ifyoursocketjustdisappearswithout
doing a close, the socket at the other end may hang indefinitely, thinking you’re just being slow. Please close
yoursocketswhenyou’redone.
4.1 When Sockets Die
Probablytheworstthingaboutusingblockingsocketsiswhathappenswhentheothersidecomesdownhard(without
doingaclose). Yoursocketislikelytohang. TCPisareliableprotocol,anditwillwaitalong,longtimebefore
givinguponaconnection. Ifyou’reusingthreads,theentirethreadisessentiallydead. There’snotmuchyoucando
aboutit. Aslongasyouaren’tdoingsomethingdumb, likeholdingalockwhiledoingablockingread, thethread
isn’treallyconsumingmuchinthewayofresources. Donottrytokillthethread-partofthereasonthatthreadsare
moreefficientthanprocessesisthattheyavoidtheoverheadassociatedwiththeautomaticrecyclingofresources. In
otherwords,ifyoudomanagetokillthethread,yourwholeprocessislikelytobescrewedup.
5 Non-blocking Sockets
Ifyou’veunderstoodthepreceding,youalreadyknowmostofwhatyouneedtoknowaboutthemechanicsofusing
sockets. You’llstillusethesamecalls,inmuchthesameways. It’sjustthat,ifyoudoitright,yourappwillbealmost
inside-out.
In Python, you use socket.setblocking(False) to make it non-blocking. In C, it’s more complex, (for one
thing, you’ll need to choose between the BSD flavor O_NONBLOCK and the almost indistinguishable POSIX flavor
O_NDELAY, which is completely different from TCP_NODELAY), but it’s the exact same idea. You do this after
creatingthesocket,butbeforeusingit. (Actually,ifyou’renuts,youcanswitchbackandforth.)
Themajormechanicaldifferenceisthatsend,recv,connectandacceptcanreturnwithouthavingdoneanything.
Youhave(ofcourse)anumberofchoices. Youcancheckreturncodeanderrorcodesandgenerallydriveyourself
crazy. If you don’t believe me, try it sometime. Your app will grow large, buggy and suck CPU. So let’s skip the
brain-deadsolutionsanddoitright.
Useselect.
InC,codingselectisfairlycomplex. InPython,it’sapieceofcake,butit’scloseenoughtotheCversionthatif
youunderstandselectinPython,you’llhavelittletroublewithitinC:
ready_to_read, ready_to_write, in_error = \
select.select(
potential_readers,
potential_writers,
potential_errs,
timeout)
5

### 第6页

You pass select three lists: the first contains all sockets that you might want to try reading; the second all the
socketsyoumightwanttotrywritingto,andthelast(normallyleftempty)thosethatyouwanttocheckforerrors.
You should note that a socket can go into more than one list. The select call is blocking, but you can give it a
timeout. This is generally a sensible thing to do - give it a nice long timeout (say a minute) unless you have good
reasontodootherwise.
Inreturn,youwillgetthreelists. Theycontainthesocketsthatareactuallyreadable,writableandinerror. Eachof
theselistsisasubset(possiblyempty)ofthecorrespondinglistyoupassedin.
Ifasocketisintheoutputreadablelist,youcanbeas-close-to-certain-as-we-ever-get-in-this-businessthatarecv
onthatsocketwillreturnsomething. Sameideaforthewritablelist. You’llbeabletosendsomething. Maybenotall
youwantto,butsomethingisbetterthannothing. (Actually,anyreasonablyhealthysocketwillreturnaswritable-it
justmeansoutboundnetworkbufferspaceisavailable.)
Ifyouhavea“server”socket,putitinthepotential_readerslist. Ifitcomesoutinthereadablelist,youracceptwill
(almostcertainly)work. Ifyouhavecreatedanewsockettoconnecttosomeoneelse,putitinthepotential_writers
list. Ifitshowsupinthewritablelist,youhaveadecentchancethatithasconnected.
Actually,selectcanbehandyevenwithblockingsockets. It’sonewayofdeterminingwhetheryouwillblock-the
socketreturnsasreadablewhenthere’ssomethinginthebuffers. However,thisstilldoesn’thelpwiththeproblemof
determiningwhethertheotherendisdone,orjustbusywithsomethingelse.
Portabilityalert: OnUnix,selectworksbothwiththesocketsandfiles. Don’ttrythisonWindows. OnWindows,
selectworkswithsocketsonly. AlsonotethatinC,manyofthemoreadvancedsocketoptionsaredonedifferently
onWindows. Infact,onWindowsIusuallyusethreads(whichworkvery,verywell)withmysockets.
6

