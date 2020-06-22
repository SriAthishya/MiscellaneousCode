def palin(str1):
  a=len(str1)//2
  for i in range(0,a):
    for j in range(-1,a):
      
      if str1[i]==str1[j]:
        return("Palindrome")
      else:
        return("Not Palindrome")

#Matrix Multiplication
def matrix_mul(m1,m2):
  m3=[[0,0],
      [0,0]]
  for i in range(len(m1)):
      for j in range(len(m2)):
        for k in range(len(m3)):
          m3[i][j]+=m1[i][k]*m2[k][j]
  return m3
  

#Matrix Addition
def matrix_add(m1,m2):
  m4=[[0,0],
    [0,0]]
  for i in range(len(m1)):
      for j in range(len(m2)):
        m4[i][j]=m1[i][j]+m2[i][j]
  return m4

#display letters after last vowel of the string
def stringee(str10):
    lt=[]
    for i in range(0,len(str10)):
        if str10[i] in "aeiou":
            lt.append(i)
    j=max(lt)+1
    str12=str10[j:]
    return(str12)
