# Task 04 – Descriptive Statistics System (Pure Python, Pandas, Polars)

This is my submission for Task 04, where the goal was to build a flexible system that can generate descriptive statistics for **any CSV dataset** — not just the 2024 US election files. I focused on making all three scripts reusable, neutral, and smart enough to handle unknown column names and formats.

---

## 📂 What's Included

- `pure_python_stats.py`  
  → No external libraries. Everything from scratch using built-in Python. Took the longest but helped me understand the core logic (mean, std, frequency counts).

- `pandas_stats.py`  
  → Uses `pandas.describe()`, `.value_counts()`, and `.groupby()` for quick and readable stats. I added logic to detect grouping columns dynamically if needed.

- `polars_stats.py`  
  → Fastest and cleanest. Works well with large files. Auto-detects numeric and categorical columns and handles optional grouping safely.

---

## 🚀 How to Run

Make sure you have Python installed, then run any of the scripts from terminal or Jupyter.

```bash
# Pure Python version
python pure_python_stats.py your_file.csv

# Pandas version
python pandas_stats.py your_file.csv

# Polars version
python polars_stats.py your_file.csv
