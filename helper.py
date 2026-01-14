from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    num_of_msgs = df.shape[0]

    words = []
    for message in df['messages']:
        words.extend(message.split())
    total_words = len(words)

    num_of_media = df[df['messages'] == '<Media omitted>\n'].shape[0]

    links = []
    extracter = URLExtract()
    for message in df['messages']:
        links.extend(extracter.find_urls(message))
    total_links = len(links)

    return num_of_msgs, total_words, num_of_media, total_links


def most_busy_users(df):
    x = df['users'].value_counts().head()
    df = round((df['users'].value_counts() / df.shape[0] * 100), 2)\
            .reset_index()\
            .rename(columns={'users': 'name', 'count': 'percent'})
    return x, df


def create_WordCloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r', encoding='utf-8')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    temp = df[df['users'] != 'group_notification']
    temp = temp[temp['messages'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(
        width=600,
        height=600,
        min_font_size=10,
        background_color='#0f172a'
    )

    temp['messages'] = temp['messages'].apply(remove_stop_words)
    text = temp['messages'].dropna().str.cat(sep=" ")

    return wc.generate(text)


def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r', encoding='utf-8')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    temp = df[df['users'] != 'group_notification']
    temp = temp[temp['messages'] != '<Media omitted>\n']

    words = []
    for message in temp['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    return pd.DataFrame(Counter(words).most_common(20))


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    emojis = []
    for message in df['messages'].dropna():
        for ch in message:
            if ch in emoji.EMOJI_DATA:
                emojis.append(ch)

    return pd.DataFrame(Counter(emojis).most_common())


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    timeline = df.groupby(
        ['year', 'month_num', 'month']
    ).count()['messages'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(
            timeline['month'][i] + "-" + str(timeline['year'][i])
        )

    timeline['time'] = time
    return timeline


def daily_timeline(selected_user, df):
    return df.groupby('only_date').count()['messages'].reset_index()


def day_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    return df.groupby('day_name').count()['messages'].reset_index()


def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]

    return df.pivot_table(
        index='day_name',
        columns='period',
        values='messages',
        aggfunc='count'
    ).fillna(0)
