import streamlit as st
import function

todos=function.get_todos()

def add_todo():
    todo1=st.session_state["new_todo"] + "\n"
    print(todo1)
    todos.append(todo1)
    function.write_todos(todos)

todos=function.get_todos()
st.title("My TO-DO APP")
st.subheader("This app is designed by Shubham Gugaliya")
st.write("This will help you to increase your productivity and maintain your daily activities")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="add new todo...",on_change=add_todo,key="new_todo")