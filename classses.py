from main import Database
from datetime import datetime


class CountryTable:
    def __init__(self, name: str):
        self.name = name
        self.create_date = str(datetime.now())

    @staticmethod
    def select(table="country"):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, "select")

    def insert(self):
        query = f"""INSERT INTO country(name, create_date) VALUES('{self.name}', '{self.create_date}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def delete(column, data, table="country"):
        if isinstance(data, str):
            query = f"""DELETE FROM {table} WHERE {column} = '{data}';"""

        elif isinstance(data, int):
            query = f"""DELETE FROM {table} WHERE {column} = {data};"""

        return Database.connect(query, "delete")

    @staticmethod
    def update(query):
        return Database.connect(query, "update")


class CityTable(CountryTable):
    def __init__(self, name: str, country_id: int):
        super().__init__(name)

        countryidlist = []
        for i in Database.connect("""Select country_id FROM country""", "select"):
            countryidlist.append(i[0])

        while not country_id in countryidlist:
            print("\t\t<-- 🛑country id not in table country🛑 -->")
            country_id = int(input("\t\tEnter country id: "))

        self.country_id = country_id

    def insert(self):
        query = f"""INSERT INTO city(name, country_id, create_date) VALUES('{self.name}', '{self.country_id}', '{self.create_date}');"""
        return Database.connect(query, "insert")


class Address(CityTable):
    def __init__(self, name: str, country_id: int, city_id: int):
        super().__init__(name, country_id)
        cityidlist = []
        for i in Database.connect("""Select city_id FROM city""", "select"):
            cityidlist.append(i[0])

        while not city_id in cityidlist:
            print("\t\t<-- 🛑city id not in table city🛑 -->")
            country_id = int(input("\t\tEnter city id: "))

        self.city_id = city_id

    def insert(self):
        query = f"""INSERT INTO address(name, country_id, city_id, create_date) VALUES('{self.name}', '{self.country_id}', '{self.city_id}' , '{self.create_date}');"""
        return Database.connect(query, "insert")


class Customer(CountryTable):
    def __init__(self, first_name: str, last_name: str, phone_number: int, birt_date: str, address_id: int):
        super().__init__(first_name)
        self.last_name = last_name

        while len(str(phone_number)) != 9:
            print("\t\t<-- 🛑7 number of phone number🛑 -->")
            phone_number = int(input("\t\tEnter phone number: "))
        self.phone_number = phone_number
        self.birt_date = birt_date

        addressidlist = []
        for i in Database.connect("""Select address_id FROM address""", "select"):
            addressidlist.append(i[0])

        while not address_id in addressidlist:
            print("\t\t<-- 🛑address id not in table address🛑 -->")
            address_id = int(input("\t\tEnter address id: "))

        self.address_id = address_id

    @staticmethod
    def checkcustomerid(customer_id):
        customeridlist = []

        for i in Database.connect("SELECT customer_id FROM customer", "select"):
            customeridlist.append(i[0])

        return customer_id in customeridlist

    def insert(self):
        query = f"""INSERT INTO 
        customer(first_name, last_name, phone_number, birt_date, address_id, create_date) 
        VALUES('{self.name}', 
        '{self.last_name}',
         '{self.phone_number}',
          '{self.birt_date}',
          '{self.address_id}',
          '{self.create_date}');"""

        return Database.connect(query, "insert")

    @staticmethod
    def checkcustomerid(customer_id):
        customeridlist = []
        for i in Database.connect("""SELECT customer_id FROM customer""", "select"):
            customeridlist.append(i[0])

        return customer_id in customeridlist


class Category(CountryTable):
    def __init__(self, title: str, description: str):
        super().__init__(title)
        self.description = description

    def insert(self):
        query = f"""INSERT INTO category(title, description, create_date)
        VALUES('{self.name}', '{self.description}', '{self.create_date}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def checkcategoryid(category_id: int):
        """Argumentni category_id lar ichida borligini tekshiradi return True or False"""
        categoryidlist = []

        for i in Database.connect("SELECT category_id FROM category", "select"):
            categoryidlist.append(i[0])

        return category_id in categoryidlist


class Product(Category):
    def __init__(self, title: str, description: str, reyting: float):
        super().__init__(title, description)
        self.reyting = reyting

    def insert(self):
        query = f"""INSERT INTO product(title, description, reyting, create_date)
        VALUES('{self.name}', '{self.description}', '{self.reyting}', '{self.create_date}');"""
        return Database.connect(query, "insert")

    @staticmethod
    def checkproductid(product_id):
        """Argumentni product_id lar ichida borligini tekshiradi return True or False"""
        productidlist = []

        for i in Database.connect("SELECT product_id FROM product", "select"):
            productidlist.append(i[0])

        return product_id in productidlist


class ProductType(CountryTable):
    def __init__(self, name: str, color: str, price: float, product_id: int):
        super().__init__(name)
        self.color = color
        self.price = price
        while not Product.checkproductid(product_id):
            print("\t\t<-- 🛑product id not in table product🛑 -->")
            product_id = int(input("\t\tEnter product id: "))
        self.product_id = ProductType.checkproductid(product_id)

    def insert(self):
        query = f"""INSERT INTO product_type(name, color, price, product_id, create_date)
        VALUES('{self.name}', '{self.color}', '{self.price}', '{self.product_id}', '{self.create_date}');"""
        return Database.connect(query, "insert")


class ProductCategory:
    def __init__(self, product_id: int, category_id: int):

        while not Product.checkproductid(product_id):
            print("\t\t<-- 🛑product id not in table product🛑 -->")
            product_id = int(input("\t\tEnter product id: "))
        self.product_id = product_id

        while not Category.checkcategoryid(category_id):
            print("\t\t<-- 🛑Category id not in table product🛑 -->")
            category_id = int(input("\t\tEnter category id: "))
        self.category_id = category_id
        self.create_date = datetime.date

    @staticmethod
    def select(self):
        return CountryTable.select(table="product_category")

    @staticmethod
    def delete(column, table="product_category"):
        return CountryTable.delete(column,table)

    @staticmethod
    def update(query):
        return CountryTable.update(query)

    def insert(self):
        query = f"""INSERT INTO product_category(product_id, category_id, create_date) 
        VALUES('{self.product_id}', '{self.category_id}', '{self.create_date}');"""

        return Database .connect(query, "insert")


class PymentType(CountryTable):
    def __init__(self, name):
        super().__init__(name)

    def insert(self):
        query = f"""INSERT INTO payment_type(name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class PaymentStatus(CountryTable):
    def __init__(self, name):
        super().__init__(name)

    def insert(self):
        query = f"""INSERT INTO payment_status(name) VALUES('{self.name}')"""
        return Database.connect(query, "insert")


class ProductCustomer:
    def __init__(self, product_id, customer_id):
        while not Product.checkproductid(product_id):
            print("\t\t<-- 🛑product id not in table product🛑 -->")
            product_id = int(input("\t\tEnter product id: "))
        self.product_id = product_id

        while not Customer.checkcustomerid(customer_id):
            print("\t\t<-- 🛑Customer id not in table product🛑 -->")
            category_id = int(input("\t\tEnter customer id: "))
        self.category_id = category_id
        self.create_date = datetime.date

    @staticmethod
    def select():
        return CountryTable.select(table="product_customer")

    @staticmethod
    def delete(column, table="product_customer"):
        return CountryTable.delete(column, table)

    @staticmethod
    def update(query):
        return CountryTable.update(query)

    def insert(self):
        query = f"""INSERT INTO product_category(product_id, category_id, create_date) 
            VALUES('{self.product_id}', '{self.category_id}', '{self.create_date}');"""

        return Database.connect(query, "insert")


class Store(Category):
    def __init__(self, name, description, address_id):
        super().__init__(name, description)

        addressidlist = []
        for i in Database.connect("""Select address_id FROM address""", "select"):
            addressidlist.append(i[0])

        while not address_id in addressidlist:
            print("\t\t<-- 🛑address id not in table address🛑 -->")
            address_id = int(input("\t\tEnter address id: "))

        self.address_id = address_id

    def insert(self):
        query = f"""INSERT INTO store(name, description, address_id)"""
        return Database.connect(query, "insert")


class Punk(CountryTable):
    def __init__(self, name, address_id):
        super().__init__(name)

        addressidlist = []
        for i in Database.connect("""Select address_id FROM address""", "select"):
            addressidlist.append(i[0])

        while not address_id in addressidlist:
            print("\t\t<-- 🛑address id not in table address🛑 -->")
            address_id = int(input("\t\tEnter address id: "))

        self.address_id = address_id

    def insert(self):
        query = f"""INSERT INTO punk(name, address_id) VALUES('{self.name}', '{self.address_id}')"""
        return Database.connect(query, "insert")
