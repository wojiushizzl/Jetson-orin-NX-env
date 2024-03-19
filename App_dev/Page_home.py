
import os
import streamlit as st
import shutil
import ruamel.yaml
from  yolov8_train import train
from streamlit_extras.grid import grid 

yaml = ruamel.yaml.YAML()
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        st.error(f'文件夹 "{folder_name}" 已经存在。')


def create_yaml(project_name):
    file_name=project_name+'/train.yaml'
    # 复制文件
    shutil.copyfile("train.yaml", file_name)

    # 读取复制的文件并更改其中一行代码
    with open(file_name, "r", encoding="utf-8") as file:
        lines = yaml.load(file)

    path=os.path.join(project_name, 'datasets')
    if "path" in lines:
        lines["path"] =path

    # 将更改后的内容写回文件
    with open(file_name, "w", encoding="utf-8") as file:
        yaml.dump(lines, file)

def get_all_projects():
    # 获取项目文件夹下的所有文件夹列表
    folder_list = [f.name for f in os.scandir('projects') if f.is_dir()]
    return folder_list

def create_project():
    # 创建项目
    project_name = st.text_input('输入项目名称：')

    message_container = st.empty()
    folder_name = os.path.join('projects', project_name)
    if st.button('创建项目'):
        if project_name:
            try:
                create_folder(folder_name)
                subfolder_path = os.path.join(folder_name, 'datasets')
                create_folder(subfolder_path)
                imagefolder_path = os.path.join(subfolder_path, 'images')
                create_folder(imagefolder_path)
                labelfolder_path = os.path.join(subfolder_path, 'labels')
                create_folder(labelfolder_path)
                message_container.success(f'项目 "{project_name}" 创建成功！')
                create_yaml(folder_name)

            except FileExistsError:
                message_container.error(f'项目 "{project_name}" 已经存在。')
        else:
            message_container.warning('请输入项目称。')

def delete_project(selected_projects):
    #删除项目
    if st.button('删除项目'):
        if selected_projects:
            try:
                selected_projects = os.path.join('projects', selected_projects)
                # 删除文件夹及其内容
                shutil.rmtree(selected_projects)
                st.success(f'项目 "{selected_projects}" 删除成功！')
            except FileExistsError:
                st.error(f'项目 "{selected_projects}" 不存在。')
        else:
            st.warning('请选择项目。')

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

def train_project(selected_projects):
    epochs=int(st.number_input('epochs'))
    batch=int(st.number_input('batch'))

    if st.button("训练项目"):
        train(selected_projects,epochs,batch)


def homepage():
    # 创建项目
    create_project()
    # 选择项目
    projects_list=get_all_projects()
    selected_projects = st.selectbox('请选择一个项目：', projects_list)
    # 删除项目
    delete_project(selected_projects)

    # # 导入图片至目标项目
    # upload_images(selected_projects)
    # # 导入标签至目标项目
    # upload_labels(selected_projects)
    # 训练
    train_project(selected_projects)