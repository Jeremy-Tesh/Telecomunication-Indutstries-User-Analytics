from os import write
import streamlit as st
import numpy as np
import pandas as pd
import query
import pickle


# loading the trained model
pickle_in = open('models/scores_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)

def display_df(table_name):
    df = query.fetch_data(table_name)
    return df

def toggle_bn_pages():
    pages = ['Display Data','model ']
    option = st.sidebar.selectbox('Choose:',pages)
    if option == pages[0]:
        st.markdown("<h1 style='color: gray;'>"+option+" of our users</h1>", unsafe_allow_html=True)
        st.write(display_df("user_scores"))
    else:
        st.markdown("<h1 style='color: gray;'>"+option+" satisfaction score</h1>", unsafe_allow_html=True)
        model_page()

@st.cache()  
# defining the function which will make 
# the prediction using data about the users 
def prediction(exp_score, eng_score):   
 
    # Making predictions 
    prediction = classifier.predict(np.array([[eng_score,exp_score]]))
     
    if prediction[0] == 0:
        pred = 'Satisfied'
    else:
        pred = 'Not Satisfied'
    return pred

def model_page():
      
    # create input fields to enter model inputs
    engagement_score = st.text_input("Input engagement_score:")
    experience_score = st.text_input("Input experience score:")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(engagement_score,experience_score) 
        st.success('The user is {}'.format(result))     
  
# webpage elements
def main():       
    # front end elements of the web page 
    toggle_bn_pages()
    

     
if __name__=='__main__': 
    main()
