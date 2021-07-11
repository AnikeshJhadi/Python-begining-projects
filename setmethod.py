set1={"banana","apple","grapes"}
print("Items in the set 1:-")
print(set1)
set1.add("mango")
print("Set 1 after adding:-")
print(set1)
set2=set1.copy()
print("Items in the set 2 after copying from set 1:-")
print(set2)
set1.clear()
print("Items in the set 1 after clearing:-")
print(set1)
set3={"kiwi","pineapple","pomegranate","mango"}
print("Items in set 3:-")
print(set3)
set4=set2.difference(set3)
print("Difference of set 2 and set 3:-")
print(set4)
set5=set2.difference_update(set3)
print("Difference update of set 2 and set 3:-")
print(set5)
set2.discard("apple")
print("Set 2 after removing \"apple\":-")
print(set2)
set6={"Mumbai","Chennai","Newdelhi"}
print("Items of set 6 are:-")
print(set6)
set7={"Bangalore","Mumbai","Kolkata"}
print("Items of set 7 are:-")
print(set7)
print("Intersection of set 6 and set 7:-")
print(set6.intersection(set7))
print("Intersection update of set 6 and set 7:-")
set6.intersection_update(set7)
print(set6)
set8={"Google","Microsoft","Apple"}
print("Items of set 8 are:-")
print(set8)
set9={"Microsoft","Alphabet","Facebook"}
print("Items of set 9 are:-")
print(set9)
z=set8.isdisjoint(set9)
if z==True:
    print("Sets are disjoint")
else:
    print("Not disjoint")
set10={"Google","Microsoft","Apple","Alphabet","Facebook"}
print("Items of set 10 are:-")
print(set10)
set11={"Microsoft","Alphabet"}
print("Items of set 11 are:-")
print(set11)
x=set11.issubset(set10)
if x==True:
    print("Set 11 is subset of set 10")
else:
    print("Set 11 is not a subset of set 10")
x=set10.issuperset(set11)
if x==True:
    print("Set 10 is superset of set 11.")
else:
    print("Set 10 is not a superset of set 11.")
set10.pop()
print("Set 10 after popping:-")
print(set10)
set12={"silver","gold","copper","platinum","iron"}
print("Items of set 12 are:-")
print(set12)
set12.remove("gold")
print("Set12 after removing element \"gold\":-")
print(set12)
set13={"chemistry","physics","biology"}
print("Items of set 13 are:-")
print(set13)
set14={"maths","history","chemistry","computer"}
print("Items of set 14 are:-")
print(set14)
z=set13.symmetric_difference(set14)
print("Set after symmetric difference of set 13 and set 14:-")
print(z)
set13.symmetric_difference_update(set14)
print("Set 13 after symmetric difference update of set 13 and set 14:-")
print(set13)
z=set13.union(set14)
print("Union set of set 13 and set 14:-")
print(z)
set15={"abc","xyz","pqr"}
print("Items of set 15 are:-")
print(set15)
set16={"123","abc","xyz","lmn"}
print("Items of set 15 are:-")
print(set16)
set15.update(set16)
print("Set 15 after updation from set 16:-")
print(set15)
