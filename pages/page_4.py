import streamlit as st

def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Data Science Study Material📚")
    st.image("https://media.licdn.com/dms/image/C4D12AQGD_su1k14bYA/article-cover_image-shrink_720_1280/0/1583217310732?e=2147483647&v=beta&t=an15cumXvL1rLYucw3WqOUkf-27-B-l52jkmpEfPaKw")
    st.sidebar.success("SELECT THE PAGE ABOVE⚡")
    st.sidebar.markdown('''
    ---
    **Contact Information:**

    For any queries, please contact:
    - Admin: Belal Ahmed Siddiqui
    - Email: qr2304@isical.ac.in
    - LinkedIn: https://bit.ly/belallin
    ''')
    selected_material = st.selectbox("Select the Options", ["YT PLAYLIST","PROJECT","DRIVE STUDY MATERIAL"])
    if selected_material=="DRIVE STUDY MATERIAL":
            st.link_button("DOWNLOAD DATA SCIENCE STUDY MATERIAL[COMPILED BY SOUBHIK BHATTACHARYA]",url="https://drive.google.com/drive/folders/1tMlOwyXzpiiSWmvlP-X7HSrc4dxBi0YJ?usp=sharing")











if __name__ == "__main__":
    main()