import streamlit as st

def main():
    # 1. Page Configuration
    st.set_page_config(
        page_title="ISI QROR Study Hub",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # 2. Custom CSS for animations and modern styling
    st.markdown("""
        <style>
        /* Main container padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Smooth hover effects for custom HTML cards */
        .hover-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 10px;
        }
        .hover-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
        }
        
        /* Typography tweaks */
        .streamlit-expanderHeader {
            font-size: 1.05rem;
            font-weight: 600;
        }
        .stMarkdown ul { margin-top: 0.5rem; }
        .stMarkdown li { margin-bottom: 0.4rem; }
        </style>
    """, unsafe_allow_html=True)

    # 3. Sidebar
    with st.sidebar:
        st.markdown("### 📬 Contact & Info")
        st.info("**Admin:**\n\nBelal Ahmed Siddiqui")
        
        st.divider()
        st.caption("Made with ❤️ for ISI QROR Students")

    # 4. Hero Section (Gradient Banner)
    st.markdown("""
        <div class="hover-card" style='text-align: center; padding: 1rem 0.75rem; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h1 style='color: white; font-size: 2.2rem; font-weight: 500; margin: 0 0 0.5rem 0;'>
                 M.Tech QROR Study Hub
            </h1>
            <p style='color: rgba(255,255,255,0.9); font-size: 1.1rem; margin: 0; font-weight: 400;'>
                Indian Statistical Institute, Kolkata
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 5. Quote Section (Using native info for theme adaptability)
    st.info("""
    *"Arise, awake, and stop not until the goal is reached."*  
    **— Swami Vivekananda**
    """, icon="💡")

    st.write("<br>", unsafe_allow_html=True)

    # 6. About Section
    st.markdown("## 🏫 About the Program")
    st.write("""
        The **Indian Statistical Institute, Kolkata** offers the **M.Tech in Quality, Reliability & Operations Research (QROR)** — 
        a program designed to transform theory into real-world impact.
        
        Work on challenging problems, master data-driven decision making, and develop expertise that drives innovation across global industries.
    """)
    
    st.write("<br>", unsafe_allow_html=True)

    # 7. Key Outcomes (Using native containers for perfect Dark/Light mode support)
    st.markdown("### 🌟 What You'll Become")
    
    cols = st.columns(3)
    
    with cols[0]:
        with st.container(border=True):
            st.markdown("### 📊")
            st.markdown("**Data Professional**")
            st.caption("Turn raw data into actionable business insights.")
            
    with cols[1]:
        with st.container(border=True):
            st.markdown("### 🧠")
            st.markdown("**Problem Solver**")
            st.caption("Use advanced AI to tackle real-world challenges.")
            
    with cols[2]:
        with st.container(border=True):
            st.markdown("### 🚀")
            st.markdown("**Industry Leader**")
            st.caption("Lead initiatives in finance, tech & core research.")

    st.write("<br>", unsafe_allow_html=True)

    # 8. Core Areas
    st.markdown("### 🎯 Core Areas of Study")
    
    areas = {
        "🤖 AI & Machine Learning": "Build intelligent, adaptive systems",
        "🧠 Deep Learning & GenAI": "From neural networks to advanced models",
        "📈 Quantitative Finance": "Risk modeling and market analysis",
        "📊 Statistical Analytics": "Foundation of data-driven decisions",
        "🛠 Operations Research": "Solve complex optimization problems",
        "🔧 Quality Engineering": "Ensure reliability and performance"
    }
    
    # Render Core Areas in a 2-column grid using native containers
    area_cols = st.columns(2)
    for idx, (area, desc) in enumerate(areas.items()):
        with area_cols[idx % 2]:
            with st.container(border=True):
                st.markdown(f"**{area}**")
                st.caption(desc)

    st.write("<br>", unsafe_allow_html=True)

    # 9. Specialization Tracks (Fixed: Now actually renders using expanders)
    st.markdown("### 🎓 Specialization Tracks")
    
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
    
    # Split the tracks dictionary into two columns for a compact layout
    track_items = list(tracks.items())
    mid_point = (len(track_items) + 1) // 2
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        for title, items in track_items[:mid_point]:
            with st.expander(title):
                for item in items:
                    st.write(f"- {item}")
                    
    with col_right:
        for title, items in track_items[mid_point:]:
            with st.expander(title):
                for item in items:
                    st.write(f"- {item}")

    # 10. Syllabus Section
    st.divider()
    st.markdown("## 📘 Course Syllabus")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button(
            "📒 View Detailed Syllabus (PDF)",
            url="https://drive.google.com/file/d/1otS_-835q4W_EuDuWLtTTGohF-d21Wzk/view?usp=sharing",
            use_container_width=True,
            type="primary" # Makes the button pop with the theme's primary color
        )

    # 11. Disclaimer & Footer
    st.divider()
    st.caption("⚠️ **Disclaimer:** All shared materials are for educational use only. Copyright belongs to the original owners.")

if __name__ == "__main__":
    main()