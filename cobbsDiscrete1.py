#extending the Loren Cobbs models to the discrete case for political modelling

print('ok')

#The attractor coefficient/constant GG (what is the 'normal' for each node)
GG = 0.7

#The coefficitent of feedback to state GG (how much force to return to GG)
RR = 1

#The coefficient/constant EE for neighboring influence (how much do they affect)
EE = 1

#The ratio of internal to external influence
DD = EE / RR


#u_i^{t+1} = (u_i^{t}) + (dt * RR * (GG - u_i^{k})) + (EE * u_i^{k} * (1-u_i^{k}) * Su_j^{k}))  for all j neighbors of i, j in a_{i,j} 

