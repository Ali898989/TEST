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
for mm in range(3):
     print (mm," ali")



"""
print (cyan,test)
print (g)
all = input("-------->")
all2 = input("-------->")
all3 = input("-------->")

gg.close()
if all == "0 ali"and all2 == "1 ali"and all3 == "2 ali":
   
   print (p,"good ",g,"Level +1")
   
   new = (int(max)+1)
   new1 = str(new) 
   gg2 = open("/data/data/com.termux/files/home/level.txt","w")
   
   gg2.write(new1)
   
   gg2.close()
   aa("TEST")
else :
   print (p,"error ",r,"Level -1")
   
   new = (int(max)-1)

   new1 = str(new)
   gg2 = open("/data/data/com.termux/files/home/level.txt","w")
   gg2.write(new1)
   gg2.close()
   aa("TEST")
