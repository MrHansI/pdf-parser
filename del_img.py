import fitz  # PyMuPDF
import os
import re

pdf_path = "Bruns.pdf"
output_dir = "mnt/data/text"

os.makedirs(output_dir, exist_ok=True)

pdf_document = fitz.open(pdf_path)

for page_num in range(26, 39):
    page = pdf_document[page_num]
    text = page.get_text("text")

    lines = text.splitlines()
    for i in range(len(lines)):
        if lines[i].strip() and i + 1 < len(lines) and lines[i + 1].strip():
            title = lines[i].strip() + " " + lines[i + 1].strip()
            main_text = []
            for j in range(i + 2, len(lines)):
                if lines[j].strip():
                    main_text.append(lines[j].strip())
                else:
                    break
            main_text_str = "\n".join(main_text)

            safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
            safe_title = re.sub(r'\s+', '_', safe_title)
            text_file_path = os.path.join(output_dir, f"{safe_title}.txt")
            with open(text_file_path, "w", encoding="utf-8") as text_file:
                text_file.write(main_text_str)
            print(f"Сохранён файл: {text_file_path}")

pdf_document.close()

print("Извлечение завершено. Данные сохранены в папке:", output_dir)