import streamlit as st

def greet():
    st.write("INPUT CHNAGED")

def name(nem_first):
    st.write("hello", nem_first)

name = st.text_input("Enter your name",#makes a entry brox with the label give and there are many arguments you can pass
                     #value='name', # sets the intial value when nothing is written
                     max_chars=15, # sets the maximum number of charcters we can give either int or none
                     key='name1',# makes unique identity for similar entry widgets and labels you can either give int or str as parameter
                     type="default",# you can use either "default" or "password"
                     help='Enter a valid name ', #adds a icon to show text releated to the topic 
                     autocomplete='name',
                    #  on_change=greet
                    on_change=name, args=("rihaan",), # arguments passed to on_change function
                    placeholder='example@gmail.com', # adds a transparent text to the widget
                    disabled=False, # true or false
                    label_visibility="visible"
                     )

