import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loads data from files stored in S3 bucket into the staging tables using the copy_table queries stated on the 
    sql_queries script. 
    Parameters
    ----------
    cur: database cursor
    conn: database connector
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Selects and transforms data from the staging tables into the dimensional tables using the insert_table 
    queries stated on the sql_queries script.
    Parameters
    ----------
    cur: Database cursor
    conn: Database connector
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Extracts the activity data of the user and songs metadata from a S3 bucket, transforms the data with the use 
    of a staging table, and loads the data into  the dimensional tables for further analysis.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()