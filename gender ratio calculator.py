#ask user for the number of male and female students and then calculates the gender ratio
def calcualate_gender_ratio
    male_students=int(input("Enter the number of male students:"))
    female_students=int(input("Enter the number of female students:"))

    total=(male_students+female_students)
    male_precent=((male_students/total)*100)
    female_precent=((female_students/total)*100)
    print(format(male_precent,'.0f')+'%')
    print(format(female_precent,'.0f')+'%')
