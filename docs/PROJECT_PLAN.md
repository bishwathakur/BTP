# Project Plan — Autonomous Bus: Multi-Perspective Analysis

## Team

3 members, each owning one topic.

## Topics

| # | Topic | Deliverable |
|---|-------|-------------|
| 1 | **Public Acceptance** (ML-based sentiment analysis) | Working ML pipeline + Streamlit demo |
| 2 | Workforce Alternative | Presentation slides |
| 3 | Financial Viability | Presentation slides |

Topic 1 is the core technical contribution. Topics 2 and 3 provide breadth for the presentation.

---

## Repository Structure

```
H:\BTP\
├── sentiment_analysis/          # ML project (Topic 1)
│   ├── data/                    # Generated / synthetic dataset
│   ├── models/                  # Trained model artifacts
│   ├── results/                 # Charts, metrics, word clouds
│   ├── data_collector.py        # Synthetic data generation
│   ├── train_model.py           # Model training & evaluation
│   ├── app.py                   # Streamlit interactive demo
│   ├── run_all.py               # One-command pipeline runner
│   └── requirements.txt         # Python dependencies
├── presentation/                # Slide content (all 3 topics)
│   ├── slides_public_acceptance.md
│   ├── slides_workforce_alternative.md
│   ├── slides_financial_viability.md
│   ├── speaking_notes.md
│   └── references.md
└── docs/                        # Documentation
    ├── PROJECT_PLAN.md           # ← this file
    └── IDEAS.md
```

---

## Timeline

### Day 1 — Nov 11 (Build)

- [ ] Generate synthetic sentiment dataset (`data_collector.py`)
- [ ] Train ML model, save artifacts (`train_model.py`)
- [ ] Verify accuracy metrics and export charts to `results/`
- [ ] Build Streamlit demo (`app.py`)
- [ ] Test full pipeline end-to-end (`run_all.py`)
- [ ] Draft slide content markdown for all 3 topics

### Day 2 — Nov 12 (Polish)

- [ ] Create PowerPoint / Google Slides from markdown content files
- [ ] Add charts and screenshots from `results/` to slides
- [ ] Practice presentation (aim for 15–20 min total)
- [ ] Dry-run the Streamlit demo on the presentation laptop
- [ ] Prepare backup screenshots in case live demo fails

### Day 3 — Nov 13 (Present)

- [ ] Final check: demo runs, slides load, speaking notes ready
- [ ] Present to professor

---

## How to Run the ML Pipeline

### Prerequisites

- Python 3.8 or newer
- pip (comes with Python)

### Steps

```bash
# 1. Navigate to the ML project folder
cd sentiment_analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline (generate data → train → evaluate → save results)
python run_all.py

# 4. Launch the interactive demo
streamlit run app.py

# 5. Open browser
#    Streamlit will print a URL — typically http://localhost:8501
```

If `streamlit` is not on PATH after install, use `python -m streamlit run app.py`.

---

## What to Show the Professor

1. **Live Streamlit demo** — type a sentence, get sentiment prediction in real time
2. **Training accuracy charts** — precision, recall, F1-score (in `results/`)
3. **Word clouds** — most common positive vs. negative terms
4. **Code walkthrough** — briefly walk through `train_model.py` (model choice, preprocessing, evaluation)
5. **Slides** — cover all 3 topics: public acceptance, workforce impact, financial viability

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Language | Python 3 |
| ML | scikit-learn, pandas, numpy |
| NLP | TF-IDF vectorization |
| Visualization | matplotlib, seaborn, wordcloud |
| Demo | Streamlit |
| Slides | PowerPoint / Google Slides (built from markdown drafts) |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Live demo crashes during presentation | Keep screenshots of every demo screen in `results/` |
| Model accuracy is low on synthetic data | Acceptable for a prototype — mention real-data integration as future work |
| Laptop / projector issues | Export slides to PDF as backup |
