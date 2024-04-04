# Credit Card Attrition Prediction

---


# Introduction

This project aims to develop a predictive model to identifying credit card users that has a potential to churn/attrition. By analyzing customer behavior, the goal is to create a reliable tool that can assist the marketing team in mitifating potential attrition by creating prevention strategies. With accurate predictions, we can create a more effective targeted marketing. In this project, various classification algorithm will be evaluated to find the best model for the dataset

---

# Problem Identification

## Case Study:

In this Scenario I am a data scientist working in SBank where safety and satisfaction is guaranteed (Made up bank). Our bank prioritize customer satisfaction by looking at the customer retention and customer churn rate. We can see from the data gather last year which is 2023 that there are some customers that has churned.

I am tasked by Sbank to analyze and predict potential customers that might/already left in order for Sbank marketing team, product team and sales team to mitigate a potential attrition of our users. With the goal to lower customer churn by 5%.

---

# Data Cleaning and Preprocessing

The raw data was cleaned to ensure it is appropriate for statistical measurements. This involved adjusting data types and removing rows with missing values as well feature engineering from creation to selection and further scaling and encoding to be done before modeling.

---

# Data Analysis and Insights

Based on the EDA we can gather that :

- Attrition :
  - There are more users that still use our credit card compared to attrited customers.

  - around 16.1% of users that are attrited compared to the 83.9% that are with us.
  
  - Data is proved to be imbalanced.

- Age :
  - Age is normally distributed, with the most users being aroung 48 years old and the least being above 60.

  - Majority of users are still using our service, around 16% - 25% of each age group are attributed.

  Bussines Insight: 
  - We can provide financial stability anfd planning, people at the age of 40 to 50 usualy prioritize financial stability and planning become more important  thus we can provide them with the necessary assistance.

  - Long term reward benefits can be given to users that has been with as for a long period of time which can reduce potential churn rate.

- Dependancy Count : 

  Dependant_Count refers to the number of people who are financialy dependant to the user (example a father with two kids has a dependant count of 2 or 3 ( 3 if the wife is included)).

  Based in the graph abive we can say that :

  - Majority of your users has a dependancy of around 2 or 3 people and the least being 5 dependence count.
  - Majority of users are still using our service, around 16% - 25% of each dependence group are attributed/churn

  Bussiness Insight :
  
  - We can provide family oriented services towards users that has a dependancy of 1 or higher like a joint accoutn to reduce churn rate
  - A reward program that i family oriented like educational resources, financial planning tools, ect.

- Inactivity within 12 Months : 

  - users are still in contact with use around 2 - 3 months with the highest being 3 months
  - there are almost no users around 1 which means that they are still in contact with us on after the frist month.
  - around 3 moths the attrition is at it's highest at 8.2%.

- Contact with bank within 12 Months : 

  - users are still in contact with use around 2 - 3 months with the highest being 2 months
  - there are no users around 6 and later months.
  - around 3 moths the attrition is at it's highest at 6.7%.

Bussines insght:
  - users contact banks to seek result/answer regarding our credit cards, we can increase ourr customer services in order to lower customer churn.

-  Months on Book :

  - most users has been with us for over 30 months (more than 2 -3 years).
  - Attrition is higer around the months of 30 to 39.

Bussines Insight:

  - the same as the age we can give long term users award based on how long they gav been with us.
  - Financialy consulting for long term users.

- Gender : 

  - There are 3.8 more females than there are male.
  - both gender are quite evenly distributed with females having a higher attrition comapred to males by 1.2%.

- Education Level : 

  - Majority of users are around high school, graduate, and uneducated with the most being graduate.
  - majority of our users makes less then 40K.
  - Unknown catagory will be randomly imputated during missing value handling.

  Bussiness Insight:
  
  - We cam give give financial counceling to high school and uneducated users so they can be more financially stable and lower churn rate.

- Income Catagory : 

  - majority of our users makes less then 40K.
  - Unknown catagory will be randomly imputated during missing value handling.
  - arounf 2 to 6 % of each demograpich attributed/churn

Bussiness Insight:

  - We cam give give financial counceling to those that make less than 40K.
  - we can give some leniency for user that make less than 60K to pay of their credit card.  

---
# Conclusion

Based on the comperhensive exploratory data analysis (EDA) and model evaluation, it is evident that **Boosting after hpyerparamter tunning emerges as the most optimal choice to predict attired users in the given dataset.** The EDA insight shows some insight regarding our demographic and their activity of 12 months of this data has been collected which can give as a lot of bussiness insight. Such as giving reward system that base on how active and how long they have been using our services as well as giving financial consultinh towards those that has low income and a lot of depeneces.

Regarding the model that shows the best which os boosting after conducting hyperparameter tuning, we can see the recall difference between tran and test of 12% although it is higher we can see a more significant decreese in the false negative value on the confusion matrix and an increase in stability on the cross validation. Moving forward, ufrther experimentation could be done by either increasing the numbers of features and hyperparameter tuning using grid search instead of randomsearchCV, alternatif model evaluation and feature selection using other means than correlation and feature of importance such as the feature selection liblary.

# Deployment Link

Deployment Link:
https://huggingface.co/spaces/Rafion101/Milestone_2