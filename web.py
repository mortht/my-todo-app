import streamlit as st
import functions

functions.init_todos()
todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.save_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to increase your productivity.")

for idx, todo in enumerate(todos):
    key = 'todo-' + str(idx)
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(idx)
        functions.save_todos(todos)
        del st.session_state[key]
        st.rerun()

st.text_input(label="New Todo:", placeholder="Add a new todo ...",
              key='new_todo', on_change=add_todo)
