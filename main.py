import asyncio
import logging

import text_generation
import os

from torch import Tensor
from dotenv import load_dotenv
import sys
from fastapi import FastAPI
from pydantic import BaseModel
import asyncpg
import uuid
from contextlib import asynccontextmanager

# sys.path.insert(0, '/pb/')
app = FastAPI()
logging.info('new ver')
class Request(BaseModel):
    # source_key: str
    # target_key: str
    # user_id: str
    # session_id: str
    prompt: str

class Response(BaseModel):
    result: list[str]

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/chat/")
async def face_swap(request: Request):
    # conn = await connect_db()

    # session_id = await create_session(request.user_id, conn)
    # result = insight_face.face_swap(request.source_key, request.target_key, request.user_id, session_id)
    # logging.info("result: %s", result)
    # bucket_name = os.environ.get('AWS_S3_BUCKET')
    # logging.info("bucket_name: %s", bucket_name)
    # presigned_url = s3.generate_presigned_url(bucket_name, result)
    # logging.info("presigned_url: %s", presigned_url)
    # await update_session('success', session_id, conn)
    # await disconnect_db(conn)
    print(request.prompt)
    # result = [request.prompt]


    result = text_generation.generate_text(request.prompt)
    print(result)
    return Response(result=result)
