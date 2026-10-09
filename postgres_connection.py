import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="researchhub",
    user="postgres",
    password="nivas@0101",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("""
    SELECT publication_id, title, publication_year, journal, research_area
    FROM research.publications
    ORDER BY publication_id;
""")

publications = cursor.fetchall()

for publication in publications:
    print(publication)

cursor.close()
connection.close()