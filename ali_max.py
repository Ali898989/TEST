g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
from os import system as aa
aa("clear")
gg = open("level.txt","r")
max = gg.read()


print (p,"            ali_max",g," ahmed",y,"Level ",max)
print (" ")
print (" ")
print (y,"(",g,"1",y,")",cyan," ")
print (y,"(",g,"2",y,")",cyan," bvhvc")
ali = input("--------> ")
if ali == "1":
  aa("cd TEST && python 1.py")
elif ali == "2":
  aa("cd TEST && python 2.py")
else :
  aa("TEST")
