from utils.db import get_connection

from entities.image import ImageEntity


class ImageRepository:
    """Image Repository"""

    @staticmethod
    def create(image_entity: ImageEntity):
        sql_string = "INSERT INTO itpartner_image(url, product_sku) VALUES (%s, %s);"

        prepared_statements = (
            image_entity.url,
            image_entity.sku,
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
