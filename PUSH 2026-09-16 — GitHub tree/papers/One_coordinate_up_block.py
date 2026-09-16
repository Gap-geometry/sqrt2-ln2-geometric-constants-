# ---------------------------------------------------------------------------
#  ONE COORDINATE UP -- every number in the rows, checked.
#  G(r) := 1 - p(ln r),  p(L) = L/(2 sinh(L/2))
# ---------------------------------------------------------------------------
from mpmath import (mp, mpf, sqrt, log, sinh, cosh, tanh, asinh, acosh, atan, pi, degrees,
        findroot, quad, inf, nstr, exp)
import sys
FAILS = 0; CHECKS = 0
def ck(label, ok):
    global FAILS, CHECKS
    CHECKS += 1
    if not ok: FAILS += 1; print("  [FAIL]", label)
    elif VERBOSE: print("  [ok]  ", label)
VERBOSE = "-v" in sys.argv

def row(r):
    L = log(r); X = sinh(L/2); u = cosh(L); base = 4/X**2 if X != 0 else mpf('inf')
    p = L/(2*sinh(L/2)) if L != 0 else mpf(1)
    th = atan(sinh(L)); tau = (r-1)/(r+1)
    return dict(r=r, L=L, X=X, u=u, base=base, p=p, G=1-p, theta=th, tau=tau)

for dps in (30, 60, 200, 500):
    mp.dps = dps; eps = mpf(10)**(-(dps-6))
    phi = (1+sqrt(5))/2; ln2 = log(2)
    # ---- row r = 1: the wall
    R = row(mpf(1)); ck("r=1: L=0, X=0, u=1, p=1, G=0", R['L']==0 and R['X']==0 and R['u']==1
            and R['G']==0)
    # ---- row r = 2: The complement's point
    R = row(mpf(2))
    ck("r=2: X = 1/(2 sqrt2), X^2 = 1/8, base 32",      abs(R['X']-1/(2*sqrt(2)))<eps
            and abs(R['X']**2-mpf(1)/8)<eps and abs(R['base']-32)<eps)
    ck("r=2: u = 5/4",                                   abs(R['u']-mpf(5)/4)<eps)
    ck("r=2: p = sqrt2 ln2 = 0.98025814346854719171...", abs(R['p']-sqrt(2)*ln2)<eps
            and abs(R['p']-mpf('0.98025814346854719171'))<mpf('1e-20'))
    ck("r=2: G = 0.019741856531452808286...",
            abs(R['G']-mpf('0.019741856531452808286'))<mpf('1e-21'))
    ck("r=2: arsinh(X) = ln2/2 (HK Thm 4.4; HK Closed Form and the Framework sec 2)",
            abs(asinh(R['X'])-ln2/2)<eps)
    ck("r=2: HK's S = X/arsinh X = 1/p = 1.02013944659678948...",
             abs(R['X']/asinh(R['X'])-1/R['p'])<eps
            and abs(1/R['p']-mpf('1.0201394465967894817'))<mpf('1e-18'))
    ck("r=2: EA's b = 2+sqrt2 solves b^2-4b+2=0 with b = 1/(1-e^{-L/2}) (Saturation "
            "Constants Thm 3.2)",
            
            abs(1/(1-exp(-ln2/2))-(2+sqrt(2)))<eps
            and abs((2+sqrt(2))**2-4*(2+sqrt(2))+2)<eps)
    ck("r=2: tau = 1/3; theta = arctan(3/4) = 36.8699 deg; sinh L = 3/4, cosh L = 5/4 (the "
            "3-4-5 triangle)",
            
            abs(R['tau']-mpf(1)/3)<eps
            and abs(R['theta']-atan(mpf(3)/4))<eps
            and abs(sinh(R['L'])-mpf(3)/4)<eps)
    ck("r=2: series 1/48 - 3/2560 + ... = G (first two partial sums bracket)",
            mpf(151)/7680 < R['G'] < mpf(1)/48)
    # ---- row r = 1+sqrt2 (door one): dome self-reference, sinh L = 1
    R = row(1+sqrt(2))
    ck("r=1+sqrt2: u = cosh L = sqrt2; sinh L = 1",      abs(R['u']-sqrt(2))<eps
            and abs(sinh(R['L'])-1)<eps)
    ck("r=1+sqrt2: chord r - 1/r = 2 (metallic k=2, norm -1)",
            abs((1+sqrt(2))-1/(1+sqrt(2))-2)<eps and abs((1+sqrt(2))*(1-sqrt(2))+1)<eps)
    ck("r=1+sqrt2: theta = 45 deg exactly",              abs(R['theta']-pi/4)<eps)
    gu = lambda v: sqrt(v-1)/(v*sqrt(v+1))
    from mpmath import diff
    ck("r=1+sqrt2: dome g'/g = g at u = sqrt2 (eta Corridor Thm 9.4); g = 1 - 1/sqrt2",
             abs(diff(gu,sqrt(2))/gu(sqrt(2))-gu(sqrt(2)))<mpf(10)**(-(dps-12))
            and abs(gu(sqrt(2))-(1-1/sqrt(2)))<eps)
    ck("r=1+sqrt2: X = sinh(L/2) = sqrt((sqrt2-1)/2) = 0.45508986...",
            abs(R['X']-sqrt((sqrt(2)-1)/2))<eps)
    ck("r=1+sqrt2: base 4/X^2 = 8/(sqrt2-1) = 8(sqrt2+1) = 19.3137...",
            abs(R['base']-8*(sqrt(2)+1))<eps)
    # ---- row r = phi^2: golden cell
    R = row(phi**2)
    ck("r=phi^2: X = 1/2 (chord of phi is 1); u = 3/2 (t₂ = 3); base 16",
            abs(R['X']-mpf(1)/2)<eps and abs(R['u']-mpf(3)/2)<eps and abs(R['base']-16)<eps)
    ck("r=phi^2: G(phi^2) = 1 - 2 ln phi (the L=2 ln phi, X=1/2 evaluation)",
            abs(R['G']-(1-2*log(phi)))<eps)
    ck("r=phi^2: theta = arctan(sinh L) = arccos(2/3) = 48.1897 deg",
            abs(R['theta']-mp.acos(mpf(2)/3))<eps)
    # ---- row r = phi + sqrt(phi): dome peak u = phi
    rpk = phi+sqrt(phi); R = row(rpk)
    ck("r=phi+sqrt(phi): u = cosh L = phi exactly",     abs(R['u']-phi)<eps)
    ck("r=phi+sqrt(phi): g(u) = phi^(-5/2), g'(u) = 0 (eta Corridor Cor 9.3)",
            abs(gu(phi)-phi**(-mpf(5)/2))<eps and abs(diff(gu,phi))<mpf(10)**(-(dps-12)))
    ck("r=phi+sqrt(phi): X = sinh(L/2) = sqrt((phi-1)/2) = sqrt(1/(2 phi)); base = 8 phi",
            abs(R['X']-sqrt(1/(2*phi)))<eps and abs(R['base']-8*phi)<eps)
    # ---- row r = 2+sqrt3: HK's R0, base 8
    R = row(2+sqrt(3))
    ck("r=2+sqrt3: X = 1/sqrt2, base 8, u = 2 (t₂ = 4)", abs(R['X']-1/sqrt(2))<eps
            and abs(R['base']-8)<eps and abs(R['u']-2)<eps)
    ck("r=2+sqrt3: L/2 = arcosh(2)/2 = arsinh(1/sqrt2) = artanh(1/sqrt3) = R0 = "
            "0.658478948...",
            
            abs(R['L']/2-acosh(2)/2)<eps
            and abs(R['L']/2-asinh(1/sqrt(2)))<eps
            and abs(R['L']/2-mpf('0.6584789484624083'))<mpf('1e-15'))
    ck("r=2+sqrt3: dome g(2) = 1/(2 sqrt3); D[sech^2] maximal at L/2 (tanh = 1/sqrt3)",
            abs(gu(2)-1/(2*sqrt(3)))<eps and abs(tanh(R['L']/2)-1/sqrt(3))<eps)
    ck("r=2+sqrt3: theta = 60 deg exactly; partner of 2+sqrt3 is sqrt3 (sinh L * sinh L' = 1)",
            abs(R['theta']-pi/3)<eps and abs(sinh(R['L'])*sinh(log(sqrt(3)))-1)<eps)
    # ---- row r = 3: complement of 2
    R = row(mpf(3))
    ck("r=3: X = 1/sqrt3, base 12, u = 5/3; K(3) = sqrt3 ln3 = 2 p(ln3)",
            abs(R['X']-1/sqrt(3))<eps and abs(R['base']-12)<eps
                    and abs(sqrt(3)*log(3)-2*R['p'])<eps)
    ck("r=3: theta(2)+theta(3) = 90 deg (sinh ln2 * sinh ln3 = 1)",
            abs(row(mpf(2))['theta']+R['theta']-pi/2)<eps)
    # ---- row r = 5: last integer base
    R = row(mpf(5))
    ck("r=5: X = 2/sqrt5, base 5, u = 13/5 (the 5-12-13 triangle); K(5) = 4 p(ln5)",
             abs(R['X']-2/sqrt(5))<eps and abs(R['base']-5)<eps and abs(R['u']-mpf(13)/5)<eps
            and abs(sqrt(5)*log(5)-4*R['p'])<eps)
    ck("integer base 16n/(n-1)^2 is an integer only for n = 2, 3, 5 (n <= 60)",
            [n for n in range(2,61) if (16*n) % ((n-1)**2)==0]==[2,3,5])
    # ---- row r = 3+2sqrt2: the boundary
    R = row(3+2*sqrt(2))
    ck("r=3+2sqrt2: X = 1, base 4, u = 3 (t₂ = 6); = (1+sqrt2)^2", abs(R['X']-1)<eps
            and abs(R['base']-4)<eps and abs(R['u']-3)<eps
                    and abs((1+sqrt(2))**2-(3+2*sqrt(2)))<eps)
    ck("r=3+2sqrt2: L = 2 ln(1+sqrt2): the square of door one, one doubling up",
            abs(R['L']-2*log(1+sqrt(2)))<eps)
    ck("r=3+2sqrt2: theta = arccos(1/3) = 70.5288 deg", abs(cosh(R['L'])-3)<eps)
    # ---- the inflection of G in L
    Gfun = lambda L: 1 - L/(2*sinh(L/2))
    Lstar = findroot(lambda L: diff(Gfun, L, 2), 3.2)
    ck("inflection: L* = 3.212230597605..., r* = e^{L*} = 24.834...",
            abs(Lstar-mpf('3.212230597605'))<mpf('1e-11')
                    and abs(exp(Lstar)-mpf('24.834'))<mpf('1e-3'))
    ck("inflection: G' > 0 at every tested L (no extremum)", all(diff(Gfun,
            mpf(t)) > 0 for t in [0.1,0.5,1,2,3,5,8]))
    # ---- Bernoulli radius
    ck("Bernoulli series radius: |L/2| < pi  <=>  r < e^{2 pi} = 535.4916...",
            abs(exp(2*pi)-mpf('535.49165552476473'))<mpf('1e-10'))
    # ---- the wall from the other side: the circular twin at the matched Cayley coordinate
    tau = mpf(1)/3; beta = 2*atan(tau)
    ck("twin at r=2's tau: beta = 2 arctan(1/3) = theta(2); beta/(2 sin(beta/2)) = "
            "1.01746459...",
            
            abs(beta-row(mpf(2))['theta'])<eps
            and abs(beta/(2*mp.sin(beta/2))-mpf('1.01746459032'))<mpf('1e-10'))
    # ---- the offered row: O(N) cells 2^{12/(N+8)}
    for N, val in [(0, 2*sqrt(2)), (1, mpf(2)**(mpf(4)/3)), (2, mpf(2)**(mpf(6)/5)), (3,
            mpf(2)**(mpf(12)/11)), (4, mpf(2))]:
        ck(f"offered row: r_N = 2^(12/(N+8)) at N={N}", abs(mpf(2)**(mpf(12)/(N+8))-val)<eps)
    ck("offered row: N = 4 lands on r = 2, i.e. c*a(4) = 2 ln2 * 3/12 = ln2/2",
            abs(2*ln2*mpf(3)/12-ln2/2)<eps)
    # ---- the mirror: r and 1/r give the same G
    ck("mirror: G(1/2) = G(2); G(1/(2+sqrt3)) = G(2+sqrt3)",
             abs(row(mpf(1)/2)['G']-row(mpf(2))['G'])<eps
            and abs(row(1/(2+sqrt(3)))['G']-row(2+sqrt(3))['G'])<eps)
    print(f"dps {dps:4d}   checks so far {CHECKS}   failures {FAILS}")

print("="*64); print(f"  CHECKS {CHECKS}   FAILURES {FAILS}"); print("="*64)
if FAILS: sys.exit(1)
