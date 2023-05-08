import psycopg2

def sql_read(query, parameters=[]):
    connection = psycopg2.connect(host='dpg-ch8fghmsi8uhth77afeg-a.oregon-postgres.render.com', user='project2_qc0g_user', port=5432, password='14IHid8sJP55UojaIAJ8cE8k47YNbiMA', dbname='project2')
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results

def sql_write(query, parameters=[]):
    connection = psycopg2.connect(host='dpg-ch8fghmsi8uhth77afeg-a.oregon-postgres.render.com', user='project2_qc0g_user', port=5432, password='14IHid8sJP55UojaIAJ8cE8k47YNbiMA', dbname='project2')
    cursor = connection.cursor()
    cursor.execute(query,parameters)
    connection.commit()
    connection.close()