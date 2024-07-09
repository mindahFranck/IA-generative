from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import GenerationResult, SessionLocal, init_db
from datetime import datetime
import random
import string

router = APIRouter()

@router.post("/generate")
async def generate_plate(country: str):
    try:
        # Génération de la plaque (simulée ici, à remplacer par le modèle de génération)
        generated_plate = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

        # Sauvegarde dans la base de données
        db: Session = SessionLocal()
        generation_result = GenerationResult(
            country=country,
            generated_plate=generated_plate,
            timestamp=datetime.utcnow()
        )
        db.add(generation_result)
        db.commit()
        db.refresh(generation_result)

        return {
            "country": country,
            "generated_plate": generated_plate,
            "id": generation_result.id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
