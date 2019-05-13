from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "get_active_products.log"
logger = create_rotating_log(log_file)

from services.product import ProductService


@exception(logger)
def main():
    ProductService.get_active_products()

if __name__ == '__main__':
    """Timeit 199.82189220799773"""
    """Crontab: 30 * * * * /path/to/get_active_products.py"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
