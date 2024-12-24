import streamlit as st
def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Resume Building💻")
    st.sidebar.success("SELECT THE PAGE ABOVE ")
    st.sidebar.markdown('''
    ---
    **Contact Information:**

    For any queries, please contact:
    - Admin: Belal Ahmed Siddiqui
   
    
    ''')

    st.subheader("HackerResume Builder") 
    st.write('''HackerResume is a good site to make resume in a very structured format.
    Here you can add heading in your resume based on various sections available.
    Creating resume is very easy compared to MS Word.''')
    st.write("NOTE: Better to make resume here and download the latex code and upload the latex code in Overleaf to get the PDF.")
    st.write("Later add the ISI Kolkata LOGO using some PDF Editor Tool.")
    st.link_button("VISIT HACKERRESUME WEBSITE",url="https://www.hackerrank.com/resume")
    st.subheader("Overleaf Template") 
    st.write('''This template is quite good,just edit this template using overleaf,it has all the required section
             that constitutes a GOOD Resume''')
    st.link_button("DOWNLOAD TEMPLATE",url="https://drive.google.com/file/d/1bhrEj7RR-omwHE-T0c_yfA0_DsqERn2h/view?usp=sharing")

    st.write("How to Use the Template") 
    st.write("""
1. **Download the Template**: Use the provided link to download the resume template.

2. **Edit in Overleaf**: Open the template in Overleaf and personalize it with your details.

3. **Export as PDF**: After finalizing your edits, export the resume as a PDF file.
""")



if __name__ == "__main__":
    main()
