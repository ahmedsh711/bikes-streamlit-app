#Import Libraries:
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('bikes.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df['day'] = df['datetime'].dt.day.astype(str)
df['month'] = df['datetime'].dt.month_name().astype(str)
df['year'] = df['datetime'].dt.year.astype(str)
df['hour'] = df['datetime'].dt.hour.astype(str)

histfunc = st.sidebar.radio('Choose Aggregation Function', ('avg', 'sum'))
period = st.sidebar.radio('Choose Time Period', ('day', 'month','year','hour'))
def page1():
    tab1 , tab2 = st.tabs(['Profit' , 'Number of Rented Bikes'])

    with tab1:
        fig = px.histogram(data_frame=df, x=period, y='Profit', histfunc=histfunc, text_auto=True)
        fig.update_xaxes(categoryorder='total descending')
        st.plotly_chart(fig)

    with tab2:
        col1 , col2 , col3 = st.columns(3)

        with col1 :
            st.subheader('Total Rented Bikes')
            fig = px.histogram(data_frame=df, x=period, y='rented_bikes_count', histfunc=histfunc, text_auto=True)
            fig.update_xaxes(categoryorder='total descending')
            st.plotly_chart(fig)

        with col2 :
            st.subheader('Registered Members')
            fig = px.histogram(data_frame=df, x=period, y='registered', histfunc=histfunc, text_auto=True)
            fig.update_xaxes(categoryorder='total descending')
            st.plotly_chart(fig)

        with col3 :
            st.subheader('Casual Members')
            fig = px.histogram(data_frame=df, x=period, y='casual', histfunc=histfunc, text_auto=True)
            fig.update_xaxes(categoryorder='total descending')
            st.plotly_chart(fig)




def page2():
    x = st.radio('Select a Feature', ('weather','season'))
    tab1, tab2 = st.tabs(['Profit' , 'Number of Rented Bikes'])
    with tab1:
      st.plotly_chart(px.histogram(data_frame= df, x= x, y= 'Profit', histfunc= histfunc, text_auto= True).update_xaxes(categoryorder = 'total descending'))

    with tab2:
      col1, col2, col3 = st.columns(3)
      with col1:
        st.subheader('Total Rented Bikes')
        st.plotly_chart(px.histogram(data_frame= df, x= x, y='rented_bikes_count', histfunc= histfunc, text_auto= True).update_xaxes(categoryorder = 'total descending'))
      with col2:
        st.subheader('Registered Members')
        st.plotly_chart(px.histogram(data_frame=df, x= x, y= 'registered', text_auto= True, histfunc= histfunc).update_xaxes(categoryorder = 'total descending'))
      with col3:
        st.subheader('Casual Member')
        st.plotly_chart(px.histogram(data_frame=df, x=x , y= 'casual',histfunc= histfunc , text_auto= True).update_xaxes(categoryorder = 'total descending'))


def page3():
  x= st.radio('Select a Feature',('windspeed','humidity','temp'))
  tab1, tab2 = st.tabs(['Profit','Number of Rented Bikes'])
  with tab1:
    st.plotly_chart(px.histogram(data_frame=df, x= x, y= 'Profit', histfunc= histfunc, text_auto= True).update_xaxes(categoryorder = 'total descending'))
  with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
      st.subheader('Total Rented Bikes')
      st.plotly_chart(px.histogram(data_frame= df, x= x, y='rented_bikes_count', histfunc= histfunc, text_auto= True).update_xaxes(categoryorder = 'total descending'))
    with col2:
      st.subheader('Registered Members')
      st.plotly_chart(px.histogram(data_frame=df, x= x, y= 'registered', text_auto= True, histfunc= histfunc).update_xaxes(categoryorder = 'total descending'))
    with col3:
      st.subheader('Casual Member')
      st.plotly_chart(px.histogram(data_frame=df, x=x , y= 'casual',histfunc= histfunc , text_auto= True).update_xaxes(categoryorder = 'total descending'))

pages = {
    "Page 1: Time-based Analysis": page1,
    "Page 2: Weather and Season": page2,
    "Page 3: Environmental Factors": page3,
}
pg = st.sidebar.radio('Navigate between pages' , pages.keys())

pages[pg]()
