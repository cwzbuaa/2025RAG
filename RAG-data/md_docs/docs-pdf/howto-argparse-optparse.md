### 第1页

Migrating optparse code to argparse
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
Theargparsemoduleoffersseveralhigherlevelfeaturesnotnativelyprovidedbytheoptparsemodule,including:
• Handlingpositionalarguments.
• Supportingsubcommands.
• Allowingalternativeoptionprefixeslike+and/.
• Handlingzero-or-moreandone-or-morestylearguments.
• Producingmoreinformativeusagemessages.
• Providingamuchsimplerinterfaceforcustomtypeandaction.
Originally,theargparsemoduleattemptedtomaintaincompatibilitywithoptparse. However,thefundamental
designdifferencesbetweensupportingdeclarativecommandlineoptionprocessing(whileleavingpositionalargument
processing to application code), and supporting both named options and positional arguments in the declarative
interfacemeanthattheAPIhasdivergedfromthatofoptparseovertime.
Asdescribedinchoosing-an-argument-parser, applicationsthatarecurrentlyusingoptparseandarehappywith
thewayitworkscanjustcontinuetouseoptparse.
Applicationdevelopersthatareconsideringmigratingshouldalsoreviewthelistofintrinsicbehaviouraldifferences
describedinthatsectionbeforedecidingwhetherornotmigrationisdesirable.
Forapplicationsthatdochoosetomigratefromoptparsetoargparse,thefollowingsuggestionsshouldbehelpful:
• Replacealloptparse.OptionParser.add_option()callswithArgumentParser.add_argument()
calls.
• Replace(options, args) = parser.parse_args()withargs = parser.parse_args()andadd
additionalArgumentParser.add_argument()callsforthepositionalarguments. Keepinmindthatwhat
waspreviouslycalledoptions,nowintheargparsecontextiscalledargs.
• Replace optparse.OptionParser.disable_interspersed_args() by using
parse_intermixed_args()insteadofparse_args().
• Replacecallbackactionsandthecallback_*keywordargumentswithtypeoractionarguments.
• Replacestringnamesfortypekeywordargumentswiththecorrespondingtypeobjects(e.g. int,float,complex,
etc).
• Replace optparse.Values with Namespace and optparse.OptionError and optparse.
OptionValueErrorwithArgumentError.
1

### 第2页

• Replacestringswithimplicitargumentssuchas%defaultor%progwiththestandardPythonsyntaxtouse
dictionariestoformatstrings,thatis,%(default)sand%(prog)s.
• Replace the OptionParser constructor version argument with a call to parser.
add_argument('--version', action='version', version='<the version>').
2

