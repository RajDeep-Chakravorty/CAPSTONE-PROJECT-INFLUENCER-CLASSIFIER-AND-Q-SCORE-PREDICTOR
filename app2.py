import streamlit as st
import pandas as pd
import pickle
import base64
from PIL import Image

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
add_bg_from_local('image2.jpg') 

def load_model():
    with open('classification.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title("INFLUENCER CLASSIFICATION APP")
    st.write('Influencer Id list')
    # Load CSV file
    #csv_file = st.file_uploader("Final.csv", type=["csv"])
    #if csv_file is not None:
        #df = pd.read_csv(csv_file)
        #st.dataframe(df)
    # Read the CSV file
    data = pd.read_csv("Influencer Id List.csv")
    
    # Display the image in a column next to the DataFrame
    col1, col2 = st.columns(2)

    # Image column
    with col2:
        image = Image.open("inf.jpg")
        st.image(image)

    # DataFrame column
    with col1:
        #st.write("Influencer Id List")
        st.dataframe(data)
    
    # Load model
    model = load_model()

    # Input variables
    variable1 = st.number_input("Enter the Followers of influencer")
    variable2 = st.number_input("Enter the Avg_Likes of influencer")
    variable3 = st.number_input("Enter the Avg_Views of influencer")
    variable4 = st.number_input("Enter the Categories of influencer")
    variable5 = st.number_input("Enter the Name_id of Influencer \n (please refer to the list above)")

    # Make prediction
    if st.button("Classify"):
        input_data = [[variable1, variable2, variable3, variable4, variable5]]
        prediction = model.predict(input_data)
        #prediction.dtypes
        if prediction == 0:
            modified_prediction = "Celebrity"
            #return "Mid Tier"
        elif prediction == 1:
            modified_prediction = "Mega Influencer"
        elif prediction == 2:
            modified_prediction = "Micro Influencer"
        else:
            modified_prediction = "Mid Tier Influencer"
            
        #st.success(f"The prediction is {prediction}")
        st.success(f"The Influencer is {modified_prediction}")

if __name__ == "__main__":
    main()
