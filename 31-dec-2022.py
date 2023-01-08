#regular expressions

import re
str = "My name is Anurag"
a = re.search("^My.*Anurag$", str)
if a:
    print("Match found")
else:
    print("No match found")

#__________________________________

import re
str = "My name is Anurag"
a = re.findall("n", str)
print(a)
if a:
    print("Match found")
else:
    print("No match found")

#__________________________________

import re
str = "My name is Anurag"
a = re.split("\s",str,1)
print(a)

#__________________________________

import re
str = "My name is Anurag"
a = re.sub("\s","2",str,2)
print(a)
  
#__________________________________