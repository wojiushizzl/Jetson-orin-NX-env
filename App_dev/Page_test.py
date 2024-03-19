import os
import streamlit as st


def testpage():

    st.write("asdasd")
    directory_path = './projects/'

    # 获取目录下的文件夹列表
    folder_list = [folder for folder in os.listdir(directory_path) if
                   os.path.isdir(os.path.join(directory_path, folder))]

    # 在Streamlit中展示文件夹列表
    st.write("Projects 文件夹下的文件夹列表：")
    for folder in folder_list:
        st.write(folder)