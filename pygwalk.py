import streamlit as st
import pandas as pd
import pygwalker as pyg
from PIL import Image


page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
background:linear-gradient(rgb(17,121,191),rgb(0,77,122),rgb(0,16,36));
}
</style>
"""
st.set_page_config(page_title="sample data visualization",page_icon=":tada:",layout="wide")
st.markdown(page_bg_img,unsafe_allow_html=True)
image = Image.open('zf_logo.png')

st.image(image, width=100)

st.header('Sample ConAct data')
st.subheader('Pneumatic Clutch Actuation data from vehicles')


@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df = load_data("Book1 (17k).csv")


def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str
config = load_config('config(book1).json')
#pyg.walk(df.head(10500), env='Streamlit', dark='dark', spec=config)
pyg.walk(df, env='Streamlit', dark='dark', spec=config)
