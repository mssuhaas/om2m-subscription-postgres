from sqlalchemy import Column, Integer, String, Float, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'

    node_id = Column(Integer, primary_key=True)
    node_name = Column(String(100), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)

    air_quality_data = relationship("AirQualityData", back_populates="node")

class AirQualityData(Base):
    __tablename__ = 'air_quality_data'

    data_id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey('nodes.node_id'))
    timestamp = Column(BigInteger, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    air_quality = Column(Float, nullable=False)

    node = relationship("Node", back_populates="air_quality_data")
