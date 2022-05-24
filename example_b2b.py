import cv2

from generate_image import read_byte_image
from image import byte_to_image, image_to_byte

PATH_IMAGE = 'data/example.jpg'

byte_image_before = read_byte_image(PATH_IMAGE)

numpy_image = byte_to_image(byte_image_before)

# preprocessing, e.x.:
# numpy_image = resize(numpy_image)

byte_image_after = image_to_byte(numpy_image)
