# Dammy
import streamlit as st
import pandas as pd
import seaborn as sns

st.title('My Data Analysis App')
st.subheader('Data Analysis Using Python And Streamlit')

upload=st.file_uploader('Upload your Dataset(In csv format)')
if upload is not None:
    data=pd.read_csv(upload)
if st.checkbox('preview Dataset'):
    if st.button('Head'):
        st.write(data.head())
    if st.button('Tail'):
        st.write(data.tail())

if upload is not None:
    if st.checkbox('DataType of Each Column'):
        st.text('DataTypes')
        st.write(data.dtypes.astype(str))   
        
if upload is not None:
    data_shape=st.radio('What dimension do you wan to check?',('Rows','Columns'))
    if data_shape=='Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])

if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox('Null Values in the Dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()     
    else:         
        st.success('Nice Job!,No Missing Values')
        
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning('This Dataset contains some duplicate values!')
        dup=st.selectbox('Do you want to remove Duplicates Values?',\
                         ('Select one','Yes','No'))
        if dup=='Yes':
           data=data.drop_duplicates()
           st.text('Duplicate Values Are removed')
        if dup=='No':
           st.write('Ok,you Can Still proceed')
    
if upload is not None:
     if st.checkbox('Summary of the Dataset'):
         st.write(data.describe())
         
if st.button('About App'):
    st.text('Built with Streamlit')
    st.text('A special thanks to streamlit')
if st.checkbox('By'):
    st.success('Abdulazeez Sodiq Adedamola')
    
        
        
        
        