import tkinter as tk
from tkinter import ttk, messagebox
import math

def alignment(panel_tilt, sun_elevation):
    # Simple 2D model: best alignment is when panel tilt is
    # approximately 90 degrees minus the sun elevation.
    target = 90 - sun_elevation
    error = abs(panel_tilt - target)
    return max(0.0, math.cos(math.radians(error))) * 100

def calculate():
    try:
        sun = float(sun_var.get())
        panel = float(panel_var.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    if not -90 <= sun <= 90:
        messagebox.showerror("Invalid sun angle", "Use a value from -90° to 90°.")
        return
    if not 0 <= panel <= 90:
        messagebox.showerror("Invalid panel angle", "Use a value from 0° to 90°.")
        return

    value = alignment(panel, sun)
    result_var.set(f"{value:.1f}%")
    detail_var.set(f"Sun elevation: {sun:.1f}°   |   Panel tilt: {panel:.1f}°")
    draw_scene(sun, panel)

def best_angle():
    try:
        sun = float(sun_var.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid sun elevation.")
        return
    if not -90 <= sun <= 90:
        messagebox.showerror("Invalid sun angle", "Use a value from -90° to 90°.")
        return

    # Search possible panel angles rather than assuming the answer.
    values = [(alignment(a, sun), a) for a in range(91)]
    value, angle = max(values)
    panel_var.set(str(angle))
    recommendation_var.set(
        f"Best simulated panel tilt: {angle}° ({value:.1f}% alignment)"
    )
    calculate()

def reset():
    sun_var.set("45")
    panel_var.set("45")
    result_var.set("—")
    detail_var.set("Enter values and click Calculate.")
    recommendation_var.set("Click 'Find best angle' to get a recommendation.")
    draw_scene(45, 45)

def draw_scene(sun, panel):
    canvas.delete("all")
    w = max(canvas.winfo_width(), 500)
    h = max(canvas.winfo_height(), 350)
    ground = h - 55

    canvas.create_line(35, ground, w - 35, ground, fill="#b8c0c8", width=3)

    # Sun
    sx, sy = w - 100, 75
    canvas.create_oval(sx-28, sy-28, sx+28, sy+28,
                       fill="#f2b705", outline="")
    canvas.create_text(sx, sy+48, text="Sun", font=("Segoe UI", 11, "bold"))

    # Rays
    for dy in (-35, -15, 5, 25, 45):
        canvas.create_line(sx-22, sy+dy, w-190, ground-130+dy,
                           fill="#d9a400", width=2)

    # Panel
    px, py = w * .45, ground - 25
    length = 190
    a = math.radians(panel)
    dx = math.cos(a) * length / 2
    dy = math.sin(a) * length / 2
    x1, y1 = px-dx, py+dy
    x2, y2 = px+dx, py-dy

    canvas.create_line(x1, y1, x2, y2, fill="#263238", width=30)
    canvas.create_line(x1, y1, x2, y2, fill="#3f73d9", width=22)

    canvas.create_line(px, py, px, ground, fill="#555", width=4)
    canvas.create_oval(px-6, py-6, px+6, py+6, fill="#202124", outline="")

    canvas.create_text(45, ground+25, anchor="w",
                       text=f"Panel tilt = {panel:.1f}°",
                       font=("Segoe UI", 11, "bold"))
    canvas.create_text(45, ground+45, anchor="w",
                       text=f"Sun elevation = {sun:.1f}°",
                       font=("Segoe UI", 10))

root = tk.Tk()
root.title("SunTrack - Solar Panel Angle & Efficiency Calculator")
root.geometry("1000x680")
root.minsize(800, 560)
root.configure(bg="#f4f6f8")

style = ttk.Style()
try:
    style.theme_use("vista")
except tk.TclError:
    pass

sun_var = tk.StringVar(value="45")
panel_var = tk.StringVar(value="45")
result_var = tk.StringVar(value="—")
detail_var = tk.StringVar(value="Enter values and click Calculate.")
recommendation_var = tk.StringVar(
    value="Click 'Find best angle' to get a recommendation."
)

header = ttk.Frame(root, padding=(25, 20, 25, 10))
header.pack(fill="x")
ttk.Label(header, text="SunTrack",
          font=("Segoe UI", 23, "bold")).pack(anchor="w")
ttk.Label(header, text="Solar Panel Angle & Efficiency Calculator",
          font=("Segoe UI", 10)).pack(anchor="w")

main = tk.Frame(root, bg="#f4f6f8")
main.pack(fill="both", expand=True, padx=25, pady=15)

controls = tk.Frame(main, bg="white", highlightbackground="#d0d7de",
                    highlightthickness=1, width=310)
controls.pack(side="left", fill="y", padx=(0, 15))
controls.pack_propagate(False)

tk.Label(controls, text="Inputs", bg="white", fg="#202124",
         font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=20, pady=(20,15))

tk.Label(controls, text="Sun elevation (°)", bg="white").pack(
    anchor="w", padx=20)
ttk.Entry(controls, textvariable=sun_var, width=24).pack(
    anchor="w", padx=20, pady=(5,15))

tk.Label(controls, text="Panel tilt (°)", bg="white").pack(
    anchor="w", padx=20)
ttk.Entry(controls, textvariable=panel_var, width=24).pack(
    anchor="w", padx=20, pady=(5,20))

ttk.Button(controls, text="Calculate", command=calculate).pack(
    fill="x", padx=20, pady=4)
ttk.Button(controls, text="Find best angle", command=best_angle).pack(
    fill="x", padx=20, pady=4)
ttk.Button(controls, text="Reset", command=reset).pack(
    fill="x", padx=20, pady=4)

tk.Label(controls, textvariable=recommendation_var, bg="white",
         fg="#238636", wraplength=260, justify="left",
         font=("Segoe UI", 10, "bold")).pack(
             anchor="w", padx=20, pady=(25,10))

tk.Label(controls, text=(
    "This is a simplified educational model. "
    "Real solar output also depends on weather, shading, "
    "temperature, panel characteristics and location."
), bg="white", fg="#5f6368", wraplength=260, justify="left",
font=("Segoe UI", 9)).pack(anchor="w", padx=20, pady=10)

right = tk.Frame(main, bg="white", highlightbackground="#d0d7de",
                 highlightthickness=1)
right.pack(side="left", fill="both", expand=True)

tk.Label(right, text="Estimated sunlight alignment", bg="white",
         fg="#5f6368", font=("Segoe UI", 10)).pack(anchor="w", padx=20, pady=(20,0))
tk.Label(right, textvariable=result_var, bg="white", fg="#202124",
         font=("Segoe UI", 28, "bold")).pack(anchor="w", padx=20)
tk.Label(right, textvariable=detail_var, bg="white", fg="#5f6368",
         font=("Segoe UI", 9)).pack(anchor="w", padx=20)

canvas = tk.Canvas(right, bg="#fbfcfe", highlightthickness=0)
canvas.pack(fill="both", expand=True, padx=20, pady=20)

root.bind("<Return>", lambda e: calculate())
draw_scene(45, 45)
root.mainloop()
