from myfaker.createsourcecsv import CreateSourceCSV
from mydb.dboperation import Dboperation

createSourcefile = CreateSourceCSV()
dbOps = Dboperation()

if __name__ == "__main__":
     dbOps.createDatabase()
     dbOps.createStudentsTable()
     dbOps.createProgrammingTable()
     dbOps.createSoftSkillsTable()
     dbOps.createPlacementsTable()
     createSourcefile.createStudentCSV()
     createSourcefile.createProgrammingCSV()
     createSourcefile.createSoftSkillCSV()
     createSourcefile.createPlacementsCSV()
     dbOps.populateStudentsTable()
     dbOps.populateProgrammingTable()
     dbOps.populateSoftskillsTables()
     dbOps.populatePlacementsTable()