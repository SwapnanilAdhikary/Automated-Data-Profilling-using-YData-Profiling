import os
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import  st_profile_report
from ydata_profiling import  ProfileReport
#from pycaret.regression import setup, compare_models,pull,save_model



with st.sidebar:
    st.image("img.jpeg")
    st.title("AutoStreamMl")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info(
        "This application allow you to build an Automated ML pipeline using Streamlit, Pandas Profiling and PyCaret")
#st.write("Hello world!")
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload your data for modeling!")
    file = st.file_uploader("Upload you dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    profile = ProfileReport(df)
    st.title("Profiling in streamlit")
    st.write(df)
    st_profile_report(profile)

if choice == "ML":
    pass
    # st.title("Machine learning pipeline")
    # target = st.selectbox("selec your target",df.columns)

if choice == "Download":
    pass
