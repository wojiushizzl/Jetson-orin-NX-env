# from ultralytics import YOLO
# import cv2
# 加载模型
# model = YOLO('weights/detection/marking_work.pt')  # 加载官方模型

# 使用模型进行预测
# results = model('../../datasets/MissingPartsCLS/train/NonMissingParts/IMG_20231127_085731.jpg')  # 对图像进行预测
# results = model.track('../../datasets/打码视频3.mp4',conf=0.75,save=True)  # 对图像进行预测

# # print(results)
#
#
# # 导出模型
# # model.export(format='onnx')
#


#
# import torch
# print(torch.version.cuda)   # CUDA版本
# print(torch.cuda.is_available())   # torch能否成功调用CUDA

from paddleocr import  PaddleOCR,draw_ocr

ocr=PaddleOCR(use_angle_cls=True,lang="en")
img_path='./img/??'
result=ocr.ocr(img_path,cls=True)
for idx in range(len(result)):
    res=result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')