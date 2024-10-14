package main

import "strings"

func WelcomeMessage(customer string) string {
	// Converter o nome do cliente para maiúsculas
	upperCustomer := strings.ToUpper(customer)

	// Retornar a mensagem de boas-vindas formatada
	return "Welcome to the Tech Palace, " + upperCustomer + "!"
}

func main() {
	// Adicionar um border à mensagem de boas-vindas
	welcomeMsg := WelcomeMessage("Alice")
	println(welcomeMsg)

}
