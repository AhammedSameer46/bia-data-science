students=["Ahammed","Sameer","Ahad",]
#print(students)
students[2]="jasneem"
#print(students)

## apend()

fruits=["apple","banana","orange"]
fruits.append("green apple")
#print(fruits)

#insert()
students1=["Ahammed","Ahad",]
students1.insert(1,"sameer")
#print(students1)

#remove()
students1=["Ahammed","Ahad",]
students1.remove("Ahad")
#print(students1)

#pop()
students1=["Ahammed","Ahad",]
students1.pop(1)
#print(students1)

#len()
students1=["Ahammed","Ahad",]
print(len(students1))




#sort()
numbers=[5,2,9,1,3]
numbers.sort()
#print(numbers)



#reverse()
numbers=[5,2,9,1,3]
numbers.sort()  
numbers.reverse()
#print(numbers)

#count()
fruits=["apple","banana","orange","apple"]
fruits.count("apple")
print(fruits.count("apple"))


#index()

fruits=["apple","banana","orange","apple"]
print(fruits.index("banana"))
