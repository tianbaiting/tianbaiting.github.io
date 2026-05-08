"""Rank-1 separable Yamaguchi potential. Units: hbar=1, 2mu=1, E=k^2.

V(p,p')=lam*g(p)g(p'), g(p)=1/(p^2+beta^2). T=tau(E)g(p)g(p') with
tau=lam/(1-lam*I), I(E)=-1/[8*pi*beta*(beta-i*k)^2]. ERE:
k cot(delta_0) = -4*pi*(beta^2+k^2)^2/lam + (k^2-beta^2)/(2*beta).
Bound state (lam<-8*pi*beta^3): (beta+kappa)^2 = -lam/(8*pi*beta).
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ASSETS = Path(__file__).parent / "assets" / "separable_rank1"
ASSETS.mkdir(parents=True, exist_ok=True)

g = lambda p, b: 1.0 / (p ** 2 + b ** 2)


def I_E(E, beta):
    k = np.sqrt(E + 0j)
    if np.imag(k) < 0:
        k = -k
    return -1.0 / (8 * np.pi * beta * (beta - 1j * k) ** 2)


def tau(E, lam, beta):
    return lam / (1.0 - lam * I_E(E, beta))


def kcot(k, lam, beta):
    return -4 * np.pi * (beta ** 2 + k ** 2) ** 2 / lam + (k ** 2 - beta ** 2) / (2 * beta)


def a_re(lam, beta):
    return 1.0 / (4 * np.pi * beta ** 4 / lam + beta / 2.0), 1.0 / beta - 16 * np.pi * beta ** 2 / lam


def kappa_bound(lam, beta):
    rhs = -lam / (8 * np.pi * beta)
    if rhs <= 0:
        return np.nan
    kap = np.sqrt(rhs) - beta
    return kap if kap > 0 else np.nan


def numerical_LS(E, lam, beta, N=128, qmax=30.0):
    x, w = np.polynomial.legendre.leggauss(N)
    q = 0.5 * qmax * (x + 1); wq = 0.5 * qmax * w; G = g(q, beta)
    if E < 0:
        I_num = np.sum(wq * (q ** 2 / (2 * np.pi ** 2)) * G ** 2 / (E - q ** 2))
        return lam / (1 - lam * I_num), I_num
    k0 = np.sqrt(E); g0 = g(k0, beta)
    pv_int = np.sum(wq * (q ** 2 * G ** 2 - k0 ** 2 * g0 ** 2) / (E - q ** 2))
    pv_tail = -(k0 * g0 ** 2 / 2.0) * np.log(abs((qmax - k0) / (qmax + k0)))
    re = (pv_int + pv_tail) / (2 * np.pi ** 2)
    im = -(k0 * g0 ** 2) / (4 * np.pi)
    I_num = re + 1j * im
    return lam / (1 - lam * I_num), I_num


def fig_tau_vs_E(lam=-30.0, beta=1.0):
    E = np.linspace(-3.0, 8.0, 2000)
    tt = np.array([tau(e, lam, beta) for e in E])
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(E, np.abs(tt), label=r"$|\tau(E)|$")
    kap = kappa_bound(lam, beta)
    if not np.isnan(kap):
        ax.axvline(-kap ** 2, color="r", ls="--", lw=1,
                   label=fr"bound state $E_b={-kap**2:.3f}$")
    ax.axvline(0, color="k", lw=0.5); ax.set_yscale("log")
    ax.set_xlabel("E"); ax.set_ylabel(r"$|\tau(E)|$")
    ax.set_title(fr"Yamaguchi rank-1: $\lambda={lam}$, $\beta={beta}$")
    ax.grid(alpha=0.3); ax.legend()
    fig.tight_layout(); fig.savefig(ASSETS / "tau_vs_E.png", dpi=140); plt.close(fig)


def fig_phase_shift():
    k = np.linspace(0.05, 3.0, 300)
    fig, ax = plt.subplots(figsize=(7, 4))
    for lam, beta, c in [(-30.0, 1.0, "C0"), (-10.0, 1.0, "C1"), (-50.0, 1.5, "C2")]:
        ax.plot(k, np.arctan2(k, kcot(k, lam, beta)), c,
                label=fr"analytic $\lambda={lam},\beta={beta}$")
        ks = k[::40]; d_num = []
        for kk in ks:
            tn, _ = numerical_LS(kk ** 2, lam, beta)
            T0 = tn / (kk ** 2 + beta ** 2) ** 2
            d_num.append(np.arctan2(kk, -4 * np.pi * (1 / T0).real))
        ax.plot(ks, d_num, c + "o", ms=5, mfc="none", label="numerical LS")
    ax.set_xlabel("k"); ax.set_ylabel(r"$\delta_0(k)$ [rad]")
    ax.set_title("s-wave phase shift: closed form vs numerical LS")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(ASSETS / "phase_shift.png", dpi=140); plt.close(fig)


def fig_effective_range():
    k = np.linspace(0.05, 1.5, 200)
    fig, ax = plt.subplots(figsize=(7, 4))
    for lam, beta, c in [(-30.0, 1.0, "C0"), (-50.0, 1.5, "C2")]:
        a, re = a_re(lam, beta)
        ax.plot(k ** 2, kcot(k, lam, beta), c, label=fr"exact $\lambda={lam},\beta={beta}$")
        ax.plot(k ** 2, -1 / a + 0.5 * re * k ** 2, c + "--",
                label=fr"ERE: $a={a:.3f}, r_e={re:.3f}$")
    ax.set_xlabel(r"$k^2$"); ax.set_ylabel(r"$k\cot\delta_0$")
    ax.set_title("Effective range expansion (truncates exactly at $k^4$)")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(ASSETS / "effective_range.png", dpi=140); plt.close(fig)


def fig_off_shell(lam=-30.0, beta=1.0, k0=0.8):
    p = np.linspace(0.0, 6.0, 400); E = k0 ** 2
    T_pp = tau(E, lam, beta) * g(p, beta) * g(k0, beta)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(p, np.real(T_pp), label=r"Re $T(p,k_0;E)$")
    ax.plot(p, np.imag(T_pp), label=r"Im $T(p,k_0;E)$")
    ax.axvline(k0, color="grey", ls=":", lw=1, label=fr"on-shell $p=k_0={k0}$")
    ax.set_xlabel("p"); ax.set_ylabel("T")
    ax.set_title(r"Off-shell $T$: separable factorisation $T(p,k_0)\propto g(p)$")
    ax.grid(alpha=0.3); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(ASSETS / "off_shell.png", dpi=140); plt.close(fig)


def sanity_checks():
    lam, beta = -30.0, 1.0
    t_an = tau(1.0, lam, beta); t_num, _ = numerical_LS(1.0, lam, beta, N=128, qmax=40.0)
    assert abs(t_an - t_num) / abs(t_an) < 1e-4, (t_an, t_num)
    kap = kappa_bound(lam, beta); Eb = -kap ** 2
    assert abs(1.0 - lam * I_E(Eb, beta)) < 1e-10
    k = np.linspace(0.01, 0.4, 30); coef = np.polyfit(k ** 2, kcot(k, lam, beta), 2)
    a_an, re_an = a_re(lam, beta)
    assert abs(coef[2] - (-1 / a_an)) < 1e-8 and abs(coef[1] - re_an / 2) < 1e-8
    print(f"sanity: tau_an={t_an:.6f}, tau_num={t_num:.6f}; "
          f"kappa={kap:.4f}, E_b={Eb:.4f}; a={a_an:.4f}, r_e={re_an:.4f}")


if __name__ == "__main__":
    sanity_checks()
    fig_tau_vs_E(); fig_phase_shift(); fig_effective_range(); fig_off_shell()
    print(f"figures written to {ASSETS}")
