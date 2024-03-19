import os
import streamlit as st
from  yolov8_train import train
import cv2
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import uuid
import threading
from streamlit_extras.grid import grid 
from streamlit_card import card

def example():
    card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )
    card(
        title="Hello Wodd!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )


def testpage():
    st.write("test")
    my_grid = grid([2,2,2,2,2], [2, 2],[2,2], vertical_align="bottom")
    with my_grid.container():
        card(
            title="Hello World!",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    with my_grid.container():
        card(
            title="Hellod!",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    with my_grid.container():
        card(
            title="Hed World!",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    with my_grid.container():
        card(
            title="Hdd!",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
    with my_grid.container():
        card(
            title="Hello Word",
            text="Some description",
            image="http://placekitten.com/300/250",
            url="https://www.google.com",
        )
