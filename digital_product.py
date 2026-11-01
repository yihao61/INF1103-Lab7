from product import Product

class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, download_size):
        super().__init__(id, name, price, stock)
        self.download_size = download_size

    def display_information(self):
        return f"ID: {self.__id}    | Name: {self.__name}   | Price: ${self.__price}    | Stock: {self.__stock}     | Download Size: {self.download_size}MB"

    def get_download_size(self):
        return self.download_size