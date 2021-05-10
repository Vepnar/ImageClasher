"""Generate Images & try to create a collision with malware"""

__version__ = '0.1'
__author__ = 'Arjan de Haan'

import io
import os
import hashlib

from time import sleep
from PIL import Image
import numpy as np
import multiprocessing as mp

# Last variable in this tuple is the colour bytes
IMAGE_SIZE = (512, 512, 3)
IMAGE_TYPES = ['PNG', 'JPEG']

def read_hash_file(path: str) -> list:
	"""Read the file with hashes, and store the hashes in a list which is returned"""
	hashes = []
	with open(path, 'r') as file:
		# Convert lowercase & remove new line character.
		hashes.append(line.lower()[:-1])

	return hashes

def read_hash_files(algorithms: list) -> dict:
	"""Read multiple hashing files and return them into a dict with the according algorithm name"""
	hashing_dict = {}
	for algorithm in algorithms:
		hashes = read_hash_file(f'{algoritm}.txt')
		hashing_dict.update({algorithm: hashes})
	return hashing_dict

def generate_hash(image_bytes : bytes, algoritm : str) -> str:
	"""Hash the given image with the given hashing algorithm"""
	hash_function = hashlib.new(algoritm)
	hash_function.update(image_bytes)
	return hash_function.hexdigest()

def generate_image() -> Image:
	pixels = np.random.randint(0, 255, IMAGE_SIZE, dtype='uint8')
	image = Image.fromarray(pixels, 'RGB')
	return image

def get_image_bytes(image : Image, image_type : str) -> bytes:
	# There should be a better way of doing this.
	# Removing pillow from the process might speed up the application a lot

	# Get bytes from image
	output = io.BytesIO()
	image.save(output, format=image_type)
	return output.getvalue()


	
