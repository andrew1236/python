#program converts feet to inches, inches to feet, yards to feet, and feet to yards
def feet_to_inches(feet):
    return feet*12

def inches_to_feet(inches):
    return inches/12

def yards_to_feet(yards):
    return yards*3

def feet_to_yards(feet):
    return feet/3

def main():
    feet=int(input('Enter feet:'))
    print(feet_to_inches(feet))

    inches=int(input('Enter inches:'))
    print(inches_to_feet(inches))

    yards=int(input('Enter yards:'))
    print(yards_to_feet(yards))

    feet=int(input('Enter feet:'))
    print(feet_to_yards(feet))

main()
