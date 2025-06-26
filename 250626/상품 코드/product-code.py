product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self,name,code):
        self.name = name
        self.code = code

product_1 = Product("codetree",50)
product_2 = Product(product_name,product_code)

print(f"product {product_1.code} is {product_1.name}")
print(f"product {product_2.code} is {product_2.name}")