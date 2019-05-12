from services.product import ProductService


def main():
    ProductService.update_or_create()

if __name__ == '__main__':
    import timeit
    print(timeit.Timer(main).timeit(number=1))
