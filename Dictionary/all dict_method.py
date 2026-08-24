#get value of key(no error if key missing)
adhar_card={
    'name':'sohail', 'DOB': '04/08/2005'
}
name=adhar_card.get('name')
print(name)


# key is missing (default value)
adhar_card={
    'name':'sohail', 'age':'20'
}
age=(adhar_card.get('DOB','not found'))
print(age)

#keys method
keys=adhar_card.keys()
print(list(keys))

#values method
values=adhar_card.values()
print(list(values))

#items- use when we need to print key and value both then we use item.
all_items=adhar_card.items()
print(list(all_items))

# pop (remove)
popped=adhar_card.pop('age')
print(popped)
print(adhar_card)

#clear method
cleared=adhar_card.clear()
print(cleared)
print(adhar_card)

# loop_dict.py
adhar_card={
    'name':'sohail', 'age':20
}
for k in adhar_card.values():
    print(k)