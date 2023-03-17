function sol = master_func(pyonin)
% This is the master script for running a single simulation.

% Begin
tic;
fprintf('Computation started at %s\n', datestr(now));
reset_path();

% Create a structure filled with the user-defined parameters
params = pyonio_slow_jv(pyonin);

% Solve the equations
if strcmp(params.applied_voltage{1},'impedance')
    % if the voltage protocol specifies an impedance protocol
    sol = IS_solver(params);
else
    sol = numericalsolver(params);
end

% Stop stopwatch and output nice message
fprintf('Completed simulation at %s, taking %s\n', ...
    datestr(now), secs2hms(toc) );
