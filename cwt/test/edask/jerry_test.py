def main():
    import cdms2, vcs, genutil, cdutil
    import numpy as np
    import MV2
    phifsc = np.array([[10,50,30],[60,20,40],[30,50,20]])
    ps = np.array([[110,510,310],[200,300,100],[300,550,210]])
    ta = np.array([[102,503,304],[605,206,407],[330,540,250]])

    [pmsl, tsfc1, a1] = surface(phifsc, ps, ta)

    print pmsl
    print tsfc1
    print a1


def surface(phifsc, ps, ta):
    import numpy as np
    a = 0.190357143
    rd = 287.
    x = np.divide(phifsc, np.multiply(rd, ta))
    ax = np.multiply(a, x)
    ts = np.add(np.subtract(1.0, np.multiply(0.5, ax)), np.multiply(0.3333, np.multiply(ax, ax)))
    pmsl = np.multiply(ps, np.exp(np.multiply(x, ts)))
    t0 = np.add(ta, (np.multiply(.0065, (np.divide(phifsc, 9.8)))))

    mask0 = ((ta <= 290.5) & (t0 > 290.5))
    mask1 = ((ta > 290.5) & (t0 > 290.5))
    mask2 = (ta < 255)

    tsfc1 = ta.copy()
    tsfc1[mask1] = np.multiply(0.5, np.add(290.5, ta[mask1]))
    tsfc1[mask2] = np.multiply(0.5, np.add(255, ta[mask2]))

    a1 = np.zeros(phifsc.shape, phifsc.dtype)
    a1[mask0] = np.multiply(np.divide(rd, phifsc[mask0]), np.subtract(290.5, ta[mask0]))

    return [pmsl,tsfc1,a1]


main()
