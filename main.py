import pandas as pd

# 1. Create student data
data = {
    "Student Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [85, 72, 45, 91, 58]
}

# 2. Store data in Pandas DataFrame
df = pd.DataFrame(data)


# 3. Display all student records
def display_students():
    print(df)


# 4. Calculate average marks
def average_marks():
    average = df["Marks"].mean()
    print("Average Marks:", average)


# 5. Find highest marks
def highest_marks():
    highest = df["Marks"].max()
    print("Highest Marks:", highest)


# 6. Find lowest marks
def lowest_marks():
    lowest = df["Marks"].min()
    print("Lowest Marks:", lowest)


# 7. Count passing students
def passing_students():
    passing = (df["Marks"] >= 50).sum()
    print("Passing Students:", passing)


# 8. Count failing students
def failing_students():
    failing = (df["Marks"] < 50).sum()
    print("Failing Students:", failing)


# 9. Find student with highest marks
def top_student():
    student = df.loc[df["Marks"].idxmax()]

    print("Top Student")
    print("Name:", student["Student Name"])
    print("Roll Number:", student["Roll Number"])
    print("Marks:", student["Marks"])


# 10. Filter students based on marks
def filter_students():
    marks = int(input("Enter minimum marks: "))

    result = df[df["Marks"] >= marks]
    print(result)


# Menu
while True:

    print("~~ STUDENT MARKS SYSTEM ~~")
    print("1. Display All Students")
    print("2. Average Marks")
    print("3. Highest Marks")
    print("4. Lowest Marks")
    print("5. Count Passing Students")
    print("6. Count Failing Students")
    print("7. Find Top Student")
    print("8. Filter Students")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_students()

    elif choice == "2":
        average_marks()

    elif choice == "3":
        highest_marks()

    elif choice == "4":
        lowest_marks()

    elif choice == "5":
        passing_students()

    elif choice == "6":
        failing_students()

    elif choice == "7":
        top_student()

    elif choice == "8":
        filter_students()

    elif choice == "9":
        print("Program Ended")
        break

    else:
        print("Invalid choice")