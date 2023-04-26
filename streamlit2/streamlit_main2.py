from datetime import date
from turtle import width
from matplotlib import table
import streamlit as st

st.title("Uploading Files")
st.markdown("---")

image = st.file_uploader("please upload an Image", type=["png", "jpg", "jpeg"])

if image is not None:
    st.image(image, caption="NLP", width=680)

st.markdown("---")

video = st.file_uploader("please upload an video", type="mp4")

if image is not None:
    st.video(video)

# birden fazla dosya yüklemek istiyorsak
st.markdown("---")
image1 = st.file_uploader("please upload an Image", type=["png", "jpg", "jpeg"], accept_multiple_files =True )

if image1 is not None:
    st.image(image1)

st.markdown("---")
###################### slider #######################

st.slider("This is a Slider") # varsayılan olarak 0-100 arası 
st.markdown("---")

st.slider("This is a second Slider", min_value=50, max_value=100, value=70) # başlangıc 50, son 10, varsayılan olarak 70 de duruyor

st.markdown("---")

#################### input ################

val = st.text_input("Enter your Course Title", max_chars=60)
# print(val)

val1 = st.text_area("Course Description", max_chars=100)
#print(val1)
st.markdown("---")
date_ = st.date_input("Enter your registiration Date")
#print(date_)

# time = st.time_input("Set timer") # default olarak gerçek zamanı getiriyor
#print(time)

st.markdown("---")

#################### progress ################
import time as ts
#bar = st.progress(0) # default olarak 100 basamak var
#for i in range(10): # her bir saniye de 10 basamak ilerlesin
#    bar.progress((i+1)*10) 
#    ts.sleep(1)

st.markdown("---")

from datetime import time as zeit 



def converter(value):
    m, s, ms = value.split(":")
    t_s = int(m)*60 + int(s) + int(ms)/1000 # birdakika 60 sn, 1 saniye 1000 milisaniye
    return t_s

val5 = st.time_input("Set timer", value=zeit(0,0,0)) # value değeri ile varsayılan bir zaman atamış oluyoruz
if str(val5) == "00.00.00": # dakika, saniye , mili saniye
    st.write("Please sent timer")
else:
    sec = converter(str(val5))
    bar = st.progress(0) # default olarak 100 basamak var
    per = sec/100
    progress_status = st.empty()
    for i in range(1, 101): # elimizdeki toplam saniyeyi 100 parçaya ayırmamız gerekiyr
        bar.progress((i)) 
        progress_status.write(str(i) + " %")
        ts.sleep(per)







