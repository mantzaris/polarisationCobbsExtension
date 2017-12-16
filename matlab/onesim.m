%ONESIM.M
% Accompanies BIFSIM.M
% DOES A SINGLE RUN WHERE U1 ans U2 ARE STABLE.
%
% Shows how the existence of two differemt, stable solutions can 
% affect the intermediate time behaviour.
% Eventually, one of the two solutions dominates. 
% In this case the lower value, u1, wins out in the end.
% But we can see u2 tryng to attract the solution before it loses out.
%
% DJH Dec 2016
%
% This version Oct 2017

figure(1)
clf

r = 0.5;
theta = 0.5;

N = 12;
N = 32;

% Set up A for nearest neighbour ring network
A = zeros(N,N);
A = diag(ones(N-1,1),1) + diag(ones(N-1,1),-1);
A(1,N) = 1;
A(N,1) = 1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

epsi = 2.5;
u1 = 0.5 - 0.5*sqrt(1 - 4*r/epsi)
u2 = 0.5 + 0.5*sqrt(1 - 4*r/epsi)

%%%%% Initial values %%%%
Uzero = linspace(0.2,0.8,N)';   % initial data in (0,1)
x = linspace(-10,10,N)';
Uzero = (0.5 + 0.2*sin(x));   % initial data in (0,1)
sig1 = exp(x)./(1 + exp(x));
sig2 = exp(10-x)./(1+exp(10-x));
%Uzero = 0.3*sig1 + 0.25*sig2; % initial data in (0,1)
Uzero = 0.35*sig1 + 0.2*sig2; % initial data in (0,1)
Uk = Uzero;
steps = 400-1;
Usol = zeros(N,steps+1);
Usol(:,1) = Uzero;
for k = 1:steps   
   Ukp1 = Uk + r*(theta - Uk) + (epsi)*(Uk.*(1-Uk)).*(0.5*A*Uk - theta);      %%%%%% Reflection---could make this better? %%%%
   [a1,b1] = find(Ukp1<0);
   [a2,b2] = find(Ukp1>1);
   Ukp1(a1) = 0.05;   % just reflect back to 0.05
   Ukp1(a2) = 0.95;   % or 0.95 
   Usol(:,k+1) = Ukp1;
   Uk = Ukp1;
end


waterfall(Usol')
ylabel('time')
xlabel('U component')
xlim([0 N])
%xlim([1 12])
%xlabel('Components of U')
print -dpdf pic_onesima.pdf 

figure(2)
clf
plot(Usol(:,1),'r-')
hold on
plot(Usol(:,200),'b-')
plot(Usol(:,end),'k-')
xlim([1 N])
xlabel('U component')
legend('Initial','Intermediate','Final','Location','Northwest') 
print -dpdf pic_onesimb.pdf 
