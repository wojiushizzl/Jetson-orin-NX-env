#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import os
import streamlit as st
import hydralit_components as hc
import datetime
from Page_home import homepage
from Page_dataset import datasetPage
from Page_test import testpage


#make it look nice from the start
st.set_page_config(
    page_title="FAHAI_dev",
    page_icon='/home/zzl/Desktop/logo.png',
    layout='wide',
    initial_sidebar_state='collapsed',)

# specify the primary menu definition
menu_data = [
    {'icon': "far fa-copy", 'label':"Dataset"},
    {'icon': "far fa-chart-bar", 'label':"Page2"},#no tooltip message
]

over_theme =  {'txc_inactive': 'white','menu_background':'#000080'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)

#get the id of the menu item clicked
st.info(f"{menu_id}")


if menu_id=='Home':
    homepage()

if menu_id=='Dataset':
    datasetPage()


if menu_id=='Page2':
    testpage()