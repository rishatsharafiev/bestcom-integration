from utils.db import get_connection

from entities.category import CategoryEntity


class CategoryRepository:
    """Category Repository"""

    @staticmethod
    def mark_all_as_deleted():
        sql_string = "UPDATE itpartner_category SET is_deleted=TRUE;"

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
    def update_or_create(category_entity: CategoryEntity):
        sql_string = """INSERT INTO itpartner_category(id, name, parent_id, is_deleted) 
        VALUES (%s, %s, %s, FALSE)
        ON DUPLICATE KEY UPDATE
            name = %s, 
            parent_id = %s,
            is_deleted=FALSE;
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
          
