import pandas as pd
import streamlit as st
import plotly.express as px
import neptune

project = neptune.init(project_qualified_name='mwitiderrick/LightGBM', api_token='eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vdWkubmVwdHVuZS5haSIsImFwaV91cmwiOiJodHRwczovL3VpLm5lcHR1bmUuYWkiLCJhcGlfa2V5IjoiMmRkMDI5NGItYTJjYy00Yjc0LWE0OTEtM2FiMjE1MmVmZjA0In0=')
@st.cache(ttl=60)
def get_leaderboard_data():
    leaderboard = project.get_leaderboard()
    return leaderboard
    
df = get_leaderboard_data()

def visualize_leaderboard_data():
    fig = px.pie(
        df,
        hole=0.2,
        values="running_time",
        names="parameter_boosting_type",
        title="Running time vs Parameter boosting type",
        color_discrete_sequence=px.colors.sequential.Blackbody,
    )
    st.plotly_chart(fig)

if __name__ == "__main__":
    visualize_leaderboard_data()


