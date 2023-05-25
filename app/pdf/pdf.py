# coding: utf-8

import logging
from typing import List
from pathlib import Path

import fitz

logger = logging.getLogger(__name__)

class PdfMerger:

    _pdf_folder: Path
    _pdf_files: List[Path]

    def __init__(self, pdf_folder: Path) -> None:
        logger.info(f'init pdfs files merging at {pdf_folder}')
        self._pdf_folder = pdf_folder
        find_pdf_query = pdf_folder.rglob('*.pdf')
        self._pdf_files = list(find_pdf_query)
        self._pdf_files.sort()

    def merge(self, output: Path) -> None:
        merger_document = fitz.open()
        for pdf_path in self._pdf_files:
            logger.info(f'insert {pdf_path} to document')
            document = fitz.open(pdf_path)
            merger_document.insert_pdf(document)
        merger_document.save(output)
