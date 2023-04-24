function output = export_all(sol)

output.t = transpose(sol.time);
output.v = sol.V;
output.j = sol.J;
output.jd = sol.Jd;

[output.phi, output.phiE, output.phiH] = ...
    struct2array(sol.dstrbns,{'phi','phiE','phiH'});

[output.n, output.nE] = ...
    struct2array(sol.dstrbns,{'n','nE'});

[output.p, output.pH] = ...
    struct2array(sol.dstrbns,{'p','pH'});

[output.P] = ...
    struct2array(sol.dstrbns,{'P'});

[output.x, output.xE, output.xH] = ...
    struct2array(sol.vectors,{'x','xE','xH'});

sol = compute_QFLs(sol);

[output.efn, output.efp, output.efne, output.efph] = ...
    struct2array(sol.dstrbns,{'Efn','Efp','EfnE','EfpH'});

output.pb = abs(sol.dstrbns.phiE(:,1)-sol.dstrbns.phi(:,end) ...
    +sol.params.Ev-sol.dstrbns.EfpH(:,1)-sol.dstrbns.phiE(:,1));

output.nb = abs(sol.dstrbns.phiE(:,1)-sol.dstrbns.phi(:,1) ...
    +sol.params.Ec-sol.dstrbns.EfnE(:,1)-sol.dstrbns.phiE(:,1));

end