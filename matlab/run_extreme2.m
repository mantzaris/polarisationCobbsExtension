%RUN_EXTREME.M
% Cobb-inspired ODE model for political opinion.
%
% Hi Alex,
% Below is a MATLAB code for the model.
% The roots of the quadratic u(1-u) = r/epsi are u=0.9472 and 0.0528
% I can see these values arising in the iteration,
% The ietation can tend to a steady state at one of these
% values or thet other. If we start with two levels: first N/2
% nodes low and last N/2 nodes high, then the fisrt N/2 nodes tend to the 
% low value and the seod N/2 modes tend to the high vaue, before one
% the levels eventually wins out.
% 
% I can also see iterations were everyhtign tends to g.
%
% So I think we need to do a stability analysis to see when 
% these states are attractive.
%
% cheers,
% Des
%
% DJH Dec 2016
%

r = 0.05;
epsi = 1;
g = 0.7;

N = 12;

% Set up A for nearest neighbour ring network
A = zeros(N,N);
A = diag(ones(N-1,1),1) + diag(ones(N-1,1),-1);
A(1,N) = 1;
A(N,1) = 1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%% Initial values %%%%
Uzero = zeros(N,1);
%Uzero = g + 0.2*rand(N,1);   % initial data random in (0,1)
Uzero(1:N/2) = 0.35;          %
Uzero(N/2+1:end) = 0.8;       %
%Uzero = 0.8*ones(N,1);       % all fixed at 0.8
Uk = Uzero;
steps = 50;
Usol = zeros(N,steps+1);
Usol(:,1) = Uzero;
for k = 1:steps
    Ukp1 = Uk + r*(g - Uk) + (epsi)*(Uk.*(1-Uk)).*(0.5*A*Uk - g);
    %%%%%% Reflection---cold make this better? %%%%
    [a1,b1] = find(Uk<0);
    [a2,b2] = find(Uk>1);
    Uk(a1) = 0.005;   % just reflect back to 0.005
    Uk(a2) = 0.995;   % or 0.995
    Uk'    
    Usol(:,k+1) = Ukp1;
    Uk = Ukp1;
end

waterfall(Usol')
c(1) = 1; 
c(2) = -1;
c(3) = r/epsi;
roots(c)