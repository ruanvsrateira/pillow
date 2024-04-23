import os
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
IMAGE_NAME = input("Digite o nome do arquivo da imagem: ")

try:
  if not IMAGE_NAME in os.listdir():
    raise FileNotFoundError()
  
  pill_image = Image.open(ROOT / IMAGE_NAME)
  width, height = pill_image.size

  print(
  f"\n[Arquivo Encontrado]\nNome do Arquivo: {IMAGE_NAME}\nDimensões da Imagem: {width}x{height}\n")

  new_width = int(input("Digite a nova largura da imagem para realizar o redimensionamento: "))
  new_image_name = input("Digite o novo nome do arquivo (OBS: sem a extensão): ")
  new_height = round(height * new_width / width)
  new_pill_image = pill_image.resize(size=(new_width, new_height))
  new_pill_image.save(f"{ROOT / new_image_name}.{pill_image.format.lower()}")
  print(f"\n[Imagem Criada]\nNova Dimensão: {new_width}x{new_height}\n")
  
except FileNotFoundError:
  print("Arquivo não encontrado")
except ValueError as ve:
  print("Valor Inválido!")