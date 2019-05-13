#!/usr/bin/env python3

from utils.logging.loggers import create_rotating_log
from utils.logging.decorators import exception

log_file = "exception.log"
logger = create_rotating_log(log_file)

@exception(logger)
def main():
    raise Exception('Hello')

if __name__ == '__main__':
    main()
