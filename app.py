# -*- coding:utf-8 -*-

import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

@st.cache_data
def load_data(filename):
    df = pd.read_csv('./'+filename)
    return df

def main():
    st.title("Hello World on Streamlit.io")
    orders_df = load_data("orders.csv")

    cnt_srs = orders_df.eval_set.value_counts()

    # Plotly 그래프 생성
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cnt_srs.index,
        y=cnt_srs.values,
        marker_color='rgba(50, 171, 96, 0.6)',
        text=cnt_srs.values,
        textposition='outside',
    ))

    fig.update_layout(
        title='각 고객군의 수',
        xaxis=dict(title='고객 Type 군'),
        yaxis=dict(title='총 갯수'),
    )

    st.plotly_chart(fig)

    st.write("-"*50)

    cnt_srs = orders_df.groupby("user_id")["order_number"].aggregate(np.max).reset_index()
    cnt_srs = cnt_srs.order_number.value_counts().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
       x=cnt_srs['order_number'],
       y=cnt_srs['count'],
        marker_color='rgba(50, 171, 96, 0.6)',
        text = cnt_srs['count'],
        textposition = 'outside',
    ))

    fig.update_layout(
        title='주문 갯수 별 고객 빈도',
        xaxis=dict(title='Maximum 구매 갯수'),
        yaxis=dict(title='구매 발생 횟수'),
    )

    st.plotly_chart(fig)

    st.write("-"*50)

    cnt_srs = orders_df.groupby("order_dow")['order_id'].count().reset_index()

    dow_mapping = {0: 'saturday', 1:'sunday', 2:'monday', 3:'tuesday', 4:'wednesday', 5:'thursday', 6:'friday'}
    cnt_srs['order_dow'] = cnt_srs['order_dow'].map(dow_mapping)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x = cnt_srs['order_dow'],
        y = cnt_srs['order_id'],
        marker_color='rgba(50, 171, 96,0.6)',
        text = cnt_srs['order_id'],
        textposition = 'outside',
    ))

    fig.update_layout(
        title = '요일 별 구매량',
        xaxis=dict(title='요일'),
        yaxis=dict(title='구매량'),
    )

    st.plotly_chart(fig)

    st.write("-"*50)

    cnt_srs = orders_df.groupby('order_hour_of_day')['order_id'].count().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cnt_srs['order_hour_of_day'],
        y=cnt_srs['order_id'],
        marker_color='rgba(50, 171, 96,0.6)',
        text=cnt_srs['order_id'],
        textposition='outside',
    ))

    fig.update_layout(
        title="각 시간대별 구매 개수",
        xaxis=dict(title='시간대'),
        yaxis=dict(title='구매개수'),
    )

    st.plotly_chart(fig)

    st.write("-"*50)

    grouped_df = orders_df.groupby(['order_dow', 'order_hour_of_day'])['order_number'].aggregate('count').reset_index()
    grouped_df = grouped_df.pivot(index='order_dow', columns='order_hour_of_day', values='order_number')
    fig = go.Figure()
    fig.add_trace(go.Heatmap(
        x=grouped_df.index,
        y=grouped_df.columns,
        z=grouped_df.values,
        colorscale='Viridis'
    ))

    fig.update_layout(
        title='주문 요일 및 시간대에 따른 주문 번호 히트맵',
        xaxis=dict(title = "주문 요일"),
        yaxis=dict(title = "주문 시간대"),
    )

    st.plotly_chart(fig)

    st.write("-"*50)
if __name__ == "__main__":
    main()