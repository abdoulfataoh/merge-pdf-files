# coding: utf-8

import logging
from environs import Env

logging.basicConfig(level=logging.INFO)

env = Env()

PDFS_FOLDER = env.path('PDFS_FOLDER', r'pdf-folder')
DEFAULT_OUTPUT_DOC = env.path('DEFAULT_OUTPUT_DOC', 'document.pdf')
