# management/commands/import_books.py

from ...models import Libro, Autor
import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Agregar libros desde un archivo CSV después de limpiar la tabla'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Ruta al archivo CSV con los datos de los libros')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        # Elimina todos los registros de la tabla Libro
        Libro.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Tabla Libro limpiada correctamente'))

        with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:  # Agregar 'utf-8-sig' para manejar el BOM
            reader = csv.DictReader(file)

            # Mostrar los nombres de las columnas para depuración
            self.stdout.write("Nombres de las columnas en el archivo CSV:")
            self.stdout.write(", ".join(reader.fieldnames))

            for row in reader:
                # Eliminar BOM
                row = {key.lstrip('\ufeff'): value for key, value in row.items()}
                print("Procesando fila:", row)
                titulo = row['libro']  # Ajusta el nombre de la columna según el archivo CSV
                autor_nombre = row['autor']  # Ajusta el nombre de la columna según el archivo CSV
                lenguaje = row['lenguaje']
                publicacion = row['publicacion']  # Ya no es un DateField, así que se mantiene como cadena
                ventas = row['ventas']
                genero = row['genero']

                # Busca o crea el autor
                autor, _ = Autor.objects.get_or_create(nombre=autor_nombre)

                # Crea el libro
                Libro.objects.create(
                    titulo=titulo,
                    autor=autor,
                    lenguaje=lenguaje,
                    publicacion=publicacion,  # Mantén como CharField o similar
                    ventas=ventas,
                    genero=genero
                )

            self.stdout.write(self.style.SUCCESS('Datos del CSV importados correctamente'))