#stremalit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcom to your Grouwt Journey!")
st.write("Emprace challenges, learn from mistakes, and unlock you full potential. This AI-powered app helps you build a grout mindset with reflection, challenges, and achievments! ✨")

# "quoute section"
st.header("📍 Today's Growth mindest Quote")
st.write("'Sucess in not final, failure is not fatal: it is the courage to continue that counts.'-Winston Churchill")

st.header("🔑 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# condition

if user_input:
    st.success(f"💪 you are facing: {user_input}, Keep pushing format towords your goal!🚀") 
else:
    st.warning("Tell us about your challenge to get started!")


# reflexing
    st.header("Reflect on Your Learning")
    reflection = st.text_area("write your reflections here:")
     
    if reflection:
        st.success(f"Great insight! your reflection: {reflection}")
    else:
        st.info("reflecting on post experience hlep you grow! Share your difficulties")
    
# achivements
st.header("🏆 Celebrate your wins!")
achievement = st.text_input("Share Someting you've recently accomplished:") 

if achievement:
    st.success(f" 💐 Amazing! you achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now! 🤩")

# footer
st.write(" - - - ")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("**⛔ Created by Irfan Zaidi**")
