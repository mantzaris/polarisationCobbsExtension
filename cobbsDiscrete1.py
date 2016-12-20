import numpy 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as P
#extending the Loren Cobbs models to the discrete case for political modelling

####NETWORK SETUP
#time points
time_pnts = 14
#number of nodes in linear network
u_N = 15
#nodes in the linear network
network = numpy.random.rand(1,u_N)
network_tmp = numpy.zeros((1,u_N))
network_total = numpy.zeros((time_pnts,u_N))
network_total[0,:] = network
####

####CONSTANTS
#The attractor coefficient/constant GG (what is the 'normal' for each node)
GG = 0.5
#The coefficitent of feedback to state GG (how much force to return to GG)
RR = 0.001
#The coefficient/constant EE for neighboring influence (how much do they affect)
EE = 1000
#The ratio of internal to external influence
DD = EE / RR

####MODEL
#u_i^{t+1} = (u_i^{t}) + (dt * RR * (GG - u_i^{k})) + (EE * u_i^{k} * (1-u_i^{k}) *( Su_j^{k}-GG))  for all j neighbors of i, j in a_{i,j} 
#different components for this will be aggregated for clarity

for tt in range(1,time_pnts):
    for ii in range(u_N):        
        u_i = network_total[tt-1,ii]#value of current node        
        neighbors_i = -1
        if (ii == 0):#sum neighbors
            neighbors_i = network_total[tt-1,1]
        elif (ii == (u_N-1)):
            neighbors_i = network_total[tt-1,u_N-2]
        else:
            neighbors_i = 0.5*((network_total[tt-1,ii-1]) + (network_total[tt-1,ii+1]))
        #the feedback effect to return to natural internal state G upon deviation
        fb_i = RR * (GG - u_i)                  
        #contribution of neighbors upon polarisation extent
        pol_i = EE * u_i * (1 - u_i) * (neighbors_i - GG)
        #put all the contributions together for the iteration
        u_i_t = u_i + fb_i + pol_i
        if(u_i_t < 0):
            u_i_t = 0
        elif(u_i_t > 1):
            u_i_t = 1   
        #update the network temp array
        network_tmp[0,ii] = u_i_t    
    network_total[tt,:] = network_tmp[0,:]    
    #plot the histogram of the u_i after each iteration
binspaces = [ii/10 for ii in range(0,11)]
#P.figure()
print(network_total)
f,axarr = plt.subplots(time_pnts,sharex=True)
for ii in range(time_pnts):
    axarr[ii].hist(network_total[ii,:], binspaces,normed=1,histtype='bar')
    axarr[ii].set_title('iteration:'+str(ii))
    #axarr[ii].xlabel('u')
f.suptitle('RR value='+str(RR)+', EE value='+str(EE)+', DD value='+str(DD))
P.show()
#axarr[0].hist(network_total[0,:], binspaces,normed=1,histtype='bar')
#axarr[1].hist(network_total[1,:], binspaces,normed=1,histtype='bar')
