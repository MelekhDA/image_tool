"""
Functions for creating, generating or getting a image
"""

import numpy as np


def generate_numpy_image(shape: tuple,
                         intensity_color: int = 0) -> np.ndarray:
    """
    Generate image as 3d numpy martix (with RGB)

    :param shape: (height, width, channels)
    :param intensity_color: defines the intensity of the color as an integer between 0 and 255

    :return: image as 3d numpy matrix
    """

    if 0 > intensity_color > 255:
        raise ValueError(f'Value {intensity_color} must be between 0 and 255')

    image = np.full(shape, intensity_color, dtype=np.uint8)

    return image


def read_byte_image(path_image: str) -> bytes:
    """
    Get image as bytes

    :param path_image: path to image

    :return: image as bytes
    """

    with open(path_image, 'rb') as fio:
        byte_image = fio.read()

    return byte_image
