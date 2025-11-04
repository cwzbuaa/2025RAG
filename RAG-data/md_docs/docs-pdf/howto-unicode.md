### 第1页

Unicode HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 IntroductiontoUnicode 1
1.1 Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Encodings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2 Python’sUnicodeSupport 3
2.1 TheStringType . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 ConvertingtoBytes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.3 UnicodeLiteralsinPythonSourceCode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4 UnicodeProperties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.5 ComparingStrings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.6 UnicodeRegularExpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.7 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 ReadingandWritingUnicodeData 8
3.1 Unicodefilenames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2 TipsforWritingUnicode-awarePrograms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4 Acknowledgements 11
Index 12
Release
1.12
This HOWTO discusses Python’s support for the Unicode specification for representing textual data, and explains
variousproblemsthatpeoplecommonlyencounterwhentryingtoworkwithUnicode.
1 Introduction to Unicode
1.1 Definitions
Today’sprogramsneedtobeabletohandleawidevarietyofcharacters. Applicationsareofteninternationalizedto
displaymessagesandoutputinavarietyofuser-selectablelanguages;thesameprogrammightneedtooutputanerror
messageinEnglish, French, Japanese, Hebrew, orRussian. Webcontentcanbewritteninanyoftheselanguages
1

### 第2页

and can also include a variety of emoji symbols. Python’s string type uses the Unicode Standard for representing
characters,whichletsPythonprogramsworkwithallthesedifferentpossiblecharacters.
Unicode(https://www.unicode.org/)isaspecificationthataimstolisteverycharacterusedbyhumanlanguagesand
giveeachcharacteritsownuniquecode. TheUnicodespecificationsarecontinuallyrevisedandupdatedtoaddnew
languagesandsymbols.
Acharacteristhesmallestpossiblecomponentofatext. ‘A’,‘B’,‘C’,etc.,arealldifferentcharacters. Soare‘È’and
‘I’́.Charactersvarydependingonthelanguageorcontextyou’retalkingabout. Forexample,there’sacharacterfor
“RomanNumeralOne”,‘Ⅰ’,that’sseparatefromtheuppercaseletter‘I’.They’llusuallylookthesame,buttheseare
twodifferentcharactersthathavedifferentmeanings.
TheUnicodestandarddescribeshowcharactersarerepresentedbycodepoints. Acodepointvalueisanintegerin
therange0to0x10FFFF(about1.1millionvalues,theactualnumberassignedislessthanthat). Inthestandardand
inthisdocument,acodepointiswrittenusingthenotationU+265Etomeanthecharacterwithvalue0x265e(9,822
indecimal).
TheUnicodestandardcontainsalotoftableslistingcharactersandtheircorrespondingcodepoints:
0061 'a'; LATIN SMALL LETTER A
0062 'b'; LATIN SMALL LETTER B
0063 'c'; LATIN SMALL LETTER C
...
007B '{'; LEFT CURLY BRACKET
...
2167 'Ⅷ'; ROMAN NUMERAL EIGHT
2168 'Ⅸ'; ROMAN NUMERAL NINE
...
265E '♞'; BLACK CHESS KNIGHT
265F '♟'; BLACK CHESS PAWN
...
1F600 '(cid:0)'; GRINNING FACE
1F609 '(cid:0)'; WINKING FACE
...
Strictly,thesedefinitionsimplythatit’smeaninglesstosay‘thisischaracterU+265E’.U+265Eisacodepoint,which
represents some particular character; in this case, it represents the character ‘BLACK CHESS KNIGHT’, ‘♞’. In
informalcontexts,thisdistinctionbetweencodepointsandcharacterswillsometimesbeforgotten.
Acharacterisrepresentedonascreenoronpaperbyasetofgraphicalelementsthat’scalledaglyph. Theglyphfor
anuppercaseA,forexample,istwodiagonalstrokesandahorizontalstroke,thoughtheexactdetailswilldependon
thefontbeingused. MostPythoncodedoesn’tneedtoworryaboutglyphs;figuringoutthecorrectglyphtodisplay
isgenerallythejobofaGUItoolkitoraterminal’sfontrenderer.
1.2 Encodings
Tosummarizetheprevioussection: aUnicodestringisasequenceofcodepoints,whicharenumbersfrom0through
0x10FFFF(1,114,111decimal). Thissequenceofcodepointsneedstoberepresentedinmemoryasasetofcode
units,andcodeunitsarethenmappedto8-bitbytes. TherulesfortranslatingaUnicodestringintoasequenceof
bytesarecalledacharacterencoding,orjustanencoding.
Thefirstencodingyoumightthinkofisusing32-bitintegersasthecodeunit,andthenusingtheCPU’srepresentation
of32-bitintegers. Inthisrepresentation,thestring“Python”mightlooklikethis:
P y t h o n
0x50 00 00 00 79 00 00 00 74 00 00 00 68 00 00 00 6f 00 00 00 6e 00 00 00
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
Thisrepresentationisstraightforwardbutusingitpresentsanumberofproblems.
1. It’snotportable;differentprocessorsorderthebytesdifferently.
2

### 第3页

2. It’sverywastefulofspace. Inmosttexts,themajorityofthecodepointsarelessthan127,orlessthan255,so
alotofspaceisoccupiedby0x00bytes. Theabovestringtakes24bytescomparedtothe6bytesneededfor
anASCIIrepresentation. IncreasedRAMusagedoesn’tmattertoomuch(desktopcomputershavegigabytes
ofRAM,andstringsaren’tusuallythatlarge),butexpandingourusageofdiskandnetworkbandwidthbya
factorof4isintolerable.
3. It’snotcompatiblewithexistingCfunctionssuchasstrlen(),soanewfamilyofwidestringfunctionswould
needtobeused.
Thereforethisencodingisn’tusedverymuch,andpeopleinsteadchooseotherencodingsthataremoreefficientand
convenient,suchasUTF-8.
UTF-8isoneofthemostcommonlyusedencodings,andPythonoftendefaultstousingit. UTFstandsfor“Unicode
TransformationFormat”,andthe‘8’meansthat8-bitvaluesareusedintheencoding. (TherearealsoUTF-16and
UTF-32encodings,buttheyarelessfrequentlyusedthanUTF-8.) UTF-8usesthefollowingrules:
1. Ifthecodepointis<128,it’srepresentedbythecorrespondingbytevalue.
2. If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes, where each byte of the
sequenceisbetween128and255.
UTF-8hasseveralconvenientproperties:
1. ItcanhandleanyUnicodecodepoint.
2. AUnicodestringisturnedintoasequenceofbytesthatcontainsembeddedzerobytesonlywheretheyrepresent
thenullcharacter(U+0000). ThismeansthatUTF-8stringscanbeprocessedbyCfunctionssuchasstrcpy()
andsentthroughprotocolsthatcan’thandlezerobytesforanythingotherthanend-of-stringmarkers.
3. AstringofASCIItextisalsovalidUTF-8text.
4. UTF-8isfairlycompact;themajorityofcommonlyusedcharacterscanberepresentedwithoneortwobytes.
5. Ifbytesarecorruptedorlost,it’spossibletodeterminethestartofthenextUTF-8-encodedcodepointand
resynchronize. It’salsounlikelythatrandom8-bitdatawilllooklikevalidUTF-8.
6. UTF-8 is a byte oriented encoding. The encoding specifies that each character is represented by a specific
sequence of one or more bytes. This avoids the byte-ordering issues that can occur with integer and word
orientedencodings,likeUTF-16andUTF-32,wherethesequenceofbytesvariesdependingonthehardware
onwhichthestringwasencoded.
1.3 References
The Unicode Consortium site has character charts, a glossary, and PDF versions of the Unicode specification. Be
preparedforsomedifficultreading. AchronologyoftheoriginanddevelopmentofUnicodeisalsoavailableonthe
site.
OntheComputerphileYoutubechannel,TomScottbrieflydiscussesthehistoryofUnicodeandUTF-8(9minutes
36seconds).
Tohelpunderstandthestandard,JukkaKorpelahaswrittenanintroductoryguidetoreadingtheUnicodecharacter
tables.
AnothergoodintroductoryarticlewaswrittenbyJoelSpolsky. Ifthisintroductiondidn’tmakethingscleartoyou,
youshouldtryreadingthisalternatearticlebeforecontinuing.
Wikipediaentriesareoftenhelpful;seetheentriesfor“characterencoding”andUTF-8,forexample.
2 Python’s Unicode Support
Nowthatyou’velearnedtherudimentsofUnicode,wecanlookatPython’sUnicodefeatures.
3

### 第4页

2.1 The String Type
SincePython3.0,thelanguage’sstrtypecontainsUnicodecharacters,meaninganystringcreatedusing"unicode
rocks!",'unicode rocks!',orthetriple-quotedstringsyntaxisstoredasUnicode.
ThedefaultencodingforPythonsourcecodeisUTF-8, soyoucansimplyincludeaUnicodecharacterinastring
literal:
try:
with open('/tmp/input.txt', 'r') as f:
...
except OSError:
# 'File not found' error message.
print("Fichier non trouvé")
Sidenote: Python3alsosupportsusingUnicodecharactersinidentifiers:
répertoire = "/tmp/records.log"
with open(répertoire, "w") as f:
f.write("test\n")
Ifyoucan’tenteraparticularcharacterinyoureditororwanttokeepthesourcecodeASCII-onlyforsomereason,
youcanalsouseescapesequencesinstringliterals. (Dependingonyoursystem,youmayseetheactualcapital-delta
glyphinsteadofauescape.)
>>> "\N{GREEK CAPITAL LETTER DELTA}" # Using the character name
'\u0394'
>>> "\u0394" # Using a 16-bit hex value
'\u0394'
>>> "\U00000394" # Using a 32-bit hex value
'\u0394'
Inaddition,onecancreateastringusingthedecode()methodofbytes. Thismethodtakesanencodingargument,
suchasUTF-8,andoptionallyanerrorsargument.
The errors argument specifies the response when the input string can’t be converted according to the encoding’s
rules. Legal values for this argument are 'strict' (raise a UnicodeDecodeError exception), 'replace'
(use U+FFFD, REPLACEMENT CHARACTER), 'ignore' (just leave the character out of the Unicode result), or
'backslashreplace'(insertsa\xNNescapesequence). Thefollowingexamplesshowthedifferences:
>>> b'\x80abc'.decode("utf-8", "strict")
Traceback (most recent call last):
...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0:
invalid start byte
>>> b'\x80abc'.decode("utf-8", "replace")
'\ufffdabc'
>>> b'\x80abc'.decode("utf-8", "backslashreplace")
'\\x80abc'
>>> b'\x80abc'.decode("utf-8", "ignore")
'abc'
Encodingsarespecifiedasstringscontainingtheencoding’sname. Pythoncomeswithroughly100differentencod-
ings; seethePythonLibraryReferenceatstandard-encodingsforalist. Someencodingshavemultiplenames; for
example,'latin-1','iso_8859_1'and'8859’areallsynonymsforthesameencoding.
One-characterUnicodestringscanalsobecreatedwiththechr()built-infunction,whichtakesintegersandreturns
aUnicodestringoflength1thatcontainsthecorrespondingcodepoint. Thereverseoperationisthebuilt-inord()
functionthattakesaone-characterUnicodestringandreturnsthecodepointvalue:
4

### 第5页

>>> chr(57344)
'\ue000'
>>> ord('\ue000')
57344
2.2 Converting to Bytes
Theoppositemethodofbytes.decode()isstr.encode(),whichreturnsabytesrepresentationoftheUnicode
string,encodedintherequestedencoding.
The errors parameter is the same as the parameter of the decode() method but supports a few more possible
handlers. As well as 'strict', 'ignore', and 'replace' (which in this case inserts a question mark in-
steadoftheunencodablecharacter),thereisalso'xmlcharrefreplace'(insertsanXMLcharacterreference),
backslashreplace(insertsa\uNNNNescapesequence)andnamereplace(insertsa\N{...}escapesequence).
Thefollowingexampleshowsthedifferentresults:
>>> u = chr(40960) + 'abcd' + chr(1972)
>>> u.encode('utf-8')
b'\xea\x80\x80abcd\xde\xb4'
>>> u.encode('ascii')
Traceback (most recent call last):
...
UnicodeEncodeError: 'ascii' codec can't encode character '\ua000' in
position 0: ordinal not in range(128)
>>> u.encode('ascii', 'ignore')
b'abcd'
>>> u.encode('ascii', 'replace')
b'?abcd?'
>>> u.encode('ascii', 'xmlcharrefreplace')
b'&#40960;abcd&#1972;'
>>> u.encode('ascii', 'backslashreplace')
b'\\ua000abcd\\u07b4'
>>> u.encode('ascii', 'namereplace')
b'\\N{YI SYLLABLE IT}abcd\\u07b4'
Thelow-levelroutinesforregisteringandaccessingtheavailableencodingsarefoundinthecodecsmodule. Im-
plementingnewencodingsalsorequiresunderstandingthecodecsmodule. However, theencodinganddecoding
functions returned by this module are usually more low-level than is comfortable, and writing new encodings is a
specializedtask,sothemodulewon’tbecoveredinthisHOWTO.
2.3 Unicode Literals in Python Source Code
InPythonsourcecode,specificUnicodecodepointscanbewrittenusingthe\uescapesequence,whichisfollowed
byfourhexdigitsgivingthecodepoint. The\Uescapesequenceissimilar,butexpectseighthexdigits,notfour:
>>> s = "a\xac\u1234\u20ac\U00008000"
... # ^^^^ two-digit hex escape
... # ^^^^^^ four-digit Unicode escape
... # ^^^^^^^^^^ eight-digit Unicode escape
>>> [ord(c) for c in s]
[97, 172, 4660, 8364, 32768]
Usingescapesequencesforcodepointsgreaterthan127isfineinsmalldoses,butbecomesanannoyanceifyou’re
using many accented characters, as you would in a program with messages in French or some other accent-using
language. Youcanalsoassemblestringsusingthechr()built-infunction,butthisisevenmoretedious.
Ideally,you’dwanttobeabletowriteliteralsinyourlanguage’snaturalencoding. YoucouldtheneditPythonsource
codewithyourfavoriteeditorwhichwoulddisplaytheaccentedcharactersnaturally,andhavetherightcharacters
5

### 第6页

usedatruntime.
PythonsupportswritingsourcecodeinUTF-8bydefault, butyoucanusealmostanyencodingifyoudeclarethe
encodingbeingused. Thisisdonebyincludingaspecialcommentaseitherthefirstorsecondlineofthesourcefile:
#!/usr/bin/env python
# -*- coding: latin-1 -*-
u = 'abcdé'
print(ord(u[-1]))
The syntax is inspired by Emacs’s notation for specifying variables local to a file. Emacs supports many different
variables,butPythononlysupports‘coding’. The-*-symbolsindicatetoEmacsthatthecommentisspecial;they
have no significance to Python but are a convention. Python looks for coding: name or coding=name in the
comment.
Ifyoudon’tincludesuchacomment,thedefaultencodingusedwillbeUTF-8asalreadymentioned. SeealsoPEP
263formoreinformation.
2.4 Unicode Properties
TheUnicodespecificationincludesadatabaseofinformationaboutcodepoints. Foreachdefinedcodepoint, the
informationincludesthecharacter’sname,itscategory,thenumericvalueifapplicable(forcharactersrepresenting
numeric concepts such as the Roman numerals, fractions such as one-third and four-fifths, etc.). There are also
display-relatedproperties,suchashowtousethecodepointinbidirectionaltext.
The following program displays some information about several characters, and prints the numeric value of one
particularcharacter:
import unicodedata
u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)
for i, c in enumerate(u):
print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
print(unicodedata.name(c))
# Get numeric value of second character
print(unicodedata.numeric(u[1]))
Whenrun,thisprints:
0 00e9 Ll LATIN SMALL LETTER E WITH ACUTE
1 0bf2 No TAMIL NUMBER ONE THOUSAND
2 0f84 Mn TIBETAN MARK HALANTA
3 1770 Lo TAGBANWA LETTER SA
4 33af So SQUARE RAD OVER S SQUARED
1000.0
The category codes are abbreviations describing the nature of the character. These are grouped into categories
such as “Letter”, “Number”, “Punctuation”, or “Symbol”, which in turn are broken up into subcategories. To take
the codes from the above output, 'Ll' means ‘Letter, lowercase’, 'No' means “Number, other”, 'Mn' is “Mark,
nonspacing”, and 'So' is “Symbol, other”. See the General Category Values section of the Unicode Character
Databasedocumentationforalistofcategorycodes.
2.5 Comparing Strings
Unicode adds some complication to comparing strings, because the same set of characters can be represented by
differentsequencesofcodepoints. Forexample,aletterlike‘ê’canberepresentedasasinglecodepointU+00EA,
orasU+0065U+0302,whichisthecodepointfor‘e’followedbyacodepointfor‘COMBININGCIRCUMFLEX
6

### 第7页

ACCENT’.Thesewillproducethesameoutputwhenprinted,butoneisastringoflength1andtheotherisoflength
2.
One tool for a case-insensitive comparison is the casefold() string method that converts a string to a case-
insensitive form following an algorithm described by the Unicode Standard. This algorithm has special handling
forcharacterssuchastheGermanletter‘ß’(codepointU+00DF),whichbecomesthepairoflowercaseletters‘ss’.
>>> street = 'Gürzenichstraße'
>>> street.casefold()
'gürzenichstrasse'
Asecondtoolistheunicodedatamodule’snormalize()functionthatconvertsstringstooneofseveralnormal
forms, where letters followed by a combining character are replaced with single characters. normalize() can
be used to perform string comparisons that won’t falsely report inequality if two strings use combining characters
differently:
import unicodedata
def compare_strs(s1, s2):
def NFD(s):
return unicodedata.normalize('NFD', s)
return NFD(s1) == NFD(s2)
single_char = 'ê'
multiple_chars = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print('length of first string=', len(single_char))
print('length of second string=', len(multiple_chars))
print(compare_strs(single_char, multiple_chars))
Whenrun,thisoutputs:
$ python compare-strs.py
length of first string= 1
length of second string= 2
True
Thefirstargumenttothenormalize()functionisastringgivingthedesirednormalizationform,whichcanbeone
of‘NFC’,‘NFKC’,‘NFD’,and‘NFKD’.
TheUnicodeStandardalsospecifieshowtodocaselesscomparisons:
import unicodedata
def compare_caseless(s1, s2):
def NFD(s):
return unicodedata.normalize('NFD', s)
return NFD(NFD(s1).casefold()) == NFD(NFD(s2).casefold())
# Example usage
single_char = 'ê'
multiple_chars = '\N{LATIN CAPITAL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print(compare_caseless(single_char, multiple_chars))
ThiswillprintTrue. (WhyisNFD()invokedtwice? Becausethereareafewcharactersthatmakecasefold()
returnanon-normalizedstring,sotheresultneedstobenormalizedagain. Seesection3.13oftheUnicodeStandard
foradiscussionandanexample.)
7

### 第8页

2.6 Unicode Regular Expressions
Theregularexpressionssupportedbytheremodulecanbeprovidedeitherasbytesorstrings. Someofthespecial
charactersequencessuchas\dand\whavedifferentmeaningsdependingonwhetherthepatternissuppliedasbytes
orastring. Forexample,\dwillmatchthecharacters[0-9]inbytesbutinstringswillmatchanycharacterthat’s
inthe'Nd'category.
Thestringinthisexamplehasthenumber57writteninbothThaiandArabicnumerals:
import re
p = re.compile(r'\d+')
s = "Over \u0e55\u0e57 57 flavours"
m = p.search(s)
print(repr(m.group()))
When executed, \d+ will match the Thai numerals and print them out. If you supply the re.ASCII flag to
compile(),\d+willmatchthesubstring“57”instead.
Similarly, \w matches a wide variety of Unicode characters but only [a-zA-Z0-9_] in bytes or if re.ASCII is
supplied,and\swillmatcheitherUnicodewhitespacecharactersor[ \t\n\r\f\v].
2.7 References
SomegoodalternativediscussionsofPython’sUnicodesupportare:
• ProcessingTextFilesinPython3,byNickCoghlan.
• PragmaticUnicode,aPyCon2012presentationbyNedBatchelder.
ThestrtypeisdescribedinthePythonlibraryreferenceattextseq.
Thedocumentationfortheunicodedatamodule.
Thedocumentationforthecodecsmodule.
Marc-AndréLemburggaveapresentationtitled“PythonandUnicode”(PDFslides)atEuroPython2002. Theslides
are an excellent overview of the design of Python 2’s Unicode features (where the Unicode string type is called
unicodeandliteralsstartwithu).
3 Reading and Writing Unicode Data
Once you’ve written some code that works with Unicode data, the next problem is input/output. How do you get
Unicodestringsintoyourprogram,andhowdoyouconvertUnicodeintoaformsuitableforstorageortransmission?
It’spossiblethatyoumaynotneedtodoanythingdependingonyourinputsourcesandoutputdestinations;youshould
checkwhetherthelibrariesusedinyourapplicationsupportUnicodenatively. XMLparsersoftenreturnUnicode
data,forexample. ManyrelationaldatabasesalsosupportUnicode-valuedcolumnsandcanreturnUnicodevalues
fromanSQLquery.
Unicode data is usually converted to a particular encoding before it gets written to disk or sent over a socket. It’s
possibletodoalltheworkyourself: openafile,readan8-bitbytesobjectfromit,andconvertthebyteswithbytes.
decode(encoding). However,themanualapproachisnotrecommended.
Oneproblemisthemulti-bytenatureofencodings; oneUnicodecharactercanberepresentedbyseveralbytes. If
youwanttoreadthefileinarbitrary-sizedchunks(say,1024or4096bytes),youneedtowriteerror-handlingcode
tocatchthecasewhereonlypartofthebytesencodingasingleUnicodecharacterarereadattheendofachunk.
Onesolutionwouldbetoreadtheentirefileintomemoryandthenperformthedecoding,butthatpreventsyoufrom
workingwithfilesthatareextremelylarge;ifyouneedtoreada2GiBfile,youneed2GiBofRAM.(More,really,
sinceforatleastamomentyou’dneedtohaveboththeencodedstringanditsUnicodeversioninmemory.)
Thesolutionwouldbetousethelow-leveldecodinginterfacetocatchthecaseofpartialcodingsequences. Thework
ofimplementingthishasalreadybeendoneforyou: thebuilt-inopen()functioncanreturnafile-likeobjectthat
assumesthefile’scontentsareinaspecifiedencodingandacceptsUnicodeparametersformethodssuchasread()
8

### 第9页

andwrite(). Thisworksthroughopen()’sencodinganderrorsparameterswhichareinterpretedjustlikethosein
str.encode()andbytes.decode().
ReadingUnicodefromafileisthereforesimple:
with open('unicode.txt', encoding='utf-8') as f:
for line in f:
print(repr(line))
It’salsopossibletoopenfilesinupdatemode,allowingbothreadingandwriting:
with open('test', encoding='utf-8', mode='w+') as f:
f.write('\u4500 blah blah blah\n')
f.seek(0)
print(repr(f.readline()[:1]))
TheUnicodecharacterU+FEFFisusedasabyte-ordermark(BOM),andisoftenwrittenasthefirstcharacterofa
fileinordertoassistwithautodetectionofthefile’sbyteordering. Someencodings,suchasUTF-16,expectaBOM
tobepresentatthestartofafile;whensuchanencodingisused,theBOMwillbeautomaticallywrittenasthefirst
characterandwillbesilentlydroppedwhenthefileisread. Therearevariantsoftheseencodings,suchas‘utf-16-le’
and‘utf-16-be’forlittle-endianandbig-endianencodings,thatspecifyoneparticularbyteorderinganddon’tskipthe
BOM.
Insomeareas,itisalsoconventiontousea“BOM”atthestartofUTF-8encodedfiles;thenameismisleadingsince
UTF-8isnotbyte-orderdependent. ThemarksimplyannouncesthatthefileisencodedinUTF-8. Forreadingsuch
files,usethe‘utf-8-sig’codectoautomaticallyskipthemarkifpresent.
3.1 Unicode filenames
Most of the operating systems in common use today support filenames that contain arbitrary Unicode characters.
UsuallythisisimplementedbyconvertingtheUnicodestringintosomeencodingthatvariesdependingonthesystem.
TodayPythonisconvergingonusingUTF-8: PythononMacOShasusedUTF-8forseveralversions,andPython3.6
switchedtousingUTF-8onWindowsaswell. OnUnixsystems,therewillonlybeafilesystemencoding. ifyou’ve
settheLANGorLC_CTYPEenvironmentvariables;ifyouhaven’t,thedefaultencodingisagainUTF-8.
Thesys.getfilesystemencoding()functionreturnstheencodingtouseonyourcurrentsystem,incaseyou
wanttodotheencodingmanually,butthere’snotmuchreasontobother. Whenopeningafileforreadingorwriting,
youcanusuallyjustprovidetheUnicodestringasthefilename, anditwillbeautomaticallyconvertedtotheright
encodingforyou:
filename = 'filename\u4500abc'
with open(filename, 'w') as f:
f.write('blah\n')
Functionsintheosmodulesuchasos.stat()willalsoacceptUnicodefilenames.
Theos.listdir()functionreturnsfilenames,whichraisesanissue: shoulditreturntheUnicodeversionoffile-
names,orshoulditreturnbytescontainingtheencodedversions? os.listdir()candoboth,dependingonwhether
youprovidedthedirectorypathasbytesoraUnicodestring. IfyoupassaUnicodestringasthepath,filenameswill
bedecodedusingthefilesystem’sencodingandalistofUnicodestringswillbereturned,whilepassingabytepath
will return the filenames as bytes. For example, assuming the default filesystem encoding is UTF-8, running the
followingprogram:
fn = 'filename\u4500abc'
f = open(fn, 'w')
f.close()
import os
print(os.listdir(b'.'))
print(os.listdir('.'))
9

### 第10页

willproducethefollowingoutput:
$ python listdir-test.py
[b'filename\xe4\x94\x80abc', ...]
['filename\u4500abc', ...]
ThefirstlistcontainsUTF-8-encodedfilenames,andthesecondlistcontainstheUnicodeversions.
Notethatonmostoccasions,youshouldcanjuststickwithusingUnicodewiththeseAPIs. ThebytesAPIsshould
onlybeusedonsystemswhereundecodablefilenamescanbepresent;that’sprettymuchonlyUnixsystemsnow.
3.2 Tips for Writing Unicode-aware Programs
ThissectionprovidessomesuggestionsonwritingsoftwarethatdealswithUnicode.
Themostimportanttipis:
SoftwareshouldonlyworkwithUnicodestringsinternally,decodingtheinputdataassoonaspossible
andencodingtheoutputonlyattheend.
IfyouattempttowriteprocessingfunctionsthatacceptbothUnicodeandbytestrings,youwillfindyourprogram
vulnerable to bugs wherever you combine the two different kinds of strings. There is no automatic encoding or
decoding: ifyoudoe.g. str + bytes,aTypeErrorwillberaised.
Whenusingdatacomingfromawebbrowserorsomeotheruntrustedsource,acommontechniqueistocheckfor
illegalcharactersinastringbeforeusingthestringinageneratedcommandlineorstoringitinadatabase. Ifyou’re
doingthis,becarefultocheckthedecodedstring,nottheencodedbytesdata;someencodingsmayhaveinteresting
properties,suchasnotbeingbijectiveornotbeingfullyASCII-compatible. Thisisespeciallytrueiftheinputdata
also specifies the encoding, since the attacker can then choose a clever way to hide malicious text in the encoded
bytestream.
ConvertingBetweenFileEncodings
TheStreamRecoderclasscantransparentlyconvertbetweenencodings,takingastreamthatreturnsdatainencod-
ing#1andbehavinglikeastreamreturningdatainencoding#2.
Forexample, ifyouhaveaninputfilef that’sinLatin-1, youcanwrapitwithaStreamRecodertoreturnbytes
encodedinUTF-8:
new_f = codecs.StreamRecoder(f,
# en/decoder: used by read() to encode its results and
# by write() to decode its input.
codecs.getencoder('utf-8'), codecs.getdecoder('utf-8'),
# reader/writer: used to read and write to the stream.
codecs.getreader('latin-1'), codecs.getwriter('latin-1') )
FilesinanUnknownEncoding
What can you do if you need to make a change to a file, but don’t know the file’s encoding? If you know the
encodingisASCII-compatibleandonlywanttoexamineormodifytheASCIIparts,youcanopenthefilewiththe
surrogateescapeerrorhandler:
with open(fname, 'r', encoding="ascii", errors="surrogateescape") as f:
data = f.read()
# make changes to the string 'data'
with open(fname + '.new', 'w',
encoding="ascii", errors="surrogateescape") as f:
f.write(data)
10

### 第11页

Thesurrogateescapeerrorhandlerwilldecodeanynon-ASCIIbytesascodepointsinaspecialrangerunning
fromU+DC80toU+DCFF.Thesecodepointswillthenturnbackintothesamebyteswhenthesurrogateescape
errorhandlerisusedtoencodethedataandwriteitbackout.
3.3 References
OnesectionofMasteringPython3Input/Output,aPyCon2010talkbyDavidBeazley,discussestextprocessingand
binarydatahandling.
The PDF slides for Marc-André Lemburg’s presentation “Writing Unicode-aware Applications in Python” discuss
questionsofcharacterencodingsas wellas howto internationalizeandlocalizean application. Theseslidescover
Python2.xonly.
The Guts of Unicode in Python is a PyCon 2013 talk by Benjamin Peterson that discusses the internal Unicode
representationinPython3.3.
4 Acknowledgements
TheinitialdraftofthisdocumentwaswrittenbyAndrewKuchling. IthassincebeenrevisedfurtherbyAlexander
Belopolsky,GeorgBrandl,AndrewKuchling,andEzioMelotti.
Thankstothefollowingpeoplewhohavenotederrorsorofferedsuggestionsonthisarticle: ÉricAraujo,Nicholas
Bastin, Nick Coghlan, Marius Gedminas, Kent Johnson, Ken Krugler, Marc-André Lemburg, Martin von Löwis,
TerryJ.Reedy,SerhiyStorchaka,ErykSun,ChadWhitacre,GrahamWideman.
11

### 第12页

Index
P
Python Enhancement Proposals
PEP 263,6
12

