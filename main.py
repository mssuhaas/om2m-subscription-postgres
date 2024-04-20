from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from database import create_engine_and_session
from ingest_data import insert_node, insert_air_quality_data

# Define FastAPI app
app = FastAPI()

# Create engine and session
session = create_engine_and_session()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
# API endpoints
@app.post("/nodes/")
def create_node(request: Request):
    node_data = request.body()
    print(f"Received node data: {node_data.decode()}")
    # Process and insert node data
    # insert_node(session, ...)
    return {"message": "Node created successfully"}

@app.post("/air_quality_data/{node_name}")
def create_air_quality_data(node_name: str, request: Request):
    air_quality_data = request.body()
    print(f"Received air quality data for node {node_name}: {air_quality_data.decode()}")
    # Process and insert air quality data
    # insert_air_quality_data(session, ...)
    return {"message": "Air quality data received"}

