import streamlit as st
import matplotlib.pyplot as plt
import helper

st.title("☁️ WordCloud")

if 'df' not in st.session_state:
    st.warning("Please upload chat file from Home page")
    st.stop()

df = st.session_state['df']
selected_user = st.session_state['selected_user']

df_wc = helper.create_WordCloud(selected_user, df)
fig, ax = plt.subplots()
ax.imshow(df_wc)
ax.axis("off")
st.pyplot(fig)

st.title("Most Common Words")
most_common_words = helper.most_common_words(selected_user, df)
fig, ax = plt.subplots()
ax.barh(most_common_words[0], most_common_words[1])
st.pyplot(fig)
