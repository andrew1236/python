
###asks user for principal, annual interest rate, times compounded per year, time, and then calculates compound intrest.
def main():
    
    principal=int(input('Enter the starting principal in USD:'))
    annual_interest_rate=int(input('Enter the annual interest rate percentage:'))/100
    compounded=int(input('How many times per year is the interest compounded?'))
    time=int(input('For how many years will the account earn interest?'))

    formula=format((principal*(1+annual_interest_rate/compounded)**(compounded*time)),'.2f')
    print('At the end of',time, 'years you will have','$'+formula)

main()
