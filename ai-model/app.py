from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import numpy as np
import cv2
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charge le modèle YOLO 
model = YOLO("models/yolov8n.pt")

@app.get("/")
async def root():
    return {"message": "Backend IA opérationnel avec YOLO"}

# Route GET simple pour tester la connexion
@app.get("/")
async def root():
    return {"message": "Connexion au backend réussie !"}

@app.websocket("/ws/detections")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # Pour cet exemple, on simule la détection sur une image fixe ou flux réel plus tard
    # Ici, on renvoie des résultats factices toutes les secondes
    try:
        while True:
            # Exemple : lecture d'une image test (ou flux à intégrer)
            # img = cv2.imread("test.jpg")  # tu remplaceras par ton flux drone

            # Pour cet exemple, on crée une image noire (vide)
            img = np.zeros((640, 480, 3), dtype=np.uint8)

            # Prédiction YOLO
            results = model(img)

            # Extraction des détections
            detections = []
            for r in results:
                for box in r.boxes:
                    detections.append({
                        "class": r.names[int(box.cls)],
                        "confidence": float(box.conf),
                        "bbox": box.xyxy[0].tolist()
                    })

            # Envoi au frontend
            await websocket.send_json({"detections": detections})

            await asyncio.sleep(1)  # envoyer toutes les secondes

    except Exception:
        await websocket.close()
