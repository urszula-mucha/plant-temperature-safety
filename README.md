# Plant Weather Safety App — Phase 1 MVP
[1. Overview](#overview) <br>
[2. Origin of the project](#origin-of-the-project) <br>
[3. Problem statement](#problem-statement) <br>
[4. Phase 1 MVP features](#phase-1-mvp-features) <br>
[5. Architecture](#architecture) <br>
[6. Module responsibilities](#module-responsibilities) <br>
[7. How it works](#how-it-works) <br>
[8. Example output](#example-output) <br>
[9. Planned Improvements](#planned-improvements) <br>
[10. Technical stack](#technical-stack) <br>
[11. Current status](#current-status) <br>

## Overview
The Plant Weather Safety App is a Python application that evaluates whether outdoor plants are at risk based on the current temperature.

This project focuses on clean architecture, modular design, and clear separation of responsibilities. Phase 1 delivers a small but fully working system that can be extended in later iterations.

## Origin of the project
This application was inspired by a personal mistake.

I had an avocado tree that I grew for three years. This autumn, I forgot to bring it inside before temperatures dropped. It did not survive the cold.

_RIP Avocado Tree (2022–2025)._

I decided to build something that would prevent that from happening again. This project is a practical solution and an exercise in clean system design with structured Python development.

## Problem statement
Outdoor plants can be damaged when temperatures drop below their tolerance threshold.

**This application answers a simple question:**
Are my outdoor plants currently at risk based on today’s temperature?

## Phase 1 MVP features
- Predefined plant database stored in a local JSON file
- Separate configuration for owned plants
- Indoor and outdoor plant distinction
- Mock WeatherService that simulates current temperature
- Logic that evaluates temperature risk
- Command-line interface output
- Layered project structure

## Architecture

The project follows a layered structure:

plant_weather_app/ <br> 
│<br> 
├── models/<br> 
│   └── plant.py <br> 
│<br> 
├── repositories/<br> 
│   └── plant_repository.py<br> 
│<br> 
├── services/<br> 
│   ├── weather_service.py<br> 
│   └── safety_evaluator.py<br> 
│<br> 
├── data/<br> 
│   ├── plant_database.json<br> 
│   └── owned_plants.json<br> 
│<br> 
├── main.py<br> 
└── README.md 

## Module Responsibilities

### models/
Contains domain objects such as Plant.

### repositories/
Handles loading and mapping data from JSON files into domain objects.

### services/
Includes:
- WeatherService, which provides temperature data
- SafetyEvaluator, which contains the temperature evaluation logic

### main.py
Coordinates the application flow.

## How It Works
1. The application loads the plant database.
2. It loads the list of owned plants.
3. It filters plants that are currently located outdoors.
4. It retrieves the current temperature.
5. It evaluates whether any outdoor plant is at risk.
6. It prints the result to the console.

## Example output
--- Plant Weather Safety Report --- <br> 
Current temperature: 6.0°C

WARNING: Temperature risk detected! <br> 
Most fragile plant: Monstera deliciosa <br> 
Minimum safe temperature: 14°C <br> 
Current temperature: 6.0°C <br> 
Risk of plant damage!

----------------------------------

## Planned Improvements
Future versions may include:
- Integration with a real weather API
- Multi-day forecast evaluation
- Additional plant attributes
- A graphical user interface
- A scraping module to enrich plant data

## Technical Stack
- Python 3.x
- JSON for local persistence
- Layered project structure
- Command-line interface

## Current status
Phase 1 MVP is complete. The application is fully functional and structured to support additional features without major refactoring.