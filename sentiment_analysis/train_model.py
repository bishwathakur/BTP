"""
Train and evaluate sentiment analysis models for autonomous bus opinions.
Compares Naive Bayes, SVM, and Random Forest. Saves best model + all results.
"""

import os
import re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
import joblib

# Download NLTK data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

RESULTS_DIR = "results"
MODELS_DIR = "models"


def preprocess_text(text):
    """Lowercase, remove special chars, tokenize, remove stopwords."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)          # urls
    text = re.sub(r"#\w+", "", text)                     # hashtags
    text = re.sub(r"[^a-z\s]", "", text)                 # non-alpha
    text = re.sub(r"\s+", " ", text).strip()             # extra spaces

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


def plot_accuracy_comparison(names, scores):
    """Bar chart comparing model accuracies."""
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ["#2196F3", "#4CAF50", "#FF9800"]
    bars = ax.bar(names, scores, color=colors, edgecolor="black", linewidth=0.5)
    for bar, score in zip(bars, scores):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.005,
            f"{score:.2%}",
            ha="center", va="bottom", fontweight="bold", fontsize=13,
        )
    ax.set_ylabel("Accuracy", fontsize=12)
    ax.set_title("Model Accuracy Comparison", fontsize=14, fontweight="bold")
    ax.set_ylim(0, 1.1)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "accuracy_comparison.png"), dpi=150)
    plt.close()


def plot_confusion_matrix(y_true, y_pred, labels, model_name):
    """Heatmap confusion matrix for the best model."""
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=labels, yticklabels=labels, ax=ax,
        linewidths=0.5, linecolor="gray",
    )
    ax.set_xlabel("Predicted", fontsize=12)
    ax.set_ylabel("Actual", fontsize=12)
    ax.set_title(f"Confusion Matrix — {model_name}", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"), dpi=150)
    plt.close()


def plot_word_clouds(df):
    """Generate word clouds for positive and negative opinions."""
    for sentiment, fname in [("positive", "word_cloud_positive.png"),
                              ("negative", "word_cloud_negative.png")]:
        text = " ".join(df[df["sentiment"] == sentiment]["clean_text"])
        wc = WordCloud(
            width=800, height=400,
            background_color="white",
            colormap="Greens" if sentiment == "positive" else "Reds",
            max_words=100,
            contour_width=1,
            contour_color="steelblue",
        ).generate(text if text.strip() else "no data")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        ax.set_title(
            f"Word Cloud — {sentiment.capitalize()} Opinions",
            fontsize=14, fontweight="bold",
        )
        plt.tight_layout()
        plt.savefig(os.path.join(RESULTS_DIR, fname), dpi=150)
        plt.close()


def plot_sentiment_distribution(df):
    """Pie chart of overall sentiment split."""
    counts = df["sentiment"].value_counts()
    colors = ["#4CAF50", "#F44336", "#FFC107"]
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=counts.index.str.capitalize(),
        autopct="%1.1f%%",
        colors=colors,
        startangle=140,
        textprops={"fontsize": 12},
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )
    for t in autotexts:
        t.set_fontweight("bold")
    ax.set_title(
        "Sentiment Distribution in Dataset",
        fontsize=14, fontweight="bold", pad=20,
    )
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "sentiment_distribution.png"), dpi=150)
    plt.close()


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)

    # --- Load data ---
    print("Loading data...")
    df = pd.read_csv("data/opinions.csv")
    print(f"  {len(df)} samples loaded")

    # --- Preprocess ---
    print("Preprocessing text...")
    df["clean_text"] = df["text"].apply(preprocess_text)

    # --- Vectorize ---
    print("Vectorizing with TF-IDF...")
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = vectorizer.fit_transform(df["clean_text"])
    y = df["sentiment"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"  Train: {X_train.shape[0]}, Test: {X_test.shape[0]}")

    # --- Train models ---
    models = {
        "Naive Bayes": MultinomialNB(),
        "SVM (Linear)": LinearSVC(max_iter=5000, random_state=42),
        "Random Forest": RandomForestClassifier(
            n_estimators=200, random_state=42, n_jobs=-1
        ),
    }

    results = {}
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = {"model": model, "accuracy": acc, "predictions": y_pred}
        print(f"  {name} accuracy: {acc:.4f}")

    # --- Pick best ---
    best_name = max(results, key=lambda k: results[k]["accuracy"])
    best = results[best_name]
    print(f"\nBest model: {best_name} ({best['accuracy']:.4f})")

    # --- Save model + vectorizer ---
    joblib.dump(best["model"], os.path.join(MODELS_DIR, "best_model.joblib"))
    joblib.dump(vectorizer, os.path.join(MODELS_DIR, "vectorizer.joblib"))
    joblib.dump(best_name, os.path.join(MODELS_DIR, "best_model_name.joblib"))
    print(f"Saved model and vectorizer to {MODELS_DIR}/")

    # --- Classification report ---
    labels = sorted(y.unique())
    report = classification_report(y_test, best["predictions"], target_names=labels)
    print(f"\nClassification Report ({best_name}):\n{report}")
    with open(os.path.join(RESULTS_DIR, "classification_report.txt"), "w") as f:
        f.write(f"Best Model: {best_name}\n")
        f.write(f"Accuracy: {best['accuracy']:.4f}\n\n")
        f.write("Classification Report:\n")
        f.write(report)
        f.write("\n\nAll Model Accuracies:\n")
        for name, res in results.items():
            f.write(f"  {name}: {res['accuracy']:.4f}\n")

    # --- Generate plots ---
    print("Generating plots...")
    names = list(results.keys())
    scores = [results[n]["accuracy"] for n in names]

    plot_accuracy_comparison(names, scores)
    print("  accuracy_comparison.png")

    plot_confusion_matrix(y_test, best["predictions"], labels, best_name)
    print("  confusion_matrix.png")

    plot_word_clouds(df)
    print("  word_cloud_positive.png, word_cloud_negative.png")

    plot_sentiment_distribution(df)
    print("  sentiment_distribution.png")

    print(f"\nAll results saved to {RESULTS_DIR}/")
    print("Done!")


if __name__ == "__main__":
    main()
