library(data.table)
setwd('/home/chik/Downloads/images')

#load data
data <- fread('sample_labels.csv')

#
dim(data)
head(data)

# Rearrange
problem.data <- data[!data$`Finding Labels`=='No Finding',]
problem.data$`Finding Labels` <- 'Anamoly'
head(problem.data)

no.data <- data[data$`Finding Labels`=='No Finding',]

new.data<- rbind(no.data,problem.data)
new.data$`Patient ID` <- NULL
head(new.data)

library('dplyr')

names(new.data)[1:6] <- c("Image_Index", "Finding_Labels", "Follow_up","Patient_Age", "Patient_gender", "View_Position") 
new.data$Patient_Age <- as.numeric(substr(new.data$Patient_Age,1,3))
new.data$Patient_gender <- as.factor(new.data$Patient_gender)
new.data$View_Position <- as.factor(new.data$View_Position)

write.csv(new.data, file = "newcsv.csv", row.names = FALSE)

