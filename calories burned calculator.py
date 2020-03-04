#calculates calories burned every 5 minutes starting at 10 minutes
def calculate_calories_burned():
    print('Minutes	                  Calories Burned')
    print('-----------------------------------------')
 
    counter=1

    minutes=10
    calories_burned=42
    
    while counter<=5:
        print(minutes,'                      ',format(calories_burned,'.1f'))
        minutes=minutes+5
        calories_burned+=21
        counter+=1

main()
