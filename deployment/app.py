import streamlit as st
import pandas as pd
import joblib
import numpy as np
from streamlit_lottie import st_lottie
import json
import requests
from streamlit_option_menu import option_menu

import Prediction
import EDA






def home():
  with st.container():
    st.title("Credit Card Attrition Model Prediction")
    st.subheader("Hi, I am M. Irsyad Rafif :wave:")
    st.title("A Data Scientist From Indonesia")
    st.write(
        "In this webApp i am going to analyze and predict customer attrition so we can mitigate ahead of time."
    )

  def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

  # ---- LOAD ASSETS ----
  lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
  # img_contact_form = Image.open("images/yt_contact_form.png")
  # img_lottie_animation = Image.open("images/yt_lottie_animation.png")

  # ---- WHAT I DO ----
  with st.container():
      st.write("---")
      left_column, right_column = st.columns(2)
      with left_column:
          st.header("Study Case/Problem Statement")
          st.write("##")
          st.write(
              """
              In this Scenario i am a data scientist working in SBank where safety and satisfaction is guranteeed (Made up bank). Our bank prioritize customer satisfaction by looking at the customer rentention and customer churn rate. We can see from the data gather last year which is 2023 that there are some customers that  has churned.

              I am tasked by Sbank to analyze and predict potential customers that might/already left in order for Sbank marketing team and sales team to mitiagete a potential attrition of our users. With the goal to lower costomer churn by 5%


              """
          )

      with right_column:
          st_lottie(lottie_coding, height=550, key="coding")


# Sidebar Menu
with st.sidebar:
  selected = option_menu(
    menu_title=None, 
    options=['Home', 'Model Prediction','Exploratory Data Analysis'],
    icons = ['house', 'credit-card', 'bar-chart-fill'],
    styles={
        "container": {"background-color": "#161A30"},
        "icon": {"color": "F0ECE5", "font-size": "25px"}, 
        "nav-link-selected": {"background-color": "#818FB4"},
    },   
    default_index=0
  )

if selected == 'Home':
  home()

elif selected == 'Model Prediction':
  Prediction.user_input()

else:
  EDA.graph()

