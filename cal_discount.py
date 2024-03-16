def calculate_discount(price, discount_percent):
    
    # using if statement to check weather discount is greater or equal to 20%
    if discount_percent >= 20:
        discount_amount = price + (discount_percent / 100)
        final_price= price - discount_amount
        return final_price
    else:
        price
        
# testing the function
discount_percent = 35
original_price = 200
final_price= calculate_discount(original_price, discount_percent)
print("after discount: ",  final_price)
        