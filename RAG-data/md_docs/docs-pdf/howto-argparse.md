### 第1页

Argparse Tutorial
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
1 Concepts 2
2 Thebasics 2
3 IntroducingPositionalarguments 3
4 IntroducingOptionalarguments 4
4.1 Shortoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
5 CombiningPositionalandOptionalarguments 6
6 Gettingalittlemoreadvanced 10
6.1 Specifyingambiguousarguments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
6.2 Conflictingoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
7 Howtotranslatetheargparseoutput 13
8 Customtypeconverters 14
9 Conclusion 14
author
TshepangMbambo
Thistutorialisintendedtobeagentleintroductiontoargparse,therecommendedcommand-lineparsingmodule
inthePythonstandardlibrary.
(cid:174) Note
The standard library includes two other libraries directly related to command-line parameter processing: the
lowerleveloptparsemodule(whichmayrequiremorecodetoconfigureforagivenapplication, butalsoal-
lowsanapplicationtorequestbehaviorsthatargparsedoesn’tsupport),andtheverylowlevelgetopt(which
specifically serves as an equivalent to the getopt() family of functions available to C programmers). While
neitherofthosemodulesiscovereddirectlyinthisguide,manyofthecoreconceptsinargparsefirstoriginated
inoptparse,sosomeaspectsofthistutorialwillalsoberelevanttooptparseusers.
1

### 第2页

1 Concepts
Let’sshowthesortoffunctionalitythatwearegoingtoexploreinthisintroductorytutorialbymakinguseofthels
command:
$ ls
cpython devguide prog.py pypy rm-unused-function.patch
$ ls pypy
ctypes_configure demo dotviewer include lib_pypy lib-python ...
$ ls -l
total 20
drwxr-xr-x 19 wena wena 4096 Feb 18 18:51 cpython
drwxr-xr-x 4 wena wena 4096 Feb 8 12:04 devguide
-rwxr-xr-x 1 wena wena 535 Feb 19 00:05 prog.py
drwxr-xr-x 14 wena wena 4096 Feb 7 00:59 pypy
-rw-r--r-- 1 wena wena 741 Feb 18 01:01 rm-unused-function.patch
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
...
Afewconceptswecanlearnfromthefourcommands:
• Thelscommandisusefulwhenrunwithoutanyoptionsatall. Itdefaultstodisplayingthecontentsofthe
currentdirectory.
• Ifwewantbeyondwhatitprovidesbydefault,wetellitabitmore. Inthiscase,wewantittodisplayadifferent
directory,pypy. Whatwedidisspecifywhatisknownasapositionalargument. It’snamedsobecausethe
programshouldknowwhattodowiththevalue,solelybasedonwhereitappearsonthecommandline. This
conceptismorerelevanttoacommandlikecp,whosemostbasicusageiscp SRC DEST.Thefirstposition
iswhatyouwantcopied,andthesecondpositioniswhereyouwantitcopiedto.
• Now, say we want to change behaviour of the program. In our example, we display more info for each file
insteadofjustshowingthefilenames. The-linthatcaseisknownasanoptionalargument.
• That’sasnippetofthehelptext. It’sveryusefulinthatyoucancomeacrossaprogramyouhaveneverused
before,andcanfigureouthowitworkssimplybyreadingitshelptext.
2 The basics
Letusstartwithaverysimpleexamplewhichdoes(almost)nothing:
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
Followingisaresultofrunningthecode:
$ python prog.py
$ python prog.py --help
usage: prog.py [-h]
options:
-h, --help show this help message and exit
$ python prog.py --verbose
usage: prog.py [-h]
prog.py: error: unrecognized arguments: --verbose
$ python prog.py foo
(continuesonnextpage)
2

### 第3页

(continuedfrompreviouspage)
usage: prog.py [-h]
prog.py: error: unrecognized arguments: foo
Hereiswhatishappening:
• Runningthescriptwithoutanyoptionsresultsinnothingdisplayedtostdout. Notsouseful.
• Thesecondonestartstodisplaytheusefulnessoftheargparsemodule. Wehavedonealmostnothing,but
alreadywegetanicehelpmessage.
• The --help option, which can also be shortened to -h, is the only option we get for free (i.e. no need to
specifyit). Specifyinganythingelseresultsinanerror. Buteventhen,wedogetausefulusagemessage,also
forfree.
3 Introducing Positional arguments
Anexample:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
Andrunningthecode:
$ python prog.py
usage: prog.py [-h] echo
prog.py: error: the following arguments are required: echo
$ python prog.py --help
usage: prog.py [-h] echo
positional arguments:
echo
options:
-h, --help show this help message and exit
$ python prog.py foo
foo
Hereiswhat’shappening:
• We’ve added the add_argument() method, which is what we use to specify which command-line options
theprogramiswillingtoaccept. Inthiscase,I’venameditechosothatit’sinlinewithitsfunction.
• Callingourprogramnowrequiresustospecifyanoption.
• Theparse_args()methodactuallyreturnssomedatafromtheoptionsspecified,inthiscase,echo.
• Thevariableissomeformof‘magic’thatargparseperformsforfree(i.e. noneedtospecifywhichvariable
thatvalueisstoredin). Youwillalsonoticethatitsnamematchesthestringargumentgiventothemethod,
echo.
Notehoweverthat,althoughthehelpdisplaylooksniceandall,itcurrentlyisnotashelpfulasitcanbe. Forexample
we see that we got echo as a positional argument, but we don’t know what it does, other than by guessing or by
readingthesourcecode. So,let’smakeitabitmoreuseful:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
(continuesonnextpage)
3

### 第4页

(continuedfrompreviouspage)
args = parser.parse_args()
print(args.echo)
Andweget:
$ python prog.py -h
usage: prog.py [-h] echo
positional arguments:
echo echo the string you use here
options:
-h, --help show this help message and exit
Now,howaboutdoingsomethingevenmoreuseful:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)
Followingisaresultofrunningthecode:
$ python prog.py 4
Traceback (most recent call last):
File "prog.py", line 5, in <module>
print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
Thatdidn’tgosowell. That’sbecauseargparsetreatstheoptionswegiveitasstrings,unlesswetellitotherwise.
So,let’stellargparsetotreatthatinputasaninteger:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
type=int)
args = parser.parse_args()
print(args.square**2)
Followingisaresultofrunningthecode:
$ python prog.py 4
16
$ python prog.py four
usage: prog.py [-h] square
prog.py: error: argument square: invalid int value: 'four'
Thatwentwell. Theprogramnowevenhelpfullyquitsonbadillegalinputbeforeproceeding.
4 Introducing Optional arguments
Sofarwehavebeenplayingwithpositionalarguments. Letushavealookonhowtoaddoptionalones:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
(continuesonnextpage)
4

### 第5页

(continuedfrompreviouspage)
args = parser.parse_args()
if args.verbosity:
print("verbosity turned on")
Andtheoutput:
$ python prog.py --verbosity 1
verbosity turned on
$ python prog.py
$ python prog.py --help
usage: prog.py [-h] [--verbosity VERBOSITY]
options:
-h, --help show this help message and exit
--verbosity VERBOSITY
increase output verbosity
$ python prog.py --verbosity
usage: prog.py [-h] [--verbosity VERBOSITY]
prog.py: error: argument --verbosity: expected one argument
Hereiswhatishappening:
• Theprogramiswrittensoastodisplaysomethingwhen--verbosityisspecifiedanddisplaynothingwhen
not.
• Toshowthattheoptionisactuallyoptional,thereisnoerrorwhenrunningtheprogramwithoutit. Notethat
bydefault, ifanoptionalargumentisn’tused, therelevantvariable, inthiscaseargs.verbosity, isgiven
Noneasavalue,whichisthereasonitfailsthetruthtestoftheifstatement.
• Thehelpmessageisabitdifferent.
• Whenusingthe--verbosityoption,onemustalsospecifysomevalue,anyvalue.
Theaboveexampleacceptsarbitraryintegervaluesfor--verbosity,butforoursimpleprogram,onlytwovalues
areactuallyuseful,TrueorFalse. Let’smodifythecodeaccordingly:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
action="store_true")
args = parser.parse_args()
if args.verbose:
print("verbosity turned on")
Andtheoutput:
$ python prog.py --verbose
verbosity turned on
$ python prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1
$ python prog.py --help
usage: prog.py [-h] [--verbose]
options:
-h, --help show this help message and exit
--verbose increase output verbosity
Hereiswhatishappening:
5

### 第6页

• Theoptionisnowmoreofaflagthansomethingthatrequiresavalue. Weevenchangedthenameoftheoption
tomatchthatidea. Notethatwenowspecifyanewkeyword,action,andgiveitthevalue"store_true".
Thismeansthat,iftheoptionisspecified,assignthevalueTruetoargs.verbose. Notspecifyingitimplies
False.
• Itcomplainswhenyouspecifyavalue,intruespiritofwhatflagsactuallyare.
• Noticethedifferenthelptext.
4.1 Short options
Ifyouarefamiliarwithcommandlineusage,youwillnoticethatIhaven’tyettouchedonthetopicofshortversions
oftheoptions. It’squitesimple:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
action="store_true")
args = parser.parse_args()
if args.verbose:
print("verbosity turned on")
Andheregoes:
$ python prog.py -v
verbosity turned on
$ python prog.py --help
usage: prog.py [-h] [-v]
options:
-h, --help show this help message and exit
-v, --verbose increase output verbosity
Notethatthenewabilityisalsoreflectedinthehelptext.
5 Combining Positional and Optional arguments
Ourprogramkeepsgrowingincomplexity:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
print(f"the square of {args.square} equals {answer}")
else:
print(answer)
Andnowtheoutput:
$ python prog.py
usage: prog.py [-h] [-v] square
prog.py: error: the following arguments are required: square
$ python prog.py 4
(continuesonnextpage)
6

### 第7页

(continuedfrompreviouspage)
16
$ python prog.py 4 --verbose
the square of 4 equals 16
$ python prog.py --verbose 4
the square of 4 equals 16
• We’vebroughtbackapositionalargument,hencethecomplaint.
• Notethattheorderdoesnotmatter.
Howaboutwegivethisprogramofoursbacktheabilitytohavemultipleverbosityvalues, andactuallygettouse
them:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
print(f"{args.square}^2 == {answer}")
else:
print(answer)
Andtheoutput:
$ python prog.py 4
16
$ python prog.py 4 -v
usage: prog.py [-h] [-v VERBOSITY] square
prog.py: error: argument -v/--verbosity: expected one argument
$ python prog.py 4 -v 1
4^2 == 16
$ python prog.py 4 -v 2
the square of 4 equals 16
$ python prog.py 4 -v 3
16
Thesealllookgoodexceptthelastone,whichexposesabuginourprogram. Let’sfixitbyrestrictingthevaluesthe
--verbosityoptioncanaccept:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
print(f"{args.square}^2 == {answer}")
(continuesonnextpage)
7

### 第8页

(continuedfrompreviouspage)
else:
print(answer)
Andtheoutput:
$ python prog.py 4 -v 3
usage: prog.py [-h] [-v {0,1,2}] square
prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)
$ python prog.py 4 -h
usage: prog.py [-h] [-v {0,1,2}] square
positional arguments:
square display a square of a given number
options:
-h, --help show this help message and exit
-v, --verbosity {0,1,2}
increase output verbosity
Notethatthechangealsoreflectsbothintheerrormessageaswellasthehelpstring.
Now,let’suseadifferentapproachofplayingwithverbosity,whichisprettycommon. Italsomatchesthewaythe
CPythonexecutablehandlesitsownverbosityargument(checktheoutputofpython --help):
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
print(f"{args.square}^2 == {answer}")
else:
print(answer)
Wehaveintroducedanotheraction,“count”,tocountthenumberofoccurrencesofspecificoptions.
$ python prog.py 4
16
$ python prog.py 4 -v
4^2 == 16
$ python prog.py 4 -vv
the square of 4 equals 16
$ python prog.py 4 --verbosity --verbosity
the square of 4 equals 16
$ python prog.py 4 -v 1
usage: prog.py [-h] [-v] square
prog.py: error: unrecognized arguments: 1
$ python prog.py 4 -h
usage: prog.py [-h] [-v] square
positional arguments:
square display a square of a given number
(continuesonnextpage)
8

### 第9页

(continuedfrompreviouspage)
options:
-h, --help show this help message and exit
-v, --verbosity increase output verbosity
$ python prog.py 4 -vvv
16
• Yes,it’snowmoreofaflag(similartoaction="store_true")inthepreviousversionofourscript. That
shouldexplainthecomplaint.
• Italsobehavessimilarto“store_true”action.
• Nowhere’sademonstrationofwhatthe“count”actiongives. You’veprobablyseenthissortofusagebefore.
• Andifyoudon’tspecifythe-vflag,thatflagisconsideredtohaveNonevalue.
• Asshouldbeexpected,specifyingthelongformoftheflag,weshouldgetthesameoutput.
• Sadly,ourhelpoutputisn’tveryinformativeonthenewabilityourscripthasacquired,butthatcanalwaysbe
fixedbyimprovingthedocumentationforourscript(e.g. viathehelpkeywordargument).
• Thatlastoutputexposesabuginourprogram.
Let’sfix:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
# bugfix: replace == with >=
if args.verbosity >= 2:
print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
print(f"{args.square}^2 == {answer}")
else:
print(answer)
Andthisiswhatitgives:
$ python prog.py 4 -vvv
the square of 4 equals 16
$ python prog.py 4 -vvvv
the square of 4 equals 16
$ python prog.py 4
Traceback (most recent call last):
File "prog.py", line 11, in <module>
if args.verbosity >= 2:
TypeError: '>=' not supported between instances of 'NoneType' and 'int'
• Firstoutputwentwell,andfixesthebugwehadbefore. Thatis,wewantanyvalue>=2tobeasverboseas
possible.
• Thirdoutputnotsogood.
Let’sfixthatbug:
9

### 第10页

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
print(f"{args.square}^2 == {answer}")
else:
print(answer)
We’vejustintroducedyetanotherkeyword,default. We’vesetitto0inordertomakeitcomparabletotheother
intvalues. Rememberthatbydefault,ifanoptionalargumentisn’tspecified,itgetstheNonevalue,andthatcannot
becomparedtoanintvalue(hencetheTypeErrorexception).
And:
$ python prog.py 4
16
Youcangoquitefarjustwithwhatwe’velearnedsofar, andwehaveonlyscratchedthesurface. Theargparse
moduleisverypowerful,andwe’llexploreabitmoreofitbeforeweendthistutorial.
6 Getting a little more advanced
Whatifwewantedtoexpandourtinyprogramtoperformotherpowers,notjustsquares:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
print(f"{args.x} to the power {args.y} equals {answer}")
elif args.verbosity >= 1:
print(f"{args.x}^{args.y} == {answer}")
else:
print(answer)
Output:
$ python prog.py
usage: prog.py [-h] [-v] x y
prog.py: error: the following arguments are required: x, y
$ python prog.py -h
usage: prog.py [-h] [-v] x y
positional arguments:
x the base
y the exponent
(continuesonnextpage)
10

### 第11页

(continuedfrompreviouspage)
options:
-h, --help show this help message and exit
-v, --verbosity
$ python prog.py 4 2 -v
4^2 == 16
Notice that so far we’ve been using verbosity level to change the text that gets displayed. The following example
insteadusesverbosityleveltodisplaymoretextinstead:
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
print(f"Running '{__file__}'")
if args.verbosity >= 1:
print(f"{args.x}^{args.y} == ", end="")
print(answer)
Output:
$ python prog.py 4 2
16
$ python prog.py 4 2 -v
4^2 == 16
$ python prog.py 4 2 -vv
Running 'prog.py'
4^2 == 16
6.1 Specifying ambiguous arguments
Whenthereisambiguityindecidingwhetheranargumentispositionalorforan argument, -- canbe usedto tell
parse_args()thateverythingafterthatisapositionalargument:
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-n', nargs='+')
>>> parser.add_argument('args', nargs='*')
>>> # ambiguous, so parse_args assumes it's an option
>>> parser.parse_args(['-f'])
usage: PROG [-h] [-n N [N ...]] [args ...]
PROG: error: unrecognized arguments: -f
>>> parser.parse_args(['--', '-f'])
Namespace(args=['-f'], n=None)
>>> # ambiguous, so the -n option greedily accepts arguments
>>> parser.parse_args(['-n', '1', '2', '3'])
Namespace(args=[], n=['1', '2', '3'])
>>> parser.parse_args(['-n', '1', '--', '2', '3'])
Namespace(args=['2', '3'], n=['1'])
11

### 第12页

6.2 Conflicting options
So far, we have been working with two methods of an argparse.ArgumentParser instance. Let’s introduce a
thirdone,add_mutually_exclusive_group(). Itallowsforustospecifyoptionsthatconflictwitheachother.
Let’salsochangetherestoftheprogramsothatthenewfunctionalitymakesmoresense:we’llintroducethe--quiet
option,whichwillbetheoppositeofthe--verboseone:
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
if args.quiet:
print(answer)
elif args.verbose:
print(f"{args.x} to the power {args.y} equals {answer}")
else:
print(f"{args.x}^{args.y} == {answer}")
Ourprogramisnowsimpler,andwe’velostsomefunctionalityforthesakeofdemonstration. Anyways,here’sthe
output:
$ python prog.py 4 2
4^2 == 16
$ python prog.py 4 2 -q
16
$ python prog.py 4 2 -v
4 to the power 2 equals 16
$ python prog.py 4 2 -vq
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
$ python prog.py 4 2 -v --quiet
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
Thatshouldbeeasytofollow. I’veaddedthatlastoutputsoyoucanseethesortofflexibilityyouget, i.e. mixing
longformoptionswithshortformones.
Beforeweconclude,youprobablywanttotellyourusersthemainpurposeofyourprogram,justincasetheydon’t
know:
import argparse
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
if args.quiet:
(continuesonnextpage)
12

### 第13页

(continuedfrompreviouspage)
print(answer)
elif args.verbose:
print(f"{args.x} to the power {args.y} equals {answer}")
else:
print(f"{args.x}^{args.y} == {answer}")
Notethatslightdifferenceintheusagetext. Notethe[-v | -q],whichtellsusthatwecaneitheruse-vor-q,
butnotbothatthesametime:
$ python prog.py --help
usage: prog.py [-h] [-v | -q] x y
calculate X to the power of Y
positional arguments:
x the base
y the exponent
options:
-h, --help show this help message and exit
-v, --verbose
-q, --quiet
7 How to translate the argparse output
The output of the argparse module such as its help text and error messages are all made translatable using the
gettextmodule. Thisallowsapplicationstoeasilylocalizemessagesproducedbyargparse. Seealsoi18n-howto.
Forinstance,inthisargparseoutput:
$ python prog.py --help
usage: prog.py [-h] [-v | -q] x y
calculate X to the power of Y
positional arguments:
x the base
y the exponent
options:
-h, --help show this help message and exit
-v, --verbose
-q, --quiet
The strings usage:, positional arguments:, options: and show this help message and exit are
alltranslatable.
In order to translate these strings, they must first be extracted into a .po file. For example, using Babel, run this
command:
$ pybabel extract -o messages.po /usr/lib/python3.12/argparse.py
This command will extract all translatable strings from the argparse module and output them into a file named
messages.po. ThiscommandassumesthatyourPythoninstallationisin/usr/lib.
Youcanfindoutthelocationoftheargparsemoduleonyoursystemusingthisscript:
13

### 第14页

import argparse
print(argparse.__file__)
Oncethemessagesinthe.pofilearetranslatedandthetranslationsareinstalledusinggettext,argparsewillbe
abletodisplaythetranslatedmessages.
Totranslateyourownstringsintheargparseoutput,usegettext.
8 Custom type converters
Theargparsemoduleallowsyoutospecifycustomtypeconvertersforyourcommand-linearguments. Thisallows
you to modify user input before it’s stored in the argparse.Namespace. This can be useful when you need to
pre-processtheinputbeforeitisusedinyourprogram.
Whenusingacustomtypeconverter,youcanuseanycallablethattakesasinglestringargument(theargumentvalue)
andreturnstheconvertedvalue. However,ifyouneedtohandlemorecomplexscenarios,youcanuseacustomaction
classwiththeactionparameterinstead.
Forexample,let’ssayyouwanttohandleargumentswithdifferentprefixesandprocessthemaccordingly:
import argparse
parser = argparse.ArgumentParser(prefix_chars='-+')
parser.add_argument('-a', metavar='<value>', action='append',
type=lambda x: ('-', x))
parser.add_argument('+a', metavar='<value>', action='append',
type=lambda x: ('+', x))
args = parser.parse_args()
print(args)
Output:
$ python prog.py -a value1 +a value2
Namespace(a=[('-', 'value1'), ('+', 'value2')])
Inthisexample,we:
• Createdaparserwithcustomprefixcharactersusingtheprefix_charsparameter.
• Definedtwoarguments,-aand+a,whichusedthetypeparametertocreatecustomtypeconverterstostore
thevalueinatuplewiththeprefix.
Withoutthecustomtypeconverters,theargumentswouldhavetreatedthe-aand+aasthesameargument,which
wouldhavebeenundesirable. Byusingcustomtypeconverters,wewereabletodifferentiatebetweenthetwoargu-
ments.
9 Conclusion
The argparse module offers a lot more than shown here. Its docs are quite detailed and thorough, and full of
examples. Havinggonethroughthistutorial,youshouldeasilydigestthemwithoutfeelingoverwhelmed.
14

