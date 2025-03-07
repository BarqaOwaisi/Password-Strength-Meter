import streamlit as st
import random
import string

st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔑", layout="centered")

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter Your Password:", type="password")
score = 0

if password:

    common_passwords = {
    "123456", "123456789", "qwerty", "password", "12345", "12345678",  
    "111111", "123123", "password1", "1234abcd", "admin", "qwerty123",  
    "1234567", "letmein", "welcome", "abc123", "password123", "1q2w3e4r",  
    "654321", "987654321", "name123", "123", "000000", "zaq12wsx", "sunshine"
}
    if password in common_passwords :
        st.error ("❌ This password is too common! Please choose a stronger one. 🚨")
    else :
        if len(password) >= 8:
          score += 1
        else:
          st.warning("⚠️ Password should be at least 8 characters long!")
    
        if any(digit in password for digit in "0123456789"):
           score += 1
        else:
           st.warning("⚠️ The password should contain at least one digit! 🔢")
    
        if any(char in password for char in "!@#$%^&*()-_+=~`{}[]|:;'<>,.?/"):
           score += 1
        else:
          st.warning("⚠️ The password should contain at least one special character! 💥")
    
        upper = any(char.isupper() for char in password)
        lower = any(char.islower() for char in password)
    
        if upper and lower:
          score += 2
        else:
          st.warning("⚠️ The password should contain both uppercase and lowercase letters! 🔠🔡")

    st.subheader("Generate a strong password")

    def genword () :
        characters= string.ascii_letters+string.digits+"!@#$%^&*()-_+=~`{}[]|:;'<>,.?/"
        password = "".join(random.choice(characters) for _ in range(11))
        return(password)
    if st.button("Generate Strong Password"):
        st.text_input(f"Suggested Password:",genword())

    
    st.subheader(f"🔢 Password Strength Score: {score}/5")
    if score == 5 :
        st.success("🔒✅Very Strong Password🔒")
    elif score == 4:
        st.success("✅ Strong Password! 🔒")
    elif score == 3:
        st.info("⚠️ Moderate Password! Consider making it stronger. 🛠️")
    else:
        st.error("❌ Weak Password! Please improve it. 🚨")
