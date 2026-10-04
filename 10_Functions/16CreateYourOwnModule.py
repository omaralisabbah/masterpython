# ------------------------------------------------------
# Python Modules (Built In Modules)
# ---------------------------------
# You can create your own modules
# ------------------------------------------------------
# Notes: We can add more pathes in run time to add modules
# ------------------------------------------------------


#
import sys

#
sys.path.append(r"/home/ingenium/github/masterpython/10_Functions")

# Printing python system pathes (to import your own module)
print(sys.path)


print("=============================================")


# 
import MyOwnModule

print(dir(MyOwnModule))

MyOwnModule.MyOwn_Method01("Omar")
MyOwnModule.MyOwn_Method02("Ali")
MyOwnModule.MyOwn_Method03("Sabbah")


print("=============================================")


# Creating alias for your module
import MyOwnModule as zThreeMethods

zThreeMethods.MyOwn_Method01("Omar")
zThreeMethods.MyOwn_Method02("Ali")
zThreeMethods.MyOwn_Method03("Sabbah")


print("=============================================")


#
from MyOwnModule import MyOwn_Method01 as zTM
zThreeMethods.MyOwn_Method01("Robototype")

#
from MyOwnModule import MyOwn_Method01
zTM("Robototype From Alias")