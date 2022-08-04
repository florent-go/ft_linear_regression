file  = open("save.csv", 'r')

theta, theta1 = file.read().split(' ')

x = input("Enter a kilometer: ")
print('Predicted price: ', float(theta1) + float(x) * float(theta))