import re
import pandas as pd


def preprocess(data):
    # 🔧 REQUIRED: normalize mobile unicode characters
    data = data.replace('\u202f', ' ').replace('\u200e', '')

    # 🔧 REQUIRED: support both '-' and '–' (mobile WhatsApp uses –)
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\s[-–]\s"


    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_msg': messages, 'msg_dates': dates})
    df['msg_dates'] = pd.to_datetime(
        df['msg_dates'],
        format='%d/%m/%Y, %H:%M - ',
        errors='coerce'
    )

    users = []
    messages_clean = []

    for message in df['user_msg']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages_clean.append(entry[2])
        else:
            users.append('group_notification')
            messages_clean.append(entry[0])

    df['users'] = users
    df['messages'] = messages_clean
    df.drop(columns=['user_msg'], inplace=True)

    # ---------- Date-time features ----------
    df['year'] = df['msg_dates'].dt.year
    df['month_num'] = df['msg_dates'].dt.month
    df['month'] = df['msg_dates'].dt.month_name()
    df['only_date'] = df['msg_dates'].dt.date
    df['day_name'] = df['msg_dates'].dt.day_name()
    df['day'] = df['msg_dates'].dt.day
    df['hour'] = df['msg_dates'].dt.hour
    df['minutes'] = df['msg_dates'].dt.minute

    # ---------- Period column ----------
    period = []
    for hour in df['hour']:
        start = str(hour).zfill(2)
        end = str(hour + 1).zfill(2)
        if hour == 23:
            end = "00"
        period.append(start + "-" + end)

    df['period'] = period

    return df

