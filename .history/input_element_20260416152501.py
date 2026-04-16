import streamlit as st
st.title("Input your Information ",anchor=False)
st.divider();
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age: ",value = None,placeholder="Enter your age")
print(type(age))
pressed = st.button("Click me to see the result",button=primary)


