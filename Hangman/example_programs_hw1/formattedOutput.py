"""
    File:  formattedOutput.py
    Description:  Simple program to demonstrate string formatting to print a
    table.  See section 1.4.2.1 (pp. 24 - 27) of the textbook.
    You generate a formatted string by embedding string formatting into the
    string based on type: "%d" for int, "%f" for float, "%s" for string.
    For example, print("Name: %s, Student #: %d, "GPA: %f" % ("Mark", 123456, 4.0))
    would print "Name: Mark, Student #: 123456, GPA: 4.000000". Each formatting
    specifier in the string is replaces by the corresponding positional tuple value
    supplied after the string using the "%" operator (%s replaced by the string
    "Mark", etc.)

    For printing a table it is useful to supply additional formatting options
    to specify:
    * the minimal field width (e.g., %10s meaning print the string
      using at least 10 spaces so "Mark" would print as "      Mark")
    * justification of the value is indicated by the sign of the field width
      with positive value meaning left-justified and negative value meaning
      right-justified
    * floating point formatting can specify the number of characters to the
      right of the decimal (e.g., "GPA: %4.2f" % 4.0) would generate "GPA: 4.00"
    
"""
def main():
    """Writes the following student information to a file as a table"""

    studentsList = [["Mark", 123456, 4.0],
                    ["Bob", 234567, 2.586],
                    ["Sally", 345678, 3.982],
                    ["Virginia", 456789, 3.66]]

    studentFile = open("student_table.txt", "w")  # open file for writing

    # write report header -- note the usage of the string .center method
    studentFile.write("Student Information Report".center(36) + "\n\n\n")
    
    # write column header for the table
    studentFile.write("%-15s %9s %8s\n" % ("Name", "Student #", "GPA"))
    studentFile.write("-"*36+"\n")

    # write body of the table
    for student in studentsList:
        name = student[0]
        studentNumber = student[1]
        GPA = student[2]
        studentFile.write("%-15s %7d %11.2f\n" % (name, studentNumber, GPA))

    # close file when done writing
    studentFile.close()

main()
