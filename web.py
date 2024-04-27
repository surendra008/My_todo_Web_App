import  streamlit as st
import functions as fu

todos = fu.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    fu.write_todos(todos)

st.title('My Todo APP')
st.subheader('This is My Todo APP')
#st.sidebar.title('My Todo APP')

st.text_input(label="", placeholder="Add a todo item",on_change=add_todo,key="new_todo")


for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fu.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


