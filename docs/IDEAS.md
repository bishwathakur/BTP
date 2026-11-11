# Ideas — Autonomous Bus Project

Brain dump of everything considered, what was chosen, what was dropped, and where the project could go next.

---

## Ideas Explored

### ✅ Chosen: Sentiment Analysis on Autonomous Bus Opinions

ML pipeline that classifies public opinions as positive, negative, or neutral. Synthetic dataset generated to simulate social-media-style comments. TF-IDF + classifier approach — simple, explainable, runs on any laptop.

### ❌ Rejected Ideas

| Idea | Why Dropped |
|------|-------------|
| **Survey-based analysis** | No time to design, distribute, and collect real survey responses before Nov 13 |
| **Social media scraping (Twitter/X, Reddit)** | API restrictions, rate limits, authentication costs; switched to synthetic data instead |
| **Computer vision for bus lane detection** | Needs GPU, labeled image dataset, and hardware — too heavy for a 3-day timeline |
| **Route optimization algorithm** | Interesting but doesn't fit the public acceptance angle the team chose |
| **Chatbot for bus passenger queries** | Not ML-heavy enough to demonstrate as a B.Tech project |
| **Reinforcement learning for bus scheduling** | Scope too large, simulation environment needed |

---

## Future Scope

Mention these in the presentation to show awareness of where the project could grow.

1. **Real-time Twitter/X API integration** — stream live tweets about autonomous buses, classify sentiment on the fly, show a live dashboard
2. **Multilingual support** — extend to Hindi, Tamil, Telugu, and other regional languages using multilingual embeddings
3. **Fine-tune BERT or GPT** — replace TF-IDF with transformer-based models for significantly better accuracy on nuanced text
4. **Mobile app** — let commuters submit feedback on autonomous bus trials, analyze sentiment in real time
5. **Smart city dashboard integration** — feed sentiment scores into city transport authority dashboards alongside ridership data
6. **Longitudinal study** — track how public sentiment changes over months/years as autonomous bus pilots expand
7. **Cross-country comparison** — compare sentiment in India vs. Singapore vs. Europe to understand cultural factors

---

## Key Stats to Mention in Presentation

Use these to ground the discussion in real-world context.

| Stat | Source |
|------|--------|
| Global autonomous bus market projected to reach **$1.3 billion by 2030** | Allied Market Research |
| **62% of people** have safety concerns about driverless vehicles | AAA Survey, 2023 |
| Singapore, Helsinki, and Las Vegas are already running autonomous bus pilots | Various news reports |
| Autonomous buses could save **40–60% in operational costs** | McKinsey & Company |
| India's public transport sector employs **2.5 million+ bus drivers** | Ministry of Road Transport |

---

## Presentation Tips (Internal Notes)

- Lead with the stats — they grab attention
- Demo the Streamlit app live, type a few sample sentences
- Show the word cloud — it is visually striking and easy to explain
- For workforce topic: be balanced — acknowledge job displacement but highlight reskilling opportunities
- For financial topic: use a simple cost comparison table (driver salary vs. autonomous tech cost over 10 years)
- Close with future scope to show the project has legs beyond a college submission
