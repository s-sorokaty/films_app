from settings import get_settings
import routers as psql_routers

print(get_settings())
print(psql_routers.save_emotion_events())