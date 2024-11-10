import fitz  # PyMuPDF
import os

pdf_path = "Katalog_Lorberg_RU.pdf"
output_dir = "extracted_text_only"

os.makedirs(output_dir, exist_ok=True)

pdf_document = fitz.open(pdf_path)

text_counter = 1
start_saving = False

for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    images = page.get_images(full=True)

    for img_index, img in enumerate(images):
        xref = img[0]

        image_rect = page.get_image_rects(xref)[0]
        text_rect = fitz.Rect(image_rect.x0, image_rect.y1, image_rect.x1, page.rect.y1)
        text_under_image = page.get_text("text", clip=text_rect).strip()

        if "Качество" in text_under_image:
            start_saving = True

        if start_saving:
            text_file_path = os.path.join(output_dir, f"text_{text_counter}.txt")
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                if text_under_image:
                    text_file.write(text_under_image)
                else:
                    text_file.write("Под изображением нет данных.")

            text_counter += 1

pdf_document.close()

print("Извлечение текстов завершено. Данные сохранены в папке:", output_dir)
