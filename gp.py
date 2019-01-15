DSC = '''
                                +=======================================+
                                |.......Engineering GP calculator.......|
                                +---------------------------------------+
                                |#Author: Konstantine                   |
                                |#Contact: cutejosh2@gmail.com          |
                                |#Date: sometime 2018                   |
                                |#This tool is made for eng students    |
                                |#Changing the Description of this tool |
                                |Won't made you the coder ^_^ !!!       |
                                |#Respect Coderz ^_^                    |
                                |                                       |
                                |                                       |
                                +=======================================+
                                |.......Engineering GP calculator.......|
                                +---------------------------------------+
'''
import time
import logging


logging.basicConfig(filename="gp_log.txt", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

continuee=""
courseList = []
registered_credits = []
credits_passed = []
cgpa=0

while continuee != "quit" or continuee != "QUIT" or continuee != "q":
    def drawLine():
        horizontalDash="-"
        print("\t\t" + horizontalDash*67)

    t1=time.clock()

    print()
    print(DSC)
    # drawLine()
    # print("\t\t|\t\tENGINEERING GP CALCULATOR 2.0 (*__*)")
    # print("\t\t|\t\t\tAll credits go to ")
    # print("\t\t|\t\t\tthe developer Joshua")

    drawLine()
    print("\t\t|\t[+] Script execution begins ", time.ctime())

    def addCourse(course, credit_load):
        courseList.append(course)
        courseList.append(credit_load)
        registered_credits.append(credit_load)

    def calculateTotalCredits(grade, credit_load):
        if grade == "A":
            obtained = 5*credit_load
        elif grade == "B":
            obtained = 4*credit_load
        elif grade == "C":
            obtained = 3*credit_load
        elif grade == "D":
            obtained = 2*credit_load
        elif grade == "F":
            obtained = 0*credit_load
        else:
            print("Invalid grade! ")
        
        credits_passed.append(obtained)

    def calculateCGPA(registered_credits, registered_credits_passed):
        global cgpa;
        cgpa = sum(registered_credits_passed)/sum(registered_credits)
        print("\t\t|\tYour CGPA is " + str(cgpa))
        
    def showCourses():
        print("\t\t|\tCourse List:",courseList)
        print("\t\t|\tTotal Credits Registered = " + str(sum(registered_credits)))
        print("\t\t|\tTotal Credits passed = " + str(sum(credits_passed)))
        calculateCGPA(registered_credits, credits_passed)

    number_of_courses=float(input("\t\t|\tnumber of courses: "))

    drawLine()
    while number_of_courses!=0:

        course=str(input("\t\t|\tCourse: "))
        credit=int(input("\t\t|\tCredits: "))
        grade=input("\t\t|\tGrade: ")
        drawLine()
        course1= addCourse(course, credit)
        calculateTotalCredits(grade, credit)
        number_of_courses -=1

    showCourses()
    drawLine()
    print("\t\t|\t[+] Script execution ends ", time.ctime())
    t2=time.clock()
    print("\t\t|\t[+] Script execution time ", str(t2-t1) + " seconds")
    drawLine()





















































































    logging.info("\t\t|\t######################################################################")
    logging.info("\t\t|\t\t\tENGINEERING GP CALCULATOR 2.0 (*__*)\n")
    logging.info("\t\t|\t\t\t\tAll credits go to \n")
    logging.info("\t\t|\t\t\t\tthe developer Joshua\n")
    logging.info("\t\t|\t----------------------------------------------------------------------")
    logging.info("\t\t|\t[+] Script execution begins " + str(time.ctime()) + "\n")
    logging.info("\t\t|\t----------------------------------------------------------------------")


    logging.info("\t\t|\tCourse List:" + str(courseList) + "\n")
    logging.info("\t\t|\tTotal Credits Registered = " + str(sum(registered_credits)) + "\n")
    logging.info("\t\t|\tTotal Credits passed = " + str(sum(credits_passed)) + "\n")
    logging.info("\t\t|\tYour CGPA is " + str(cgpa) + "\n")
    logging.info("\t\t|\t----------------------------------------------------------------------")
    logging.info("\t\t|\t[+] Script execution ends " + str(time.ctime()) + "\n")
    logging.info("\t\t|\t[+] Script execution time "+ str(t2-t1) + " seconds\n")
    logging.info("\t\t|\t######################################################################\n\n\n")


    continuee = input("\t\t\tTo exit type q or quit, press enter to continue: ")
