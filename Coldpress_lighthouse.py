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

import altair as alt
from matplotlib import container
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

path = 'murder_rate_vs_article_rate_2.csv'
m_df = pd.read_csv(path)


# title and header
# Creating the App: Title & Header
with st.container():
    col1, col2 = st.columns(2)
with col2:
    lighthouse_image = 'lighthouse_waves.jpeg'
    st.image(lighthouse_image, width=200)

st.title('ColdPress Lighthouse')
st.write('''
        Coldpress intends to show that the increase or decrease in the frequency of news reports on a particular event type, 
        does not necessarily align with the true frequency of events in real time within that particular category.

        ''')

# This line of code will present the heat graph and the statement explaining the map

with st.container():
    st.write('---')
    col1, col2 = st.columns(2)
    with col1:
        st.header("Correlation Heat Map")
        corr_murders, ax = plt.subplots()
        sns.heatmap(m_df.corr(), ax=ax, center=0, annot=True, cmap='coolwarm')
        st.write(corr_murders)
    with col2:
        st.write("Heat map explained: ")

        st.write(''' Here we can see that the rate at which articles about this topic are published each year has a moderate correlation to murder rate in a given year; while not shown here, the article count had a weak correlation to the murder rate.
                     Since crime rises and falls throughout the years, there is only a weak correlation between the murder rate, and time.
                ''')

        st.write('''The article rate was used, instead of the article count due to the fact that this fluctuates wildly based on resources available to the news agency in any given year, 
                     including the number of news staff available in any given year.''')

        st.write('''Staff fluctuations: https://www.statista.com/statistics/192894/number-of-employees-at-the-new-york-times-company/

                     These data were taken from the New York Times API, and can be found here: https://www.kaggle.com/datasets/tumanovalexander/nyt-articles-data

                     Data on the murder rate for each year were taken from the FBI database and can be found here: https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/topic-pages/tables/table-1''')

# cod
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


# registering to our app sidebar


st.sidebar.title("Registration Form")
first, last = st.sidebar.columns(2)
first.text_input("First Name")
last.text_input("Last Name")
email, mob = st.sidebar.columns([3, 1])
email.text_input("Email ID")
mob.text_input("Cell Phone Number ")

user, pw, pw2 = st.sidebar.columns(3)
user.text_input("Username")
pw.text_input("Password", type="password")
pw2.text_input("Retype your Password", type="password")

ch, bl, sub = st.sidebar.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")

# calling the dataset
st.write('---')
st.header("Articles about Murder vs. Murder rate")

if 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows'] = 5
    st.session_state['type'] = 'Categorial'

m_df = pd.read_csv(path)

increament = st.button('Show more')
if increament:
    st.session_state.number_of_rows += 1
decrement = st.button('Show less')
if decrement:
    st.session_state.number_of_rows -= 1

st.table(m_df.head(st.session_state['number_of_rows']))


# User interaction
with st.container():
    col1, col2, col3 = st.columns(3)
    st.write('---')
    # Creating a drop down menu
    # all the years that are in the dataset
    with col1:
        year_options = m_df["year"].unique().tolist()
        year_options.sort()
        # # Select box with the default the first year in the data
        # year_sel_box = st.selectbox("Select year range", year_options)

        # I need some range in the past
        #year_range = range(1959, 2020)
        st.slider('Select year range', min_value=1959,
                  max_value=2019, value=[1959, 2019])
    with col3:
        slider_button = st.button('Click here')
        if slider_button:
            st.write(m_df)
    # create a drop down menu to select Article count/ Actual count
    with col2:
        sel_opt = ['Actual Count', 'Article Rate']
        sel_box_opt = st.multiselect("Choose count ", sel_opt)

    # Filtering the dataset bas on the year the user wants

    # Create a histogram plot


# with container:

#     st.header("Interactive Graph")
#     st.altair_chart(m_df, use_container_width=True)

#     st.header("Compare actual count with article count by year")

#     instructions = """
#     Click and drag line chart to select and pan date interval\n
#     Hover over bar chart to view downloads\n
#     Click on a bar to highlight that package
#     """
#     select_packages = st.multiselect(
#         "Select ",
#         year_options,
#         default=[
#             1961,
#             2019,
#         ],
#         help=instructions,
#     )

#     select_packages_df = pd.DataFrame(m_df).rename(columns={0: "project"})

#     if not select_packages:
#         st.stop()

#     filtered_df = m_df[
#         m_df["year"].isin(m_df["year"])
#     ]

#     st.altair_chart(m_df(filtered_df), use_container_width=True)
