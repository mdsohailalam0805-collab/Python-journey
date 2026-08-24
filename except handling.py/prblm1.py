#-> exception handling
try:
  num= int(input("enter a num:"))
  result = 50 / num
  print(f'reuslt:{result}')

except ZeroDivisionError:
   print("you can't devide number by 0")

except ValueError:
   print('please  enter a valid number ')

finally:
   print("program execution completed")

