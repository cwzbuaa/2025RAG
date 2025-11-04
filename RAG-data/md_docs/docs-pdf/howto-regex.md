### 第1页

Regular Expression HOWTO
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Introduction 2
2 SimplePatterns 2
2.1 MatchingCharacters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 RepeatingThings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
3 UsingRegularExpressions 4
3.1 CompilingRegularExpressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 TheBackslashPlague . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3 PerformingMatches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.4 Module-LevelFunctions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.5 CompilationFlags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4 MorePatternPower 9
4.1 MoreMetacharacters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.2 Grouping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
4.3 Non-capturingandNamedGroups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.4 LookaheadAssertions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
5 ModifyingStrings 14
5.1 SplittingStrings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
5.2 SearchandReplace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
6 CommonProblems 16
6.1 UseStringMethods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.2 match()versussearch() . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.3 GreedyversusNon-Greedy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.4 Usingre.VERBOSE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
7 Feedback 18
Author
A.M.Kuchling<amk@amk.ca>
1

### 第2页

Abstract
ThisdocumentisanintroductorytutorialtousingregularexpressionsinPythonwiththeremodule. Itprovides
agentlerintroductionthanthecorrespondingsectionintheLibraryReference.
1 Introduction
Regularexpressions(calledREs,orregexes,orregexpatterns)areessentiallyatiny,highlyspecializedprogramming
languageembeddedinsidePythonandmadeavailablethroughtheremodule. Usingthislittlelanguage,youspecify
therulesforthesetofpossiblestringsthatyouwantto match; thissetmightcontainEnglishsentences, ore-mail
addresses,orTeXcommands,oranythingyoulike. Youcanthenaskquestionssuchas“Doesthisstringmatchthe
pattern?”,or“Isthereamatchforthepatternanywhereinthisstring?”. YoucanalsouseREstomodifyastringor
tosplititapartinvariousways.
Regularexpressionpatternsarecompiledintoaseriesofbytecodeswhicharethenexecutedbyamatchingengine
writteninC.Foradvanceduse,itmaybenecessarytopaycarefulattentiontohowtheenginewillexecuteagiven
RE,andwritetheREinacertainwayinordertoproducebytecodethatrunsfaster. Optimizationisn’tcoveredin
thisdocument,becauseitrequiresthatyouhaveagoodunderstandingofthematchingengine’sinternals.
Theregularexpressionlanguageisrelativelysmallandrestricted,sonotallpossiblestringprocessingtaskscanbe
doneusingregularexpressions. Therearealsotasksthatcanbedonewithregularexpressions,buttheexpressions
turnouttobeverycomplicated. Inthesecases,youmaybebetteroffwritingPythoncodetodotheprocessing;while
Pythoncodewillbeslowerthananelaborateregularexpression,itwillalsoprobablybemoreunderstandable.
2 Simple Patterns
We’llstartbylearningaboutthesimplestpossibleregularexpressions. Sinceregularexpressionsareusedtooperate
onstrings,we’llbeginwiththemostcommontask: matchingcharacters.
For a detailed explanation of the computer science underlying regular expressions (deterministic and non-
deterministicfiniteautomata),youcanrefertoalmostanytextbookonwritingcompilers.
2.1 Matching Characters
Mostlettersandcharacterswillsimplymatchthemselves. Forexample,theregularexpressiontestwillmatchthe
stringtestexactly. (Youcanenableacase-insensitivemodethatwouldletthisREmatchTestorTESTaswell;
moreaboutthislater.)
Thereareexceptionstothisrule;somecharactersarespecialmetacharacters,anddon’tmatchthemselves. Instead,
theysignalthatsomeout-of-the-ordinarythingshouldbematched,ortheyaffectotherportionsoftheREbyrepeating
themorchangingtheirmeaning. Muchofthisdocumentisdevotedtodiscussingvariousmetacharactersandwhat
theydo.
Here’sacompletelistofthemetacharacters;theirmeaningswillbediscussedintherestofthisHOWTO.
. ^ $ * + ? { } [ ] \ | ( )
The first metacharacters we’ll look at are [ and ]. They’re used for specifying a character class, which is a set of
charactersthatyouwishtomatch. Characterscanbelistedindividually,orarangeofcharacterscanbeindicatedby
givingtwocharactersandseparatingthembya'-'. Forexample,[abc]willmatchanyofthecharactersa,b,or
c;thisisthesameas[a-c],whichusesarangetoexpressthesamesetofcharacters. Ifyouwantedtomatchonly
lowercaseletters,yourREwouldbe[a-z].
Metacharacters(except\)arenotactiveinsideclasses. Forexample,[akm$]willmatchanyofthecharacters'a',
'k','m',or'$';'$'isusuallyametacharacter,butinsideacharacterclassit’sstrippedofitsspecialnature.
Youcanmatchthecharactersnotlistedwithintheclassbycomplementingtheset. Thisisindicatedbyincludinga
'^'asthefirstcharacteroftheclass. Forexample,[^5]willmatchanycharacterexcept'5'. Ifthecaretappears
elsewhereinacharacterclass, itdoesnothavespecialmeaning. Forexample: [5^]willmatcheithera'5'ora
'^'.
2

### 第3页

Perhaps the most important metacharacter is the backslash, \. As in Python string literals, the backslash can be
followed by various characters to signal various special sequences. It’s also used to escape all the metacharacters
so you canstill matchthem inpatterns; for example, if you needto matcha [ or \, you canprecede themwith a
backslashtoremovetheirspecialmeaning: \[or\\.
Someofthespecialsequencesbeginningwith'\'representpredefinedsetsofcharactersthatareoftenuseful,such
asthesetofdigits,thesetofletters,orthesetofanythingthatisn’twhitespace.
Let’s take an example: \w matches any alphanumeric character. If the regex pattern is expressed in bytes, this is
equivalenttotheclass[a-zA-Z0-9_]. Iftheregexpatternisastring,\wwillmatchallthecharactersmarkedas
lettersintheUnicodedatabaseprovidedbytheunicodedatamodule. Youcanusethemorerestricteddefinition
of\winastringpatternbysupplyingthere.ASCIIflagwhencompilingtheregularexpression.
Thefollowinglistofspecialsequencesisn’tcomplete. Foracompletelistofsequencesandexpandedclassdefinitions
for Unicode string patterns, see the last part of Regular Expression Syntax in the Standard Library reference. In
general,theUnicodeversionsmatchanycharacterthat’sintheappropriatecategoryintheUnicodedatabase.
\d
Matchesanydecimaldigit;thisisequivalenttotheclass[0-9].
\D
Matchesanynon-digitcharacter;thisisequivalenttotheclass[^0-9].
\s
Matchesanywhitespacecharacter;thisisequivalenttotheclass[ \t\n\r\f\v].
\S
Matchesanynon-whitespacecharacter;thisisequivalenttotheclass[^ \t\n\r\f\v].
\w
Matchesanyalphanumericcharacter;thisisequivalenttotheclass[a-zA-Z0-9_].
\W
Matchesanynon-alphanumericcharacter;thisisequivalenttotheclass[^a-zA-Z0-9_].
Thesesequencescanbeincludedinsideacharacterclass. Forexample,[\s,.]isacharacterclassthatwillmatch
anywhitespacecharacter,or','or'.'.
Thefinalmetacharacterinthissectionis.. Itmatchesanythingexceptanewlinecharacter,andthere’sanalternate
mode(re.DOTALL)whereitwillmatchevenanewline. . isoftenusedwhereyouwanttomatch“anycharacter”.
2.2 Repeating Things
Beingabletomatchvaryingsetsofcharactersisthefirstthingregularexpressionscandothatisn’talreadypossible
withthemethodsavailableonstrings. However,ifthatwastheonlyadditionalcapabilityofregexes,theywouldn’t
bemuchofanadvance. AnothercapabilityisthatyoucanspecifythatportionsoftheREmustberepeatedacertain
numberoftimes.
Thefirstmetacharacterforrepeatingthingsthatwe’lllookatis*. *doesn’tmatchtheliteralcharacter'*';instead,
itspecifiesthatthepreviouscharactercanbematchedzeroormoretimes,insteadofexactlyonce.
Forexample,ca*twillmatch'ct'(0'a'characters),'cat'(1'a'),'caaat'(3'a'characters),andsoforth.
Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as
possible. Iflaterportionsofthepatterndon’tmatch,thematchingenginewillthenbackupandtryagainwithfewer
repetitions.
A step-by-step example will make this more obvious. Let’s consider the expression a[bcd]*b. This matches the
letter'a',zeroormorelettersfromtheclass[bcd],andfinallyendswitha'b'. NowimaginematchingthisRE
againstthestring'abcbd'.
3

### 第4页

Step Matched Explanation
1 a TheaintheREmatches.
2 abcbd Theenginematches[bcd]*,goingasfarasitcan,whichistotheendofthestring.
3 Failure Theenginetriestomatchb,butthecurrentpositionisattheendofthestring,soitfails.
4 abcb Backup,sothat[bcd]*matchesonelesscharacter.
5 Failure Trybagain,butthecurrentpositionisatthelastcharacter,whichisa'd'.
6 abc Backupagain,sothat[bcd]*isonlymatchingbc.
6 abcb Trybagain. Thistimethecharacteratthecurrentpositionis'b',soitsucceeds.
TheendoftheREhasnowbeenreached,andithasmatched'abcb'. Thisdemonstrateshowthematchingengine
goesasfarasitcanatfirst,andifnomatchisfounditwillthenprogressivelybackupandretrytherestoftheRE
againandagain. Itwillbackupuntilithastriedzeromatchesfor[bcd]*,andifthatsubsequentlyfails,theengine
willconcludethatthestringdoesn’tmatchtheREatall.
Another repeating metacharacter is +, which matches one or more times. Pay careful attention to the difference
between * and +; * matches zero or more times, so whatever’s being repeated may not be present at all, while +
requiresatleastoneoccurrence. Touseasimilarexample,ca+twillmatch'cat'(1'a'),'caaat'(3'a's),but
won’tmatch'ct'.
There are two more repeating operators or quantifiers. The question mark character, ?, matches either once or
zerotimes;youcanthinkofitasmarkingsomethingasbeingoptional. Forexample,home-?brewmatcheseither
'homebrew'or'home-brew'.
Themostcomplicatedquantifieris{m,n},wheremandnaredecimalintegers. Thisquantifiermeanstheremustbe
atleastmrepetitions,andatmostn. Forexample,a/{1,3}bwillmatch'a/b','a//b',and'a///b'. Itwon’t
match'ab',whichhasnoslashes,or'a////b',whichhasfour.
Youcanomiteithermorn;inthatcase,areasonablevalueisassumedforthemissingvalue. Omittingmisinterpreted
asalowerlimitof0,whileomittingnresultsinanupperboundofinfinity.
Thesimplestcase{m}matchestheprecedingitemexactlymtimes. Forexample,a/{2}bwillonlymatch'a//b'.
Readers of a reductionist bent may notice that the three other quantifiers can all be expressed using this notation.
{0,}isthesameas*,{1,}isequivalentto+,and{0,1}isthesameas?. It’sbettertouse*,+,or?whenyou
can,simplybecausethey’reshorterandeasiertoread.
3 Using Regular Expressions
Nowthatwe’velookedatsomesimpleregularexpressions,howdoweactuallyusetheminPython? Theremodule
providesaninterfacetotheregularexpressionengine, allowingyoutocompileREsintoobjectsandthenperform
matcheswiththem.
3.1 Compiling Regular Expressions
Regularexpressionsarecompiledintopatternobjects,whichhavemethodsforvariousoperationssuchassearching
forpatternmatchesorperformingstringsubstitutions.
>>> import re
>>> p = re.compile('ab*')
>>> p
re.compile('ab*')
re.compile()alsoacceptsanoptionalflagsargument,usedtoenablevariousspecialfeaturesandsyntaxvariations.
We’llgoovertheavailablesettingslater,butfornowasingleexamplewilldo:
>>> p = re.compile('ab*', re.IGNORECASE)
TheREispassedtore.compile()asastring. REsarehandledasstringsbecauseregularexpressionsaren’tpartof
thecorePythonlanguage,andnospecialsyntaxwascreatedforexpressingthem. (Thereareapplicationsthatdon’t
4

| Step | Matched | Explanation |
| --- | --- | --- |
| 1 | a | TheaintheREmatches. |
| 2 | abcbd | Theenginematches[bcd]*,goingasfarasitcan,whichistotheendofthestring. |
| 3 | Failure | Theenginetriestomatchb,butthecurrentpositionisattheendofthestring,soitfails. |
| 4 | abcb | Backup,sothat[bcd]*matchesonelesscharacter. |
| 5 | Failure | Trybagain,butthecurrentpositionisatthelastcharacter,whichisa'd'. |
| 6 | abc | Backupagain,sothat[bcd]*isonlymatchingbc. |
| 6 | abcb | Trybagain. Thistimethecharacteratthecurrentpositionis'b',soitsucceeds. |

### 第5页

needREsatall,sothere’snoneedtobloatthelanguagespecificationbyincludingthem.) Instead,theremoduleis
simplyaCextensionmoduleincludedwithPython,justlikethesocketorzlibmodules.
PuttingREsinstringskeepsthePythonlanguagesimpler, buthasonedisadvantagewhichisthetopicofthenext
section.
3.2 The Backslash Plague
Asstatedearlier,regularexpressionsusethebackslashcharacter('\')toindicatespecialformsortoallowspecial
characterstobeusedwithoutinvokingtheirspecialmeaning. ThisconflictswithPython’susageofthesamecharacter
forthesamepurposeinstringliterals.
Let’s say you want to write a RE that matches the string \section, which might be found in a LaTeX file. To
figureoutwhattowriteintheprogramcode,startwiththedesiredstringtobematched. Next,youmustescapeany
backslashesandothermetacharactersbyprecedingthemwithabackslash,resultinginthestring\\section. The
resultingstringthatmustbepassedtore.compile()mustbe\\section. However,toexpressthisasaPython
stringliteral,bothbackslashesmustbeescapedagain.
Characters Stage
\section Textstringtobematched
\\section Escapedbackslashforre.compile()
"\\\\section" Escapedbackslashesforastringliteral
Inshort,tomatchaliteralbackslash,onehastowrite'\\\\'astheREstring,becausetheregularexpressionmustbe
\\,andeachbackslashmustbeexpressedas\\insidearegularPythonstringliteral. InREsthatfeaturebackslashes
repeatedly,thisleadstolotsofrepeatedbackslashesandmakestheresultingstringsdifficulttounderstand.
ThesolutionistousePython’srawstringnotationforregularexpressions;backslashesarenothandledinanyspecial
wayinastringliteralprefixedwith'r',sor"\n"isatwo-characterstringcontaining'\'and'n',while"\n"is
aone-characterstringcontaininganewline. RegularexpressionswilloftenbewritteninPythoncodeusingthisraw
stringnotation.
Inaddition,specialescapesequencesthatarevalidinregularexpressions,butnotvalidasPythonstringliterals,now
resultinaDeprecationWarningandwilleventuallybecomeaSyntaxError,whichmeansthesequenceswillbe
invalidifrawstringnotationorescapingthebackslashesisn’tused.
RegularString Rawstring
"ab*" r"ab*"
"\\\\section" r"\\section"
"\\w+\\s+\\1" r"\w+\s+\1"
3.3 Performing Matches
Onceyouhaveanobjectrepresentingacompiledregularexpression,whatdoyoudowithit? Patternobjectshave
severalmethodsandattributes. Onlythemostsignificantoneswillbecoveredhere;consulttheredocsforacomplete
listing.
Method/Attribute Purpose
match() DetermineiftheREmatchesatthebeginningofthestring.
search() Scanthroughastring,lookingforanylocationwherethisREmatches.
findall() FindallsubstringswheretheREmatches,andreturnsthemasalist.
finditer() FindallsubstringswheretheREmatches,andreturnsthemasaniterator.
match() and search() return None if no match can be found. If they’re successful, a match object instance is
returned,containinginformationaboutthematch: whereitstartsandends,thesubstringitmatched,andmore.
5

| Characters | Stage |
| --- | --- |
| \section | Textstringtobematched |
| \\section | Escapedbackslashforre.compile() |
| "\\\\section" | Escapedbackslashesforastringliteral |


| RegularString | Rawstring |
| --- | --- |
| "ab*" | r"ab*" |
| "\\\\section" | r"\\section" |
| "\\w+\\s+\\1" | r"\w+\s+\1" |


| Method/Attribute | Purpose |
| --- | --- |
| match() | DetermineiftheREmatchesatthebeginningofthestring. |
| search() | Scanthroughastring,lookingforanylocationwherethisREmatches. |
| findall() | FindallsubstringswheretheREmatches,andreturnsthemasalist. |
| finditer() | FindallsubstringswheretheREmatches,andreturnsthemasaniterator. |

### 第6页

Youcanlearnaboutthisbyinteractivelyexperimentingwiththeremodule.
ThisHOWTOusesthestandardPythoninterpreterforitsexamples. First,runthePythoninterpreter,importthere
module,andcompileaRE:
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')
Now,youcantrymatchingvariousstringsagainsttheRE[a-z]+. Anemptystringshouldn’tmatchatall,since+
means‘oneormorerepetitions’. match()shouldreturnNoneinthiscase,whichwillcausetheinterpretertoprint
nooutput. Youcanexplicitlyprinttheresultofmatch()tomakethisclear.
>>> p.match("")
>>> print(p.match(""))
None
Now,let’stryitonastringthatitshouldmatch,suchastempo. Inthiscase,match()willreturnamatchobject,so
youshouldstoretheresultinavariableforlateruse.
>>> m = p.match('tempo')
>>> m
<re.Match object; span=(0, 5), match='tempo'>
Now you can query the match object for information about the matching string. Match object instances also have
severalmethodsandattributes;themostimportantonesare:
Method/Attribute Purpose
group() ReturnthestringmatchedbytheRE
start() Returnthestartingpositionofthematch
end() Returntheendingpositionofthematch
span() Returnatuplecontainingthe(start,end)positionsofthematch
Tryingthesemethodswillsoonclarifytheirmeaning:
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)
group() returns the substring that was matched by the RE. start() and end() return the starting and ending
indexofthematch. span()returnsbothstartandendindexesinasingletuple. Sincethematch()methodonly
checksiftheREmatchesatthestartofastring,start()willalwaysbezero. However,thesearch()methodof
patternsscansthroughthestring,sothematchmaynotstartatzerointhatcase.
>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)
Inactualprograms,themostcommonstyleistostorethematchobjectinavariable,andthencheckifitwasNone.
Thisusuallylookslike:
6

| Method/Attribute | Purpose |
| --- | --- |
| group() | ReturnthestringmatchedbytheRE |
| start() | Returnthestartingpositionofthematch |
| end() | Returntheendingpositionofthematch |
| span() | Returnatuplecontainingthe(start,end)positionsofthematch |

### 第7页

p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
print('Match found: ', m.group())
else:
print('No match')
Twopatternmethodsreturnallofthematchesforapattern. findall()returnsalistofmatchingstrings:
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
The r prefix, making the literal a raw string literal, is needed in this example because escape sequences in a nor-
mal “cooked” string literal that are not recognized by Python, as opposed to regular expressions, now result in a
DeprecationWarningandwilleventuallybecomeaSyntaxError. SeeTheBackslashPlague.
findall()hastocreatetheentirelistbeforeitcanbereturnedastheresult. Thefinditer()methodreturnsa
sequenceofmatchobjectinstancesasaniterator:
>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator
<callable_iterator object at 0x...>
>>> for match in iterator:
... print(match.span())
...
(0, 2)
(22, 24)
(29, 31)
3.4 Module-Level Functions
Youdon’thavetocreateapatternobjectandcallitsmethods;theremodulealsoprovidestop-levelfunctionscalled
match(), search(), findall(), sub(), and so forth. These functions take the same arguments as the corre-
spondingpatternmethodwiththeREstringaddedasthefirstargument,andstillreturneitherNoneoramatchobject
instance.
>>> print(re.match(r'From\s+', 'Fromage amk'))
None
>>> re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.Match object; span=(0, 5), match='From '>
Underthehood,thesefunctionssimplycreateapatternobjectforyouandcalltheappropriatemethodonit. They
alsostorethecompiledobjectinacache,sofuturecallsusingthesameREwon’tneedtoparsethepatternagainand
again.
Shouldyouusethesemodule-levelfunctions,orshouldyougetthepatternandcallitsmethodsyourself? Ifyou’re
accessingaregexwithinaloop,pre-compilingitwillsaveafewfunctioncalls. Outsideofloops,there’snotmuch
differencethankstotheinternalcache.
3.5 Compilation Flags
Compilationflagsletyoumodifysomeaspectsofhowregularexpressionswork. Flagsareavailableintheremodule
under two names, a long name such as IGNORECASE and a short, one-letter form such as I. (If you’re familiar
withPerl’spatternmodifiers,theone-letterformsusethesameletters;theshortformofre.VERBOSEisre.X,for
example.) MultipleflagscanbespecifiedbybitwiseOR-ingthem; re.I | re.MsetsboththeIandMflags, for
example.
Here’satableoftheavailableflags,followedbyamoredetailedexplanationofeachone.
7

### 第8页

Flag Meaning
ASCII,A Makesseveralescapeslike\w,\b,\sand\dmatchonlyonASCIIcharacterswiththe
respectiveproperty.
DOTALL,S Make.matchanycharacter,includingnewlines.
IGNORECASE,I Docase-insensitivematches.
LOCALE,L Doalocale-awarematch.
MULTILINE,M Multi-linematching,affecting^and$.
VERBOSE, X (for ‘ex- EnableverboseREs,whichcanbeorganizedmorecleanlyandunderstandably.
tended’)
re.I
re.IGNORECASE
Performcase-insensitivematching;characterclassandliteralstringswillmatchlettersbyignoringcase. For
example,[A-Z]willmatchlowercaseletters,too. FullUnicodematchingalsoworksunlesstheASCIIflagis
usedtodisablenon-ASCIImatches. WhentheUnicodepatterns[a-z]or[A-Z]areusedincombinationwith
theIGNORECASEflag,theywillmatchthe52ASCIIlettersand4additionalnon-ASCIIletters: ‘İ’(U+0130,
LatincapitalletterIwithdotabove),‘ı’(U+0131,Latinsmallletterdotlessi),‘ſ’(U+017F,Latinsmallletter
longs)and‘K’(U+212A,Kelvinsign). Spamwillmatch'Spam','spam','spAM',or'ſpam'(thelatteris
matchedonlyinUnicodemode). Thislowercasingdoesn’ttakethecurrentlocaleintoaccount;itwillifyou
alsosettheLOCALEflag.
re.L
re.LOCALE
Make \w, \W, \b, \B and case-insensitivematchingdependentonthe currentlocaleinsteadoftheUnicode
database.
Locales are a feature of the C library intended to help in writing programs that take account of language
differences. Forexample,ifyou’reprocessingencodedFrenchtext,you’dwanttobeabletowrite\w+tomatch
words,but\wonlymatchesthecharacterclass[A-Za-z]inbytespatterns;itwon’tmatchbytescorresponding
toéorç. IfyoursystemisconfiguredproperlyandaFrenchlocaleisselected, certainCfunctionswilltell
theprogramthatthebytecorrespondingtoéshouldalsobeconsideredaletter. SettingtheLOCALEflagwhen
compilingaregularexpressionwillcausetheresultingcompiledobjecttousetheseCfunctionsfor\w; this
isslower,butalsoenables\w+tomatchFrenchwordsasyou’dexpect. Theuseofthisflagisdiscouragedin
Python3asthelocalemechanismisveryunreliable,itonlyhandlesone“culture”atatime,anditonlyworks
with8-bitlocales. UnicodematchingisalreadyenabledbydefaultinPython3forUnicode(str)patterns,and
itisabletohandledifferentlocales/languages.
re.M
re.MULTILINE
(^and$haven’tbeenexplainedyet;they’llbeintroducedinsectionMoreMetacharacters.)
Usually^matchesonlyatthebeginningofthestring,and$matchesonlyattheendofthestringandimmedi-
atelybeforethenewline(ifany)attheendofthestring. Whenthisflagisspecified,^matchesatthebeginning
ofthestringandatthebeginningofeachlinewithinthestring,immediatelyfollowingeachnewline. Similarly,
the$metacharactermatcheseitherattheendofthestringandattheendofeachline(immediatelypreceding
eachnewline).
re.S
re.DOTALL
Makes the '.' special character match any character at all, including a newline; without this flag, '.' will
matchanythingexceptanewline.
re.A
re.ASCII
Make\w,\W,\b,\B,\sand\SperformASCII-onlymatchinginsteadoffullUnicodematching. Thisisonly
meaningfulforUnicodepatterns,andisignoredforbytepatterns.
re.X
8

| Flag | Meaning |
| --- | --- |
| ASCII,A | Makesseveralescapeslike\w,\b,\sand\dmatchonlyonASCIIcharacterswiththe
respectiveproperty. |
| DOTALL,S | Make.matchanycharacter,includingnewlines. |
| IGNORECASE,I | Docase-insensitivematches. |
| LOCALE,L | Doalocale-awarematch. |
| MULTILINE,M | Multi-linematching,affecting^and$. |
| VERBOSE, X (for ‘ex-
tended’) | EnableverboseREs,whichcanbeorganizedmorecleanlyandunderstandably. |

### 第9页

re.VERBOSE
Thisflagallowsyoutowriteregularexpressionsthataremorereadablebygrantingyoumoreflexibilityinhow
youcanformatthem. Whenthisflaghasbeenspecified, whitespacewithintheREstringisignored, except
whenthewhitespaceisinacharacterclassorprecededbyanunescapedbackslash;thisletsyouorganizeand
indenttheREmoreclearly. ThisflagalsoletsyouputcommentswithinaREthatwillbeignoredbytheengine;
commentsaremarkedbya'#'that’sneitherinacharacterclassorprecededbyanunescapedbackslash.
Forexample,here’saREthatusesre.VERBOSE;seehowmucheasieritistoread?
charref = re.compile(r"""
&[#] # Start of a numeric entity reference
(
0[0-7]+ # Octal form
| [0-9]+ # Decimal form
| x[0-9a-fA-F]+ # Hexadecimal form
)
; # Trailing semicolon
""", re.VERBOSE)
Withouttheverbosesetting,theREwouldlooklikethis:
charref = re.compile("&#(0[0-7]+"
"|[0-9]+"
"|x[0-9a-fA-F]+);")
In the above example, Python’s automatic concatenation of string literals has been used to break up the RE
intosmallerpieces,butit’sstillmoredifficulttounderstandthantheversionusingre.VERBOSE.
4 More Pattern Power
Sofarwe’veonlycoveredapartofthefeaturesofregularexpressions. Inthissection,we’llcoversomenewmetachar-
acters,andhowtousegroupstoretrieveportionsofthetextthatwasmatched.
4.1 More Metacharacters
Therearesomemetacharactersthatwehaven’tcoveredyet. Mostofthemwillbecoveredinthissection.
Some of the remaining metacharacters to be discussed are zero-width assertions. They don’t cause the engine to
advancethroughthestring;instead,theyconsumenocharactersatall,andsimplysucceedorfail. Forexample,\b
isanassertionthatthecurrentpositionislocatedatawordboundary;thepositionisn’tchangedbythe\batall. This
meansthatzero-widthassertionsshouldneverberepeated,becauseiftheymatchonceatagivenlocation,theycan
obviouslybematchedaninfinitenumberoftimes.
|
Alternation,orthe“or”operator. IfAandBareregularexpressions,A|Bwillmatchanystringthatmatches
eitherAorB.|hasverylowprecedenceinordertomakeitworkreasonablywhenyou’realternatingmulti-
character strings. Crow|Servo will match either 'Crow' or 'Servo', not 'Cro', a 'w' or an 'S', and
'ervo'.
Tomatchaliteral'|',use\|,orencloseitinsideacharacterclass,asin[|].
^
Matchesatthebeginningoflines. UnlesstheMULTILINEflaghasbeenset,thiswillonlymatchatthebeginning
ofthestring. InMULTILINEmode,thisalsomatchesimmediatelyaftereachnewlinewithinthestring.
Forexample,ifyouwishtomatchthewordFromonlyatthebeginningofaline,theREtouseis^From.
>>> print(re.search('^From', 'From Here to Eternity'))
<re.Match object; span=(0, 4), match='From'>
>>> print(re.search('^From', 'Reciting From Memory'))
None
9

### 第10页

Tomatchaliteral'^',use\^.
$
Matches at the end of a line, which is defined as either the end of the string, or any location followed by a
newlinecharacter.
>>> print(re.search('}$', '{block}'))
<re.Match object; span=(6, 7), match='}'>
>>> print(re.search('}$', '{block} '))
None
>>> print(re.search('}$', '{block}\n'))
<re.Match object; span=(6, 7), match='}'>
Tomatchaliteral'$',use\$orencloseitinsideacharacterclass,asin[$].
\A
Matchesonlyatthestartofthestring. WhennotinMULTILINEmode,\Aand^areeffectivelythesame. In
MULTILINEmode,they’redifferent: \Astillmatchesonlyatthebeginningofthestring,but^maymatchat
anylocationinsidethestringthatfollowsanewlinecharacter.
\z
Matchesonlyattheendofthestring.
\Z
Thesameas\z. ForcompatibilitywitholdPythonversions.
\b
Wordboundary. Thisisazero-widthassertionthatmatchesonlyatthebeginningorendofaword. Aword
is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a
non-alphanumericcharacter.
The following example matches class only when it’s a complete word; it won’t match when it’s contained
insideanotherword.
>>> p = re.compile(r'\bclass\b')
>>> print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'>
>>> print(p.search('the declassified algorithm'))
None
>>> print(p.search('one subclass is'))
None
Therearetwosubtletiesyoushouldrememberwhenusingthisspecialsequence. First,thisistheworstcollision
betweenPython’sstringliteralsandregularexpressionsequences. InPython’sstringliterals,\bisthebackspace
character,ASCIIvalue8. Ifyou’renotusingrawstrings,thenPythonwillconvertthe\btoabackspace,and
yourREwon’tmatchasyouexpectitto. ThefollowingexamplelooksthesameasourpreviousRE,butomits
the'r'infrontoftheREstring.
>>> p = re.compile('\bclass\b')
>>> print(p.search('no class at all'))
None
>>> print(p.search('\b' + 'class' + '\b'))
<re.Match object; span=(0, 7), match='\x08class\x08'>
Second,insideacharacterclass,wherethere’snouseforthisassertion,\brepresentsthebackspacecharacter,
forcompatibilitywithPython’sstringliterals.
\B
Anotherzero-widthassertion,thisistheoppositeof\b,onlymatchingwhenthecurrentpositionisnotata
wordboundary.
10

### 第11页

4.2 Grouping
FrequentlyyouneedtoobtainmoreinformationthanjustwhethertheREmatchedornot. Regularexpressionsare
often used to dissect strings by writing a RE divided into several subgroups which match different components of
interest. Forexample,anRFC-822headerlineisdividedintoaheadernameandavalue,separatedbya':',like
this:
From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com
Thiscanbehandledbywritingaregularexpressionwhichmatchesanentireheaderline,andhasonegroupwhich
matchestheheadername,andanothergroupwhichmatchestheheader’svalue.
Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning as they do in
mathematicalexpressions;theygrouptogethertheexpressionscontainedinsidethem,andyoucanrepeatthecontents
ofagroupwithaquantifier,suchas*,+,?,or{m,n}. Forexample,(ab)*willmatchzeroormorerepetitionsof
ab.
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)
Groupsindicatedwith'(',')'alsocapturethestartingandendingindexofthetextthattheymatch;thiscanbe
retrievedbypassinganargumenttogroup(),start(),end(),andspan(). Groupsarenumberedstartingwith
0. Group0isalwayspresent;it’sthewholeRE,somatchobjectmethodsallhavegroup0astheirdefaultargument.
Laterwe’llseehowtoexpressgroupsthatdon’tcapturethespanoftextthattheymatch.
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'
Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just
counttheopeningparenthesischaracters,goingfromlefttoright.
>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'
group()canbepassedmultiplegroupnumbersatatime,inwhichcaseitwillreturnatuplecontainingthecorre-
spondingvaluesforthosegroups.
>>> m.group(2,1,2)
('b', 'abc', 'b')
Thegroups()methodreturnsatuplecontainingthestringsforallthesubgroups,from1uptohowevermanythere
are.
>>> m.groups()
('abc', 'b')
11

### 第12页

Backreferencesinapatternallowyoutospecifythatthecontentsofanearliercapturinggroupmustalsobefoundat
thecurrentlocationinthestring. Forexample,\1willsucceediftheexactcontentsofgroup1canbefoundatthe
currentposition,andfailsotherwise. RememberthatPython’sstringliteralsalsouseabackslashfollowedbynumbers
toallowincludingarbitrarycharactersinastring,sobesuretousearawstringwhenincorporatingbackreferences
inaRE.
Forexample,thefollowingREdetectsdoubledwordsinastring.
>>> p = re.compile(r'\b(\w+)\s+\1\b')
>>> p.search('Paris in the the spring').group()
'the the'
Backreferences like this aren’t often useful for just searching through a string — there are few text formats which
repeatdatainthisway—butyou’llsoonfindoutthatthey’reveryusefulwhenperformingstringsubstitutions.
4.3 Non-capturing and Named Groups
ElaborateREsmayusemanygroups,bothtocapturesubstringsofinterest,andtogroupandstructuretheREitself.
IncomplexREs,itbecomesdifficulttokeeptrackofthegroupnumbers. Therearetwofeatureswhichhelpwiththis
problem. Bothofthemuseacommonsyntaxforregularexpressionextensions,sowe’lllookatthatfirst.
Perl 5 is well known for its powerful additions to standard regular expressions. For these new features the Perl
developerscouldn’tchoosenewsingle-keystrokemetacharactersornewspecialsequencesbeginningwith\without
makingPerl’sregularexpressionsconfusinglydifferentfromstandardREs. Iftheychose&asanewmetacharacter,
forexample,oldexpressionswouldbeassumingthat&wasaregularcharacterandwouldn’thaveescapeditbywriting
\&or[&].
The solution chosen by the Perl developers was to use (?...) as the extension syntax. ? immediately after a
parenthesiswasasyntaxerrorbecausethe?wouldhavenothingtorepeat,sothisdidn’tintroduceanycompatibility
problems. Thecharactersimmediatelyafterthe?indicatewhatextensionisbeingused,so(?=foo)isonething(a
positivelookaheadassertion)and(?:foo)issomethingelse(anon-capturinggroupcontainingthesubexpression
foo).
Python supports several of Perl’s extensions and adds an extension syntax to Perl’s extension syntax. If the first
characterafterthequestionmarkisaP,youknowthatit’sanextensionthat’sspecifictoPython.
Nowthatwe’velookedatthegeneralextensionsyntax,wecanreturntothefeaturesthatsimplifyworkingwithgroups
incomplexREs.
Sometimesyou’llwanttouseagrouptodenoteapartofaregularexpression,butaren’tinterestedinretrievingthe
group’scontents. Youcanmakethisfactexplicitbyusinganon-capturinggroup: (?:...),whereyoucanreplace
the...withanyotherregularexpression.
>>> m = re.match("([abc])+", "abc")
>>> m.groups()
('c',)
>>> m = re.match("(?:[abc])+", "abc")
>>> m.groups()
()
Except for the fact that you can’t retrieve the contents of what the group matched, a non-capturing group behaves
exactlythesameasacapturinggroup;youcanputanythinginsideit,repeatitwitharepetitionmetacharactersuchas
*,andnestitwithinothergroups(capturingornon-capturing). (?:...) isparticularlyusefulwhenmodifyingan
existingpattern,sinceyoucanaddnewgroupswithoutchanginghowalltheothergroupsarenumbered. Itshouldbe
mentionedthatthere’snoperformancedifferenceinsearchingbetweencapturingandnon-capturinggroups;neither
formisanyfasterthantheother.
Amoresignificantfeatureisnamedgroups: insteadofreferringtothembynumbers,groupscanbereferencedbya
name.
ThesyntaxforanamedgroupisoneofthePython-specificextensions: (?P<name>...). nameis,obviously,the
nameofthegroup. Namedgroupsbehaveexactlylikecapturinggroups, andadditionallyassociateanamewitha
group. Thematchobjectmethodsthatdealwithcapturinggroupsallaccepteitherintegersthatrefertothegroupby
12

### 第13页

numberorstringsthatcontainthedesiredgroup’sname. Namedgroupsarestillgivennumbers,soyoucanretrieve
informationaboutagroupintwoways:
>>> p = re.compile(r'(?P<word>\b\w+\b)')
>>> m = p.search( '(((( Lots of punctuation )))' )
>>> m.group('word')
'Lots'
>>> m.group(1)
'Lots'
Additionally,youcanretrievenamedgroupsasadictionarywithgroupdict():
>>> m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
>>> m.groupdict()
{'first': 'Jane', 'last': 'Doe'}
Namedgroupsarehandybecausetheyletyouuseeasilyrememberednames,insteadofhavingtoremembernumbers.
Here’sanexampleREfromtheimaplibmodule:
InternalDate = re.compile(r'INTERNALDATE "'
r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
r'(?P<year>[0-9][0-9][0-9][0-9])'
r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
r'"')
It’sobviouslymucheasiertoretrievem.group('zonem'),insteadofhavingtoremembertoretrievegroup9.
Thesyntaxforbackreferencesinanexpressionsuchas(...)\1referstothenumberofthegroup. There’snaturally
avariantthatusesthegroupnameinsteadofthenumber. ThisisanotherPythonextension: (?P=name)indicates
thatthecontentsofthegroupcallednameshouldagainbematchedatthecurrentpoint. Theregularexpressionfor
findingdoubledwords,\b(\w+)\s+\1\bcanalsobewrittenas\b(?P<word>\w+)\s+(?P=word)\b:
>>> p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
>>> p.search('Paris in the the spring').group()
'the the'
4.4 Lookahead Assertions
Another zero-width assertion is the lookahead assertion. Lookahead assertions are available in both positive and
negativeform,andlooklikethis:
(?=...)
Positive lookahead assertion. This succeeds if the contained regular expression, represented here by ...,
successfullymatchesatthecurrentlocation,andfailsotherwise. But,oncethecontainedexpressionhasbeen
tried,thematchingenginedoesn’tadvanceatall;therestofthepatternistriedrightwheretheassertionstarted.
(?!...)
Negativelookaheadassertion. Thisistheoppositeofthepositiveassertion; itsucceedsifthecontainedex-
pressiondoesn’tmatchatthecurrentpositioninthestring.
Tomakethisconcrete,let’slookatacasewherealookaheadisuseful. Considerasimplepatterntomatchafilename
andsplititapartintoabasenameandanextension,separatedbya.. Forexample,innews.rc,newsisthebase
name,andrcisthefilename’sextension.
Thepatterntomatchthisisquitesimple:
.*[.].*$
Notice that the . needs to be treated specially because it’s a metacharacter, so it’s inside a character class to only
matchthatspecificcharacter. Alsonoticethetrailing$;thisisaddedtoensurethatalltherestofthestringmustbe
13

### 第14页

includedintheextension. Thisregularexpressionmatchesfoo.barandautoexec.batandsendmail.cfand
printers.conf.
Now,considercomplicatingtheproblemabit;whatifyouwanttomatchfilenameswheretheextensionisnotbat?
Someincorrectattempts:
.*[.][^b].*$
Thefirstattemptabovetriestoexcludebatbyrequiringthatthefirstcharacteroftheextensionisnotab. Thisis
wrong,becausethepatternalsodoesn’tmatchfoo.bar.
.*[.]([^b]..|.[^a].|..[^t])$
The expression gets messier when you try to patch up the first solution by requiring one of the following cases to
match: the first character of the extension isn’t b; the second character isn’t a; or the third character isn’t t. This
accepts foo.bar and rejects autoexec.bat, but it requires a three-letter extension and won’t accept a filename
withatwo-letterextensionsuchassendmail.cf. We’llcomplicatethepatternagaininanefforttofixit.
.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$
Inthethirdattempt,thesecondandthirdlettersareallmadeoptionalinordertoallowmatchingextensionsshorter
thanthreecharacters,suchassendmail.cf.
The pattern’s getting really complicated now, which makes it hard to read and understand. Worse, if the problem
changesandyouwanttoexcludebothbatandexeasextensions,thepatternwouldgetevenmorecomplicatedand
confusing.
Anegativelookaheadcutsthroughallthisconfusion:
.*[.](?!bat$)[^.]*$
Thenegativelookaheadmeans: iftheexpressionbatdoesn’tmatchatthispoint,trytherestofthepattern;ifbat$
does match, the whole pattern will fail. The trailing $ is required to ensure that something like sample.batch,
wheretheextensiononlystartswithbat,willbeallowed. The[^.]*makessurethatthepatternworkswhenthere
aremultipledotsinthefilename.
Excludinganotherfilenameextensionisnoweasy;simplyadditasanalternativeinsidetheassertion. Thefollowing
patternexcludesfilenamesthatendineitherbatorexe:
.*[.](?!bat$|exe$)[^.]*$
5 Modifying Strings
Up to this point, we’ve simply performed searches against a static string. Regular expressions are also commonly
usedtomodifystringsinvariousways,usingthefollowingpatternmethods:
Method/Attribute Purpose
split() Splitthestringintoalist,splittingitwherevertheREmatches
sub() FindallsubstringswheretheREmatches,andreplacethemwithadifferentstring
subn() Doesthesamethingassub(),butreturnsthenewstringandthenumberofreplacements
5.1 Splitting Strings
Thesplit()methodofapatternsplitsastringapartwherevertheREmatches,returningalistofthepieces. It’s
similartothesplit()methodofstringsbutprovidesmuchmoregeneralityinthedelimitersthatyoucansplitby;
stringsplit()onlysupportssplittingbywhitespaceorbyafixedstring. Asyou’dexpect, there’samodule-level
re.split()function,too.
[ ]
.split(string ,maxsplit=0 )
Splitstringbythematchesoftheregularexpression. IfcapturingparenthesesareusedintheRE,thentheir
contents will also be returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits are
performed.
14

| Method/Attribute | Purpose |
| --- | --- |
| split() | Splitthestringintoalist,splittingitwherevertheREmatches |
| sub() | FindallsubstringswheretheREmatches,andreplacethemwithadifferentstring |
| subn() | Doesthesamethingassub(),butreturnsthenewstringandthenumberofreplacements |

### 第15页

Youcanlimitthenumberofsplitsmade,bypassingavalueformaxsplit. Whenmaxsplitisnonzero,atmostmaxsplit
splits will be made, and the remainder of the string is returned as the final element of the list. In the following
example,thedelimiterisanysequenceofnon-alphanumericcharacters.
>>> p = re.compile(r'\W+')
>>> p.split('This is a test, short and sweet, of split().')
['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']
>>> p.split('This is a test, short and sweet, of split().', 3)
['This', 'is', 'a', 'test, short and sweet, of split().']
Sometimesyou’renotonlyinterestedinwhatthetextbetweendelimitersis,butalsoneedtoknowwhatthedelimiter
was. IfcapturingparenthesesareusedintheRE,thentheirvaluesarealsoreturnedaspartofthelist. Comparethe
followingcalls:
>>> p = re.compile(r'\W+')
>>> p2 = re.compile(r'(\W+)')
>>> p.split('This... is a test.')
['This', 'is', 'a', 'test', '']
>>> p2.split('This... is a test.')
['This', '... ', 'is', ' ', 'a', ' ', 'test', '.', '']
Themodule-levelfunctionre.split()addstheREtobeusedasthefirstargument,butisotherwisethesame.
>>> re.split(r'[\W]+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'([\W]+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'[\W]+', 'Words, words, words.', 1)
['Words', 'words, words.']
5.2 Search and Replace
Anothercommontaskistofindallthematchesforapattern,andreplacethemwithadifferentstring. Thesub()
methodtakesareplacementvalue,whichcanbeeitherastringorafunction,andthestringtobeprocessed.
[ ]
.sub(replacement,string ,count=0 )
Returnsthestringobtainedbyreplacingtheleftmostnon-overlappingoccurrencesoftheREinstringbythe
replacementreplacement. Ifthepatternisn’tfound,stringisreturnedunchanged.
Theoptionalargumentcountisthemaximumnumberofpatternoccurrencestobereplaced;countmustbea
non-negativeinteger. Thedefaultvalueof0meanstoreplacealloccurrences.
Here’sasimpleexampleofusingthesub()method. Itreplacescolournameswiththewordcolour:
>>> p = re.compile('(blue|white|red)')
>>> p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes'
>>> p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
Thesubn()methoddoesthesamework,butreturnsa2-tuplecontainingthenewstringvalueandthenumberof
replacementsthatwereperformed:
>>> p = re.compile('(blue|white|red)')
>>> p.subn('colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
>>> p.subn('colour', 'no colours at all')
('no colours at all', 0)
Emptymatchesarereplacedonlywhenthey’renotadjacenttoapreviousemptymatch.
15

### 第16页

>>> p = re.compile('x*')
>>> p.sub('-', 'abxd')
'-a-b--d-'
Ifreplacementisastring,anybackslashescapesinitareprocessed. Thatis,\nisconvertedtoasinglenewlinechar-
acter,\risconvertedtoacarriagereturn,andsoforth. Unknownescapessuchas\&areleftalone. Backreferences,
suchas\6,arereplacedwiththesubstringmatchedbythecorrespondinggroupintheRE.Thisletsyouincorporate
portionsoftheoriginaltextintheresultingreplacementstring.
This example matches the word section followed by a string enclosed in {, }, and changes section to
subsection:
>>> p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
>>> p.sub(r'subsection{\1}','section{First} section{second}')
'subsection{First} subsection{second}'
There’salsoasyntaxforreferringtonamedgroupsasdefinedbythe(?P<name>...)syntax. \g<name>willuse
thesubstringmatchedbythegroupnamedname,and\g<number>usesthecorrespondinggroupnumber. \g<2>is
thereforeequivalentto\2,butisn’tambiguousinareplacementstringsuchas\g<2>0. (\20wouldbeinterpretedas
areferencetogroup20,notareferencetogroup2followedbytheliteralcharacter'0'.) Thefollowingsubstitutions
areallequivalent,butuseallthreevariationsofthereplacementstring.
>>> p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
>>> p.sub(r'subsection{\1}','section{First}')
'subsection{First}'
>>> p.sub(r'subsection{\g<1>}','section{First}')
'subsection{First}'
>>> p.sub(r'subsection{\g<name>}','section{First}')
'subsection{First}'
replacement canalsobeafunction,whichgivesyouevenmorecontrol. Ifreplacement isafunction,thefunctionis
calledforeverynon-overlappingoccurrenceofpattern. Oneachcall,thefunctionispassedamatchobjectargument
forthematchandcanusethisinformationtocomputethedesiredreplacementstringandreturnit.
Inthefollowingexample,thereplacementfunctiontranslatesdecimalsintohexadecimal:
>>> def hexrepl(match):
... "Return the hex string for a decimal number"
... value = int(match.group())
... return hex(value)
...
>>> p = re.compile(r'\d+')
>>> p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
'Call 0xffd2 for printing, 0xc000 for user code.'
Whenusingthemodule-levelre.sub()function, thepatternispassedasthefirstargument. Thepatternmaybe
provided as an object or as a string; if you need to specify regular expression flags, you must either use a pattern
objectasthefirstparameter,oruseembeddedmodifiersinthepatternstring,e.g. sub("(?i)b+", "x", "bbbb
BBBB")returns'x x'.
6 Common Problems
Regularexpressionsareapowerfultoolforsomeapplications, butinsomewaystheirbehaviourisn’tintuitiveand
attimestheydon’tbehavethewayyoumayexpectthemto. Thissectionwillpointoutsomeofthemostcommon
pitfalls.
16

### 第17页

6.1 Use String Methods
Sometimes using the re module is a mistake. If you’re matching a fixed string, or a single character class, and
you’renotusinganyrefeaturessuchastheIGNORECASEflag,thenthefullpowerofregularexpressionsmaynotbe
required. Stringshaveseveralmethodsforperformingoperationswithfixedstringsandthey’reusuallymuchfaster,
becausetheimplementationisasinglesmallCloopthat’sbeenoptimizedforthepurpose,insteadofthelarge,more
generalizedregularexpressionengine.
Oneexamplemightbereplacingasinglefixedstringwithanotherone; forexample,youmightreplacewordwith
deed. re.sub()seemslikethefunctiontouseforthis,butconsiderthereplace()method. Notethatreplace()
willalsoreplacewordinsidewords,turningswordfishintosdeedfish,butthenaiveREwordwouldhavedone
that,too. (Toavoidperformingthesubstitutiononpartsofwords,thepatternwouldhavetobe\bword\b,inorder
torequirethatwordhaveawordboundaryoneitherside. Thistakesthejobbeyondreplace()’sabilities.)
Anothercommontaskisdeletingeveryoccurrenceofasinglecharacterfromastringorreplacingitwithanother
singlecharacter. Youmightdothiswithsomethinglikere.sub('\n', ' ', S),buttranslate()iscapable
ofdoingbothtasksandwillbefasterthananyregularexpressionoperationcanbe.
In short, before turning to the re module, consider whether your problem can be solved with a faster and simpler
stringmethod.
6.2 match() versus search()
The match() function only checks if the RE matches at the beginning of the string while search() will scan
forwardthrough the stringfor a match. It’s important to keep this distinction inmind. Remember, match() will
onlyreportasuccessfulmatchwhichwillstartat0;ifthematchwouldn’tstartatzero,match()willnotreportit.
>>> print(re.match('super', 'superstition').span())
(0, 5)
>>> print(re.match('super', 'insuperable'))
None
Ontheotherhand,search()willscanforwardthroughthestring,reportingthefirstmatchitfinds.
>>> print(re.search('super', 'superstition').span())
(0, 5)
>>> print(re.search('super', 'insuperable').span())
(2, 7)
Sometimes you’ll be tempted to keep using re.match(), and just add .* to the front of your RE. Resist this
temptationandusere.search()instead. TheregularexpressioncompilerdoessomeanalysisofREsinorderto
speeduptheprocessoflookingforamatch. Onesuchanalysisfiguresoutwhatthefirstcharacterofamatchmust
be; forexample,apatternstartingwithCrowmustmatchstartingwitha'C'.Theanalysisletstheenginequickly
scanthroughthestringlookingforthestartingcharacter,onlytryingthefullmatchifa'C'isfound.
Adding.*defeatsthisoptimization,requiringscanningtotheendofthestringandthenbacktrackingtofindamatch
fortherestoftheRE.Usere.search()instead.
6.3 Greedy versus Non-Greedy
Whenrepeatinga regularexpression, asin a*, theresultingactionistoconsumeasmuchofthepatternaspossi-
ble. Thisfactoftenbitesyouwhenyou’retryingtomatchapairofbalanceddelimiters,suchastheanglebrackets
surroundinganHTMLtag. ThenaivepatternformatchingasingleHTMLtagdoesn’tworkbecauseofthegreedy
natureof.*.
>>> s = '<html><head><title>Title</title>'
>>> len(s)
32
>>> print(re.match('<.*>', s).span())
(0, 32)
(continuesonnextpage)
17

### 第18页

(continuedfrompreviouspage)
>>> print(re.match('<.*>', s).group())
<html><head><title>Title</title>
TheREmatchesthe'<'in'<html>',andthe.*consumestherestofthestring. There’sstillmoreleftintheRE,
though, andthe>can’tmatchattheendofthestring, sotheregularexpressionenginehastobacktrackcharacter
by character until it finds a match for the >. The final match extends from the '<' in '<html>' to the '>' in
'</title>',whichisn’twhatyouwant.
In this case, the solution is to use the non-greedy quantifiers *?, +?, ??, or {m,n}?, which match as little text as
possible. Intheaboveexample,the'>'istriedimmediatelyafterthefirst'<'matches,andwhenitfails,theengine
advancesacharacteratatime,retryingthe'>'ateverystep. Thisproducesjusttherightresult:
>>> print(re.match('<.*?>', s).group())
<html>
(NotethatparsingHTMLorXMLwithregularexpressionsispainful. Quick-and-dirtypatternswillhandlecommon
cases, but HTML and XML have special cases that will break the obvious regular expression; by the time you’ve
written a regular expression that handles all of the possible cases, the patterns will be very complicated. Use an
HTMLorXMLparsermoduleforsuchtasks.)
6.4 Using re.VERBOSE
Bynowyou’veprobablynoticedthatregularexpressionsareaverycompactnotation,butthey’renotterriblyreadable.
REsofmoderatecomplexitycanbecomelengthycollectionsofbackslashes,parentheses,andmetacharacters,making
themdifficulttoreadandunderstand.
For such REs, specifying the re.VERBOSE flag when compiling the regular expression can be helpful, because it
allowsyoutoformattheregularexpressionmoreclearly.
There.VERBOSEflaghasseveraleffects. Whitespaceintheregularexpressionthatisn’t insideacharacterclassis
ignored. Thismeansthatanexpressionsuchasdog | catisequivalenttothelessreadabledog|cat,but[a b]
willstillmatchthecharacters'a','b',oraspace. Inaddition,youcanalsoputcommentsinsideaRE;comments
extendfroma#charactertothenextnewline. Whenusedwithtriple-quotedstrings,thisenablesREstobeformatted
moreneatly:
pat = re.compile(r"""
\s* # Skip leading whitespace
(?P<header>[^:]+) # Header name
\s* : # Whitespace, and a colon
(?P<value>.*?) # The header's value -- *? used to
# lose the following trailing whitespace
\s*$ # Trailing whitespace to end-of-line
""", re.VERBOSE)
Thisisfarmorereadablethan:
pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")
7 Feedback
Regularexpressionsareacomplicatedtopic. Didthisdocumenthelpyouunderstandthem? Weretherepartsthat
wereunclear,orProblemsyouencounteredthatweren’tcoveredhere? Ifso,pleasesendsuggestionsforimprovements
totheauthor.
ThemostcompletebookonregularexpressionsisalmostcertainlyJeffreyFriedl’sMasteringRegularExpressions,
publishedbyO’Reilly. Unfortunately, itexclusivelyconcentratesonPerlandJava’sflavoursofregularexpressions,
anddoesn’tcontainanyPythonmaterialatall,soitwon’tbeusefulasareferenceforprogramminginPython. (The
firsteditioncoveredPython’snow-removedregexmodule,whichwon’thelpyoumuch.) Considercheckingitout
fromyourlibrary.
18

