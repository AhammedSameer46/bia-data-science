def greet(name):
    print("My name is",name,"i am a python programmer")

greet("Ahammed")


## Addition of two numbers

def add(a,b):
    return a+b

result = add(10,20)
print("The sum of two numbers is:",result)


def square(num):
    return num*num

result = square(5)
print("The square of the number is:",result)





def student_info(name,age,course):
    print("My name is ",name,"and my age is ",age,"and I am studying ",course)


    
student_info("Ahammed",21,"computer science")




## looping through a def

def print_numbers():
    for i in range(1,11):
        print(i)

print_numbers()




### def list

def show_students():
    students = ["Ahammed", "Ali", "Ahmed", "Abdul"]

    for student in students:
        print(student)

show_students()





def personal_info():
    bio_data={
        "name":"Ahammed",
        "age":21,
        "course":"computer science"
    }

    data_scinece={
        "python":"intermediate",
        "numpy":"beginner",
        "pandas":"beginner",
        "machine learning":"intermediate"
    }

    print("My name is ",bio_data["name"],"and my age is ",bio_data["age"],"and I am studying ",bio_data["course"])
    print("My python skill level is ",data_scinece["python"])
personal_info()