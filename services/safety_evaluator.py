from __future__ import annotations

from typing import List, Optional
from models.Plant import Plant


class SafetyEvaluator:
    """
    Checking if the plants are safe.
    """

    def evaluate(self,
                 outdoor_plants: List[Plant],
                 current_temperature: float,
                 ) -> str:
        """
        Args:
            outdoor_plants: List of Plant objects currently outside
            current_temperature: Current temperature in Celsius
        Returns:
            Message about plant safety
        """

        if not outdoor_plants:
            return "No outdoor plants to evaluate. All plants are safe inside."

        most_fragile_plant = self._get_most_fragile_plant(outdoor_plants)

        if most_fragile_plant is None:
            return "No valid plants to evaluate."

        if current_temperature < most_fragile_plant.min_temperature:
            return (
                f"WARNING: Temperature risk!\n"
                f"Most fragile plant: {most_fragile_plant.name}\n"
                f"Minimal safe temperature: {most_fragile_plant.min_temperature}°C\n"
                f"Current temperature: {current_temperature}°C\n"
                f"Hide this plant now!"
            )

        return (
            f"All outdoor plants are safe.\n"
            f"Lowest tolerance plant: {most_fragile_plant.name}\n"
            f"Minimal safe temperature: {most_fragile_plant.min_temperature}°C\n"
            f"Current temperature: {current_temperature}°C\n"
        )

    def _get_most_fragile_plant(self, plants: List[Plant]) -> Optional[Plant]:
        """
        Determine the plant with the highest minimum temperature requirement.
        """
        if not plants:
            return None

        return max(plants, key=lambda plant: plant.min_temperature)