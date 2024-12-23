# Codsoft Internship Projects

This repository contains the projects I worked on during my internship with Codsoft. Each project demonstrates a unique implementation of AI/ML concepts and practical application of programming techniques.

---

## Table of Contents
1. [Movie Recommendation System](#movie-recommendation-system)
2. [Rule-Based Chatbot](#rule-based-chatbot)
3. [Face Detection and Recognition](#face-detection-and-recognition)

---

## Movie Recommendation System
### Overview
This project is a content-based recommendation system designed to suggest movies similar to a selected title. The application leverages data processing and similarity metrics to identify and display top recommendations.

### Key Features
- Movie title-based recommendations.
- Fetches movie posters dynamically using TMDB API.
- Displays the top 5 recommendations with their respective posters.

### Tools and Libraries
- **Python**
- **Streamlit**: For creating the web interface.
- **Pickle**: For saving and loading preprocessed datasets and similarity scores.
- **Requests**: For accessing TMDB API.

### How It Works
1. Loads preprocessed movie datasets and similarity metrics.
2. Users select a movie title from a dropdown menu.
3. Recommends and displays similar movies along with their posters.

---

## Rule-Based Chatbot
### Overview
This project implements a simple rule-based chatbot to handle predefined questions and provide responses. It was designed as an introductory step into conversational AI.

### Key Features
- Predefined responses for specific queries.
- Basic NLP for keyword matching and response generation.

### Tools and Libraries
- **Python**
- **Regex**: For keyword pattern matching.

---

## Face Detection and Recognition
### Overview
This project focuses on object detection using the YOLOv7-tiny model. It is capable of detecting and recognizing faces or objects in real-time.

### Key Features
- Real-time video and image processing.
- Object detection using pre-trained YOLOv7-tiny ONNX model.
- Bounding box and confidence score display for detected objects.

### Tools and Libraries
- **Python**
- **OpenCV**: For image and video processing.
- **ONNX Runtime**: For running the YOLOv7-tiny model.

### How It Works
1. Takes input from a video file or webcam.
2. Processes the frames using the YOLOv7-tiny model.
3. Draws bounding boxes around detected objects with class names and confidence scores.

### Files
- `detection.py`: Main script for running the detection pipeline.
- `yolov7-tiny.onnx`: Pre-trained model weights.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/codsoft-projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd codsoft-projects
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the respective project:
   - **Movie Recommendation System:**
     ```bash
     streamlit run setup.py
     ```
   - **Face Detection and Recognition:**
     ```bash
     python detection.py --source your_video.mp4
     ```

---

## Future Improvements
- Enhance the chatbot to include dynamic response generation using machine learning or NLP techniques.
- Integrate collaborative filtering into the recommendation system.
- Optimize the face detection pipeline for faster processing on edge devices.
