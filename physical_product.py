from product import Product

class PhysicalProduct(Product):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self.weight = weight

    def display_information(self):
        return f"ID: {self.__id}    | Name: {self.__name}   | Price: ${self.__price}    | Stock: {self.__stock}     | Weight: {self.weight}kg"

    def get_weight(self):
        return self.weight