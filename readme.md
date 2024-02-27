# Rock paper scissor object detection

## Project Overview
This project aims to make AI as referee for rock paper scissor game using webcam as input, i use yoloV5 algorithm to detect user hand and determine the hand of left side and right side. the result is shown when the left side and right side hand is captured.
<p align="center">
  <img src="https://github.com/Benedixx/rock-paper-scissor-game/blob/main/assets/demo.gif" alt="animated" />
</p>

## Project Inspiration

## Dataset

The dataset used for this project can be found [here](https://universe.roboflow.com/ikan-vzjcv/rock-paper-scissor-coy2k). It consists of human hand that form a shape of rock, paper, scissor that already annotated. you can export the dataset with yolov5 yaml format.

## Installation
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
pip install shapely=2.0.1 & numpy=1.16.0
```

## usage
```
python main.py
```

## Training Result
### yolov5s result
![results](https://github.com/Benedixx/rock-paper-scissor-game/assets/97221880/ab3e32d5-64f7-4709-9776-3c8d473a3faa)


### yolov5m result
![results](https://github.com/Benedixx/rock-paper-scissor-game/assets/97221880/debeca0e-17c6-4e13-a73e-12107adaa4dd)

## Future Development
* The result only shown if the left hand and right hand hand is detected or at least 1 second after one of the either hand detected
* The main script need to run continuously after the round is over/result is shown
* Need to clean the code ofc hehehehehehe ٩(◕‿◕｡)۶


