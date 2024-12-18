package speed

// TODO: define the 'Car' type struct
type Car struct {
	battery      int
	batteryDrain int
	speed        int
	distance     int
}

// NewCar creates a new remote controlled car with full battery and given specifications.
func NewCar(speed, batteryDrain int) Car {
	newCar := Car{speed: speed, batteryDrain: batteryDrain, battery: 100}
	return newCar
}

// TODO: define the 'Track' type struct

type Track struct {
	distance int
}

// NewTrack creates a new track
func NewTrack(distance int) Track {
	distanceTrack := Track{distance: distance}
	return distanceTrack
}

// Drive drives the car one time. If there is not enough battery to drive one more time,
// the car will not move.
func Drive(car Car) Car {
	if car.battery < car.batteryDrain {
		return car // Retorna o carro sem movimento caso não tenha bateria suficiente para drenar.
	}

	// Atualiza a distância e reduz a bateria.
	car.distance += car.speed
	car.battery -= car.batteryDrain
	return car
}

// CanFinish checks if a car is able to finish a certain track.
func CanFinish(car Car, track Track) bool {
	if (car.battery/car.batteryDrain)*car.speed >= track.distance {
		return true
	} else {
		return false
	}
}
