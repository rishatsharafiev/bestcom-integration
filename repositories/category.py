from utils.db import get_connection

from entities import CategoryEntity


class CategoryRepository:
    """Category Repository"""

    @staticmethod
    def update_or_create(category_entity: CategoryEntity):
        sql_string = """INSERT INTO itpartner_category(id, name, parent_id) 
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = %s, 
            parent_id = %s;
        """
        prepared_statements = (
            category_entity.id,
            category_entity.name,
            category_entity.parent_id,
            category_entity.name,
            category_entity.parent_id,
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
          
