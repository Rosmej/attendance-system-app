<<<<<<< HEAD
import streamlit as st
from Home import face_rec
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av

#st.set_page_config(page_title='Registration Form')
st.subheader('Registration Form')

# init registration form
registration_form = face_rec.RegistrationForm()
# Step-1: collect person name and role
# form 
person_name = st.text_input(label='Name',placeholder='First & Last Name')
Emp_Id = st.text_input(label='Emp Id',placeholder='ARC@12344')
role= st.selectbox(label='select your Role',options=('SuperAdmin','Supervisor','User','Manager','HR'))

#step-2: Collect Facial embedding of the person

def video_callback_func(frame):
    img=frame.to_ndarray(format='bgr24') #3d array bgr
    reg_image,embedding = registration_form.get_embedding(img)
    # two step process
    #1st step save data into local computer txt
    if embedding is not None:
        with open('face_embedding.txt',mode='ab') as f:
            np.savetxt(f,embedding)
    return av.VideoFrame.from_ndarray(reg_image,format='bgr24')

webrtc_streamer(key="realtimePrediction", video_frame_callback=video_callback_func, rtc_configuration={
    "iceServers": [{"urls": ["stun:16.171.132.146:5349","turn:16.171.132.146:5349"]}]
})

#step-3: save the data in redis Database

if st.button('submit'):
    return_value = registration_form.save_data_in_redis_db(person_name,role,Emp_Id)
    if return_value == True:
        st.success(f"{person_name} registered successfully")
    elif return_value == 'name_false':
        st.error('please enter the name : Name cannot be empty or spaces')
    elif return_value == 'file_false':
=======
import streamlit as st
from Home import face_rec
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
import os
from twilio.rest import Client
#st.set_page_config(page_title='Registration Form')
st.subheader('Registration Form')

# init registration form
registration_form = face_rec.RegistrationForm()
# Step-1: collect person name and role
# form 
person_name = st.text_input(label='Name',placeholder='First & Last Name')
Emp_Id = st.text_input(label='Emp Id',placeholder='ARC@12344')
role= st.selectbox(label='select your Role',options=('SuperAdmin','Supervisor','User','Manager','HR'))
account_sid = os.environ['AC22fad8fc98762c8a961730377698f54b']
auth_token = os.environ['5491572a11fa6ff2c945bdfd175d62b2']
client = Client(account_sid, auth_token)
token = client.tokens.create()
#step-2: Collect Facial embedding of the person

def video_callback_func(frame):
    img=frame.to_ndarray(format='bgr24') #3d array bgr
    reg_image,embedding = registration_form.get_embedding(img)
    # two step process
    #1st step save data into local computer txt
    if embedding is not None:
        with open('face_embedding.txt',mode='ab') as f:
            np.savetxt(f,embedding)
    return av.VideoFrame.from_ndarray(reg_image,format='bgr24')

webrtc_streamer(key="registration", video_frame_callback=video_callback_func, rtc_configuration={
         "iceServers": token.ice_servers
    })
#step-3: save the data in redis Database

if st.button('submit'):
    return_value = registration_form.save_data_in_redis_db(person_name,role,Emp_Id)
    if return_value == True:
        st.success(f"{person_name} registered successfully")
    elif return_value == 'name_false':
        st.error('please enter the name : Name cannot be empty or spaces')
    elif return_value == 'file_false':
>>>>>>> 2ce46fe9e23a8c689194b0cc268337b77cc76a63
        st.error('face_embedding.txt is not found. Please refresh the page and execute again')