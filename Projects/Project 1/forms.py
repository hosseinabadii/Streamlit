import streamlit as st

st.title("User Information Form")

form_values = {
    "name": "",
    "age": None,
    "gender": None,
    "dob": None,
    "location": None,
}

with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Name")
    form_values["age"] = st.number_input("Age")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["dob"] = st.date_input("Date of Birth")
    form_values["location"] = st.selectbox("Location", ["Delhi", "Mumbai", "Chennai"])

    submit_button = st.form_submit_button(label="Submit")
if submit_button:
    if not all(form_values.values()):
        st.warning("Please fill in all the required fields.")
    else:
        st.balloons()
        st.write("### Info")
        for key, value in form_values.items():
            st.write(f"{key}: {value}")
