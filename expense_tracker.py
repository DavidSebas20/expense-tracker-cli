import argparse
from datetime import datetime
import json
import os


ARCHIVO_GASTOS = 'expenses.json'

#Funcion para cargar el archivo json
def cargar_archivo():
    if not os.path.exists(ARCHIVO_GASTOS):
        print("El archivo no exite creando el archivo...")
        with open(ARCHIVO_GASTOS, 'w') as file:
            json.dump([],file)
        return []
    with open(ARCHIVO_GASTOS, 'r') as file:
        return json.load(file)

#Funcion para guardar los gastos en el json
def gruardar_gastos(tasks):
    with open(ARCHIVO_GASTOS, 'w') as file:
        json.dump(tasks, file, indent=2)
    
def add_gasto(description, mount):
    gastos = cargar_archivo()
    new_id = max(gasto['id'] for gasto in gastos) + 1 if gastos else 1
    new_gasto = {
        "id": new_id,
        "descripcion": description,
        "creacion": datetime.now().strftime('%Y-%m-%d'),
        "monto": mount
    }
    gastos.append(new_gasto)
    gruardar_gastos(gastos)
    print(f"Gasto añadido correctamente (ID: {new_id})")


parser = argparse.ArgumentParser(description="Seguimiento de Gastos CLI")
    
subparsers = parser.add_subparsers(dest="command")

# Comando para agregar un gasto
add_parser = subparsers.add_parser("add", help="Añadir un nuevo gasto")
add_parser.add_argument("--descripcion", required=True, help="Descripcion del gasto")    
add_parser.add_argument("--monto", type=float, required=True, help="Monto del gasto")
args = parser.parse_args()

if args.command == "add":
    add_gasto(args.descripcion, args.monto)
else:
    parser.print_help()
