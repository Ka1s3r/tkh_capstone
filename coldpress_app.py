# #importing the libraries
# import pandas as pd
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns
# import glob
# from sklearn.linear_model import LinearRegression

# murders = [5.1, 4.8, 4.6, 4.6, 4.9, 5.1, 5.6, 6.2, 6.9, 7.3, 7.9, 8.6,
# 9.0, 9.4, 9.8, 9.6, 8.7, 8.8, 9.0, 9.8, 10.2, 9.8, 9.1, 8.3, 7.9, 8.0,
# 8.6, 8.3, 8.4, 8.7, 9.4, 9.8, 9.3, 9.5, 9.0, 8.2, 7.4, 6.8, 6.3, 5.7,
# 5.5, 5.6, 5.6, 5.7, 5.5, 5.6, 5.7, 5.6, 5.4, 5.0, 4.8, 4.7, 4.7, 4.5,
# 4.4, 4.9, 5.4, 5.3, 5.0, 5.0]
# murders = pd.Series(murders)

# # Here we'll iterate through all the csv's, turn them into dataframes, then put them in a list.
# # Then we'll stack them all on top of each other as a single dataframe, hence axis = 0.

#  #self_ex
# path = r'~\Desktop\Coldpress_Lighthous\code\1920_News'
# #all_files = glob.glob(path + "/*.csv") # Grab all CSVs in this location.
# li = [] # List to put them all in.
# for filename in all_files:
#     df = pd.read_csv(filename, index_col=None, header=0)
#     li.append(df)
# frame = pd.concat(li, axis=0, ignore_index=True)

# df = frame[frame.sentence.str.contains('murder')]

# def row_count(df):
#     article_count = [] # Establish empty list in which to hold counts for each year.
#     for year in range(1960, 2020): #2020 is excluded
#         l = (len(df[df.year == year])) # Get length of df with murders for that year
#         article_count.append(l)

#     return article_count

# article_count = pd.Series(row_count(df))

# years = pd.Series(df.year.unique())

# m_df = pd.concat([years, article_count, murders], axis=1)
# m_df.columns = ['year', 'article_count','murders']

# m_df

# #this is the line plot axis 0 = murder and axis 1 = article
# sns.set(rc = {'figure.figsize':(25,10)})

# fig, axes = plt.subplots(1, 2)

# sns.lineplot(x = 'year', y = 'murders',data = m_df, ax = axes[0])
# sns.lineplot(x = 'year', y = 'article_count',data = m_df, ax = axes[1])

# axes[0].set_title("Murders")
# axes[1].set_title("Articles")

# '''
# Absolute value of r | Strength of relationship
# r < 0.25| No relationship
# 0.25 < r < 0.5| Weak relationship
# 0.5 < r < 0.75| Moderate relationship
# r > 0.75| Strong relationship

# '''

# # heat map showing the correlation
# corr_murders = sns.heatmap(m_df.corr(), center = 0,  annot=True)

# # When murder goes up, so do the number of articles about murders.
# # As the years go by, the murder rate decreases.
# # As the years go by, however, the article count is only weakly tied to that.

# #

# # Plot another line on the same chart/graph
# plt.plot(m_df.year, m_df.murders, 'r', label='Murders')

# plt.legend()
# plt.show()


# #articles

# plt.plot(m_df.year, m_df.article_count, 'b', label='Articles')

# plt.legend()
# plt.show()

# creating the app to store the information
# imports for different libraries 

from operator import index
from dateutil.relativedelta import relativedelta
import datetime as dt
import altair as alt
from matplotlib import container
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

#creating a path for csv
path = 'murder_rate_vs_article_rate_2.csv'
m_df = pd.read_csv(path)


# title and header
# Creating the App: Title & Header
with st.container():
    col1, col2 = st.columns(2)
# with col2:
#     lighthouse_image = 'lighthouse_waves.JPEG'
#     st.image(lighthouse_image, width=200)

st.title('Career Team 2: ColdPress')

# This line of code will present the heat graph and the statement explaining the map
with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.title("Hypothesis: ")
        st.write(""" On the question of correlation between events occuring in the real world, and the rate at which articles about those events are published:

Ho: The correlation between events and their report-rate is strong (r >= 0.75). 

Ha: The correlation between events and their report-rate is not strong (r < 0.75).
        
        """)
    with col2: 
        question_image = 'question_mark_PNG56.png'
        st.image(question_image, width=200)


with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.title("Methods:")
        st.write("""

1. These data were taken from the New York Times API, and can be found here: 

https://www.kaggle.com/datasets/tumanovalexander/nyt-articles-data
   
   Data on the murder rate for each year were taken from the FBI database and can be found here: 
   
   https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/topic-pages/tables/table-1

2. These data were retrieved in the form of 60 csvs, one for each year from 1960 to 2019. These csv’s were then turned into a glob-object using the glob library. We iterated through the object, turning each csv into a Pandas DataFrame, concatenating them vertically to create a time series based dataframe in Pandas. 

3. We then filtered the rows of the resulting DataFrame by any keyword we choose, generating a sub-DataFrame.

4. We created a function which takes a DataFrame where years are the time measure, and steps through a range of years, counting the number of times we encounter an event (articles in this case) for each year.

5. This was used to engineer a new Series called “article_count” which gives us the number of articles for each year in our sub_DataFrame related to murders.      
        """)
    with col2: 
        nyt_image = '05insider-gun-sub-a-superJumbo.jpg'
        st.image(nyt_image, width=300)

        fbi_image = '920x920.jpg'
        st.image(fbi_image, width=300)

        st.write(""" 6. We also engineered a similar column by applying the same function to the main DataFrame containing all articles. This is done so that we can find out what percentage of articles in a given year were about a particular topic with regard to that particular news agency. In our demo case, the New York Times on the topic of “murder”.

7. To test this, we used FBI data from the same year range as the dataset after turning it into a Series.

8. In all, we have 5 Series: “Years”, “murder_article_count”, ”murder_rate”, “murder_article_rate_,  “all_article_count”.

9. We concatenated these series horizontally to create a single DataFrame. """)


with st.container():
    st.write('---')
    st.title("Results:")
    st.write("""
    
    
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.header("Correlation Heat Map")
        corr_murders, ax = plt.subplots()
        sns.heatmap(m_df.corr(), ax=ax, center=0, annot=True, cmap='coolwarm')
        st.write(corr_murders)
        st.write(""" 
        With 8,857,300 rows of data total, and 53,715 for our sub-DataFrame, we have enough statistical power to show that on the topic of murder, the rate at which the New York Times publishes articles about said topic, has a moderate correlation with the rate at which events occur over time, with a correlation coefficient (Pearson’s) of 0.63.
        """)
    with col2:
        st.write(''' ---
 As the murder rate goes up, so too does the rate at which articles about murder are published.
 This is however, a moderate effect, and does not support the hypothesis that there is a strong correlation between real world event-rates and their publication-rates.
 
 
 The rate of publication was chosen instead of the raw number of articles each year, since article count varies with the resources available to the news agency. 
 
 (Staff fluctuations: https://www.statista.com/statistics/192894/number-of-employees-at-the-new-york-times-company/), and other hidden factors.
 For reference, the murder rate had a weak correlation with the number of articles published about murder in any given year; r = 0.39. 
        ''')
with st.container():
    col1, col2, col3 = st.columns(3)
    st.write('---')
    # Creating a drop down menu
    # all the years that are in the dataset


    # Filtering the dataset bas on the year the user wants
    def year_range(strt_year,end_year ):
        flter = m_df.loc[m_df['year'].isin(range(strt_year, end_year))]
        
        return flter
# plots and graph data
    def plot_filter_data(df):
        fig, ax = plt.subplots()
        sns.lineplot(x= df["year"], y = df["m_art_rt"], ax = ax)
        sns.lineplot(x = df['year'], y = df["murders"], ax = ax )
        plt.show()
        st.write(fig)
    # values for the select box will return as a tuple.

    sel_box_opt = st.slider("SELECT A YEAR RANGE",value = (1959,2019), min_value = 1959, max_value = 2019, step=10)
    plot_filter_data(year_range(sel_box_opt[0], sel_box_opt[1]))
#[I'm having an  error in line 248, it is not accepting my function]
           

with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.header('Murders')
        fig2, ax = plt.subplots()
        plt.plot(m_df.year, m_df.murders, 'r', label='Murders')
        plt.legend()
        plt.show()
        st.write(fig2)

    with col2:
        st.header('Articles')
        fig3, ax = plt.subplots()
        plt.plot(m_df.year, m_df.m_art_rt, 'b', label='Articles')
        plt.legend()
        plt.show()
        st.write(fig3)


st.write(""" A closer look at the comparison, where the ranges are more comparable shows the afformentioned moderate correlation.""")

# registering to our app sidebar
# At the moment registering to this app is not needed


# st.sidebar.title("Registration Form")
# first, last = st.sidebar.columns(2)
# first.text_input("First Name")
# last.text_input("Last Name")
# email, mob = st.sidebar.columns([3, 1])
# email.text_input("Email ID")
# mob.text_input("Cell Phone Number ")

# user, pw, pw2 = st.sidebar.columns(3)
# user.text_input("Username")
# pw.text_input("Password", type="password")
# pw2.text_input("Retype your Password", type="password")

# ch, bl, sub = st.sidebar.columns(3)
# ch.checkbox("I Agree")
# sub.button("Submit")

# # calling the dataset
# st.write('---')
# st.header("Articles about Murder vs. Murder rate")

# if 'number_of_rows' not in st.session_state:
#     st.session_state['number_of_rows'] = 5
#     st.session_state['type'] = 'Categorial'

# m_df = pd.read_csv(path)

# increament = st.button('Show more')
# if increament:
#     st.session_state.number_of_rows += 1
# decrement = st.button('Show less')
# if decrement:
#     st.session_state.number_of_rows -= 1

# st.table(m_df.head(st.session_state['number_of_rows']))


# # User interaction
# with st.container():
#     col1, col2, col3 = st.columns(3)
#     st.write('---')
#     # Creating a drop down menu
#     # all the years that are in the dataset
#     with col1:
#         year_options = m_df["year"].unique().tolist()
#         year_options.sort()
#         # # Select box with the default the first year in the data
#         # year_sel_box = st.selectbox("Select year range", year_options)

#         # I need some range in the past
#         #year_range = range(1959, 2020)
#         st.slider('Select year range', min_value=1959,
#                   max_value=2019, value=[1959, 2019])
#     with col3:
#         slider_button = st.button('Click here')
#         if slider_button:
#             st.write(m_df)
#     # create a drop down menu to select Article count/ Actual count
#     with col2:
#         sel_opt = ['Actual Count', 'Article Rate']
#         sel_box_opt = st.multiselect("Choose count ", sel_opt)

    # Filtering the dataset bas on the year the user wants

    # Create a histogram plot

    # User interaction
    
# with st.container():
#     col1, col2, col3 = st.columns(3)
#     st.write('---')
#     # Creating a drop down menu
#     # all the years that are in the dataset


#     # Filtering the dataset bas on the year the user wants
#     def year_range(strt_year,end_year ):
#         flter = m_df.loc[m_df['year'].isin(range(strt_year, end_year))]
        
#         return flter
# # plots and graph data
#     def plot_filter_data(df):
#         fig, ax = plt.subplots()
#         sns.lineplot(x= df["year"], y = df["m_art_rt"], ax = ax)
#         sns.lineplot(x = df['year'], y = df["murders"], ax = ax )
#         plt.show()
#         st.write(fig)
#     # values for the select box will return as a tuple.

#     sel_box_opt = st.slider("Select the year ",value = (1959,2019), min_value = 1959, max_value = 2019, step=10)
#     plot_filter_data(year_range(sel_box_opt[0], sel_box_opt[1]))
#[I'm having an  error in line 248, it is not accepting my function]
           

#creating a multiselect search for key works to show count of relating article publish 
#The future venture of the app

st.header("Discussion:")
st.write("""ColdPress was born out of the knowledge that news has a tendency to report on things in a biased fashion. 
This divide is pretty visible in our everyday life, and in the conversations we have with others. 
With the data that we have curated from various publications and APIs, we wanted to create an app that shows you how frequently various news topics are mentioned as compared to how often these things actually occur. 
Because news reports often influence how people view the world, this is a great way to observe realistic data about the frequency of these occurrences in our society.

The future of ColdPress would provide a hub for unbiased and clear data on news topics in such a way that it is unemotional, and unprovocative. 
ColdPress would include more data on different statistics that frequently show up in the news, such as immigration, assault, and other hot button issues without being particularly triggering to the reader and without eliciting fluff pieces or op eds that could lead a reader to a particular view point. 
ColdPress should allow for readers to see the grand scale of the issues they’re interested in researching. Overall, the mission statement is plain and simple, to keep the user informed about the degree to which a particular news agency deviates from reality in terms of how information is passed on to the reader. 
ColdPress will hopefully help in understanding our news, our world, and each other a little better. 
""")

with st.container():
    path_2 = 'sample_df_7300.csv'
    df = pd.read_csv(path_2)
    
    # ignore
    def pretty(s: str) -> str:
        try:
            return dict(js="JavaScript")[s]
        except KeyError:
            return s.capitalize()


#create a function that allows the user to search topics in the article and returns topic as key and count as value to a dictionary
   
    def search_bar(df, topics):
        result_dic = {}
        topic_count = len(topics)
        index = [x for x in range(topic_count)]

        for topic in topics:
            result = df['sentence'].str.contains(topic)
            result = list(result.value_counts())[1]
            result_dic[topic] = result

        return pd.DataFrame(result_dic, index=index)

    list_of_topics = ['man', 'woman', 'pandemic','bee', 'civil war', 'capitalism', 'war', "homeless", 'safety', 'shooting', 'hate crime']
    
    topic_df = search_bar(df, list_of_topics)

    multi_sel_topics = st.multiselect(
        "Count Result per Topic", options= list_of_topics, default = list_of_topics, format_func=pretty
    )

    # PROBLEM DIRECTLY BELOW
    # plot_df =  #pd.DataFrame.from_dict()

    chart = (alt.Chart(topic_df,title="Frequency News Article Published ",).mark_bar().encode(x=alt.X("topic_count:Q", title="Frequency of Topic"),
        y=alt.Y("topics:N",sort=alt.EncodingSortField(field="Topic", order="descending"),title="Topics"),
        color=alt.Color("topics:N",legend=alt.Legend(title="Topics"),scale=alt.Scale(scheme="category10"),),
        tooltip=["name:N", "count:O"],))


st.altair_chart(chart, use_container_width=True)


