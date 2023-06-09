import psycopg2
import os

def sql_read(query, parameters=[]):
    connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results

def sql_read2(query, parameters=[]):
    connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchone()
    connection.close()
    return results    

def sql_write(query, parameters=[]):
    connection = psycopg2.connect(host=os.getenv("PGHOST"), user=os.getenv("PGUSER"), password=os.getenv("PGPASSWORD"), port=os.getenv("PGPORT"), dbname=os.getenv("PGDATABASE"))
    cursor = connection.cursor()
    cursor.execute(query,parameters)
    connection.commit()
    connection.close()

