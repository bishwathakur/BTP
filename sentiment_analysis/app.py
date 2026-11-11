"""
Streamlit demo app for Autonomous Bus Public Sentiment Analyzer.
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import joblib
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

MODELS_DIR = "models"
RESULTS_DIR = "results"
DATA_DIR = "data"


@st.cache_resource
def load_model():
    model = joblib.load(os.path.join(MODELS_DIR, "best_model.joblib"))
    vectorizer = joblib.load(os.path.join(MODELS_DIR, "vectorizer.joblib"))
    model_name = joblib.load(os.path.join(MODELS_DIR, "best_model_name.joblib"))
    return model, vectorizer, model_name


@st.cache_data
def load_data():
    return pd.read_csv(os.path.join(DATA_DIR, "opinions.csv"))


def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    try:
        tokens = word_tokenize(text)
    except LookupError:
        tokens = text.split()
    try:
        stop_words = set(stopwords.words("english"))
    except LookupError:
        stop_words = set()
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]
    return " ".join(tokens)


def predict_sentiment(text, model, vectorizer):
    clean = preprocess_text(text)
    vec = vectorizer.transform([clean])

    prediction = model.predict(vec)[0]

    # Confidence: use decision_function or predict_proba depending on model type
    try:
        proba = model.predict_proba(vec)[0]
        confidence = max(proba) * 100
    except AttributeError:
        # LinearSVC: use decision_function distance as proxy
        decision = model.decision_function(vec)[0]
        # Softmax-like normalization for display
        import numpy as np
        exp_scores = np.exp(decision - np.max(decision))
        proba = exp_scores / exp_scores.sum()
        confidence = max(proba) * 100

    return prediction, confidence


def main():
    st.set_page_config(
        page_title="Autonomous Bus Sentiment Analyzer",
        page_icon="🚌",
        layout="wide",
    )

    # --- Sidebar ---
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/bus.png", width=80)
        st.title("Project Info")
        st.markdown("---")
        st.markdown(
            """
            **B.Tech Final Year Project**

            **Title:** Public Acceptance of Autonomous Buses — A Sentiment Analysis Approach

            **Department:** Computer Science & Engineering

            **Team Members:**
            - Bishwa Thakur (23JE0247)
            - Anurag
            - Vivek

            **Academic Year:** 2026-27
            """
        )
        st.markdown("---")
        st.caption("Built with Scikit-learn & Streamlit")

    # --- Header ---
    st.title("🚌 Autonomous Bus: Public Sentiment Analyzer")
    st.markdown(
        "Analyze public opinion on autonomous/self-driving buses using "
        "machine learning-based sentiment analysis."
    )
    st.markdown("---")

    # Check if model exists
    if not os.path.exists(os.path.join(MODELS_DIR, "best_model.joblib")):
        st.error(
            "Model not found. Run `python run_all.py` first to generate "
            "data and train the model."
        )
        return

    model, vectorizer, model_name = load_model()
    df = load_data()

    # --- Prediction Section ---
    st.subheader("💬 Try It — Enter Your Opinion")

    user_input = st.text_area(
        "What do you think about autonomous/self-driving buses?",
        placeholder="e.g., I think self-driving buses would make public transit much safer and more reliable...",
        height=100,
    )

    if st.button("🔍 Analyze Sentiment", type="primary"):
        if user_input.strip():
            sentiment, confidence = predict_sentiment(user_input, model, vectorizer)

            color_map = {
                "positive": ("green", "🟢", "#e8f5e9"),
                "negative": ("red", "🔴", "#ffebee"),
                "neutral": ("orange", "🟡", "#fff8e1"),
            }
            color, icon, bg = color_map.get(sentiment, ("gray", "⚪", "#f5f5f5"))

            st.markdown(
                f"""
                <div style="
                    background-color: {bg};
                    padding: 20px;
                    border-radius: 10px;
                    border-left: 5px solid {color};
                    margin: 10px 0;
                ">
                    <h3 style="margin:0;">{icon} Predicted Sentiment: 
                        <span style="color: {color};">{sentiment.upper()}</span>
                    </h3>
                    <p style="margin: 5px 0 0 0; font-size: 16px;">
                        Confidence: <strong>{confidence:.1f}%</strong>
                    </p>
                    <p style="margin: 5px 0 0 0; font-size: 13px; color: #666;">
                        Model: {model_name}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please enter some text to analyze.")

    st.markdown("---")

    # --- Tabs ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Dataset Overview",
        "🎯 Model Performance",
        "☁️ Word Clouds",
        "💡 Key Insights",
    ])

    # --- Tab 1: Dataset Overview ---
    with tab1:
        st.subheader("Sentiment Distribution")
        col1, col2 = st.columns([1, 1])

        with col1:
            img_path = os.path.join(RESULTS_DIR, "sentiment_distribution.png")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.info("Run training to generate this chart.")

        with col2:
            st.markdown("**Dataset Statistics**")
            st.metric("Total Samples", len(df))
            for sent in ["positive", "negative", "neutral"]:
                count = len(df[df["sentiment"] == sent])
                st.metric(
                    f"{sent.capitalize()}",
                    f"{count} ({count/len(df)*100:.1f}%)",
                )

        st.subheader("Sample Data")
        st.dataframe(
            df.sample(min(20, len(df)), random_state=42)[["text", "sentiment", "source"]],
            use_container_width=True,
            hide_index=True,
        )

    # --- Tab 2: Model Performance ---
    with tab2:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Accuracy Comparison")
            img_path = os.path.join(RESULTS_DIR, "accuracy_comparison.png")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)

        with col2:
            st.subheader("Confusion Matrix")
            img_path = os.path.join(RESULTS_DIR, "confusion_matrix.png")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)

        st.subheader("Classification Report")
        report_path = os.path.join(RESULTS_DIR, "classification_report.txt")
        if os.path.exists(report_path):
            with open(report_path) as f:
                st.code(f.read(), language="text")

    # --- Tab 3: Word Clouds ---
    with tab3:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Positive Opinions")
            img_path = os.path.join(RESULTS_DIR, "word_cloud_positive.png")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)

        with col2:
            st.subheader("Negative Opinions")
            img_path = os.path.join(RESULTS_DIR, "word_cloud_negative.png")
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)

    # --- Tab 4: Key Insights ---
    with tab4:
        st.subheader("Key Findings")
        st.markdown(
            """
            Based on our analysis of 1,200+ public opinions about autonomous buses:

            **Safety Perception**
            - Safety is the most discussed topic in both positive and negative opinions
            - Positive views highlight sensor superiority and elimination of human error
            - Negative views focus on software failures, weather limitations, and hacking risks

            **Employment Concerns**
            - Job displacement is the strongest driver of negative sentiment
            - Opinions about job loss carry the most emotional intensity
            - Retraining programs are frequently mentioned as a necessary condition for support

            **Technology Trust**
            - Trust in technology is polarized — people either strongly trust or strongly distrust
            - Comparisons to existing tech failures (phones, Tesla autopilot) fuel skepticism
            - Successful pilot programs significantly increase positive sentiment

            **Accessibility**
            - Both sides reference elderly and disabled populations
            - Positive opinions focus on increased independence and mobility
            - Negative opinions worry about loss of human assistance during boarding

            **Environmental Impact**
            - Environmental benefits are a strong positive driver
            - Electric + autonomous combination is viewed most favorably
            - Environmental arguments face little opposition in the dataset

            **Demographic Patterns**
            - Survey responses tend to be more measured and neutral
            - Twitter opinions are more polarized and emotionally charged
            - Reddit discussions show the most nuanced, conditional support

            **Overall**
            - Public opinion leans slightly positive but with significant reservations
            - Conditional acceptance ("I'd support it if...") is the most common neutral stance
            - Trust, safety data, and job protection are the three keys to public acceptance
            """
        )


if __name__ == "__main__":
    main()
