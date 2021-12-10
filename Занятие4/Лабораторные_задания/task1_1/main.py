import json
import re

BOOKS_FILE = "books.md"
# BOOK_REGEX = r"""####\s+(?P<position>\d+)\.\s+\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>.+?)\s+\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)\s+!\[.*?\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)"""
position = r'#\s(?P<position>\d+)'
book_ = r'\[(?P<book>.+?)\]'
book_url = r'//(?P<book_url>.+?)\).+by'
author = r'by\s(?P<author>.+)\s\('
recommended = r'(?P<recommended>\d{1,3}\.\d+%)'
cover_url = r'//(?P<book_url>.+\.png.+?)\)'
description = r'\"(?P<description>.+)\"'
BOOK_REGEX = f'{cover_url}'



def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
