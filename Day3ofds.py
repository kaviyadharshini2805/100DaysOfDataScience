import numpy as np
import matplotlib.pyplot as plt

temps_15days = np.array([32, 34, 30, 31, 33, 35, 36, 34, 32, 31, 29, 28, 30, 33, 34])

print(f"📌 Average Temperature: {np.mean(temps_15days):.2f}°C")
print(f"❄️ Minimum Temperature: {np.min(temps_15days)}°C")
print(f"🔥 Maximum Temperature: {np.max(temps_15days)}°C")
print(f"📉 Std Deviation: {np.std(temps_15days):.2f}")

temps_week = np.array([32, 34, 30, 29, 35, 36, 33])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.figure(figsize=(8,5))
plt.plot(days, temps_week, 
         marker="o", markersize=8, 
         color="#1f77b4", linewidth=2, linestyle="--", 
         label="Temperature")

plt.title("🌤 Weekly Temperature Trend")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()