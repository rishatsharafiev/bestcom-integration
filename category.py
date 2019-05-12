from services.category import CategoryService


def main():
    CategoryService.update_or_create()

if __name__ == '__main__':
    import timeit
    print(timeit.Timer(main).timeit(number=1))
