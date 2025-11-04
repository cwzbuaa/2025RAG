### 第1页

HOWTO Fetch Internet Resources
Using The urllib Package
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Introduction 1
2 FetchingURLs 2
2.1 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Headers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3 HandlingExceptions 4
3.1 URLError . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 HTTPError . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3 WrappingitUp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4 infoandgeturl 6
5 OpenersandHandlers 7
6 BasicAuthentication 7
7 Proxies 8
8 SocketsandLayers 9
9 Footnotes 9
Index 10
Author
MichaelFoord
1 Introduction
RelatedArticles
YoumayalsofindusefulthefollowingarticleonfetchingwebresourceswithPython:
1

### 第2页

• BasicAuthentication
AtutorialonBasicAuthentication,withexamplesinPython.
urllib.requestisaPythonmoduleforfetchingURLs(UniformResourceLocators). Itoffersaverysimpleinterface,
intheformoftheurlopenfunction. ThisiscapableoffetchingURLsusingavarietyofdifferentprotocols. Italso
offersaslightlymorecomplexinterfaceforhandlingcommonsituations-likebasicauthentication,cookies,proxies
andsoon. Theseareprovidedbyobjectscalledhandlersandopeners.
urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ":" in URL -
forexample"ftp"istheURLschemeof"ftp://python.org/")usingtheirassociatednetworkprotocols(e.g.
FTP,HTTP).Thistutorialfocusesonthemostcommoncase,HTTP.
Forstraightforwardsituationsurlopenisveryeasytouse. Butassoonasyouencountererrorsornon-trivialcases
whenopeningHTTPURLs,youwillneedsomeunderstandingoftheHyperTextTransferProtocol. Themostcom-
prehensiveandauthoritativereferencetoHTTPisRFC2616. Thisisatechnicaldocumentandnotintendedtobe
easytoread. ThisHOWTOaimstoillustrateusingurllib,withenoughdetailaboutHTTPtohelpyouthrough. Itis
notintendedtoreplacetheurllib.requestdocs,butissupplementarytothem.
2 Fetching URLs
Thesimplestwaytouseurllib.requestisasfollows:
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
html = response.read()
If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the shutil.
copyfileobj()andtempfile.NamedTemporaryFile()functions:
import shutil
import tempfile
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
shutil.copyfileobj(response, tmp_file)
with open(tmp_file.name) as html:
pass
Manyusesofurllibwillbethatsimple(notethatinsteadofan‘http:’ URLwecouldhaveusedaURLstartingwith
‘ftp:’,‘file:’,etc.). However,it’sthepurposeofthistutorialtoexplainthemorecomplicatedcases,concentratingon
HTTP.
HTTP is based on requests and responses - the client makes requests and servers send responses. urllib.request
mirrorsthiswithaRequestobjectwhichrepresentstheHTTPrequestyouaremaking. Initssimplestformyou
createaRequestobjectthatspecifiestheURLyouwanttofetch. CallingurlopenwiththisRequestobjectreturns
aresponseobjectfortheURLrequested. Thisresponseisafile-likeobject,whichmeansyoucanforexamplecall
.read()ontheresponse:
import urllib.request
req = urllib.request.Request('http://python.org/')
with urllib.request.urlopen(req) as response:
the_page = response.read()
Notethaturllib.requestmakesuseofthesameRequestinterfacetohandleallURLschemes. Forexample,youcan
makeanFTPrequestlikeso:
2

### 第3页

req = urllib.request.Request('ftp://example.com/')
InthecaseofHTTP,therearetwoextrathingsthatRequestobjectsallowyoutodo: First,youcanpassdatatobe
senttotheserver. Second,youcanpassextrainformation(“metadata”)aboutthedataorabouttherequestitself,to
theserver-thisinformationissentasHTTP“headers”. Let’slookateachoftheseinturn.
2.1 Data
SometimesyouwanttosenddatatoaURL(oftentheURLwillrefertoaCGI(CommonGatewayInterface)script
orotherwebapplication). WithHTTP,thisisoftendoneusingwhat’sknownasaPOSTrequest. Thisisoftenwhat
yourbrowserdoeswhenyousubmitaHTMLformthatyoufilledinontheweb. NotallPOSTshavetocomefrom
forms: youcanuseaPOSTtotransmitarbitrarydatatoyourownapplication. InthecommoncaseofHTMLforms,
thedataneedstobeencodedinastandardway,andthenpassedtotheRequestobjectasthedataargument. The
encodingisdoneusingafunctionfromtheurllib.parselibrary.
import urllib.parse
import urllib.request
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
'location' : 'Northampton',
'language' : 'Python' }
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
the_page = response.read()
Notethatotherencodingsaresometimesrequired(e.g. forfileuploadfromHTMLforms-seeHTMLSpecification,
FormSubmissionformoredetails).
Ifyoudonotpassthedataargument,urllibusesaGETrequest. OnewayinwhichGETandPOSTrequestsdiffer
is that POST requests often have “side-effects”: they change the state of the system in some way (for example by
placing an order with the website for a hundredweight of tinned spam to be delivered to your door). Though the
HTTP standard makes it clear that POSTs are intended to always cause side-effects, and GET requests never to
cause side-effects, nothing prevents a GET request from having side-effects, nor a POST requests from having no
side-effects. DatacanalsobepassedinanHTTPGETrequestbyencodingitintheURLitself.
Thisisdoneasfollows:
>>> import urllib.request
>>> import urllib.parse
>>> data = {}
>>> data['name'] = 'Somebody Here'
>>> data['location'] = 'Northampton'
>>> data['language'] = 'Python'
>>> url_values = urllib.parse.urlencode(data)
>>> print(url_values) # The order may differ from below.
name=Somebody+Here&language=Python&location=Northampton
>>> url = 'http://www.example.com/example.cgi'
>>> full_url = url + '?' + url_values
>>> data = urllib.request.urlopen(full_url)
NoticethatthefullURLiscreatedbyaddinga?totheURL,followedbytheencodedvalues.
3

### 第4页

2.2 Headers
We’lldiscusshereoneparticularHTTPheader,toillustratehowtoaddheaderstoyourHTTPrequest.
Some websites1 dislike being browsed by programs, or send different versions to different browsers2. By default
urllib identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the
Pythonrelease,e.g. Python-urllib/2.5),whichmayconfusethesite,orjustplainnotwork. Thewayabrowser
identifiesitselfisthroughtheUser-Agentheader3. WhenyoucreateaRequestobjectyoucanpassadictionary
ofheadersin. Thefollowingexamplemakesthesamerequestasabove,butidentifiesitselfasaversionofInternet
Explorer4.
import urllib.parse
import urllib.request
url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
'location': 'Northampton',
'language': 'Python' }
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
the_page = response.read()
Theresponsealsohastwousefulmethods. Seethesectiononinfoandgeturl whichcomesafterwehavealookat
whathappenswhenthingsgowrong.
3 Handling Exceptions
urlopenraisesURLErrorwhenitcannothandlearesponse(thoughasusualwithPythonAPIs,built-inexceptions
suchasValueError,TypeErroretc. mayalsoberaised).
HTTPErroristhesubclassofURLErrorraisedinthespecificcaseofHTTPURLs.
Theexceptionclassesareexportedfromtheurllib.errormodule.
3.1 URLError
Often,URLErrorisraisedbecausethereisnonetworkconnection(noroutetothespecifiedserver),orthespecified
server doesn’t exist. In this case, the exception raised will have a ‘reason’ attribute, which is a tuple containing an
errorcodeandatexterrormessage.
e.g.
>>> req = urllib.request.Request('http://www.pretend_server.org')
>>> try: urllib.request.urlopen(req)
... except urllib.error.URLError as e:
... print(e.reason)
...
(4, 'getaddrinfo failed')
1Googleforexample.
2Browsersniffingisaverybadpracticeforwebsitedesign-buildingsitesusingwebstandardsismuchmoresensible.Unfortunatelyalotof
sitesstillsenddifferentversionstodifferentbrowsers.
3TheuseragentforMSIE6is‘Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;.NETCLR1.1.4322)’
4FordetailsofmoreHTTPrequestheaders,seeQuickReferencetoHTTPHeaders.
4

### 第5页

3.2 HTTPError
EveryHTTPresponsefromtheservercontainsanumeric“statuscode”. Sometimesthestatuscodeindicatesthatthe
serverisunabletofulfiltherequest. Thedefaulthandlerswillhandlesomeoftheseresponsesforyou(forexample,
iftheresponseisa“redirection”thatrequeststheclientfetchthedocumentfromadifferentURL,urllibwillhandle
that for you). For those it can’t handle, urlopen will raise an HTTPError. Typical errors include ‘404’ (page not
found),‘403’(requestforbidden),and‘401’(authenticationrequired).
Seesection10ofRFC2616forareferenceonalltheHTTPerrorcodes.
TheHTTPErrorinstanceraisedwillhaveaninteger‘code’attribute,whichcorrespondstotheerrorsentbytheserver.
ErrorCodes
Because the default handlers handle redirects (codes in the 300 range), and codes in the 100–299 range indicate
success,youwillusuallyonlyseeerrorcodesinthe400–599range.
http.server.BaseHTTPRequestHandler.responsesisausefuldictionaryofresponsecodesthatshowsall
theresponsecodesusedbyRFC2616. Anexcerptfromthedictionaryisshownbelow
responses = {
...
<HTTPStatus.OK: 200>: ('OK', 'Request fulfilled, document follows'),
...
<HTTPStatus.FORBIDDEN: 403>: ('Forbidden',
'Request forbidden -- authorization will '
'not help'),
<HTTPStatus.NOT_FOUND: 404>: ('Not Found',
'Nothing matches the given URI'),
...
<HTTPStatus.IM_A_TEAPOT: 418>: ("I'm a Teapot",
'Server refuses to brew coffee because '
'it is a teapot'),
...
<HTTPStatus.SERVICE_UNAVAILABLE: 503>: ('Service Unavailable',
'The server cannot process the '
'request due to a high load'),
...
}
WhenanerrorisraisedtheserverrespondsbyreturninganHTTPerrorcodeand anerrorpage. Youcanusethe
HTTPErrorinstanceasaresponseonthepagereturned. Thismeansthataswellasthecodeattribute, italsohas
read,geturl,andinfo,methodsasreturnedbytheurllib.responsemodule:
>>> req = urllib.request.Request('http://www.python.org/fish.html')
>>> try:
... urllib.request.urlopen(req)
... except urllib.error.HTTPError as e:
... print(e.code)
... print(e.read())
...
404
b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n\n<html
...
<title>Page Not Found</title>\n
...
5

### 第6页

3.3 Wrapping it Up
So if you want to be prepared for HTTPError or URLError there are two basic approaches. I prefer the second
approach.
Number1
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request(someurl)
try:
response = urlopen(req)
except HTTPError as e:
print('The server couldn\'t fulfill the request.')
print('Error code: ', e.code)
except URLError as e:
print('We failed to reach a server.')
print('Reason: ', e.reason)
else:
# everything is fine
(cid:174) Note
Theexcept HTTPErrormustcomefirst,otherwiseexcept URLErrorwillalsocatchanHTTPError.
Number2
from urllib.request import Request, urlopen
from urllib.error import URLError
req = Request(someurl)
try:
response = urlopen(req)
except URLError as e:
if hasattr(e, 'reason'):
print('We failed to reach a server.')
print('Reason: ', e.reason)
elif hasattr(e, 'code'):
print('The server couldn\'t fulfill the request.')
print('Error code: ', e.code)
else:
# everything is fine
4 info and geturl
Theresponsereturnedbyurlopen(ortheHTTPErrorinstance)hastwousefulmethodsinfo()andgeturl()and
isdefinedinthemoduleurllib.response.
• geturl-thisreturnstherealURLofthepagefetched. Thisisusefulbecauseurlopen(ortheopenerobject
used)mayhavefollowedaredirect. TheURLofthepagefetchedmaynotbethesameastheURLrequested.
• info-thisreturnsadictionary-likeobjectthatdescribesthepagefetched,particularlytheheaderssentbythe
server. Itiscurrentlyanhttp.client.HTTPMessageinstance.
Typicalheadersinclude‘Content-length’,‘Content-type’,andsoon. SeetheQuickReferencetoHTTPHeadersfor
ausefullistingofHTTPheaderswithbriefexplanationsoftheirmeaninganduse.
6

### 第7页

5 Openers and Handlers
When you fetch a URL you use an opener (an instance of the perhaps confusingly named urllib.request.
OpenerDirector). Normallywehavebeenusingthedefaultopener-viaurlopen-butyoucancreatecustom
openers. Openers use handlers. All the “heavy lifting” is done by the handlers. Each handler knows how to open
URLsforaparticularURLscheme(http,ftp,etc.),orhowtohandleanaspectofURLopening,forexampleHTTP
redirectionsorHTTPcookies.
You will want to create openers if you want to fetch URLs with specific handlers installed, for example to get an
openerthathandlescookies,ortogetanopenerthatdoesnothandleredirections.
Tocreateanopener,instantiateanOpenerDirector,andthencall.add_handler(some_handler_instance)
repeatedly.
Alternatively,youcanusebuild_opener,whichisaconveniencefunctionforcreatingopenerobjectswithasingle
functioncall. build_openeraddsseveralhandlersbydefault,butprovidesaquickwaytoaddmoreand/oroverride
thedefaulthandlers.
Other sorts of handlers you might want to can handle proxies, authentication, and other common but slightly spe-
cialisedsituations.
install_opener can be used to make an opener object the (global) default opener. This means that calls to
urlopenwillusetheopeneryouhaveinstalled.
Openerobjectshavean open method, whichcanbe calleddirectlyto fetchurlsinthesamewayas theurlopen
function: there’snoneedtocallinstall_opener,exceptasaconvenience.
6 Basic Authentication
ToillustratecreatingandinstallingahandlerwewillusetheHTTPBasicAuthHandler. Foramoredetaileddis-
cussionofthissubject–includinganexplanationofhowBasicAuthenticationworks-seetheBasicAuthentication
Tutorial.
Whenauthenticationisrequired,theserversendsaheader(aswellasthe401errorcode)requestingauthentication.
This specifies the authentication scheme and a ‘realm’. The header looks like: WWW-Authenticate: SCHEME
realm="REALM".
e.g.
WWW-Authenticate: Basic realm="cPanel Users"
The client should then retry the request with the appropriate name and password for the realm included as a
header in the request. This is ‘basic authentication’. In order to simplify this process we can create an instance
ofHTTPBasicAuthHandlerandanopenertousethishandler.
TheHTTPBasicAuthHandlerusesanobjectcalledapasswordmanagertohandlethemappingofURLsandrealms
topasswordsandusernames. Ifyouknowwhattherealmis(fromtheauthenticationheadersentbytheserver),then
youcanuseaHTTPPasswordMgr. Frequentlyonedoesn’tcarewhattherealmis. Inthatcase,itisconvenienttouse
HTTPPasswordMgrWithDefaultRealm. ThisallowsyoutospecifyadefaultusernameandpasswordforaURL.
Thiswillbesuppliedintheabsenceofyouprovidinganalternativecombinationforaspecificrealm. Weindicate
thisbyprovidingNoneastherealmargumenttotheadd_passwordmethod.
The top-level URL is the first URL that requires authentication. URLs “deeper” than the URL you pass to
.add_password()willalsomatch.
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)
(continuesonnextpage)
7

### 第8页

(continuedfrompreviouspage)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
# use the opener to fetch a URL
opener.open(a_url)
# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)
(cid:174) Note
IntheaboveexampleweonlysuppliedourHTTPBasicAuthHandlertobuild_opener. Bydefaultopeners
havethehandlersfornormalsituations–ProxyHandler(ifaproxysettingsuchasanhttp_proxyenvironment
variableisset),UnknownHandler,HTTPHandler,HTTPDefaultErrorHandler,HTTPRedirectHandler,
FTPHandler,FileHandler,DataHandler,HTTPErrorProcessor.
top_level_urlisinfacteitherafullURL(includingthe‘http:’schemecomponentandthehostnameandoptionally
the port number) e.g. "http://example.com/" or an “authority” (i.e. the hostname, optionally including the
portnumber)e.g. "example.com"or"example.com:8080"(thelatterexampleincludesaportnumber). The
authority,ifpresent,mustNOTcontainthe“userinfo”component-forexample"joe:password@example.com"
isnotcorrect.
7 Proxies
urllibwillauto-detectyourproxysettingsandusethose. ThisisthroughtheProxyHandler,whichispartofthe
normalhandlerchainwhenaproxysettingisdetected. Normallythat’sagoodthing,butthereareoccasionswhenit
maynotbehelpful5. OnewaytodothisistosetupourownProxyHandler,withnoproxiesdefined. Thisisdone
usingsimilarstepstosettingupaBasicAuthenticationhandler:
>>> proxy_support = urllib.request.ProxyHandler({})
>>> opener = urllib.request.build_opener(proxy_support)
>>> urllib.request.install_opener(opener)
(cid:174) Note
Currentlyurllib.requestdoesnot supportfetchingofhttpslocationsthroughaproxy. However,thiscan
beenabledbyextendingurllib.requestasshownintherecipe6.
(cid:174) Note
HTTP_PROXYwillbeignoredifavariableREQUEST_METHODisset;seethedocumentationongetproxies().
5InmycaseIhavetouseaproxytoaccesstheinternetatwork.IfyouattempttofetchlocalhostURLsthroughthisproxyitblocksthem.IE
issettousetheproxy,whichurllibpicksupon.Inordertotestscriptswithalocalhostserver,Ihavetopreventurllibfromusingtheproxy.
6urllibopenerforSSLproxy(CONNECTmethod):ASPNCookbookRecipe.
8

### 第9页

8 Sockets and Layers
ThePythonsupportforfetchingresourcesfromthewebislayered. urllibusesthehttp.clientlibrary,whichin
turnusesthesocketlibrary.
AsofPython2.3youcanspecifyhowlongasocketshouldwaitforaresponsebeforetimingout. Thiscanbeuseful
inapplicationswhichhavetofetchwebpages. Bydefaultthesocketmodulehasnotimeoutandcanhang. Currently,
thesockettimeoutisnotexposedatthehttp.clientorurllib.requestlevels. However,youcansetthedefaulttimeout
globallyforallsocketsusing
import socket
import urllib.request
# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)
# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.voidspace.org.uk')
response = urllib.request.urlopen(req)
9 Footnotes
ThisdocumentwasreviewedandrevisedbyJohnLee.
9

### 第10页

Index
R
RFC
RFC 2616,2,5
10

