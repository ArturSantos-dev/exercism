score <- function(x, y) {
    distancia <- sqrt(x^2 + y^2)
    
    if (distancia > 10) {
        return(0)
    } else if (distancia <= 1) {
        return(10)
    } else if (distancia <= 5) {
        return(5)
    } else {
        return(1)
    }
}

