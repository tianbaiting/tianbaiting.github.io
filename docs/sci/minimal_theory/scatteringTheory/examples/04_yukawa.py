"""Yukawa potential V(r) = -V0 * exp(-mu r) / (mu r), units hbar = 2m = 1.

Companion code for the markdown note. Four figures:
  1. Born amplitude |f_B(q)|^2 for several screening masses mu
  2. s-wave phase shift delta_0(k): Numerov-exact vs Born approximation
  3. Differential cross section dsigma/dOmega: Born vs exact partial-wave sum
  4. Bound-state threshold scan: delta_0(k->0) vs V0, Bargmann line
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "04_yukawa"
ASSETS.mkdir(parents=True, exist_ok=True)

V_yukawa = lambda r, V0, mu: -V0 * np.exp(-mu * r) / (mu * r)
f_born = lambda q, V0, mu: (V0 / mu) / (q ** 2 + mu ** 2)
delta0_born = lambda k, V0, mu: V0 / (4.0 * k * mu) * np.log1p(4.0 * k ** 2 / mu ** 2)


def numerov_phase(k, V0, mu, l=0, r_max=60.0, N=20000):
    """Solve u'' + [k^2 - V(r) - l(l+1)/r^2] u = 0 with u ~ r^{l+1} near 0,
    return delta_l from a two-point match to spherical Bessel asymptotes."""
    r = np.linspace(r_max / N, r_max, N)
    h = r[1] - r[0]
    f = k ** 2 - V_yukawa(r, V0, mu) - l * (l + 1) / r ** 2
    u = np.zeros(N)
    u[0] = r[0] ** (l + 1)
    u[1] = r[1] ** (l + 1) * (1.0 + h ** 2 * f[0] / 6.0)
    c = h ** 2 / 12.0
    for n in range(1, N - 1):
        u[n + 1] = (2 * u[n] * (1 - 5 * c * f[n])
                    - u[n - 1] * (1 + c * f[n - 1])) / (1 + c * f[n + 1])
    i1, i2 = N - 200, N - 100
    if l == 0:
        num = u[i1] * np.sin(k * r[i2]) - u[i2] * np.sin(k * r[i1])
        den = u[i2] * np.cos(k * r[i1]) - u[i1] * np.cos(k * r[i2])
        return np.arctan2(num, den)
    # spherical Bessel by upward recurrence: A = kr j_l, B = kr y_l (Riccati form)
    def riccati(L, x):
        S0, S1 = np.sin(x), np.sin(x) / x - np.cos(x)
        C0, C1 = -np.cos(x), -np.cos(x) / x - np.sin(x)
        for L_ in range(1, L):
            S0, S1 = S1, (2 * L_ + 1) / x * S1 - S0
            C0, C1 = C1, (2 * L_ + 1) / x * C1 - C0
        return (S1, C1) if L >= 1 else (S0, C0)
    A1, B1 = riccati(l, k * r[i1]); A2, B2 = riccati(l, k * r[i2])
    num = u[i1] * A2 - u[i2] * A1
    den = u[i2] * B1 - u[i1] * B2
    return np.arctan2(num, den)


def fig_born_amplitude():
    q = np.linspace(0.01, 8.0, 400)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for mu, c in zip([0.3, 1.0, 3.0], ["C0", "C1", "C2"]):
        ax.plot(q, np.abs(f_born(q, 1.0, mu)) ** 2, c, label=fr"$\mu={mu}$")
    ax.set(xlabel="q", ylabel=r"$|f^B(q)|^2$",
           title=r"Born amplitude squared, $V_0=1$")
    ax.set_yscale("log"); ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "born_amplitude.png", dpi=140)
    plt.close(fig)


def fig_phase_shift_compare():
    mu = 1.0
    k_arr = np.linspace(0.2, 4.0, 30)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for V0, c in zip([0.1, 0.5, 1.5], ["C0", "C1", "C2"]):
        d_num = np.array([numerov_phase(k, V0, mu) for k in k_arr])
        ax.plot(k_arr, d_num, c + "-", label=fr"exact, $V_0/\mu^2={V0}$")
        ax.plot(k_arr, delta0_born(k_arr, V0, mu), c + "--",
                label=fr"Born, $V_0/\mu^2={V0}$")
    ax.set(xlabel="k", ylabel=r"$\delta_0(k)$",
           title=r"s-wave phase shift, exact vs Born, $\mu=1$")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "phase_shift_compare.png", dpi=140)
    plt.close(fig)


def fig_cross_section():
    k, mu, V0, lmax = 1.5, 1.0, 1.0, 6
    th = np.linspace(0.01, np.pi - 0.01, 200)
    f_b = f_born(2 * k * np.sin(th / 2), V0, mu)
    f_exact = np.zeros_like(th, dtype=complex)
    P_prev, P_curr = np.ones_like(th), np.cos(th)
    for l in range(lmax + 1):
        d = numerov_phase(k, V0, mu, l=l, r_max=80.0, N=24000)
        if l == 0:   P = P_prev
        elif l == 1: P = P_curr
        else:
            P = ((2 * l - 1) * np.cos(th) * P_curr - (l - 1) * P_prev) / l
            P_prev, P_curr = P_curr, P
        f_exact += (2 * l + 1) * np.exp(1j * d) * np.sin(d) / k * P
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(th, np.abs(f_b) ** 2, "C0--", label="Born")
    ax.plot(th, np.abs(f_exact) ** 2, "C3-", label=f"exact (lmax={lmax})")
    ax.set(xlabel=r"$\theta$", ylabel=r"$d\sigma/d\Omega$",
           title=rf"Differential cross section, $k={k}$, $V_0={V0}$, $\mu={mu}$")
    ax.set_yscale("log"); ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "cross_section.png", dpi=140)
    plt.close(fig)


def fig_bound_state_threshold():
    mu, k = 1.0, 0.05
    V0_arr = np.linspace(0.05, 3.0, 60)
    d0 = np.array([numerov_phase(k, V, mu) for V in V0_arr])
    d0_unwrap = np.unwrap(2 * d0) / 2
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(V0_arr, d0_unwrap, "C0o-", ms=3, label=fr"$\delta_0(k\to 0)$, $k={k}$")
    ax.axvline(0.84, color="k", ls="--",
               label=r"Bargmann threshold $V_0/\mu^2 \approx 0.84$")
    ax.axhline(np.pi / 2, color="grey", ls=":", lw=0.8)
    ax.set(xlabel=r"$V_0$ (with $\mu=1$)", ylabel=r"$\delta_0$",
           title="First bound state appears as Levinson jump")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "bound_state_threshold.png", dpi=140)
    plt.close(fig)


def sanity_checks():
    d_w = numerov_phase(1.0, 0.01, 1.0); d_wb = delta0_born(1.0, 0.01, 1.0)
    assert abs(d_w - d_wb) < 1e-3, f"weak-coupling mismatch: {d_w} vs {d_wb}"
    d_s = numerov_phase(1.0, 2.0, 1.0); d_sb = delta0_born(1.0, 2.0, 1.0)
    assert abs(d_s - d_sb) > 0.1, f"strong-coupling too close: {d_s} vs {d_sb}"
    d_lo = numerov_phase(2.0, 1.0, 1.0)
    d_mid = numerov_phase(8.0, 1.0, 1.0, r_max=40.0, N=20000)
    d_hi = numerov_phase(40.0, 1.0, 1.0, r_max=20.0, N=40000)
    assert abs(d_lo) > abs(d_mid) > abs(d_hi), "phase shift not monotone"
    print("sanity checks passed: weak match, strong deviate, monotone decay")


if __name__ == "__main__":
    sanity_checks()
    fig_born_amplitude()
    fig_phase_shift_compare()
    fig_cross_section()
    fig_bound_state_threshold()
    print(f"figures written to {ASSETS}")
