# 🚌 Public Acceptance of Autonomous Buses — Sentiment Analysis

**B.Tech Final Year Project (BTP)**

A machine learning-based sentiment analysis system that analyzes public opinion on autonomous/self-driving buses. Built with Scikit-learn for ML and Streamlit for the interactive demo.

## Overview

This project collects and analyzes public opinions about autonomous buses from simulated social media and survey data. It trains multiple ML models (Naive Bayes, SVM, Random Forest) to classify opinions as positive, negative, or neutral, and provides an interactive web dashboard for real-time sentiment prediction.

## Project Structure

```
sentiment_analysis/
├── data/                    # Generated dataset
│   └── opinions.csv
├── models/                  # Trained model + vectorizer
│   ├── best_model.joblib
│   ├── best_model_name.joblib
│   └── vectorizer.joblib
├── results/                 # Charts and reports
│   ├── accuracy_comparison.png
│   ├── confusion_matrix.png
│   ├── classification_report.txt
│   ├── sentiment_distribution.png
│   ├── word_cloud_positive.png
│   └── word_cloud_negative.png
├── data_collector.py        # Synthetic dataset generator
├── train_model.py           # Model training and evaluation
├── app.py                   # Streamlit web app
├── run_all.py               # One-click pipeline runner
├── requirements.txt
└── README.md
```

## Installation

```bash
# Clone or navigate to the project directory
cd sentiment_analysis

# Install dependencies
pip install -r requirements.txt
```

## Usage

### 1. Run the full pipeline (recommended)

```bash
python run_all.py
```

This generates the dataset, trains all models, and saves results.

### 2. Run steps individually

```bash
python data_collector.py     # Generate synthetic dataset
python train_model.py        # Train and evaluate models
```

### 3. Launch the interactive demo

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Features

- **Synthetic Dataset**: 1,200+ realistic opinions with typos, slang, and emoji — mimicking Twitter, Reddit, and survey responses
- **Three ML Models**: Naive Bayes, SVM (Linear), Random Forest — compared on accuracy
- **TF-IDF Vectorization**: Unigram + bigram features (up to 5,000)
- **Interactive Dashboard**: Real-time sentiment prediction with confidence scores
- **Visualizations**: Accuracy comparison, confusion matrix, word clouds, sentiment distribution

## Screenshots

*(Add screenshots of the Streamlit app here after running it)*

## Results

After training, check `results/classification_report.txt` for detailed metrics. The best-performing model is automatically selected and saved.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| ML | Scikit-learn |
| NLP | NLTK, TF-IDF |
| Visualization | Matplotlib, Seaborn, WordCloud |
| Web App | Streamlit |
| Data | Pandas, NumPy |

## Team Members

| Name | Roll No. |
|------|----------|
| Student 1 | XXXXXXXXX |
| Student 2 | XXXXXXXXX |
| Student 3 | XXXXXXXXX |

**Project Guide:** Prof. [Name]

## License

Academic project — not for commercial use.
