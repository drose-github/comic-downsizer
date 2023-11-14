import os
import zipfile
import rarfile
import shutil
from PIL import Image

def extract_resize_rearchive(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            extract_dir = os.path.join(root, os.path.splitext(file)[0])
            if file.lower().endswith('.cbz'):
                print(f"Extracting: {file}")
                with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)

            elif file.lower().endswith('.cbr'):
                print(f"Extracting: {file}")
                with rarfile.RarFile(os.path.join(root, file), 'r') as rar_ref:
                    rar_ref.extractall(extract_dir)

            resize_images(extract_dir)
            rearchive(extract_dir, file)

def resize_images(directory):
    print(f"Entered Resizing Function")
    contains_webp = False
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg', '.webp')):
                if file.lower().endswith('.webp'):
                    contains_webp = True
                img_path = os.path.join(root, file)
                img = Image.open(img_path)
                if img.height > 1500:
                    print(f"Resizing: {file}")
                    w = int((1440 / img.height) * img.width)
                    img = img.resize((w, 1440), Image.LANCZOS)
                    img.save(img_path)
    if contains_webp:
        print(f"Contains WebP: {directory}")
        with open('webp_archives.txt', 'w') as f:
            f.write(f"{os.path.basename(directory)}\n")

def rearchive(directory, original_file):
    print(f"Re-archiving: {original_file}")
    shutil.make_archive(directory, 'zip', directory)
    new_file_name = f"{directory}.cbz"
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    os.rename(f"{directory}.zip", new_file_name)
    if original_file.lower().endswith('.cbr'):
        os.remove(os.path.join(os.path.dirname(directory), original_file))
    shutil.rmtree(directory)

# Use the function
extract_resize_rearchive('c:\\comictest')