### calculates the shipping charge for a package

def calculate_shipping_charge():
    package_weight=float(input('Enter the weight of the package in pounds:'))

    #if package weight is 1 pound or less, the shipping charge will be $1.50 per pound.
    if package_weight<=1:
        shipping_charge=package_weight*1.50

    #if package weight is 2 pounds or more, the shipping charge will be $2.00 per pound.
    if package_weight>=2:
        shipping_charge=package_weight*2.00

    #if package weight is 5 pounds or more, the shipping charge will be $3.00 per pound.
    if package_weight>=5:
        shipping_charge=package_weight*3.00

    #if package weight is 7 pounds or more, the shipping charge will be $4.00 per pound.
    if package_weight>=7:
        shipping_charge=package_weight*4.00
    

    print('Shipping charge:','$'+format(shipping_charge,'.2f'))


