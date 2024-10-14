package partyrobot

import (
	"fmt"
)

// Welcome greets a person by name.
func Welcome(name string) string {
	//panic("Please implement the Welcome function")
	return "Welcome to my party, " + name + "!"
}

// HappyBirthday wishes happy birthday to the birthday person and exclaims their age.
func HappyBirthday(name string, age int) string {
	// Usa fmt.Sprintf para converter o inteiro para string corretamente
	return fmt.Sprintf("Happy birthday %s! You are now %d years old!", name, age)
}

// AssignTable assigns a table to each guest.
func AssignTable(name string, table int, neighbor, direction string, distance float64) string {
	//panic("Please implement the AssignTable function")
	tableStr := fmt.Sprintf("%03d", table)
	return "Welcome to my party, " + name + "!" + "\nYou have been assigned to table " + tableStr + ". Your table is " + direction + ", " + "exactly " + fmt.Sprintf("%.1f", distance) + " meters from here." + "\nYou will be sitting next to " + neighbor + "."
}
