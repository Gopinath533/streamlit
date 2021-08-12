import streamlit as st

st.sidebar.title('Home')
menu = ["Home Page","LOG IN","sign up"]
choice = st.sidebar.selectbox("Menu",menu)



if choice == "Home Page":
    st.title("HOME PAGE")
    st.balloons()

if choice == "LOG IN":
    st.title("LOG IN")
    EmailID = st.text_input("EmailID")
    password1 = st.text_input("Password",type = "password")
    if st.button("submit"):
        st.title("Login success")
        st.balloons()


if choice == "sign up":
    st.title("SIGN UP")
    firstname = st.text_input("First name")
    lastname = st.text_input("Last name")
    Email = st.text_input("Email ID")
    pwd = st.text_input("password",type = "password")
    if st.button("submit"):
        result = firstname.title()
        reslut1 = lastname.title()
        reslut2 = Email.title()
        st.success("{} has created successfully".format(firstname))
        st.success(result)
        st.success(reslut1)
        st.success(reslut2)