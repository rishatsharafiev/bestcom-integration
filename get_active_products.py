from services.product import ProductService


def main():
    ProductService.get_active_products()

if __name__ == '__main__':
    """Timeit 199.82189220799773"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
