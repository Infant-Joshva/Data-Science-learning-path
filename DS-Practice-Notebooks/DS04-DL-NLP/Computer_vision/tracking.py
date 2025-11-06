from ultralytics import YOLO
from pathlib import Path

model_path = Path("C:/Users/infan/OneDrive/Desktop/Data Science Guvi Py(Git)/Data-Science-learning-path/DS-Practice-Notebooks/DS04-DL-NLP/Computer_vision/model/best.pt")
video_path = Path("C:/Users/infan/OneDrive/Desktop/Data Science Guvi Py(Git)/Data-Science-learning-path/DS-Practice-Notebooks/DS04-DL-NLP/Computer_vision/bold_washer.mp4")

model = YOLO(model_path)
# model.track(source=video_path, show=True)
