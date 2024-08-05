import io
import os
import shutil
from typing import Optional

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from .audio2text import Audio2TextTool

router = APIRouter()

whisper_api = Audio2TextTool()


class AudioTextQueryItem(BaseModel):
    file: UploadFile = File(...)


@router.post(
    "/tools/audio2text", summary="A tool that converts audio to natural language text."
)
async def audio2text(item: AudioTextQueryItem = Depends()):
    try:
        # Create a temporary file to save the uploaded audio.
        with open(item.file.filename, "wb") as buffer:
            shutil.copyfileobj(item.file.file, buffer)
        with open(item.file.filename, "rb") as audio:
            caption = whisper_api.caption(audio_file=audio)
        # Clean up temporary files.
        os.remove(item.file.filename)
        return {"text": caption}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
