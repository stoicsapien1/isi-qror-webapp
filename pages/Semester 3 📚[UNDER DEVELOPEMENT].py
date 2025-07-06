import streamlit as st
def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Third Semester Study Material📚")
    st.sidebar.success("SELECT THE PAGE ABOVE")
    st.write("***PLEASE SELECT THE SUBJECT*** 🤓")

   
    
  
    selected_material = st.selectbox("Select the Subjects",[
    "OPERATIONS RESEARCH",
    "INDUSTRIAL EXPERIMENTATION",
    "RELIABILITY - II",
    "ADVANCED MULTIVARIATE ANALYSIS",
    "BUSINESS ANALYTICS",
    "SIX SIGMA",
    "EXAMINATION PAPERS"])
    


if __name__ == "__main__":
    main()
