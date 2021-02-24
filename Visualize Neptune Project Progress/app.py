import streamlit as st
import neptune
from neptunecontrib.viz.projects import project_progress
from neptunecontrib.api.utils import extract_project_progress_info
import altair as at

project = neptune.init(project_qualified_name='mwitiderrick/LightGBM', api_token='eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vdWkubmVwdHVuZS5haSIsImFwaV91cmwiOiJodHRwczovL3VpLm5lcHR1bmUuYWkiLCJhcGlfa2V5IjoiMmRkMDI5NGItYTJjYy00Yjc0LWE0OTEtM2FiMjE1MmVmZjA0In0=')

def get_progress_data():
    leaderboard = project.get_leaderboard()
    progress_df = extract_project_progress_info(leaderboard,
                                            metric_colname='running_time',
                                            time_colname='created')
    return progress_df
    
progress_df = get_progress_data()

def visualize_progress():
    plot = project_progress(progress_df, width=400, heights=[50, 200])
    st.altair_chart(plot)

if __name__ == "__main__":
    visualize_progress()


