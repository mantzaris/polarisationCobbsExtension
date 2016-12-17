import numpy 
#extending the Loren Cobbs models to the discrete case for political modelling

print('ok')
####NETWORK SETUP
#number of nodes in linear network
u_N = 5
#nodes in the linear network
numpy.random.rand(1,u_N)
####

####CONSTANTS
#The attractor coefficient/constant GG (what is the 'normal' for each node)
GG = 0.7
#The coefficitent of feedback to state GG (how much force to return to GG)
RR = 1
#The coefficient/constant EE for neighboring influence (how much do they affect)
EE = 1
#The ratio of internal to external influence
DD = EE / RR

#u_i^{t+1} = (u_i^{t}) + (dt * RR * (GG - u_i^{k})) + (EE * u_i^{k} * (1-u_i^{k}) * Su_j^{k}))  for all j neighbors of i, j in a_{i,j} 
#different components for this will be aggregated for clarity



#the feedback effect to return to natural internal state G upon deviation
fb_i = RR * (GG - u_i)
#the contribution of neighbors upon how polarised the node is, more distant less effect
#pol_i = EE * u_i * (1 - u_i) * neighbors_i


