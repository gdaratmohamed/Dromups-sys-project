from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Configure CORS middleware to allow communication with the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://frontend-service:80"],  # Adjust this to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Commented out as per your request
# from ultralytics import YOLO
# import numpy as np
# import cv2

# Commented out YOLO model loading
# model = YOLO("models/yolov8n.pt")

# Remove duplicate root endpoint and keep only one
@app.get("/")
async def root():
    return {"message": "Backend IA opérationnel"}

@app.websocket("/ws/detections")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Simulate detection data (placeholder for actual YOLO detections)
            # Replace this with real detection logic when integrating YOLO later
            dummy_detections = [
                {
                    "class": "example_object",
                    "confidence": 0.95,
                    "bbox": [100, 100, 200, 200]  # Example bounding box [x_min, y_min, x_max, y_max]
                },
                {
                    "class": "another_object",
                    "confidence": 0.85,
                    "bbox": [300, 300, 400, 400]
                }
            ]

            # Send dummy detections to the frontend
            await websocket.send_json({"detections": dummy_detections})

            # Wait 1 second before sending the next update
            await asyncio.sleep(1)

    except Exception as e:
        # Log the exception for debugging (optional)
        print(f"WebSocket error: {e}")
        await websocket.close()