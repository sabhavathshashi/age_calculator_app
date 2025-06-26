import streamlit as st
from datetime import date

st.title("AGE CALCULATOR APP")
st.subheader("CALCULATE YOUR AGE BY GIVING YOUR DATE OF BIRTH")

today = date.today()
min_dob = date(1990,1,1,)
max_dob = date.today()
default_dob = date(2000,1,1)

dob = st.date_input("enter your date of birth:",min_value=min_dob,max_value=max_dob,value = default_dob)
if dob > today:
    st.write("Entered dob is incorrrect!")
elif dob < today :
    st.write(f"Entered dob is {dob}")
    
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
st.write(f"Your age is {age}")

if age > 18 :
    st.write("You are a major and you can drive vehicle ")
elif age < 18 :
    st.write("You are a minor and you can't drive vehicle")
    