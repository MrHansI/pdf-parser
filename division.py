import os
import shutil

source_folder = 'extracted_trees_data'

txt_folder = os.path.join(source_folder, 'txt_files')
png_folder = os.path.join(source_folder, 'png_files')

os.makedirs(txt_folder, exist_ok=True)
os.makedirs(png_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        if filename.endswith('.txt'):
            shutil.move(file_path, os.path.join(txt_folder, filename))
        elif filename.endswith('.png'):
            shutil.move(file_path, os.path.join(png_folder, filename))

print("Файлы успешно разнесены по папкам.")
