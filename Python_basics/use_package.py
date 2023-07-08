#--------------------Approch 1----------------------
#import learn_package.A_module

#learn_package.A_module.a_function()

#--------------------Approch 2----------------------
#from learn_package import A_module
#A_module.a_function()

#--------------------Approch 3----------------------
from learn_package.A_module import a_function, b_function
a_function()
b_function()

#--------------------Doesnot Work----------------------
#import learn_package
#learn_package.A_module.a_function()