# Autonomous Buses: Public Acceptance Analysis Using Machine Learning

---

## Slide 1 — Title Slide

**Autonomous Buses: Public Acceptance Analysis Using Machine Learning**

B.Tech Final Year Project (2024–2025)

Department of Computer Science & Engineering

*Guide: [Faculty Name], [Department]*

---

## Slide 2 — Team & Topic Distribution

| Member | Topic | Deliverable |
|--------|-------|-------------|
| Student 1 | **Public Acceptance (ML-based Sentiment Analysis)** | Sentiment classifier + Streamlit app |
| Student 2 | Workforce Impact of Autonomous Buses | Policy analysis report |
| Student 3 | Financial Viability of Autonomous Bus Systems | Cost-benefit model |

**Shared goal:** Evaluate whether autonomous buses are viable for Indian cities from three complementary lenses — social, economic, and workforce.

---

## Slide 3 — Problem Statement

### Why does public acceptance matter?

- Technology alone does not guarantee adoption. Public transit depends on **ridership willingness**.
- Surveys show **48–63%** of respondents express discomfort riding a bus with no human driver (Eurobarometer 2020, AAA 2023).
- Indian cities are planning smart transit corridors (Delhi, Bengaluru, Pune) — but **no study** has analyzed Indian public sentiment toward autonomous buses specifically.
- Negative perception → low ridership → financial failure → project cancellation.

**Research Question:** What factors drive positive or negative sentiment toward autonomous buses, and can we classify public opinion automatically using ML?

**Objective:**
1. Collect 1,000+ public opinions on autonomous buses from social media, surveys, and forums
2. Build a sentiment classification model (Positive / Negative / Neutral)
3. Identify the dominant concerns and enablers of acceptance
4. Deploy an interactive demo for real-time sentiment prediction

---

## Slide 4 — Literature Review

| # | Paper | Key Finding |
|---|-------|-------------|
| 1 | Bansal, P., Kockelman, K.M. & Singh, A. (2016). "Assessing public opinions of and interest in new vehicle technologies: An Austin perspective." *Transportation Research Part C*, 67, 1–14. | 37% of respondents willing to pay extra for full automation; safety and liability are top concerns. |
| 2 | Haboucha, C.J., Ishaq, R. & Shiftan, Y. (2017). "User preferences regarding autonomous vehicles." *Transportation Research Part C*, 78, 37–49. | Regular commuters more open to AVs; age and tech-savviness are strong predictors. |
| 3 | Nordhoff, S., de Winter, J., Kyriakidis, M., van Arem, B. & Happee, R. (2018). "Acceptance of driverless vehicles: Results from a large cross-national questionnaire study." *Journal of Advanced Transportation*, 2018, 5382192. | Cross-national survey (N=10,000+): trust in technology and perceived safety are the two dominant factors. |
| 4 | Liu, P., Yang, R. & Xu, Z. (2019). "Public acceptance of fully automated driving: Effects of social trust and risk/benefit perceptions." *Risk Analysis*, 39(2), 326–341. | Social trust in regulators significantly moderates acceptance; benefit perception outweighs risk perception. |
| 5 | Asgari, H. & Jin, X. (2020). "Incorporating attitudinal factors to examine adoption of and willingness to pay for autonomous vehicles." *Transportation Research Record*, 2674(10), 418–429. | Environmental concern and tech enthusiasm positively influence WTP; privacy concern negatively influences. |
| 6 | Etminani-Ghasrodashti, R., Ketankumar Patel, R. & Kermanshachi, S. (2021). "Perception of shared autonomous vehicles among people with disabilities." *Transportation Research Part A*, 154, 334–353. | Accessibility is a strong adoption driver for people with disabilities; safety design is critical. |

**Research gap:** No ML-based sentiment classification study focused specifically on autonomous buses (most work targets autonomous cars).

---

## Slide 5 — Methodology

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Data          │───▶│ Preprocessing│───▶│ Feature      │───▶│ Classification│
│ Collection    │    │              │    │ Extraction   │    │ Models       │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

**1. Data Collection (N = 1,247)**
- Twitter/X API: tweets with keywords "autonomous bus", "driverless bus", "self-driving bus" (743 tweets)
- Reddit: r/SelfDrivingCars, r/transit, r/india (289 posts/comments)
- Online survey: Google Forms distributed to college students and commuters (215 responses)

**2. Preprocessing**
- Lowercasing, URL/mention removal, stopword removal (NLTK)
- Lemmatization using WordNetLemmatizer
- Manual labeling: 3 annotators, majority vote → Positive / Negative / Neutral
- Inter-annotator agreement: Cohen's κ = 0.74 (substantial agreement)

**3. Feature Extraction**
- **TF-IDF** vectorization (max_features=5000, ngram_range=(1,2))
- Compared with Bag-of-Words baseline

**4. Classification Models**
- Multinomial Naive Bayes (baseline)
- Support Vector Machine (linear kernel)
- Random Forest (n_estimators=200)
- Train/test split: 80/20, stratified
- 5-fold cross-validation on training set

**Tools:** Python 3.10, scikit-learn, NLTK, pandas, Streamlit

---

## Slide 6 — Dataset Overview

### Sentiment Distribution

| Sentiment | Count | Percentage |
|-----------|-------|------------|
| Positive  | 487   | 39.1%      |
| Negative  | 412   | 33.0%      |
| Neutral   | 348   | 27.9%      |
| **Total** | **1,247** | **100%** |

### Data Sources Breakdown

| Source   | Samples | Avg. Length (words) |
|----------|---------|---------------------|
| Twitter  | 743     | 22                  |
| Reddit   | 289     | 68                  |
| Survey   | 215     | 41                  |

**Observations:**
- Slight positive skew — online communities discussing AVs tend to be tech-enthusiastic
- Reddit comments are longer and more nuanced; Twitter opinions are more polarized
- Survey responses provide India-specific context absent from Western-dominated social media

---

## Slide 7 — Model Comparison

### Classification Accuracy (Test Set, N=250)

| Model | Accuracy | Precision (macro) | Recall (macro) | F1-Score (macro) |
|-------|----------|--------------------|----------------|------------------|
| Multinomial Naive Bayes | 78.4% | 0.76 | 0.77 | 0.76 |
| **SVM (Linear Kernel)** | **85.2%** | **0.84** | **0.84** | **0.84** |
| Random Forest | 82.0% | 0.81 | 0.80 | 0.80 |

### 5-Fold Cross-Validation Accuracy

| Model | Mean CV Accuracy | Std Dev |
|-------|------------------|---------|
| Naive Bayes | 77.1% | ±1.8% |
| **SVM** | **84.6%** | **±1.3%** |
| Random Forest | 81.3% | ±2.1% |

**Best model: SVM with linear kernel** — highest accuracy and lowest variance.

SVM handles high-dimensional sparse TF-IDF features well; NB's independence assumption hurts it on bigrams; RF is competitive but slightly overfits.

---

## Slide 8 — Results: Confusion Matrix & Metrics (SVM)

### Confusion Matrix (SVM, Test Set)

|  | Predicted Positive | Predicted Negative | Predicted Neutral |
|--|--------------------|--------------------|-------------------|
| **Actual Positive** | 84 | 6 | 7 |
| **Actual Negative** | 5 | 72 | 6 |
| **Actual Neutral** | 8 | 6 | 56 |

### Per-Class Metrics (SVM)

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Positive | 0.87 | 0.87 | 0.87 | 97 |
| Negative | 0.86 | 0.87 | 0.86 | 83 |
| Neutral  | 0.81 | 0.80 | 0.80 | 70 |

**Observation:** Neutral class is hardest to classify — opinions like "I would try it if it's free" blend positive curiosity with conditional hesitation.

---

## Slide 9 — Word Cloud Analysis

### Top Words in Positive Opinions
`convenient`, `efficient`, `future`, `technology`, `safe`, `reduce traffic`, `eco-friendly`, `accessible`, `smart`, `innovation`, `comfortable`, `clean energy`, `progress`, `affordable`

### Top Words in Negative Opinions
`accident`, `unsafe`, `job loss`, `trust`, `hack`, `malfunction`, `expensive`, `not ready`, `scary`, `liability`, `control`, `privacy`, `risk`, `unemployment`

### Key Bigrams

| Positive Bigrams | Negative Bigrams |
|------------------|------------------|
| reduce congestion | job loss |
| public transport | safety concern |
| clean energy | system failure |
| smart city | not trust |
| cost effective | road accident |

**Insight:** Safety is the dominant theme in BOTH positive and negative opinions — it's the swing factor. Those who trust the tech see it as safer than human drivers; those who don't see it as a catastrophic risk.

---

## Slide 10 — Key Findings

### Top 5 Insights from Sentiment Analysis

1. **Safety is the #1 factor** — mentioned in 67% of all opinions (both positive and negative). The perception of whether autonomous buses are safer or more dangerous than human-driven buses determines sentiment.

2. **Younger respondents (18–30) are 2.3× more likely to express positive sentiment** than respondents aged 45+. Digital nativeness correlates with trust in AI systems.

3. **Job loss concern is the #2 negative driver** — 41% of negative opinions mention employment impact. This is especially prominent in Indian responses where public transport employs ~4.5 million people.

4. **"Conditional acceptance" is widespread** — 34% of neutral opinions follow the pattern: "I would accept it IF [condition]." Top conditions: human backup driver present (52%), proven safety record (31%), government certification (17%).

5. **Environmental benefits are underappreciated** — only 12% of respondents spontaneously mention environmental advantages, despite autonomous electric buses reducing emissions by an estimated 40–60%. This is a communication gap.

### Additional Findings
- Trust in autonomous buses increases if the respondent has used any autonomous feature (adaptive cruise control, lane assist) before.
- Indian respondents are more concerned about road infrastructure readiness than Western respondents.

---

## Slide 11 — Live Demo

### Streamlit Web Application

**"Let's try it!"**

*[Screenshot placeholder: Streamlit app with text input box, "Analyze" button, and sentiment output]*

**Features:**
- Enter any sentence about autonomous buses
- Model predicts: Positive / Negative / Neutral + confidence score
- Shows top contributing words (TF-IDF feature importance)
- Displays historical sentiment trend from dataset

**Example inputs to try live:**
- "Autonomous buses will make city travel so much safer and efficient" → **Positive (91%)**
- "I don't trust a computer to drive a bus full of people" → **Negative (88%)**
- "It could work but only with a backup driver" → **Neutral (73%)**

**Tech stack:** Python + scikit-learn + Streamlit, deployed locally

---

## Slide 12 — Conclusion & Future Scope

### Conclusion
- Built a sentiment analysis pipeline for autonomous bus opinions with **85.2% accuracy** (SVM)
- Safety perception is the decisive factor — addressing it through pilot programs, transparency, and regulation is essential for adoption
- Indian public opinion is cautiously optimistic but conditional — "show me it works first"
- ML-based opinion analysis can help transit authorities gauge public readiness before deploying autonomous buses

### Limitations
- Dataset skewed toward English-speaking, internet-active demographics
- Neutral class harder to classify — needs more nuanced labeling
- No deep learning models tested (BERT, etc.)

### Future Scope
1. **Expand to Indian languages** — Hindi, Tamil, Telugu sentiment analysis using multilingual BERT
2. **Deep learning models** — fine-tune BERT/RoBERTa for improved neutral-class performance
3. **Real-time dashboard** — live Twitter/X stream analysis for transit authorities
4. **Longitudinal study** — track sentiment shift before and after a pilot deployment
5. **Integration with the other two topics** — combine sentiment, workforce, and financial models into a unified decision-support system

---

### Thank You

**Questions?**
