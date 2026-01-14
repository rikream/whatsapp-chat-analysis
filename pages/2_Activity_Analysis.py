import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import helper

st.title("🔥 Activity Analysis")

if 'df' not in st.session_state:
    st.warning("Please upload chat file from Home page")
    st.stop()

df = st.session_state['df']
selected_user = st.session_state['selected_user']

# -------- Monthly Timeline --------
st.title("Monthly Timeline")
timeline = helper.monthly_timeline(selected_user, df)
fig, ax = plt.subplots()
ax.plot(timeline['time'], timeline['messages'], color='green')
plt.xticks(rotation='vertical')
st.pyplot(fig)

# -------- Daily Timeline --------
st.title("Daily Timeline")
daily_timeline = helper.daily_timeline(selected_user, df)
fig, ax = plt.subplots()
ax.plot(daily_timeline['only_date'], daily_timeline['messages'], color='black')
plt.xticks(rotation='vertical')
st.pyplot(fig)

# -------- Activity Map --------
st.title("Activity Map")
col1, col2 = st.columns(2)

with col1:
    st.header("Most Busy Day")
    busy_day = helper.week_activity_map(selected_user, df)
    fig, ax = plt.subplots()
    ax.bar(busy_day.index, busy_day.values)
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

with col2:
    st.header("Most Busy Month")
    busy_month = helper.month_activity_map(selected_user, df)
    fig, ax = plt.subplots()
    ax.bar(busy_month.index, busy_month.values, color='orange')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

# -------- Heatmap --------
st.title("Weekly Activity Map")
user_heatmap = helper.activity_heatmap(selected_user, df)
fig, ax = plt.subplots()
sns.heatmap(user_heatmap, ax=ax)
st.pyplot(fig)
