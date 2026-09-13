# SunTrack ☀️

## Solar Panel Angle & Efficiency Calculator

SunTrack is a beginner-friendly Python project that simulates how changing the tilt of a solar panel affects its alignment with sunlight.

### Features

- Enter the sun elevation angle.
- Enter the solar panel tilt angle.
- Calculate a simple sunlight-alignment percentage.
- Search for the best panel tilt for the selected sun elevation.
- View a simple visual simulation of the sun and panel.
- Reset the simulation to default values.

### Built with

- Python
- Tkinter
- Basic mathematics and trigonometry
- Tkinter Canvas for visualization

### Run the project

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows:

```powershell
py main.py
```

### How it works

The program uses a simplified 2D geometric model. It compares the panel tilt with the direction needed for better alignment with the incoming sunlight.

The percentage shown is an **alignment estimate**, not a real measurement of electrical power.

Real solar production depends on many other factors, including weather, shading, temperature, panel characteristics, location and time.

### Future ideas

- Add a graph of efficiency versus panel angle.
- Simulate the sun moving during the day.
- Add simulated light-sensor input.
- Connect the model to an Arduino and servo motor.
