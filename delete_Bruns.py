import fitz
import os

pdf_path = "Bruns.pdf"
output_dir = "mnt/data/images"

os.makedirs(output_dir, exist_ok=True)

pdf_document = fitz.open(pdf_path)

# Изменяем диапазон на страницы с 27 по 39 (индексы 26-38)
for page_num in range(26, 39):
    page = pdf_document[page_num]
    text = page.get_text("text")

    text_file_path = os.path.join(output_dir, f"page_{page_num + 1}_text.txt")
    with open(text_file_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]

        image_ext = base_image["ext"]
        image_file_path = os.path.join(output_dir, f"page_{page_num + 1}_image_{img_index + 1}.{image_ext}")

        with open(image_file_path, "wb") as image_file:
            image_file.write(image_bytes)

pdf_document.close()

print("Извлечение завершено. Данные сохранены в папке:", output_dir)
