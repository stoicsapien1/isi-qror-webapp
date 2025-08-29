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
    "EXAMINATION PAPERS","RMMR TABLE"])
    
    if selected_material=="EXAMINATION PAPERS":
        
        st.link_button("DOWNLOAD MID SEM PAPERS[NEW]📚",url="https://drive.google.com/file/d/1vuO_BLW8CaQOG0WP1QD6yXArQ08g9IKF/view?usp=sharing")
        st.link_button("DOWNLOAD END SEM PAPERS[NEW]🤓",url="https://drive.google.com/file/d/1GYFlYqzq3_i_-8ip6HQz20TVctEdXx_7/view?usp=sharing")
    elif selected_material=="SIX SIGMA":
        st.link_button("DOWNLOAD SIX SIGMA MATERIAL😎",url="https://drive.google.com/drive/folders/1TYK0ZDAxQbcemu9KB6owts6AEY9L2YnF?usp=sharing")
    

    elif selected_material=="BUSINESS ANALYTICS":
        st.link_button("DOWNLOAD BUSINESS ANALYTICS MATERIAL💻",url ="")
    
    elif selected_material=="ADVANCED MULTIVARIATE ANALYSIS":
        st.link_button("DOWNLOAD AMA BOOK📒",url="https://drive.google.com/file/d/10_hHk0NmSVAJUWvNVWduwapujwNNRxxG/view?usp=sharing")
        st.link_button("DOWNLOAD AMA COMPLETE NOTES⚡",url= "https://drive.google.com/file/d/1JTWZFjCDjI7l60N1QrYYZlAAPOVTl7c3/view?usp=sharing")
    
    elif selected_material=="RELIABILITY - II":
        st.link_button("DOWNLOAD RELIABILITY MATERIAL📊",url="")

    elif selected_material=="INDUSTRIAL EXPERIMENTATION":
        st.link_button("DOWNLOAD IE MATERIAL💻",url="")
    
    elif selected_material=="OPERATIONS RESEARCH":
        st.link_button("DOWNLOAD OR MATERIAL📉",url= "")
    

    elif selected_material=="RMMR TABLE":
        st.link_button("DOWNLOAD RMMR TABLE📥",url="https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link")
    

    
if __name__ == "__main__":
    main()
