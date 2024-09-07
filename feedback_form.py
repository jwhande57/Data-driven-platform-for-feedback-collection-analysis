import streamlit as st
from datetime import datetime
from utils import save_data

# Function to display the questionnaire form
def show_questionnaire():
    if st.session_state.get("form_submitted", False):
        st.warning("You have already submitted the form. You cannot submit it again.")
    else:
        st.title("📋 Share Your Feedback")
        st.header(
            "We Value Your Feedback, Please take a moment to share your thoughts with us. Your input helps us improve!"
        )
        with st.form("questionnaire_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                department = st.selectbox(
                    "Select department", ["Business", "Technical"]
                )
                program_of_study = st.selectbox(
                    "Program of study",
                    [
                        "Digital Marketing",
                        "Computer Networking",
                        "Financial Engineering",
                        "Software Engineering",
                        "Telecommunication",
                        "Data Science",
                    ],
                )
                year_of_study = st.selectbox(
                    "Year of study", [1.1, 1.2, 2.1, 2.2, 3.1, 3.2]
                )
                overall_quality = st.slider(
                    "How satisfied are you with the overall quality of education at the college?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )

                accessibility = st.slider(
                    "Rate the accessibility of college resources (e.g., library, labs, online materials).",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
            with col2:

                communication = st.slider(
                    "How effective are the college’s communication channels (emails, announcements, etc.)?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )

                career_services = st.slider(
                    "Evaluate the effectiveness of the career services center.",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )

                it_support = st.slider(
                    "How satisfied are you with the technology and IT support provided by the college?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
                academic_support = st.slider(
                    "Rate the support provided by academic advisors.",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
            with col3:
                campus_facilities = st.slider(
                    "How would you rate the quality of campus facilities (classrooms, cafeteria, etc.)?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
                recommendation = st.slider(
                    "How likely are you to recommend this college to prospective students?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )

                extracurricular_activities = st.slider(
                    "How satisfied are you with the extracurricular activities offered?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
                diversity_inclusion = st.slider(
                    "How would you rate the college’s efforts in promoting diversity and inclusion?",
                    min_value=1,
                    max_value=5,
                    step=1,
                    format="%d",
                )
            st.write(
                "##### Your voice matters! 🗣️ In the next few questions, feel free to share your thoughts and insights in as much detail as you'd like. The more expressive you are, the better we can understand your experience and improve. We're listening!"
            )

            greatest_strength = st.text_area(
                "What do you consider the greatest strength of the college?"
            )
            areas_of_improvement = st.text_area(
                "What areas do you think need improvement at the college?"
            )
            positive_experience = st.text_area(
                "Can you share an experience where a professor or staff member positively impacted your college life?"
            )
            additional_resources = st.text_area(
                "What additional resources or support would you like the college to provide?"
            )
            engagement_suggestions = st.text_area(
                "Do you have any suggestions on how the college could enhance student engagement?"
            )

            if submitted := st.form_submit_button(
                "Submit", type="primary", use_container_width=True
            ):
                data = {
                    "date": datetime.now().strftime(
                        "%Y-%m-%d"
                    ), 
                    "department": department,
                    "program of study": program_of_study,
                    "year of study": year_of_study,
                    "overall quality of education": overall_quality,
                    "accessibility of college resources": accessibility,
                    "effectiveness of communication channels": communication,
                    "quality of campus facilities": campus_facilities,
                    "likelihood to recommend the college": recommendation,
                    "satisfaction with extracurricular activities": extracurricular_activities,
                    "support provided by academic advisors": academic_support,
                    "promotion of diversity and inclusion": diversity_inclusion,
                    "effectiveness of career services": career_services,
                    "satisfaction with IT support": it_support,
                    "greatest strength": greatest_strength,
                    "areas needing improvement": areas_of_improvement,
                    "positive experience with professor/staff": positive_experience,
                    "additional resources or support desired": additional_resources,
                    "suggestions for enhancing student engagement": engagement_suggestions,
                }
                save_data(data)
                st.success(
                    "Thank You for Your Feedback! \nYour responses are invaluable to us and help shape the future of our college."
                )
                st.session_state["form_submitted"] = True
