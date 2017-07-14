import glob
import os
from PIL import Image


def make_image_thumbnail(filename):
    base_filename, file_extension = os.path.splitext(filename)
    thumbnail_filename = f"{base_filename}_thumbnail{file_extension}"

    image = Image.open(filename)
    image.thumbnail(size=(128, 128))
    image.save(thumbnail_filename, "JPEG")

    return thumbnail_filename


for image_file in glob.glob("images/*.jpg"):
    thumbnail_file = make_image_thumbnail(image_file)

    print(f"A thumbnail for {image_file} was saved as {thumbnail_file}")
