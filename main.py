from ultralytics import YOLO
import torch
import cv2 
import numpy as np
import pathlib
import matplotlib.pyplot as plt
from contextlib import redirect_stdout
import time
# Load a model
model = YOLO("D:\TITO\Documents\Deep-learning\yolov8\\runs\detect\\train\weights\\best.pt")  
vehicle_count = 0
history = {}
counted_ids = set()

def predict(chosen_model, img, classes=[], conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf, verbose=False)
    else:
        results = chosen_model.track(img, conf=conf, persist=True, verbose=False)
    return results

def predict_and_detect(chosen_model, img, classes=[], conf=0.4):
    results = predict(chosen_model, img, classes, conf=conf)
    boxes = results[0].boxes.xywh.cpu()
    track_ids = results[0].boxes.id.int().cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    names = results[0].names
    track_history = {}
    
    for box, track_id, cls in zip(boxes, track_ids, clss):
        x, y, w, h = (box[0] - box[2] / 2).int().item(), (box[1] - box[3] / 2).int().item(), box[2].int().item(), box[3].int().item()
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
        center_box = (int(x + w / 2), int(y + h / 2))
        track_history[track_id] = center_box
        cv2.circle(img, center_box, 5, (0, 255, 0), -1)
        cv2.putText(img, f"{names[cls]}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_PLAIN, 1, (10, 0, 255), 1)
    return img, results, center_box, track_history

cap = cv2.VideoCapture('D:\TITO\Documents\Deep-learning\yolov8\data\data.mp4')

frame_count = 0
start_time = time.time()
fps = 0
detection_history = []

while True:
    success, img = cap.read()
    width = img.shape[1]
    height = img.shape[0]

    if not success:
        print("no video found")
        break
    
    result_img, _, center_box, track_history = predict_and_detect(model, img, classes=[], conf=0.5)
    
    # center of object goes to bottom
    for track_id, center in track_history.items():
        if center[1] > height - 150 and track_id not in counted_ids:
            vehicle_count += 1
            counted_ids.add(track_id)
            print(track_id, "is at the bottom, Vehicle count:", vehicle_count)
        
    frame_count += 1
    if frame_count % 10 == 0:
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time
    
    cv2.putText(result_img, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(result_img, f"Vehicle count: {vehicle_count}", (width-300, height-200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 
    cv2.line(result_img, (0, height-150), (width, height-150), (0, 0, 255), 10)
    cv2.imshow("Image", result_img)
    
    
    
    if cv2.waitKey(1) == 27: # Esc key 
        break