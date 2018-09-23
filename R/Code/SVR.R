dataset = read.csv("Position_Salaries.csv")

dataset = dataset[2:3]
#Feature Scaling

# regressor
#create regressor
library(e1071)
regressor= svm(formula= Salary ~ .,data= dataset, type= 'eps-regression')

#predict with regression
y_pred = predict(regressor, data.frame(Level = 6.5))


#visualize regression
library(ggplot2)

ggplot() + geom_point(aes(x= dataset$Level, y=dataset$Salary), color='red')+ geom_line(aes(x=dataset$Level, y=predict(regressor, newdata= dataset)), color='blue')
+ ggtitle("SVR")+ xlab("Level")+ ylab("Salary")

#visualize regression smooth curve

x_grid= seq(min(dataset$Level), max(dataset$Level),0.1)
ggplot() + geom_point(aes(x= dataset$Level, y=dataset$Salary), color='red')+ geom_line(aes(x=x_grid, y=predict(regressor, newdata= data.frame(Level= x_grid))), color='blue')
+ ggtitle("SVR")+ xlab("Level")+ ylab("Salary")

