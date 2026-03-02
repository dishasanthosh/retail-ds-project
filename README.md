# retail-ds-project
Retail Customer Intelligence & Revenue Analytics


📌 Project Overview

Retail businesses must proactively manage customer churn, optimize marketing strategy, and forecast revenue to remain competitive.

This project builds an end-to-end retail analytics system using 500K+ transactional records to:

Predict customer churn

Segment customers into behavioral cohorts

Forecast monthly revenue

Quantify business impact

The project demonstrates full lifecycle data science: data engineering → feature engineering → modeling → evaluation → explainability → business translation.

📊 Dataset

541,909 raw retail transactions

8 original features (InvoiceNo, CustomerID, InvoiceDate, Quantity, UnitPrice, etc.)

After cleaning: 397,884 valid transactions

~4,300 unique customers

Data Cleaning Steps

Removed missing CustomerID entries

Removed product returns (negative quantities)

Removed invalid pricing

Engineered revenue feature (TotalPrice = Quantity × UnitPrice)

🧠 Feature Engineering

Customer-level behavioral features engineered:

Recency – Days since last purchase

Frequency – Number of unique purchases

Monetary – Total spending

Tenure – Customer lifespan

Average Order Value

Frequency Rate – Orders per active day

Revenue Per Day

These features capture customer engagement, loyalty, value, and intensity of purchasing behavior.

🔮 Churn Prediction Model
 Target Definition

Churn defined as:

No purchase within 90 days

This converts transactional data into a supervised classification problem.

 Model

Random Forest Classifier

Stratified train/test split

Threshold tuning for recall optimization

  Performance

ROC-AUC: ~0.75

Accuracy: ~0.68

Precision (churn): ~0.52

Recall (churn): ~0.44

Performance is realistic and avoids data leakage.

🔍 Model Explainability (SHAP)

SHAP analysis identified the strongest drivers of churn:

Tenure (most important)

Monetary value

Engagement rate (FrequencyRate)

Key Insight

Long-tenure customers exhibit significantly lower churn risk

High-spending customers are more stable

Low engagement strongly increases churn probability

This aligns with retail behavioral theory.

👥 Customer Segmentation

Applied KMeans clustering with standardized behavioral features.

Identified 4 segments:

Segment	Description	Churn Rate
Loyal Customers	High spend, long tenure, frequent buyers	~13%
New Customers	Short tenure, recent purchase	~22%
Inactive / Low Value	Low engagement, long inactivity	~100%
Wholesale Outlier	Single extreme bulk buyer	100%
Business Implication

Protect Loyal segment with loyalty incentives

Target New segment with onboarding campaigns

Evaluate ROI before targeting fully churned segments

📈 Revenue Forecasting

Aggregated monthly revenue

Created lag-based time-series features

Benchmarked Random Forest against naive forecast

Due to limited historical coverage (~12 months), forecasting performance is moderate, highlighting the importance of historical depth in time-series modeling.

💼 Business Impact

This system enables:

Proactive churn prevention

Revenue-at-risk estimation

Segment-specific marketing strategies

Data-driven planning

🛠 Technologies Used

Python

pandas

scikit-learn

SHAP

matplotlib / seaborn

KMeans Clustering

Random Forest

Time-series feature engineering

🗂 Project Structure
data/
notebooks/
  01_cleaning.ipynb
  02_feature_engineering.ipynb
  03_churn_model.ipynb
  04_segmentation.ipynb
  05_forecasting.ipynb
src/
README.md
requirements.txt
🎓 Key Learnings

Feature engineering drives model performance more than algorithm complexity

Preventing data leakage is critical in churn modeling

Simple baselines are essential in time-series evaluation

Model explainability strengthens business trust

🚀 Future Improvements

Multi-year revenue forecasting

Uplift modeling for retention campaigns

Automated feature pipelines

Deployment via Streamlit dashboard
