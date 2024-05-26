# Importing Libraries
import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
import os
import json
from streamlit_option_menu import option_menu
from PIL import Image
from git.repo.base import Repo

# Setting up page configuration
icon = Image.open(r"C:\Users\HP\Downloads\pngtree-analytics-icon-design-template-vector-isolated-png-image_745938.jpg")
st.set_page_config(page_title= "Phonepe Pulse Data Visualization", page_icon= icon,
                   layout= "wide",initial_sidebar_state= "expanded")

st.sidebar.header(":wave: :green[**Hello! Welcome to the dashboard**]")

with st.sidebar:
    selected = option_menu("Menu", ["Insurance","Transactions","Users"], 
                icons=["list","list","list"],
                menu_icon="cast",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#1fad96"},
                        "nav-link-selected": {"background-color": "#1fad96"}})
    

if selected == "Transactions":
    option = st.selectbox(
     'Select one option',
       ('','Statewise Analytics'))
            
