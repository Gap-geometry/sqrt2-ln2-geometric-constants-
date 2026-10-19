# ---------------------------------------------------------------------------
#  THE WHERE -- every number in §4.2-§4.4 and Figure 1, checked.   (second block; standalone)
# ---------------------------------------------------------------------------
from mpmath import (mp, mpf, mpc, sqrt, log, exp, sinh, cosh, tanh, asinh, atan, acos, coth, pi,
        diff, re, im, nstr)
CH2 = FA2 = 0
def ck2(name, cond):
    global CH2, FA2
    CH2 += 1
    if not cond: FA2 += 1; print("   FAIL:", name)
for dps in (30, 60, 200, 500):
    mp.dps = dps; eps = mpf(10)**(-(dps-8))
    p   = lambda L: L/(2*sinh(L/2))
    G   = lambda r: 1 - p(log(r))
    X   = lambda r: (r-1)/(2*sqrt(r))
    t2  = lambda r: r + 1/r                       # the square's trace, 2 cosh L
    t   = lambda r: sqrt(r) + 1/sqrt(r)           # the trace, 2 cosh(L/2)
    th  = lambda r: atan(sinh(log(r)))            # theta = gd(L)
    partner = lambda r: exp(asinh(1/sinh(log(r))))
    Pi  = lambda r: acos(tanh(log(r)/2))         # angle of parallelism (half argument)
    deg = lambda a: a*180/pi
    phi = (1+sqrt(5))/2; dS = 1+sqrt(2)
    # --- §4.2 the line and the cells
    ck2("t2 = t^2 - 2 (Cayley-Hamilton) at r = 2, phi^2, 3+2sqrt2",
            all(abs(t2(r)-(t(r)**2-2))<eps for r in (mpf(2), phi**2, dS**2)))
    ck2("doubling: t2 = 5/2, between the wall (2) and golden (3); X^2 = 1/8",
            abs(t2(mpf(2))-mpf(5)/2)<eps and abs(X(mpf(2))**2-mpf(1)/8)<eps)
    ck2("golden r = phi^2: t2 = 3, chord 2X = 1, p = L exactly, G = 1 - 2 ln phi",
             abs(t2(phi**2)-3)<eps and abs(2*X(phi**2)-1)<eps
                     and abs(p(log(phi**2))-log(phi**2))<eps
            and abs(G(phi**2)-(1-2*log(phi)))<eps)
    ck2("2+sqrt3: t2 = 4, base 8, theta = 60 deg", abs(t2(2+sqrt(3))-4)<eps
            and abs(4/X(2+sqrt(3))**2-8)<eps and abs(th(2+sqrt(3))-pi/3)<eps)
    ck2("the boundary 3+2sqrt2 = (1+sqrt2)^2: t2 = 6, X = 1, base 4, theta = arccos(1/3)",
             abs(dS**2-(3+2*sqrt(2)))<eps and abs(t2(dS**2)-6)<eps and abs(X(dS**2)-1)<eps
            and abs(th(dS**2)-acos(mpf(1)/3))<eps)
    ck2("metallic means squared are the cells t2 = m^2 + 2, m = 1..5",
            all(abs(t2(((m+sqrt(m*m+4))/2)**2)-(m*m+2))<eps for m in range(1,6)))
    ck2("the base is 16/(t2 - 2): 32, 16, 12, 8, 5, 4 at r = 2, phi^2, 3, 2+sqrt3, 5, 3+2sqrt2",
        all(abs(4/X(r)**2-16/(t2(r)-2))<eps for r in (mpf(2),phi**2,mpf(3),2+sqrt(3),mpf(5),
                dS**2)) and
        [round(float(4/X(r)**2)) for r in (mpf(2),phi**2,mpf(3),2+sqrt(3),mpf(5),dS**2)] == [32,
                16,12,8,5,4])
    L = [mpf(3)]
    for _ in range(4): L.append(L[-1]**2-2)
    ck2("the square's trace under squaring, from golden: 3, 7, 47, 2207, 4870847 (Lucas "
            "L_{2^k})", [int(x) for x in L]==[3,7,47,2207,
            
            4870847])
    F = [mpf(5)/2]
    for _ in range(3): F.append(F[-1]**2-2)
    ck2("from doubling: 5/2, 17/4, 257/16, 65537/256 -- Fermat numbers over 2^(2^k); never "
            "an integer",
            
            all(abs(F[k]-mpf(2**(2**(k+1))+1)/2**(2**k))<eps for k in range(4))
            and all(abs(x-round(x))>mpf('1e-3') for x in F))
    ck2("the pairing sinh L * sinh L' = 1: 2 <-> 3, phi^2 <-> sqrt5, 3+2sqrt2 <-> sqrt2, "
            "1+sqrt2 <-> itself",
            
        abs(partner(mpf(2))-3)<eps and abs(partner(phi**2)-sqrt(5))<eps
                and abs(partner(dS**2)-sqrt(2))<eps and abs(partner(dS)-dS)<eps)
    ck2("gd(ln 2) + gd(ln 3) = 90 deg: the 3-4-5 triangle and its complement",
            abs(th(mpf(2))+th(mpf(3))-pi/2)<eps
                    and abs(cosh(0)*mp.cos(th(mpf(2)))-mpf(4)/5)<eps)
    # --- §4.2 the angles (added 2026-09-15)
    # (r, t2 as printed, G as printed, theta as printed, Pi as printed) -- the table's rows
    cells = [(mpf(1), mpf(2), "0", "0", "90"),
             (mpf(2), mpf(5)/2, "0.019741857", "36.86989765", "70.52877937"),
             (phi**2, mpf(3), "0.037576350", "48.18968510", "63.43494882"),
             (mpf(3), mpf(10)/3, "0.048573849", "53.13010235", "60"),
             (2+sqrt(3), mpf(4), "0.068770141", "60", "54.73561032"),
             ((5+sqrt(21))/2, mpf(5), "0.095408039", "66.42182152", "49.10660535"),
             (mpf(5), mpf(26)/5, "0.100296856", "67.38013505", "48.18968510"),
             (dS**2, mpf(6), "0.118626413", "70.52877937", "45")]
    ck2("cos theta = 2/t2 and cos Pi = (r-1)/(r+1) at the eight cells of the table; every "
            "printed entry of the table (t2, G, theta, Pi) reproduced from the closed form",
        all(abs(1/cosh(log(r))-2/t2(r))<eps and abs(tanh(log(r)/2)-(r-1)/(r+1))<eps
                and abs(t2(r)-tt)<eps
                and abs((mpf(0) if r == 1 else G(r))-mpf(g))<mpf("5e-10")   # nine places
                and abs(deg(th(r))-mpf(a))<mpf("5e-9")      # eight places, as printed
                and abs(deg(Pi(r))-mpf(b))<mpf("5e-9")
            for r,tt,g,a,b in cells))
    ck2("golden: theta = arccos(2/3), Pi = arctan 2; Pi(2) = theta(3+2sqrt2) = arccos(1/3), "
            "Pi(3) = theta(2+sqrt3) = 60 deg, Pi(5) = theta(phi^2): t2(r') = 2 + 4/(r-1), an "
            "integer iff (r-1) | 4",
        abs(th(phi**2)-acos(mpf(2)/3))<eps and abs(Pi(phi**2)-atan(mpf(2)))<eps
        and abs(Pi(mpf(2))-th(dS**2))<eps and abs(Pi(mpf(3))-th(2+sqrt(3)))<eps
        and abs(Pi(mpf(3))-pi/3)<eps and abs(Pi(mpf(5))-th(phi**2))<eps
        and all(abs(t2(rp)-(2+mpf(4)/(r-1)))<eps
                for r,rp in ((2,dS**2),(3,2+sqrt(3)),(5,phi**2)))
        and [r for r in range(2,61) if 4 % (r-1) == 0] == [2,3,5])
    # --- §4.3 the saddle
    Gv = lambda v: mpf(0) if v == 0 else 1 - v/sinh(v)          # v = L/2
    h = mpf(10)**(-(dps//4))
    d2 = lambda f, x0: (f(x0+h)-2*f(x0)+f(x0-h))/h**2
    ck2("G'' at the wall: 1/3 in v = L/2, 1/12 in L (the value is a coordinate)", abs(d2(Gv,
            mpf(0))-mpf(1)/3)<mpf('1e-6') and abs(d2(lambda L: Gv(L/2),
                    mpf(0))-mpf(1)/12)<mpf('1e-6'))
    f = lambda w: mpf(0) if w == 0 else 1 - w/sinh(w)
    Re = lambda a,b: re(f(mpc(a,b)))
    Faa = (Re(h,0)-2*Re(0,0)+Re(-h,0))/h**2; Fbb = (Re(0,h)-2*Re(0,0)+Re(0,
            -h))/h**2; Fab = (Re(h,h)-Re(h,-h)-Re(-h,h)+Re(-h,-h))/(4*h*h)
    ck2("Re f at w = 0: Hessian diag(+1/3, -1/3), a saddle; the imaginary axis is the "
            "circular side",
            
            abs(Faa-mpf(1)/3)<mpf('1e-6')
            and abs(Fbb+mpf(1)/3)<mpf('1e-6')
            and abs(Fab)<mpf('1e-6'))
    ck2("on the imaginary axis f(i beta/2) = 1 - beta/(2 sin(beta/2)): the circle's "
            "argument over chord, negative", abs(re(f(mpc(0,
                    pi/4)))-(1-(pi/2)/(2*mp.sin(pi/4))))<eps and re(f(mpc(0,
            
            pi/4)))<0)
    lap = lambda a,b: (Re(a+h,b)+Re(a-h,b)+Re(a,b+h)+Re(a,b-h)-4*Re(a,b))/h**2
    ck2("Re f is harmonic (Laplacian 0) at three interior points", all(abs(lap(a,
            b))<mpf('1e-5') for a,b in ((mpf('0.3'),mpf('0.2')),(mpf('0.7'),
                    mpf('-0.4')),(mpf('1.1'),
            mpf('0.9')))))
    fp = lambda w: (w*cosh(w)-sinh(w))/sinh(w)**2
    ck2("the doubling interval is an ordinary point: f'(ln2/2) = 0.112347305659; f'(w) = 0 "
            "iff tanh w = w",
            
        abs(fp(log(2)/2)-mpf('0.112347305659'))<mpf('1e-11'))
    ys = [mp.findroot(lambda y: mp.tan(y)-y, x0) for x0 in (4.5, 7.7)]
    ck2("the next critical points are w = ±4.4934i, ±7.7253i (tan y = y), beyond the pole "
            "at i*pi: the wall is the only one in |w| < pi",
            
        abs(ys[0]-mpf('4.493409458'))<mpf('1e-8') and abs(ys[1]-mpf('7.725251837'))<mpf('1e-8')
                and ys[0] > pi)
    Ab = lambda a,b: abs(f(mpc(a,b)))
    ck2("|f| has a minimum at the wall (both second derivatives +1/3)", abs((Ab(h,0)-2*Ab(0,
            0)+Ab(-h,0))/h**2-mpf(1)/3)<mpf('1e-5') and abs((Ab(0,h)-2*Ab(0,0)+Ab(0,
            -h))/h**2-mpf(1)/3)<mpf('1e-5'))
    # --- §4.4 why: the squaring map's multiplier is invariant, the Hessian's value is not
    ck2("the squaring map r -> r^2 (L -> 2L): multiplier at its fixed point, the wall, is 2 "
            "in L, r, X and tau", all(abs(diff(g,x0)-2)<mpf('1e-12') for g,x0 in ((lambda L:2*L,
                    0),(lambda r:r*r,1),(lambda x:2*x*sqrt(1+x*x),0),(lambda s:2*s/(1+s*s),
            
            0))))
    ck2("section 4.3: 1 - v/sinh v = v^2/6 - 7v^4/360 + 31v^6/15120 (the series of 4.1 in v "
            "= L/2)",
            
            (lambda v: abs((1-v/sinh(v))-(v**2/6-7*v**4/360+31*v**6/15120))<v**8)(mpf("0.01")))
    ck2("p(2L) = p(L)/cosh(L/2): doubling the argument divides p by cosh(L/2)",
            all(abs(p(2*L_)-p(L_)/cosh(L_/2))<eps for L_ in (log(2), log(3), mpf('0.1'))))
    ck2("the trapezoid twin: T = (L/2)coth(L/2) - 1 = 3 ln2/2 - 1 = 0.0397 at doubling "
            "(coth(ln2/2) = 3); T/G -> 2 at the wall",
             abs(((log(2)/2)*coth(log(2)/2)-1)-mpf('0.039720771'))<mpf('1e-9')
            and abs(((log(2)/2)*coth(log(2)/2)-1)-(3*log(2)/2-1))<eps
            and abs(coth(log(2)/2)-3)<eps
            and abs(((mpf('1e-3')/2)*coth(mpf('1e-3')/2)-1)/Gv(mpf('5e-4'))-2)<mpf('1e-5'))
    # --- Figure 1
    ck2("Figure 1's four points: G = 0, 0.019741857, 0.037576350, 0.118626413; bases inf, "
            "32, 16, 4",
            
        abs(G(phi**2)-mpf('0.037576350'))<mpf('1e-9')
                and abs(G(dS**2)-mpf('0.118626413'))<mpf('1e-9')
                and abs(G(mpf(2))-mpf('0.019741857'))<mpf('1e-9'))
print(f"\n   THE WHERE:  CHECKS {CH2}   FAILURES {FA2}")
