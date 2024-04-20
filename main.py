# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
from database import create_engine_and_session
from ingest_data import insert_node, insert_air_quality_data

# Define FastAPI app
# app = FastAPI()

# Pydantic models for request bodies
# class NodeCreate(BaseModel):
#     node_name: str
#     longitude: float
#     latitude: float

# class AirQualityDataCreate(BaseModel):
#     node_id: int
#     timestamp: int
#     temperature: float
#     humidity: float
#     air_quality: float

# Create engine and session
session = create_engine_and_session()

# API endpoints
# @app.post("/nodes/")
# def create_node(node_data: NodeCreate):
#     insert_node(session, node_data.node_name, node_data.longitude, node_data.latitude)
#     return {"message": "Node created successfully"}

# @app.post("/air_quality_data/")
# def create_air_quality_data(data: AirQualityDataCreate):
#     insert_air_quality_data(session, data.node_id, data.timestamp, data.temperature, data.humidity, data.air_quality)
#     return {"message": "Air quality data inserted successfully"}