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

def model_config():
    # model options
    task_type = st.selectbox(
        "Select Task",
        config.TASK_TYPE_LIST
    )

    model_type = None
    model_type = st.selectbox(
            "Select Model",
            config.MODEL_LIST[task_type]
        )


    confidence = float(st.slider(
        "Select Model Confidence", 30, 100, 30)) / 100

    model_path = ""

    if model_type:
        model_path=Path(config.MODEL_DIR[task_type],str(model_type))
    else:
        st.error("Please Select Model in Sidebar")

    # load pretrained DL model
    try:
        model,classes = load_model(model_path)
        st.write(classes)
    except Exception as e:
        st.error(f"Unable to load model. Please check the specified path: {model_path}")
    return task_type,model,confidence

def source_switch():
    # image/video options
    source_selectbox = st.selectbox(
        "Select Source",
        config.SOURCES_LIST,
        index=2
    )
    return source_selectbox


def target_select():
    ### find the classes from the project , output classes selected list ###
    target_list=st.multiselect("Target",[1,2,3,],default=[1])
    return target_list

def logic_select():
    ### select the logic  ###
    logic=st.multiselect("Logic",[1,2,3,],default=[1])
    return logic

def output_select():
    ### select the output ###
    output_list=st.multiselect("Output",[1,2,3,],default=[1])
    reaction_speed=int(st.slider(
        "Select Reaction Speed", 10, 100, 30)) 
    return output_list,reaction_speed


# sidebar
st.sidebar.header("Customer Config")
with st.sidebar:
    with st.expander("Model Config", expanded=True):
        task_type,model,confidence=model_config()
    with st.expander("Video&Image Switch", expanded=False):
        source_selectbox=source_switch()
    with st.expander("Target Select", expanded=False):
        target_list=target_select()
    with st.expander("Logic Select",expanded=False):
        logic_list=logic_select()
    with st.expander("Output Select",expanded=True):
        output_list,reaction_speed=output_select()


source_img = None


if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    if task_type== config.TASK_TYPE_LIST[0]:
        infer_uploaded_webcam_det(confidence, model,reaction_speed) # Detection task


else:
    st.error("Currently only 'Image' and 'Video' source are implemented")
    

