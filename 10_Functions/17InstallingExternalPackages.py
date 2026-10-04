# ------------------------------------------------------
# Installing External Packages
# ----------------------------
# Module vs Package
#
# Built in Modules List "https://docs.python.org/3/py-modindex.html"
#
# External packages can be downloaded from the internet
# Using Python package manager PIP
#
# PIP installs the package and it is dependencies
# Package and Modules Directory "https://pypi.org/"
# PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# 
# ------------------------------------------------------
# Notes: 
# ------------------------------------------------------


# First thing you need to see if you have a package manager (from terminal)
# pip --version >> pip 25.1.1 from /usr/lib/python3/dist-packages/pip (python 3.14)
# pip list >> to list the packages
# If you want to install a package (pip install <package_name> or <module_name>)

import termios

print(dir(termios))