# !pip install pandas plotly streamlit
import ast
import pandas as pd
import plotly.express as px
import streamlit as st

# Load in and clean data
pokemon_df = pd.read_csv('https://raw.githubusercontent.com/ajaverett/data/main/poke.csv')
pokemon_df['types'] = pokemon_df['types'].apply(ast.literal_eval)
all_types = list(set([x for t in pokemon_df['types'] for x in t]))
st.title('Pokémon Data Explorer')

# User chooses Pokémon type
selected_type = st.multiselect('Select a Pokémon Type', all_types)
filtered_df = pokemon_df[pokemon_df['types'].apply(lambda x: all(t in x for t in selected_type))]

# Display Pokémon stats
st.dataframe(filtered_df[['name','types','attack','defense','height_m','weight_kg']])

# Attack vs. Defense Scatter Plot
st.header('Attack vs. Defense Scatter Plot')
fig1 = (px.scatter(filtered_df, 
                   x="attack", 
                   y='defense', 
                   opacity=0.8, 
                   color='speed',
                   hover_data=['name'], 
                   trendline='ols')
        .update_traces(marker_size=12, 
                       marker_line_width=2, 
                       marker_line_color='black'))

st.plotly_chart(fig1, use_container_width=True)

# Height vs. Weight Scatter Plot
st.header('Height vs. Weight Scatter Plot')

fig2 = (px.scatter(filtered_df, 
                   x="height_m", 
                   y='weight_kg',
                   opacity=0.8, 
                   color='hp',
                   hover_data=['name'], 
                   log_x=True, 
                   log_y=True, 
                   trendline="ols", 
                   trendline_options=dict(log_x=True, log_y=True))
        .update_traces(marker_size=12, 
                       marker_line_width=2, 
                       marker_line_color='black')
)

st.plotly_chart(fig2, use_container_width=True)
