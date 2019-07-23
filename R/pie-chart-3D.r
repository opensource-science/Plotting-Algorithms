library(plotrix)
x <- c(1:100)
lab <- c("her ex", "The guy she tells you not to worry about", "you")
pie3D(x, col=rainbow(length(x)), explode=0.1)

pie(x, lab, col=rainbow(length(x)))
