print("=" * 50)
print("     PERSONAL POCKET CGPA CALCULATOR (PPC)")
print("=" * 50)

while True:

    total_units = 0
    total_points = 0

    number_of_courses = int(input("\nEnter number of courses: "))

    for course in range(1, number_of_courses + 1):

        print(f"\nCourse {course}")

        course_unit = int(input("Enter Course Unit: "))
        score = int(input("Enter Score: "))

        match score:

            case s if 70 <= s <= 100:
                grade = "A"
                point = 5

            case s if 60 <= s <= 69:
                grade = "B"
                point = 4

            case s if 50 <= s <= 59:
                grade = "C"
                point = 3

            case s if 45 <= s <= 49:
                grade = "D"
                point = 2

            case s if 40 <= s <= 44:
                grade = "E"
                point = 1

            case s if 0 <= s <= 39:
                grade = "F"
                point = 0

            case _:
                print("Invalid Score!")
                continue

        quality_point = course_unit * point

        total_units += course_unit
        total_points += quality_point

        print("Grade:", grade)
        print("Grade Point:", point)
        print("Quality Point:", quality_point)

    cgpa = total_points / total_units

    print("\n" + "=" * 50)
    print("Total Course Units:", total_units)
    print("Total Quality Points:", total_points)
    print("CGPA =", round(cgpa, 2))
    print("=" * 50)

    choice = input("\nCalculate Again? (Y/N): ").upper()

    match choice:
        case "Y":
            continue
        case "N":
            print("\nThank you for using PPC.")
            break
        case _:
            print("\nInvalid Choice.")
            break