import os
import streamlit as st
from  yolov8_train import train
import cv2
from PIL import Image
from streamlit_webrtc import webrtc_streamer
import uuid
import threading
from streamlit_extras.grid import grid 

def upload_images(selected_projects):
    # 创建一个用于保存图片的文件夹
    target_folder = os.path.join('projects', selected_projects)
    target_folder = os.path.join(target_folder, "datasets")
    target_folder = os.path.join(target_folder, "images")
    # 上传图片文件
    uploaded_files = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    # st.write(uploaded_files)


    # 将上传的图片保存到指定文件夹中
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            # 获取上传文件的文件名
            filename = os.path.join(target_folder, uploaded_file.name)
            # 保存文件
            with open(filename, "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success(f"图片已成功保存到 {filename}。")

def upload_labels(selected_projects):
    # 创建一个用于保存标签的文件夹
    target_folder = os.path.join('projects', selected_projects)
    target_folder = os.path.join(target_folder, "datasets")
    target_folder = os.path.join(target_folder, "labels")

    # 上传标签文件
    uploaded_files = st.file_uploader("上传标签", type=["txt"], accept_multiple_files=True)
    # st.write(uploaded_files)

    # 将上传的标签保存到指定文件夹中
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            # 获取上传文件的文件名
            filename = os.path.join(target_folder, uploaded_file.name)
            # 保存文件
            with open(filename, "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success(f"标签已成功保存到 {filename}。")


def get_all_projects():
    # 获取项目文件夹下的所有文件夹列表
    folder_list = [f.name for f in os.scandir('projects') if f.is_dir()]
    return folder_list



lock = threading.Lock()
img_container = {"img": None}

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    # img = frame
    with lock:
        img_container["img"] = img
    return frame


def datasetPage():

    my_grid = grid([2], [2, 2],[2,2], vertical_align="bottom")

    # Row 1:
    projects_list=get_all_projects()
    selected_projects = my_grid.selectbox('请选择一个项目：', projects_list)
    # Row 2:
    with my_grid.expander("导入图片", expanded=False):
        # 导入图片至目标项目
        upload_images(selected_projects)
    with my_grid.expander("导入标签", expanded=False):
        # 导入标签至目标项目
        upload_labels(selected_projects)

    with my_grid.container():
        webrtc_ctx=webrtc_streamer(key="demo",video_frame_callback=video_frame_callback)
    image_name=str(uuid.uuid4())+".png"
    target_folder = os.path.join('projects', selected_projects)
    target_folder = os.path.join(target_folder, "datasets")
    target_folder = os.path.join(target_folder, "images")
    save_path = os.path.join(target_folder, image_name)
    img=img_container["img"]
    if img is not None:
        pil_image=Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    with my_grid.container():        
        if st.button("save"):
            pil_image.save(save_path)
            st.success(f"Saved to {save_path}  successfully")
            st.image(pil_image)
