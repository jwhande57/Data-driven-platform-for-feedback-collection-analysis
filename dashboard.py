import streamlit as st
from data_processing import load_data, apply_filters
from visualization import display_overview
from analysis import generate_feedback_summary, generate_recommendations, predict_future_trends

def dashboard():
    df = load_data("data/student_feedback_data_500.csv")
    st.sidebar.video("assets/viz.mp4",autoplay=True,loop=True,muted=True)
    # Sidebar for filtering options
    st.sidebar.title("Filters")
    years, months = df['date'].dt.year.unique(), df['date'].dt.month.unique()
    selected_year = st.sidebar.selectbox("Select Year", options=["All"] + sorted(years.tolist()))
    selected_month = st.sidebar.selectbox("Select Month", options=["All"] + sorted(months.tolist()))

    department_filter = st.sidebar.selectbox("Select Department", options=["All", "Technical", "Business"])
    program_filter = st.sidebar.selectbox("Select Program of Study", options=["All"] + df["program of study"].unique().tolist())
    year_filter = st.sidebar.selectbox("Select Year of Study", options=["All"] + df["year of study"].unique().tolist())

    filtered_df = apply_filters(df, department_filter, program_filter, year_filter, selected_year, selected_month)
    st.sidebar.markdown("<center>🌐 Developed with care by Jerald Whande</center>", unsafe_allow_html=True)

    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Feedback Summary", "Recommendations", "Future Trends Prediction"])

    with tab1:
        display_overview(filtered_df)
    with tab2:
        generate_feedback_summary(filtered_df)
    with tab3:
        generate_recommendations(filtered_df)
    with tab4:
        predict_future_trends(filtered_df)
