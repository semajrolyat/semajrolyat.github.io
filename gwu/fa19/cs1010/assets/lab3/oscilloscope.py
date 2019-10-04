"""


********************************************************************
The basis of this code is derived from:

Display analog data from Arduino using Python (matplotlib)
Author: Mahesh Venkitachalam
Website: electronut.in
"""

import serial
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, plot, ser, buffer, maxLen):
  try:
    line = ser.readline().decode('UTF-8')
    data = [int(val) for val in line.split()]
    if len(buffer) < maxLen:
      buffer.append(data[0])
    else:
      buffer.pop()
      buffer.appendleft(data[0])
    plot.set_data(range(maxLen), buffer)
    print(data[0])
  except KeyboardInterrupt:
    print('Exiting')
  except serial.SerialException:
    print("Error reading from serial port")
    ser.flush()
    ser.close()    
  except ValueError:
    print("Value error, dropping packet.")
  return plot,

strPort = '/dev/ttyACM1'  # The serial port to listen for data on
extens=((0,100),(0,200))  # (x_lo, x_hi),(y_lo, y_hi)

ser = serial.Serial(strPort, 9600)
buf = deque([0.0]*extens[0][1])

fig = plt.figure()
ax = plt.axes(xlim=extens[0], ylim=extens[1])
ax.set_title("Measured Distance")
ax.set_xlabel("Buffered Sample")
ax.set_ylabel("Distance (cm)")
a0, = ax.plot([], [])
anim = animation.FuncAnimation(fig,
                               update,
                               fargs=(a0, ser, buf, extens[0][1]),
                               interval=50)

plt.show()

ser.flush()
ser.close()    

print('Exiting')
