from __future__ import annotations

from pathlib import Path

from repositories.plant_repository import PlantRepository
from services.safety_evaluator import SafetyEvaluator
from services.weather_service import WeatherService


def main() -> None:
    #Resolve data paths
    base_dir =Path(__file__).resolve().parent

    plant_db_path = base_dir / "data" / "plant_database.json"
    owned_plants_path = base_dir / "data" / "owned_plants.json"

    #Initialize core components
    repository = PlantRepository(
        plant_database_path=plant_db_path,
        owned_plants_path=owned_plants_path,
    )

    weather_service = WeatherService()
    safety_evaluator = SafetyEvaluator()

    #Load outdoor plants
    outdoor_plants = repository.get_outdoor_plants()

    #Get current temperature
    current_temperature = weather_service.get_current_temperature()

    #Evaluate safety
    result_message = safety_evaluator.evaluate(
        outdoor_plants=outdoor_plants,
        current_temperature=current_temperature,
    )

    #Output result
    print("\n--- Plant weather safety report ---")
    print(f"Current temperature: {current_temperature}°C\n")
    print(result_message)
    print("\n------------------------------------\n")

if __name__ == "__main__":
    main()