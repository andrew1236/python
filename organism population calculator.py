#ask user for number of intital organisms, the average increases of organisms, and how many days to calcualte
def calculate_organism_population():
    organisms=int(input('Enter number of organisms:'))
    average_increase =int(input('Enter average daily increase:'))
    days=int(input('Enter number of days to multiply:'))
    counter=days-days+1
    days=days-days+1
    print('DAY	 APPROXIMATE POPULATION')
    print('-------------------------------')

    while counter<=10:
        organisms=organisms*(1+average_increase/100)
        if days==1:
            organisms=organisms-.600
            print(days,"      ", format(organisms, '.0f'))
        if days>1 and days<10:
            print(days,"      ", format(organisms, '.3f'))
        if days==10:
            print(days,"     ", format(organisms, '.3f'))
        
        days+=1
        counter+=1


