# Presentation Script & Runbook
**Project:** Autonomous Bus — Multi-Perspective Analysis  
**Date:** 13 Nov 2026  
**Duration:** ~15 minutes + Q&A

## Team & Roles
| Name | Topic | Speaks |
|---|---|---|
| **Bishwa Thakur** | Public Acceptance (ML Sentiment Analysis) | Main presenter (Slides 1–12 + live demo) |
| **Anurag** | Workforce Alternative | Slide 13 (brief) + Q&A on workforce |
| **Vivek** | Financial Viability | Slide 14 (brief) + Q&A on finance |

> If faculty expects 3 separate mini-presentations, use the topic-specific slides in `slides_workforce_alternative.md` and `slides_financial_viability.md`. If one integrated flow is preferred, Bishwa presents the ML core and hands off for 1 slide each.

---

## Before Presentation (Nov 12 / morning of Nov 13)
1. **Test demo machine**
   - Open terminal in `H:\BTP\sentiment_analysis`
   - Run: `pip install -r requirements.txt` (if needed)
   - Run: `streamlit run app.py`
   - Confirm browser opens at `http://localhost:8501`
   - Test 2 inputs:
     - Positive: `Autonomous buses will make travel safer and more reliable`
     - Negative: `I do not trust a bus without a driver`
2. **Prepare backup (important)**
   - Keep screenshots of: app home, prediction result, accuracy chart, confusion matrix, word clouds
   - Keep `results/*.png` open in a folder as fallback
3. **Slides**
   - Build PowerPoint/Google Slides from:
     - `slides_public_acceptance.md` (main)
     - `slides_workforce_alternative.md` (1 summary slide or full 6)
     - `slides_financial_viability.md` (1 summary slide or full 6)
   - Add Bishwa/Anurag/Vivek names on title/team slide
4. **Practice**
   - 1 full run-through with timer (target 15 min)
   - Practice demo transition and backup line

---

## On-Stage Setup (2 minutes before start)
1. Laptop connected, slides open in present mode.
2. Streamlit app already running in background tab (`localhost:8501`).
3. `results/` folder open as backup.
4. Water/notes ready. Mic checked.

---

## Presentation Flow (Step-by-Step Script)

### 0:00–0:30 — Opening Hook (Bishwa)
**Say:**  
"Good morning respected faculty and everyone. I'm **Bishwa Thakur**, and with my teammates **Anurag** and **Vivek**, we worked on *Autonomous Buses — Multi-Perspective Analysis*.  
Imagine tomorrow a bus arrives at your stop with no driver. Would you board it? That hesitation is exactly what we studied."

**Action:** Title slide on screen.

---

### 0:30–1:00 — Team & Topic Split (Bishwa)
**Say:**  
"Our project has three perspectives: I worked on **Public Acceptance using Machine Learning and sentiment analysis** with a working demo. **Anurag** covers **Workforce Alternative** — impact on drivers and new roles. **Vivek** covers **Financial Viability** — costs, savings, and ROI. Together this answers: will people accept it, what happens to jobs, and does it make financial sense?"

**Action:** Team slide.

---

### 1:00–2:30 — Problem Statement (Bishwa)
**Say:**  
"Autonomous bus technology is advancing fast, but adoption depends on public trust. If people don't feel safe, ridership drops and projects fail. Our question: what drives positive or negative public opinion on autonomous buses, and can we classify it automatically using ML?"

**Action:** Problem statement slide. Emphasize safety, trust, adoption.

---

### 2:30–4:00 — Literature / Gap (Bishwa)
**Say:**  
"Prior studies show safety, trust, and liability are top concerns in autonomous vehicle acceptance. Most existing work focuses on cars, not buses, and many are survey-only. Our contribution: an ML-based sentiment pipeline on 1,200+ opinions to quantify acceptance signals at scale."

**Action:** Literature slide. Mention 2-3 key papers only (don't read all).

---

### 4:00–6:00 — Methodology (Bishwa)
**Say:**  
"Pipeline: collected 1,200+ opinions (synthetic dataset modeled on Twitter/Reddit/survey) → preprocessing (cleaning, tokenization, stopword removal) → TF-IDF features (uni+bi-grams) → trained and compared three models: Naive Bayes, Linear SVM, Random Forest → evaluated with accuracy, precision/recall/F1, confusion matrix. Best model deployed in a Streamlit app for live prediction."

**Action:** Methodology diagram/slide.

---

### 6:00–7:00 — Dataset Overview (Bishwa)
**Say:**  
"Dataset includes positive, negative, and neutral opinions covering safety, convenience, jobs, environment, cost, and accessibility. Distribution and samples are shown here — this mix helps the model learn realistic language patterns."

**Action:** Dataset/distribution slide or app Tab 1 screenshot.

---

### 7:00–8:30 — Model Comparison & Results (Bishwa)
**Say:**  
"We compared Naive Bayes, SVM, and Random Forest. SVM performed best on this dataset. Here are the accuracy comparison and confusion matrix. Neutral opinions are hardest because they often contain conditions like 'I'd use it if there's a backup driver' — mixed signals."

**Action:** Accuracy + confusion matrix charts (`results/accuracy_comparison.png`, `results/confusion_matrix.png`).

---

### 8:30–9:30 — Word Clouds & Insights (Bishwa)
**Say:**  
"Word clouds show what drives sentiment. Safety appears in both positive and negative opinions — same concern, opposite conclusions. Job loss is a strong negative driver, while efficiency, accessibility, and environment appear in positive opinions."

**Action:** Word cloud slide/images.

---

### 9:30–10:30 — Key Findings (Bishwa)
**Say:**  
"Key findings: 1) Safety perception is the deciding factor. 2) Acceptance is often conditional, not absolute rejection. 3) Workforce concerns strongly influence negativity — linking to Anurag's topic. 4) Clear communication and proven pilots can improve trust."

**Action:** Key findings slide.

---

### 10:30–12:00 — Live Demo (Bishwa) **[Most important]**
**Say (transition):**  
"Now let me show this working live."

**Steps:**
1. Switch to Streamlit app tab.
2. Show title/sidebar briefly: "This is our sentiment analyzer for autonomous bus opinions."
3. Enter positive example:  
   `Autonomous buses will reduce accidents and make public transport more reliable.`  
   Click **Analyze Sentiment** → show result/confidence.
4. Enter negative example:  
   `I don't feel safe riding a bus without a human driver.`  
   → show result.
5. (Optional) Invite faculty: "Would you like to test a sentence?"
6. Quickly show one tab (Model Performance or Word Clouds) if time permits.
7. Switch back to slides.

**Backup if demo fails:**  
"Due to setup constraints I'll show captured results." → open `results/` screenshots/charts and explain same flow.

---

### 12:00–12:45 — Workforce Alternative (Anurag)
**Say (Anurag):**  
"I'm **Anurag**. Autonomous buses may reduce demand for traditional driving roles but create new roles in monitoring, fleet operations, maintenance, and safety supervision. Evidence from pilot cities shows transition works best with reskilling programs and phased deployment rather than sudden replacement."

**Action:** Workforce summary slide (use `slides_workforce_alternative.md`).

---

### 12:45–13:30 — Financial Viability (Vivek)
**Say (Vivek):**  
"I'm **Vivek**. Financial viability depends on high upfront vehicle/infra cost versus long-term savings in labor and optimized operations. Break-even is possible over time in high-utilization routes, but infrastructure, regulation, and maintenance costs are major risks."

**Action:** Financial summary slide (use `slides_financial_viability.md`).

---

### 13:30–14:30 — Conclusion & Future Scope (Bishwa)
**Say:**  
"To conclude: autonomous bus adoption is not just a technology problem — it's trust, jobs, and economics. Our ML model achieved strong performance for sentiment classification and gave actionable insights, especially around safety concerns. Future work: real-time social media data, multilingual (Hindi/regional) support, transformer models like BERT, and integration with workforce/finance decision models. Thank you."

**Action:** Conclusion slide.

---

### 14:30–15:00 — Q&A Handoff (All)
**Bishwa says:**  
"We're happy to take questions."

**Who answers:**
- ML/model/demo/data/questions on acceptance → **Bishwa**
- Jobs, drivers, reskilling, case studies → **Anurag**
- Costs, ROI, market, feasibility → **Vivek**

---

## Quick Q&A Prep (short answers)
- **Why SVM?** Best accuracy and stable on high-dimensional TF-IDF features for our dataset size.
- **Is data real?** Synthetic dataset modeled on realistic public opinions (Twitter/Reddit/survey style) due to time/API limits; pipeline supports real data later.
- **Why not BERT?** Time/compute constraints; classical ML gives fast, explainable baseline. BERT is future scope.
- **Can neutral be wrong?** Yes, neutral is hardest due to conditional/mixed statements; visible in confusion matrix.
- **How is this useful?** Helps transit planners measure public concerns before deployment and target communication/safety pilots.

## Emergency Lines
- Demo slow/crash: "I'll show the saved outputs — the trained model and charts are already generated." (open `results/`)
- Forgot stat: "I don't have the exact figure right now, but the trend in our analysis shows…" (stay honest, don't invent)
- Tough question outside scope: "That's outside our current scope, but it's a strong direction for future work."
