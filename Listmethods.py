list1=["banana","apple","grapes"]
print("Items in the list 1:-")
print(list1)
list1.append("mango")
print("List 1 after appending:-")
print(list1)
list2=list1.copy()
print("Items in the list 2 after copying from list 1:-")
print(list2)
list1.clear()
print("Items in the list 1 after clearing:-")
print(list1)
print("No of element \"mango\" in the list 2:-"+str(list2.count("mango")))
list3=["banana","kiwi","orange"]
print("Items in the list 3:-")
print(list3)
list2.extend(list3)
print("List 2 after extending by list 3:-")
print(list2)
print("Index of element \"grapes\" in list 2:-"+str(list2.index("grapes")))
list2.insert(3,"guava")
print("List 2 after inserting element \"guava\" in index 3:-")
print(list2)
list2.pop(5)
print("List 2 after popping the element present at index 5:-")
print(list2)
list2.remove("apple")
print("List 2 after removing element \"apple\":-")
print(list2)
list2.reverse()
print("List 2 after reversing:-")
print(list2)
list2.sort()
print("List 2 after sorting:-")
print(list2)


    

    
        
      
