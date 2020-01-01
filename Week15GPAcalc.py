#Week 15 GPA Calculator

grades = []

classes = int(raw_input("How Many Classes Do You Have: "))
#Classes gets the number of classes the individual has

def GetClassGrade():  
    '''This function gets the user's grades and assigns them to the list of grades'''
    
    grades = []
    number = 1
    
    for x in range(0, classes): 
        while number <= classes:
            grade = raw_input("Enter Your Grade For Class " + str(number) + " (Letter Form, Half Grades Such as A/B Are Acceptable): ")
            #Gets the user's grade
            number = number + 1
            
            grade = grade.upper()
            
            grades += [grade]
            #Puts the grade in the list
    
    print(grades)    
    #Prints out the grades
    calculate(grades)
    
def calculate(grades):
    '''This function assings the inputed grade to a number value and calculates its average'''
    
    total= 0
    
    for score in grades:
        if score == "A":
            total = total + 4.0
        elif score == "A/B":
            total = total + 3.5
        elif score == "B":
            total = total + 3.0
        elif score == "B/C":
            total = total + 2.5
        elif score == "C":
            total = total + 2.0
        elif score == "C/D":
            total = total + 1.5
        elif score == "D":
            total = total + 1.0
        #This is the calculation part. Assigns a number value to the inputted grade
    
    gpa = total / classes
    #Averages the sum of the grades by the number of classes the user indicated
    
    print(gpa)
    
GetClassGrade()

