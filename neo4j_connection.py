import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

user = os.getenv("NEO4J_USER")
protocol = os.getenv("NEO4J_PROTOCOL")
password = os.getenv("NEO4J_PASSWORD")
host = os.getenv("NEO4J_HOST")
port = os.getenv("NEO4J_PORT")
db_name = os.getenv("NEO4J_DB")

neo4j_url = f"{protocol}://{host}:{port}"
neo4j_auth = (user, password)

driver = GraphDatabase.driver(neo4j_url, auth=neo4j_auth)
with GraphDatabase.driver(neo4j_url, auth=neo4j_auth) as driver:
    driver.verify_connectivity()


def read(cypher, database="neo4j"):
    records, summary, keys = driver.execute_query(cypher, database_=database)
    return records, summary, keys


def write(cypher, database="neo4j"):
    records, summary, keys = driver.execute_query(cypher, database_=database)
    return summary
