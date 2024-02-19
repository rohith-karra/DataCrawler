import os
import psycopg2
import matplotlib.pyplot as plt
import pandas as pd

from datetime import datetime
from wordcloud import WordCloud
from flask import request
from flask import Flask, render_template,send_file


#worldcloud generator for youtube
yt_data = pd.read_csv("top_words_yt.csv")
words = yt_data["Title"].tolist()
wordcloud = WordCloud().generate(str(words))
wordcloud.to_file("youtube_wordcloud.png")

#worldcloud generator for Reddit
reddit_data = pd.read_csv("top_words_reddit.csv")
words = reddit_data["Title"].tolist()
wordcloud = WordCloud().generate(str(words))
wordcloud.to_file("reddit_wordcloud.png")

#worldcloud generator for Twitter
# twitter_data = pd.read_csv("top words_yt.csv")
#words = twitter_data["Title"].tolist()
#wordcloud = WordCloud().generate(str(words))
#wordcloud.to_file("Twitter_wordcloud.png")

app = Flask(__name__)


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

#connecting to database 
def get_db_connection():
    conn = psycopg2.connect(host='127.0.0.1',
                            database='pulldata',
                            user='postgres',
                            password='postgres')
    return conn

#returns sample data from three platforms based on user input
@app.route('/query',methods=['POST','GET'])
def index():
    if 'text' in request.args and 'platform' in request.args:
        conn = get_db_connection()
        cur = conn.cursor()
        text = str(request.args.get('text'))
        platform=str(request.args.get('platform'))

        if(platform=="youtube"):
            cur.execute("SELECT * FROM "+platform+"_data where tags like '%"+text+"%' limit 5;")

        elif(platform=="twitter"):
            cur.execute("SELECT * FROM "+platform+"_data where text like '%"+text+"%' limit 5;")
            
        else:
            cur.execute("SELECT * FROM "+platform+"_data where title like '%"+text+"%' limit 5;")
        fetch = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('query.html', fetch=fetch)
    else:
        return render_template('base.html')


@app.route('/',methods=['POST','GET'])
def default():
    return render_template('index.html')

@app.route("/wordcloud")
def default1():
    return render_template('word.html')

@app.route('/youtube',methods=['POST','GET'])
def show_wordcloud():
    return send_file("youtube_wordcloud.png", mimetype="image/png")

@app.route('/reddit',methods=['POST','GET'])
def show_wordcloud1():
    return send_file("reddit_wordcloud.png", mimetype="image/png")

@app.route('/sentiment',methods=['POST','GET'])
def sentiment():
    if 'sentiment_type1' in request.args:
        sentiment_type1 = request.args.get('sentiment_type1')
        if sentiment_type1 == 'positive':
            df = pd.read_csv('sentiment scores.csv')
            df = df.sort_values(by=['positive'], ascending=False)
            title = df['Title'].values.tolist()
            positive = df['positive'].values.tolist()
            negative = []
            neutral = []
            if 'start_percent' in request.args and 'end_percent' not in request.args:
                start_percent = request.args.get('start_percent')
                start = abs((int(start_percent) / 100) * len(title))
                title = title[int(start):]
                positive = positive[int(start):]
            if 'start_percent' not in request.args and 'end_percent' in request.args:
                end_percent = request.args.get('end_percent')
                end = abs((int(end_percent) / 100) * len(title))
                title = title[:int(end)]
                positive = positive[:int(end)]
            if 'start_percent' in request.args and 'end_percent' in request.args:
                start_percent = request.args.get('start_percent')
                end_percent = request.args.get('end_percent')
                start = abs((int(start_percent) / 100) * len(title))
                end = abs((int(end_percent) / 100) * len(title))
                title = title[int(start):int(end)]
                positive = positive[int(start):int(end)]
                return render_template('stacked_bar.html', title='Positive Sentiment Chart', names=title,positive=positive,neutral=neutral, negative=negative)
            else:
                return render_template('stacked_bar.html', title='Positive Sentiment Chart', names=title,positive=positive,neutral=neutral, negative=negative)
            
        elif sentiment_type1 == 'neutral':
            df = pd.read_csv('sentiment scores.csv')
            df = df.sort_values(by=['neutral'], ascending=False)
            title = df['Title'].values.tolist()
            positive = []
            negative = []
            neutral = df['neutral'].values.tolist()
            if 'start_percent' in request.args and 'end_percent' not in request.args:
                start_percent = request.args.get('start_percent')
                start = abs((int(start_percent) / 100) * len(title))
                title = title[int(start):]
                positive = positive[int(start):]
            if 'start_percent' not in request.args and 'end_percent' in request.args:
                end_percent = request.args.get('end_percent')
                end = abs((int(end_percent) / 100) * len(title))
                title = title[:int(end)]
                positive = positive[:int(end)]
            if 'start_percent' in request.args and 'end_percent' in request.args:
                start_percent = request.args.get('start_percent')
                end_percent = request.args.get('end_percent')
                start = abs((int(start_percent) / 100) * len(title))
                end = abs((int(end_percent) / 100) * len(title))
                title = title[int(start):int(end)]
                neutral = positive[int(start):int(end)]
                return render_template('stacked_bar.html', title='Neutral Sentiment Chart', names=title,positive=positive, neutral=neutral,negative=negative)
            else:
                return render_template('stacked_bar.html', title='Neutral Sentiment Chart', names=title,positive=positive, neutral=neutral,negative=negative)

            
        elif sentiment_type1 == 'negative':
            df = pd.read_csv('sentiment scores.csv')
            df = df.sort_values(by=['negative'], ascending=False)
            title = df['Title'].values.tolist()
            positive = []
            negative = df['negative'].values.tolist()
            neutral = []
            if 'start_percent' in request.args and 'end_percent' not in request.args:
                start_percent = request.args.get('start_percent')
                start = abs((int(start_percent) / 100) * len(title))
                title = title[int(start):]
                positive = positive[int(start):]
            if 'start_percent' not in request.args and 'end_percent' in request.args:
                end_percent = request.args.get('end_percent')
                end = abs((int(end_percent) / 100) * len(title))
                title = title[:int(end)]
                positive = positive[:int(end)]
            if 'start_percent' in request.args and 'end_percent' in request.args:
                start_percent = request.args.get('start_percent')
                end_percent = request.args.get('end_percent')
                start = abs((int(start_percent) / 100) * len(title))
                end = abs((int(end_percent) / 100) * len(title))
                title = title[int(start):int(end)]
                neutral = positive[int(start):int(end)]
                return render_template('stacked_bar.html', title='Negative Sentiment Chart', names=title,positive=positive,neutral=neutral, negative=negative)
            else:
                return render_template('stacked_bar.html', title='Negative Sentiment Chart', names=title,positive=positive, neutral=neutral,negative=negative)                
    elif 'sentiment_type1' not in request.args:
        df = pd.read_csv('sentiment scores.csv')
        df['total_cnt'] = df.apply(lambda row: row.positive + row.neutral + row.negative, axis=1)
        df = df.sort_values(by=['total_cnt'], ascending=False)
        print(df.head())
        title = df['Title'].values.tolist()
        positive = df['positive'].values.tolist()
        negative = df['neutral'].values.tolist()
        neutral = df['negative'].values.tolist()
        
        if 'start_percent' in request.args and 'end_percent' not in request.args:
            start_percent = request.args.get('start_percent')
            start = abs((int(start_percent) / 100) * len(title))
            title = title[int(start):]
            neutral = positive[int(start):]
            return render_template('stacked_bar.html', title='Sentiment Chart Analysis', names=title,positive=positive, neutral=neutral,negative=negative)
        if 'start_percent' not in request.args and 'end_percent' in request.args:
            end_percent = request.args.get('end_percent')
            end = abs((int(end_percent) / 100) * len(title))
            title = title[:int(end)]
            neutral = positive[:int(end)]
            return render_template('stacked_bar.html', title='Sentiment Chart Analysis', names=title,positive=positive, neutral=neutral,negative=negative)
        if 'start_percent' in request.args and 'end_percent' in request.args:
            start_percent = request.args.get('start_percent')
            end_percent = request.args.get('end_percent')
            start = abs((int(start_percent) / 100) * len(title))
            end = abs((int(end_percent) / 100) * len(title))
            title = title[int(start):int(end)]
            neutral = positive[int(start):int(end)]
            return render_template('stacked_bar.html', title='Sentiment Chart', names=title,positive=positive, neutral=neutral,negative=negative)
        else:
            return render_template('stacked_bar.html', title='Sentiment Chart', names=title,positive=positive, neutral=neutral,negative=negative)


@app.route('/timeseries',methods=['POST','GET'])
def line():
    if 'start_date' in request.args and 'end_date' in request.args:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        df = pd.read_csv('final_twitter_time.csv')
        df['newdate'] = None
        df['newdate']=df.date.str.split(' ').str[0].tolist()
        df['newdate'] = df['newdate'].astype('datetime64[ns]')
        df['date'] = df['date'].astype('datetime64[ns]')
        df['newdate'] = df['newdate'].astype(str)
        df["newdate"] = pd.to_datetime(df["newdate"])

        after_start_date = df["newdate"] >= start_date
        before_end_date = df["newdate"] <= end_date
        between_two_dates = after_start_date & before_end_date
        filtered_dates = df.loc[between_two_dates]

        filtered_dates['date'] = filtered_dates['date'].apply(str)
        filtered_dates['date']=filtered_dates.date.str.split(' ').str[0].tolist()
        date_list = filtered_dates['date'].values.tolist()

        count_labels = filtered_dates['cnt'].values.tolist()
        line_labels=date_list
        line_values=count_labels
        return render_template('timeseries.html', title='Timeseries', max=130000, labels=line_labels, values=line_values)
    else:
        return render_template('time.html')
      
if __name__ == '__main__':
    app.run()