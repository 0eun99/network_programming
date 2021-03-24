import re

c1=[]
c2=[]
s = 'led=on&motor=off&switch=off'
def changeDic(words):
        for i in range(0,6,2):
          c1.append(words[i])
          c2.append(words[i+1])

        result = dict(zip(c1,c2))
        print(result)

dv_str = re.split('&|=', s)
changeDic(dv_str)