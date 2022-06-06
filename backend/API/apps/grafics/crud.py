from sqlalchemy.orm import Session
from apps.place_routers.models import place_info 
from apps.hall_routers.models import hall_info
import matplotlib.pyplot as plt
import pandas as pd

def get(db):
    place_data = db.query(place_info).all()
    hall_data = db.query(hall_info).all()
    place_df = pd.DataFrame([o.__dict__ for o in place_data])
    hall_df = pd.DataFrame([o.__dict__ for o in hall_data])
    place_df.loc[(place_df['placeType'] == 'базовое'), 'placeType'] = 0
    place_df.loc[(place_df['placeType'] == 'премиум'), 'placeType'] = 1
    fig, ax = plt.subplots()
    ax.set_title('Расределение мест по залам') 
    ax.set_xlabel('ID зала')
    ax.set_ylabel('Тип места зала (Больше - лучше)')
    ax.scatter(x = place_df['idHall'], y = place_df['placeType'])
    ax.legend()
    fig.savefig('graphics/hall_info')
    return 'OK'