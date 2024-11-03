import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")
print("before")
if st.button("Increment Counter"):
    print("after")
    st.session_state.counter += 1

if st.button("Decrement Counter"):
    st.session_state.counter -= 1

if st.button("Reset Counter"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")
