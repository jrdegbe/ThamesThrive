import logging
from typing import Optional

from ThamesThrive.config import ThamesThrive
from ThamesThrive.domain.geo import Geo
from ThamesThrive.exceptions.log_handler import log_handler
from ThamesThrive.process_engine.action.v1.connectors.maxmind.geoip.model.maxmind_geolite2_client \
    import GeoLiteCredentials, MaxMindGeoLite2Client


logger = logging.getLogger(__name__)
logger.setLevel(ThamesThrive.logging_level)
logger.addHandler(log_handler)


async def get_geo_maxmind_location(creds: GeoLiteCredentials, ip: str) -> Optional[Geo]:
    client = MaxMindGeoLite2Client(credentials=creds)
    try:
        _geo = await client.read(ip=ip)
        _geo = Geo(**{
            "city": _geo.city.name,
            "country": {
                "name": _geo.country.name,
                "code": _geo.country.iso_code
            },
            "county": _geo.subdivisions.most_specific.name,
            "postal": _geo.postal.code,
            "latitude": _geo.location.latitude,
            "longitude": _geo.location.longitude,
            "location": (_geo.location.longitude, _geo.location.latitude)
        })

        return _geo
    except Exception as e:
        logger.error(f"Could not fetch GEO location. Error: {str(e)}")
        return None

    finally:
        await client.close()
