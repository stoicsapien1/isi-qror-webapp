# MADE BY BELAL AHMED SIDDIQUI
import streamlit as st

def main():
    
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Welcome to the M.Tech QROR Study Material Hub!📚💻")
    st.image("https://i.postimg.cc/Xq92QSJF/SQC-AND-OR-UNIT.png")
    st.markdown('***"❤️Arise, awake, and stop not until the goal is reached.❤️"***')
    st.write("-Swami Vivekanand")
    st.write('''The Master of Technology (M.Tech) in Quality, Reliability, and Operations Research (QROR) is a full-time program offered at the Indian Statistical Institute (ISI) in Kolkata. This specialized program aims to produce experts in Quality Management, emphasizing Statistical Quality Control, Reliability, Operations Research, Computer Software, and Management Systems.''')
    st.link_button("View Syllabus📒", url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing")
    st.sidebar.success("SELECT THE PAGE ABOVE")
    # Footer
    
    st.sidebar.markdown('''
    ---
    **Contact Information:**

    For any queries, please contact:
    - Admin: Belal Ahmed Siddiqui
    
    
    ''')
    st.write('''❗All materials, including PDFs,Books,and Notes, belong to their respective owners.
             They are shared here for educational purposes only; no copyright infringement is intended.❗''')
    
    
if __name__ == "__main__":
    main()
