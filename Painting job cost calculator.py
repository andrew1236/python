#program asks user how many square feet need to be painted and the price of paint per gallon. Then calculates how many gallons are needed, number of labor hours, and the charges for paint, labor, the total cost. 

def show_cost_estimate(gallons_of_paint, hours_of_labor, cost_of_paint, cost_of_labor):
    total_cost = cost_of_paint + cost_of_labor
    return format(total_cost,'.2f')
   
   
def main():
    square_feet = int(input('Enter square feet to be painted:'))
    
    if square_feet>0 and square_feet<60:
        gallons_of_paint=1
    else:
        gallons_of_paint=square_feet//60
        
    hours_of_labor=square_feet/7.5//1
    cost_of_labor=hours_of_labor*35
    cost_of_paint=(int(input('Enter price per gallon of paint: ')))*gallons_of_paint
    
    print('Gallons of paint:',format(gallons_of_paint,'.0f'))
    print('Hours of labor:',format(hours_of_labor,'.0f'))
    print('Paint charges:','$'+format(cost_of_paint,'.2f'))
    print('Labor charges:','$'+format(cost_of_labor,'.2f'))
    print('Total cost:','$'+show_cost_estimate(gallons_of_paint, hours_of_labor, cost_of_paint, cost_of_labor,))
   
    
main()
