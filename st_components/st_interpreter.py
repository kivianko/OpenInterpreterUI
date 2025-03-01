import streamlit as st

def setup_interpreter():
    try:
        st.session_state['interpreter'].reset()
    except:
        pass
        
    if st.session_state['api_choice'] == 'openrouter':    
        st.session_state['interpreter'].api_key = st.session_state['openrouter_key']
    elif st.session_state['api_choice'] == 'openapi':     
        st.session_state['interpreter'].api_key = st.session_state['openai_key']
    
    st.session_state['interpreter'].conversation_filename = st.session_state['current_conversation']["id"]
    st.session_state['interpreter'].conversation_history = True
    st.session_state['interpreter'].messages = st.session_state.get(
        'messages',
        st.session_state.get('mensajes',[])
    )
    st.session_state['interpreter'].model = st.session_state['model']
    st.session_state['interpreter'].context_window = st.session_state['context_window']
    st.session_state['interpreter'].temperature = st.session_state['temperature']
    st.session_state['interpreter'].max_tokens = st.session_state['max_tokens']
    st.session_state['interpreter'].system_message = st.session_state['system_message']
    st.session_state['interpreter'].auto_run = True

    # Debug
    # st.write(interpreter.__dict__)
    # st.write(f'{interpreter.conversation_history_path=}')
    # st.write(f'{interpreter.conversation_filename =}')
