from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "category.log"
logger = create_rotating_log(log_file)

from services.category import CategoryService


@exception(logger)
def main():
    CategoryService.update_or_create()

if __name__ == '__main__':
    """Timeit 13.403407009001967"""
    import timeit
    print(timeit.Timer(main).timeit(number=1))
