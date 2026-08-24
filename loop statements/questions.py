"""for i in range(1,100):
    if i %2==0:
        continue
        print('even',i)
    else:
        print('odd',i)
 """

"""num=int(input('enter  a number'))
if num %2==0:
 print('even')
else:  
 print('odd')"""


start=int(input('enter a start number'))
stop=int(input('enter a stop number'))

hold=int(input('enter a hold number'))
for sohail in range(start,stop):
 if sohail==hold:
  break
 print(sohail)