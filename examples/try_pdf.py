from io import BytesIO

from img2table.document import PDF
from img2table.ocr import TesseractOCR, PaddleOCR


def extract_pdf():
    pdf = PDF(src="data/tables.pdf")
    paddle_ocr = PaddleOCR(lang="en", kw={"use_dilation": True})

    # Extract tables
    extracted_tables = pdf.extract_tables(ocr=paddle_ocr,
                                          implicit_rows=False,
                                          borderless_tables=False,
                                          min_confidence=50)

    print(extracted_tables)

    for page, tables in extracted_tables.items():
        for idx, table in enumerate(tables):
            print(page, idx, table)

    pdf.to_xlsx('data/pdf_tables.xlsx',
                ocr=paddle_ocr)


if __name__ == "__main__":
    extract_pdf()
