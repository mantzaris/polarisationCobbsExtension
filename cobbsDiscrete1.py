import numpy 
#extending the Loren Cobbs models to the discrete case for political modelling

print('ok')
####NETWORK SETUP
#number of nodes in linear network
u_N = 5
#nodes in the linear network
network = numpy.random.rand(1,u_N)
#time points
time_pnts = 4
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

####MODEL
#u_i^{t+1} = (u_i^{t}) + (dt * RR * (GG - u_i^{k})) + (EE * u_i^{k} * (1-u_i^{k}) * Su_j^{k}))  for all j neighbors of i, j in a_{i,j} 
#different components for this will be aggregated for clarity

for tt in range(time_pnts):
    for ii in range(u_N):
        u_i = network[0,ii]#value of current node
        neighbors_i = -1
        if (ii == 0):#sum neighbors
            neighbors_i = network[0,1]
        elif (ii == (u_N-1)):
            neighbors_i = network[0,u_N-2]
        else:
            neighbors_i = (network[0,ii-1] + network[0,ii+1])
        #the feedback effect to return to natural internal state G upon deviation
        fb_i = RR * (GG - u_i)
        #contribution of neighbors upon polarisation extent
        pol_i = EE * u_i * (1 - u_i) * neighbors_i
        #put all the contributions together for the iteration
        u_i_t = u_i + fb_i + pol_i
        print(network)
        print([u_i,neighbors_i,u_i_t])
        print([fb_i,pol_i])

