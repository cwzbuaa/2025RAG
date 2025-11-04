### 第1页

An introduction to the ipaddress
module
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 CreatingAddress/Network/Interfaceobjects 1
1.1 ANoteonIPVersions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 IPHostAddresses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 DefiningNetworks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.4 HostInterfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 InspectingAddress/Network/InterfaceObjects 3
3 NetworksaslistsofAddresses 4
4 Comparisons 5
5 UsingIPAddresseswithothermodules 5
6 Gettingmoredetailwheninstancecreationfails 5
author
PeterMoody
author
NickCoghlan
Overview
Thisdocumentaimstoprovideagentleintroductiontotheipaddressmodule. Itisaimedprimarilyatusers
thataren’talreadyfamiliarwithIPnetworkingterminology,butmayalsobeusefultonetworkengineerswanting
anoverviewofhowipaddressrepresentsIPnetworkaddressingconcepts.
1 Creating Address/Network/Interface objects
SinceipaddressisamoduleforinspectingandmanipulatingIPaddresses,thefirstthingyou’llwanttodoiscreate
someobjects. Youcanuseipaddresstocreateobjectsfromstringsandintegers.
1

### 第2页

1.1 A Note on IP Versions
Forreadersthataren’tparticularlyfamiliarwithIPaddressing,it’simportanttoknowthattheInternetProtocol(IP)
iscurrentlyintheprocessofmovingfromversion4oftheprotocoltoversion6. Thistransitionisoccurringlargely
becauseversion4oftheprotocoldoesn’tprovideenoughaddressestohandletheneedsofthewholeworld,especially
giventheincreasingnumberofdeviceswithdirectconnectionstotheinternet.
Explainingthedetailsofthedifferencesbetweenthetwoversionsoftheprotocolisbeyondthescopeofthisintro-
duction, but readers need to at least be aware that these two versions exist, and it will sometimes be necessary to
forcetheuseofoneversionortheother.
1.2 IP Host Addresses
Addresses, often referred to as “host addresses” are the most basic unit when working with IP addressing. The
simplest way to create addresses is to use the ipaddress.ip_address() factory function, which automatically
determineswhethertocreateanIPv4orIPv6addressbasedonthepassedinvalue:
>>> ipaddress.ip_address('192.0.2.1')
IPv4Address('192.0.2.1')
>>> ipaddress.ip_address('2001:DB8::1')
IPv6Address('2001:db8::1')
Addresses can also be created directly from integers. Values that will fit within 32 bits are assumed to be IPv4
addresses:
>>> ipaddress.ip_address(3221225985)
IPv4Address('192.0.2.1')
>>> ipaddress.ip_address(42540766411282592856903984951653826561)
IPv6Address('2001:db8::1')
ToforcetheuseofIPv4orIPv6addresses,therelevantclassescanbeinvokeddirectly. Thisisparticularlyusefulto
forcecreationofIPv6addressesforsmallintegers:
>>> ipaddress.ip_address(1)
IPv4Address('0.0.0.1')
>>> ipaddress.IPv4Address(1)
IPv4Address('0.0.0.1')
>>> ipaddress.IPv6Address(1)
IPv6Address('::1')
1.3 Defining Networks
Host addresses are usually grouped together into IP networks, so ipaddress provides a way to create, inspect
and manipulate network definitions. IP network objects are constructed from strings that define the range of host
addressesthatarepartofthatnetwork. Thesimplestformforthatinformationisa“networkaddress/networkprefix”
pair,wheretheprefixdefinesthenumberofleadingbitsthatarecomparedtodeterminewhetherornotanaddress
ispartofthenetworkandthenetworkaddressdefinestheexpectedvalueofthosebits.
Asforaddresses,afactoryfunctionisprovidedthatdeterminesthecorrectIPversionautomatically:
>>> ipaddress.ip_network('192.0.2.0/24')
IPv4Network('192.0.2.0/24')
>>> ipaddress.ip_network('2001:db8::0/96')
IPv6Network('2001:db8::/96')
Networkobjectscannothaveanyhostbitsset. Thepracticaleffectofthisisthat192.0.2.1/24doesnotdescribe
anetwork. Suchdefinitionsarereferredtoasinterfaceobjectssincetheip-on-a-networknotationiscommonlyused
todescribenetworkinterfacesofacomputeronagivennetworkandaredescribedfurtherinthenextsection.
By default, attempting to create a network object with host bits set will result in ValueError being raised. To
requestthattheadditionalbitsinsteadbecoercedtozero,theflagstrict=Falsecanbepassedtotheconstructor:
2

### 第3页

>>> ipaddress.ip_network('192.0.2.1/24')
Traceback (most recent call last):
...
ValueError: 192.0.2.1/24 has host bits set
>>> ipaddress.ip_network('192.0.2.1/24', strict=False)
IPv4Network('192.0.2.0/24')
Whilethestringformofferssignificantlymoreflexibility,networkscanalsobedefinedwithintegers,justlikehost
addresses. Inthiscase,thenetworkisconsideredtocontainonlythesingleaddressidentifiedbytheinteger,sothe
networkprefixincludestheentirenetworkaddress:
>>> ipaddress.ip_network(3221225984)
IPv4Network('192.0.2.0/32')
>>> ipaddress.ip_network(42540766411282592856903984951653826560)
IPv6Network('2001:db8::/128')
As with addresses, creation of a particular kind of network can be forced by calling the class constructor directly
insteadofusingthefactoryfunction.
1.4 Host Interfaces
As mentioned just above, if you need to describe an address on a particular network, neither the address nor the
networkclassesaresufficient. Notationlike192.0.2.1/24iscommonlyusedbynetworkengineersandthepeople
whowritetoolsforfirewallsandroutersasshorthandfor“thehost192.0.2.1onthenetwork192.0.2.0/24”,
Accordingly,ipaddressprovidesasetofhybridclassesthatassociateanaddresswithaparticularnetwork. The
interfaceforcreationisidenticaltothatfordefiningnetworkobjects,exceptthattheaddressportionisn’tconstrained
tobeinganetworkaddress.
>>> ipaddress.ip_interface('192.0.2.1/24')
IPv4Interface('192.0.2.1/24')
>>> ipaddress.ip_interface('2001:db8::1/96')
IPv6Interface('2001:db8::1/96')
Integerinputsareaccepted(aswithnetworks),anduseofaparticularIPversioncanbeforcedbycallingtherelevant
constructordirectly.
2 Inspecting Address/Network/Interface Objects
You’vegonetothetroubleofcreatinganIPv(4|6)(Address|Network|Interface)object,soyouprobablywanttoget
informationaboutit. ipaddresstriestomakedoingthiseasyandintuitive.
ExtractingtheIPversion:
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> addr6 = ipaddress.ip_address('2001:db8::1')
>>> addr6.version
6
>>> addr4.version
4
Obtainingthenetworkfromaninterface:
>>> host4 = ipaddress.ip_interface('192.0.2.1/24')
>>> host4.network
IPv4Network('192.0.2.0/24')
>>> host6 = ipaddress.ip_interface('2001:db8::1/96')
>>> host6.network
IPv6Network('2001:db8::/96')
3

### 第4页

Findingouthowmanyindividualaddressesareinanetwork:
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> net4.num_addresses
256
>>> net6 = ipaddress.ip_network('2001:db8::0/96')
>>> net6.num_addresses
4294967296
Iteratingthroughthe“usable”addressesonanetwork:
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> for x in net4.hosts():
... print(x)
192.0.2.1
192.0.2.2
192.0.2.3
192.0.2.4
...
192.0.2.252
192.0.2.253
192.0.2.254
Obtainingthenetmask(i.e. setbitscorrespondingtothenetworkprefix)orthehostmask(anybitsthatarenotpart
ofthenetmask):
>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> net4.netmask
IPv4Address('255.255.255.0')
>>> net4.hostmask
IPv4Address('0.0.0.255')
>>> net6 = ipaddress.ip_network('2001:db8::0/96')
>>> net6.netmask
IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff::')
>>> net6.hostmask
IPv6Address('::ffff:ffff')
Explodingorcompressingtheaddress:
>>> addr6.exploded
'2001:0db8:0000:0000:0000:0000:0000:0001'
>>> addr6.compressed
'2001:db8::1'
>>> net6.exploded
'2001:0db8:0000:0000:0000:0000:0000:0000/96'
>>> net6.compressed
'2001:db8::/96'
WhileIPv4doesn’tsupportexplosionorcompression,theassociatedobjectsstillprovidetherelevantpropertiesso
thatversionneutralcodecaneasilyensurethemostconciseormostverboseformisusedforIPv6addresseswhile
stillcorrectlyhandlingIPv4addresses.
3 Networks as lists of Addresses
It’ssometimesusefultotreatnetworksaslists. Thismeansitispossibletoindexthemlikethis:
>>> net4[1]
IPv4Address('192.0.2.1')
(continuesonnextpage)
4

### 第5页

(continuedfrompreviouspage)
>>> net4[-1]
IPv4Address('192.0.2.255')
>>> net6[1]
IPv6Address('2001:db8::1')
>>> net6[-1]
IPv6Address('2001:db8::ffff:ffff')
Italsomeansthatnetworkobjectslendthemselvestousingthelistmembershiptestsyntaxlikethis:
if address in network:
# do something
Containmenttestingisdoneefficientlybasedonthenetworkprefix:
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> addr4 in ipaddress.ip_network('192.0.2.0/24')
True
>>> addr4 in ipaddress.ip_network('192.0.3.0/24')
False
4 Comparisons
ipaddressprovidessomesimple,hopefullyintuitivewaystocompareobjects,whereitmakessense:
>>> ipaddress.ip_address('192.0.2.1') < ipaddress.ip_address('192.0.2.2')
True
ATypeErrorexceptionisraisedifyoutrytocompareobjectsofdifferentversionsordifferenttypes.
5 Using IP Addresses with other modules
OthermodulesthatuseIPaddresses(suchassocket)usuallywon’tacceptobjectsfromthismoduledirectly. Instead,
theymustbecoercedtoanintegerorstringthattheothermodulewillaccept:
>>> addr4 = ipaddress.ip_address('192.0.2.1')
>>> str(addr4)
'192.0.2.1'
>>> int(addr4)
3221225985
6 Getting more detail when instance creation fails
When creating address/network/interface objects using the version-agnostic factory functions, any errors will be
reportedasValueErrorwithagenericerrormessagethatsimplysaysthepassedinvaluewasnotrecognizedasan
objectofthattype. Thelackofaspecificerrorisbecauseit’snecessarytoknowwhetherthevalueissupposedtobe
IPv4orIPv6inordertoprovidemoredetailonwhyithasbeenrejected.
Tosupportusecaseswhereitisusefultohaveaccesstothisadditionaldetail,theindividualclassconstructorsactually
raisetheValueErrorsubclassesipaddress.AddressValueErrorandipaddress.NetmaskValueErrorto
indicateexactlywhichpartofthedefinitionfailedtoparsecorrectly.
Theerrormessagesaresignificantlymoredetailedwhenusingtheclassconstructorsdirectly. Forexample:
>>> ipaddress.ip_address("192.168.0.256")
Traceback (most recent call last):
(continuesonnextpage)
5

### 第6页

(continuedfrompreviouspage)
...
ValueError: '192.168.0.256' does not appear to be an IPv4 or IPv6 address
>>> ipaddress.IPv4Address("192.168.0.256")
Traceback (most recent call last):
...
ipaddress.AddressValueError: Octet 256 (> 255) not permitted in '192.168.0.256'
>>> ipaddress.ip_network("192.168.0.1/64")
Traceback (most recent call last):
...
ValueError: '192.168.0.1/64' does not appear to be an IPv4 or IPv6 network
>>> ipaddress.IPv4Network("192.168.0.1/64")
Traceback (most recent call last):
...
ipaddress.NetmaskValueError: '64' is not a valid netmask
However,bothofthemodulespecificexceptionshaveValueErrorastheirparentclass,soifyou’renotconcerned
withtheparticulartypeoferror,youcanstillwritecodelikethefollowing:
try:
network = ipaddress.IPv4Network(address)
except ValueError:
print('address/netmask is invalid for IPv4:', address)
6

