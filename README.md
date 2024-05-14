# US Energy Prices Visualization

This Python program provides a visual analysis of US energy prices over time, specifically focusing on Crude Oil Prices (WTI), Average Gasoline Prices in the US, and Henry Hub Natural Gas Spot Prices from the year 2000 onwards.

## Description

The program fetches historical price data using the `pandas_datareader` library from the Federal Reserve Economic Data (FRED) service. It then visualizes these prices on a line graph using `matplotlib`, allowing us to observe trends and fluctuations in energy prices over the past two decades.

## Installation

To run this program, ensure you have Python installed along with the following libraries:
- pandas
- matplotlib
- pandas_datareader

You can install these libraries using pip:
```
pip install pandas matplotlib pandas_datareader
```

## Usage

Simply run the script, and the graph will automatically generate, displaying the trends in energy prices from 2000 to the present.

## Findings from the Graph (2000 - Present)

The graph presents several key observations:

1. **Crude Oil Price (WTI)**: The price of crude oil shows significant volatility. Notable peaks occur around 2008 and 2014, with a dramatic fall in prices seen starting in late 2014 and another sharp decline in 2020. These fluctuations can generally be attributed to global economic conditions, geopolitical tensions, and changes in supply and demand.

2. **Average Gasoline Price (US)**: Gasoline prices closely follow the trends in crude oil prices due to crude oil being a primary input in gasoline production. The peaks and troughs in gasoline prices correlate with those of crude oil, albeit with less amplitude.

3. **Henry Hub Natural Gas Spot Price**: Natural gas prices are generally lower and less volatile than oil prices, but spikes can be observed, which are often a result of temporary regional demand increases, supply disruptions, or severe weather conditions.

## Historical Context and Analysis

- **Early 2000s**: Modest fluctuations reflecting relatively stable market conditions.
- **2008 Financial Crisis**: A sharp peak in oil and gasoline prices just before the crisis, followed by a steep decline as global demand plummeted.
- **2010-2014**: Prices recovered and increased due to stronger economic conditions and Middle Eastern political unrest.
- **2014-2016 Oil Price Crash**: Prices collapsed due to a global oversupply of crude oil exacerbated by U.S. shale oil production and OPEC's strategy to maintain output levels.
- **2020 COVID-19 Pandemic**: Energy prices crashed as demand for oil and gasoline dropped significantly due to worldwide lockdowns and travel restrictions.

Understanding these trends is crucial for stakeholders in energy markets, policy-making, and economic forecasting.

## Conclusion

This visual analysis offers a clear picture of how external events and economic cycles influence energy prices. Stakeholders can use this data to make informed decisions about investments, energy policies, and resource management.