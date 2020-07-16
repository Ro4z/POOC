from datetime import datetime

list=[]

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
alertMsg = "out of visual range"
list.append([date,alertMsg])

for i in range(0,len(list)):
    print(list[i][0] + "    " + list[i][1])
