from ultralytics import YOLO
model=YOLO("flower55.pt")
model.predict(source=0,show=True)
