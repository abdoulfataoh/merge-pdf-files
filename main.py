# coding: utf-8

import logging
from typing import List
from pathlib import Path
import argparse

from app import settings
from app.pdf import PdfMerger


parser = argparse.ArgumentParser(
    prog='pdfs-merger',
    description='A simple tool to merge pdfs file',
    epilog='https://github.com/abdoulfataoh')

parser.add_argument(
    '-f', '--files',
    action='append',
    required=True,
    nargs='+',
    help='pdf files'
)

parser.add_argument(
    '-o', '--output',
    action='store',
    required=True,
    nargs=1,
    help='destination',
    default=settings.DEFAULT_OUTPUT_DOC
)

parser.add_argument(
    '-s', '--sort',
    action='store_true'
)

parser.add_argument(
    '-v', '--verbose',
    action='store_true'
)

if __name__ == '__main__':
    args = parser.parse_args()
    sort = args.sort
    destination = args.output[0]
    pdfs_paths: List[Path] = []

    if args.verbose is True:
        logging.basicConfig(level=logging.DEBUG)

    for file in args.files[0]:
        path = Path(file)
        if path.suffix == '.pdf':
            pdfs_paths.append(path)

    if not destination.endswith('.pdf'):
        destination = destination + '.pdf'

    merger = PdfMerger(
        pdfs_paths=pdfs_paths,
        sort=sort
    )

    merger.merge(destination)

(merge-pdf-files-py3.10) abdoulfataoh@pc:~/pdfs-merger$ python main.py --help
usage: pdfs-merger [-h] -f FILES [FILES ...] -o OUTPUT [-s] [-v]

A simple tool to merge pdfs file

options:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        pdf files
  -o OUTPUT, --output OUTPUT
                        destination
  -s, --sort
  -v, --verbose

https://github.com/abdoulfataoh
