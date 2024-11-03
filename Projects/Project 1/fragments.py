import streamlit as st


@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].button("Toggle")
    cols[1].text_area("Text")


@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].file_uploader("Upload image")
    cols[1].date_input("Date")


toggle_and_text()
st.divider()

cols = st.columns(2)
cols[0].selectbox("Filter", ["A", "B", "C"])
cols[1].button(("Upload"))
st.divider()

filter_and_file()
