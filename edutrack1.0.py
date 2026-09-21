
import csv
student_list=[]
data="grades.csv"
with open(data) as file:
    reader=csv.DictReader(file)
    for i in reader:
        student_list.append(i)
def main():
    def menu():
        print("==============================================")
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Register a new student")
        print("2. Display all students")
        print("3. search for a new student")
        print("4. Update a student's grade")
        print("5. Generate performance report")
        print("6. Exit")
        print("==============================================")
        while True:
            try:
                menu_input=int(input("please choose an option: "))
                
            except ValueError:
                print("you should enter a number from 1 to 6 ")
            else:
                if menu_input>6 or menu_input<1:
                    print("you should enter a number from 1 to 6 ")
                else:
                    return menu_input
    def register():
        while True:
            new_name=input("please enter the new student name: ").strip().title()
            if new_name=='':
                print('name can not be empty! ')
            else: 
                break
        while True:
            try:
                new_grade=int(input("please enter the grade: "))
            except ValueError:
                print('grade should be a number and no decimal')
            else:
                if new_grade>100 or new_grade<0:
                    print("grade must be between 0 and 100 ")
                else:
                    break
        with open(data,"a",newline="") as file:
            writer=csv.DictWriter(file, fieldnames=['name','grade'])
            writer.writerow({'name':new_name,'grade':new_grade})
        student_list.append({"name": new_name, "grade": new_grade})
        print("student saved to the database succesfully!")
    def display_students():
        if not student_list:
                print("No students available!")
                return
        for student in student_list:
            print(f"name: {student["name"]}, grade: {student["grade"]}")
        print(f'total students: {len(student_list)}')
    def search_student():
        while True:
            while True:
                search_name=input("search student name:  ").strip()
                if search_name=='':
                    print('you did not enetr any name! ')
                else:
                    break
            search_result=False
            for student in student_list:
                if search_name.lower()==student["name"].lower():
                    print("student found!")
                    print(student["name"], student["grade"])
                    search_result=True
                    return 
            if search_result==False:
                print("no student found! ")
            while True:
                again=input('do you want to try another name? Y/N').strip()
                if again.upper()=="N":
                    return
                elif again.upper()=="Y":
                    break
                else:
                    print("please enetr Y or N ")
    def update_grade():
        while True:
            student_name = input("Which student's grade do you want to change? ").strip()
            if student_name=='':
                print("name can not be empty! ")
            else:
                break
        search=False
        for i in student_list:
            if student_name.lower() == i["name"].lower():
                print("Student found!")
                print(i["name"], i["grade"])
                while True:
                    try:
                        upgrade = int(input("What should the new grade be? "))
                    except ValueError:
                        print('updated grade should be a number! ')
                    else:
                        if upgrade < 0 or upgrade > 100:
                            print("Grade must be between 0 and 100.")
                        else:
                            break
                i["grade"] = upgrade
                search=True
        if search==False:
            print('no students found! ')
            return
        with open(data, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "grade"])
            writer.writeheader()
            writer.writerows(student_list)
    #generate performance report
    def average():
        total=0
        av_list=[]
        if not student_list:
            print("No students available!")
            return
        print(f"total number of students: {len(student_list)}")
        for i in student_list:
            total=total+int(i["grade"])
        av=total/len(student_list)
        for i in student_list:
            if int(i['grade'])>av:
                av_list.append(i)
        print(f"the average score of the students is: {round(av,2)}")
        print(f'students who score above average are: ')
        for i in av_list:
            print(f'{i["name"]},{i["grade"]}')
        print(f'total students who scored above average: {len(av_list)}')
    def highest_grade():
        if not student_list:
            print("No students available!")
            return
        hgrade=-1
        for h in student_list:
            if int(h["grade"])>hgrade:
                hgrade=int(h["grade"])
                hname=h["name"]
        print(f"{hname} got the HIGHEST garde: {hgrade} ")
    def lowest_grade():
        if not student_list:
                print("No students available!")
                return
        lgrade=101
        for h in student_list:
            if int(h['grade'])<lgrade:
                lgrade=int(h['grade'])
                lname=h['name']
        print(f"{lname} got the LOWEST grade: {lgrade}")
    while True:
        choice=menu()
        if choice==1:
            register()
        elif choice==2:
            display_students()
        elif choice==3:
            search_student()
        elif choice==4:
            update_grade()
        elif choice==5:
            average()
            highest_grade()
            lowest_grade()
        elif choice==6:
            print("goodbye")
            break
main()