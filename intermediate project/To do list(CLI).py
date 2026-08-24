
print(" To do List minor project")

tasks=[]

while True:
    
    print("\n1.add tasks")
    print("2.view tasks")
    print("3.delete tasks")
    print("4.Exit")
    
    choice=input("enter  your choice:")
    
    if choice =="1":
        task=input("enter tasks:")
        tasks.append(task)
        
    elif choice=="2":
        if len(tasks)==0:
            print("no tasks found")
        else:
            for i in range(len(tasks)):
                print(i+1 ,".", tasks[i])
                
    elif choice=="3":
        num=int(input("enter task number to delete"))
        if 0<num<=len(tasks):
            tasks.pop(num-1)
            print("task deleted")  
        else:
            print("invalid task number")          
            
    elif choice=="4":
        print("exiting....")
        break
    
    else:
        print("invalid choice")      


