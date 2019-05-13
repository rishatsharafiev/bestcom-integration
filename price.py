from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "price.log"
logger = create_rotating_log(log_file)

from services.price import PriceService


@exception(logger)
def main():
    PriceService.update()

if __name__ == '__main__':
    """Timeit 655.981519066001"""
    """Crontab: 50 * * * * /path/to/price.py"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
