#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image
import streamlit as st
import os

# setting page layout
st.set_page_config(
    page_title="FAHAI_dev",
    page_icon='/home/zzl/Desktop/logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)

# sidebar
st.sidebar.header("Develop Bar")


# select project



# model options
task_type = st.sidebar.selectbox(
    "Select Task",
    ['dataset','train','test','deploy']
)



