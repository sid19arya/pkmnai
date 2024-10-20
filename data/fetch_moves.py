import os
import sys
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm


if __name__ == "__main__":
        
    base_url = "https://pokeapi.co/api/v2/move/"

    # df = pd.DataFrame(columns=["pkdx_id", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "total"])
    df = pd.DataFrame(columns=["name", "power", "accuracy", "pp", "priority","damage_class", "target", "type", "effect"])
    
    for mv_id in tqdm(range(1, 920)):
        response = requests.get(base_url + f"{mv_id}")
        if response.status_code != 200:
            print(f"Error grabbing move: {mv_id}")
            continue
        
        move = response.json()
        try:
            move_df = pd.DataFrame({
                "name": [move["name"]],
                "power": [move["power"]],
                "accuracy": [move["accuracy"]],
                "pp": [move["pp"]],
                "priority": [move["priority"]],
                "damage_class": [move["damage_class"]["name"]],
                "target": [move["target"]["name"]],
                "type": [move["type"]["name"]],
                "effect": [move["effect_entries"][0]["short_effect"] if move["effect_entries"] else ""],              
                })
        except Exception as e:
            print(f"Error : {e}")
            exit(1)
        
        df = pd.concat([df, move_df])

    df.to_csv("move_data.csv")