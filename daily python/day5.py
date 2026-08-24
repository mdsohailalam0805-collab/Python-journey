#tuple indexing
tpl=(5,4,6,8,3)
print(tpl[4])

#convert tuple →list
tuple=(10,5,0,1)
print(list(tuple))

#set remove duplicate
a=(2,4,5,6,4,2,5)
b=set(a)
print(b)

#dictionary keys print
identity={'name': 'sohail', 'age': 20}
print(identity.keys())

#dictionary values print
s={'name': 'sohail', 'DOB':'4/08/05'}
e=s.values()
print(e)
 
#update dictionary
altamsh={"name":"sohail", "age":20}
altamsh["age"]=21
print(altamsh)
#2nd method
altamsh={"name": "sohail", "age":25, "course":"(ai&ml)"}
altamsh.update({"age":20,"course":"CSE"})
print(altamsh)


#count value frequency(bar bar aana)
text="i am not always right but never wrong"
count=0
ch="n"
for letter in text:
    if letter==ch:
     count+=1
print(count) 


#max value key
marks={1:80, 2:90,6:80}
print(max(marks, key=marks.get))

#sort dictionary
d={"b":1, "c":3, "a":10}
sohail=dict(sorted(d.items()))
print(sohail)