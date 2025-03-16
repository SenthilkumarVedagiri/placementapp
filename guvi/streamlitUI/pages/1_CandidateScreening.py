import streamlit as st
import pandas as pd
from utils.db_connection import DatabaseManager

############################################# Candidate Screening page ##########################################
#Candidate Screening UI interface which displays various parameters to filter the candidates accordingly.  
#It has an interactive UI form with various input elements which helps the placement team to screen the candidates
#easy and interactive manner. 
##################################################################################################################

# Set the page layout to wide
st.set_page_config(layout="wide")  

# Split the columns in to 1:3 ratio
col1, col2 = st.columns([1, 3])
with col1:    
    st.image("assets\guvi.jpeg", width=250) 
with col2:
    st.markdown(
            """<h2 style="text-align: center; color: #4CAF50;">
                Candidate Screening section
            </h2>
            """,
            unsafe_allow_html=True
        )
st.write("<h3 style='font-size:20px; color:green;'>Fill the form with the required criteria and submit to screen the candidates:</h3>", unsafe_allow_html=True)


# Split the page in the ratio 20%, 60% & 20% 
col1, col2, col3 = st.columns([20, 60, 20])  

st.markdown("""
    <style>
        .custom-form {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            border-radius: 8px !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)


# Centered column
with col2:  
    with st.form(key="custom_form"):            
        selected_gender = st.radio("Candidate's Gender", ["Male", "Female", "Both"])
        
        enrollmentYearOptions = ["NA"]+list(range(1995,2025))
        selected_enrollmentYear = st.selectbox("Select the enrollment year: (select NA if not applicable)", enrollmentYearOptions)

        graduationYearOptions = ["NA"]+list(range(1995,2025))        
        selected_graduationYear = st.selectbox("Select the graduated year: (select NA if not applicable)", graduationYearOptions)

        courseBatchOptions = ['NA','AE-WBD01','AE-WBD02','AE-WBD03','AE-WBD04','AE-WBD05','AE-WBD06']
        selected_courseBatch = st.selectbox("Select the batch: (select NA if not applicable)", courseBatchOptions)

        communication = st.slider("Min communication score required:", min_value=0, max_value=100, value=40)

        teamwork = st.slider("Min team work score required:", min_value=0, max_value=100, value=40)

        presentation = st.slider("Min presentation skill score required:", min_value=0, max_value=100, value=50)

        leadership = st.slider("Min leadership skill score required:", min_value=0, max_value=100, value=30)

        criticalThinking = st.slider("Min critical thinking score required:", min_value=0, max_value=100, value=40)

        interpersonalSkill = st.slider("Min interpersonal skill score required:", min_value=0, max_value=100, value=30)

        problemsSolved = st.slider("Min no of Codekata problems solved:", min_value=0, max_value=300, value=30)

        assessmentsCompleted = st.slider("Min no of assessments completed:", min_value=0, max_value=10, value=6)
        
        submit_button = st.form_submit_button("Submit")

        query = """
                SELECT 
                    a.student_id AS ID,
                    a.name AS Name, 
                    a.age AS Age, 
                    a.gender AS Gender, 
                    a.enrollment_year AS EnrollmentYear, 
                    a.graduation_year, 
                    a.course_batch, 
                    b.communication, 
                    b.teamwork, 
                    c.language, 
                    c.problems_solved, 
                    c.certifications_earned
                FROM students AS a 
                INNER JOIN softskills AS b ON a.student_id = b.student_id
                INNER JOIN programming AS c ON b.student_id = c.student_id 
                """
        params = []

        if selected_gender != 'Both':
            query += " and a.gender = %s"
            params.append(selected_gender)             
        if selected_enrollmentYear != 'NA':            
            query += " and a.enrollment_year = %s"
            params.append(selected_enrollmentYear)
        if selected_graduationYear != 'NA':
            query += " and a.graduation_year = %s"            
            params.append(selected_graduationYear)
        if selected_courseBatch != 'NA':
            query += " and a.course_batch = %s"            
            params.append(selected_courseBatch)
        
        query += " and b.communication >= %s"
        params.append(communication)

        query += " and b.teamwork >= %s"
        params.append(teamwork)        
        
        query += " and b.presentation >= %s"
        params.append(presentation)        

        query += " and b.leadership >= %s"
        params.append(leadership)        

        query += " and b.critical_thinking >= %s"
        params.append(criticalThinking)  

        query += " and b.interpersonal_skills >= %s"
        params.append(interpersonalSkill)       

        query += " and c.problems_solved >= %s"
        params.append(problemsSolved)            

        query += " and c.assessments_completed >= %s"
        params.append(assessmentsCompleted)           

        query += " ORDER BY ID"
        print("Here is the query",query)


# Split the page in the ratio 10%, 80% & 10% 
col1, col2, col3 = st.columns([5, 90, 5])  

with col2:
     if submit_button:        
        db = DatabaseManager()        
        results = db.executeQuery(query,params)
        df = pd.DataFrame(results, columns=['ID','Name','Age','Gender','Enrollment Year','Graduation Year','Batch','Communication','Teamwork','Language','Problems Solved','No of Certifications'])    
        st.dataframe(df)