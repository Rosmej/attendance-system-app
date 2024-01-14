import streamlit as st
from Home import face_rec
# st.set_page_config(page_title='Reporting',layout='wide')
st.subheader('Reporting')

# retrieve Logd data and show in report.py

# extract date from redis list
name  = 'ArcEmployeeattendance:logs'

def load_logs(name,end=-1):
    logs_list = face_rec.r.lrange(name,start=0,end= end) # extract all data from redis database
    return logs_list

# tabs to show the info
tab1, tab2 = st.tabs(['Registered Data','Logs'])

with tab1:
    if st.button('Refresh Data'):
    # Retrieve the data from Redis Database
        with st.spinner('Retrieving Data from Redis DB...'):
            redis_face_db = face_rec.retrieve_data(name='ArcEmployees:register')
            st.dataframe(redis_face_db[['Name','Role','Emp_Id']])
    
with tab2:
    if st.button('Refresh logs'):
        st.write(load_logs(name=name)) 