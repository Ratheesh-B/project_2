# Importing Libraries
import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
import os
import json
from streamlit_option_menu import option_menu
from PIL import Image
import mysql.connector as mc

mydb= mc.connect(host='localhost' , user='root' , password='1234' , database = 'sample4')
mycursor=mydb.cursor()

#mycursor.execute('CREATE TABLE IF NOT EXISTS Channel(channel_id VARCHAR(255) PRIMARY KEY,playlist_id VARCHAR(255),channel_name VARCHAR(255),channel_type VARCHAR(255),total_videos INT,channel_views INT,channel_description VARCHAR(255),channel_status VARCHAR(255))')
#mycursor.execute('CREATE TABLE IF NOT EXISTS Channel(channel_id VARCHAR(255) PRIMARY KEY,playlist_id VARCHAR(255),channel_name VARCHAR(255),channel_type VARCHAR(255),total_videos INT,channel_views INT,channel_description VARCHAR(255),channel_status VARCHAR(255))')


def getTransactions():
    path = "C:\\Users\\HP\\Dataset\\pulse\\data\\aggregated\\transaction\\country\\india\\state"
    Agg_state_list=os.listdir(path)
    clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
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
                    clm['Transaction_type'].append(l['name'])
                    clm['Transaction_count'].append(l['paymentInstruments'][0]['count'])
                    clm['Transaction_amount'].append(l['paymentInstruments'][0]['amount'])
                    clm['State'].append(i)
                    clm["Year"].append(j)
                    clm["Quater"].append(k)
    Agg_Trans=pd.DataFrame(clm)                  
    return Agg_Trans

def getInsurance():
    path = "C:\\Users\\HP\\Dataset\\pulse\\data\\aggregated\\insurance\\country\\india\\state"
    Agg_state_list=os.listdir(path)
    clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
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
                    clm['Transaction_type'].append(l['name'])
                    clm['Transaction_count'].append(l['paymentInstruments'][0]['count'])
                    clm['Transaction_amount'].append(l['paymentInstruments'][0]['amount'])
                    clm['State'].append(i)
                    clm["Year"].append(j)
                    clm["Quater"].append(k)
    Agg_ins=pd.DataFrame(clm)                    
    return Agg_ins

def getUsers():
    path = "C:\\Users\\HP\\Dataset\\pulse\\data\\aggregated\\user\\country\\india\\state"
    Agg_state_list=os.listdir(path)
    users={'State':[], 'Year':[],'Quater':[],'Registeredusers':[]}
    
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
                registeredusers = js['data']["aggregated"]["registeredUsers"]
                users['State'].append(i)
                users["Year"].append(j)
                users["Quater"].append(k)
                users['Registeredusers'].append(registeredusers)
    Agg_Users=pd.DataFrame(users)                  
    return Agg_Users    

def getInsuranceMap(df):
    fig1 = px.choropleth(
                  df,
                  geojson="https://gist.githubusercontent.com/Ratheesh-B/84642d9197b0a2b93785585fb45a887f/raw/a093adf6dd2ff3a189d523ae944b146027d96815/india_states.geojson",
                  featureidkey='properties.ST_NM',
                  locations = 'State',
                  color = 'Transaction_count',
                  color_continuous_scale='blugrn')
    fig2 = px.bar(df, x="Transaction_count", y="State",color='Transaction_count',color_continuous_scale = 'blugrn', orientation='h')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig1,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)

def getTransactionsMap(df):
    fig1 = px.choropleth(
                  df,
                  geojson="https://gist.githubusercontent.com/Ratheesh-B/84642d9197b0a2b93785585fb45a887f/raw/a093adf6dd2ff3a189d523ae944b146027d96815/india_states.geojson",
                  featureidkey='properties.ST_NM',
                  locations = 'State',
                  color = 'Transaction_count',
                  color_continuous_scale='blugrn') 
    fig2 = px.bar(df, x="Transaction_count", y="State", color = 'Transaction_count', color_continuous_scale = 'blugrn' , orientation='h')
    fig1.update_traces(showscale=False)
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig1,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)

def getUsersMap(df):
    fig1 = px.choropleth(
                  df,
                  geojson="https://gist.githubusercontent.com/Ratheesh-B/84642d9197b0a2b93785585fb45a887f/raw/a093adf6dd2ff3a189d523ae944b146027d96815/india_states.geojson",
                  featureidkey='properties.ST_NM',
                  locations = 'State',
                  color = 'Registeredusers',
                  color_continuous_scale='blugrn')
    fig2 = px.bar(df, x="Registeredusers", y="State", color = 'Registeredusers', color_continuous_scale = 'blugrn' , orientation='h')    
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig1,use_container_width=True)
    st.plotly_chart(fig2,use_container_width=True)


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
    option = st.selectbox('Select one option',('','Nationwide Total Insurance'))
    if(option == 'Nationwide Total Insurance'):
        df = getInsurance()
        avl_year = getInsurance()
        l=[]
        l.append(' ')
        l.append('all')
        years = df.Year.unique()
        l.extend(years)
        suboption = st.selectbox('Select the year',l)
        if(suboption == 'all'):
            data = df[['State','Transaction_count']]
            df = data.groupby(by ="State").sum()
            df.reset_index(inplace = True)
            getInsuranceMap(df)
        elif(suboption!=' '):
            y = str(suboption)
            data_f = df[df['Year'] == y]    
            data_frame = data_f[['State','Transaction_count']]
            fin_data = data_frame.groupby(by ="State").sum()
            fin_data.reset_index(inplace = True)
            getInsuranceMap(fin_data) 


if selected == "Transactions":
    option = st.selectbox(
     'Select one option',
       ('','Nationwide Total Transactions'))
    if(option == 'Nationwide Total Transactions'):
        df = getTransactions()
        avl_year = getTransactions()
        l=[]
        l.append(' ')
        l.append('all')
        years = df.Year.unique()
        l.extend(years)
        suboption = st.selectbox('Select the year',l)
        if(suboption == 'all'):
            data = df[['State','Transaction_count']]
            df = data.groupby(by ="State").sum()
            df.reset_index(inplace = True)
            getTransactionsMap(df)
        elif(suboption!=' '):
            y = str(suboption)
            data_f = df[df['Year'] == y]    
            data_frame = data_f[['State','Transaction_count']]
            fin_data = data_frame.groupby(by ="State").sum()
            fin_data.reset_index(inplace = True)
            getTransactionsMap(fin_data) 
           
if selected =="Users":
    option = st.selectbox(
     'Select one option',
       ('','Nationwide Total Users'))
    if(option == 'Nationwide Total Users'):
        df = getUsers()
        avl_year = getTransactions()
        l=[]
        l.append(' ')
        l.append('all')
        years = df.Year.unique()
        l.extend(years)
        suboption = st.selectbox('Select the year',l)
        if(suboption == 'all'):
            st.write(':green[Total Number of Registered users ]')
            data = df[['State','Registeredusers']]
            df = data.groupby(by ="State").sum()
            df.reset_index(inplace = True)
            getUsersMap(df)
        elif(suboption!=' '):
            st.write(':green[Total Number of Registered users ]')
            y = str(suboption)
            data_f = df[df['Year'] == y]    
            data_frame = data_f[['State','Registeredusers']]
            fin_data = data_frame.groupby(by ="State").sum()
            fin_data.reset_index(inplace = True)
            getUsersMap(fin_data) 
        
                   
            
