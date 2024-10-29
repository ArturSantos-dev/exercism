two_fer <- function(input = "") {
    if (input == "") {
        return("One for you, one for me.")
    } else {
        return(paste0("One for ", input, ", one for me."))
    }
}
