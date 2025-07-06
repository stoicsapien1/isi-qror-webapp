import streamlit as st

def main():
    st.set_page_config(page_title="ISI QROR MATERIAL HUB", page_icon="📚", layout="centered", initial_sidebar_state="auto", menu_items=None)
    st.title("Second Semester Study Material📚")
    
    st.write("***PLEASE SELECT THE SUBJECT*** 🤓")
    st.sidebar.success("SELECT THE PAGE ABOVE")

    selected_material = st.selectbox("Select the Subjects", ["IEM", "STATISTICAL METHOD 2", "RELIABILITY", "STOCHASTIC PROCESSES", "SQC", "RMMR TABLE","EXAMINATION PAPERS"])
    if selected_material=="SQC":
        st.link_button("DOWNLOAD SQC STUDY MATERIAL(COMPILED BY PRAKASH KUMAR)⚡",url="https://drive.google.com/file/d/1nnIxDBcuXPNKgi-dOdZDpf5FaqOwMnn5/view?usp=sharing")
        st.link_button("DOWNLOAD SQC QUIZ📚",url="https://drive.google.com/file/d/1OPrGzX0tiWjG29rc07XztYRYZ7iR1-7M/view?usp=sharing")
        st.link_button("LECTURE WISE NOTES❤️",url="https://drive.google.com/drive/folders/1rnlw7uOY9-B2Wvjy1LWqFANEyefQSNPN?usp=sharing")
    elif selected_material == "RMMR TABLE":
        st.link_button("DOWNLOAD RMMR TABLE📥", url="https://drive.google.com/file/d/1GxYgJQlY4sl6XDwmna01JFAVojprTuF5/view?usp=drive_link")
    elif selected_material == "EXAMINATION PAPERS":
        st.link_button("DOWNLOAD PAPERS[OLD]📄", url="https://drive.google.com/drive/folders/1OU3Q5o9s0GYnd54FA3mV-ZDmTt32bX0e?usp=sharing")
        st.link_button("DOWNLOAD MID SEM PAPERS[NEW]📚",url="https://drive.google.com/file/d/1L1ah2nSwfExuZDQpVtQoVkbcnbux_ruu/view?usp=sharing")
        st.link_button("DOWNLOAD END SEM PAPERS[NEW]🤓",url="https://drive.google.com/file/d/1CORRJ2dNQck7of-wQiVvO27Grtc-GNKE/view?usp=sharing")
        
    elif selected_material=="STOCHASTIC PROCESSES":
        st.link_button("DOWNLOAD NOTES OF SUMIT KR GUPTA 🤓⚡",url="https://drive.google.com/file/d/1BsEoA4EyWQdj8lo5wa8tsBN1KbPV0oPY/view?usp=sharing")
        st.link_button("DOWNLOAD NOTES OF SOUMYADEEP MONDAL⚡",url="https://drive.google.com/file/d/1d0weHrafTONxKm2pgQc1gtgRNWzuVwgT/view?usp=sharing")
        st.link_button("DOWNLOAD DIGITAL NOTES⚡🤓",url="https://drive.google.com/drive/folders/1XIJPCLtu8J8WrSXrCpXx_16mViIWAnrN?usp=sharing")
    elif selected_material=="RELIABILITY":
        st.link_button("DOWNLOAD NOTES OF SOUMYADEEP MONDAL⚡",url="https://drive.google.com/file/d/1gHiVCOTznLRFLDEuuEpsLEqeEzV-gYCy/view?usp=sharing")
        st.link_button("DOWNLOAD DIGITAL NOTES🖤",url="https://drive.google.com/drive/folders/1UAC9V3l0irJy8UnxiQuzt68714hRXcZI?usp=sharing")
        st.link_button("DOWNLOAD RELIABILITY END SEM'23 PAPER📚",url="https://drive.google.com/file/d/1_7_kJobSaHOLtr_OJL5LAhC1QwlO503L/view?usp=sharing")
        st.link_button("DOWNLOAD RELIABILITY NOTES OF SUMIT KR GUPTA🖤",url="https://drive.google.com/file/d/16wjkhSdc3Q1upUrbYgiymyXWTNUL-5iD/view?usp=sharing")
        st.link_button("DOWNLOAD RELAIBILITY NOTES OF PRAKASH KUMAR⚡",url="https://drive.google.com/file/d/1Qv2AgKjpIoSrhxO61l45i7TDUxmaUN1c/view?usp=sharing")
    elif selected_material=="STATISTICAL METHOD 2":
        st.link_button("DOWNLOAD APPLIED STATISTICS & PROBABILITY FOR ENGINEERS[BOOK]⚡",url="https://drive.google.com/file/d/1zl1Pr1vzxL50-hCxC8erNuqiWMkNuXku/view?usp=sharing")
        st.link_button("DOWNLOAD HYPOTHESIS TESTING NOTES❤️",url="https://drive.google.com/drive/folders/1sJWCY9wsFlnJksUnzMt2pXRMSC-ZahSO?usp=sharing")
        st.link_button("DOWNLOAD ANOVA NOTES⚡",url="https://drive.google.com/drive/folders/1vy_669nBzsQdUBTsm8hv9LKW_Iuo8OFN?usp=sharing") 
        st.link_button("DOWNLOAD SIMPLE LINEAR REGRESSION NOTES💹",url="https://drive.google.com/drive/folders/1JtGStvIyrjN37Wdklth76jBNWHOGLwH6?usp=sharing") 
        st.link_button("DOWNLOAD MULTIPLE LINEAR REGRESSION NOTES💹",url="https://drive.google.com/drive/folders/19yOCk-F_ZBll16CbGlmfwfDJ3Su8ft1q?usp=sharing") 
        st.link_button("DOWNLOAD ANCOVA NOTES📊",url="https://drive.google.com/drive/folders/1UQsOjw7l2Wso6W4h6AnIgCDmy6pOwX1Y?usp=sharing")
        st.link_button("DOWNLOAD NPT NOTES🧪",url="https://drive.google.com/drive/folders/1Yfgi4So82e8SYVXLal-4NBbxMOuSXkoE?usp=sharing")
    elif selected_material=="IEM":
        st.link_button("DOWNLOAD KK SIR MATERIAL[BEFORE MID SEM]⚡",url="https://drive.google.com/drive/folders/1KuRRgp-U6ymxQzB9zSNSPoRyQI6ThUax?usp=sharing")
        st.link_button("DOWNLOAD IEM MID SEM PAPER📊",url="https://drive.google.com/file/d/1KIxPTu0px4THDmA4EZ_Ft86w-PmonltD/view?usp=sharing")
        st.link_button("DOWNLOAD KK SIR COMPLETE NOTES📚📊",url="https://drive.google.com/file/d/1zWDk6OliPUgnq_FFmwPkYkDptI6BOXMi/view?usp=sharing")

if __name__ == "__main__":
    main()
