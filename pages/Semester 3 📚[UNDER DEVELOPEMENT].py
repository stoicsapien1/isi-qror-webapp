import streamlit as st
def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Third Semester Study Material📚")
    st.sidebar.success("SELECT THE PAGE ABOVE")
    st.write("***PLEASE SELECT THE SUBJECT*** 🤓")
    st.sidebar.markdown('''
    ---
    **Contact Information:**

    For any queries, please contact:
    - Admin: Belal Ahmed Siddiqui
   
    
    ''')

if __name__ == "__main__":
    main()
