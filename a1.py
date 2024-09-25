#All inputs start here
lab = int(input("Enter the number of labs completed: "))
quiz = int(input("Enter the number of quizzes completed: "))
a1 = float(input("Enter grade for Assignment 1"))
a2 = float(input("Enter grade for Assignment 2"))
a3 = float(input("Enter grade for Assignment 3"))
a4 = float(input("Enter grade for Assignment 4"))
mid1 = float(input("Enter grade for Midterm 1"))
mid2 = float(input("Enter grade for Midterm 2"))
fin = float(input("Enter grade for Final Exam"))
prp = float(input("Enter grade for Midterms and Final Preparation"))

#All calculations start here
ag = (a1/25) + (a2/25) + (a3/25) + (a4/25)
midg = (mid1/8) + (mid2/8)
fing = (fin/(100/18))
prpg = (prp/(100/6))
calc = (ag + midg + fing + prpg)
