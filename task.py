

#Product
products = {
    "Product A":20,
    "Product B":40,
    "Product C":50
}

#Discount rules
discount_rules={
    "flat_10_discount":10,
    "bulk_5_discount":5,
    "bulk_10_discount":10,
    "tiered_50_discount":50
}

#Fees
gift_wrap_fee=1
shipping_fee_per_package=5
products_per_package=10


subtotal=0
total_quantity=0
discount_applied=None
discount_amount=0
gift_wrap_total=0
shipping_fee=0

#quantity,gift wrap
for product_name in products:
    quantity=int(input(f"Enter the quantity of {product_name}: "))
    is_gift_wrapped=input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower()=="yes"

    #product total
    product_price=products[product_name]
    product_total=quantity*product_price

    #gift wrap fee
    if is_gift_wrapped:
        gift_wrap_total+=quantity*gift_wrap_fee

    #subtotal,total
    subtotal+=product_total
    total_quantity+=quantity

    #apply rules
    if total_quantity>30 and quantity>15:
        if discount_applied!="tiered_50_discount":
            discount_applied="tiered_50_discount"
            discount_amount=(total_quantity-15)*product_price*discount_rules["tiered_50_discount"]/100
    elif total_quantity>20:
        if discount_applied!="bulk_10_discount":
            discount_applied="bulk_10_discount"
            discount_amount=subtotal*discount_rules["bulk_10_discount"]/100
    elif quantity>10:
        if discount_applied!="bulk_5_discount":
            discount_applied="bulk_5_discount"
            discount_amount=product_total*discount_rules["bulk_5_discount"]/100
    elif subtotal>200:
        if discount_applied!="flat_10_discount":
            discount_applied="flat_10_discount"
            discount_amount=discount_rules["flat_10_discount"]

#shipping fee
shipping_packages=total_quantity//products_per_package
if total_quantity%products_per_package!=0:
    shipping_packages+=1
shipping_fee=shipping_packages*shipping_fee_per_package

#total amount
total=subtotal-discount_amount+gift_wrap_total+shipping_fee

#details
print("Product Details:")
for product_name in products:
    product_total=quantity*products[product_name]
    print(f"{product_name} - Quantity: {quantity} - Total: ${product_total}")

print(f"\nSubtotal: ${subtotal}")
print(f"Discount Applied: {discount_applied} - Amount: ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_total}")
print(f"Total: ${total}")
