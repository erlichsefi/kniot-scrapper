#%%
import pandas as pd
import streamlit as st
import numpy as np
import datetime
#%%
#@st.cache
def load_data():
    import os
    import datetime
    files_in_dir = os.listdir("dumps") 

    files = [] 
    for store_name in files_in_dir:
        if store_name.startswith("."):
            continue
        for xml in os.listdir("dumps/%s" % store_name): 
            file_name, store_number, date = xml.split(".")[0].split("-")
            date = datetime.datetime.strptime(date, '%Y%m%d%H%M')
            files.append((file_name,store_number,date,store_name))

    df = pd.DataFrame(files,columns=['file','branch store','date','store name'])
    df['branch store'] = df['branch store'].astype(int)
    return df.set_index('date'),files_in_dir
#%%


#%%
st.title('Files collected')

data_load_state = st.text('Loading data...')
df, stores_name = load_data()
update = df[df.index>datetime.datetime(2020,8,1)].groupby(["store name",'date'])['branch store'].count().reset_index()
import plotly.express as px
# Plotly figure 1
fig = px.line(update, x='date', y='branch store',
              color="store name")
fig.update_layout(title='Productivity, Europe' , showlegend=False)
st.plotly_chart(fig)
# %%
