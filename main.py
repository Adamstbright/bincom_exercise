import psycopg2


connection = psycopg2.connect(database="bincom", user="postgres", password="tobebe1995", host="localhost", port="5432")

cursor = connection.cursor()
cursor.execute("SELECT SUM(green)from color;")
data = cursor.fetchall()

