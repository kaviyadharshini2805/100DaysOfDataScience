import matplotlib.pyplot as plt
import pandas as pd

# Load and Inspect
df = pd.read_csv("C:\\Users\\kaviyadividh\\Downloads\\screen_time.csv")
print(df.head())
print(df.info())

# Cleaning
# Converting numeric columns safely
for col in ["Instagram", "YouTube", "WhatsApp", "Chrome", "Others"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.fillna(0)

order = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df["Day"] = pd.Categorical(df["Day"], categories=order, ordered=True)
df = df.sort_values("Day")

# Clip values to a realistic range (0 to 1440 minutes per day)
for col in ["Instagram", "YouTube", "WhatsApp", "Chrome", "Others"]:
    df[col] = df[col].clip(lower=0, upper=1440)

# Feature Engineering
df["Total"] = df[["Instagram", "YouTube", "WhatsApp", "Chrome", "Others"]].sum(axis=1)
weekly_avg = df[["Instagram", "YouTube", "WhatsApp", "Chrome", "Others"]].mean().sort_values(ascending=False)
total = df["Total"].sum()
share = (weekly_avg / weekly_avg.sum()) * 100

# Visualization

# Line Chart - Daily total screen time
plt.plot(df["Day"], df["Total"], marker="o")
plt.title("Total Screen Time per Day")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.grid(True)
plt.tight_layout()
plt.savefig("total_screen_time.png", dpi=150)
plt.show()

# Bar Chart - Weekly average per app
weekly_avg.plot(kind="bar")
plt.title("Weekly Average Screen Time per App")
plt.ylabel("Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weekly_avg.png", dpi=150)
plt.show()

# Pie Chart - Share of apps
share.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Screen Time Distribution by App (Weekly)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie.png", dpi=150)
plt.show()

# Print insights for LinkedIn post
print("\n📊 Insights:")
print(f"Total screen time in the week: {total:.0f} minutes (~{total/60:.1f} hours)")
print(f"Day with highest usage: {df.loc[df['Total'].idxmax(), 'Day']} ({df['Total'].max()} minutes)")
print(f"Most used app: {weekly_avg.idxmax()} ({weekly_avg.max():.1f} minutes per day on average)")
