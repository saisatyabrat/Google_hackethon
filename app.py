import streamlit as st
import google.generativeai as genai



f = open('keys\.gemini.txt')
api_key = f.read()
genai.configure(api_key=api_key)


st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .title {
        font-size: 36px;
        color: #333333;
        text-align: center;
        padding-top: 20px;
        padding-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #555555;
        text-align: center;
    }
    .chat-container {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set title and subtitle
st.markdown('<h1 class="title">❤️‍🩹 Welcome to my latest project ❤️‍🩹</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Google\'s Hackathon</h2>', unsafe_allow_html=True)


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                            system_instruction="""You are a AI chat bot name as Chiti 
                            what ever user ask their query you have to explain the question and write the 
                            answer in case if you dont know the answer dont provide wrong information just
                            politely say you are unable to 
                            answer this question""")
if 'google' not in st.session_state:
    st.session_state['google']= []

st.chat_message("AI").write("Hii...how can i help you?")

chat = model.start_chat(history=st.session_state['google'])

for mes in chat.history:
    st.chat_message(mes.role).write(mes.parts[0].text)


user_input = st.chat_input()
if user_input:
    st.chat_message("user").write(user_input)
    response = chat.send_message(user_input)
    st.chat_message("AI").write(response.text)
    st.session_state['google'] = chat.history
