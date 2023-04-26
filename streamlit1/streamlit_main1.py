from matplotlib import table
import streamlit as st

# streamlit çalışması için terminale -- streamlit run main.py(ilgili dosyanın adı)-- yazıp local host da ne yaptığımızı görebiliriz

st.title("Hi! I am Streamlit Web App")
st.subheader(("Hi! I am your Subheader"))
st.header("I am Header")
st.text("I am text function an programmers uses me inplace of paragraph tag")

st.markdown("**Hello** World") # ** yazılan kakakteri bold haline getiriyor.
# https://www.markdownguide.org/cheat-sheet/ buradan daha detaylı bakılabilir
st.markdown("# Hello World")
st.write("## H2 HEADER")
st.markdown("> Hello World")
st.markdown("---")
st.markdown("[Google](http://www.google.com)")
st.markdown("---")

st.caption("Hi I am Caption") 
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") #formül vs. yazmak için  https://katex.org/docs/supported.html

st.markdown("---")

json={"a": "1,2,3", "b":"4,5,6"}
st.json(json)

st.markdown("---")

code = """
    def func():
        print("Hello World)"""
st.code(code, language="python")

st.markdown("---")

st.metric(label = "Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹") # üzeri sayı yazmak için 120ms\-1 yazıp tab a basacağız.

st.markdown("---")
import pandas as pd
tabel = pd.DataFrame({"Column1": [1,2,3,4,5,6], "Column2":[11,12,13,14,15,16]})
st.table(tabel) # df yi tablo halinde göstermek istediğimizde 

st.markdown("---")

st.dataframe(tabel) # bu şekilde yaptığımızda aktif bir tablo elde edebiliyoruz. sıralama yapabiliyoruz.

st.markdown("---")
################## resim video ses dosyası  yükleme ########################
st.header("video resim veya ses dosyasını sayfaya nasıl yükleyebiliriz")

st.image("seldabgcn.jpg", caption="Selda BAGCAN", width=680)

st.audio(("selda.mp3"))

st.video("videoplayback.mp4")

################## kullanıcının görmesini istemediğimiz öğelerin sayfada görünmemesini sağlama ########################
# sayfada sağ üstte gözüken ayarlar bölümünü sayfadan kaldırmak için

# sayfanın inspect bölümüne girip ilgili noktaların css classlarını boşluk yerine araya nokta koyarak 
# aşağıdaki kodu kullanarak yazıyoruz böylece artık bu öğeler gözükmüyor.
# css-1rs6os edgvbvh3 öğesini css-1rs6os.edgvbvh3 şeklinde yazıyoruz.

st.markdown("""
<style>
.css-1rs6os.edgvbvh3
{
visibility: hidden;
}
.css-cio0dv.egzxvld1
{
visibility: hidden;
}
<style>
""", unsafe_allow_html=True)

################################ widgets  #################################
st.markdown("---") 
state = st.checkbox("Checkbox 1", value=True)
if state:
    st.write("CHECKED")
else:
    pass

st.markdown("---") 
def change():
    print(2+5)
st.checkbox("Checkbox 2", value=True, on_change=change) # tike dokunduğunda arkaplanda yazdığmıız fonsiyon çalışıyor

st.markdown("---") 

def change1():
    print(st.session_state.checker)
st.checkbox("Checkbox 3", value=True, on_change=change1, key="checker") # bu checker ı koyunca boolean değerler elde ediyoruz.

st.markdown("---") 

radio_btn = st.radio("in which Country do you live?", options = ("US", "UK", "Germany"))
# print(radio_btn)

st.markdown("---") 

def btn_click():
    print("Button Clicked")
btn = st.button("Click Me!", on_click=btn_click)

st.markdown("---") 

select=st.selectbox("What is your favourite car?", options=("Audi", "VW", "BMW"))
#print(select)

multi_select = st.multiselect("What is your favourite Tech Brand?", options=("Microsoft", "Apple", "Amazon", "Google", "Oracle"))
st.write(multi_select)

# run komutunu durdurmak için terminalde ctrl+C yapmamız yeterli