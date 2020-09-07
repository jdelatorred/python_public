import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

data = pd.read_excel("C:/Data/TeslaSales.xls")

data = data.loc[data['Model'] == 'Model S']

cols = ['Model', 'Country', 'Purchase type', 'Version', 'Gross Profit']

data.drop(cols, axis=1, inplace=True)

data['Period'] = data['Period'].astype(str).str[0:4] + "-" + data['Period'].astype(str).str[4:6]

data = data.groupby('Period', as_index=False)['Price'].sum()

data['Period'] = pd.DatetimeIndex(data['Period'])

data = data.rename(columns={'Period': 'ds','Price': 'y'})

ax = data.set_index('ds').plot(figsize=(12, 8))

ax.set_ylabel('Monthly Tesla Sales')

ax.set_xlabel('Date')

plt.show()

my_model = Prophet(interval_width=0.95)

my_model.fit(data)

future_dates = my_model.make_future_dataframe(periods=36, freq='MS')

future_dates.tail()

forecast = my_model.predict(future_dates)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

my_model.plot(forecast, uncertainty=True)

my_model.plot_components(forecast)