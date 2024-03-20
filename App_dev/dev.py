#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import streamlit as st
import hydralit_components as hc
import datetime
from Page_home import homepage
from Page_dataset import datasetPage
from Page_train import trainpage
from streamlit_option_menu import option_menu

# make it look nice from the start
st.set_page_config(
    page_title="FAHAI_dev",
    page_icon='/home/zzl/Desktop/logo.png',
    layout='wide',
    # initial_sidebar_state='collapsed',
)
def get_all_projects():
    # 获取项目文件夹下的所有文件夹列表
    folder_list = [f.name for f in os.scandir('projects') if f.is_dir()]
    return folder_list

# 选择项目
projects_list = get_all_projects()
# 1. as sidebar menu
with st.sidebar:
    selected_project = option_menu(
        "Select Projects",
        options=projects_list,
        # icons=['house'],
        menu_icon="cast",
        default_index=0
    )

menu_data = [
    {'icon': "far fa-copy", 'label': "Datasets"},
    {'icon': "far fa-chart-bar", 'label': "Train"},  # no tooltip message
]

over_theme = {'txc_inactive': 'white', 'menu_background': '#000080'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    use_animation=True,
    home_name='Home',
    login_name='Q&A',
    hide_streamlit_markers=True,  # will show the st hamburger as well as the navbar now!
    sticky_nav=True,  # at the top or not
    sticky_mode='pinned',  # jumpy or not-jumpy, but sticky or pinned
)

# get the id of the menu item clicked
# st.info(f"{menu_id}")


if menu_id == 'Home':
    homepage(selected_project)

if menu_id == 'Datasets':
    datasetPage(selected_project)

if menu_id == 'Train':
    trainpage(selected_project)
