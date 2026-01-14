import streamlit as st
import matplotlib.pyplot as plt
import helper

st.title("😀 Emoji Analysis")

if 'df' not in st.session_state:
    st.warning("Please upload chat file from Home page")
    st.stop()

df = st.session_state['df']
selected_user = st.session_state['selected_user']

emoji_df = helper.emoji_helper(selected_user, df)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(emoji_df)

with col2:
    fig, ax = plt.subplots()
    ax.pie(
        emoji_df[1].head(10),
        labels=emoji_df[0].head(10),
        autopct="%0.2f"
    )
    st.pyplot(fig)
