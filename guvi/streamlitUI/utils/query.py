from utils.db_connection import DatabaseManager

# Creating a DB instance for DatabaseManager class
db = DatabaseManager()


# Class to manage the repository of queries used to populate the dashboard
class Query:
    # Query: To fetch the total no of candidates placed in top international MNC's
    def candidatesPlacedinMNC(self):
        query = """
            select count(student_id) as 'Total Candidates placed', company_name as 'Organization' 
            from placements where company_name in ('Microsoft','Tesla','Adobe','Oracle')
            group by company_name;
        """
        return(db.fetchResults(query))
    
    # Query: To fetch the Male & Female ratio per batch
    def femaleMaleRatio(self):
        query = """SELECT course_batch as 'Batch', SUM(gender = 'Male') AS 'Male', SUM(gender = 'Female') AS 'Female' FROM students GROUP BY course_batch order by course_batch;"""
        return (db.fetchResults(query))
    
    # Query: To fetch the top 5 candidates who are ready and eligible for placement
    def top5Candidates(self):
        query = """
                    select a.name as 'Candidate', round(avg(((b.problems_solved * 0.5 + 
                                                                b.assessments_completed * 0.5 +
                                                                b.mini_projects * 0.6 +
                                                                b.certifications_earned * 0.7 +
                                                                b.latest_project_score * 0.4)/ (0.5+0.5+0.6+0.7+0.4))))  as 'Weighted_Avg_Programming_Score',
                                                                round(avg((c.communication * 0.6 +
                                                                c.teamwork * 0.8 +
                                                                c.presentation * 0.6 +
                                                                c.leadership * 0.75 +
                                                                c.critical_thinking * 0.5 +
                                                                c.interpersonal_skills * 0.8)/(0.6+0.8+0.6+0.75+0.5+0.8))) as 'Weighted_Avg_Softskill_Score'
                    from students as a
                    left join programming b on a.student_id=b.student_id 
                    left join softskills as c on b.student_id = c.student_id
                    group by a.name order by 2 desc LIMIT 5;
            """        
        return (db.fetchResults(query))
    
    # Query: To fetch the distribution of candidates placed across various organizations
    def placedCandidatesOrgDistribution(self):
        query = """
                select count(student_id) as 'Count', company_name as 'Organization'  from placements
                group by company_name;
            """
        return (db.fetchResults(query))
    
    # Query: To fetch the most popular course opted by students
    def mostPopularCourse(self):
        query = """select language as 'Course', count(*) as 'Count' from programming group by language order by count desc;"""
        return (db.fetchResults(query))    
    
    # Query: To fetch average performance of the batch
    def batchWisePerformance(self):
        query = """
                select b.course_batch as 'Batch', AVG(((a.problems_solved + a.assessments_completed +a.mini_projects)/3)) as 'Average Performance'
                from programming as a
                inner join students b on a.student_id=b.student_id
                group by b.course_batch order by b.course_batch;
                """        
        return (db.fetchResults(query)) 
    
    # Query: To fetch the candidates who are skilled in programming but lacking in soft skills
    def skilledProgLackSoftSkills(self):
        query = """
                    select a.name as 'Candidate', round(avg(((b.problems_solved * 0.5 + 
                                                                b.assessments_completed * 0.5 +
                                                                b.mini_projects * 0.6 +
                                                                b.certifications_earned * 0.7 +
                                                                b.latest_project_score * 0.4)/ (0.5+0.5+0.6+0.7+0.4))))  as 'Weighted_Avg_Programming_Score',
                                                                round(avg((c.communication * 0.6 +
                                                                c.teamwork * 0.8 +
                                                                c.presentation * 0.6 +
                                                                c.leadership * 0.75 +
                                                                c.critical_thinking * 0.5 +
                                                                c.interpersonal_skills * 0.8
                                                                )/(0.6+0.8+0.6+0.75+0.5+0.8))) as 'Weighted_Avg_Softskill_Score'
                    from students as a
                    left join programming b on a.student_id=b.student_id 
                    left join softskills as c on b.student_id = c.student_id
                    group by a.name having Weighted_Avg_Softskill_Score < 30 and Weighted_Avg_Programming_Score > 40;               
            """      
        return (db.fetchResults(query))
    

    # Query: To fetch the candidates who are skills in soft skills but lacking in programming
    def skilledSoftSkillsLackInProg(self):
        query = """
                    select a.name as 'Candidate', round(avg(((b.problems_solved * 0.5 + 
                                                                b.assessments_completed * 0.5 +
                                                                b.mini_projects * 0.6 +
                                                                b.certifications_earned * 0.7 +
                                                                b.latest_project_score * 0.4)/ (0.5+0.5+0.6+0.7+0.4))))  as 'Weighted_Avg_Programming_Score',
                                                                round(avg((c.communication * 0.6 +
                                                                c.teamwork * 0.8 +
                                                                c.presentation * 0.6 +
                                                                c.leadership * 0.75 +
                                                                c.critical_thinking * 0.5 +
                                                                c.interpersonal_skills * 0.8
                                                                )/(0.6+0.8+0.6+0.75+0.5+0.8))) as 'Weighted_Avg_Softskill_Score'
                    from students as a
                    left join programming b on a.student_id=b.student_id 
                    left join softskills as c on b.student_id = c.student_id
                    group by a.name having Weighted_Avg_Softskill_Score > 50 and Weighted_Avg_Programming_Score < 80;               
            """    
        return (db.fetchResults(query)) 
    
    # Query: To fetch the relationship between programming & soft skill scores
    def progVsSoftSkillScore(self):
        query = """
                    select a.name as 'Candidate', round(avg(((b.problems_solved * 0.5 + 
                                                                b.assessments_completed * 0.5 +
                                                                b.mini_projects * 0.6 +
                                                                b.certifications_earned * 0.7 +
                                                                b.latest_project_score * 0.4)/ (0.5+0.5+0.6+0.7+0.4))))  as 'ProgrammingSkill',
                                                                round(avg((c.communication * 0.6 +
                                                                c.teamwork * 0.8 +
                                                                c.presentation * 0.6 +
                                                                c.leadership * 0.75 +
                                                                c.critical_thinking * 0.5 +
                                                                c.interpersonal_skills * 0.8
                                                                )/(0.6+0.8+0.6+0.75+0.5+0.8))) as 'SoftSkill'
                    from students as a
                    left join programming b on a.student_id=b.student_id 
                    left join softskills as c on b.student_id = c.student_id
                    group by a.name;
                """  
        return (db.fetchResults(query)) 
    
    # Query: To fetch the relationship between certifications earned & avg salary
    def certVsAvgSalary(self):
        query = """
                    select a.student_id, sum(a.certifications_earned) as 'Total certifications earned', 
                        round(avg(b.placement_package)) as 'Avg Salary'
                    from programming as a 
                    left join placements as b on a.student_id=b.student_id
                    group by a.student_id;
                """
        return (db.fetchResults(query)) 