from faker import Faker
import csv
from .commonCustomProvider import commonCustomProvider
import pandas as pd

############################################ Create source CSV files ##############################################
# Using the faker library, the source data is generated in the four different CSV files mentioned below:
# students.csv
# programming.csv
# softskills.csv
# placements.csv

# The data from the source file is later used to populate the tables accordingly.
###################################################################################################################

class CreateSourceCSV: 
    def __init__(self):
        self.fake = Faker('en-IN')
        self.fake.add_provider(commonCustomProvider)

    # Creates students.csv file
    def createStudentCSV(self):
        try:
            with open('students.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['student_id','name','age','gender','email','phone','enrollment_year','course_batch','city','graduation_year'])
                for n in range(1,101):
                    writer.writerow(self.generate_studentInfo(n))
        except PermissionError:
            print("Error:  No permission to create/write to the file")
        except OSError as e:
            print(f"OS Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    def generate_studentInfo(self, studentID):
        return [studentID, 
                self.fake.name(),
                self.fake.age(),
                self.fake.gender(),
                self.fake.email(),
                self.fake.phone_number(),
                self.fake.year(2020, 2025),
                self.fake.course(),
                self.fake.city(),
                self.fake.year(2000 ,2025)]

    # Creates programming.csv file
    def createProgrammingCSV(self):
        try:
            with open('programming.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['programming_id','student_id','language','problems_solved','assessments_completed','mini_projects','certifications_earned','latest_project_score'])
                for n in range(1,501):
                   writer.writerow(self.generate_programmingPerformance(n))            
        except PermissionError:
            print("Error:  No permission to create/write to the file")
        except OSError as e:
            print(f"OS Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    def getStudentID(self):
        df = pd.read_csv('students.csv', encoding="ISO-8859-1")
        return df['student_id'].sample(n=1).iloc[0]

    def generate_programmingPerformance(self,progamID):
        return [progamID,                 
                self.getStudentID(),
                self.fake.language(),
                self.fake.num(0, 300),
                self.fake.num(0, 10),
                self.fake.num(0, 10),
                self.fake.num(0, 50),
                self.fake.num(0, 100)]
    
    # Creates softskills.csv file
    def createSoftSkillCSV(self):
        try:
            with open('softskills.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['soft_skill_id','student_id','communication','teamwork','presentation','leadership','critical_thinking','interpersonal_skills'])
                for n in range(1,101):
                    writer.writerow(self.generate_softskills(n))
        except PermissionError:
            print("Error:  No permission to create/write to the file")
        except OSError as e:
            print(f"OS Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")


    def generate_softskills(self, softSkillID):
        return [softSkillID, 
                softSkillID,
                self.fake.num(0, 100),
                self.fake.num(0, 100),
                self.fake.num(0, 100),
                self.fake.num(0, 100),
                self.fake.num(0, 100),
                self.fake.num(0, 100)]
    
    # Creates placements.csv file
    def createPlacementsCSV(self):
        try:
            with open('placements.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['placement_id','student_id','mock_interview_score','internships_completed','placement_status','company_name','placement_package','interview_rounds_cleared','placement_date'])
                for n in range(1,101):
                    writer.writerow(self.generate_placements(n))
        except PermissionError:
            print("Error:  No permission to create/write to the file")
        except OSError as e:
            print(f"OS Error: {e}")
        except Exception as e:
            print(f"An unexpected error has occurred: {e}")

    def generate_placements(self, placementID):
        return [placementID, 
                placementID,
                self.fake.num(0, 100),
                self.fake.num(0, 5),
                self.fake.placementStatus(),
                self.fake.companyName(),
                self.fake.num(1500000, 10000000),
                self.fake.num(0, 10),
                self.fake.placedDate(self.fake)]