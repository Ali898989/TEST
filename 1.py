g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
r='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
gg = open("/data/data/com.termux/files/home/level.txt","r")
max = gg.read()
from os import system as aa
aa("clear")
test = """
a = "ali_max"
print (a)




"""
print (cyan,test)

all = input("-------->")
gg.close()
if all == "ali_max":
   print (p,"good ",g,"Level +1")
   new = (int(max)+1)
   new1 = str(new) 
   gg2 = open("/data/data/com.termux/files/home/level.txt","w")
   
   gg2.write(new1)
   
   gg2.close()
   aa("TEST")
else :
   print (p,"error ",r,"Level -1")
   new2 = (int(max))-(1)
   gg2 = open("/data/data/com.termux/files/home/level.txt","w")
   gg2.write(new2)
   gg2.close()
   aa("TEST")
