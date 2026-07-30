x=3+1j
com=1+0j
print(com)
print(x)
print(type(x))
print(type(com))
A=None             #to denote missing data
print(A)
print(type(A))
s1='hello'
s2="world"
s3="""this is
 multiple line"""
print(s1, s2)
print(s1+s2)
print(s3)
s="python"
print('s[0]=',s[0])
print('s[-1]=',s[-1])
print('s[1:4]=',s[1:4])  #count before the last number given here
print('s[:3]=',s[:3])    
print('s[::2]=',s[::2])    #: denote full copy when 2 implies that 2,5,7
print('Reverse:',s[::-1])
Shakkira= 'SOS|Shakkira UV|Data Science And Analytics|JULY2026|Morning|Offline'
print(Shakkira[4:12]+Shakkira[13:15]+Shakkira[16]+Shakkira[21]+Shakkira[33]+Shakkira[43:46]+Shakkira[49:51]+Shakkira[52]+Shakkira[60])
name="hi Shakkira"
print(name.upper())    #full capitalize
print(name.lower())    #full small letter
print(name.title())    #all first letters will be capital
print(name.capitalize())  #only the first letter will be capital
print(name.swapcase())    #capital letters will be small and vise versa
print(len(name))
print(name.find('S'))  #find the letter(if it is not here -1 will be the output)
print(name.split())      #split the sentence
t='this-is-a-good-tea'
print(t.split('-'))      #split by mention 
print(t.replace('good','bad'))     #change or replace a word
#translate a word by replace one by another
orig='aeiou'
tr=str.maketrans('aeiou','12345')
print('translate:','education'.translate(tr))
print('Hi everyone\nI am Shakkira from Thavanur\nage 25')    #new line
print('Hi everyone\tI am Shakkira from Thavanur\tage 25')    #space
#chnge the string into integer
num="123"
print(type(num))
y=int(num)    
print(y)
print(type(y))