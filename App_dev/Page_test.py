import os
import streamlit as st
from  yolov8_train import train
import cv2
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import uuid
import threading
from streamlit_extras.grid import grid 



def testpage():
    st.write("test")
   