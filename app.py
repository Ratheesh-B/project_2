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


def getTransactions():
    path = "C:\\Users\\HP\\Dataset\\pulse\\data\\aggregated\\transaction\\country\\india\\state"
    Agg_state_list=os.listdir(path)
    clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
    for i in Agg_state_list:
        p_i=path+"\\"+i+"\\"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+"\\"+j+"\\"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                js=json.load(Data)
                for l in js['data']['transactionData']:
                    clm['Transacion_type'].append(l['name'])
                    clm['Transacion_count'].append(l['paymentInstruments'][0]['count'])
                    clm['Transacion_amount'].append(l['paymentInstruments'][0]['amount'])
                    clm['State'].append(i)
                    clm["Year"].append(j)
                    clm["Quater"].append(k)
    Agg_Trans=pd.DataFrame(clm)
    data = Agg_Trans[['State','Transacion_count']]
    df = data.groupby(by ="State").sum()
    df.reset_index(inplace = True)                 
    return df

def getTransactionsMapping(df):
    fig = px.choropleth(
                  df,
                  geojson="https://gist.githubusercontent.com/Ratheesh-B/84642d9197b0a2b93785585fb45a887f/raw/a093adf6dd2ff3a189d523ae944b146027d96815/india_states.geojson",
                  featureidkey='properties.ST_NM',
                  locations = 'State',
                  color = 'Transacion_count',
                  color_continuous_scale='blugrn')
        
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)

# Setting up page configuration
icon = Image.open(r"C:\Users\HP\Downloads\pngtree-analytics-icon-design-template-vector-isolated-png-image_745938.jpg")
json_data = json.load(open(r"C:\Users\HP\Downloads\states_india.geojson","r"))
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
    

if selected =="Insurance":
    st.write("under development")


if selected == "Transactions":
    option = st.selectbox(
     'Select one option',
       ('','Statewise Analytics'))
    if(option == 'Statewise Analytics'):
        df = getTransactions()
        getTransactionsMapping(df)
        

if selected =="Users":
    st.write("under development")            
            
