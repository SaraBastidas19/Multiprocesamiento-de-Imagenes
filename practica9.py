from multiprocessing import Pool, cpu_count
from PIL import Image, ImageFilter
import os
import time

input_dir = '/home/adduser/practica4/Multiprocesamiento/val2017/'
output_dir = '/home/adduser/practica4/Multiprocesamiento/'

def procesamiento(file):
    image = Image.open(os.path.join(input_dir, file))
    image = image.filter(ImageFilter.GaussianBlur(2))
    image = image.rotate(45, expand=True)
    image = image.convert('L')
    image = image.filter(ImageFilter.CONTOUR)  # Cambia el filtro a CONTOUR
    image.save(os.path.join(output_dir, file))

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

list_files = os.listdir(input_dir)

# Secuencial
start = time.time()
for file in list_files:
    procesamiento(file)
print('Tiempo total serial: ', time.time() - start, '\n')

# Multiprocesamiento
start = time.time()
p = Pool(processes=cpu_count())
p.map(procesamiento, list_files)
p.close()
p.join()
print('Tiempo total paralelo: ', time.time() - start, '\n')
