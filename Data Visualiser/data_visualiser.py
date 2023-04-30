import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

figure = plt.figure()
def date_converter(date_col):
    result = list()
    values = date_col.values
    for value in values:
        result.append(str(value).split("T")[0])

    return result


st.markdown("<h1 style='text-align: center;'>Data Visualizer</h1>", unsafe_allow_html = True)
st.markdown("---")

files_names = list()
files = st.file_uploader("Upload Multiple Files", type=["xlsx", "csv", "txt"], accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)
    selected_files = st.multiselect("Select Files", options=files_names)
    if selected_files:
        option = st.radio("Select Entity Against Date", options = ['None', "GPU","CPU", "MOUSE", "KEYBOARD", "CASTING"])
        
        if option != "None":
            for file in files:
                if file.name in selected_files:
                    data = pd.read_excel(file, index_col=0) # index olarak atamak istediğimiz bir sütun olursa index_col = 0 fonksiyonunu kullanabiliriz.
                    item = list(data[option])
                    dates = date_converter(data["DATE"])
                    index = np.arange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.plot(index, item, label=file.name, marker='o')
                    plt.xlabel("Date")
                    plt.ylabel(option)
                    plt.title(option + " Chart")
                    plt.grid(True)
                    plt.legend()
            st.write(figure)
        