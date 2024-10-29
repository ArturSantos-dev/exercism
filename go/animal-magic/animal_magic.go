package chance

import (
	"math/rand"
)

// RollADie returns a random int d with 1 <= d <= 20.
func RollADie() int {
	dice := rand.Intn(20) + 1
	return dice
}

// GenerateWandEnergy returns a random float64 f with 0.0 <= f < 12.0.
func GenerateWandEnergy() float64 {
	flutuante := rand.Float64() * 12
	return flutuante
}

// ShuffleAnimals returns a slice with all eight animal strings in random order.
func ShuffleAnimals() []string {
	animals := []string{"ant", "beaver", "cat", "dog", "elephant", "fox", "giraffe", "hedgehog"}

	// Fisher-Yates shuffle algorithm
	for i := len(animals) - 1; i > 0; i-- {
		j := rand.Intn(i + 1)                           // Seleciona um índice aleatório
		animals[i], animals[j] = animals[j], animals[i] // Troca os elementos
	}

	return animals
}
