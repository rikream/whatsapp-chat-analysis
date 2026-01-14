import streamlit as st
import matplotlib.pyplot as plt
import helper

st.title("📌 Chat Overview")

if 'df' not in st.session_state:
    st.warning("Please upload chat file from Home page")
    st.stop()

df = st.session_state['df']
selected_user = st.session_state['selected_user']

# -------- Top Statistics --------
num_of_msgs, total_words, num_of_media, num_of_links = helper.fetch_stats(
    selected_user, df
)

st.title("Top Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Messages", num_of_msgs)
with col2:
    st.metric("Total Words", total_words)
with col3:
    st.metric("Media Shared", num_of_media)
with col4:
    st.metric("Links Shared", num_of_links)

# -------- Most Busy Users --------
if selected_user == 'Overall':
    st.title("Most Busy Users")
    x, new_df = helper.most_busy_users(df)

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        ax.bar(x.index, x.values, color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col2:
        st.dataframe(new_df)
