from database import create_engine_and_session
from models import Node, AirQualityData

def insert_node(session, node_name, longitude, latitude):
    new_node = Node(node_name=node_name, longitude=longitude, latitude=latitude)
    session.add(new_node)
    session.commit()

def insert_air_quality_data(session, node_id, timestamp, temperature, humidity, air_quality):
    new_data = AirQualityData(node_id=node_id, timestamp=timestamp, temperature=temperature, humidity=humidity, air_quality=air_quality)
    session.add(new_data)
    session.commit()
