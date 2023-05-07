import streamlit as st
import os
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

st.title('Diary Tone')

files = os.listdir('diary')
result = SentimentIntensityAnalyzer()
dates = []
positive_values = []
negative_values = []


for file in files:
    with open(f'diary/{file}', 'r') as f:
        file_content = f.read()
    score = result.polarity_scores(file_content)
    dates.append(file.strip('.txt'))
    positive_values.append(score['pos'])
    negative_values.append(score['neg'])

st.subheader('Positivity')
figure = px.line(x=dates, y=positive_values, labels={'x': 'Date', 'y': 'Positive values'})
st.plotly_chart(figure)


st.subheader('Negativity')
figure = px.line(x=dates, y=negative_values, labels={'x': 'Date', 'y': 'Negative values'})
st.plotly_chart(figure)
