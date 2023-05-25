# coding: utf-8

from app import settings
from app.pdf import PdfMerger

merger = PdfMerger(settings.PDFS_FOLDER)
