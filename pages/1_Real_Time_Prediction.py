<<<<<<< HEAD
import streamlit as st
from Home import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import time
#st.set_page_config(page_title='Predictions')

st.subheader('Punch In')
#Retrieve data from Redis Database
with st.spinner('Retrieving Data from Redis DB...'):
    redis_face_db = face_rec.retrieve_data(name='ArcEmployees:register')
    st.dataframe(redis_face_db)
st.success("Data successfully retrieved fro, Redis")
# time
waitTime= 10 # time in sec
setTime = time.time()
realtimepred = face_rec.RealTimePred() # Real Time Prediction class
# Real Time Prediction
#streamlit webrtc

# callback function
difftime=0
def video_frame_callback(frame):
    global setTime
    img = frame.to_ndarray(format="bgr24") #3d numpy array
    #operation that can perform on the array
    pred_img,person_name= realtimepred.face_prediction(img,redis_face_db,'facial_features',['Name','Role'],thresh=0.5)
    timenow =time.time()
    difftime = timenow - setTime
    if difftime >= waitTime:
        if(person_name != 'Unknown'):
            st.success(f'{person_name} Logged in successfully')
            realtimepred.saveLogs_redis()
            setTime = time.time() # reset time
            print(person_name)
            print('save data to redis db') 
          
           
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

webrctc_ctxt = webrtc_streamer(key="realtimePrediction", video_frame_callback=video_frame_callback, rtc_configuration={
        "iceServers": [{"urls": ["stun:16.171.132.146:5349","turn:16.171.132.146:5349"]}]
    })
=======
import streamlit as st
from Home import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import time
import os
from twilio.rest import Client
#st.set_page_config(page_title='Predictions')

st.subheader('Punch In')
#Retrieve data from Redis Database
with st.spinner('Retrieving Data from Redis DB...'):
    redis_face_db = face_rec.retrieve_data(name='ArcEmployees:register')
    st.dataframe(redis_face_db)
st.success("Data successfully retrieved from Redis")
# time
waitTime= 10 # time in sec
setTime = time.time()
realtimepred = face_rec.RealTimePred() # Real Time Prediction class
# Real Time Prediction
#streamlit webrtc
account_sid = os.environ['AC22fad8fc98762c8a961730377698f54b']
auth_token = os.environ['5491572a11fa6ff2c945bdfd175d62b2']
client = Client(account_sid, auth_token)

token = client.tokens.create()
# callback function
difftime=0
def video_frame_callback(frame):
    global setTime
    img = frame.to_ndarray(format="bgr24") #3d numpy array
    #operation that can perform on the array
    pred_img,person_name= realtimepred.face_prediction(img,redis_face_db,'facial_features',['Name','Role'],thresh=0.5)
    timenow =time.time()
    difftime = timenow - setTime
    if difftime >= waitTime:
        if(person_name != 'Unknown'):
            st.success(f'{person_name} Logged in successfully')
            realtimepred.saveLogs_redis()
            setTime = time.time() # reset time
            print(person_name)
            print('save data to redis db') 
          
           
    return av.VideoFrame.from_ndarray(pred_img, format="bgr24")

webrctc_ctxt = webrtc_streamer(key="realtimePrediction", video_frame_callback=video_frame_callback, rtc_configuration={
        "iceServers": token.ice_servers
    })
>>>>>>> 2ce46fe9e23a8c689194b0cc268337b77cc76a63
