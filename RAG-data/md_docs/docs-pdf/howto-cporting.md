### 第1页

Porting Extension Modules to Python
3
Release 3.14.0rc3
Guido van Rossum and the Python development team
October01,2025
PythonSoftwareFoundation
Email: docs@python.org
Contents
WerecommendthefollowingresourcesforportingextensionmodulestoPython3:
• The Migrating C extensions chapter from Supporting Python 3: An in-depth guide, a book on moving from
Python2toPython3ingeneral,guidesthereaderthroughportinganextensionmodule.
• ThePortingguidefromthepy3cprojectprovidesopinionatedsuggestionswithsupportingcode.
• RecommendedthirdpartytoolsofferabstractionsoverthePython’sCAPI.Extensionsgenerallyneedtobe
re-writtentouseoneofthem, butthelibrarythenhandlesdifferencesbetweenvariousPythonversionsand
implementations.
1

