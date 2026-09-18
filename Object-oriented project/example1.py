class Product:
    current_id = 0
    def __init__(self, description, price): #instance method
        self.description = description
        self.id_num = Product.current_id
        Product.current_id += 1
        self.price = price
    def __str__(self):
        return(f'product {self.description}, id {self.id_num} @{self.price}')

p = Product('thinkpad', 0, 1299.95)
print(p)