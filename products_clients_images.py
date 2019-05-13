#!/usr/bin/env python3

from ...utils.db.connection import get_connection

if __name__ == '__main__':
    a = get_connection()
    print(a)
