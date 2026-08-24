#using list constructor
sitamarhi=list(("akhta", "suppi", "bairganiya"))
print(sitamarhi)


#update with f-string
college=["class","library","lab"]
print(f'before college {college}')
college[0]="hostel"
college[1:2]="ground","building"
print(f'after college {college}')

#repeat list
munawwar="montu boss"
print((munawwar +"\n") * 10)


#membership to check things present in code or not.
station=["train","shop","passenger","ticket"]
if "train" in station:
    print("found")
else:
   print("not found")



college=["class","library", "canteen"]
print(college)
#change list items:
college[2]="hostel"
print(college)
#add items:
college.append("lab")
print(college)
#remove itemm
college.remove("library")
print(college)
#add item at any position
college.insert(0,"girls hostel")
print(college)


#insert
a=[1,2,3]
a.insert(1,-6)
print(a) 
#remove by value
a=[1,2,3]
a.remove(3)
print(a)
#pop-remove by position
a=[1,2,3]
a.pop(0)
print(a)
#sort list
a=[1,2,3,6,9,6]
a.sort()
print(a)


#list concate method
sohail=[1,2,3]
saif=[4,5,6]
result=sohail+saif
print(result)

#extend method
a=[1,2,3]
b=[4,5,6,7]
a.extend(b)
print(a) 

#reverse method
a=[1,2,3,4]
a.reverse()
print(a)


#minimum and maximum
a=[500,232,-562]
print(min(a))
print(max(a))