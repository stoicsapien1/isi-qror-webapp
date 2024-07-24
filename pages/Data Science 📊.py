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
    - Email: belalahmedsiddiqui8@gmail.com
    - LinkedIn: https://bit.ly/belallin
    - Add Your Study Material: https://forms.gle/KG1RHiWeJDgrsJrx6
    ''')
    selected_material = st.selectbox("Select the Options", ["YT PLAYLIST","PROJECT","DRIVE STUDY MATERIAL"])
    if selected_material=="DRIVE STUDY MATERIAL":
            st.link_button("DOWNLOAD DATA SCIENCE STUDY MATERIAL[COMPILED BY SOUBHIK BHATTACHARYA]⚡⚡",url="https://drive.google.com/drive/folders/1tMlOwyXzpiiSWmvlP-X7HSrc4dxBi0YJ?usp=sharing")
            st.write("THIS DRIVE FOLDER HAVE ML BOOKS📚")
    elif selected_material=="YT PLAYLIST":

        data=st.selectbox("Select the Topic💹",["Python","ML"])
        if data=="ML":
            st.link_button("ML CAMPUSX[Code+ Concepts]",url="https://www.youtube.com/watch?v=ZftI2fEz0Fw&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH")
            st.link_button("ML STATSQUEST[Concepts]",url="https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF")
        elif data=="Python":
            st.link_button("YT Python Playlist",url="https://www.youtube.com/playlist?list=PLDSuOcTPwmj_IRd6hei9fVNI_QGa5LRCN")
            st.link_button("Python Practice[HACKERRANK]",url="https://www.hackerrank.com/domains/python")
            st.link_button("Python Question[PDF]",url="https://docs.google.com/document/d/1CuKacG3lnnt5B-7kB9p1DiJ2PLFW8TQWn9JG1lTYRJs/edit#heading=h.ghy5ky51yxzv")
    elif selected_material=="PROJECT":
        st.link_button("BASIC ML PROJECT",url="https://www.youtube.com/watch?v=fiz1ORTBGpY&list=PLfFghEzKVmjvuSA67LszN1dZ-Dd_pkus6")         
         
         










if __name__ == "__main__":
    main()