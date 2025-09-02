import streamlit as st

st.set_page_config(layout="wide")

# === Page Setup ===
jasa_omc = st.Page(
    page="views/jasa_omc.py",
    title="Jasa Operasi Modifikasi Cuaca",
    icon="🌧️",
    default=True
)
kelayakan = st.Page(
    page="views/jasa_kelayakan.py",
    title="Jasa Studi Kelayakan Operasi Modifikasi Cuaca",
    icon="📑"
)
survey = st.Page(
    page="views/jasa_survey.py",
    title="Jasa Survey Lokasi & Commissioning",
    icon="📍"
)
omc_darat = st.Page(
    page="views/jasa_omc_darat.py",
    title="Jasa OMC Wahana Darat",
    icon="🚚"
)

supervisi = st.Page(
    page="views/supervisi.py",
    title="Supervisi Pelaksanaan OMC",
    icon="🛠️"
)

# === Navigation ===
pg = st.navigation({
    "Layanan Modifikasi Cuaca": [jasa_omc, kelayakan, survey, omc_darat,  supervisi]
})

pg.run()