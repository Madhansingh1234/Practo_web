import streamlit as s

name=s.text_input("Enter your name")
fname=s.text_input("Enter your father name")
adr=s.text_area("Enter your addresss")
classdata=s.selectbox("Enter your class :",(1,2,3,4,5,6))

button=s.button("Done")

if button:
    s.markdown(f'''Name:{name} \n Father name:{fname} \n address :{adr} class:{classdata}''')
    

