"""Produces a student report from data extracted from an external source."""
from student import StudentFileReader

# Name of the file to open.
FILE_NAME = "students.txt"


def report():
    """Extract the student records from the given text file."""
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    student_list = reader.fetch_all()
    reader.close()

    """
    Sort the list by id number. Each object is passed to the lambda
    expression which returns the idNum field of the object.
    """
    student_list.sort(key=lambda rec: rec.id_num)
    # Print the student report.
    show_report(student_list)


def show_report(records):
    """The class names associated with the class codes."""
    class_names = (None, "Freshman", "Sophomore", "Junior", "Senior")

    # Print the header.
    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s %-25s %-10s %-4s" % ("ID", "NAME", "CLASS", "GPA"))
    print("%5s %25s %10s %4s" % ("-"*5, "-"*25, "-"*10, "-"*4))

    # Print the body.
    for record in records:
        print("%5d %-25s %-10s %4.2f" % (record.id_num,
                                         record.last_name + ", " + record.first_name,
                                         class_names[record.class_code], record.gpa))

    # Add a footer.
    print("-"*50)
    print("Number of students:", len(records))


if __name__ == "__main__":
    report()
