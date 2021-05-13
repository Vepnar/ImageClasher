"""Generate Images & try to create a collision with malware"""

__version__ = '0.1'
__author__ = 'Arjan de Haan'

import io
import os
import time
import hashlib

from PIL import Image
import numpy as np
import multiprocessing as mp

# Last variable in this tuple are the colour bytes
IMAGE_SIZE = (512, 512, 3)
IMAGE_TYPES = ['PNG', 'JPEG']
ALGORITHMS = ['MD5', 'SHA1', 'SHA2', 'SHA256']

def read_hash_file(path: str) -> list:
    """Read the file with hashes and store the hashes in a list which is returned"""
    hashes = []
    with open(path, 'r') as file:
        for line in file:
            # Convert lowercase & remove new line character.
            hashes.append(line.lower()[:-1])
    return hashes

def read_hash_files(algorithms: list) -> dict:
    """Read multiple hash files and return them into a dict with the according algorithm name"""
    hashing_dict = {}
    for algorithm in algorithms:
        file_name = f'{algorithm}.txt'

        # Check if the file exists & skip if it doesn't exist.
        if not os.path.isfile(file_name):
            print(f'Hash list {file_name} is not found.')
            continue

        # Read the hashes & update the hashing dict
        hashes = read_hash_file(file_name)

        print(f'Hash file: {file_name} found with {len(hashes)} entries')
        hashing_dict.update({algorithm: hashes})
    return hashing_dict

def generate_hash(image_bytes : bytes, algoritm : str) -> str:
	"""Hash the given image with the given hashing algorithm"""
	hash_function = hashlib.new(algoritm)
	hash_function.update(image_bytes)
	return hash_function.hexdigest()

def generate_image() -> Image:
	"""Generate a random image"""
	pixels = np.random.randint(0, 255, IMAGE_SIZE, dtype='uint8')
	image = Image.fromarray(pixels, 'RGB')
	return image

def get_image_bytes(image : Image, image_type : str) -> bytes:
	"""Convert image object into bytes.
	
	TODO: There should be a better way of doing this.
	Removing pillow from the process will most likely speed up the application a lot.
    	"""
	# Get bytes from image
	output = io.BytesIO()
	image.save(output, format=image_type)
	return output.getvalue()


def clash_hashes(hash_dict: dict):
    """Do a single attempt of clashing a random image with the hash dict"""

    # Create pillow image object
    image = generate_image()
    for image_format in IMAGE_TYPES:
        image_bytes = get_image_bytes(image, image_format)

        collisions = []
        for algorithm in hash_dict.keys():
            image_hash = generate_hash(image_bytes, algorithm)

            # Check if there is a collision
            if image_hash in hash_dict[algorithm]:
                print(image_hash, algorithm)  # Print success
                collisions.append(algorithm)

        if collisions:
            # Add a random bit to prevent collisions in the path :)
            collisions.append(round(time.time() * 1000))

            # Use the collisions & the random bits to generate a name for the file.
            image.save('-'.join(collisions), image_format)

    clash_hashes(hash_dict)

def main():
    """Infinite loop to keep trying to clash hashes"""
    hashing_dict = read_hash_files(ALGORITHMS)

    if not hashing_dict:
        print('No hashing files found')
        return

    # Random seed since the multiprocess instances have the same seed.
    np.random.seed(seed=None)

    while 1:
        clash_hashes(hashing_dict)

if __name__ == '__main__':
    main()
