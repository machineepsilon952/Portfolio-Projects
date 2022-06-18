library(forecast)
df = read.csv(file = 'POP.csv')

pop = ts(df["value"], start = 1, frequency = 1)
pop_train = pop[1:600]
plot.ts(pop)
# population growth looks roughly linear
acf(pop)
pacf(pop)
#the acf of the population data tails off really slowly since the 
#data is not stationary
#if we apply differencing with a lag of 1 we end up with the following acf and pacf
plot(diff(pop))
acf(diff(pop))
pacf(diff(pop))
#it appears there is a seasonal component to this data with a season length of 12
# if we use differencing again with lag 12 we end up with the following acf and pacf plots
plot(diff(diff(pop,12)))
acf(diff(diff(pop),  12))
pacf(diff(diff(pop), 12))
# the acf and pacf indicate that this time series can be modeled using p = 1,q=1, d=1 or 2 with a seasonal component with lag 12.

# the final model was chosen based on performance compared to several other canadate models. 
model <- Arima(pop_train, order = c(1,1,2), seasonal = list(order = c(1,1,0), period = 12))
autoplot(model)
checkresiduals(model) # not normally distributed indicating the confidence intervals in the next plot are not meaningful
# the residuals do not look normally distrubuted so the confidence intervals in the following plot are not meaningful.
autoplot(forecast(model,h=200))+autolayer(pop)
