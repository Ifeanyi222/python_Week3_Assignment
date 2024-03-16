def calculate_discount(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    return final_price

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    if discount_percentage > 0:
        final_price = calculate_discount(original_price, discount_percentage)
        print("after applying the discount: ", final_price)
    else:
        print("Original price: ", original_price)

if __name__ == "__main__":
    main()