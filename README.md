# placementapp
GUVI's placement app
Readme documentation on Placement app & Streamlit UI app

The project has a directory called “guvi” from the root.  Inside guvi, there are two directories called “placementapp” & “streamlitUI”.  

          guvi
            placementapp
            streamlitUI

Placementapp project involves in creating the database, and creates the necessary tables inside the database.  And then creates the source files in csv format using faker library for all the four tables.  And then reads the source csv files and populates the table accordingly.  All the above mentioned operations happens in a single click.  
StreamlitUI project involves in providing an interactive UI in Streamlit.  It has two pages, Candidate Screening which has provision to provide varieties of criteria to filter the suitable candidates.  And it also has Dashboard page which provides some key insights on the placements app.
Following software’s are required as a prerequisite:
•	Python (3.12.1, latest version)
•	Visual studio code
•	MySQL(running instance)

Follow the steps to execute placementapp project:
1.	Open Visual Studio code 
2.	File > Open Folder > point the placementapp folder to launch placementapp project
3.	Navigate to dboperation.py file
4.	In the __init__ method of Dboperation class, update host, password & root and save the file
 
5.	From VS Code terminal, navigate to main.py 
6.	Execute python.exe main.py

Expected outcome:

1.	In MySql, the guvi database is created
2.	Inside guvi database, the following tables are created:
a.	Students
b.	Placements
c.	Softskills
d.	Programming
3.	Following source files are generated in the local:
a.	Students.csv	
b.	Placements.csv
c.	Programming.csv
d.	Softskills.csv
4.	Tables are populated with the source file generated accordingly

Follow the steps to execute streamlitUI project:
1.	Open Visual Studio code 
2.	File > Open Folder > point the streamlitUI folder to launch streamlitUI project
3.	Navigate to db_connection.py file
4.	In the __init__ method of DatabaseManager class, update user, password, host, & database and save the file
5.	From VS Code terminal, navigate to main.py
               
6.	Execute streamlit run main.py


Expected outcome:

1.	A browser is launched with the url http://locahost:{port} 
2.	The side navigation bar has two pages, CandidateScreening & Dashboard
3.	The CandidateScreening section has a form with various input criteria and submit button to filter the candidates
4.	The Dashboard section is the readonly section which provides some key insights on the placement side.
