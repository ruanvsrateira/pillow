from pathlib  import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / "original.webp"
REDIMENSIONED_IMAGE_PATH = ROOT_FOLDER / "redimensioned.webp"

#Abrindo Imagem no Pillow
pil_image = Image.open(IMAGE_PATH)

#Mostando Largura e Altura da Imagem
width, height = pil_image.size
print(f"Width: {width}px\nHeight: {height}px\n")

#Pegando Metadados
exif = pil_image.info
print(f"Metadata: {exif}\n")

#Redimensionando Imagem
new_width = 1920
new_height = round(height * new_width / width)
redimensioned_image = pil_image.resize(size=(new_width, new_height))
redimensioned_image.save(REDIMENSIONED_IMAGE_PATH)

print(f"Redimensioned width: {new_width}px\nRedimensioned height: {new_height}px\n")