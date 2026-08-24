student={
    "name":"sohail", "age":20 , "marks":81.4 , "course":"python"
}
print(student)

#add method
student["session"]=(2024,2028)
print(student)


#update details
student["age"]=18
print(student)


#delete details
del student["marks"]
print(student)