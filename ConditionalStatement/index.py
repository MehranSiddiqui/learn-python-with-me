# With conditional statement we have also used comparing operators
marks_obtained = input("Please enter the marks obtained: ")

numberMarks = float(marks_obtained)
if numberMarks == 100:
    print("The student has got perfect score")
elif (numberMarks >= 90):
    print("The student has got A grade")
elif (numberMarks >= 75 and numberMarks < 90):
    print("The student has got B grade")
elif (numberMarks >= 60 and numberMarks < 75):
    print("The student has got C grade")
elif (numberMarks >= 40 and numberMarks < 60):
    print("The student has got D grade")
else:
    print("Unfortunately! The student has failed")
