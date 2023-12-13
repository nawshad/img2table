import os
import cv2
from utils import display_borderless_tables

'''
Steps:

(1) You need to setup venv, pycharm should automatically get it 
otherwise create an environment and use pip -r requirements.txt
(2) Install PaddleOCR through pip install img2table[paddle]
(3) You should be able to run this file which can parse a borderless
table. 

'''

from img2table.document import Image
from img2table.ocr import TesseractOCR, PaddleOCR


def table_extract():
    img = Image("data/borderless.jpg")
    # tesseract = TesseractOCR()
    paddle_ocr = PaddleOCR(lang="en", kw={"use_dilation": True})

    # Extract tables with Tesseract and PaddleOCR
    tables = img.extract_tables(ocr=paddle_ocr, borderless_tables=True)
    tables[0].df.to_csv("data/borderless_table.csv")
    print(tables[0].df)


if __name__ == "__main__":
    table_extract()