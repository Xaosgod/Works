
i=0
k=3
n=0
x=0
j=0
l=-1
t=0
h=0
y=0
answer=[]
vocab=[]
num=[]
prefix_words=[]
n = int(input())
slova=[]
for i in range(n) : 
 a=input()
 slova=(list(a.split()))
 if (slova[0]=='+'):
  x=0
  j=0
 
  while ((j<=l) and x==0 and l>-1):
   if slova[2]==vocab[j] :
     num[j]=(int(num[j])+int(slova[1]))
     x=1
   j=j+1
  if x==0 :
   vocab.append(slova[2])
   num.append(slova[1])
   l=l+1
 else :
  prefix_word = ''
  maximum = 0 
  t=0

  for h in range(len(vocab)) :
   if slova[1] == vocab[h][:len(str(slova[1]))] :
    prefix_word = vocab[h]    
    if int(num[h])>= maximum :
     if int(num[h])> maximum :
         maximum=int(num[h])
         t=h
     else:
       if (len(vocab[h])<len(vocab[t])):
        t=h   
  if maximum == 0 :
     answer.append(slova[1])
  else : 
     answer.append(vocab[t])
for i in range(len(answer)):
 print(answer[i])



  



