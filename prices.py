import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

codes = ['DCOILWTICO', 'APU000074714', 'DHHNGSP']
start = datetime(2000, 1, 1)
end = datetime.now()

energy_prices = web.DataReader(codes, 'fred', start, end)

energy_prices.rename(columns={
    'DCOILWTICO': 'Crude Oil Price (WTI)',
    'APU000074714': 'Average Gasoline Price (US)',
    'DHHNGSP': 'Henry Hub Natural Gas Spot Price'
}, inplace=True)

plt.figure(figsize=(14, 7))  

# Plot each energy price as a separate line
plt.plot(energy_prices.index, energy_prices['Crude Oil Price (WTI)'], label='Crude Oil Price (WTI)', color='blue')
plt.plot(energy_prices.index, energy_prices['Average Gasoline Price (US)'], label='Average Gasoline Price (US)', color='red')
plt.plot(energy_prices.index, energy_prices['Henry Hub Natural Gas Spot Price'], label='Henry Hub Natural Gas Spot Price', color='green')

# Adding titles and labels
plt.title('US Energy Prices Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()

# Adding grid for better readability of the plot
plt.grid(True)

plt.show()