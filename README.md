# 🥑 What's in an Avocado Toast?

## A Supply Chain Analysis Using Open Food Facts


## 📌 Project Overview

Avocado toast may look simple, but its ingredients travel across continents before reaching your plate. In this project, I analyzed the **global supply chain** behind three key ingredients used in making avocado toast in the United Kingdom:

* Avocado
* Olive Oil
* Sourdough Bread

Using data from the **Open Food Facts** database, this project uncovers where these ingredients most commonly originate and highlights the hidden complexity of everyday food systems.

---

## 🎯 Objective

To determine the **most common country of origin** for each ingredient by:

* Filtering relevant food categories
* Cleaning and transforming raw data
* Analyzing origin frequency

---

## 🗂️ Dataset Description

Each ingredient includes:

* A `.csv` file containing product-level data
* A `.txt` file listing **relevant category tags**

### Key Columns Used:

* `product_name_en` – Product name
* `categories_tags` – Food classification tags
* `countries` – Country of sale
* `origins_tags` – Country of origin

---

## ⚙️ Methodology

### 1. Data Loading

* Imported datasets using **pandas**
* Loaded relevant category filters from text files

### 2. Data Cleaning

* Selected only necessary columns
* Split `categories_tags` into lists
* Removed missing or irrelevant entries

### 3. Filtering

* Retained only rows matching relevant categories
* Focused exclusively on products sold in the **United Kingdom**

### 4. Analysis

* Counted frequency of `origins_tags`
* Extracted the most common origin
* Cleaned text (removed prefixes like `en:` and hyphens)

---

## 🧠 Key Results

| Ingredient   | Top Country of Origin |
| ------------ | --------------------- |
| 🥑 Avocado   | **Peru**              |
| 🫒 Olive Oil | **Greece**            |
| 🍞 Sourdough | **United Kingdom**    |

---

## 🔍 Insights & Interpretation

### 🌍 1. Global vs Local Supply Chains

* **Avocados (Peru)** → Highly globalized supply chain

  * Peru is one of the world’s leading avocado exporters
  * Indicates reliance on imports for fresh produce

* **Olive Oil (Greece)** → Regional specialization

  * Mediterranean countries dominate olive oil production
  * Reflects climate dependency of certain crops

* **Sourdough (United Kingdom)** → Local production

  * Bread is largely produced domestically
  * Suggests shorter, more resilient supply chains

---

### 🚢 2. Hidden Complexity in Simple Meals

Even a “simple” avocado toast involves:

* Cross-continental sourcing (South America → Europe)
* Agricultural specialization
* Logistics and distribution networks

---

### 🌱 3. Sustainability Considerations

* Imported ingredients (like avocados) may have a **higher carbon footprint**
* Locally sourced items (like sourdough) are typically more sustainable
* This opens opportunities for:

  * Supply chain optimization
  * Ethical sourcing strategies

---

### 📊 4. Data Challenges & Observations

* Many products contain **multiple category tags**, requiring careful filtering
* Missing or inconsistent origin data needed cleaning
* Standardizing text (e.g., removing `"en:"`) was crucial for accurate analysis

---

## 🛠️ Tech Stack

* **Python**
* **Pandas** for data manipulation
* Text processing for cleaning and filtering

---

## 📁 Project Structure

```
├── data/
│   ├── avocado.csv
│   ├── olive_oil.csv
│   ├── sourdough.csv
│   ├── relevant_avocado_categories.txt
│   ├── relevant_olive_oil_categories.txt
│   ├── relevant_sourdough_categories.txt
│
├── notebook.ipynb / script.py
└── README.md
```

---

## 🚀 Future Improvements

* Analyze **transport distances & carbon emissions**
* Include additional ingredients (e.g., lemons, salt)
* Build a **data visualization dashboard**
* Compare supply chains across different countries

---

## 💡 Conclusion

This project demonstrates how **data analysis can uncover the global journey behind everyday foods**.

A single dish like avocado toast reflects:

* International trade dependencies
* Regional agricultural strengths
* Opportunities for more sustainable consumption

---

## 📬 Let's Connect

If you're interested in data analytics, supply chain insights, or similar projects, feel free to connect or explore more of my work!

---
