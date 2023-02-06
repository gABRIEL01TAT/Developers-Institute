store = {
    'name': 'mango',
    'number': 5,
    'item': 'fruits'
}

am_store = {
    'name': 'Apple',
    'number': 9,
    'item': 'vegetable'
}

#print(store.items())

for key, value in store.items():
    print(key, '->', value)










shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]

for y in shirts:
    print(y["name"])







sample_dict = {
   "class":{
      "student" : {
         "name" : "Mike",
         "marks" : {
            "physics" : 70,
            "history" : 80
         }
      }
   }
}

#for a in sample_dict:

print(sample_dict["class"]["student"]["marks"]["history"])






sample_dicts = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}
key_to_remove = ["name", "salary"]
for key in key_to_remove:
    del sample_dicts[key]
print(sample_dicts)



list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

(1, 'a', 1.1)
(2, 'b', 2.2)
(3, 'c', 3.3)









