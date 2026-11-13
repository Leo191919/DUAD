#Precio de producto con descuento


product_price=0
discount1=0.02
discount2=0.1
end_price=0

product_price=float(input("Enter the item price: "))

if product_price<100:
    end_price=product_price_(product_price*discount1)
else:
    product_price>=100
    end_price=product_price_(product_price*discount2)

print(end_price)