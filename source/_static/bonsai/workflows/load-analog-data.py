import numpy as np
import matplotlib.pyplot as plt

# Load data from AnalogIO workflow
suffix = '2024-04-11T12_24_25'; # Change to match file names' suffix

analog_time = np.fromfile('analog-clock_' + suffix + '.raw', dtype=np.uint64) / 250e6
analog_data = np.fromfile('analog-data_' + suffix + '.raw', dtype=np.float32)
analog_data = np.reshape(analog_data, (-1, 12))


# plot the first 100k samples on each channel (1 second of data)
plt.close('all')
plt.plot(analog_time[0:100000], analog_data[0:100000, :])
