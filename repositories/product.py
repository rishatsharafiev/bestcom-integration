import pydash

from utils.db import get_connection

from entities.product import ProductEntity


class ProductRepository:
    """Product Repository"""

    @staticmethod
    def mark_all_as_deleted():
        sql_string = "UPDATE itpartner_product SET is_deleted=TRUE;"

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string)
                connection.commit()
                return cursor.lastrowid
        finally:
            if connection:
                connection.close()

        return False

    @staticmethod
    def mark_all_as_inactive():
        sql_string = "UPDATE itpartner_product SET is_active=FALSE;"

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string)
                connection.commit()
                return cursor.lastrowid
        finally:
            if connection:
                connection.close()

        return False

    @staticmethod
    def update_or_create(cursor, product_entity: ProductEntity):
        sql_string = """INSERT INTO itpartner_product(sku, name, part, vendor, description, volume, has_image, weight, min_quantity, category_id, is_deleted)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, FALSE)
        ON DUPLICATE KEY UPDATE
            name = %s,
            part = %s,
            vendor = %s,
            description = %s,
            volume = %s,
            has_image = %s,
            weight = %s,
            min_quantity = %s,
            category_id = %s,
            is_deleted=FALSE;
        """
        prepared_statements = (
            product_entity.sku,
            product_entity.name,
            product_entity.part,
            product_entity.vendor,
            product_entity.description,
            product_entity.volume,
            product_entity.has_image,
            product_entity.weight,
            product_entity.min_quantity,
            product_entity.category_id,
            product_entity.name,
            product_entity.part,
            product_entity.vendor,
            product_entity.description,
            product_entity.volume,
            product_entity.has_image,
            product_entity.weight,
            product_entity.min_quantity,
            product_entity.category_id,
        )

        cursor.execute(sql_string, prepared_statements)

    @staticmethod
    def update_partially(cursor, product_entity: ProductEntity):
        sql_string = "UPDATE itpartner_product SET price = %s, quantity = %s, is_active=True WHERE sku=%s;"

        prepared_statements = (
            product_entity.price,
            product_entity.quantity,
            product_entity.sku,
        )

        cursor.execute(sql_string, prepared_statements)

    @staticmethod
    def get_products_without_images(limit=1000):
        sql_string = """SELECT `itpartner_product`.`sku` FROM `itpartner_product` 
            LEFT JOIN `itpartner_image` ON `itpartner_product`.`sku` = `itpartner_image`.`product_sku` 
            WHERE `itpartner_product`.`has_image`=True AND `itpartner_image`.`url` IS NULL LIMIT %s;"""
        
        prepared_statements = (
            limit,
        )

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string, prepared_statements)
                products = cursor.fetchall()

                return [ProductEntity(_sku=product[0]) for product in products]
        finally:
            if connection:
                connection.close()

        return False

    @staticmethod
    def get_active_products_count():
        sql_string = """SELECT COUNT(*) FROM `itpartner_product`
            WHERE `itpartner_product`.`is_deleted`=FALSE 
                AND `itpartner_product`.`is_active`=TRUE;
        """
        
        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string)
                result = cursor.fetchone()

                return pydash.get(result, '0', 0)
        finally:
            if connection:
                connection.close()

        return False

    @staticmethod
    def get_products(limit=1000, offset=0):
        sql_string = """SELECT ip.part, ip.sku, ip.name, ip.price, ip.quantity, ii.url
            FROM itpartner_product ip
            LEFT JOIN (
                SELECT url, product_sku
                FROM itpartner_image
                WHERE id IN (
                SELECT min(id) 
                FROM itpartner_image
                GROUP BY product_sku
                )
            ) ii ON ip.sku =  ii.product_sku
            WHERE ip.is_deleted=FALSE AND ip.is_active=TRUE
            LIMIT %s
            OFFSET %s;"""
        
        prepared_statements = (
            limit,
            offset,
        )

        connection = None

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(sql_string, prepared_statements)
                products = cursor.fetchall()

                return [ProductEntity(
                    _part=product[0], 
                    _sku=product[1],
                    _name=product[2],
                    _price=product[3] if product[3] else '',
                    _quantity=product[4] if product[4] else '',
                    _url=product[5] if product[5] else '',
                    ) for product in products]
        finally:
            if connection:
                connection.close()

        return False
