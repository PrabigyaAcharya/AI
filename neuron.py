import math

def sigmoid(x):
    return 1/(1+math.pow(math.e, -x))



def activate(inputs, weights):
    #sum calculation and activation
    h = float(0)
    for x, w in zip(inputs, weights):
        h += w*x
    return sigmoid(h)
    


inputs=[.5, .3, .2]
weights=[.4, .7, .2]
output=activate(inputs, weights)
print(output)
