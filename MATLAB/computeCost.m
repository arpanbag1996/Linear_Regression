%%Arpan Bag
%%Cost Function

function J = computeCost(X, Y, theta)

%COMPUTECOST Compute cost for linear regression with multiple variables
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y




% Initialize some useful values
m = length(Y); %Number of training examples

J = 0;	%Cost

% =========================== CODE HERE ========================
% Instructions: Compute the cost of a particular choice of theta
%               Should set J to the cost.


J = 1/(2*m)*sum((X*theta - Y).^2);


% =========================================================================

end
