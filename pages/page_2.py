import streamlit as st

def main():
    st.title("First Semester Study Material 📚")
    st.sidebar.success("SELECT THE PAGE ABOVE 📄")
    st.write("***PLEASE SELECT THE SUBJECT*** 🤓")
    
    selected_material = st.selectbox("Select the Subjects", ["QMS", "STATISTICAL METHOD 1", "PROBABILITY", "OPERATIONS RESEARCH", "PROGRAMMING AND DATA STRUCTURES", "RMMR TABLE","EXAMINATION PAPERS"])
    
    if selected_material == "RMMR TABLE":
        st.link_button("DOWNLOAD RMMR TABLE📥", url="https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link")
    elif selected_material == "QMS":
        st.link_button("Download QMS STUDY MATERIAL 📖", url="https://drive.google.com/drive/folders/1AYiY3CMUkNWluAnP9BhMmZkx5RRZciwD?usp=sharing")
        st.link_button("Download QMS ASSIGNMENT 📝", url="https://drive.google.com/drive/folders/1oWbDYyQ_ExKCuGF-B7aWfkh68MlCYllM?usp=sharing")
    elif selected_material == "EXAMINATION PAPERS":
        st.link_button("DOWNLOAD PAPERS[OLD] 📄", url="https://drive.google.com/drive/folders/1OU3Q5o9s0GYnd54FA3mV-ZDmTt32bX0e?usp=sharing")
    elif selected_material=="PROBABILITY":
        st.link_button("DOWNLOAD PROBABILITY NOTES🚀📚",url="https://drive.google.com/drive/folders/18SWl8nmu-TUET0ox2UiINcAw3d-X1Pg8?usp=sharing")
    elif selected_material=="STATISTICAL METHOD 1":
        st.link_button("DOWNLOAD SM1 NOTES🚀📚",url="https://drive.google.com/drive/folders/1EkesCgrU8dyRuIMuadtYVLqx8jwguN4l?usp=sharing")
    elif selected_material=="OPERATIONS RESEARCH":
        st.link_button("DOWNLOAD SKD SIR MATERIAL🚀📚",url="https://drive.google.com/file/d/1L2zAAHCSsqROBFeRSQ-Tqf4tAuvRnpki/view?usp=sharing")
        st.link_button("DOWNLOAD KK SIR MATERIAL🚀📚",url="https://drive.google.com/drive/folders/16KjUsw_BoQIzOkxTMrtMqfte5uqYFb0r?usp=sharing")
    elif selected_material=="PROGRAMMING AND DATA STRUCTURES":
        st.link_button("DOWNLOAD UB SIR MATERIAL🚀📚",url="https://drive.google.com/drive/folders/1E7lieYsGwp8UXsHXrogh0818iwuMlj6d?usp=drive_link")

if __name__ == "__main__":
    main()
