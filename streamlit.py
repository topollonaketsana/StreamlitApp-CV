import streamlit as st
import pandas as pd
#import plotly.express as px
import os



import streamlit as st

# Set page config
st.set_page_config(page_title="Topollo Naketsana - CV", page_icon="📄", layout="wide")

# Title and Header
st.title("Topollo Naketsana")
st.subheader("Data Scientist | Machine Learning Analyst | Researcher")

# Contact Information
st.markdown('<h3 style="color: #87CEEB;">Contact Information</h3>', unsafe_allow_html=True)
#st.markdown("### Contact Information")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Email:** topollonaketsana60@gamil.com")  
with col2:
    st.write("**Phone:** 078 280 6610")  
with col3:
    st.write("**Location:** Cape town, South Africa")  

# Professional Summary
st.markdown('<h3 style="color: #87CEEB;">Professional Summary</h3>', unsafe_allow_html=True)
#st.markdown("### Professional Summary")
st.write("""
Passionate Astrophysicist with expertise in Mathematical techniques for machine learning, research-driven decision skills and data analysis. Experienced in developing predictive models, conducting research, and collaborating on interdisciplinary projects. Committed to advancing scientific knowledge through data-driven insights.
         I enjoy exploring the cosmos through data and simulation.
""")

# Education
st.markdown('<h3 style="color: #87CEEB;">Education</h3>', unsafe_allow_html=True)
#st.markdown("### Education")
st.write("""
- **Master of Science in Astroparticle physics**  
  Stellenbosch University, (2026)  
  Thesis: Analysis of the Cosmic microwave background (CMB) and studying the parity violation in the CMB

- **Bachelor of Science Hounours in Astrophysics**  
  University of the Western Cape, (2025) 

- **Bachelor of Science in Physics**
  University of the Western Cape (2022-2024)
  
""")

# Professional Experience
st.markdown('<h3 style="color: #87CEEB;">Professional experience</h3>', unsafe_allow_html=True)
#st.markdown("### Professional Experience")
st.write("""
- **Theoretical Physics intern**  
  NiThecs, Nelson Mandel University (2025)  
  - Researched on Compact stellar objects.  
  - Studied and modelled the properties of Binary Neutron Stars.  
  - 

- **Student Assistant in science faculty**  
  University of the western cape, (2024)  
  - Assisted with upfront application process. 

- **SME - Subject Matter Expert, NASA hackathon**
  - Apointed to be a subject matter expert during the NASA space apps challenge** 
  - Developed skills to judge the final hackathon projecs for local participants

""")

# Skills
st.markdown('<h3 style="color: #87CEEB;">Skills</h3>', unsafe_allow_html=True)
#st.markdown("### Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    - Python, Octave, SQL, Bash, Latex
    - Machine Learning 
    - Data Visualization
    - Modelling and Simulations
    """)
with col2:
    st.write("""
    - Data analysis (Big data - Astronomical data)
    - Quantum Computing (QWorld)
    - Research skills
    """)

# Certifications and Achievements
st.markdown('<h3 style="color: #87CEEB;">Certification and Achievements</h3>', unsafe_allow_html=True)
#st.markdown("### Certifications")
st.write("""
- Certified Data Scientist (IDIA)
- Certified Quantum computing scientist (QWorld)
- Participated in the IAU GA (2024)
- Volunteered to engage in science activities - outreach to some of Cape Town schools
""")

# Projects
st.markdown("### Projects")
st.write("""
- **Project 1: Exoplanet Classification**  
  Description: Developed a predictive machine learning model to classify exoplanets.  
  Tools: Python, TensorFlow, Pandas, scikit learn.
- Used data from TESS/NASA

- **Project 2: Galaxy Classification (CNN)**  
  Description: Analyzed large galaxy datasets from HST - Hubble Space telescope.  
  Tools: CNN, LOF.
  
- **Used one of the ESA data clouds - ESA dataLabs**
""")

# Languages
st.markdown('<h3 style="color: #87CEEB;">Languages</h3>', unsafe_allow_html=True)
#st.markdown("### Languages")
st.write("""
- English: Fluent
- Other Language: Proficient
""")

# Publications
st.markdown('<h3 style="color: #87CEEB;">Publications</h3>', unsafe_allow_html=True)
#st.markdown("### Publications")
st.write("""
- **Naketsana, T., Santos, M., Karin F. (Year). Analysis of HI 21 cm signal, foreground cleaning for the HI 21 cm intensity mapping.**  
  DOI: 10.5281/zenodo.17649438


""")


# Interests
st.markdown('<h3 style="color: #87CEEB;">Interests</h3>', unsafe_allow_html=True)
#st.markdown("### Interests")
st.write("""
- Research in AI and Machine Learning
- Open-source contributions
- Scientific literature and conferences
""")



# set an image
#st


# Footer
st.markdown("---")
st.write("© 2026 Topollo Naketsana. Built with Streamlit.")