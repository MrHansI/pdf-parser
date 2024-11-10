import fitz  # PyMuPDF
import easyocr
import cv2
import numpy as np
import os
from tqdm import tqdm

pdf_path = "trees.pdf"
output_dir = "extracted_trees_data"

os.makedirs(output_dir, exist_ok=True)

reader = easyocr.Reader(['ru', 'en'])

pdf_document = fitz.open(pdf_path)

for page_num in tqdm(range(pdf_document.page_count), desc="Обработка страниц", unit="страница"):
    page = pdf_document[page_num]

    pix = page.get_pixmap()
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    result = reader.readtext(img_rgb)

    text = '\n'.join([det[1] for det in result])

    with open(f"{output_dir}/page_{page_num + 1}_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    cv2.imwrite(f"{output_dir}/page_{page_num + 1}.png", img_rgb)

pdf_document.close()

print("Извлечение текста и изображений завершено.")
