#Student management system
print("\nSTUDENT MANAGEMENT SYSTEM")
print("-------------------------")

#student database
student_grades={}

#add student
def add(name,grade):
    student_grades[name]=grade
    print(f"-->Added {name}: {grade}")

#update student
def update(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Updated student {name}: {grade}")
    else:
        print(f"{name} not found!")    

#delete student
def delete(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted...")        
    else:
        print(f"{name} not found!")    

#display student
def display():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"-->{name}: {grade}")
    else:
        print("No student found/added!")


while True:
        choice=int(input("\n\t1. Add Student\n\t2. Update Student\n\t3. Delete Student\n\t4. View Student\n\t5. Exit\nEnter the choice:"))
        if choice==1:
            name=input("\nEnter Name: ")
            grade=int(input("Enter Grade: "))
            add(name,grade)

        elif choice==2:
            name=input("\nEnter Name: ")
            grade=int(input("Enter Grade: "))
            update(name,grade)

        elif choice==3:
            name=input("\nEnter Name: ")
            delete(name)

        elif choice==4:
            display()

        elif choice==5:
            print("\nTHANK YOU!")
            print("-------------------------\n")
            break

        else:
            print("Invalid Input")        

      