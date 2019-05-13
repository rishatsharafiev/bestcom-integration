from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "product.log"
logger = create_rotating_log(log_file)

from services.product import ProductService


@exception(logger)
def main():
    ProductService.update_or_create()

if __name__ == '__main__':
    """Timeit 565.488064137"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
