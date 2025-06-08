# MADE BY BELAL AHMED SIDDIQUI
import streamlit as st

def main():
    
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Welcome to the M.Tech QROR Study Material Hub!📚💻")
    st.image("https://i.postimg.cc/Xq92QSJF/SQC-AND-OR-UNIT.png")
    st.markdown('***"❤️Arise, awake, and stop not until the goal is reached.❤️"***')
    # Add quote attribution with styling
    st.markdown("*- Swami Vivekanand*", help="Quote by Swami Vivekanand")
    
    # Program description with better formatting
    st.markdown("""
    ### About the Program
    The Master of Technology (M.Tech) in QROR is a full-time program offered at the 
    Indian Statistical Institute (ISI) in Kolkata. This specialized program aims to produce 
    experts in:
    * Data Science/Analytics
    * Artificial Intelligence
    * Survival Analysis
    * Machine Learning
    * Statistical Quality Control
    * Quantitative Finance
    """)
    
    # Syllabus button with custom styling
    st.link_button(
        "View Syllabus 📒", 
        url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing",
    )
    
    # Sidebar navigation
    st.sidebar.success("SELECT THE PAGE ABOVE")
    
    # Contact information in sidebar with improved formatting
    st.sidebar.markdown("""
    ---
    ### Contact Information
    For any queries, please contact:
    * **Admin:** Belal Ahmed Siddiqui
    """)
    
    # Copyright notice with better visibility
    st.warning("""
    ⚠️ **Copyright Notice:**
    All materials, including PDFs, Books, and Notes, belong to their respective owners.
    They are shared here for educational purposes only; no copyright infringement is intended.
    """)
    
    st.write("Made with ❤️ by Belal Ahmed Siddiqui")
if __name__ == "__main__":
    main()
