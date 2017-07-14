import glob
import os
from PIL import Image
import concurrent.futures


def make_image_thumbnail(filename):
    base_filename, file_extension = os.path.splitext(filename)
    thumbnail_filename = f"{base_filename}_thumbnail{file_extension}"

    image = Image.open(filename)
    image.thumbnail(size=(128, 128))
    image.save(thumbnail_filename, "JPEG")

    return thumbnail_filename


with concurrent.futures.ProcessPoolExecutor() as executor:
    image_files = glob.glob("images/*.jpg")

    for image_files, thumbnail_file in zip(image_files, executor.map(make_image_thumbnail, image_files)):
        print(f"A thumbnail for {image_files} was saved as {thumbnail_file}")
