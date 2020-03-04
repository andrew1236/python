#program ask user for 5 test scores, and calculates the grade average and the letter grade

def calculate_average(grade1,grade2,grade3,grade4,grade5):
    average= (grade1+grade2+grade3+grade4+grade5)/5
    return average
    
def determine_grade(average):
        if average >=90:
            grade ='A'
        if average >=80 and average<90:
            grade ='B' 
        if average >=70 and average<80:
            grade ='C'
        if average >=60 and average<70:
            grade ='D' 
        if average<60:
            grade ='F'
        
        return grade

   
def main():
    grade1=int(input('Enter score 1: '))
    grade2=int(input('Enter score 2: '))
    grade3=int(input('Enter score 3: '))
    grade4=int(input('Enter score 4: '))
    grade5=int(input('Enter score 5: '))
    average=(grade1+grade2+grade3+grade4+grade5)/5
    print('The average is',calculate_average(grade1,grade2,grade3,grade4,grade5))
    print('The grade is',determine_grade(average))
  
    
main()
