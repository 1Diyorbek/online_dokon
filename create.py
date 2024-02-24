import psycopg2
from main import Database


def created_table():
    country_table = f"""
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    city_table = f"""
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(country_id),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    address = f"""
        CREATE TABLE address(
            address_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(country_id),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    customer = f"""
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50),
            phone_number VARCHAR(10) NOT NULL,
            birt_date DATE NOT NULL,
            address_id INT REFERENCES address(address_id),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    product = f"""
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            reyting FLOAT,
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    category = f"""
        CREATE TABLE category(
            category_id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    product_type = f"""
        CREATE TABLE product_type(
            product_type_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            color VARCHAR(20),
            price FLOAT NOT NULL,
            product_id INT REFERENCES product(product_id),
            last_update TIMESTAMP DEFAULT now(),
            create_date DATE);"""

    product_category = f"""
            CREATE TABLE product_category(
                product_category_id SERIAL PRIMARY KEY,
                product_id INT REFERENCES product(product_id),
                category_id INT REFERENCES category(category_id),
                last_update TIMESTAMP DEFAULT now(),
                create_date DATE);"""

    payment_type = f"""
            CREATE TABLE payment_type(
                payment_type_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                last_update TIMESTAMP DEFAULT now());"""

    payment_status = f"""
        CREATE TABLE payment_status(
            payment_status_id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            last_update TIMESTAMP DEFAULT now());"""

    product_customer = f"""
            CREATE TABLE product_customer(
                product_customer_id SERIAL PRIMARY KEY,
                product_id INT REFERENCES product(product_id),
                customer_id INT REFERENCES customer(customer_id),
                last_update TIMESTAMP DEFAULT now());"""

    store = f"""
            CREATE TABLE store(
                store_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                description TEXT,
                address_id INT REFERENCES address(address_id),
                last_update TIMESTAMP DEFAULT now());"""

    punk = f"""
            CREATE TABLE punk(
                punk_id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                address_id INT REFERENCES address(address_id),
                last_update TIMESTAMP DEFAULT now());"""

    data = {
        # "country_table": country_table,
        # "city_table": city_table,
        # "address": address,
        # "customer": customer,
        # "product": product,
        # "category": category,
        # "product_type": product_type,
        # "product_category": product_category,
        # "payment_type": payment_type,
        # "payment_status": payment_status,
        # "product_customer": product_customer,
        # "store": store,
        # "punk": punk
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "insert")}")