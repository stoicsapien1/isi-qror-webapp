import streamlit as st

def main():
    st.title("Second Semester Study Material📚")
    st.sidebar.success("SELECT THE PAGE ABOVE⚡")
    st.write("***PLEASE SELECT THE SUBJECT*** 🤓")
    selected_material = st.selectbox("Select the Subjects", ["IEM", "STATISTICAL METHOD 2", "RELIABILITY", "STOCHASTIC PROCESSES", "SQC", "RMMR TABLE","EXAMINATION PAPERS"])
    if selected_material=="SQC":
        st.link_button("DOWNLOAD SQC STUDY MATERIAL(COMPILED BY PRAKASH KUMAR)⚡",url="https://drive.google.com/file/d/1nnIxDBcuXPNKgi-dOdZDpf5FaqOwMnn5/view?usp=sharing")
        st.link_button("LECTURE WISE NOTES",url="https://drive.google.com/drive/folders/1rnlw7uOY9-B2Wvjy1LWqFANEyefQSNPN?usp=sharing")
    elif selected_material == "RMMR TABLE":
        st.link_button("DOWNLOAD RMMR TABLE📥", url="https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link")
    elif selected_material == "EXAMINATION PAPERS":
        st.link_button("DOWNLOAD PAPERS[OLD]📄", url="https://drive.google.com/drive/folders/1OU3Q5o9s0GYnd54FA3mV-ZDmTt32bX0e?usp=sharing")
    elif selected_material=="STOCHASTIC PROCESSES":
        st.link_button("DOWNLOAD NOTES OF SUMIT KR GUPTA 🤓⚡",url="https://drive.google.com/file/d/1BsEoA4EyWQdj8lo5wa8tsBN1KbPV0oPY/view?usp=sharing")
        st.link_button("DOWNLOAD NOTES OF SOUMYODEEP MONDAL⚡",url="https://drive.google.com/file/d/1d0weHrafTONxKm2pgQc1gtgRNWzuVwgT/view?usp=sharing")
        st.link_button("DOWNLOAD DIGITAL NOTES⚡🤓",url="https://drive.google.com/drive/folders/1XIJPCLtu8J8WrSXrCpXx_16mViIWAnrN?usp=sharing")
    elif selected_material=="RELIABILITY":
        st.link_button("DOWNLOAD NOTES OF SOUMYODEEP MONDAL⚡",url="https://drive.google.com/file/d/1BsEoA4EyWQdj8lo5wa8tsBN1KbPV0oPY/view?usp=sharing")
        st.link_button("DOWNLOAD DIGITAL NOTES🖤",url="https://drive.google.com/drive/folders/1UAC9V3l0irJy8UnxiQuzt68714hRXcZI?usp=sharing")
    elif selected_material=="STATISTICAL METHOD 2":
        st.link_button("DOWNLOAD APPLIED STATISTICS & PROBABILITY FOR ENGINEERS[BOOK]",url="https://drive.google.com/file/d/1zl1Pr1vzxL50-hCxC8erNuqiWMkNuXku/view?usp=sharing")
       
if __name__ == "__main__":
    main()
