# MADE BY BELAL AHMED SIDDIQUI
import streamlit as st
from pages import page_2, page_3

def main():
    
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Welcome to the M.Tech QROR Study Material Hub!⚡⚡")
    st.image("https://beeimg.com/images/s53843333701.png")
    st.markdown('***"❤️Arise, awake, and stop not until the goal is reached.❤️"***')
    st.write("-Swami Vivekanand")
    st.write('''The Master of Technology (M.Tech) in Quality, Reliability, and Operations Research (QROR) is a full-time program offered at the Indian Statistical Institute (ISI) in Kolkata. This specialized program aims to produce experts in Quality Management, emphasizing Statistical Quality Control, Reliability, Operations Research, Computer Software, and Management Systems.''')
    st.link_button("Link to syllabus", url="https://www.isical.ac.in/~deanweb/qror.html")
    st.write("This webapp is useful for the 1st year M.Tech QROR Student. 🚀📚")
    st.sidebar.success("SELECT THE PAGE ABOVE❤️")
    # Footer
    
    st.write('***Page 2 contains Semester 1 Study Material***')
    st.write('''***Page 3 contains Semester 2 Study Material***''')
    st.write('***Page 4 contains Data Science Study Material***')
    st.sidebar.markdown('''
    ---
    **Contact Information:**

    For any queries, please contact:
    - Admin: Belal Ahmed Siddiqui
    - Email: belalahmedsiddiqui8@gmail.com
    - LinkedIn: https://bit.ly/belallin
    
    ''')
    
if __name__ == "__main__":
    main()
