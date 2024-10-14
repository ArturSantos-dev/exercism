// Package weather provides tools to forecast the current weather condition in different cities.
package weather

// CurrentCondition holds the current weather condition for the specified city.
var CurrentCondition string

// CurrentLocation holds the name of the city for which the weather condition is being forecasted.
var CurrentLocation string

// Forecast returns the current weather condition for a given city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
