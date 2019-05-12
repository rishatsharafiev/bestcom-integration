from api.category import CategoryApi
from repositories.category import CategoryRepository
from entities.category import CategoryEntity


class CategoryService:

    @classmethod
    def parse(cls, childrens, parent_id=None):
        for category in childrens:
            childrens = category.get('childrens', [])
            category_id = category.get('id')
            category_name = category.get('name')
            if not category.get('leaf'):
                category_entity = CategoryEntity(
                    _id=category_id,
                    _name=category_name,
                    _parent_id=parent_id,
                )
                category_row_id = CategoryRepository.update_or_create(category_entity=category_entity)
                cls.parse(childrens, category_id)
            else:
                category_entity = CategoryEntity(
                    _id=category_id,
                    _name=category_name,
                    _parent_id=parent_id,
                )
                category_row_id = CategoryRepository.update_or_create(category_entity=category_entity)

    @classmethod
    def update_or_create(cls):
        # mark all previous data as deleted
        CategoryRepository.mark_all_as_deleted()

        # get data
        categories = CategoryApi.get_all()

        # parse and save
        cls.parse(categories)
