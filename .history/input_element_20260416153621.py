import streamlit as st
st.title("Input your Information ",anchor=False)
st.divider();
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age: ",value = None,placeholder="Enter your age")
print(type(age))
profession = st.selectbox("Choose your profession:",
                          ("Doctor","Teacher","Engineer","Businessman"),
                          index = None,
                          accept_new_options= True)
pressed = st.button("Click me to see the result",type="primary")
print(type(profession))
if pressed:
    st.write(f"Your name is {name} and your age is {age}");
else:
    st.write("Provide your information first")


