library(plot3D)

#' 
get_utility <- function(labor, consumption, alpha=1.45) {
  small <- 1
  klabor <- labor / 1000

  (klabor * (consumption / klabor + small)^(1-alpha) - 1) / (1 - alpha)
}

#' Objective:
#' max consumption, min labor
plot_utility <- function(phi=15, theta=50) {
  labor <- seq(0,1000,10)
  consumption <- seq(0,20,0.5)
  #utility <- get_utility(labor, consumption)
  #z <- outer(labor, consumption, get_utility)
  #persp(labor, consumption, z)

  M <- mesh(labor, consumption)
  x <- M$x
  y <- M$y
  z <- get_utility(x,y)
  surf3D(x, y, z, colvar=z, colkey=TRUE, box=TRUE, bty="b", phi=phi, theta=theta)
}
