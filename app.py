import streamlit as st
import streamlit_option_menu
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import mysql.connector as mc
import pandas as pd
import re 
 

mydb= mc.connect(host='localhost' , user='root' , password='1234' , database = 'sample4')

mycursor=mydb.cursor()

#mycursor.execute('CREATE TABLE IF NOT EXISTS Channel(channel_id VARCHAR(255) PRIMARY KEY,playlist_id VARCHAR(255),channel_name VARCHAR(255),channel_type VARCHAR(255),total_videos INT,channel_views INT,channel_description VARCHAR(255),channel_status VARCHAR(255))')



st.set_page_config(page_title= 'Phonepe Pulse Data Visualization and Exploration:',layout= 'wide',initial_sidebar_state= 'expanded')

    
#with st.sidebar:
#    opt_selected = streamlit_option_menu.option_menu('', ['Home','SQL','Previously Searched'],
#                           icons=['house','database','card-text'])


#if opt_selected=='Home':
  
option = st.selectbox('Select one option', ('','Statewise Analytics'))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#if opt_selected=='SQL':

 # option = st.selectbox(
  #   'Select one option',
   #  ('','What are the names of all the videos and their corresponding channels?',
    #     'Which channels have the most number of videos, and how many videos do they have?',
        #  'What are the top 10 most viewed videos and their respective channels?',
        # 'How many comments were made on each video, and what are their corresponding video names?',
        #  'Which videos have the highest number of likes, and what are their corresponding channel names?',
        # 'What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
        #'What is the total number of views for each channel, and what are their corresponding channel names?',
        # 'What are the names of all the channels that have published videos in the year 2022?',
        # 'What is the average duration of all videos in each channel, and what are their corresponding channel names?',
        # 'Which videos have the highest number of comments, and what are their corresponding channel names?'))

