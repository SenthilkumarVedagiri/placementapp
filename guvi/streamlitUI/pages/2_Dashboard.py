import streamlit as st
import matplotlib.pyplot as plt
from utils.query import Query
import plotly.express as px


############################################# Dashboard page ##########################################
# Interactive dashboard page which provides various key insights 
# on the students, placements and their skills  
########################################################################################################

# Create a query instance to access the query repository 
query = Query()

# Set page layout as wide
st.set_page_config(layout="wide")

# Split the layout into two columns with the ratio of 1:3
col1, col2 = st.columns([1, 3])
with col1:    
    st.image("assets\guvi.jpeg", width=250) 
with col2:
    st.markdown(
            """<h2 style="text-align: center; color: #4CAF50;">
                    Dashboard - Key insights
               </h2>
            """, unsafe_allow_html=True
        )

# Split the layout into columns with the ratio 50:50
col1, col2 = st.columns([50,50])

with col1:
    #Col 1, 1st widget: Candidates places in top MNC's
    fig = px.bar(query.candidatesPlacedinMNC(),
                     x='Organization', 
                     y='Total Candidates placed', 
                     title='Candidates placed in leading international MNC\'s', 
                     color='Organization')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black'),
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=14,family="Arial")
    )    
    st.plotly_chart(fig)

    ##Col 1, 2nd widget: Male Vs Female ration per batch
    fig = px.bar(query.femaleMaleRatio(), 
                 x='Batch', 
                 y=["Male","Female"], 
                 barmode='stack', 
                 title='Distribution of male / female candidates per batch')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black'),
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title="Male / Female ratio",
    )      
    st.plotly_chart(fig)

    #Col3, 3rd widget: Top 5 candidates ready for placement
    fig = px.bar(query.top5Candidates(), 
                 x='Candidate', 
                 y='Weighted_Avg_Programming_Score', 
                 text='Candidate', 
                 title='Top 5 Candidates ready for placements')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black'),
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=12,family="Arial")
    )  
    fig.update_traces(marker=dict(color='lightblue'))
    st.plotly_chart(fig)

with col2:
    #Col2, 1st Widget: Distribution of candidates placed in different organizations
    explode = [0.0, 0, 0.2, 0]  # Explode effect
    fig = px.pie(query.placedCandidatesOrgDistribution(),   #Create Pie Chart
                 names='Organization', 
                 values='Count', 
                 title='Distribution of candidates placed among the organizations',
                 color_discrete_sequence=px.colors.sequential.Mint, hole=0)
    fig.update_traces(pull=explode)
    fig.update_layout(
        title_font=dict(size = 18, color='black', family='Arial'),
        width=450,height=450
    )  
    st.plotly_chart(fig)

    #Col2, 2nd Widget: Distribution of most popular course among the candidates
    fig = px.pie(query.mostPopularCourse(), 
                 names='Course', 
                 values='Count', 
                 title='Most popular tech course among the candidates')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black'),
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=12,family="Arial")
    )  
    st.plotly_chart(fig)

    #Col2, 3rd Widget: Candidates performance batch wise
    fig = px.bar(query.batchWisePerformance(), 
                    x='Batch', 
                    y='Average Performance', 
                    title='Batch performance based on the programming skills', 
                    color='Batch')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black'),
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=14,family="Arial")
    )  
    st.plotly_chart(fig)

# Setting the wide layout by merging the columns
merged_col = st.container()

with merged_col:
    #1st Widget: Candidates skilled in programming but lacking in soft skills
    fig = px.bar(query.skilledProgLackSoftSkills(), 
                 x='Candidate', 
                 y=['Weighted_Avg_Programming_Score','Weighted_Avg_Softskill_Score'], 
                 barmode='group',
                 title='Candidates skilled in Programming but lacking in Softskills')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black',tickangle=45),
        yaxis_title='Average score',
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=14,family="Arial")
    )  
    st.plotly_chart(fig)    

    #2nd widget: Candidates skilled in soft skills lacks in programming
    fig = px.bar(query.skilledSoftSkillsLackInProg(), x='Candidate', 
                 y=['Weighted_Avg_Programming_Score','Weighted_Avg_Softskill_Score'], 
                 barmode='group',
                 title='Candidates with reasonable Soft skills but lacking in Programming skills')
    fig.update_layout(
        xaxis=dict(showline = True, linewidth=1, linecolor='black',tickangle=45),
        yaxis_title='Average score',
        yaxis=dict(showline = True, linewidth=1, linecolor='black'), 
        title_font=dict(size = 18, color='black', family='Arial'),
        xaxis_title_font=dict(size=14,family="Arial"),
        yaxis_title_font=dict(size=14,family="Arial")
    ) 
    st.plotly_chart(fig)        

    # 3rd Widget: Relationship between Programming skills Vs Soft skills 
    df = query.progVsSoftSkillScore()
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.scatter(df["ProgrammingSkill"], df["SoftSkill"], color="blue", alpha=0.7)
    ax.set_xlabel("Avg Programming Score",fontsize=12,color='purple')
    ax.set_ylabel("Avg Soft Skills Score",fontsize=12,color='purple')
    ax.set_title("Programming vs Soft Skills Score",fontsize=12,fontweight='bold',color='darkgreen')
    ax.tick_params(axis='both', labelsize=8,colors='darkgreen')
    st.pyplot(fig)

    #4th Widget: Relationship between Certifications earned Vs Avg Salary
    df = query.certVsAvgSalary()
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.scatter(df["Total certifications earned"], df["Avg Salary"], color="blue", alpha=0.7)
    ax.set_xlabel("Certifications earned",fontsize=12,color='purple')
    ax.set_ylabel("Average Salary",fontsize=12,color='purple')
    ax.set_title("Certifications vs Avg Salary Score",fontweight='bold',fontsize=12,color='darkgreen')
    ax.tick_params(axis='both', labelsize=8,colors='darkgreen')
    st.pyplot(fig)