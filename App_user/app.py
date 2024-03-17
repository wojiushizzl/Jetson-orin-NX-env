#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image
import streamlit as st
import config
from utils import *

# setting page layout
st.set_page_config(
    page_title="FAHAI",
    page_icon='/home/zzl/Desktop/logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)
# main page heading
# st.title("Visualization")

# sidebar
st.sidebar.header("Model Config")

# model options
task_type = st.sidebar.selectbox(
    "Select Task",
    config.TASK_TYPE_LIST
)

model_type = None
model_type = st.sidebar.selectbox(
        "Select Model",
        config.MODEL_LIST[task_type]
    )


confidence = float(st.sidebar.slider(
    "Select Model Confidence", 30, 100, 30)) / 100

model_path = ""

if model_type:
    model_path=Path(config.MODEL_DIR[task_type],str(model_type))
else:
    st.error("Please Select Model in Sidebar")

# load pretrained DL model
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Unable to load model. Please check the specified path: {model_path}")

# image/video options
st.sidebar.header("Image/Video Config")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST,
    index=2
)

source_img = None


if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    if task_type== config.TASK_TYPE_LIST[0]:
        infer_uploaded_webcam_det(confidence, model) # Detection task


else:
    st.error("Currently only 'Image' and 'Video' source are implemented")
    

