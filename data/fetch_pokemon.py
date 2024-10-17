import os
import sys
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm


if __name__ == "__main__":
        
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    df = pd.DataFrame(columns=["pkdx_id", "name", "type1", "type2", "hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "total"])

    for pkdx_id in tqdm(range(1, 1011)):
        response = requests.get(base_url + f"{pkdx_id}")
        if response.status_code != 200:
            print(f"Error grabbing pokemon: {pkdx_id}")
            continue
        
        pokemon = response.json()
        
        poke_df = pd.DataFrame({
            "pkdx_id": [pkdx_id],
            "name": [pokemon["name"]],
            "type1": [pokemon["types"][0]["type"]["name"]],
            "type2": [pokemon["types"][1]["type"]["name"] if len(pokemon["types"]) > 1 else None],
            "hp": [pokemon["stats"][0]["base_stat"]],
            "attack": [pokemon["stats"][1]["base_stat"]],
            "defense": [pokemon["stats"][2]["base_stat"]],
            "sp_attack": [pokemon["stats"][3]["base_stat"]],
            "sp_defense": [pokemon["stats"][4]["base_stat"]],
            "speed": [pokemon["stats"][5]["base_stat"]],
            "total": [sum([pokemon["stats"][i]["base_stat"] for i in range(6)])]
        })
        df = pd.concat([df, poke_df])

    df.to_csv("pokemon_data.csv")