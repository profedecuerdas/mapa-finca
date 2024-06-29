#script del 1 de junio, que procesa las coordenadas de un .kml como el que se exporta de google o mi-ruta y los guarda en un csv, en este caso, incluyendo el valor del color del marcador de miruta

import xml.etree.ElementTree as ET
import csv

# Parsear el archivo .kml
tree = ET.parse('kml3p.kml')
root = tree.getroot()

# Espacio de nombres para el archivo .kml
namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

# Crear una lista para almacenar los datos
data = []

# Extraer los datos de cada Placemark
for placemark in root.findall('.//kml:Placemark', namespace):
    name = placemark.find('kml:name', namespace).text
    coordinates = placemark.find('.//kml:coordinates', namespace).text.strip()
    #color = placemark.find('.//kml:value', namespace).text
    
    # Separar las coordenadas en latitud, longitud y altitud
    lon, lat = coordinates.split(',')
    
    # Agregar los datos a la lista
    data.append([name, lat, lon, color])

# Escribir los datos en un archivo CSV
with open('kml3p.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escribir la cabecera del CSV
    csvwriter.writerow(['Nombre', 'Latitud', 'Longitud', 'Color'])
    
    # Escribir las filas de datos
    csvwriter.writerows(data)

print("Datos guardados en 'fincajun1.csv'")
