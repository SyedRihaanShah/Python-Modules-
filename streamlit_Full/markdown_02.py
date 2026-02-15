import streamlit as st 

#headings -- more # more smaller heading
st.markdown("# Heading 1")
st.markdown("## Heading 2")

#font
st.markdown("**This is Bold text**")
st.markdown("*this is italic text*")

#lists
st.markdown("""
            - apple
            - banana
            """)

#links
st.markdown("[OPEN YOUTUBE](https://www.youtube.com)")

#code formatting
st.markdown("`print('Hello wrold')`")
st.markdown("""
            ```python
            print("Hello World")""")


#markdown has multiple functions instead of showing normal text

