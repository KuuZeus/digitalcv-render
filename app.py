from pathlib import Path
import streamlit as st
from PIL import Image


PAGE_TITLE = 'Digital CV | Ekins Kuuzie'
PAGE_ICON = ':wave'
NAME= 'Ekins Kuuzie'

DESCRIPTION = """ A dynamic medical doctor and data scientist, dedicated to harnessing the power of data to drive impactful solutions in healthcare"""

EMAIL = 'kuuzieekins@gmail.com'

SOCIAL_MEDIA= {
    'LinkedIn': 'http://www.linkedin.com',
    'Twitter' : 'http://twitter.com',
    'Github' : 'http://github.com'
}

PROJECTS= {
'🏆 Data Exploration with SQL': 'https://github.com/KuuZeus/Kuuzieanalytics/blob/main/covidSQL.sql',
'📊 Patient Appointment Data Analysis with Python': 'https://github.com/KuuZeus/Kuuzieanalytics/blob/main/Investigate_a_Dataset.ipynb',
'🫁 Analysis of Air Pollution Data':'https://github.com/KuuZeus/Kuuzieanalytics/blob/main/air_pollution.ipynb',
'😷 Covid-19 Data Visualization with Tableau':'https://public.tableau.com/app/profile/ekins.kuuzie/viz/COVIDdataDashboard_16630125411020/VIZ?publish=yes',
'💉 Measles Vaccination Data Analysis': 'https://github.com/KuuZeus/Kuuzieanalytics/blob/main/measle_vaccination.ipynb',
'🦀 Global Cancer Data Visualization with Power BI': 'https://www.novypro.com/project/closing-the-care-gap',
'🫀 Hypertension Data Visualization with Power BI': 'https://www.novypro.com/project/blood-pressure-control-among-hypertensives'
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title('Hello Welcome to my digital CV')


### Modify the css file

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

# css_file = r'C:\Users\Zeus\PycharmProjects\datascienceapp\styles\main.css'
# resume_file = r'C:\Users\Zeus\PycharmProjects\datascienceapp\assets\resume.pdf'
# profile_pic= r'C:\Users\Zeus\PycharmProjects\datascienceapp\assets\profile_pic.png'


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte= pdf_file.read()
profil_pic= Image.open(profile_pic)


col1, col2 = st.columns(2, gap= 'small')

with col1:
    st.image(profil_pic, width=300)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label='📄 Download Resume',
        data= PDFbyte,
        file_name= resume_file.name,
        key= 'Download-pdf'

    )
    st.write('✉️' ,EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('#')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years experience working as a medical doctor
- ✔️ 2 Years expereince in extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('#')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: PowerBI, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees, Naive Bayes
"""
)


# --- WORK HISTORY ---
st.write('#')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("📈", "**Medical Data Analyst | minoHealth AI**")
st.write("06/2023 - Present")
st.write(
    """
- ► Conducted data curation and annotations on medical datasets.
- ► Utilized advanced analytical techniques to extract valuable insights from complex medical datasets.
- ► Trained, evaluate and deployed machine learning models.
- ► Coordinated and collaborated with interdisciplinary teams to ensure smooth project execution and timely completion.
- ► Researched and analyzed medical applications of AI to identify potential areas for implementation and improvement.
"""
)

# --- JOB 2
st.write('\n')
st.write("🩺", "**Medical Officer (SHO) | St Dominic Hospital**")
st.write("06/2022 - 06/2023")
st.write(
    """
- ► Clerked patient to gather comprehensive medical histories, perform physical examinations, and document relevant findings.
- ► Utilized clinical knowledge and diagnostic skills to accurately assess and diagnose medical conditions.
- ► Documented patient care activities, including diagnoses, treatments, and surgical interventions, accurately and comprehensively.
- ► Contributed to interdisciplinary rounds and discussions to facilitate collaborative decision-making and patient care coordination.
"""
)

# --- JOB 3
st.write('\n')
st.write("📈", "**Data Analyst Intern | Brainnest**")
st.write("03/2022 - 04/2022")
st.write(
    """
- ► Utilized SPSS software to conduct statistical analysis for scientific research projects.
- ► Applied quantitative research methodologies to gather and analyze data effectively.
- ► Developed proficiency in performing descriptive statistics to summarize data distributions and key measures.
- ► Conducted inferential statistics to draw meaningful conclusions and make evidence-based recommendations.
- ► Employed data visualization techniques to present research findings in a clear and concise manner.
"""
)
## ----JOB 4
st.write('\n')
st.write("🩺", "**Medical Officer (HO) | Korle Bu Teaching Hospital**")
st.write("05/2021 - 06/2022")
st.write(
    """
- ► Clerked patient to gather comprehensive medical histories, perform physical examinations, and document relevant findings.
- ► Utilized clinical knowledge and diagnostic skills to accurately assess and diagnose medical conditions.
- ► Documented patient care activities, including diagnoses, treatments, and surgical interventions, accurately and comprehensively.
- ► Contributed to interdisciplinary rounds and discussions to facilitate collaborative decision-making and patient care coordination.
"""
)


# --- Projects & Accomplishments ---
st.write('#')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
