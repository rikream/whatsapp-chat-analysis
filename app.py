import streamlit as st
import preprocesser

st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    # ---------- SAFE DECODING (PC + MOBILE) ----------
    try:
        data = bytes_data.decode("utf-8")
    except UnicodeDecodeError:
        data = bytes_data.decode("latin-1", errors="ignore")
    # -------------------------------------------------

    df = preprocesser.preprocess(data)

    user_list = df['users'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    # Store for multipage access
    st.session_state['df'] = df
    st.session_state['selected_user'] = selected_user

    st.success("Data loaded successfully ✅")
    st.info("📱 Mobile users: open the sidebar (☰) to navigate pages.")
    st.write("Use the sidebar to navigate between pages ⬅️")
