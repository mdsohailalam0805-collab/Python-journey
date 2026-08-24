#string length (without len)
s="sohail"
count=0
for ch in s:
    count+=1
print(count)
 

#reverse string
s="sohail"
rev=""
for ch in s:
    rev=ch+rev
print(rev)


#palindrome string
s=input("enter a text")
if s==s[::-1]:
    print ("palindrome")
else:
    print("not palindrome")


#print vowels
s="I am The Biggest Fan of 45"
count=0
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        count+=1
print(count)


#count words
s= "discipline is the ultimate form of self respect"
count=1
for ch in s:
    if ch==" ":
        count+=1
print(count)

#2nd mehtod
text="i love bauni junior"
words=text.split()
print(len(words))

#uppercase to lowercase
s= 'MD SOHAIL ALAM'
print(s.lower())

#remove spaces from strings
s="you can speak english"
print(s.replace(" ",""))

#replace words
words="you is a my brother"
print(words.replace("is","are"))

#find character frequency
text="impossible says i'm possible"
ch='s'
print(text.count(ch))
 
#2nd method
text="impossible says i am possible"
count=0
ch='a'
for l in text:
    if l==ch:
        count+=1
print(count)

#check anagram
#race-care
s1='listen'
s2='silent'
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")