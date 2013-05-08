grp<-as.data.frame(read.csv("stats.csv",header=T))

plot(grp$prediction_difference,grp$loss_of_coverage,main="Loss of Coverage vs Prediction Difference",xlab="Prediction Difference",ylab="Loss of Coverage",col="blue")

hist(grp$prediction_difference,main="Prediction Difference Histogram",xlab="Prediction Difference",col="red")

hist(grp$loss_of_coverage,main="Loss of Coverage Histogram",xlab="Loss of Coverage",col="green")