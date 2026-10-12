City Sensor Data Stream & Real-Time Monitoring Dashboard
A real-time simulation and monitoring dashboard that streams, processes, and visualizes urban sensor data from various locations across the city. Built with Python, Streamlit, and SQLite, this application provides an elegant user interface with live data streams, interactive line graphs, and automated filtering for critical alerts.

🚀 Key Features
Live Data Simulation: Simulates continuous real-time data streams from multiple urban sensors.

Interactive UI: Built with Streamlit for a clean, modern, and responsive user experience.

Real-Time Visualization: Dynamic line graphs and metrics reflecting live changes in the data stream.

Critical Value Filtering: Automatically isolates and displays critical or threshold-breaching sensor readings in a dedicated alert table.

Data Persistence: Uses SQLite3 for lightweight and reliable data storage.

Efficient Data Retrieval: Leverages Pandas for high-performance querying and data manipulation from the database.

🏙️ Monitored Urban Sensors
The system tracks and analyzes metrics across four key municipal domains:

Air Quality (Park): Environmental monitoring metrics.

Main Water Line: Flow rates and pressure stability.

Smart Light Power Consumption: Energy usage tracking for intelligent city lighting.

Street 1 Power Consumption: Sector-specific electrical load monitoring.

🧰 Tech Stack
Language: Python

Frontend & Dashboard: Streamlit

Data Processing & Analysis: Pandas

Database: SQLite3

⚙️ Getting Started
Prerequisites
Make sure you have Python installed along with the required libraries:
```bash
pip install streamlit pandas
```
Running the Application
Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
and then activate and run program with the following commands
```bash
uv run telemetry_sim.py
```
and in the separate bash
```bash
uv run streamlit run dashboard.py
```

