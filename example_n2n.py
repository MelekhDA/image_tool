import cv2
import numpy as np

from generate_image import generate_numpy_image
from image import byte_to_image, image_to_byte

height, width, channels = 510, 510, 3
shape = (height, width, channels)

numpy_image_before = generate_numpy_image(shape)

byte_image = image_to_byte(numpy_image_before, is_compress=True)

numpy_image_after = byte_to_image(byte_image, is_decompress=True)

assert numpy_image_before.shape == numpy_image_after.shape, (
    f'Dimensions {numpy_image_before.shape} and {numpy_image_after.shape} did not match'
)
assert np.array_equal(numpy_image_before, numpy_image_after), (
    f'Arrays {numpy_image_before} and {numpy_image_after} did not match'
)

cv2.imshow('image before', numpy_image_before)
cv2.imshow('image after', numpy_image_after)
cv2.waitKey(0)
