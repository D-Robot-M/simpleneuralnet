import random
import math


layers = 3

input_train = [[1,0,1],[0,0,1],[0,1,0],[1,1,1]]
output_train = [1,0,0,1]
weights = []

#generate random weights
for i in range(layers):
	weights.append(2*random.random()-1)

#Normalize the weights from 0 to 1
def normalize(inputnum):
	return 1/(1+math.exp(-inputnum))

#use weights to predict
def predict(traindata):

	finalsum = 0
	for counter,x in enumerate(traindata):
		x = x*weights[counter]
		finalsum = finalsum + x
	finalsum = normalize(finalsum)
	return finalsum
#calculate error
def errorfunc(aipredicted, desired):
	return desired - aipredicted

#adjust weight
def adjust_weights(weights, error, predicted, inputs):

	adjustmargin = error * (predicted * (1-predicted)) # x*(1-x) is the derivative of the sigmoid function
	for i in range(len(weights)):
		weights[i] = weights[i] + adjustmargin * inputs[i]
	return weights
#run code
def  Neuralnet(input_train, output_train, weights):
	prediction = predict(input_train)
	error = errorfunc(prediction, output_train)
	weights = adjust_weights(weights, error, prediction, input_train)

print('robot mind working...')
# train for 20000 iterations on all 4 inputs
for i in range(20000):
	for x in range(len(input_train)):
		Neuralnet(input_train[x], output_train[x], weights)
print(weights)
print('considering new possibility [1,1,0] ----> ? ')
print(predict([1,1,0]))
