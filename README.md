# Autonomous Bus BTP — Complete Package

**Team:** 3 students | **Presentation:** Nov 13 | **Main demo:** Public Acceptance (Sentiment Analysis ML)

## What's included

- `sentiment_analysis/` — working ML project (data, trained model, results, Streamlit demo)
- `presentation/` — slide content for all 3 topics + speaking notes + references
- `docs/` — project plan, ideas/future scope

## Run demo (fast path)

```bash
cd sentiment_analysis
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501

If you want to regenerate everything from scratch:

```bash
cd sentiment_analysis
python run_all.py
streamlit run app.py
```

## Presentation split

| Student | Topic | Material |
|---|---|---|
| You | Public Acceptance (main) | `presentation/slides_public_acceptance.md`, live Streamlit demo, `results/` charts |
| Teammate 2 | Workforce Alternative | `presentation/slides_workforce_alternative.md` |
| Teammate 3 | Financial Viability | `presentation/slides_financial_viability.md` |

## Demo talking points (your topic)

- 1200+ opinions analyzed (synthetic dataset modeled on Twitter/Reddit/survey)
- TF-IDF + 3 models compared (Naive Bayes, SVM, Random Forest), best model saved
- Show charts in app: sentiment split, accuracy comparison, confusion matrix, word clouds
- Live: type any opinion → instant sentiment + confidence
- Key insight: safety is dominant theme; acceptance often conditional

## Day 2 (Nov 12) checklist

- [ ] Convert `presentation/*.md` to PowerPoint/Google Slides
- [ ] Add screenshots from `sentiment_analysis/results/` into slides
- [ ] Test `streamlit run app.py` on presentation laptop
- [ ] Keep backup screenshots/video of demo
- [ ] Read `presentation/speaking_notes.md` and rehearse (~15 min)

## Notes

- `sentiment_analysis/models/` and `sentiment_analysis/results/` already contain generated outputs.
- References: `presentation/references.md` (verify [18] report ID before final submission).
- Future scope captured in `docs/IDEAS.md`.
