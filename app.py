import streamlit as st
import pandas as pd


st.title("Cryptocurrency Data")

df= pd.read_json('table_data.json',)
df_reset = df.reset_index(names='sino')

# Display the table using st.table
st.table(df_reset)