import os
import glob

output_dir = "extracted_data"

txt_files = glob.glob(os.path.join(output_dir, "*.txt"))
for txt_file in txt_files:
    os.remove(txt_file)

print("Все .txt файлы удалены из папки:", output_dir)