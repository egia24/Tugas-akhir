# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_resource
#mendefinisikan dan mengambil data
def load_shunyi():
    Shunyi = pd.read_csv("../data/PRSA_Data_Shunyi_20130301-20170228.csv")
    return Shunyi
Shunyi = load_shunyi()

#mendefinisikan dan mengambil data
def load_Huairou():
    Huairou = pd.read_csv("../data/PRSA_Data_Huairou_20130301-20170228.csv")
    return Huairou
Huairou = load_Huairou()

#mendefinisikan dan mengambil data
def load_Wanliu():
    Wanliu = pd.read_csv("../data/PRSA_Data_Wanliu_20130301-20170228.csv")
    return Wanliu
Wanliu = load_Wanliu()

#membuat sebuah markdown nama dan email
st.sidebar.markdown("Nama: Egia Suranta Perangin-Angin")
st.sidebar.markdown("Email : egiasuranta24@gmail.com")

#membuat checkbox untuk menampilkan data set shunyi
if st.sidebar.checkbox("Dataset Shunyi"):
    st.subheader("Raw Data")
    st.write(Shunyi)
#membuat checkbox untuk menampilkan data set huairou
if st.sidebar.checkbox("Dataset Huairou"):
    st.subheader("Data set Huairou")
    st.write(Huairou)

#membuat checkbox untuk menampilkan data set wanliu
if st.sidebar.checkbox("Dataset Wanliu"):
    st.subheader("Data set wanliu")
    st.write(Wanliu)


# create a layout with two columns
col1,col2 = st.columns(2)

with col1:
    st.header('The relationship between PM2.5 and PM10 in Shunyi')
    plt.scatter(x=Shunyi['PM2.5'], y=Shunyi['PM10'])
    plt.xlabel('PM2.5')
    plt.ylabel('PM10')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Tampilkan plot menggunakan st.pyplot() di Streamlit
    st.pyplot()
with col2:
    # biggest CO increase in Huairou
    st.header('Biggest CO increase in Huairou')
    st.bar_chart(Huairou.set_index('year')['CO'])

    # Menggunakan Seaborn untuk membuat plot bar
    st.header('SO2 distribution in Winliu')
    sns.barplot(y=Wanliu["year"], x=Wanliu["SO2"], orient="h", color='red')
    plt.xlabel("SO2")
    plt.title("SO2 distribution in wanliu")

    # Menampilkan plot menggunakan st.pyplot() di Streamlit
    st.pyplot()

#description
st.sidebar.info("Dashboard ini dibuat untuk menunjukkan relasi, data peningkatan atau penyebaran udara")
