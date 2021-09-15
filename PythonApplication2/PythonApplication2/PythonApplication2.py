



times=[]
i=0

a=input()
b=list(a.split())
n=int(b[0])
s=int(b[1])
x=0

for i in range(n):
 times.append(int(input()))
times.sort()
if s>=n :
 print ('INF')
else : 
 minimum=int(times[s])-int(times[0])
 for m in range(len(times)-s):
   if int(times[s+m])-int(times[m]) < minimum:
    minimum=int(times[s+m])-int(times[m])
   if int(times[s+m])-int(times[m]) == 0 :
    x=x+1


 if (x == 1) or (s == 0):
  print('Impossible')
 else : 
  print (minimum)

