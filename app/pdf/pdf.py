# coding: utf-8

import logging
from typing import List
from pathlib import Path

import fitz

logger = logging.getLogger(__name__)


class PdfMerger:

    _pdf_files: List[Path]

    def __init__(self, pdfs_paths: List[Path], sort: bool = False) -> None:
        self._pdf_files = pdfs_paths
        if sort:
            self._pdf_files.sort()

    def merge(self, output: Path) -> None:
        merger_document = fitz.open()
        for pdf_path in self._pdf_files:
            logger.info(f'insert {pdf_path} to document')
            document = fitz.open(pdf_path)
            merger_document.insert_pdf(document)
        merger_document.save(output)
