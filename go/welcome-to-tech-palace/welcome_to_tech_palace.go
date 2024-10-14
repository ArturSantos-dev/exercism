package techpalace

import "strings"

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	// Converter o nome do cliente para maiúsculas
	upperCustomer := strings.ToUpper(customer)

	// Retornar a mensagem de boas-vindas formatada
	return "Welcome to the Tech Palace, " + upperCustomer
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	//panic("Please implement the AddBorder() function")
	var border string
	for i := 0; i < numStarsPerLine; i++ {
		border += "*"
	}
	return border + "\n" + welcomeMsg + "\n" + border
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	// Remover todos os asteriscos
	cleanedMessage := strings.ReplaceAll(oldMsg, "*", "")

	// Remover espaços em branco do início e do fim
	cleanedMessage = strings.TrimSpace(cleanedMessage)

	// Retornar a mensagem limpa
	return cleanedMessage
}
