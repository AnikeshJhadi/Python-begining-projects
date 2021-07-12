str1 = "hello, my name is anikesh."
print("String 1:-"+str1)
txt= str1.capitalize()
print ("String 1 after capitalization:-"+txt)
str2 = "MYCAPTAIN"
print("String 2:-"+str2)
txt= str2.casefold()
print ("String 2 after casefold i.e.lowercase:-"+txt)
txt=str2.center(30,"!")
print("String 2 after centre alignment with \"!\" symbol:-"+txt)
str3="I have a car and they have a bike"
print("String 3:-"+str3)
count=str3.count("have")
print("String 3 count of \"have\":-"+str(count))
str4="Hi,iåm ånikesh"
print("String 4:-"+str4)
txt=str4.encode()
print("String 4 after encoding:-"+str(txt))
i=input("Enter the end you have to check:-")
txt=str4.endswith(i)
if txt==True:
    print("String 4 ends with "+str(i))
else:
    print("String 4 does not ends with "+str(i))
str5="A\tn\ti\tk\te\ts\th"
print("String 5:-"+str5)
txt=str5.expandtabs(5)
print("String 5 after expanding tabs:-"+txt)
txt=str3.index("car")
print("Index of car in String 3:-"+str(txt))
txt=str3.find("bike")
print("Position of bike in String 3:-"+str(txt))
str6="Price of petrol is {price:.3f} rupees."
print("String 6:-"+str6)
print("String 6 after formating:-"+str6.format(price=98.5))
str7=input("Enter the string to check alphanumeric:-")
txt=str7.isalnum()
if txt==True:
    print("String is alphanumeric")
else:
    print("Not  an alphanumeric string")
str8=input("Enter the string to check alphabetic:-")
txt=str8.isalpha()
if txt==True:
    print("String is alphabet")
else:
    print("String is not an alphabet")
str9=input("Enter the string to check decimal:-")
txt=str9.isdecimal()
if txt==True:
    print("String is a decimal")
else:
    print("String is not a decimal")
str10=input("Enter the string to check digit:-")
txt=str10.isdigit()
if txt==True:
    print("String is a digit")
else:
    print("String is not a digit")
str11=input("Enter the string to check identifier:-")
txt=str11.isidentifier()
if txt==True:
    print("String is identifier")
else:
    print("String is not identifier")
str12=input("Enter the string to check lowercase:-")
txt=str12.islower()
if txt==True:
    print("String is in lowercase")
else:
    print("String is not in lowercase")
str13=input("Enter the string to check numeric:-")
txt=str13.isnumeric()
if txt==True:
    print("String is numeric")
else:
    print("String is not numeric")
str4=input("Enter the string to check printable or not:-")
txt=str14.isprintable()
if txt==True:
    print("String is printable")
else:
    print("String is not printable")
str14=input("Enter the string to check whitespaces:-")
txt=str14.isspace()
if txt==True:
    print("String has complete whitespaces.")
else:
    print("String has not complete whitespaces.")
str15=input("Enter the string to check title:-")
txt=str15.istitle()
if txt==True:
    print("String is a title")
else:
    print("String is not a title")
str16=input("Enter the string to check uppercase:-")
txt=str16.islower()
if txt==True:
    print("String is in uppercase")
else:
    print("String is not in uppercase")
tup=("grapes","apple","mango")
print("Tuple:-"+tup)
str17="#".join(tup)
print("String 17 after joining tuple with #"+str17)
str18 = "banana"
print("String 18:-"+str18)
txt = str18.ljust(20)
print(txt, "is my favorite fruit.")
str19 = "     banana     "
print("String 19:-"+str19)
txt = str19.lstrip()
print("of all fruits", txt, "is my favorite")
str20 = "Hello Anikesh!"
print("String 20:-"+str20)
txt =str20.maketrans("k", "m")
print("String 20 after transition:-"+str20.translate(txt))
str21="I have lots of chocolates and cakes."
print("String 21:-"+str21)
txt=str21.partition("chocolates")
print("Tuple after partition of string 21 from \"chocolates\":-"+str(txt))
txt=str21.replace("chocolates","toys")
print("String 21 after replacing chocolates with toys:-"+txt)
str22="I ate an apple because apple is a healthy fruit"
print("String 22:-"+str22)
print("Index of \"apple\" from last in string 22 is:-"+str(str22.rindex("apple")))
print("Position of \"apple\" from last in string 22 is:-"+str(str22.rfind("apple")))
str23 = "banana"
print("String 23:-"+str23)
txt = str23.rjust(20)
print(txt, "is my favorite fruit.")
str24 = "     banana     "
print("String 24:-"+str24)
txt = str24.rstrip()
print("of all fruits", txt, "is my favorite")
str25="I have lots of chocolates and cakes."
print("String 25:-"+str25)
txt=str25.rpartition("chocolates")
print("Tuple after partition of string 21 from \"chocolates\":-"+str(txt))
str26 = "apple, banana, cherry"
print("String 26:-"+str26)
txt = str26.rsplit(", ")
print("List after spliting of string 26 from right:-"+str(txt))
str27 = "apple, banana, cherry"
print("String 27:-"+str27)
txt = str27.split(", ")
print("List after spliting of string 27:-"+str(txt))
str28="Iam a BTech. undergraduate\nIam 20"
print("String 28:-"+str28)
txt=str28.splitlines()
print("List of string 28 after lines splitting:-"+str(txt))
i=input("Enter the start you have to check:-")
txt=str28.startswith(i)
if txt==True:
    print("String 28 starts with "+str(i))
else:
    print("String 28 does not starts with "+str(i))
str29 = "     banana     "
print("String 29:-"+str24)
txt = str29.strip()
print("of all fruits", txt, "is my favorite")
str30="Anikesh Jhadi"
print("String 30:-"+str30)
txt=str30.swapcase()
print("String 30 after case swapping:-"+txt)
str31="the legends of narnia"
print("String 31:-"+str31)
txt=str31.title()
print("String 31 after converting into a title:-"+txt)
txt={83:80}
str32="Savagge"
print("String 32:-"+str32)
print("String 32 after translation:-"+str32.translate(txt))
str33="anikesh  the legend"
print("String 33:-"+str33)
txt=str33.upper()
print("String 33 in upper case:-"+txt)
str34="218"
print("String 34:-"+str34)
txt=str34.zfill(10)
print("String 34 after zero filling of value 10:-"+txt)
