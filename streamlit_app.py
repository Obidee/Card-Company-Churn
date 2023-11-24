import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')   #setting page layout to wide

#Adding the Dashboard header
st.title("Card Company Attrition Dashboard")
st.write("""
         An overview of the factors impacting the customer attrition of a card company
         within a 12-month period.""")


col1, col2 = st.columns(2)  #arranging the dashboard into 2 columns

with col1:
    st.subheader('Customers by Age Range')
    df = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/Age_range_attr.csv')
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x = 'Age_Range', y = 'Number of Attrited Customers', data = df, ax=ax)
    
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.xlabel('Age Range')
    plt.ylabel('Number of Customers')
    st.pyplot(fig)  # Display the Seaborn plot in Streamlit

with col2:
    st.subheader('Existing vs Attrited Customers by Gender')
    df2 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/attr_vs_exst_cust_bygender.csv')

    # Selecting the columns to use for plotting
    Gender = df2['Gender']
    existing_values = df2['Existing']
    attrited_values = df2['Attrited']

    fig2, ax2 = plt.subplots(figsize=(8, 6))

    bar_width = 0.35  # Width of each bar
    index = range(len(Gender))  # Index for x-axis

    # Plotting bars for 'Existing' values
    existing_bars = plt.bar(index, existing_values, width=bar_width, label='Existing')

    # Plotting bars for 'Attrited' values
    attrited_bars = plt.bar([i + bar_width for i in index], attrited_values, width=bar_width, label='Attrited')

    # Adding labels to each bar
    for bar in existing_bars + attrited_bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')

    # Adding labels and title
    plt.xlabel('Education Level')
    plt.ylabel('Number of Customers')
    plt.xticks([i + bar_width / 2 for i in index], Gender)  # Set x-axis labels
    plt.legend()

    plt.xlabel('Gender')
    plt.ylabel('Number of Customers')
    st.pyplot(fig2)


with col1:
    st.subheader('Average Age of Existing Customers by Gender')
    df3 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/Avg_age_exst_bygender.csv')
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.barplot(x = 'Gender', y = 'Average Customer Age', data = df3, ax=ax3)

    for p in ax3.patches:
        ax3.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.xlabel('Gender')
    plt.ylabel('Average Customer Age')
    st.pyplot(fig3)


with col2:
    st.subheader('Average Age of Attrited Customers by Gender')
    df4 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/Avg_age_attr_bygender.csv')

    fig4, ax4 = plt.subplots(figsize=(8, 6))
    sns.barplot(x = 'Gender', y = 'Average Customer Age', data = df4, ax=ax4)

    for p in ax4.patches:
        ax4.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.xlabel('Gender')
    plt.ylabel('Average Customer Age')
    st.pyplot(fig4)


col1, col2 = st.columns((5.5,4.5))
with col1:
    st.subheader('Existing and Attrited Customers by Education Level')
    df5 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/attr_vs_exst_%attr_byeducation.csv')
    
    # Selecting the columns to use for plotting
    education_levels = df5['Education level']
    existing_values = df5['Existing']
    attrited_values = df5['Attrited']

    # Creating a multiple bar chart using Matplotlib
    fig5, ax5 = plt.subplots(figsize = (15, 8))  # Adjust the figure size if needed

    bar_width = 0.35  # Width of each bar
    index = range(len(education_levels))  # Index for x-axis


    # Plotting bars for 'Existing' values
    existing_bars = plt.bar(index, existing_values, width=bar_width, label='Existing')

    # Plotting bars for 'Attrited' values
    attrited_bars = plt.bar([i + bar_width for i in index], attrited_values, width=bar_width, label='Attrited')

    # Adding labels to each bar
    for bar in existing_bars + attrited_bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')
    # Adding labels and title
    plt.xlabel('Education Level')
    plt.ylabel('Number of Customers')
    plt.xticks([i + bar_width / 2 for i in index], education_levels)  # Set x-axis labels
    plt.legend()

    # Show the plot
    st.pyplot(fig5)

with col2:
    st.subheader('Percentage Attrited by Education Level')
    # Selecting 'Education level' and 'Percentage Attrited' columns for pie plot
    education_levels = df5['Education level']
    percentage_attrited = df5['Percentage_attrited']

    # Creating a pie plot using Matplotlib
    fig5a, ax5a = plt.subplots(figsize=(10, 6))  # Adjust the figure size if needed

    # Exploding the pie slice with the highest attrition
    explode = (0.05, 0, 0, 0, 0, 0, 0)  # Explode the slice with the highest attrition (primary)
    wedgeprops = {'linewidth':10, 'edgecolor':'w'}
    # Plotting the pie chart
    plt.pie(percentage_attrited, labels=education_levels, explode=explode, autopct='%0.1f%%', startangle=140)

    # Show the plot
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    st.pyplot(fig5a)


st.subheader('Existing and Attrited Customers by Marital Status')
df6 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/exst_vs_attr_bymaritalstatus.csv')

# Selecting the columns to use for plotting
marital_status = df6['Marital Status']
existing_values = df6['Existing']
attrited_values = df6['Attrited']

# Creating a multiple bar chart using Matplotlib
fig6, ax6 = plt.subplots(figsize = (15, 6))  # Adjust the figure size if needed

bar_width = 0.35  # Width of each bar
index = range(len(marital_status))  # Index for x-axis


# Plotting bars for 'Existing' values
existing_bars = plt.bar(index, existing_values, width = bar_width, label='Existing')

# Plotting bars for 'Attrited' values
attrited_bars = plt.bar([i + bar_width for i in index], attrited_values, width=bar_width, label='Attrited')

# Adding labels to each bar
for bar in existing_bars + attrited_bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')
# Adding labels and title
plt.xlabel('Marital Status')
plt.ylabel('Number of Customers')
plt.xticks([i + bar_width / 2 for i in index], marital_status)  # Set x-axis labels
plt.legend()

# Show the plot
st.pyplot(fig6)

col1, col2 = st.columns((6,4))
with col1:
    st.subheader('Attrited Customers by Number of Months on Company Books')
    df7 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/Attr_byrelationship.csv')
    fig7, ax7 = plt.subplots(figsize = (15, 8))
    sns.barplot(x = 'Months_on_books_Range', y = 'Attrited', data = df7, ax=ax7)

    for p in ax7.patches:
        ax7.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')
        
    plt.xlabel('Months on Books')
    plt.ylabel('Attrited Customers')
    st.pyplot(fig7)



with col2:
    st.subheader('Average Utilization Percentage')
    df8 = pd.read_csv(r'/Users/mac/Desktop/Projects/Card Company Attrition/Attr_vs_exst_by_Avg_utilization.csv')
    fig8, ax8 = plt.subplots(figsize = (8, 7.5))
    sns.barplot(x = 'Attrition_Flag', y = '%age of average utilization', data = df8, ax=ax8)

    for p in ax8.patches:
        ax8.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.xlabel('Attrition_Flag')
    plt.ylabel('Percentage of average utilization')
    st.pyplot(fig8)


st.subheader("Findings")
st.write("""
         Below are the findings from my analysis of the credit card company data as regards the customer attrition of their card subscription.
         * The vast majority of the card subscribers are between the age of 40-50 years, followed by the 50-60 year olds. Their lowest subscriber demographic is the age range between 20-30 years old.
         * The average age of  the male and female customers are balanced evenly at around 46 years. This is also true for male and female existing customers.
         * The majority of the subscribers are graduates, followed by high school students.
            The risk of attrition is higher among people at the doctoeate level at 18.8%, and is closely followed by the post-graduate level at 15.3%.
         * The risk of leaving the card subscription is highest among customers who have been on the bank's books between 20-50 months.
         * The risk of attrition is lowe among the customers who utilize the card often.""")



