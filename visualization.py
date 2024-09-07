import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import plotly.express as px

def display_overview(filtered_df):
    col1, col2 = st.columns(2, gap='medium')
    col1.image("assets\je160069c17c0efb0aaefefad9ce7c8f49.jpg")
    col2.subheader("Mean satisfaction levels across various metrics.")
    mean_values = filtered_df.iloc[:, 4:14].select_dtypes(include='number').mean().round(2)
    col2.bar_chart(mean_values)

    distribution_option = col1.selectbox("Select Distribution to Display", options=filtered_df.columns[4:14])
    if distribution_option:
        col1.subheader(f"Distribution of responses for {distribution_option}.")
        fig, ax = plt.subplots()
        sns.histplot(filtered_df[distribution_option], bins=5, kde=False, ax=ax)
        col1.pyplot(fig)

    col2.subheader("Word cloud of 'Greatest Strength' comments.")
    strengths_text = " ".join(filtered_df["greatest strength"])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(strengths_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='antialiased')
    ax.axis("off")
    col2.pyplot(fig)

    col2.subheader("Word cloud of 'Areas needing improveme' comments.")
    improvements_text = " ".join(filtered_df["areas needing improvement"].fillna("").astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(improvements_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='antialiased')
    ax.axis("off")
    col2.pyplot(fig)
    satisfaction_by_department(col2,filtered_df)
    sentiment_analysis(col1, filtered_df)
    cluster_analysis(filtered_df)
    anova_satisfaction_by_program(filtered_df)
    correlation_heatmap(filtered_df)

def sentiment_analysis(col, filtered_df):
    col.subheader("Average sentiment scores for each department.")
    sentiment_score = filtered_df.groupby('department')['Sentiment'].mean().round(2)
    fig, ax = plt.subplots()
    sentiment_score.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title("Average Sentiment by Department")
    col.pyplot(fig)

    col.subheader("Distribution of sentiment scores.")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['Sentiment'], bins=10, kde=True, ax=ax, color='purple')
    ax.set_title("Distribution of Sentiment Scores")
    col.pyplot(fig)

def satisfaction_by_department(col,filtered_df):
    col.subheader("Average satisfaction levels across departments.")
    dept_satisfaction = filtered_df.groupby("department").mean().round(2)
    fig, ax = plt.subplots()
    dept_satisfaction.plot(kind='bar', ax=ax)
    ax.set_title("Average Satisfaction by Department")
    col.pyplot(fig)

def cluster_analysis(filtered_df):
    st.subheader("K-Means clustering results on satisfaction data.")
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(filtered_df.iloc[:, 4:14].select_dtypes(include='number'))
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(pca_result)
    labels = kmeans.labels_

    fig, ax = plt.subplots()
    scatter = ax.scatter(pca_result[:, 0], pca_result[:, 1], c=labels, cmap='viridis')
    ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.set_title("PCA of Satisfaction Data with K-Means Clustering")
    st.pyplot(fig)

def anova_satisfaction_by_program(filtered_df):
    st.subheader("Distribution of satisfaction scores by program.")
    anova_df = pd.melt(filtered_df, id_vars=['program of study'], value_vars=filtered_df.columns[4:14])
    fig = px.box(anova_df, x='program of study', y='value', color='variable')
    st.plotly_chart(fig)

def correlation_heatmap(filtered_df):
    st.subheader("Correlation between satisfaction metrics.")
    correlation_matrix = filtered_df.iloc[:, 4:14].select_dtypes(include='number').corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
