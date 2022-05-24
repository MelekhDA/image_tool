"""
Tools for working with images:
    1) Convert bytes to 3d numpy matrix
    2) Convert 3d numpy matrix to bytes

P.s. 3d numpy matrix is (height, width, channels=3)
"""

import zlib

import cv2
import numpy as np

DEFAULT_EXTENSION = '.jpg'


def image_to_byte(image: np.ndarray,
                  is_compress: bool = False,
                  ext: str = DEFAULT_EXTENSION) -> bytes:
    """
    Convert 3d numpy matrix to bytes

    :param image: image with shape == (height, width, channels == 3)
    :param is_compress: compress bytes if it's True
    :param ext: extension type (see cv2.imencode(...))

    :return: image as bytes
    """

    numpy_array = cv2.imencode(ext, image)[1]
    byte_image = numpy_array.tobytes()

    if is_compress:
        byte_image = zlib.compress(byte_image)

    return byte_image


def byte_to_image(image: bytes,
                  is_decompress: bool = False,
                  flags: int = cv2.IMREAD_COLOR) -> np.ndarray:
    """
    Convert bytes to 3D numpy matrix

    :param image: image
    :param is_decompress: compress bytes if it's True
    :param flags: flags for decoding (see cv2.imdecode(...))

    :return: image as 3d numpy matrix
    """

    if is_decompress:
        image = zlib.decompress(image)

    numpy_array = np.frombuffer(image, np.uint8)
    numpy_image = cv2.imdecode(numpy_array, flags)

    return numpy_image
