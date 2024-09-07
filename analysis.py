import random

from llm_integration import analyze_generate_response

def generate_feedback_summary(filtered_df):
    # Randomly select 10 items from each of the specified columns
    random_strengths = random.sample(
        filtered_df["greatest strength"].tolist(),
        min(10, len(filtered_df["greatest strength"])),
    )
    random_improvements = random.sample(
        filtered_df["areas needing improvement"].tolist(),
        min(10, len(filtered_df["areas needing improvement"])),
    )
    random_resources = random.sample(
        filtered_df["additional resources or support desired"].tolist(),
        min(10, len(filtered_df["additional resources or support desired"])),
    )

    # Concatenate the randomly selected feedback items
    feedback_data = " ".join(random_strengths)
    feedback_data += " " + " ".join(random_improvements)
    feedback_data += " " + " ".join(random_resources)

    # Generate the report summary
    report_summary = f"""
    Report Summary:

    - Total records analyzed: {len(filtered_df)}
    - Average satisfaction with the overall quality of education: {filtered_df['overall quality of education'].mean():.2f}
    - Average rating of campus facilities: {filtered_df['quality of campus facilities'].mean():.2f}
    - Sentiment analysis (based on "Greatest Strength" comments): {filtered_df['Sentiment'].mean():.2f}

    Key Findings:

    - The department with the highest average satisfaction is {filtered_df.groupby('department')['overall quality of education'].mean().idxmax()}.
    - The program with the highest overall satisfaction is {filtered_df.groupby('program of study')['overall quality of education'].mean().idxmax()}.
    - The most common strength cited by students is related to {filtered_df['greatest strength'].mode()[0]}.
    - The area needing the most improvement is {filtered_df['areas needing improvement'].mode()[0]}.
    """

    prompt = (
        f"Summarize the following student feedback data focusing on the greatest strengths, areas needing improvement, "
        f"and additional resources or support desired in their academic experiences. "
        f"Please structure the response in Markdown format and include key findings and analysis. your report should not be longer than 500 words"
        f"{feedback_data} {report_summary}"
    )
    analyze_generate_response(prompt)


def generate_recommendations(filtered_df):
    # Randomly select 10 items from "areas needing improvement" and related columns for richer context
    random_improvements = random.sample(
        filtered_df["areas needing improvement"].tolist(),
        min(10, len(filtered_df["areas needing improvement"])),
    )
    random_strengths = random.sample(
        filtered_df["greatest strength"].tolist(),
        min(10, len(filtered_df["greatest strength"])),
    )
    random_resources = random.sample(
        filtered_df["additional resources or support desired"].tolist(),
        min(10, len(filtered_df["additional resources or support desired"])),
    )

    # Concatenate the selected feedback items
    feedback_texts = " ".join(random_improvements)
    feedback_texts += " " + " ".join(random_strengths)
    feedback_texts += " " + " ".join(random_resources)

    prompt = (
        f"Based on the following student feedback concerning areas needing improvement, greatest strengths, and desired additional resources or support, "
        f"generate actionable recommendations to enhance overall student satisfaction and engagement. Consider the broader context provided by various "
        f"departments, programs of study, and satisfaction metrics. Structure the response in Markdown format, your report should not be longer than 500 words:, including specific suggestions, justifications, "
        f"and potential impacts on student,  {feedback_texts}"
    )

    analyze_generate_response(prompt)


def predict_future_trends(filtered_df):
    # Randomly select 10 items from the "suggestions for enhancing student engagement" column
    random_suggestions = random.sample(
        filtered_df["suggestions for enhancing student engagement"].tolist(),
        min(10, len(filtered_df["suggestions for enhancing student engagement"])),
    )

    # Concatenate the selected feedback items
    feedback_texts = " ".join(random_suggestions)

    prompt = (
        f"Based on the following student feedback regarding suggestions for enhancing engagement, "
        f"predict future trends in student satisfaction. Consider the potential impacts on academic success, "
        f"campus life, and overall student experience. Format the response in a structured Markdown format with "
        f"sections for predicted trends, rationale, and potential outcomes,your report should not be longer than 500 words: {feedback_texts}"
    )

    # Generate the response using the LLM
    analyze_generate_response(prompt)
