package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	//panic("Please implement the ParseCard function")
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten":
		return 10
	case "jack":
		return 10
	case "queen":
		return 10
	case "king":
		return 10
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.

// FirstTurn returns the decision for the first turn, given two cards of the player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	soma := ParseCard(card1) + ParseCard(card2)

	// Caso especial para par de ases
	if card1 == "ace" && card2 == "ace" {
		return "P"
	}

	// Se o jogador tem 21 (blackjack)
	if soma == 21 {
		// Se o dealer tiver uma carta de valor 10 (ou figuras) ou um ace, retornar "S"
		if dealerCard == "ace" || dealerCard == "king" || dealerCard == "queen" || dealerCard == "jack" || ParseCard(dealerCard) == 10 {
			return "S"
		}
		// Se o dealer tem uma carta menor, retornar "W" para vitória (Win)
		return "W"
	}

	if soma >= 17 && soma <= 20 {
		return "S"
	} else if soma >= 12 && soma <= 16 {
		if ParseCard(dealerCard) >= 7 {
			return "H"
		} else {
			return "S"
		}
	} else {
		return "H"
	}
}
