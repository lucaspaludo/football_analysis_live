from ultralytics import YOLO

MODEL_PATH = 'yolo26x.pt'
VIDEO_PATH = 'input_videos/cobaia.mp4'

model = YOLO(MODEL_PATH)
results = model.predict(VIDEO_PATH, save=True)

print(model.names)

for box in results[0].boxes:
    print(box.xyxy, box.conf, box.cls)