import streamlit as st
st.title("Input your Information ",anchor=False)
st.divider();
name = st.text_input("Enter your name:")
st.write("Your name is: ", name);
age = st.number_input("Enter your age: ",value = None,placeholder="Enter your age")
print(type(age))
st.write("Your age is ", age)


