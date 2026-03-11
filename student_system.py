records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Sneha", "Chemistry", 84],
    ["Rohit", "Physics", 72],
    ["Anita", "Math", 95],
    ["Karan", "Chemistry", 67],
    ["Pooja", "Physics", 89],
    ["Vikas", "Math", 81],
    ["Neha", "Chemistry", 90]
]

def add_student(name, subject, marks):
    
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Record already exists")
            return
    
    records.append([name, subject, marks])
    print("Student added")

def get_toppers(subject):

    filtered = [r for r in records if r[1] == subject]

    toppers = sorted(filtered, key=lambda x: x[2], reverse=True)[:3]

    for t in toppers:
        print(t)

def class_average(subject):

    marks = [r[2] for r in records if r[1] == subject]

    if not marks:
        return 0

    return sum(marks) / len(marks)

def above_average_students():

    all_marks = [r[2] for r in records]

    avg = sum(all_marks) / len(all_marks)

    result = [r for r in records if r[2] > avg]

    for r in result:
        print(r)

def remove_student(name):

    global records

    records = [r for r in records if r[0] != name]

    print("Student removed")

def save_to_file():

    with open("students.txt","w") as f:

        for r in records:
            f.write(str(r) + "\n")

while True:

    print("\n1 Add student")
    print("2 Show toppers")
    print("3 Show class average")
    print("4 Above average students")
    print("5 Remove student")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        subject = input("Subject: ")
        marks = int(input("Marks: "))
        add_student(name, subject, marks)

    elif choice == "2":
        subject = input("Subject: ")
        get_toppers(subject)

    elif choice == "3":
        subject = input("Subject: ")
        print(class_average(subject))

    elif choice == "4":
        above_average_students()

    elif choice == "5":
        name = input("Name: ")
        remove_student(name)

    elif choice == "6":
        save_to_file()
        break