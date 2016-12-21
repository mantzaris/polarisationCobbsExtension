import numpy 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as P
from pylab import *
#extending the Loren Cobbs models to the discrete case for political modelling

####NETWORK SETUP
#time points
time_pnts = 20
#number of nodes in linear network
u_N = 14
#nodes in the linear network
network = numpy.random.rand(1,u_N)
network_tmp = numpy.zeros((1,u_N))
network_total = numpy.zeros((time_pnts,u_N))
network_total[0,:] = network
####

####CONSTANTS
#The attractor coefficient/constant GG (what is the 'normal' for each node)
GG = 0.45
#The coefficitent of feedback to state GG (how much force to return to GG)
RR = 0.01
#The coefficient/constant EE for neighboring influence (how much do they affect)
EE = 100.00000
#The ratio of internal to external influence
DD = EE / RR

####MODEL
#u_i^{t+1} = (u_i^{t}) + (dt * RR * (GG - u_i^{k})) + (EE * u_i^{k} * (1-u_i^{k}) *( Su_j^{k}-GG))  for all j neighbors of i, j in a_{i,j} 
#different components for this will be aggregated for clarity

for tt in range(1,time_pnts):
    for ii in range(u_N):        
        u_i = network_total[tt-1,ii]#value of current node        
        neighbors_i = -1
        if (ii == 0):#avg neighbors for the first node that wraps to the last node
            neighbors_i = 0.5*(network_total[tt-1,1] + network_total[tt-1,u_N-1])
        elif (ii == (u_N-1)):#avg neighbors for the last node that wraps to 
            neighbors_i = 0.5*(network_total[tt-1,u_N-2] + network_total[tt-1,0])
        else:
            neighbors_i = 0.5*((network_total[tt-1,ii-1]) \
                               + (network_total[tt-1,ii+1]))
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
f,axarr = plt.subplots(time_pnts,sharex=True)
network_gryscle = numpy.zeros((time_pnts,len(binspaces)-1))
for ii in range(time_pnts):
    nn,bb,pp = axarr[ii].hist(network_total[ii,:], binspaces,normed=1,histtype='bar')
    network_gryscle[ii,:] = (nn / numpy.sum(nn))
    #axarr[ii].set_title('iteration:'+str(ii))
    #axarr[ii].xlabel('u')
f.suptitle('RR value='+str(RR)+', EE value='+str(EE)+'\n DD value='+str(DD))

#######
#grayscale/heatmap of the number of nodes occupying each bin of the spectrum
fig2,ax2 = plt.subplots(1,1)
plt.imshow(network_gryscle,cmap='gray',interpolation='none')
pos_tmp = [binspaces[ii]*10 for ii in range(len(binspaces))]
ax2.set_xticks(np.arange(-.5, 10, 1));
ax2.set_xticklabels(np.arange(0, 1.1, 0.1));

plt.xlabel('polarisation interval')
plt.ylabel('iteration number')
plt.title('density of the bins along the political spectrum over time'+'\n DD value='+str(DD))
plt.colorbar()
#figure()
################
f,ax = plt.subplots(1,1)
norm1 = mpl.colors.Normalize(vmin=0.0,vmax=1.0)
plt.imshow(network_total,cmap='gray',norm=norm1,interpolation='none')
pos_tmp = [ii for ii in range(u_N)]
pos_tmp2 = [ii+1 for ii in range(u_N)]
xticks(pos_tmp,pos_tmp2)
plt.ylabel('iteration number')
plt.xlabel('node id')
plt.title('political parameters for each node over time'+'\n DD value='+str(DD))
plt.colorbar()
f.tight_layout()
P.show()



