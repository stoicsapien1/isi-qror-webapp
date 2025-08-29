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

    st.subheader("📌 Thrust Area")
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
    <div style='text-align:center; padding: 0.8em 1em; background: #fafafa; border: 1px solid #ddd; border-radius: 8px; margin: 0.8em 0;'>
        <h1 style='font-size: 1.4em; font-weight: 600; color: #1a1a1a; margin: 0.2em 0;'>
            📚 M.Tech QROR Study Hub
        </h1>
        <p style='font-size: 0.9em; color: #444; margin: 0;'>
            Indian Statistical Institute, Kolkata
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
    The **Indian Statistical Institute, Kolkata** is home to the 
    **M.Tech in Quality, Reliability & Operations Research (QROR)** :
    A program that doesn’t just teach theory, but prepares you to **make an impact**.  
    You’ll work on real-world problems, dive deep into data, and build skills that 
    let you shape decisions in industries that matter.  

    🌟 Our students grow into:
    * Professionals who can turn data into meaningful insights.  
    * Thinkers who use AI and statistics to solve real challenges.  
    * Innovators ready to lead in finance, technology, and research.  

    ---
    ### What you’ll explore:
    * 🤖 **Artificial Intelligence & Machine Learning** – building smart, adaptive systems.  
    * 🧠 **Deep Learning & GenAI** – from neural networks to advanced chatbots.  
    * 📈 **Quantitative Finance & Risk Modelling** – making sense of uncertainty in markets.  
    * 📊 **Statistical & Industrial Analytics** – the foundation of sound decisions.  
    * 🛠 **Operations Research & Optimization** – solving complex efficiency puzzles.  
    * 🔧 **Reliability & Quality Engineering** – ensuring systems last and perform.  

    
    """
)


    

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
