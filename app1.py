import streamlit as st
import pandas as pd
import pickle
import base64

def load_model():
    with open('regressor.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image3.jpg') 

def main(): 
    st.title("Influencer's Q-score Prediction App")
    
    # Load model
    model = load_model()

    # Input variables
    variable1 = st.number_input("Enter the Followers of influencer")
    variable2 = st.number_input("Enter the Avg_Likes of influencer")
    variable3 = st.number_input("Enter the Avg_Views of influencer")
    variable4 = st.number_input("Enter the Categories of influencer")
    #variable4 = st.selectbox("Select the Categories of influencer", ["Option 1", "Option 2", "Option 3"])
    variable5 = st.number_input("Enter the Influencer_Tier of influencer")

    # Make prediction
    if st.button("Predict"):
        input_data = [[variable1, variable2, variable3, variable4, variable5]]
        prediction = model.predict(input_data)
        #st.success(f"The Q-Score is {prediction}")
        #prediction.dtypes
        if prediction < 4:
            modified_prediction = "Least Recommended"
            #return "Mid Tier"
        elif prediction >=4 and prediction <7:
            modified_prediction = "Moderately Recommended"
        elif prediction >=7:
            modified_prediction = "Highly Recommended"
            
        st.success(f"The Q Score is {prediction}")
        st.success(f"The Influencer is {modified_prediction}")

if __name__ == "__main__":
    main()
