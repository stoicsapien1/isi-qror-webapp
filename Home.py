import streamlit as st

def main():
    st.set_page_config(
        page_title="ISI QROR Study Hub",
        page_icon="📚",
        layout="centered"
    )
    
    # Custom CSS for modern styling
    st.markdown("""
        <style>
        /* Main container spacing */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            font-size: 1.05rem;
            font-weight: 500;
        }
        
        /* Better spacing for lists */
        .stMarkdown ul {
            margin-top: 0.5rem;
        }
        
        .stMarkdown li {
            margin-bottom: 0.4rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### 📬 Contact")
        st.info("**Admin** : Belal Ahmed Siddiqui")
        
        st.markdown("---")
        st.caption("Made with ❤️ for ISI QROR Students")

    # Hero Section
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0.8rem; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px; margin-bottom: 1rem; 
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
        <h1 style='color: white; font-size: 1.2rem; 
                   font-weight: 600; margin: 0 0 0.2rem 0;'>
            📚 M.Tech QROR Study Hub
        </h1>
        <p style='color: rgba(255,255,255,0.85); 
                  font-size: 0.8rem; margin: 0;'>
            Indian Statistical Institute, Kolkata
        </p>
    </div>
""", unsafe_allow_html=True)



    # Quote Section
    st.markdown("""
        <div style='background: #f8f9fa; border-left: 4px solid #667eea; padding: 1.5rem 2rem; 
                    border-radius: 8px; margin: 2rem 0;'>
            <p style='font-size: 1.15rem; font-style: italic; color: #2c3e50; margin: 0 0 0.5rem 0; line-height: 1.6;'>
                "Arise, awake, and stop not until the goal is reached."
            </p>
            <p style='text-align: right; color: #5a6c7d; font-size: 0.95rem; margin: 0;'>
                — Swami Vivekananda
            </p>
        </div>
    """, unsafe_allow_html=True)

    # About Section
    st.markdown("## About the Program")
    
    st.markdown("""
        The **Indian Statistical Institute, Kolkata** offers the **M.Tech in Quality, Reliability & Operations Research (QROR)** — 
        a program designed to transform theory into real-world impact.
        
        Work on challenging problems, master data-driven decision making, and develop expertise that drives innovation across industries.
    """)
    
    # Key Outcomes
    st.markdown("### 🌟 What You'll Become")
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
            <div style='background: #e8f4f8; padding: 1.2rem; border-radius: 10px; height: 100%;'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📊</div>
                <div style='font-weight: 600; color: #1e3a8a; margin-bottom: 0.3rem;'>Data Professional</div>
                <div style='font-size: 0.9rem; color: #475569;'>Turn data into actionable insights</div>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
            <div style='background: #f3e8ff; padding: 1.2rem; border-radius: 10px; height: 100%;'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🧠</div>
                <div style='font-weight: 600; color: #6b21a8; margin-bottom: 0.3rem;'>Problem Solver</div>
                <div style='font-size: 0.9rem; color: #475569;'>Use AI to tackle real challenges</div>
            </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
            <div style='background: #fef3c7; padding: 1.2rem; border-radius: 10px; height: 100%;'>
                <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🚀</div>
                <div style='font-weight: 600; color: #92400e; margin-bottom: 0.3rem;'>Industry Leader</div>
                <div style='font-size: 0.9rem; color: #475569;'>Lead in finance, tech & research</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Core Areas
    st.markdown("### 🎯 Core Areas of Study")
    
    areas = {
        "🤖 AI & Machine Learning": "Build intelligent, adaptive systems",
        "🧠 Deep Learning & GenAI": "From neural networks to advanced models",
        "📈 Quantitative Finance": "Risk modeling and market analysis",
        "📊 Statistical Analytics": "Foundation of data-driven decisions",
        "🛠 Operations Research": "Solve complex optimization problems",
        "🔧 Quality Engineering": "Ensure reliability and performance"
    }
    
    cols = st.columns(2)
    for idx, (area, desc) in enumerate(areas.items()):
        with cols[idx % 2]:
            st.markdown(f"""
                <div style='background: white; border: 1px solid #e5e7eb; padding: 1rem; 
                            border-radius: 8px; margin-bottom: 0.8rem;'>
                    <div style='font-weight: 600; color: #1f2937; margin-bottom: 0.3rem;'>{area}</div>
                    <div style='font-size: 0.9rem; color: #6b7280;'>{desc}</div>
                </div>
            """, unsafe_allow_html=True)

    # Specialization Tracks

    
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
    


    # Syllabus Section
    st.markdown("---")
    st.markdown("## 📘 Syllabus")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button(
            "📒 View Detailed Syllabus",
            url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing",
            use_container_width=True
        )

    # Disclaimer
    st.markdown("---")
    st.info("**Disclaimer:** All shared materials are for educational use only. Copyright belongs to the original owners.")

    # Footer
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding: 1.5rem; background: #f9fafb; border-radius: 8px; margin-top: 2rem;'>
            <p style='color: #6b7280; font-size: 0.95rem; margin: 0;'>
                Made with ❤️ by <strong>Belal Ahmed Siddiqui</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()