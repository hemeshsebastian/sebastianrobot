from ultralytics import YOLO
model=YOLO("flower55.pt")
model.predic(source=0,show=True)
