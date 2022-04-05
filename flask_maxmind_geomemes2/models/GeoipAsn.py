from sqlalchemy import Column, String, Integer, Numeric
from flask_maxmind_geomemes2 import Base

class GeoipAsn(Base):
    __tablename__ = 'geoip_asns'

    address = Column(String, primary_key=True)
    autonomous_system_number = Column(String, nullable=False)
    ip_start_range = Column(Numeric, precision=40, scale=0)
    ip_end_range = Column(Numeric, precision=40, scale=0)

