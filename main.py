import asyncio
import logging

import text_generation
import s3_client as s3
import os
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
    source_key: str
    target_key: str
    user_id: str
    # session_id: str

class Response(BaseModel):
    result: any

# async def connect_db():
#     # Establish a connection to the PostgreSQL database
#     conn = await asyncpg.connect(
#         user=os.environ.get('DATABASE_USER'),
#         password=os.environ.get('DATABASE_PASSWORD'),
#         database=os.environ.get('DATABASE_NAME'),
#         host=os.environ.get('DATABASE_HOST'),
#         port=os.environ.get('DATABASE_PORT')
#     )
#     return conn

async def disconnect_db(conn):
    # Close the connection to the PostgreSQL database
    await conn.close()


    

async def create_session(user_id: str, conn: any):
    # Example query to fetch data from the database
    # Insert a record into the database
    uuid_value = str(uuid.uuid4())
    await conn.execute("INSERT INTO session (id, user_id, status) VALUES ($1, $2, $3)", uuid_value, user_id, 'fail')
    return uuid_value

async def update_session(status: str, session_id: str, conn: any):
    # Example query to fetch data from the database
    # Insert a record into the database
    await conn.execute("UPDATE session set status = $1 where id = $2", status, session_id)



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
    result = text_generation.generate_text(request.prompt)
    print(result)
    return Response(result=result)
