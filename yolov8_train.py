from ultralytics import YOLO
from multiprocessing import Process, freeze_support


def train():

    # Load a model
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='coco128.yaml', epochs=50,batch=2,imgsz=640)

if __name__ =="__main__":
    freeze_support()

    p=Process(target=train)
    p.start()
    p.join()