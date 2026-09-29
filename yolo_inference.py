from ultralytics import YOLO

MODEL_PATH = 'models/best.pt'
VIDEO_PATH = 'input_videos/cobaia.mp4'

model = YOLO(MODEL_PATH)
results = model.predict(VIDEO_PATH, save=True)

print(f"Classes do modelo: {model.names}")
    