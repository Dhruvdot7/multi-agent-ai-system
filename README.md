# 🚀 Multi-Agent AI System – SpaceX Launch Delay Estimator

This is a simple multi-agent system that:
1. Fetches the next SpaceX launch
2. Retrieves weather at the launch site
3. Analyzes if weather may cause a delay

## 🧠 Agents Overview

| Agent           | Function                                                                 |
|----------------|--------------------------------------------------------------------------|
| `spacex_agent`  | Uses the SpaceX API to fetch upcoming launch details                    |
| `weather_agent` | Uses Open-Meteo API to get forecast for launch time/location            |
| `summary_agent` | Applies rules to predict if the launch may be delayed                   |
| `main.py`       | Orchestrates all agents to form an intelligent multi-step pipeline      |

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run

Run the complete pipeline:
```bash
python main.py
```

## 🌐 APIs Used (All Free)

- SpaceX API – https://api.spacexdata.com
- Open-Meteo API – https://open-meteo.com

No API key needed.

## 📋 Sample Output

📋 Final Status     : Launch likely on time  
  - Weather conditions are within safe limits  
💡 Advice           : No severe weather detected at launch site.

## 📁 Project Structure

```
multi_agent_system/
├── main.py
├── spacex_agent.py
├── weather_agent.py
├── summary_agent.py
├── requirements.txt
└── README.md
```

✅ 100% Working  
✅ No API keys  
✅ Beginner-friendly

#Note on Multi-Agent AI System Execution and Weather Forecast Handling
  The multi-agent AI system for evaluating upcoming SpaceX launches was successfully executed. The agents collaborated effectively to fetch launch data, obtain weather forecasts, analyze launch conditions, and determine the final launch status.

  The weather agent integrated with the Open-Meteo API and correctly matched the launch hour from the API response. However, since the system tested a historical launch (USSF-44 on 2022-11-01), the API returned null values for temperature, precipitation, and wind speed due to unavailable archived hourly data. The code was updated to gracefully handle such cases by applying default values (0.0) to ensure robust and uninterrupted operation.

  The system completed all stages of the pipeline successfully, concluding that the launch is likely on time with no severe weather conditions detected.

I'm always up for suggestions and eagerly looking forward to work with you.

Thanks and Regards,
Dhruv