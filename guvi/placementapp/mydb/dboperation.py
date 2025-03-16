import mysql.connector
import pandas as pd


# Manages the DB operations like creation of database, relevant tables, populating the tables 
# by reading the source files etc.

class Dboperation:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            password="12345678",
            user="root"
        )
        Dboperation.cursor = self.connection.cursor()

    # Create GUVI database
    def createDatabase(self):
        query = "CREATE DATABASE IF NOT EXISTS guvi" 
        Dboperation.cursor.execute(query)   

    # Use DB command
    def useDB(self, dbName):
        query = "use {}".format(dbName)
        self.executeQuery(query)    
    
    # Create Students table
    def createStudentsTable(self):
        self.useDB("guvi")       
        query = """create table if not exists students(
                    student_id int primary key,
                    name varchar(100) not null,
                    age int,
                    gender varchar(10) not null,
                    email varchar(100) not null,
                    phone varchar(20),
                    enrollment_year year,
                    course_batch varchar(20),
                    city varchar(30),
                    graduation_year year
                )"""        
        self.executeQuery(query)

    # Create Programming table
    def createProgrammingTable(self):
        self.useDB("guvi")       
        query = """create table if not exists programming(
                    programming_id int primary key,
                    student_id int, foreign key(student_id) references students(student_id),
                    language varchar(30) not null,
                    problems_solved int not null,
                    assessments_completed int not null,
                    mini_projects int not null,
                    certifications_earned int not null,
                    latest_project_score int not null
                )"""
        self.executeQuery(query)        

    # Create SoftSkills table
    def createSoftSkillsTable(self):
        self.useDB("guvi")      
        query = """create table if not exists softskills(
                    soft_skill_id int primary key,
                    student_id int, foreign key(student_id) references students(student_id),
                    communication int,
                    teamwork int not null,
                    presentation varchar(20) not null,
                    leadership varchar(50),
                    critical_thinking int,
                    interpersonal_skills int
        )"""
        self.executeQuery(query)   

    # Create Placements table
    def createPlacementsTable(self):
        self.useDB("guvi")        
        query = """create table if not exists placements(
                    placement_id int primary key,
                    student_id int, foreign key(student_id) references students(student_id),
                    mock_interview_score int,
                    internships_completed int not null,
                    placement_status varchar(20) not null,
                    company_name varchar(50),
                    placement_package int,
                    interview_rounds_cleared int,
                    placement_date date
        )"""
        self.executeQuery(query)   

    # Execute the query and commit it
    def executeQuery(self, query, row=None):
        if row is None:
            Dboperation.cursor.execute(query)
        else:
            Dboperation.cursor.execute(query, row)
        self.connection.commit()

    # Close the DB connections
    def closeConnections(self):
        Dboperation.cursor.close()
        self.connection.close()


    # Populate the students table from the data available in the source file
    def populateStudentsTable(self):
        df = pd.read_csv('students.csv', encoding='latin1')
        for index, row in df.iterrows():            
            self.useDB("guvi")
            placeholders = ','.join(['%s'] * df.shape[1])
            query = f"""INSERT INTO students VALUES ({placeholders})"""            
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])            
            Dboperation.cursor.execute(query, values)
            self.connection.commit()
            
    # Populate the programming table from the data available in the source file        
    def populateProgrammingTable(self):
        df = pd.read_csv('programming.csv', encoding='latin1')
        for index, row in df.iterrows():            
            self.useDB("guvi")
            placeholders = ','.join(['%s'] * df.shape[1])
            query = f"""INSERT INTO programming VALUES ({placeholders})"""            
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            Dboperation.cursor.execute(query, values)
            self.connection.commit()  

    # Populate the softskills table from the data available in the source file
    def populateSoftskillsTables(self):
        df = pd.read_csv('softskills.csv', encoding='latin1')
        for index, row in df.iterrows():            
            self.useDB("guvi")
            placeholders = ','.join(['%s'] * df.shape[1])
            query = f"""INSERT INTO softskills VALUES ({placeholders})"""            
            values = (int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]))
            Dboperation.cursor.execute(query, values)
            self.connection.commit()  

    # Populate the placements table from the data available in the source file
    def populatePlacementsTable(self):
        df = pd.read_csv('placements.csv', encoding='latin1')
        for index, row in df.iterrows():            
            self.useDB("guvi")
            placeholders = ','.join(['%s'] * df.shape[1])
            query = f"""INSERT INTO placements VALUES ({placeholders})"""            
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            Dboperation.cursor.execute(query, values)
            self.connection.commit()  