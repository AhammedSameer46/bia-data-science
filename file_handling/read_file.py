with open("file_handling/student.txt",'r') as file:
    content=file.read()
print(content)




## TO Write a File
with open ("file_handling/student.txt",'w') as file:
        file.write("Ahad")



## Append (a)

with open ("file_handling/student.txt",'a') as file:
        file.write("\nComputer Science")


