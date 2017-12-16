%CHECK_JAC.M
% Check my derivation of Jacobian of F.
% Use finite differences. 
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
A = 0.5*A;

chk = 0;
for j = 1:10,
    %Test Jacobian acting in a random direction 
   
    u = rand(N,1);     %point where we evaluate
    du = rand(N,1);    %direction of perturbation
    h = 1e-6;          %size of perturbation
    Fu = u + r*(g - u) + (epsi)*(u.*(1-u)).*(A*u - g);
    up = u + h*du;
    Fup = up + r*(g - up) + (epsi)*(up.*(1-up)).*(A*up - g);
    Fderiv = (Fup-Fu)/h;
    

    d1 = (1-2*u).*(A*u-g);
    d2 = u.*(1-u);
    Jac = (1-r)*eye(N,N) + epsi*diag(d1) + epsi*diag(d2)*A;
    Fderiv2 = Jac*du;

    chk = max(chk,norm(Fderiv-Fderiv2));

end
    
chk % max error
[Fderiv Fderiv2]    % check final value


