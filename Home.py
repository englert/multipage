import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="HelloHome",
    page_icon="👋",
)
components.iframe("https://embed.lottiefiles.com/animation/91045")

st.title("Home Main Page")
st.sidebar.success("Select a page above.")



if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)



