import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("fan_test_summary.csv")
labels = ["Off", "Speed 1", "Speed 2", "Speed 3"]

fig, axes = plt.subplots(2, 1, figsize=(9, 8))

axes[0].plot(labels, data["real_power_W"], marker="o", label="Real Power (W)")
axes[0].plot(labels, data["apparent_power_VA"], marker="s", label="Apparent Power (VA)")
axes[0].plot(labels, data["reactive_power_VAR"], marker="^", label="Reactive Power (VAR)")
axes[0].axhline(0, color="black", linewidth=0.8)
axes[0].set_title("Tower Fan Power by Speed")
axes[0].set_ylabel("Power")
axes[0].grid(True, alpha=0.3)
axes[0].legend()

axes[1].plot(
    labels[1:],
    data["power_factor"][1:],
    marker="o",
    color="purple"
)
axes[1].set_title("Tower Fan Power Factor by Speed")
axes[1].set_ylabel("Power Factor")
axes[1].set_ylim(0.90, 1.02)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("fan_test_results.png", dpi=300)
plt.show()