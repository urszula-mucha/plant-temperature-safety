from __future__ import annotations

import json
from typing import List, Dict
from pathlib import Path
from models.Plant import Plant


class PlantRepository:
    """
    Repository responsible for loading plant data and owned plant state
    from JSON files.

    It handles data retrieval and mapping.

    It's the librarian of plant data if you will.
    """

    def __init__(self, plant_database_path: Path,
                 owned_plants_path: Path) -> None:
        self.plant_database_path = plant_database_path
        self.owned_plants_path = owned_plants_path

    def load_all_plants(self) -> Dict[str, Plant]:
        """
        Open the general plant database and use the names to create Plant
        objects from the Plant class.
        """

        with self.plant_database_path.open("r", encoding="utf-8") as file:
            raw_data = json.load(file)

        # plants = {}
        #
        # for item in raw_data:
        #     name = item["name"]
        #     min_temp = item["min_temperature"]
        #
        #     plant_object = Plant(name=name, min_temperature=min_temp)
        #
        #     plants[name] = plant_object

        plants = {
            item["name"]: Plant(
                name=item["name"],
                min_temperature=item["min_temperature"],
            )
            for item in raw_data
        }

        return plants

    def load_owned_plants(self) -> List[dict]:
        """
        Loading the owned_plant file.
        Returns raw entries as a dict with name and location
        """

        with self.owned_plants_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_owned_plant_objects(self) -> List[Plant]:
        """
        Return a list of Plant objects which matches the plants owned by the user.
        """

        all_plants = self.load_all_plants()
        owned_entries = self.load_owned_plants()

        owned_plants: List[Plant] = []

        for entry in owned_entries:
            plant_name = entry["name"]

            if plant_name not in all_plants:
                raise ValueError(
                    f"You own a plant which is not in the database! ({plant_name})"
                )

            owned_plants.append(all_plants[plant_name])

        return owned_plants

    def get_outdoor_plants(self) -> List[Plant]:
        """
        Returns a list of plants currently outside - potentially endangered.
        """
        all_plants = self.load_all_plants()
        owned_entries = self.load_owned_plants()

        outdoor_plants: List[Plant] = []

        for entry in owned_entries:
            if entry.get("location") == "outside":
                plant_name = entry["name"]

            if plant_name not in all_plants:
                raise ValueError(
                    f"Owned plant not found in database! ({plant_name})"
                )
            outdoor_plants.append(all_plants[plant_name])
        return outdoor_plants