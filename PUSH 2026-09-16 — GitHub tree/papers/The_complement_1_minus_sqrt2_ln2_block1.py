# ---------------------------------------------------------------------------
#  1 - sqrt(2)*ln(2)  --  every claim in this paper, checked.  G := 1 - sqrt(2)*ln(2)
# ---------------------------------------------------------------------------
from mpmath import mp, mpf, sqrt, log, exp, sinh, cosh, asinh, diff, findroot, pi, quad
from fractions import Fraction as Q
from math import comb, comb as fcomb, factorial as ffact

CH = FA = 0
def ck(name, cond):
    global CH, FA
    CH += 1
    if not cond: FA += 1
    print(f"  [{'ok' if cond else 'FAIL'}]  {name}")

def term(k):                                   # k >= 1, exact rational
    return Q((-1)**(k+1) * comb(2*k, k), 32**k * (2*k+1))

for DPS in (30, 60, 200, 500):
    mp.dps = DPS
    print(f"\n--- dps {DPS} " + "-"*52)
    L  = log(mpf(2))                           # the interval:  r = 2
    X  = (mpf(2) - 1) / (2*sqrt(mpf(2)))       # half-difference coordinate
    p_ln2 = sqrt(mpf(2)) * L                  # the ratio p at r = 2
    G = 1 - p_ln2
    eps = mpf(10)**(-(DPS - 8))

    # 1. the interval
    ck("sinh(ln2 / 2) = 1/(2 sqrt2)",            abs(X - sinh(L/2)) < eps)
    ck("X^2 = 1/8 exactly",                      abs(X**2 - mpf(1)/8) < eps)
    ck("arsinh(1/(2 sqrt2)) = ln2 / 2",         abs(asinh(X) - L/2) < eps)
    ck("p(ln2) = arsinh(X)/X = sqrt2 * ln2",    abs(asinh(X)/X - p_ln2) < eps)
    ck("GM/L_log on [1,2] equals L/(2 sinh(L/2))",
       abs(sqrt(mpf(2))/((mpf(2)-1)/L) - L/(2*sinh(L/2))) < eps)

    # 1b. the chain IS Hermite-Hadamard for exp on the log interval  (section 1)
    def HH(a, b):                              # the three H-H terms at f = exp
        la, lb = log(mpf(a)), log(mpf(b))
        return (exp((la+lb)/2),                            # f((alpha+beta)/2)
                quad(exp, [la, lb])/(lb-la),               # mean of f
                (exp(la)+exp(lb))/2)                       # (f(alpha)+f(beta))/2
    def means(a, b):
        a, b = mpf(a), mpf(b)
        return sqrt(a*b), (b-a)/log(b/a), (a+b)/2          # GM, L_log, AM
    ck("Hermite-Hadamard at f=exp on [ln a, ln b] gives GM, L_log, AM exactly",
       all(max(abs(h-m) for h, m in zip(HH(a,b), means(a,b))) < eps
           for a, b in ((1,2), (1,3), (2,7), ('0.5','11.3'))))
    ck("so p = GM/L_log is H-H's LEFT half, and p <= 1 is that inequality",
       all(mpf(0) < means(a,b)[0]/means(a,b)[1] <= 1 for a, b in ((1,2),(1,3),(2,7))))
    ck("ABSOLUTE Jensen gap at r = 2 = 1/ln2 - sqrt2 = 0.02848147851586835855",
       abs((mpf(2)-1)/L - sqrt(mpf(2)) - mpf('0.02848147851586835855')) < mpf('1e-20'))
    ck("and G is that gap NORMALISED:  (L_log - GM)/L_log = (1/ln2 - sqrt2)*ln2",
       abs(((mpf(2)-1)/L - sqrt(mpf(2))) / ((mpf(2)-1)/L) - G) < eps
       and abs((1/L - sqrt(mpf(2)))*L - G) < eps)
    ck("the two are DIFFERENT numbers -- the qualifier 'relative' is load-bearing",
       abs(((mpf(2)-1)/L - sqrt(mpf(2))) - G) > mpf('0.008'))
    ck("mean-ratio and midpoint are ONE setting: GM/L_log = midpt/exact, at every L",
       all(abs(means(1, exp(mpf(t)))[0]/means(1, exp(mpf(t)))[1]
               - mpf(t)*exp(mpf(t)/2)/(exp(mpf(t))-1)) < eps
           for t in ('0.6931471805599453', '1.5', '4')))

    # 2. positivity, before any evaluation
    ck("G > 0   (arsinh strictly concave, arsinh(0)=0)", G > 0)

    # 3. the series
    S = sum((term(k) for k in range(1, 4*DPS)), Q(0))
    ck("series -> G",                            abs(mpf(S.numerator)/S.denominator - G) < eps)
    ck("S1 = 1/48",                              term(1) == Q(1, 48))
    ck("S1 + S2 = 151/7680  (exact integers)",   term(1)+term(2) == Q(151, 7680))
    ck("bracket width = 3/2560 = 0.001171875",   term(1)-(term(1)+term(2)) == Q(3, 2560))

    # 4. the ratio lemma, and the two integer facts under it
    ck("central-binomial step  C(2k+2,k+1)/C(2k,k) = 2(2k+1)/(k+1)   [proved in 5]",
       all(Q(comb(2*k+2, k+1), comb(2*k, k)) == Q(2*(2*k+1), k+1) for k in range(1, 41)))
    ck("|t(k+1)|/|t(k)| = (2k+1)^2 / (16(k+1)(2k+3)), k=1..40",
       all(abs(term(k+1))/abs(term(k)) == Q((2*k+1)**2, 16*(k+1)*(2*k+3)) for k in range(1,
               41)))
    ck("16(k+1)(2k+3) - (2k+1)^2 = 28k^2+76k+47 > 0   -> decreasing",
       all(16*(k+1)*(2*k+3) - (2*k+1)**2 == 28*k*k+76*k+47 > 0 for k in range(0, 200)))
    ck("16(k+1)(2k+3) - 8(2k+1)^2 = 48k+40 > 0        -> ratio < 1/8",
       all(16*(k+1)*(2*k+3) - 8*(2*k+1)**2 == 48*k+40 > 0 for k in range(0, 200)))

    # 5. the enclosure
    P = [sum((term(i) for i in range(1, j+1)), Q(0)) for j in range(1, 13)]
    q = lambda f: mpf(f.numerator)/f.denominator
    ck("S(2j) < G < S(2j-1)  for j = 1..6",
       all(q(P[2*j-1]) < G < q(P[2*j-2]) for j in range(1, 7)))
    ck("bracket width at step j is exactly |t(2j)|,  j = 1..6",
       all(P[2*j-2]-P[2*j-1] == abs(term(2*j)) for j in range(1, 7)))
    ck("S7/S8 narrow the first bracket by exactly 18253611008/10725",
       (Q(3,2560)) / (P[6]-P[7]) == Q(18253611008, 10725))
    ck("the j=4 bracket AS PRINTED in section 5, numerators and denominators",
       P[7] == Q(8311000980567041, 420983760821944320)
       and P[6] == Q(3819393966191, 193466801848320)
       and P[6]-P[7] == Q(6435, 9345848836096))

    # 6. the function does not select the interval   (section 2)
    #    the sign facts below are PROVED in section 2; these are regression tests.
    Gf  = lambda t: 1 - t/(2*sinh(t/2))
    Gp  = lambda t: (t/2*cosh(t/2) - sinh(t/2)) / (2*sinh(t/2)**2)
    psi = lambda t: 4*sinh(t) - t*cosh(t) - 3*t
    pts = ('0.01','0.5','0.6931471805599453','3','10','29')
    ck("G'(L) = (u cosh u - sinh u)/(2 sinh^2 u),  u = L/2",
       all(abs(diff(Gf, mpf(t)) - Gp(mpf(t))) < eps for t in pts))
    ck("its numerator f(u) = u cosh u - sinh u > 0   [f(0)=0, f'= u sinh u > 0]",
       all(mpf(t)/2*cosh(mpf(t)/2) - sinh(mpf(t)/2) > 0 for t in pts))
    ck("so G'(L) > 0  -- no extremum anywhere on (0, inf)",
       all(Gp(mpf(t)) > 0 for t in pts))
    ck("G''(L) = psi(L)/(16 sinh^3(L/2)),  psi(L) = 4 sinh L - L cosh L - 3L",
       all(abs(diff(Gf, mpf(t), 2) - psi(mpf(t))/(16*sinh(mpf(t)/2)**3)) < eps for t in pts))
    if DPS >= 30:
        Ls = findroot(psi, mpf('3.2'))
        ck("the inflection is psi's unique positive root, L* = 3.2122305976",
           abs(Ls - mpf('3.212230597605534728')) < mpf('1e-15'))
        ck("and it is a zero of G'' itself  (r = e^L* = 24.834)",
           abs(diff(Gf, Ls, 2)) < eps and abs(exp(Ls) - mpf('24.8344200858')) < mpf('1e-9'))
        ck("psi's uniqueness cascade:  v1 < v2 < v3 < L*",
           (lambda v1, v2, v3: v1 < v2 < v3 < Ls)(
               findroot(lambda v: cosh(v) - v*sinh(v), mpf('1.2')),
               findroot(lambda v: diff(psi, v, 2), mpf('1.9')),
               findroot(lambda v: diff(psi, v), mpf('2.6'))))
        ck("L/2pi = 0.110317800076 IS the decay factor, not a distance:"
           "  7*(L/4pi)^2 = (7/4)*(L/2pi)^2",
           abs(L/(2*pi) - mpf('0.110317800076')) < mpf('1e-12')
           and abs(7*(L/(4*pi))**2 - (mpf(7)/4)*(L/(2*pi))**2) < eps)
        # the inflection is NOT coordinate-free -- section 2 states both and quotes
        # no distance to either.  Gr = G as a function of r.
        Gr = lambda t: 1 - log(t)/(2*sinh(log(t)/2))
        rs = findroot(lambda t: diff(Gr, t, 2), mpf('2.4'))
        ck("in r A root sits at 2.474062197, NOT e^L* = 24.834 -- uniqueness in r NOT proved",
           abs(rs - mpf('2.474062197326598')) < mpf('1e-12')
           and abs(rs - exp(Ls)) > 20)
        ck("no extremum in r either  (dG/dr > 0; L = ln r is strictly increasing)",
           all(diff(Gr, mpf(t)) > 0 for t in ('1.05','2','5','24.834','1000')))

    # 7. what other people printed
    ck("Fishman 1996 p.189:  100 * 1.511076 * G = 2.983144  (as printed)",
       abs(100*mpf('1.511076')*G - mpf('2.983144')) < mpf('1e-6'))
    ck("section 3: that product is 2.98314456..., so his 2.983144 is TRUNCATED (rounded "
            "gives ...45)",
            
       abs(100*mpf('1.511076')*G - mpf('2.98314456')) < mpf('5e-9')
       and mp.nstr(100*mpf('1.511076')*G, 7) == '2.983145')
    ck("section 3: the alpha reproducing 2.983144 exactly is 1.5110757...",
       abs(mpf('2.983144')/(100*G) - mpf('1.5110757')) < mpf('5e-8'))
    ck("section 2: at the r-inflection 2.474062197 the argument is L = 0.905861414",
       abs(log(mpf('2.474062197326598')) - mpf('0.905861414')) < mpf('5e-10'))
    G3 = 1 - log(mpf(3))/(2*sinh(log(mpf(3))/2))          # G(3); the integral on [0, ln 3] is 2
    ck("section 5.1: at r = 3 the absolute and relative midpoint errors are 0.0971476982 "
            "and 0.0485738491",
            
       abs(2*G3 - mpf('0.0971476982')) < mpf('5e-11')
               and abs(G3 - mpf('0.0485738491')) < mpf('5e-11'))
    ck("Hodgson-Kerckhoff's coefficient X/arcsinh(X) = 1/(sqrt2 ln2)",
       abs(X/asinh(X) - 1/p_ln2) < eps)
    ck("Bala A002162 clause 1:  2*arcsinh(sqrt2/4) = ln2",
       abs(2*asinh(sqrt(mpf(2))/4) - L) < eps)
    ck("Bala's argument sqrt2/4 is this interval's X",
       abs(sqrt(mpf(2))/4 - X) < eps)
    ck("chart domains: X = 1 exactly at r = 3 + 2*sqrt2 = (1+sqrt2)^2",
       abs((3+2*sqrt(mpf(2))-1)/(2*sqrt(3+2*sqrt(mpf(2)))) - 1) < eps)

    # --- 4, the base IS the coordinate -------------------------------------
    Xof   = lambda r: (r - 1)/(2*sqrt(r))
    baseof = lambda r: 16*r/(r - 1)**2
    ck("base = 4/X^2 exactly, at r = 2, 3, 5, 3+2sqrt2",
       all(abs(baseof(r) - 4/Xof(r)**2) < eps
           for r in (mpf(2), mpf(3), mpf(5), 3+2*sqrt(mpf(2)))))
    ck("integer ratios with integer base: n = 2, 3, 5 (bases 32, 12, 5); power of two only "
            "at n = 2",
            
       [n for n in range(2, 40) if 16 % (n-1)**2 == 0] == [2, 3, 5]
       and [int(baseof(mpf(n))) for n in (2, 3, 5)] == [32, 12, 5])
    ck("the domain bound r <= 3+2sqrt2 IS base = 4, not a separate fact",
       abs(baseof(3+2*sqrt(mpf(2))) - 4) < eps)
    # (checks on other ratios — r = phi^2, 2+sqrt3, the shared numerators — belong to the family
    #  and are not printed in this note.)
    ck("Bernoulli radius |L/2| < pi  <=>  r < e^(2pi) = 535.4916..., and 2 is inside",
       abs(exp(2*pi) - mpf('535.49165552476473')) < mpf('1e-10')
       and log(2) < 2*pi)
    ck("midpoint/exact = L*e^(L/2)/(e^L - 1) = p(L)  at r = 2, 3, 5, 10",
       all(abs(log(r)*exp(log(r)/2)/(exp(log(r))-1)
               - log(r)/(2*sinh(log(r)/2))) < eps for r in (2, 3, 5, 10)))
    Gm2, Am2 = sqrt(mpf(2)), mpf(3)/2                # Sandor / Niculescu, D&P Cor. 60, at r = 2
    lo2 = (mpf(2)**(mpf(1)/4) + mpf(2)**(mpf(3)/4))/2
    hi2 = (Am2 + Gm2)/2
    ck("section 5.1: Sandor's refinement at r=2 brackets G: 0.0148286 < G < 0.0294373",
       lo2 < 1/log(2) < hi2 and abs((1 - Gm2/lo2) - mpf('0.0148286')) < mpf('5e-8')
       and abs((1 - Gm2/hi2) - mpf('0.0294373')) < mpf('5e-8')
               and (1 - Gm2/lo2) < G < (1 - Gm2/hi2))
    ck("(ln2)^2/24 carries 101.403% of G",
       abs((L**2/24)/G - mpf('1.01403')) < mpf('1e-5'))
    ck("section 4.1: (ln2)^2/24 = 0.0200188756, as printed",
       abs(L**2/24 - mpf('0.0200188756')) < mpf('5e-11'))
    ck("section 5: the narrowing factor 18253611008/10725 = 1701968.39..., as printed",
       abs(mpf(18253611008)/10725 - mpf('1701968.39')) < mpf('5e-3'))

    # --- 4.1  the Bernoulli route ------------------------------------------
    def bern(m):                               # B_j exact, from the recurrence
        B = [Q(0)] * (m + 1); B[0] = Q(1)
        for n in range(1, m + 1):
            B[n] = -sum(Q(fcomb(n + 1, j)) * B[j] for j in range(n)) / Q(n + 1)
        return B
    # 24: the 8-term sum needs B_16, the sporadic-agreement check needs B_24
    B = bern(24)
    ck("Bernoulli recurrence gives B2,B4,B6,B8 = 1/6, -1/30, 1/42, -1/30",
       (B[2], B[4], B[6], B[8]) == (Q(1,6), Q(-1,30), Q(1,42), Q(-1,30)))

    def bcoef(n):                              # coefficient of L^(2n) in G(L)
        return Q(2**(2*n) - 2) * B[2*n] / Q(2**(2*n) * ffact(2*n))
    ck("G(L) coefficients are 1/24, -7/5760, 31/967680, -127/154828800",
       [bcoef(n) for n in (1,2,3,4)]
       == [Q(1,24), Q(-7,5760), Q(31,967680), Q(-127,154828800)])
    ck("section 4.1 table: num(c_6) = 1414477 and num(c_9) = 5749691557, as printed",
       abs(bcoef(6).numerator) == 1414477 and abs(bcoef(9).numerator) == 5749691557)

    def bmp(n):
        c = bcoef(n); return mpf(c.numerator)/mpf(c.denominator)
    ck("the Bernoulli series reproduces G from B_2n alone (8 terms)",
       abs(sum(bmp(n) * L**(2*n) for n in range(1, 9)) - G) < mpf('1e-16'))

    ck("c_n carries the factor 2^(2n-1)-1 ALWAYS; only the cancellation varies",
       all(bcoef(n) == Q(2**(2*n-1)-1) * B[2*n] / Q(2**(2*n-1) * ffact(2*n))
           for n in range(1, 11)))
    ck("num(c_n) = M * num(B_2n) / (cancellation vs (2n)!)  -- TWO mechanisms",
       all((2**(2*n-1)-1) * abs(B[2*n].numerator) % abs(bcoef(n).numerator) == 0
           and ffact(2*n) % ((2**(2*n-1)-1) * abs(B[2*n].numerator)
                             // abs(bcoef(n).numerator)) == 0
           for n in range(1, 13)))
    ck("agreement num(c_n)=M is SPORADIC: n = 1,2,3,4 and 7, not a threshold",
       [n for n in range(1, 13) if abs(bcoef(n).numerator) == 2**(2*n-1)-1]
       == [1, 2, 3, 4, 7])
    ck("at n=6 NOTHING cancels and the numerator is still not M:  2047*691",
       abs(bcoef(6).numerator) == 2047*691 and 2047*691 != 2047)
    ck("prefactor identity  (2^(2n+1)-1)/(2^(2n-1)-1) = 4 + 3/(2^(2n-1)-1)",
       all(Q(2**(2*n+1)-1, 2**(2*n-1)-1) == 4 + Q(3, 2**(2*n-1)-1) for n in range(1, 41)))
    ck("so it falls strictly from 7 at n=1 toward 4  -- max is 7, by inspection",
       Q(2**3 - 1, 2**1 - 1) == 7
       and all(Q(2**(2*n+3)-1, 2**(2*n+1)-1) < Q(2**(2*n+1)-1, 2**(2*n-1)-1) > 4
               for n in range(1, 41)))
    ck("ratio bound 7*(ln2/(4*pi))^2 = 0.0212975297739, and is < 1",
       abs(7*(L/(4*pi))**2 - mpf('0.0212975297739')) < mpf('1e-12')
       and 7*(L/(4*pi))**2 < 1)

    A = [sum(bmp(n) * L**(2*n) for n in range(1, j+1)) for j in range(1, 9)]
    Sb = [sum(mpf(term(k).numerator)/mpf(term(k).denominator)
              for k in range(1, j+1)) for j in range(1, 9)]
    ck("the Bernoulli bracket lies strictly inside the S_k bracket, orders 2-8",
       all(min(Sb[j-1], Sb[j-2]) < min(A[j-1], A[j-2])
           and max(A[j-1], A[j-2]) < max(Sb[j-1], Sb[j-2]) for j in range(2, 9)))
    ck("and the width factor at 8 terms (§5's j=4) exceeds 7e5",
       abs(Sb[7]-Sb[6]) / abs(A[7]-A[6]) > mpf('7e5'))

print("\n" + "="*64)
print(f"  CHECKS {CH}   FAILURES {FA}")
print("="*64)
