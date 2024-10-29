parse_phone_number <- function(number_string) {
    number_string <- gsub("[^0-9]", "", number_string)
    
    # Verifica se o número tem 10 dígitos e não começa com '0' ou '1'
    if (nchar(number_string) == 10 && !(substr(number_string, 1, 1) %in% c("0", "1"))) {
        return(number_string)
    
    # Verifica se o número tem 11 dígitos, começa com '1', e o segundo dígito não é '0' ou '1'
    } else if (nchar(number_string) == 11 && substr(number_string, 1, 1) == "1" && !(substr(number_string, 2, 2) %in% c("0", "1"))) {
        return(substr(number_string, 2, 11))
    
    # Caso contrário, considera o número inválido
    } else {
        return(NULL)
    }
}




