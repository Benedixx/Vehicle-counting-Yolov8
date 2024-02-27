# Vehicle counting yolov8

## Project Overview
This project aims to automate counting vehicle that passes by. The class of this object detection is all vehicle from optimus prime to motorcyle
![vlcsnap-2024-02-27-15h25m52s409](https://github.com/Benedixx/Vehicle-counting-Yolov8/assets/97221880/7b1d4944-de38-439a-8a8a-8a96fa4b491d)


## Project Inspiration
I'm inspired to do this project because i saw news headline about Dishub(traffic police in indonesia) still counting vehicle manually at ramadhan event 2023
![image](https://github.com/Benedixx/Vehicle-counting-Yolov8/assets/97221880/50210587-26f0-4a27-b168-42290e214d8f)

## Dataset

The dataset used for this project can be found [here](https://universe.roboflow.com/ikan-vzjcv/traffic-f8dmr). It consists of traffic picture with vehicle that already annotated. you can export the dataset with yolov8 yaml format.

## Installation
```
git clone https://github.com/ultralytics/yolov8
cd yolov8
pip install ultralytics==8.0.196
git clone https://github.com/ultralytics/ultralytics.git
```

## usage
```
python main.py
```

## Training Result
### yolov8m result
![alt text](results.png)


## Future Development
* some optimus prime is poorly detected and motorcyle is rarely get detected
* Need to clean the code ofc hehehehehehe ٩(◕‿◕｡)۶


