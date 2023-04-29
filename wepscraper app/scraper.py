from datetime import date
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
from datetime import time
import time as ts
import streamlit as st
import webbrowser as wb

######### site için ayarlamalar yapabileceğimiz bir kod stramlit documentary den ############
import streamlit as st

st.set_page_config(page_title="Web Scraper",
                   page_icon="⚓",
                   layout = "centered",
                   menu_items={
                    'Get Help': 'https://www.extremelycoolapp.com/help',
                    'Report a bug': "https://www.extremelycoolapp.com/bug",
                    'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",  tabda görünen başlığı değiştirir
#     page_icon="🧊", # tabda görünen iconu değiştiriyor
#     layout="wide", # hazırladığımız sayfanın görünüm genişliği vs..
#     initial_sidebar_state="expanded",
#     menu_items={ # menüye tıkladığında gidilecek sayfaları oluşturmak için
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
# )
#########################

st.markdown("<h1 style = 'text-align: center;'>Web Scraper</h>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

placeholder = st.empty()

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = bs(page.content.decode('utf-8'), "lxml")
    rows = soup.find_all("div", class_="ripi6")
    col1, col2, col3 = placeholder.columns(3)

    for nr, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(len(figures)):
            image = figures[i].find("img", class_="tB6UZ a5VGX")
            liste = image["srcset"].split("?")
            anchor = figures[i].find("a", class_="rEAWd")

            if i % 3 == 0:
                col = col1
            elif i % 3 == 1:
                col = col2
            else:
                col = col3

            col.image(liste[0])
            btn = col.button("Download", key=str(nr)+str(i))
            if btn:
                wb.open_new_tab("https://unsplash.com" + anchor["href"])

