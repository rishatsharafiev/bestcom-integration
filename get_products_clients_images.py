from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "get_products_clients_images.log"
logger = create_rotating_log(log_file)

from services.product import ProductService


@exception(logger)
def main():
    ProductService.get_products_clients_images()

if __name__ == '__main__':
    """Timeit 655.981519066001"""
    """crontab every 20 minutes"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
