"""
FELIPEDELOSH

Probar conexión a base de datos POSTGRESQL
"""
import psycopg2 # python -m pip install psycopg2

try:
    # Conexión a la base de datos
    connection = psycopg2.connect(
    user="postgres",
    password="kmzwa8awaa",
    host="localhost",
    port="5432",
    database="ejemplo",
    options="-c client_encoding=UTF8"
    )

    cursor = connection.cursor()
    # Print PostgreSQL details
    print("Conexión exitosa")
    print("Información del servidor:", connection.get_dsn_parameters(), "\n")
    
    # Ejecuta una consulta
    cursor.execute("SELECT version();")
    
    # Obtén el resultado
    record = cursor.fetchone()
    print("Versión de PostgreSQL:", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error al conectar a PostgreSQL", error)

finally:
    # Cierra la conexión
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("Conexión a PostgreSQL cerrada")