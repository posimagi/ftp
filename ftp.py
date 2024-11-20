#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def f(tp, ws):
    if 1000 <= tp < 2000:
        return ws.ftp1000 + ((ws.ftp2000 - ws.ftp1000) / 1000 * (tp - 1000))
    elif 2000 <= tp <= 3000:
        return ws.ftp2000 + ((ws.ftp3000 - ws.ftp2000) / 1000 * (tp - 2000))
    else:
        return 0

class Weaponskill:
    def __init__(self, *args):
        self.name, self.ftp1000, self.ftp2000, self.ftp3000 = args

ws_list = {
    Weaponskill("Savage Blade", 4.0, 10.25, 13.75),
    Weaponskill("Rudra's Storm", 5.0, 10.19, 13),
}

x_values = np.linspace(1000, 3000, 9)
for ws in ws_list:
    y_values = np.array([f(x, ws) for x in x_values])
    plt.plot(x_values, y_values, label=ws.name)
plt.xlabel('TP')
plt.ylabel('fTP')
plt.xlim(1000, 3000)
plt.ylim(bottom=0)
plt.title('Damage Varies with TP')
plt.grid(True)
plt.legend()
plt.show()

