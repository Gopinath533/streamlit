import streamlit as st

# itle for the streamlit
st.title("GOPINATH")

# heading and subheadings
st.header("gopinath the python developer")
st.subheader("Gopinath_cool")

# Text
st.text("Hello streamlit")

# Markdown
st.markdown("### This is a markdown")

# ERROR/colorful text
st.success("successful")

st.info("Information!")

st.warning("This is a warning")

st.error("this is a error message")

st.exception("NameError('name three not defined')")

# Get Help info about python
st.help(range)


#writing text/super FXN
st.write("Text with write")

st.write(range(10))
#images
from PIL import Image
img = Image.open("./image/a.jpg")
st.image(img,width=300,caption="simple image")

#videos
vid_file = open("./image/b.mp4","rb").read()
st.video(vid_file)

audio_file = open("./image/c.mp3","rb").read()
st.audio(audio_file,format ='audio/mp3')

#widget
if st.checkbox("show/Hide"):
    st.text("showing or hiding widget")

#Radio Buttons
status = st.radio("what is your status",("Active","Inactive"))

if status == 'Active':
    st.success("your active")
else:
    st.warning("Inactive,Activate")

#selectBox
occupation = st.selectbox("your occupation",["programmer","Doctor","scientist","Gopinath"])
st.write("You selected this option")

#multiselect
location = st.multiselect("where do you work?",("Londaon","new York","hyd","melb","cannada"))
st.write("you selected",len(location),"locations")

#slider
level = st.slider("what is your level",1,5)

#Buttons
st.button("simple Button")

if st.button("About"):
    st.text("streamlit is cool")


#text Input
#firstname = st.text_input("enter your Firstname","type here..")
#if st.button("submit"):
 #   result = firstname.title()
 #   st.success(result)


message = st.text_area("enter your Firstname","type here..")
if st.button("submit"):
    result = message.title()
    st.success(result)

#DateInput
import datetime
today = st.date_input("today is",datetime.datetime.now())

#time
the_time = st.time_input("The time is ",datetime.time())

#Displaying Json
st.text("Display JSON")
st.json({'name':"jesse",'gender':"male"})

#display Raw code

st.text("display raw code")
st.code("import numpy as np")

#display raw code
with st.echo():
    #This will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

#prograss Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)


#spinner
with st.spinner("waiting.."):
    time.sleep(5)
    st.success("finished")


#ballons
st.balloons()

#sidebar
st.sidebar.header("About")
st.sidebar.text("this is streamlit tut")


#Functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

#plot()
st.pyplot()

#DataFrames
st.dataframe(df)

#Tables
st.table(df)