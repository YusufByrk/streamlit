from datetime import date
import pandas as pd
from matplotlib import table
import matplotlib.pyplot as plt
import numpy as np
from datetime import time
import time as ts
import streamlit as st

st.sidebar.write("Hello this is my side bar")

tabel = pd.DataFrame({"Column1": [1,2,3,4,5,6], "Column2":[11, 12,13,14,15,16]})
x= np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x))
st.write(fig)

st.markdown("---")

opt = st.sidebar.radio("Select Any Graph", options=("Line", "Bar", "H-Bar"))
bar_x = np.array([1, 2, 3, 4, 5])
if opt =="Line":
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html = True)
    fig = plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    st.write(fig)

elif opt == "Bar":
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html = True)
    fig = plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)

else:
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html = True)
    fig = plt.figure()
    plt.style.use("https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    bar_x = np.array([1, 2, 3, 4, 5])
    plt.barh(bar_x, bar_x*10)
    st.write(fig)