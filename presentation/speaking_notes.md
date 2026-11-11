# Speaking Notes — Public Acceptance Presentation

**Total time target: 15 minutes**
**Audience: Faculty panel + students**

---

## Opening (Before Slide 1) — 30 seconds

**Hook:** "Imagine you're at a bus stop tomorrow morning, and the bus that pulls up has no driver. Would you get on? That hesitation you just felt — that's exactly what our project is about."

---

## Slide 1 — Title (30 seconds)

- Introduce yourself and the project title
- "Our project looks at autonomous buses from three angles. My focus is on the human side — will people actually ride these buses?"

---

## Slide 2 — Team & Topics (30 seconds)

- Briefly name your teammates and their topics
- "I'll present the main topic — sentiment analysis — and my teammates will be available for questions on workforce and financial viability."
- Emphasize: "These three topics are connected. Public acceptance drives ridership, ridership determines revenue, and revenue determines whether the workforce transition is funded."

---

## Slide 3 — Problem Statement (1.5 minutes)

- Start with the statistic: "Nearly half of people surveyed globally say they would NOT ride a driverless bus. That's a problem if you're a city planning to invest hundreds of crores."
- Explain: technology readiness ≠ public readiness
- Mention Indian context: "India is investing in smart cities and electric buses. Autonomy is the next step — but nobody has asked Indian commuters what they think."
- State the research question clearly

---

## Slide 4 — Literature Review (1.5 minutes)

- Don't read every paper — pick 2–3 key ones
- "Bansal and Kockelman found that safety and liability are the top concerns — this was in 2016 and it's still true"
- "Nordhoff's massive 10,000-person survey confirmed that trust in the technology is THE deciding factor"
- End with: "What's missing is an ML-based approach to analyzing opinions at scale, especially for buses specifically — most work is on autonomous cars"

---

## Slide 5 — Methodology (2 minutes)

- Walk through the pipeline: collect → clean → extract features → classify
- Emphasize scale: "We collected over 1,200 opinions from three sources"
- Explain TF-IDF briefly: "It converts text into numbers by weighing how important each word is — common words get low weight, distinctive words get high weight"
- Mention the three models and why you chose them: "NB is our baseline, SVM is strong on text, RF is our ensemble option"
- Don't spend too long here — the panel will ask details in Q&A

---

## Slide 6 — Dataset (1 minute)

- Highlight the distribution: "Slightly more positive than negative — which makes sense because people discussing autonomous vehicles online tend to be tech-interested"
- Point out Reddit vs Twitter: "Reddit gives us nuance — longer, more reasoned opinions. Twitter gives us volume and raw sentiment."
- Mention the survey: "The survey is important because it includes people who wouldn't normally post about autonomous buses online — everyday commuters"

---

## Slide 7 — Model Comparison (1.5 minutes)

- Lead with the winner: "SVM gave us the best accuracy at 85.2%"
- Explain briefly why: "SVM handles the high-dimensional, sparse feature space of TF-IDF very well"
- Note: "NB at 78% — decent baseline but its assumption that words are independent hurts it. Random Forest at 82% — competitive but slightly overfits on our dataset size"
- Mention cross-validation: "These aren't lucky splits — 5-fold CV confirmed SVM is consistently the best"

---

## Slide 8 — Results (1 minute)

- Point to the confusion matrix: "The model does well on positive and negative — the struggle is with neutral"
- Explain why neutral is hard: "Statements like 'I'd try it if it's free' are genuinely ambiguous — positive curiosity with negative conditions"
- This is an honest limitation — the panel appreciates acknowledging it

---

## Slide 9 — Word Clouds (1 minute)

- "The most striking finding: safety appears in BOTH positive and negative opinions"
- "People who trust the tech say autonomous buses are SAFER. People who don't say they're DANGEROUS. Same concern, opposite conclusions."
- Mention job loss: "The second biggest negative theme — connects directly to my teammate's workforce analysis"

---

## Slide 10 — Key Findings (1.5 minutes)

- Go through findings 1, 2, and 4 — these are the most interesting
- Finding 1 (safety): "This tells transit authorities: your #1 marketing job is proving safety"
- Finding 2 (age): "This suggests starting deployment in tech-savvy areas — university campuses, IT parks"
- Finding 4 (conditional acceptance): "People aren't saying NO — they're saying NOT YET. That's actually encouraging."

---

## Slide 11 — Live Demo Transition (1.5 minutes)

**Transition line:** "Numbers and graphs are one thing — let me show you the model working in real time."

- Open the Streamlit app (have it running before the presentation starts)
- Type a positive example first: "Autonomous buses will reduce accidents and make travel easier" → show the Positive prediction
- Then a negative one: "I will never trust a machine to drive my children to school" → show the Negative prediction
- Invite a panel member: "Would anyone like to type a sentence and see what the model predicts?"
- If the model gets one wrong, don't panic: "And that's exactly the kind of edge case that shows where the model has room to improve"

**Backup:** If the app crashes or doesn't load, have screenshots ready in the slides. Say: "Let me show you pre-captured examples instead."

---

## Slide 12 — Conclusion (1 minute)

- Summarize in one line: "We built an 85% accurate sentiment classifier and found that safety perception is the make-or-break factor for autonomous bus adoption"
- Future scope: pick ONE — "The most impactful next step would be extending this to Indian languages"
- End: "Thank you. Happy to take questions."

---

## Q&A Preparation — Common Questions & Answers

### Q: "Why not use deep learning / BERT?"
**A:** "Good question. We tested TF-IDF + classical ML first because our dataset is ~1,200 samples. BERT typically needs 5,000+ samples to outperform classical models on specialized domains. We mention fine-tuning BERT as future scope — it would especially help with the neutral class."

### Q: "How did you ensure labeling quality?"
**A:** "Three annotators independently labeled each sample, and we used majority voting. Our inter-annotator agreement (Cohen's kappa) was 0.74, which is 'substantial agreement' by standard benchmarks. Ambiguous cases were discussed and resolved."

### Q: "Is 1,200 samples enough?"
**A:** "For classical ML with TF-IDF, yes — published studies in sentiment analysis have achieved good results with 1,000–2,000 samples. Our 5-fold CV results are stable (low standard deviation), which suggests the dataset size is adequate for these models. Scaling up would primarily help deep learning approaches."

### Q: "This is mostly Western data. How relevant is it to India?"
**A:** "Valid concern. 215 of our 1,247 samples are from an Indian survey. We found Indian respondents emphasize infrastructure readiness and job loss more than Western respondents. A full India-focused study in Hindi and regional languages would be a valuable extension."

### Q: "What's the practical application?"
**A:** "A transit authority planning to introduce autonomous buses can use this tool to gauge public readiness — feed in social media data from their city and get a sentiment breakdown. It can also identify specific concerns to address in public communication campaigns."

### Q: "Why buses specifically, not autonomous cars?"
**A:** "Autonomous cars are a personal choice — you can opt out. Autonomous buses are a public service — you can't choose your driver. The acceptance bar is higher, and the stakeholder set is different (includes non-users, workers, regulators). That makes it a richer problem."

---

## Timing Summary

| Slide | Topic | Time | Cumulative |
|-------|-------|------|------------|
| Opening + 1 | Hook + Title | 1:00 | 1:00 |
| 2 | Team | 0:30 | 1:30 |
| 3 | Problem | 1:30 | 3:00 |
| 4 | Literature | 1:30 | 4:30 |
| 5 | Methodology | 2:00 | 6:30 |
| 6 | Dataset | 1:00 | 7:30 |
| 7 | Model Comparison | 1:30 | 9:00 |
| 8 | Results | 1:00 | 10:00 |
| 9 | Word Clouds | 1:00 | 11:00 |
| 10 | Key Findings | 1:30 | 12:30 |
| 11 | Live Demo | 1:30 | 14:00 |
| 12 | Conclusion | 1:00 | 15:00 |

**Buffer:** If running long, compress slides 4 (literature) and 6 (dataset) — these are supporting detail the panel can read.

---
