from flask import Flask
import os
import psycopg2

conn = psycopg2.connect(
        host="postgresql-sflzu7",
        database="postgres_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
