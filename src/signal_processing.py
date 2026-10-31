import numpy as np
import matplotlib.pyplot as plt

# Simulated signal: a repeating wave with a little noise
time = np.linspace(0, 5, 500)
signal = np.sin(2 * np.pi * 1.5 * time)
noise = np.random.normal(0, 0.15, size=time.shape)
noisy_signal = signal + noise

plt.plot(time, noisy_signal, label="Simulated signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Signal strength")
plt.title("WiSense AI — Signal Demo")
plt.legend()
plt.tight_layout()
plt.show()
