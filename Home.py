import streamlit as st

def specialization_details():
    tracks = {
        "🧮 Data Science & Analytics": "Courses focus on analytics, statistical inference, and practical applications in real-world cases.",
        "🧑‍💻 Machine Learning": "Supervised & unsupervised learning, model validation, scalability, and hands-on projects.",
        "🧪 Statistical Quality Control": "Process control, Six Sigma methods, and reliability engineering for quality improvement.",
        "💹 Quantitative Finance": "Financial mathematics, risk measurement, and computational finance techniques.",
        "📉 Survival Analysis": "Statistical methods for time-to-event data and real-life reliability/lifetime analysis."
    }
    for track, desc in tracks.items():
        with st.expander(track):
            st.write(desc)

def main():
    st.set_page_config(
        page_title="ISI QROR Material Hub",
        page_icon="📚",
        layout="centered"
    )

    # --- SIDEBAR: Contact Section ---
    with st.sidebar:
        st.markdown(
            """
            <hr style='margin-top:1.4em; margin-bottom:0.7em;'>
            <h3 style='margin-bottom:0.5em;'>📬 Contact Information</h3>
            <div style='font-size: 1.07em; margin-bottom:7px;'>
                For any queries, please contact:
            </div>
            <ul style='font-size:1.08em; margin-top:0.2em;'>
                <li><strong>Admin:</strong> Belal Ahmed Siddiqui</li>
            </ul>
            """,
            unsafe_allow_html=True
        )

    # --- HERO SECTION ---
   
    st.markdown(
        "<h1 style='text-align:center; margin-bottom:0.2em;'>M.Tech QROR Study Material Hub</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            border-radius:14px;
            margin:19px 0 16px 0;
            padding:21px 27px 11px 27px;
            box-shadow: 0 0 12px #bbb3;
            background: rgba(127,127,127,0.022);
        ">
            <div style="font-size:1.13rem; font-style:italic; font-weight:600; line-height:1.5;">
            “Arise, awake, and stop not until the goal is reached.”
            </div>
            <div style="font-size:1.03em; text-align:right;">— Swami Vivekananda</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- ABOUT SECTION ---
    st.header("About the Program")
    st.write(
        """The **M.Tech in Quality, Reliability & Operations Research (QROR)** at the Indian Statistical Institute, Kolkata, shapes experts in advanced analytics, AI, and industrial statistics.\n"""
    )
    specialization_details()

    # --- SYLLABUS BUTTON ---
    st.markdown("---")
    st.markdown("### 📘 Syllabus")
    st.link_button(
        "📒 View Detailed Syllabus",
        url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing"
    )

    # --- CONTACT & COMMUNITY ---
    st.markdown("---")
    st.markdown(
        """
        **Disclaimer:**  
        
        """
    )

    # --- DISCLAIMER / WARNING ---
    st.warning(
        "All shared materials (PDFs, books, notes) are for educational use only. Copyright belongs to the original owners."
    )

    # --- FOOTER ---
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align:center; color: var(--secondary); font-size: 1.07em; margin-bottom:16px;'>"
        "Made with ❤️ by Belal Ahmed Siddiqui"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
