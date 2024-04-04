import pandas as pd
import numpy as np
from scipy import stats
import streamlit as st

# Liblaries for Visualization
import matplotlib.pyplot as plt
import seaborn as sns



def graph():
  # Load Data
  copy_df = pd.read_csv('BankChurners.csv')


  # Set Web Title
  st.title("EXPLORATORY DATA ANALYSIS (EDA)")


  # Divider
  st.markdown('--------------')

  #Show dataframe
  st.dataframe(copy_df)


  # Divider 1
  st.markdown('<div style="text-align: center;"><h2>EDA 1</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')


  # Seaborn count plot
  fig, ax = plt.subplots()
  ax = sns.countplot(x='Attrition_Flag', data=copy_df, palette='Set2')

  # Calculate percentages
  total_count = len(copy_df)
  for p in ax.patches:
      percentage = '{:.1f}%'.format(100 * p.get_height() / total_count)
      x = p.get_x() + p.get_width() / 2
      y = p.get_height() + 0.02 * total_count
      ax.annotate(percentage, (x, y), ha='center')

  # Set plot titles and labels
  plt.title('Attrition Flag Count')
  plt.xlabel('Attrition Flag')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(fig)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Attrition Flag Count</p></div>', unsafe_allow_html=True)
  
  description1 = """
  We can see that there are more existing customers than attributed customers, which means that the data is imbalanced. Hence, we have to handle this before modeling.

  Other insights we can gain from this data:

  - From 10,127 users, only 16.1% are attributed/left, which is a healthy amount of churn rate for our company. However, as a company, we want to further analyze potential users that will leave us.

  - For modeling our prediction, the data is imbalanced. Thus, we will balance them using SMOTE oversampling before modeling.
  """

  st.markdown(description1)


  # Divider 2
  st.markdown('<div style="text-align: center;"><h2>EDA 2</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style (optional)
  sns.set(style="darkgrid")

  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the histogram
  ax = sns.histplot(x='Customer_Age', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Set title and labels
  plt.title('Age Distribution')
  plt.xlabel('Age')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

    # Graph Info
  st.markdown('<div style="text-align: center;"><p>Age Histogram Plot</p></div>', unsafe_allow_html=True)
  
  description2 = """
  Based on the graph we can see that:

  - Age is normally distributed, with the most users being aroung 48 years old and the least being above 60
  - Majority of users are still using our service, around 16% - 25% of each age group are attributed

  Bussines Insight : 

  - We can provide financial stability anfd planning, people at the age of 40 to 50 usualy prioritize financial stability and planning become more important  thus we can provide them with the necessary assistance.
  - Long term reward benefits can be given to users that has been with as for a long period of time which can reduce potential churn rate.
  """
  st.markdown(description2)



  # Divider 3
  st.markdown('<div style="text-align: center;"><h2>EDA 3</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")

  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Dependent_count', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Dependent Count and Attrition Flag')
  plt.xlabel('Dependent Count')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Dependant Count Plot</p></div>', unsafe_allow_html=True)

  description3 = """
  Before going into the graph analysis we will explain a bit on dependent_count.

  Dependant_Count refers to the number of people who are financialy dependant to the user (example a father with two kids has a dependant count of 2 or 3 ( 3 if the wife is included)).

  Based in the graph abive we can say that :
  - Majority of your users has a dependancy of around 2 or 3 people and the least being 5 dependence count.
  - Majority of users are still using our service, around 16% - 25% of each dependence group are attributed/churn

  Bussiness Insight :
  - We can provide family oriented services towards users that has a dependancy of 1 or higher like a joint accoutn to reduce churn rate
  - A reward program that i family oriented like educational resources, financial planning tools, ect.
  """
  st.markdown(description3)





  # Divider 4
  st.markdown('<div style="text-align: center;"><h2>EDA 4</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")


  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Dependent_count', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Dependent Count with Attrition Flag')
  plt.xlabel('Dependent Count')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Dependant Count Plot</p></div>', unsafe_allow_html=True)

  description4 = """
  Before going into the graph analysis we will explain a bit on dependent_count.

  Dependant_Count refers to the number of people who are financialy dependant to the user (example a father with two kids has a dependant count of 2 or 3 ( 3 if the wife is included)).

  Based in the graph abive we can say that :
  - Majority of your users has a dependancy of around 2 or 3 people and the least being 5 dependence count.
  - Majority of users are still using our service, around 16% - 25% of each dependence group are attributed/churn

  Bussiness Insight :
  - We can provide family oriented services towards users that has a dependancy of 1 or higher like a joint accoutn to reduce churn rate
  - A reward program that i family oriented like educational resources, financial planning tools, ect.
  """
  st.markdown(description4)



  # Divider 5
  st.markdown('<div style="text-align: center;"><h2>EDA 5</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")


  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Months_Inactive_12_mon', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Months Inactive 12 month and Attrition Flag')
  plt.xlabel('Months Inactive 12 Months')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Months Inactive Count Plot</p></div>', unsafe_allow_html=True)

  description5 = """
Based on the graoh above we can say that:
- users are still in contact with use around 2 - 3 months with the highest being 3 months
- there are almost no users around 1 which means that they are still in contact with us on after the frist month.
- around 3 moths the attrition is at it's highest at 8.2%.

  """
  st.markdown(description5)


  
  # Divider 6
  st.markdown('<div style="text-align: center;"><h2>EDA 6</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")


  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Contacts_Count_12_mon', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Months in Contact and Attrition Flag')
  plt.xlabel('Months in Contact')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Months in Contact</p></div>', unsafe_allow_html=True)

  description6 = """
Based on the graoh above we can say that:
- users are still in contact with use around 2 - 3 months with the highest being 2 months
- there are no users around 6 and later months.
- around 3 moths the attrition is at it's highest at 6.7%.

Bussines insght:
- users contact banks to seek result/answer regarding our credit cards, we can increase ourr customer services in order to lower customer churn.

  """
  st.markdown(description6)



  # Divider 7
  st.markdown('<div style="text-align: center;"><h2>EDA 7</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")


  # Set the style (optional)
  sns.set(style="darkgrid")

  # Create a larger figure
  fig, ax = plt.subplots(figsize=(12, 6))

  # Create the histogram
  sns.histplot(x='Months_on_book', data=copy_df, hue='Attrition_Flag', palette='deep', ax=ax)

  # Set title and labels
  ax.set_title('Months with Bank Distribution')
  ax.set_xlabel('Months')
  ax.set_ylabel('Count')

  # Display the plot in Streamlit app
  st.pyplot(fig)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Months with Bank Count Plot</p></div>', unsafe_allow_html=True)

  description7 = """
Based on the graph above we can gather that:

- most users has been with us for over 30 months (more than 2 -3 years).
- Attrition is higer around the months of 30 to 39.

Bussines Insight:
- the same as the age we can give long term users award based on how long they gav been with us.
- Financialy consulting for long term users.

  """
  st.markdown(description7)



  # Divider 8
  st.markdown('<div style="text-align: center;"><h2>EDA 8</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

  # Set the style
  sns.set(style="darkgrid")


  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Gender', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Gender with Attrition Flag')
  plt.xlabel('Gender')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Gender Count Plot</p></div>', unsafe_allow_html=True)

  description8 = """
Male = 0 and Female = 1

Based on the graph above we can say that:

- There are 3.8 more females than there are male.
- both gender are quite evenly distributed with females having a higher attrition comapred to males by 1.2%
  """
  st.markdown(description8)



  # Divider 9
  st.markdown('<div style="text-align: center;"><h2>EDA 9</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

    # Set the style
  sns.set(style="darkgrid")

  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Education_Level', data=copy_df, hue='Income_Category', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Education Level and Income_Category')
  plt.xlabel('Education_Level')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Education Level and Income_Category</p></div>', unsafe_allow_html=True)

  description9 = """
Based on the graph above we can say that:
- Majority of users are around high school, graduate, and uneducated with the most being graduate.
- majority of our users makes less then 40K.
- Unknown catagory will be randomly imputated during missing value handling.

Bussiness Insight:
- We cam give give financial counceling to high school and uneducated users so they can be more financially stable and lower churn rate.
  """
  st.markdown(description9)



  # Divider 10
  st.markdown('<div style="text-align: center;"><h2>EDA 10</h2></div>', unsafe_allow_html=True)

  # Divider
  st.markdown('--------------')

    # Set the style
  sns.set(style="darkgrid")

  # Create a larger figure
  plt.figure(figsize=(12, 6))

  # Create the count plot with hue
  ax = sns.countplot(x='Income_Category', data=copy_df, hue='Attrition_Flag', palette='deep')

  # Calculate the percentage of each hue category
  total = len(copy_df)
  for p in ax.patches:
      height = p.get_height()
      ax.text(p.get_x() + p.get_width() / 2., height + 0.1,
              '{:.1%}'.format(height / total),
              ha="center")

  # Set title and labels
  plt.title('Income Category With Attrition')
  plt.xlabel('Education_Level')
  plt.ylabel('Count')

  # Display the plot using Streamlit
  st.pyplot(plt)

  # Graph Info
  st.markdown('<div style="text-align: center;"><p>Income Category With Attrition</p></div>', unsafe_allow_html=True)

  description10 = """
Based on the graph above we can say that:
- majority of our users makes less then 40K.
- Unknown catagory will be randomly imputated during missing value handling.
- arounf 2 to 6 % of each demograpich attributed/churn

Bussiness Insight:
- We cam give give financial counceling to those that make less than 40K.
- we can give some leniency for user that make less than 60K to pay of their credit card.
  """
  st.markdown(description10)