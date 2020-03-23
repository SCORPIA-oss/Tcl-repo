import setuptools
with open('Tcl/README.md', 'r') as rd:
	read = rd.read()


setuptools.setup(
	name = "Tcl",
	version = "0.1",


	author = "Repl.it Developer",
	author_email = "xsumagravity@gmail.com",


	description = "A coding language used for Graphical user interface",


	ld = rd,
	url = "",


	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: MacOS",
	]
)
