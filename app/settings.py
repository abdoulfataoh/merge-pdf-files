# coding: utf-8

from environs import Env

env = Env()

DEFAULT_OUTPUT_DOC = env.path('DEFAULT_OUTPUT_DOC', 'document.pdf')
