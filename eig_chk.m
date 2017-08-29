%RUN_EXTREME.M
% Check eigenvalues of ring network. 
%
% DJH March 2017
%

N = input(' Type in N   ')

% Set up A for nearest neighbour ring network
A = zeros(N,N);
A = diag(ones(N-1,1),1) + diag(ones(N-1,1),-1);
A(1,N) = 1;
A(N,1) = 1;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[V,D] = eig(A);
ev = diag(D);
sv = sort(ev);

lambdas = 2*cos(2*pi*[1:N]'/N);
lambdas = sort(lambdas);

[ev lambdas]

chk = norm(sv - lambdas)

