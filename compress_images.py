from PIL import Image
import os



FOLDER_PATH = "./src/assets/ProjectPics/"
MAX_SIZE = (640, 640)
QUALITY = 85                     


IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')


def compress_image(file_path, max_size=MAX_SIZE, quality=QUALITY):
    try:
        img = Image.open(file_path)
        img_format = img.format

        img.thumbnail(max_size, Image.LANCZOS)

        img.save(file_path, format=img_format, quality=quality, optimize=True)
        print(f"Compressed: {file_path}")

    except Exception as e:
        print(f"Error compressing {file_path}: {e}")


def compress_images_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Directory does not exist: {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            file_path = os.path.join(folder_path, filename)
            compress_image(file_path)



compress_images_in_folder(FOLDER_PATH)
