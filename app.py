import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Title
st.title("📊 Customer Churn Dashboard")

# Show raw data checkbox
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Churn count plot
st.subheader("Churn Distribution")
churn_counts = df['Churn'].value_counts()
st.bar_chart(churn_counts)

# Contract vs Churn
st.subheader("Churn by Contract Type")
fig1, ax1 = plt.subplots()
sns.countplot(x='Contract', hue='Churn', data=df, ax=ax1)
st.pyplot(fig1)

# Monthly Charges histogram
st.subheader("Monthly Charges Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(data=df, x='MonthlyCharges', hue='Churn', kde=True, bins=30, ax=ax2)
st.pyplot(fig2)
