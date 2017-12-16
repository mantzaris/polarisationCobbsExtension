%BIFSIM.M
% Cobb-inspired discrete analogue of an SDE model for political opinion.
%
% Here we run many long-time simulations of the model.
% We are studying how the long time behaviour depends on epsilon.
% Our analysis covers spatially-uniform solutions; that is, steady
% states where all components are equal.
%
% We take N = 12 components.
% In Figure 1, epsilon varies over the horizontal axis. For a given 
% epsilon, we run for a long time (5000 steps) and superimpose all 
% 12 components. So spatially uniform solution will appear as a single 
% dot (all components at the same vertical height on the plot).
%
% We are interested in making sure that the results are consistent
% with our linear stability analysis. Whenever we have identified a 
% linearly stable spatially uniform fixed point, we would like to see
% it emerge in the simulation (i.e. we want to be consistent with  
% the analytically derived bifurcation diagram in the notes).
%
% In this case, the theta = 1/2 steady state is stable for epsilon
% between 0 and 4*r = 2. So we expect to see the theta = 1/2 solution
% in this range. For epsilon between 2 and 4, there are two stable steady 
% states that depend on epsilon, u1 and u2. In order to see these two, we
% run the model twice, once with a low starting value and once with a 
% high starting value. We hope that the low starting value gets
% attracted to u1, and the high starting value to u2.
%
% Figures 2 and 3 show the full long-time solution in each case, 
% as epsilon varies. 
%
% DJH Dec 2016
%
% This version Oct 2017

r = 0.5;
theta = 0.5;

N = 12;

% Set up A for nearest neighbour ring network
A = zeros(N,N);
A = diag(ones(N-1,1),1) + diag(ones(N-1,1),-1);
A(1,N) = 1;
A(N,1) = 1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Repeat over a range of epsilon values
neps = 100;
epsvals = linspace(1,5,neps);

Uwater1 = zeros(neps,N); % use for waterfall plots
Uwater2 = zeros(neps,N); %

figure(1)
clf
for runs = 1:neps,
    runs 
    epsi = epsvals(runs);
    % Do this twice: first with low starting values
    %%%%% Initial values %%%%
    Uzero = linspace(0.1,0.4,N)';   % initial data in (0,1)
    Uk = Uzero;
    steps = 5000;
    for k = 1:steps
      Ukp1 = Uk + r*(theta - Uk) + (epsi)*(Uk.*(1-Uk)).*(0.5*A*Uk - theta);
      %%%%%% Reflection---could make this better? %%%%
      [a1,b1] = find(Ukp1<0);
      [a2,b2] = find(Ukp1>1);
      Ukp1(a1) = 0.05;   % just reflect back to 0.05
      Ukp1(a2) = 0.95;   % or 0.95 
      Uk = Ukp1;
    end
      figure(1)
      plot(epsi*ones(N,1),Uk,'r.')
      hold on
      Uwater1(runs,:) = Uk;
      
    % Second with high starting values
    %%%%% Initial values %%%%
    Uzero = linspace(0.6,0.9,N)';   % initial data in (0,1)
    Uk = Uzero;
    steps = 5000;
    for k = 1:steps
      Ukp1 = Uk + r*(theta - Uk) + (epsi)*(Uk.*(1-Uk)).*(0.5*A*Uk - theta);
      %%%%%% Reflection---could make this better? %%%%
      [a1,b1] = find(Ukp1<0);
      [a2,b2] = find(Ukp1>1);
      Ukp1(a1) = 0.05;   % just reflect back to 0.05
      Ukp1(a2) = 0.95;   % or 0.95
      Uk = Ukp1;
    end
      plot(epsi*ones(N,1),Uk,'b.')
      hold on 
      Uwater2(runs,:) = Uk;
end
ylabel('Long time U values superimposed')
xlabel('epsilon')
print -dpdf pic_bifsim.pdf

figure(2)
clf
waterfall(Uwater1)
ylabel('epsilon')
xlim([1 12])
xlabel('Index for component of U')
zlabel('Long time solution')
print -dpdf pic_water1.pdf

figure(3)
clf
waterfall(Uwater2)
ylabel('epsilon')
xlim([1 12])
xlabel('Index for component of U')
zlabel('Long time solution')
print -dpdf pic_water2.pdf