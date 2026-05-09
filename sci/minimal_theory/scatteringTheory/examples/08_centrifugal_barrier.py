"""3D attractive square well V(r)=-V0 theta(R-r), l=2 partial wave.

Centrifugal tail 6/r^2 outside the well creates a shape resonance.
Units hbar=1, 2mu=1, E=k^2. Riccati-Bessel:
  jhat_2(x) = (3/x^2 - 1) sin x - (3/x) cos x      (regular, ~ x^3/15)
  nhat_2(x) = -(3/x^2 - 1) cos x - (3/x) sin x     (irregular)
Match log-derivative at r=R: beta = K jhat'(KR)/jhat(KR), then
  tan delta_2 = (k jhat'(kR) - beta jhat(kR)) / (k nhat'(kR) - beta nhat(kR)).
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "08_centrifugal_barrier"
ASSETS.mkdir(parents=True, exist_ok=True)
L, LL1, V0_LIST = 2, 6, [12.0, 15.0, 18.0]

def jhat(x):  # series for |x|<0.4 to avoid 3/x^2 cancellation
    x = np.asarray(x, dtype=complex); o = np.empty_like(x); m = np.abs(x) > 0.4
    xb = x[m]; o[m] = (3 / xb ** 2 - 1) * np.sin(xb) - (3 / xb) * np.cos(xb)
    z = x[~m]; o[~m] = z ** 3 / 15 - z ** 5 / 210 + z ** 7 / 7560
    return o

def jhat_p(x):  # = jhat_1 - 2 jhat_2/x; jhat_1 = sin x/x - cos x
    x = np.asarray(x, dtype=complex); o = np.empty_like(x); m = np.abs(x) > 0.4
    xb = x[m]; o[m] = np.sin(xb) / xb - np.cos(xb) - 2 * jhat(xb) / xb
    z = x[~m]; o[~m] = z ** 2 / 5 - z ** 4 / 42 + z ** 6 / 1080
    return o

def nhat(x):
    x = np.asarray(x, dtype=complex)
    return -(3 / x ** 2 - 1) * np.cos(x) - (3 / x) * np.sin(x)

def nhat_p(x):
    x = np.asarray(x, dtype=complex)
    return -np.cos(x) / x - np.sin(x) - 2 * nhat(x) / x

def _D(k, V0, R):  # tan delta = num/den; S-pole at num + i den = 0
    K = np.sqrt(k * k + V0 + 0j); b = K * jhat_p(K * R) / jhat(K * R)
    return k * jhat_p(k * R) - b * jhat(k * R), k * nhat_p(k * R) - b * nhat(k * R)

def tan_delta2(k, V0, R=1.0):
    n, d = _D(np.asarray(k, dtype=complex), V0, R); return (n / d).real

def delta2(k, V0, R=1.0):  # smooth branch via atan2(num, den) instead of arctan(tan)
    n, d = _D(np.asarray(k, dtype=complex), V0, R)
    return np.unwrap(np.arctan2(n.real, d.real))

def cross_section_l2(k, V0, R=1.0):
    return 4 * np.pi * (2 * L + 1) * np.sin(delta2(k, V0, R)) ** 2 / (k * k)

def newton_pole(k0, V0, R=1.0, tol=1e-11, eps=1e-6):
    k = complex(k0)
    for _ in range(120):
        n, d = _D(k, V0, R); npp, dpp = _D(k + eps, V0, R); nm, dm = _D(k - eps, V0, R)
        f = n + 1j * d; df = ((npp - nm) + 1j * (dpp - dm)) / (2 * eps)
        dk = f / df; k -= dk
        if abs(dk) < tol: break
    return k

def numerov_delta2(k, V0, R=1.0, r_max=30.0, N=12000):
    h = r_max / N; r = np.linspace(0, r_max, N + 1)
    Vloc = np.where(r < R, -V0, 0.0); Vloc[0] = -V0
    f = k * k - Vloc - LL1 / np.where(r > 1e-12, r, 1e-12) ** 2
    u = np.zeros(N + 1); u[1] = (k * h) ** 3; h2 = h * h / 12
    for n in range(1, N):
        u[n + 1] = (2 * u[n] * (1 - 5 * h2 * f[n]) - u[n - 1] * (1 + h2 * f[n - 1])) / (1 + h2 * f[n + 1])
    n2 = N; n1 = N - max(20, int(np.pi / (k * h)))
    j1, j2 = jhat(k * r[n1]).real, jhat(k * r[n2]).real
    nn1, nn2 = nhat(k * r[n1]).real, nhat(k * r[n2]).real
    return np.arctan2(u[n1] * j2 - u[n2] * j1, u[n1] * nn2 - u[n2] * nn1)

def bw_fit(V0, R=1.0):
    k = np.linspace(0.3, 3.0, 8000); E = k * k
    dd = np.gradient(delta2(k, V0, R), E); i = int(np.argmax(dd))
    return (float(E[i]), float(2 / dd[i])) if dd[i] > 0 else (None, None)

def _save(fig, name):
    fig.tight_layout(); fig.savefig(ASSETS / name, dpi=140); plt.close(fig)

def fig_effective_potential():
    r = np.linspace(0.05, 3.0, 800); fig, ax = plt.subplots(figsize=(7, 4.4))
    for V0, c in zip(V0_LIST, ["C0", "C1", "C2"]):
        ax.plot(r, np.where(r < 1, -V0, 0) + LL1 / r ** 2, c, lw=1.6, label=rf"$V_0={V0:g}$")
        kp = newton_pole(1.5 - 0.3j, V0); ax.axhline(kp.real ** 2 - kp.imag ** 2, color=c, lw=0.6, ls="--", alpha=0.7)
    ax.axhline(0, color="k", lw=0.4); ax.axvline(1, color="gray", lw=0.4, ls=":")
    ax.set(xlabel="r", ylabel=r"$V_\mathrm{eff}(r)$", ylim=(-19, 25),
           title=r"d-wave effective potential; dashed = $E_R$ from pole")
    ax.legend(); ax.grid(alpha=0.3); _save(fig, "effective_potential.png")

def fig_phase_shift():
    k = np.linspace(0.1, 3.5, 500); fig, ax = plt.subplots(1, 2, figsize=(11, 4.4))
    for V0, c in zip(V0_LIST, ["C0", "C1", "C2"]):
        da = delta2(k, V0); dn = np.unwrap([numerov_delta2(ki, V0) for ki in k])
        dn += np.round((da[0] - dn[0]) / np.pi) * np.pi
        ax[0].plot(k, da / np.pi, c, lw=1.6, label=rf"analytic $V_0={V0:g}$")
        ax[0].plot(k[::20], dn[::20] / np.pi, c + "o", ms=3.5, mfc="none")
    ax[0].set(xlabel="k", ylabel=r"$\delta_2/\pi$", title=r"$\delta_2$: closed form vs Numerov")
    ax[0].legend(fontsize=9); ax[0].grid(alpha=0.3)
    k2 = np.linspace(0.7, 1.5, 600); kp = newton_pole(1.1 - 0.05j, 18.0)
    ER = kp.real ** 2 - kp.imag ** 2
    ax[1].plot(k2 ** 2, delta2(k2, 18) / np.pi, "C2", lw=1.6)
    ax[1].axvline(ER, color="r", lw=0.6, ls="--", label=rf"$E_R={ER:.3f}$")
    ax[1].axhline(0.5, color="gray", lw=0.4, ls=":")
    ax[1].set(xlabel=r"$E=k^2$", ylabel=r"$\delta_2/\pi$", title=r"resonance jump near $V_0=18$")
    ax[1].legend(); ax[1].grid(alpha=0.3); _save(fig, "phase_shift.png")

def fig_cross_section():
    k = np.linspace(0.1, 3.0, 3000); fig, ax = plt.subplots(figsize=(7.2, 4.6))
    for V0, c in zip(V0_LIST, ["C0", "C1", "C2"]):
        ax.plot(k * k, cross_section_l2(k, V0), c, lw=1.5, label=rf"$V_0={V0:g}$")
        kp = newton_pole(1.5 - 0.4j, V0); ax.axvline(kp.real ** 2 - kp.imag ** 2, color=c, lw=0.4, ls=":", alpha=0.7)
    ax.set(xlabel=r"$E=k^2$", ylabel=r"$\sigma_2$", yscale="log",
           title=r"d-wave cross section $\sigma_2=20\pi\sin^2\delta_2/k^2$")
    ax.legend(); ax.grid(alpha=0.3, which="both"); _save(fig, "cross_section.png")

def fig_pole_trajectory():
    Vs = np.concatenate([np.linspace(8.0, 19.5, 14), np.linspace(20.5, 26.0, 8)])
    poles, kinds, sr, sb = [], [], 2.0 - 0.6j, 0.5j
    for V in Vs[:14]: sr = newton_pole(sr, V); poles.append(sr); kinds.append("r")
    for V in Vs[14:]: sb = newton_pole(sb, V); poles.append(sb); kinds.append("b")
    poles = np.array(poles); m = np.array([k == "r" for k in kinds])
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    sc = ax.scatter(poles[m].real, poles[m].imag, c=Vs[m], cmap="viridis", s=42, label="resonance")
    ax.scatter(poles[~m].real, poles[~m].imag, c=Vs[~m], cmap="viridis", s=42, marker="^", label="bound")
    for mm in (m, ~m): ax.plot(poles[mm].real, poles[mm].imag, "k-", lw=0.6, alpha=0.5)
    fig.colorbar(sc, ax=ax, label=r"$V_0$"); ax.axhline(0, color="k", lw=0.5); ax.axvline(0, color="k", lw=0.5)
    ax.set(xlabel=r"$\mathrm{Re}\,k$", ylabel=r"$\mathrm{Im}\,k$",
           title=r"pole trajectory: resonance ($\mathrm{Im}\,k<0$) and bound state ($\mathrm{Im}\,k>0$)")
    ax.legend(loc="upper right"); ax.grid(alpha=0.3); _save(fig, "pole_trajectory.png")
    return Vs, poles, kinds

def sanity_checks():
    for V0 in [4.0, 8.0, 12.0]:
        ta = float(tan_delta2(np.array([1.0]), V0)[0]); tn = float(np.tan(numerov_delta2(1.0, V0)))
        assert abs(ta - tn) / (1 + abs(ta)) < 5e-3, (V0, ta, tn)
    kp = newton_pole(1.1 - 0.05j, 18.0); ERp = kp.real ** 2 - kp.imag ** 2
    ERb, Gb = bw_fit(18.0); assert abs(ERp - ERb) < 1e-2
    kpd = newton_pole(1.5j, 25.0); assert kpd.imag > 0.5
    print(f"sanity ok | V0=18 pole k={kp:.5f} E_R={ERp:.4f} Gamma={abs(4*kp.real*kp.imag):.4f}; "
          f"BW E_R={ERb:.4f} Gamma={Gb:.4f} | V0=25 bound k={kpd:.4f}")

if __name__ == "__main__":
    sanity_checks()
    fig_effective_potential(); fig_phase_shift(); fig_cross_section()
    Vs, poles, kinds = fig_pole_trajectory()
    for V, kp, kd in zip(Vs, poles, kinds):
        print(f"  V0={V:5.2f}[{kd}] k={kp:+.4f} E={kp.real**2-kp.imag**2:+.4f} G={abs(4*kp.real*kp.imag):.4f}")
    print(f"figures -> {ASSETS}")
