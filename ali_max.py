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
gg = open("/data/data/com.termux/files/home/level.txt","r")
max = gg.read()


print (p,"            ali_max",g," ahmed",y,"Level ",max)
print (" ")
print (" ")
print (y,"(",g,"1",y,")",cyan," 3")
print (y,"(",g,"2",y,")",cyan," 0")
ali = input("--------> ")
if ali == "1":
  aa("cd $HOME/TEST && python 1.py")
elif ali == "2":
  aa("cd $HOME/TEST && python 2.py")
elif ali == "3":
  aa("cd $HOME && rm level.txt && echo '1' >> level.txt ")
else :
  aa("TEST")
