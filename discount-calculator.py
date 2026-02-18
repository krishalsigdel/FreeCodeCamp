
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        print( 'The price should be a number')
    elif price <= 0:
        print( 'The price should be greater than 0')   
    elif not isinstance(discount, (int, float)):
        print( 'The discount should be a number') 
    elif price<=0:
      print('The price should be greater than 0')
    elif not (0 <= discount <= 100):
        print('The discount should be between 0 and 100')
    else:
        discount=(discount/100)*price
        total_cost=price-discount
    print( 'total cost:', total_cost)
price=float(input("enter price of object    :"))
discount=float(input("enter discount%       :"))
apply_discount(price,discount)

