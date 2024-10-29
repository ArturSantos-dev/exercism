package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	totalBirds := 0
	for _, bird := range birdsPerDay {
		totalBirds += bird
	}
	return totalBirds
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	totalBirds := 0
	for indice, bird := range birdsPerDay {
		if indice <= week*7 && indice >= (week-1)*7 {
			totalBirds += bird
		}
	}
	return totalBirds
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for indice, bird := range birdsPerDay {
		if indice%2 == 0 {
			birdsPerDay[indice] = bird + 1
		}
	}
	return birdsPerDay
}
