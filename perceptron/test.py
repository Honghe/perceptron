#!/usr/bin/env python
#coding: utf-8

from matplotlib.pylab import *
# local module
import generate_data
import perceptron

trainset = generate_data.generateData(80) # train set generation
testset = generate_data.generateData(20) # test set generation
p = perceptron.Perceptron() # use a short
p.train(trainset)

#Perceptron test
for x in testset:
    r = p.response(x)
    if r != x[2]: # if the response is not correct
        print 'not hit.'
    if r == 1:
        plot(x[0], x[1], 'ob')
    else:
        plot(x[0], x[1], 'or')

# plot of the separation line. 
# The centor of line is the coordinate origin
# So the length of line is 2
# The separation line is orthogonal to w
n = norm(p.w) # aka the length of p.w vector
ww = p.w / n # a unit vector
ww1 = [ww[1], -ww[0]]
ww2 = [-ww[1], ww[0]]
plot([ww1[0], ww2[0]], [ww1[1], ww2[1]], '--k')
show()
