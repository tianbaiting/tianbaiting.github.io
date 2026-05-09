"""Spin-1/2 + spin-0 polarization demo (Woods-Saxon + Thomas spin-orbit)
plus a schematic spin-1 + spin-0 tensor analyzing-power demonstration.

Units hbar=1, 2m=1.
  V_lj(r) = -V0 f(r) + V_SO <l.s> (1/r) df/dr,  f = 1/(1+exp((r-R)/a))
  <l.s> = l/2 (j=l+1/2), -(l+1)/2 (j=l-1/2)
Numerov solve u'' + [k^2 - V_lj - l(l+1)/r^2] u = 0; match Riccati-Bessel.
Build a, b from delta_l^pm, then sigma_0 and A_y.
Spin-1 + 0: schematic U,V,W,X(theta) -> iT_11, T_20, T_22 angular shapes.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ASSETS = Path(__file__).parent / "assets" / "10_polarization_demo"
ASSETS.mkdir(parents=True, exist_ok=True)
V0_, R_, A_ = 5.0, 2.0, 0.5
K0 = np.sqrt(2.0)


def riccati(l, x):
    j = [np.sin(x), np.sin(x) / x - np.cos(x)]
    n = [-np.cos(x), -np.cos(x) / x - np.sin(x)]
    for ell in range(1, l):
        j.append((2 * ell + 1) / x * j[ell] - j[ell - 1])
        n.append((2 * ell + 1) / x * n[ell] - n[ell - 1])
    if l == 0:
        return j[0], n[0]
    return j[l], n[l]


def ws_f(r): return 1.0 / (1.0 + np.exp((r - R_) / A_))


def V_lj(r, l, ls_eig, V_SO):
    rs = np.where(r > 1e-6, r, 1e-6)
    f = ws_f(r)
    return -V0_ * f + V_SO * ls_eig * (-f * (1 - f) / A_) / rs


def numerov_phase(l, ls_eig, k, V_SO, r_max=20.0, N=8000):
    h = r_max / N
    r = np.linspace(0.0, r_max, N + 1)
    rs = np.where(r > 1e-6, r, 1e-6)
    f = k * k - V_lj(r, l, ls_eig, V_SO) - l * (l + 1) / rs ** 2
    u = np.zeros(N + 1)
    u[1] = (k * h) ** (l + 1) if l > 0 else h
    h2 = h * h / 12
    for n in range(1, N):
        u[n + 1] = (2 * u[n] * (1 - 5 * h2 * f[n])
                    - u[n - 1] * (1 + h2 * f[n - 1])) / (1 + h2 * f[n + 1])
    n2 = N; n1 = N - max(20, int(np.pi / (k * h)))
    j1, nn1 = riccati(l, k * r[n1]); j2, nn2 = riccati(l, k * r[n2])
    return np.arctan2(u[n1] * j2 - u[n2] * j1, u[n1] * nn2 - u[n2] * nn1)


def legendre_table(L_max, x):
    P = [np.ones_like(x), x.copy()]
    for ell in range(1, L_max):
        P.append(((2 * ell + 1) * x * P[ell] - ell * P[ell - 1]) / (ell + 1))
    P1 = [np.zeros_like(x), -np.sqrt(np.maximum(1 - x * x, 0.0))]
    for ell in range(1, L_max):
        P1.append(((2 * ell + 1) * x * P1[ell] - (ell + 1) * P1[ell - 1]) / ell)
    return P, P1


def amplitudes(theta, k, dp, dm):
    L_max = len(dp) - 1
    P, P1 = legendre_table(L_max, np.cos(theta))
    a = np.zeros_like(theta, dtype=complex); b = np.zeros_like(theta, dtype=complex)
    for ell in range(L_max + 1):
        ep = np.exp(2j * dp[ell]) - 1
        if ell == 0:
            a += ep * P[ell]
        else:
            em = np.exp(2j * dm[ell]) - 1
            a += ((ell + 1) * ep + ell * em) * P[ell]
            b += (np.exp(2j * dp[ell]) - np.exp(2j * dm[ell])) * P1[ell]
    return a / (2j * k), b / (2j * k)


def all_phase_shifts(k, V_SO, L_max=5):
    dp = np.zeros(L_max + 1); dm = np.zeros(L_max + 1)
    for ell in range(L_max + 1):
        dp[ell] = numerov_phase(ell, ell / 2.0, k, V_SO)
        if ell >= 1:
            dm[ell] = numerov_phase(ell, -(ell + 1) / 2.0, k, V_SO)
    return dp, dm


VSO_LIST = [0.0, 2.0, 5.0, 8.0]


def fig_phase_shifts():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for V_SO in VSO_LIST:
        dp, dm = all_phase_shifts(K0, V_SO)
        ax[0].plot(range(6), dp, "o-", label=f"$V_{{SO}}={V_SO}$")
        ax[1].plot(range(1, 6), dm[1:], "s-", label=f"$V_{{SO}}={V_SO}$")
    for a, t in zip(ax, [r"$\delta_l^+\ (j=l+1/2)$", r"$\delta_l^-\ (j=l-1/2)$"]):
        a.set_xlabel("$l$"); a.set_ylabel("phase shift (rad)")
        a.set_title(t); a.grid(alpha=0.3); a.legend()
    fig.suptitle(r"Woods-Saxon + Thomas SO, $V_0=5,\ R=2,\ a=0.5,\ k=\sqrt{2}$")
    fig.tight_layout(); fig.savefig(ASSETS / "phase_shifts.png", dpi=140); plt.close(fig)


def fig_Ay_angular():
    theta = np.linspace(0.05, np.pi - 0.05, 240)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for V_SO in VSO_LIST:
        dp, dm = all_phase_shifts(K0, V_SO)
        a, b = amplitudes(theta, K0, dp, dm)
        sig0 = np.abs(a) ** 2 + np.abs(b) ** 2
        ax[0].plot(np.degrees(theta), 2 * (np.conj(a) * b).real / sig0, label=f"$V_{{SO}}={V_SO}$")
        ax[1].plot(np.degrees(theta), sig0, label=f"$V_{{SO}}={V_SO}$")
    ax[0].set_ylabel(r"$A_y(\theta)$"); ax[0].set_title("analyzing power")
    ax[1].set_ylabel(r"$\sigma_0=|a|^2+|b|^2$"); ax[1].set_title("unpolarized cross section")
    for a in ax: a.set_xlabel(r"$\theta$ (deg)"); a.grid(alpha=0.3); a.legend()
    fig.tight_layout(); fig.savefig(ASSETS / "Ay_angular.png", dpi=140); plt.close(fig)


def fig_Ay_vs_VSO():
    th = np.array([np.pi / 2]); Vs = np.linspace(0.0, 10.0, 21); Ay = []
    for V_SO in Vs:
        dp, dm = all_phase_shifts(K0, V_SO)
        a, b = amplitudes(th, K0, dp, dm)
        Ay.append((2 * (np.conj(a) * b).real / (np.abs(a) ** 2 + np.abs(b) ** 2))[0])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(Vs, Ay, "o-"); ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel(r"$V_{SO}$"); ax.set_ylabel(r"$A_y(\theta=90^\circ)$")
    ax.set_title(r"$A_y(90^\circ)$ vs spin-orbit strength"); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "Ay_vs_VSO.png", dpi=140); plt.close(fig)


def spin1_amplitudes(theta):
    """Schematic U,V,W,X mimicking low partial-wave shapes (not LS-derived)."""
    c, s = np.cos(theta), np.sin(theta)
    U = 1.0 + 0.4 * c + 0.3j * s
    V = (0.25 + 0.15j) * s
    W = (0.20 + 0.10j) * (1 - c ** 2)
    X = (0.15 - 0.05j) * s * c
    return U, V, W, X


def fig_deuteron_observables():
    th = np.linspace(0.05, np.pi - 0.05, 240)
    U, V, W, X = spin1_amplitudes(th)
    sig0 = np.abs(U) ** 2 + 2 * (np.abs(V) ** 2 + np.abs(W) ** 2 + np.abs(X) ** 2)
    iT11 = np.sqrt(3.0) * (U * np.conj(V)).imag / sig0
    T20 = (-np.abs(V) ** 2 + np.abs(W) ** 2 - np.abs(X) ** 2) / (np.sqrt(2.0) * sig0)
    T22 = np.sqrt(3.0) * (U * np.conj(W)).real / sig0
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    ax[0].plot(np.degrees(th), sig0, "k-")
    ax[0].set_xlabel(r"$\theta$ (deg)"); ax[0].set_ylabel(r"$\sigma_0$")
    ax[0].set_title("schematic unpolarized cross section"); ax[0].grid(alpha=0.3)
    ax[1].plot(np.degrees(th), iT11, label=r"$iT_{11}$")
    ax[1].plot(np.degrees(th), T20, label=r"$T_{20}$")
    ax[1].plot(np.degrees(th), T22, label=r"$T_{22}$")
    ax[1].axhline(0, color="k", lw=0.5)
    ax[1].set_xlabel(r"$\theta$ (deg)"); ax[1].set_ylabel("analyzing power")
    ax[1].set_title("schematic spin-1 + 0 tensor analyzing powers")
    ax[1].grid(alpha=0.3); ax[1].legend()
    fig.tight_layout(); fig.savefig(ASSETS / "deuteron_observables.png", dpi=140); plt.close(fig)


def sanity_checks():
    dp, dm = all_phase_shifts(K0, 0.0, L_max=4)
    for ell in range(1, 5):
        assert abs(dp[ell] - dm[ell]) < 1e-6, f"l={ell} not degenerate"
    th = np.linspace(0.1, np.pi - 0.1, 30)
    a, b = amplitudes(th, K0, dp, dm)
    assert np.max(np.abs(b)) < 1e-10, "b not zero with V_SO=0"
    Ay = 2 * (np.conj(a) * b).real / (np.abs(a) ** 2 + np.abs(b) ** 2)
    assert np.max(np.abs(Ay)) < 1e-10, "A_y not zero with V_SO=0"
    for V_SO in [2.0, 5.0, 8.0]:
        dp2, dm2 = all_phase_shifts(K0, V_SO, L_max=4)
        a2, b2 = amplitudes(th, K0, dp2, dm2)
        assert np.all(np.abs(a2) ** 2 + np.abs(b2) ** 2 > 0)
    dp, dm = all_phase_shifts(K0, 5.0)
    a, b = amplitudes(np.array([np.pi / 2]), K0, dp, dm)
    Ay90 = (2 * (np.conj(a) * b).real / (np.abs(a) ** 2 + np.abs(b) ** 2))[0]
    print(f"sanity passed.  A_y(90 deg, V_SO=5) = {Ay90:+.4f}")


if __name__ == "__main__":
    sanity_checks()
    fig_phase_shifts(); fig_Ay_angular(); fig_Ay_vs_VSO(); fig_deuteron_observables()
    print(f"figures written to {ASSETS}")
