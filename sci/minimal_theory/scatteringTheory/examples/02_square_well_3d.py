"""3D attractive square well V(r) = -V0 * theta(R-r), s-wave only.

Units: hbar = 1, 2 mu = 1, so E = k^2 and inside the well K = sqrt(k^2 + V0).
The matching condition at r=R gives k cot(kR + delta0) = K cot(KR), from
which delta0(k), the s-wave cross section, the scattering length a, and the
effective range r_e all follow analytically.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "02_square_well_3d"
ASSETS.mkdir(parents=True, exist_ok=True)


def bound_state_count(V0, R=1.0):
    """Number of s-wave bound states: K0R crosses (n - 1/2) pi for n = 1, 2, ..."""
    return int(np.floor(np.sqrt(V0) * R / np.pi + 0.5))


def delta0(k_arr, V0, R=1.0):
    """s-wave phase shift, unwrapped and anchored to Levinson value n0*pi at k->0.

    Use tan(kR + delta0) = (k/K) tan(KR), i.e. delta0 = -kR + arctan(...) + n pi.
    """
    K = np.sqrt(k_arr * k_arr + V0)
    # arctan2(k sin(KR), K cos(KR)) avoids the tan(KR) divergence at KR=pi/2 etc.
    raw = np.arctan2(k_arr * np.sin(K * R), K * np.cos(K * R)) - k_arr * R
    d = np.unwrap(raw)
    shift = np.round((bound_state_count(V0, R) * np.pi - d[0]) / np.pi) * np.pi
    return d + shift


def cross_section(k, V0, R=1.0):
    d = delta0(k, V0, R)
    return 4.0 * np.pi * np.sin(d) ** 2 / (k * k)


def scattering_length(V0, R=1.0):
    K0 = np.sqrt(V0)
    return R * (1.0 - np.tan(K0 * R) / (K0 * R))


def _save(fig, name):
    fig.tight_layout(); fig.savefig(ASSETS / name, dpi=140); plt.close(fig)


def fig_phase_shift():
    k = np.linspace(0.01, 5.0, 600)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for V0, c in zip([1.0, 5.0, 25.0, 60.0], ["C0", "C1", "C2", "C3"]):
        n0 = bound_state_count(V0)
        ax.plot(k, delta0(k, V0) / np.pi, c, label=rf"$V_0={V0}$  ($n_0={n0}$)")
    for n in range(4):
        ax.axhline(n, color="k", lw=0.4, ls=":")
    ax.set(xlabel="k", ylabel=r"$\delta_0(k)/\pi$",
           title=r"s-wave phase shift; Levinson: $\delta_0(0)=n_0\pi$")
    ax.legend(); ax.grid(alpha=0.3)
    _save(fig, "phase_shift_vs_k.png")


def fig_cross_section():
    k = np.linspace(0.05, 5.0, 600)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for V0, c in zip([1.0, 5.0, 25.0, 60.0], ["C0", "C1", "C2", "C3"]):
        ax.plot(k, cross_section(k, V0), c, label=rf"$V_0={V0}$")
    ax.set(xlabel="k", ylabel=r"$\sigma_0(k)$", yscale="log",
           title=r"s-wave total cross section $\sigma_0=4\pi\sin^2\delta_0/k^2$")
    ax.legend(); ax.grid(alpha=0.3, which="both")
    _save(fig, "cross_section.png")


def fig_scattering_length():
    V0 = np.linspace(0.001, 30.0, 4000)
    a = np.where(np.abs(scattering_length(V0)) < 50, scattering_length(V0), np.nan)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(V0, a, "C0")
    for n in (1, 2, 3):
        Vc = ((2 * n - 1) * np.pi / 2) ** 2
        if Vc < 30:
            ax.axvline(Vc, color="r", lw=0.5, ls="--",
                       label=r"$K_0R=(2n-1)\pi/2$" if n == 1 else None)
    ax.axhline(0, color="k", lw=0.4)
    ax.set(xlabel=r"$V_0$  (with $R=1$)", ylabel=r"$a(V_0)$", ylim=(-15, 15),
           title="Scattering length; poles at thresholds for new bound states")
    ax.legend(); ax.grid(alpha=0.3)
    _save(fig, "scattering_length.png")


def fig_effective_range_fit():
    V0, k = 2.0, np.linspace(0.01, 1.2, 200)
    kcot = k / np.tan(delta0(k, V0))
    slope, intercept = np.polyfit(k * k, kcot, 1)
    a_exact = scattering_length(V0)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(k * k, kcot, "C0o", ms=3, label="data")
    ax.plot(k * k, slope * k * k + intercept, "C1-",
            label=rf"fit: $-1/a={-intercept:.3f},\ r_e={2*slope:.3f}$")
    ax.axhline(-1.0 / a_exact, color="k", lw=0.5, ls=":",
               label=rf"exact $-1/a={-1/a_exact:.3f}$")
    ax.set(xlabel=r"$k^2$", ylabel=r"$k\cot\delta_0$",
           title=rf"Effective-range expansion at $V_0={V0}$, $R=1$")
    ax.legend(); ax.grid(alpha=0.3)
    _save(fig, "effective_range_fit.png")


def sanity_checks():
    # (a) scattering length matches lim_{k->0} -delta0/k
    for V0 in [0.5, 2.0, 8.0]:
        k_small = np.array([1e-4, 2e-4, 5e-4])
        d = delta0(k_small, V0)
        n0 = bound_state_count(V0)
        a_num = -(d[0] - n0 * np.pi) / k_small[0]
        a_th = scattering_length(V0)
        assert np.isclose(a_num, a_th, rtol=1e-3), \
            f"scattering length mismatch V0={V0}: num={a_num}, th={a_th}"
    # (b) near K0 R = pi/2 + 0.1 the scattering length is large
    K0R = np.pi / 2 + 0.1
    a_big = scattering_length(K0R ** 2)
    assert abs(a_big) > 5, f"expected large |a|, got {a_big}"
    # (c) elastic unitarity |S0|=1 at several k
    for V0 in [1.0, 8.0, 25.0]:
        for kk in [0.1, 0.7, 2.3, 4.5]:
            d = delta0(np.array([kk - 0.01, kk, kk + 0.01]), V0)[1]
            S0 = np.exp(2j * d)
            assert np.isclose(abs(S0), 1.0), f"|S0|!=1 at V0={V0}, k={kk}"
    print("sanity checks passed")


if __name__ == "__main__":
    sanity_checks()
    fig_phase_shift()
    fig_cross_section()
    fig_scattering_length()
    fig_effective_range_fit()
    print(f"figures written to {ASSETS}")
