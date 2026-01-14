# 📊 WhatsApp Chat Analysis (Streamlit App)

A multipage **Streamlit web application** to analyze WhatsApp chat exports and visualize insights such as message trends, activity patterns, word usage, and emojis.

---

## 🚀 Features

- 📌 **Chat Overview**
  - Total messages
  - Total words
  - Media shared
  - Links shared
  - Most active users

- 🔥 **Activity Analysis**
  - Monthly timeline
  - Daily timeline
  - Most busy day & month
  - Weekly activity heatmap (Day × Hour)

- ☁️ **WordCloud**
  - Word cloud visualization
  - Most common words (after removing stopwords)

- 😀 **Emoji Analysis**
  - Emoji frequency table
  - Top emojis pie chart

- 👤 **User-wise & Overall Analysis**
  - Filter insights for individual users or entire group

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**
- **Emoji**
- **URLExtract**

---

## 📂 Project Structure

WhatsuppChat-Analysis/
│
├── app.py # Home page (file upload & user selection)
├── preprocesser.py # Chat preprocessing & feature extraction
├── helper.py # Analysis & visualization helpers
├── stop_hinglish.txt # Stopwords file
├── requirements.txt # Project dependencies
│
└── pages/
├── 1_Chat_Overview.py
├── 2_Activity_Analysis.py
├── 3_Wordcloud.py
└── 4_Emoji_Analysis.py


---

## 📥 How to Use

### 1️⃣ Export WhatsApp Chat
- Open WhatsApp
- Select a chat → **Export chat**
- Export **without media**
- Save the `.txt` file

---

### 2️⃣ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

3️⃣ Upload Chat File
Use the sidebar to upload your WhatsApp .txt file
Select Overall or a specific user
Navigate through pages from the sidebar

🌐 Deployment
This app is deployed using Streamlit Community Cloud (free).
Steps:
Push project to GitHub
Go to 👉 https://share.streamlit.io
Select repository & app.py

Deploy 🚀
📌 Notes
Group notifications are excluded from text analysis
Media messages (<Media omitted>) are ignored
Stopwords are removed using stop_hinglish.txt

📜 License
This project is for educational and learning purposes.

🙌 Author
Developed by Rikim