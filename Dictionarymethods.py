dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Dictionary 1:-")
print(dict1)
dict2=dict1.copy()
print("Dictionary 2 after copying from dictionary 1:-")
print(dict2)
dict1.clear()
print("Dictionary 1 after clearing:-")
print(dict1)
dict3=("abc","xyz","123")
z=0
dict4=dict.fromkeys(dict3,z)
print("Dictionary 4:-")
print(dict4)
print("Model of dictionary 2:-"+str(dict2.get("model")))
dict2.pop("model")
print("Dictionary 2 after popping the element \"model\":-")
print(dict2)
dict2.popitem()
print("Dictionary 2 after popping last inserted item:-")
print(dict2)
z=dict2.setdefault("Color","White")
print("Color of dictionary 2:-"+str(z))
dict2.update({"gear":"5"})
print("Dictionary 2 after updation of element \"gear\":-")
print(dict2)
list3=dict2.values()
print("List 3 having values of dictionary 2:-")
print(list3)

