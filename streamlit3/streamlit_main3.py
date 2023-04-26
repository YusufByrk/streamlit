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


# https://www.youtube.com/watch?v=cUKqsnLGQBw&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=14