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
