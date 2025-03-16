import mysql.connector
import streamlit as st
import pandas as pd


 # Manages database connections
class DatabaseManager:
    def __init__(self):
        self.config = {
            'user': "root",
            'password': '12345678',
            'host': 'localhost',
            'database': 'guvi'
        }
        self.connection = None
    
    # Creates and returns a new database connection
    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("Database connection successful!") 
                return self.connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    # Executes the query along with the params and returns the results  
    def executeQuery(self, query, params):     
        db_connection = self.connect()
        cursor = db_connection.cursor()
        if cursor:
            try:
                cursor.execute(query,tuple(params))
                results = cursor.fetchall()
                cursor.close()
                self.close()
                return results
            except mysql.connector.Error as e:
                st.error(f"Error executing query: {e}")

    # To execute the sql query using pandas 
    def fetchResults(self, query):
        db_connection = self.connect()
        df = pd.read_sql(query, db_connection)
        self.close()
        return df
    
    # Closes the DB connection
    def close(self):        
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")