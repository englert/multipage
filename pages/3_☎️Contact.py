import streamlit as st
import sqlite3
conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()


st.title("Contact")

def form():
    st.write("Ez egy Form")
    with st.form(key="Information form"):
        name = st.text_input("Enter your name: ")
        age = st.text_input("Enter your age: ")
        college = st.text_input("Enter your College name: ")
        date = st.date_input("Dátum: ")
        submission = st.form_submit_button(label="Submit")
        if submission == True:
            add_data(name, age, college, date)
            st.success("Successfully submitted")

def add_data(a,b,c,d):
    cur.execute("""CREATE TABLE IF NOT EXISTS clg_form(NAME TEXT(50), AGE TEXT(50), CLGNAME TEXT(50), DATE TEXT(50));""")
    cur.execute("INSERT INTO clg_form VALUES (?,?,?,?)", (a,b,c,d))
    conn.commit()
    conn.close()
    st.success("Succesfully submitted sqlite3")

form()
