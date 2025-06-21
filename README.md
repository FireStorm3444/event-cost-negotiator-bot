# Event Cost Estimation & Negotiation Bot

Welcome to my submission for the UtsavAi Internship Round 1 project. This logic-based bot estimates the cost of an event based on selected services and simulates negotiation using smart pricing logic with mock data.

---

## Problem Statement

> Event organizers often struggle with budget estimation and vendor negotiation. This tool aims to automate:
- Total event cost estimation
- Negotiation based on vendor flexibility and booking conditions

---

## Features

- Estimates base event cost using mock pricing data
- Applies per-service discounts based on flexibility
- Calculates global discounts (Early Booking, Off-season, Combo)
- Generates a final negotiated cost breakdown
- Fully logic-driven, no AI APIs used

---

## Services Available

- Venue
- Catering (Rs.600 per guest)
- Photography
- Decoration
- DJ

Each service has mock pricing and a “flexibility” score that simulates how open vendors are to negotiation.

---

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/event-cost-negotiator-bot.git
cd event-cost-negotiator-bot
```
2. Run the Jupyter notebook:
```bash
jupyter notebook sample_run.ipynb
```
---
## Notes
All data used is mock-only

No AI APIs were used (per rules)

Focused on logic, structure, and clarity

---
Feel free to explore, test, and suggest improvements!