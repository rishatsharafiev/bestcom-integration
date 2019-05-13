from typing import List
from utils.db import get_connection

from entities.price import PriceEntity


class PriceRepository:
    """Price Repository"""

    @staticmethod
    def create(price_entities: List[PriceEntity]):
        sql_string = """INSERT INTO price(article, kod, name, cena, valuta, nalichie, postavchik, img, data_dobavleniya) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURDATE());"""

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                for price_entity in price_entities:

                    counter = 0

                    prepared_statements = (
                        price_entity.article,
                        price_entity.kod,
                        price_entity.name,
                        price_entity.cena,
                        price_entity.valuta,
                        price_entity.nalichie,
                        price_entity.postavchik,
                        price_entity.img,
                    )

                    cursor.execute(sql_string, prepared_statements)

                    counter += 1
                    if counter == 10000:
                        connection.commit()
                        counter = 0
                
                if counter != 0:
                    connection.commit()
        finally:
            if connection:
                connection.close()

        return False

    @staticmethod
    def clear_price_by_supplier(supplier: str = 'АЙТИ'):
        sql_string = """DELETE FROM `price` WHERE postavchik=%s;"""
        
        prepared_statements = (
            supplier,
        )

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string, prepared_statements)
                connection.commit()
                return cursor.lastrowid
        finally:
            if connection:
                connection.close()

        return False
