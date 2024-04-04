import streamlit as st
import pandas as pd
import joblib

load_model = joblib.load("model.pkl")

def user_input():
    st.title("MODEL PREDICTION")

    # Divider
    st.markdown('<div style="text-align: laeft;"><h2>Dataframe</h2></div>', unsafe_allow_html=True)

    df = pd.read_csv('BankChurners.csv')

    st.dataframe(df)

    # Divider
    st.markdown('<div style="text-align: left;"><h2>Input Data</h2></div>', unsafe_allow_html=True)

    # Customer data
    client_num = st.number_input("Client Number", value=768805383)
    customer_age = st.number_input("Customer Age", value=45, min_value=18, max_value=100)
    gender_mapping = {0: "Male", 1: "Female"}
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: gender_mapping[x], index=0)
    dependent_count = st.number_input("Dependent Count", value=3, min_value=0, max_value=5)
    education_level = st.selectbox("Education Level", ["High School", "College", "Graduate"], index=0)
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"], index=1)
    income_category = st.selectbox("Income Category", ["<$40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", ">$120K"], index=2)
    card_category = st.selectbox("Card Category", ["Blue", "Silver", "Gold", "Platinum"], index=0)
    months_on_book = st.number_input("Months on Book", value=39)
    total_relationship_count = st.number_input("Total Relationship Count", value=5)
    months_inactive_12_mon = st.number_input("Months Inactive (12 months)", value=1, min_value=0, max_value=12)
    contacts_count_12_mon = st.number_input("Contacts Count (12 months)", value=3, min_value=0, max_value=12)
    credit_limit = st.number_input("Credit Limit", value=12691.0, min_value=1438.3, max_value=50000.0)
    total_revolving_bal = st.number_input("Total Revolving Balance", value=777.0)
    avg_open_to_buy = st.number_input("Average Open To Buy", value=11914.0)
    total_amt_chng_q4_q1 = st.number_input("Total Amount Change (Q4 to Q1)", value=1.335)
    total_trans_amt = st.number_input("Total Transaction Amount", value=1144.0)
    total_trans_ct = st.number_input("Total Transaction Count", value=42)
    total_ct_chng_q4_q1 = st.number_input("Total Count Change (Q4 to Q1)", value=1.625)
    avg_utilization_ratio = st.number_input("Average Utilization Ratio", value=0.061)

    # Create a dictionary with the entered data
    data = {
        'CLIENTNUM': client_num,
        'Customer_Age': customer_age,
        'Gender': gender,
        'Dependent_count': dependent_count,
        'Education_Level': education_level,
        'Marital_Status': marital_status,
        'Income_Category': income_category,
        'Card_Category': card_category,
        'Months_on_book': months_on_book,
        'Total_Relationship_Count': total_relationship_count,
        'Months_Inactive_12_mon': months_inactive_12_mon,
        'Contacts_Count_12_mon': contacts_count_12_mon,
        'Credit_Limit': credit_limit,
        'Total_Revolving_Bal': total_revolving_bal,
        'Avg_Open_To_Buy': avg_open_to_buy,
        'Total_Amt_Chng_Q4_Q1': total_amt_chng_q4_q1,
        'Total_Trans_Amt': total_trans_amt,
        'Total_Trans_Ct': total_trans_ct,
        'Total_Ct_Chng_Q4_Q1': total_ct_chng_q4_q1,
        'Avg_Utilization_Ratio': avg_utilization_ratio
    }

    features = pd.DataFrame(data, index=[0])



    # Button to input data into DataFrame
    col1, col2 = st.columns((8, 4))
    with col1:
        input_button = st.button("Input Data into DataFrame", key="input_button", help="Click this button to input data into DataFrame.")

    with col2:
        predict_button = st.button("Run Model to Make Prediction", key="predict_button", help="Click this button to make a prediction.")

    if input_button:
        st.subheader('User Input')
        st.write(features)

    if predict_button:
        prediction = load_model.predict(features) # Get the first element of the prediction array

        if prediction == 1:
            prediction_text = 'Potential user attrition'
        else:
            prediction_text = 'Existing user/no potential attrition'

        st.subheader('Results')
        st.write(prediction_text)

user_input()