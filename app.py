from pathlib import Path

import streamlit as st
from PIL import Image

pip install streamlit

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Noman Ali"
PAGE_ICON = ":wave:"
NAME = "Noman Ali"
DESCRIPTION = """
I’m a data analyst and machine learning engineer focused on extracting insights and
building predictive models to drive decision-making.
"""
EMAIL = "noman.contact.info@gmail.com"
SOCIAL_MEDIA = {
    "💻 LinkedIn": "https://www.linkedin.com/in/noman-ali-chaudhary-baaa63302/",
    "📊 GitHub": "https://github.com/Nomanch0",
    "📈 Kaggle": "https://www.kaggle.com/nomanali0",
    "🌐 Facebook":"https://www.facebook.com/profile.php?id=100079595214477",
    "📞 Whatsapp": "https://api.whatsapp.com/send?phone=923048695679&text=Hi!%20Hope%20you%20are%20doing%20well.%20how%20may%20I%20can%20help%20you%20",
    
}


PROJECTS = {
    "🗂️ Airline Sentiment Anlaysis  ": "https://github.com/Nomanch0/Airline-Sentiment-MARJANTA_DATA",
    "📈 Stock-Market-PowerBI-Dashboard": "https://github.com/Nomanch0/Stock-Market-PowerBI-Dashboard",
    "🌐 Azghan Surgical Website": "https://www.azghan.com/",
    "🏆 Optimized COVID-19 Detection": "https://github.com/Nomanch0/Optimized-COVID-19-Detection-Transfer-Learning-Using-RGB-CT-Scan-Images/blob/main/Paper.pdf",
    "🏆 Salary Prediction System": "https://github.com/Nomanch0",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✅ 1 year of experience in deriving actionable insights from data.
- ✅ Proficient in Python, Excel, HTML, and PHP for data analysis and web development.
- ✅ Strong understanding of statistical principles and machine learning applications.
- ✅ Experienced in creating visualizations using Power BI and R.
- ✅ Collaborative team player with a proactive approach to tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy), R, SQL, VBA, Java
- 📊 Data Visulization: Power BI, Excel, Plotly, Matplotlib, ggplot2
- 📚 Machine Learning: Logistic reg, linear reg, decision trees, SVM, RF, KNN, clustering
- 📈 Deep Learning: Neural networks
- 🗄️ Database: MongoDB, MySQL
- 🔍 ML & DL: Experienced in building and deploying predictive models.
- 🌐 Web Dev: Frontend and backend development
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Qualification")
st.markdown("---")

st.write("👨🏻‍🎓", "**Bachelor of Science in Data Science**")
st.write("*02/2021 - Present*")
st.write("""
**Gift University**, *[Gujranwala, Pakistan]*
""")

st.write("📚", "**Introduction to Data Science in Python**")
st.write("*September 23, 2023*")
st.write("""
**Online**, *[University of Michigan]*
""")

st.write("📚", "**Python for Data Science, AI & Development**")
st.write("*November 24, 2023*")
st.write("""
**Online**, *[IBM]*
""")


st.write("👨🏻‍🎓", "**FSC in Pre-Engineering**")
st.write("*02/2015 - 01/2017*")
st.write("""
**Punjab College**, *[Gujranwala, Pakistan]*
""")



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Work History")
st.write("---")

st.markdown("<h2 style='color:#4B0082;'>👨🏻‍💻 Machine Learning Engineer</h2>", unsafe_allow_html=True)
st.markdown("<ul style='list-style-type:circle;'>"
            "<li><strong>Company:</strong> Softa Solutions</li>"
            "<li><strong>Duration:</strong> February 2023 - Present (1 yr 9 mos)</li>"
            "<li><strong>Type:</strong> Part-time</li>"
            "<li><strong>Location:</strong> On-site, Pakistan</li>"
            "</ul>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#4B0082;'>👨🏻‍💻 Data Analyst</h2>", unsafe_allow_html=True)
st.markdown("<ul style='list-style-type:circle;'>"
            "<li><strong>Company:</strong> Fiverr</li>"
            "<li><strong>Duration:</strong> March 2024 - Present (8 mos)</li>"
            "<li><strong>Type:</strong> Part-time</li>"
            "<li><strong>Location:</strong> Remote</li>"
            "</ul>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#4B0082;'>🎨 Canva Expert</h2>", unsafe_allow_html=True)
st.markdown("<ul style='list-style-type:circle;'>"
            "<li><strong>Platform:</strong> Fiverr</li>"
            "<li><strong>Duration:</strong> July 2023 - Present</li>"
            "<li><strong>Type:</strong> Part-time</li>"
            "<li><strong>Location:</strong> Remote</li>"
            "</ul>", unsafe_allow_html=True)

st.markdown("<h2 style='color:#4B0082;'>⚽ ARE Sports</h2>", unsafe_allow_html=True)
st.markdown("<ul style='list-style-type:circle;'>"
            "<li><strong>Role:</strong> Inventory Manager</li>"
            "<li><strong>Duration:</strong> 2018 - 2020</li>"
            "<li><strong>Type:</strong> Full-time</li>"
            "<li><strong>Location:</strong> Sialkot, Pakistan</li>"
            "</ul>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)  # Adds a horizontal line



st.write('\n')
st.subheader("Projects")
st.markdown("---")



for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
