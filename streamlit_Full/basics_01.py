import streamlit as st
import math

st.title("Hey there this is a title")#used to display a main heading (large text) at the top of your app
st.header("This is a header")#is used to display a section heading, smaller than st.title() but larger than normal text
st.subheader("This is a sub header")#smaller than header but bigger than normal text
st.text(f"This is a text ")#normal text 
st.write(f"This is wrtie {math.pi}")#normal text and also to display variables and other data types
