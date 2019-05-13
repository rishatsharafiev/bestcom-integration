from services.category import CategoryService


def main():
    CategoryService.update_or_create()

if __name__ == '__main__':
    """Timeit 13.403407009001967"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
