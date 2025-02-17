
def find_grade(score):
    """Determine the grade based on the score."""
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


try:
    score = float(input("Enter the student's score (0-100): "))
    if 0 <= score <= 100:
        grade = find_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Error: Please enter a score between 0 and 100.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")



#x=int(input("Enter input"))
#if x <=100:
 #   print "scored A+"

#elif x<=90:
    #print "scored A"
#elif x<=80:
   # print "scored B+"
#elif x<=70:
  #  print "scored B"
#else
 #   print"scored D"


