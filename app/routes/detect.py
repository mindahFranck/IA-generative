from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.models import DetectionResult, SessionLocal, init_db
from datetime import datetime
import os
import shutil
# import cv2
import numpy as np

router = APIRouter()

@router.post("/detect")
async def detect_plate(file: UploadFile = File(...)):
    try:
        temp_file = f"/tmp/{file.filename}"
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # image = cv2.imread(temp_file)
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        detected_plate = "BE-123-ABC"
        country = "Belgium"
        accuracy = 0.95

        db: Session = SessionLocal()
        detection_result = DetectionResult(
            image_url=temp_file,
            country=country,
            accuracy=accuracy,
            timestamp=datetime.utcnow()
        )
        db.add(detection_result)
        db.commit()
        db.refresh(detection_result)

        return {
            "detected_plate": detected_plate,
            "country": country,
            "accuracy": accuracy,
            "id": detection_result.id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(temp_file)
