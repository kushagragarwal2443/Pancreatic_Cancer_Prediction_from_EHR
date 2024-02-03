import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# st.sidebar.success("Navigate the dashboards above.")

#st.header("Google Health Sentinel :red[Covidcaster]")

# image = st.image("./Images/IDS_Project_Image.png", caption="Project Summary", use_column_width=True)


st.header('Motivation')
st.markdown('The COVID-19 pandemic has reshaped our world in unprecedented ways. The tracking of new COVID-19 cases proved to be the first line of defense in the fight against the virus. Rapid response is pivotal in containing outbreaks and preventing healthcare systems from becoming overwhelmed. Further, the understanding of the spread of outbreak allows us to make data-driven decisions like optimizing allocation of medical supplies, healthcare personnel, and vaccines. However, limited testing capacity, variability in testing protocols, stigma associated with a COVID-19 diagnosis, and fear of isolation and quarantine proved to be major challenges to early reporting and detection of COVID cases. As we enter a post-Covid world, we look for a solution to address these challenges by formulating a simple yet effective strategy to monitor and track the spread of any such infections in the future.')

st.header('Problem Statement')
st.markdown('The objective of our project is to leverage Google Search Trends data to develop a predictive model for monitoring and predicting the spread of infectious diseases. The project aims to harness the power of real-time search queries and patterns to enhance early detection, predict the spread of outbreaks, and provide timely insights to healthcare authorities. By doing so, we seek to contribute to proactive and data-driven measures in managing and mitigating infectious disease outbreaks.')

st.header('Dataset')
st.markdown('Our primary dataset is the [COVID-19 Search Trends symptoms dataset](https://github.com/GoogleCloudPlatform/covid-19-open-data/blob/main/docs/table-search-trends.md). This is an aggregated collection of anonymous search trends for different symptoms of COVID like - fever, difficulty breathing, stress etc.')

st.markdown('As part of the preprocessing of the data - a search query is first mapped to the set of relevant features, for e.g. “acid reflux and coughing up mucus” is mapped to three symptoms: Cough, Gastroesophageal reflux disease, and heartburn. Further, the data is organized by region (states) allowing us to study the popular symptoms in different geographical regions.')

st.markdown('Additional Data Source - [Daily USA county level case data](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/). To be able to capture regional trends, which were very prevalent in the COVID-19 pandemic, we plan to use this dataset as the ground truth of the number of daily cases and the number of covid related deaths in each state in USA.')

st.markdown('We intend to combine the data from the two sources which will allow us to model a relationship between the search trends for different covid-related symptoms to the actual confirmed COVID-19 cases registered in a particular geographical region during that period. This will be modeled as a forward-looking regression tasks, i.e, we ideally plan to predict the case load after two weeks by looking at the different search queries for a particular day. The 14-day lag will explain the conversion of initial symptoms to an actual COVID-19 diagnosis. This will allow authorities to prepare in advance if a sudden surge in symptom searches for a certain geographical region is observed.')

st.markdown("---")
st.markdown("_This streamlit application presents a series of interactive dashboards to visualisate the related datasets and the predictions from our tool_")
st.markdown("_Please choose a dashboard using the sidebar on the left._")