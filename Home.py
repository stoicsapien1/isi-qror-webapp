import streamlit as st

def specialization_details():
    tracks = {
        "🧮 Data Science & Analytics": [
            "Analytics and insights for decision-making",
            "Statistical inference & hypothesis testing",
            "Practical applications using real-world data"
        ],
        "🧑‍💻 Machine Learning": [
            "Supervised & unsupervised learning methods",
            "Model tuning, validation & deployment",
            "End-to-end ML project development"
        ],
        "🧪 Statistical Quality Control": [
            "Control charts & process monitoring",
            "Six Sigma methods & lean improvements",
            "Reliability engineering applications"
        ],
        "💹 Quantitative Finance": [
            "Financial mathematics & modeling",
            "Risk measurement methodologies",
            "Computational finance techniques"
        ],
        "📉 Survival Analysis": [
            "Time-to-event statistical modeling",
            "Hazard functions & Kaplan–Meier estimation",
            "Applications in reliability and healthcare"
        ],
        "⏳ Time Series": [
            "Modeling and forecasting time-dependent data",
            "Stationary and non-stationary processes",
            "AR, MA, ARMA, ARIMA, and seasonal models",
            "Spectral analysis and frequency domain methods"
        ],
        "📊 Econometrics": [
            "Statistical methods for economic data analysis",
            "Regression models with economic applications",
            "Time series econometrics and forecasting",
            "Panel data models and causal inference"
        ],
    }

    st.subheader("📌 Experts in these domain")
    for track, topics in tracks.items():
        with st.expander(track):
            for point in topics:
                st.markdown(f"- {point}")

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
            
            ### 📬 Contact Information
            For any queries, please contact:
            - **Admin:** Belal Ahmed Siddiqui
            """,
            unsafe_allow_html=True
        )

    # --- HERO SECTION ---
    st.markdown(
    """
    <div style='text-align:center; padding: 2em 0; background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%); border-radius: 15px; margin: 1em 0;'>
        <h1 style='font-size: 2.5em; font-weight: 700; color: #1E1E1E; margin-bottom: 0.3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>
            📚 M.Tech QROR Study Material Hub
        </h1>
        <p style='font-size: 1.2em; color: #4A4A4A; font-weight: 500; margin-top: 0.5em;'>
            Indian Statistical Institute, Kolkata 
            <span style='margin: 0 0.5em;'>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

    # Modern quote box (no fixed background)
    st.markdown(
        """
        <div style='border-radius:12px; padding:18px 24px; margin:18px 0;'>
            <div style='font-size:1.13em; font-style:italic; font-weight:600; line-height:1.5;'>
            “Arise, awake, and stop not until the goal is reached.”
            </div>
            <div style="font-size:1.02em; text-align:right;">— Swami Vivekananda</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("About the Program")
    st.markdown(
    """
    

    The Indian Statistical Institute, Kolkata offers this specialized program combining academic excellence 
    with industry relevance. 
    Our graduates emerge as:

    * 🎯 Industry-ready professionals.
    * 🔬 Data-driven decision makers.
    * 💡 Innovation leaders.

    **Key Focus Areas:**
    * Machine Learning 
    * Artificial Intelligence
    * Quant Finance
    * Statistical Analysis
    * Operations Research
    * Reliability Engineering
    * Industrial Statistics

    
    """
)

    specialization_details()

    # --- SYLLABUS SECTION ---
    st.markdown("---")
    st.markdown("### 📘 Syllabus")
    st.link_button(
        "📒 View Detailed Syllabus",
        url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing",
    )

    # --- Disclaimer / Warning ---
    st.markdown("---")
    st.markdown("**Disclaimer:**")
    st.warning(
        "All shared materials (PDFs, books, notes) are for educational use only. Copyright belongs to the original owners."
    )

    # --- Footer ---
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; font-size: 1.07em; margin-bottom:16px;'>"
        "Made with ❤️ by Belal Ahmed Siddiqui"
        "</div>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
