import streamlit as st

def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Data Science Study Material📚")
    st.image("https://media.licdn.com/dms/image/C4D12AQGD_su1k14bYA/article-cover_image-shrink_720_1280/0/1583217310732?e=2147483647&v=beta&t=an15cumXvL1rLYucw3WqOUkf-27-B-l52jkmpEfPaKw")
    st.sidebar.success("SELECT THE PAGE ABOVE")
 
    selected_material = st.selectbox("Select the Options", ["INTERVIEW","YT PLAYLIST","PROJECT","ML BOOKS"])
    if selected_material=="ML BOOKS":
            st.link_button("DOWNLOAD DATA SCIENCE BOOKS[COMPILED BY SOUBHIK BHATTACHARYA]⚡⚡",url="https://drive.google.com/drive/folders/1tMlOwyXzpiiSWmvlP-X7HSrc4dxBi0YJ?usp=sharing")
    elif selected_material=="INTERVIEW":
        st.link_button("INTERVIEW PREP PLATFORM",url="https://cracked-ds-platform.vercel.app")
            
    elif selected_material=="YT PLAYLIST":

        data=st.selectbox("Select the Topic💹",["Python","NUMPY","PANDAS","MATPLOTLIB","SEABORN","ML","DL"])
        if data=="ML":
            st.link_button("ML CAMPUSX[Code+ Concepts]",url="https://www.youtube.com/watch?v=ZftI2fEz0Fw&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH")
            st.link_button("ML STATSQUEST[Concepts]",url="https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF")
        elif data=="Python":
            st.link_button("YT Python Playlist",url="https://www.youtube.com/watch?v=JP7ITIXGpHk&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index=2")
            st.link_button("Python Practice[HACKERRANK]",url="https://www.hackerrank.com/domains/python")
            st.link_button("Python Question[PDF]",url="https://docs.google.com/document/d/1CuKacG3lnnt5B-7kB9p1DiJ2PLFW8TQWn9JG1lTYRJs/edit#heading=h.ghy5ky51yxzv")
        elif data=="NUMPY":
            st.link_button("NUMPY PLAYLIST",url="https://www.youtube.com/watch?v=d0E0_87CrFA&list=PLyMom0n-MBrpzC91Uo560S4VbsiLYtCwo&index=4")

        elif data=="PANDAS":
            st.link_button("PANDAS PLAYLIST",url="https://www.youtube.com/watch?v=CmorAWRsCAw&list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy")
            st.link_button("PANDAS PRACTICE",url="https://drive.google.com/file/d/1onfaw-0pA2fhCNccBLggoZlm53BjJ4FV/view?usp=sharing")
        elif data=="MATPLOTLIB":
            st.link_button("MATPLOTLIB PLAYLIST",url="https://www.youtube.com/watch?v=qqwf4Vuj8oM&list=PLeo1K3hjS3uu4Lr8_kro2AqaO6CFYgKOl")

        elif data=="SEABORN":
            st.link_button("SEABORN PLAYLIST",url="https://www.youtube.com/watch?v=Hb3RmWowIKw&list=PLc20sA5NNOvq8CldEUOZEHnoVIk4svXuZ")
        elif data=="DL":
            st.link_button("DL CAMPUSX",url="https://www.youtube.com/watch?v=2dH_qjc9mFg&list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn")    
    elif selected_material=="PROJECT":
        st.link_button("BASIC ML PROJECTS",url="https://www.youtube.com/watch?v=fiz1ORTBGpY&list=PLfFghEzKVmjvuSA67LszN1dZ-Dd_pkus6")         
         
         
    st.markdown("""
    <style>
        .playlist {
            color: #1f77b4; /* blue */
        }
        .project {
            color: #ff7f0e; /* orange */
        }
        .books {
            color: #2ca02c; /* green */
        }
        .highlight {
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### <span class="playlist">YT PLAYLIST</span>
    This section contains YouTube playlists on several ML topics like <span class="highlight">Numpy</span>, <span class="highlight">Pandas</span>, <span class="highlight">Seaborn</span>, etc.

    ### <span class="project">PROJECT</span>
    This section contains video links to several ML projects.

    ### <span class="books">ML BOOKS</span>
    This section contains several <span class="highlight">Machine Learning (ML)</span>, <span class="highlight">Deep Learning (DL)</span>, and <span class="highlight">Time-Series</span> books.
    """, unsafe_allow_html=True)









if __name__ == "__main__":
    main()
