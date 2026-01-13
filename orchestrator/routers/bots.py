from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Bot

router = APIRouter()

@router.post("/register_bot")
def register_bot(bot_name: str, db: Session = Depends(get_db)):
    # Create a new Bot instance — UUID is auto-generated
    new_bot = Bot(name=bot_name)
    
    # Add to session
    db.add(new_bot)
    
    # Commit to save in DB
    db.commit()
    
    # Refresh to get the generated UUID
    db.refresh(new_bot)
    
    # Return response
    return {"bot_id": new_bot.id, "bot_name": new_bot.name}
