# 🤖📈 AI BizScore — Small Business Health & Credit Risk Engine

> 💡 **Know your business health. Understand your risk. See how you can improve it.**

🚀 **Live Demo:** [🔗 Try AI BizScore on Streamlit](PASTE_YOUR_STREAMLIT_APP_LINK_HERE)

---

## 🚨 The Problem

Small businesses can struggle to obtain credit because traditional evaluation may focus heavily on the owner's credit score or limited financial information.

But a business can have a good personal credit score and still be financially unhealthy because of:

- 💸 High operating costs
- 💳 Excessive debt
- 📉 High customer churn
- 📑 Overdue invoices
- 💰 Low profit margins

So the real question is:

> **"Is this business financially healthy enough to handle more credit?"**

---

## 💡 Our Solution

**AI BizScore evaluates the business as a whole.**

The user provides:

💰 Monthly Revenue  
💸 Monthly Operating Costs  
💳 Total Business Debt  
📉 Customer Churn Rate  
👤 Owner Credit Score  
📑 Overdue Pending Invoices  

The application analyzes these factors and produces:

🎯 **Business Health Score**  
🚦 **Financial Risk Rating**  
📊 **Financial KPIs**  
🔍 **Key Risk Drivers**  
📝 **Actionable Recommendations**  
🧪 **What-If Growth Simulation**

---

## 🗂️ Dataset

AI BizScore was developed using a **40,000-record synthetic business dataset** designed to represent different financial and operational conditions of small businesses.

### 📋 Dataset Features

| Feature | What It Means |
|---|---|
| 💰 **Monthly Revenue** | Total money earned by the business each month |
| 💸 **Monthly Operating Costs** | Monthly expenses required to run the business |
| 💳 **Total Business Debt** | Total outstanding debt/loans held by the business |
| 📉 **Customer Churn Rate** | Percentage of customers who stop doing business with the company |
| 👤 **Owner Credit Score** | Creditworthiness of the business owner using a CIBIL/FICO-style score |
| 📑 **Overdue Pending Invoices** | Number of customer invoices that have not been paid on time |
| 🎯 **Risk / Default Class** | Target variable representing the business risk/default category |

### 🔢 Dataset Scale

- 📊 **Total records:** 40,000
- 🧩 **Input features:** 6
- 🎯 **Target:** Business Risk / Default Class
- 🧪 **Test records:** 8,000
- 🔄 **Validation:** 5-Fold Cross-Validation

### ⚖️ Test Set Class Distribution

| Class | Records |
|---|---:|
| 🔴 **Class 0** | 528 |
| 🟢 **Class 1** | 7,472 |
| **Total** | **8,000** |

---

## 🤖 Machine Learning Model

**XGBoost Classifier** is used for business credit/default-risk classification.

### 🔄 Cross-Validation Results

**5-Fold Accuracy Scores:**

`97.81% • 97.99% • 98.05% • 97.78% • 97.74%`

🎯 **Average Cross-Validation Accuracy: 97.87%**

### 📈 Test Set Performance

The model achieved **98% accuracy on 8,000 test records**.

| Metric | Class 0 | Class 1 |
|---|---:|---:|
| 🎯 Precision | 92% | 98% |
| 🔍 Recall | 76% | 100% |
| ⚖️ F1-Score | 83% | 99% |

**Overall Accuracy:** 98%  
**Macro F1-Score:** 91%  
**Weighted F1-Score:** 98%

> 📌 Because the dataset is imbalanced, precision, recall, and F1-score are reported alongside accuracy instead of relying on accuracy alone.

---

## 📊 Business Health Score

The application converts the business condition into a simple **5–98 health score**:

🟢 **PRIME — 70+**  
🟡 **MODERATE — 45–69**  
🔴 **HIGH RISK — Below 45**

The dashboard also calculates:

💰 Monthly Profit  
📈 Profit Margin  
💳 Debt-to-Revenue Ratio

---

## 🔍 Explainable AI

AI BizScore doesn't just give a prediction.

It uses **feature-importance analysis** to show which business factors have the strongest influence on the machine learning evaluation.

This makes the result easier for a non-technical business owner to understand.

---

## 📝 Smart Recommendations

The application provides actionable guidance based on the business condition:

✂️ Reduce unnecessary operating costs  
💵 Improve invoice collection  
❤️ Improve customer retention  
💳 Consider debt restructuring  
🛡️ Build a cash buffer

---

## 🧪 What-If Growth Simulator

Users can test possible business improvements before making real decisions.

For example:

> **"What happens if I reduce my monthly costs?"**

The simulator allows users to experiment with:

- ✂️ Monthly cost reduction
- 📉 Customer churn reduction
- 📑 Clearing overdue invoices

The application then recalculates the **Business Health Score** and shows the potential improvement.

---

## 🌐 Deployment

The complete application is built with **Streamlit** and deployed as an interactive web application.

Users can enter business information directly into the dashboard and receive the analysis in real time.

🚀 **Live Application:** [🔗 Open AI BizScore](PASTE_YOUR_STREAMLIT_APP_LINK_HERE)

---

## 🛠️ Tech Stack

🐍 **Python**  
📊 **Pandas • NumPy**  
🤖 **Scikit-learn • XGBoost**  
🔍 **SHAP**  
📈 **Matplotlib • Seaborn**  
🌐 **Streamlit**  
💾 **Joblib**

---

## 🎯 In One Line

**AI BizScore answers three simple questions:**

📊 **How healthy is my business?**  
⚠️ **What is causing the risk?**  
🚀 **What can I change to improve it?**

---

> ⚠️ **Disclaimer:** This project uses synthetic data and is a prototype decision-support system. The reported metrics demonstrate performance on the prepared dataset and should not be interpreted as proof of real-world lending accuracy.
