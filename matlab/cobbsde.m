%COBBSDE  Test SDE from Cobbb article, 1981.
%
% Solves    dx = r(G - x)dt + sqrt(eps*x(1-x))dW,  
%          where G = 0.5, r = 1.
% Gives several independent paths for various eps.
%

randn('state',100)
G = 0.5; 
r = 1;
Xzero = 0.4;    %initial condition 
T  = 10;        % time length of paths
N = 5000;      % number of timepoints in numerical method
dt = T/N;       % numerical timestep

figure(1)
clf
epsi = input('Type in a value for epsi (e.g. 0.1 or 2) ')

M = 1000;                % number of paths

xfinal = zeros(M,1);     % store endpoint value for each path
for s = 1:M,             % loop over M independent paths
    X = zeros(N+1,1);    % preallocate array
    X(1) = Xzero;
    xold = X(1);
    for n = 1:N,
        drift = r*(G - xold);             %drift 
        diff = sqrt(epsi*xold*(1-xold));  %diffusion
        dw = sqrt(dt)*randn;              %Brownian increment
        xnew = xold + dt*drift + diff*dw; %Euler-Maruyama 
        %%%% make sure xnew is between 0 and 1 %%%%%
        if abs(xnew) > 1, xnew = xnew/abs(xnew); end
        if xnew < 0, xnew = abs(xnew); end
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        X(n+1) = xnew;
        xold = xnew;  
    end
    % Plot every 100th path
    if rem(s,100) == 0,
    plot([0:dt:T],X,'r-');   % plot the sth path
    hold on
    end
    xfinal(s) = xnew;
end
title('Some paths')
xlabel('time')
ylabel('x')

figure(2)
clf
% histogram of the values at time T
hist(xfinal,40)
title('Histogram of values t = T')