import string
def is_abecedarian(str1):
  a=str1.lower()
  coun=0
  lt=[]
  b=string.ascii_lowercase
  for i in range(0,len(a)-1):
    if a[i] in b :
      n1=ord(a[i])
      n2=ord((a[i+1]))
      if(n1<n2):
        coun+=1
        lt.append(coun)
      else:
        coun=0
      maxi=max(lt)
    
  return(maxi)

def anagram(lt):
  new=[]
  for i in lt:
    for j in lt:
      if i!=j and (sorted(i))==(sorted(j)):
        new.append(i)
  ''' 
  for i in new:
    if i in lt:
      lt.remove(i)
  '''
  return new

def subinary(str1):
  coun=0
  if '101' in str1:
    coun+=1
    a=str1.index("101")
  
  return str(coun)+str(a)

def vowels(str1):
  dic={}
  coun=0
  str1=str1.split()
  
  for i in str1:
    for j in i:
      if j in 'aeiouAEIOU':
        coun+=1
        if i not in dic.values():
          dic[coun]=i
  a=sorted(dic.values(),reverse=True)
  return a

def spring_mat(m1):
  str1=""
  a=len(m1)//2
  for i in range(0,a):
    for j in range(0,len(m1)):
      str1+=str(m1[i][j])
  for i in range(a,len(m1)):
    for j in range(-1,a):
      str1+=str(m1[i][j])
  return str1

def mid_palin(str1):
  i=0
  j=-1
  coun=0
  str2=""
  while i<=len(str1)-1:
    if(str1[i]==str1[j]):
      str2+=str1[i]
    j-=1
    i+=1
  coun=len(str2)
  return coun
