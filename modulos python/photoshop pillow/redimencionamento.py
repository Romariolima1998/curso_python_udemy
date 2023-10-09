from PIL import Image
from pathlib import Path

root_folder = Path(__file__).parent
original = root_folder / 'imagem.jpg'
new = root_folder / 'nova_imagem.jpg'

pil_image = Image.open(original)

width, height = pil_image.size
# exif = pil_image.info['exif']
# print(pil_image.info)

new_width = round(width / 2)
new_height = round(height / 2)
print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    new,
    optimize=True,
)