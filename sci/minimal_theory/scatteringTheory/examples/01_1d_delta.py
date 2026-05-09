"""1D delta potential V(x) = lambda * delta(x).

Demonstrates the minimal scattering example used in the companion markdown:
- transmission/reflection amplitudes and unitarity check
- bound-state pole on the imaginary k axis (attractive case)
- even-channel phase shift, with one-dimensional Levinson signature
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "01_1d_delta"
ASSETS.mkdir(parents=True, exist_ok=True)


def t_r(k, lam):
    """Transmission and reflection amplitudes. Units: hbar=1, 2m=1."""
    denom = 2j * k - lam
    return 2j * k / denom, lam / denom


def phase_shift_even(k, lam):
    return np.arctan(-lam / (2 * k))


def fig_transmission():
    k = np.linspace(0.05, 5.0, 400)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, lam, title in zip(axes, [-2.0, +2.0],
                              ["Attractive  λ=-2", "Repulsive  λ=+2"]):
        t, r = t_r(k, lam)
        ax.plot(k, np.abs(t) ** 2, label=r"$|t|^2$")
        ax.plot(k, np.abs(r) ** 2, label=r"$|r|^2$")
        ax.plot(k, np.abs(t) ** 2 + np.abs(r) ** 2, "--", label="sum")
        ax.set_xlabel("k")
        ax.set_title(title)
        ax.legend()
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(ASSETS / "transmission.png", dpi=140)
    plt.close(fig)


def fig_pole(lam=-2.0):
    kr = np.linspace(-3, 3, 400)
    ki = np.linspace(-2, 2, 300)
    KR, KI = np.meshgrid(kr, ki)
    K = KR + 1j * KI
    T = 2j * K / (2j * K - lam)
    fig, ax = plt.subplots(figsize=(6, 5))
    pcm = ax.pcolormesh(KR, KI, np.log10(np.abs(T) + 1e-3),
                        shading="auto", cmap="viridis")
    fig.colorbar(pcm, ax=ax, label=r"$\log_{10}|t(k)|$")
    ax.axhline(0, color="w", lw=0.5)
    ax.axvline(0, color="w", lw=0.5)
    kappa = -lam / 2
    ax.plot(0, kappa, "r*", ms=15, label=f"pole  k=i·{kappa:.2f}")
    ax.set_xlabel("Re k")
    ax.set_ylabel("Im k")
    ax.legend()
    ax.set_title(rf"$|t(k)|$ on complex k plane,  λ={lam}")
    fig.tight_layout()
    fig.savefig(ASSETS / "pole.png", dpi=140)
    plt.close(fig)


def fig_phase_shift():
    k = np.linspace(0.05, 5.0, 400)
    fig, ax = plt.subplots(figsize=(7, 4))
    for lam, c in zip([-2.0, -0.5, +0.5, +2.0],
                      ["C0", "C1", "C2", "C3"]):
        ax.plot(k, phase_shift_even(k, lam), c, label=f"λ={lam}")
    ax.set_xlabel("k")
    ax.set_ylabel(r"$\delta_e(k)$")
    ax.axhline(np.pi / 2, color="k", lw=0.5, ls=":")
    ax.axhline(-np.pi / 2, color="k", lw=0.5, ls=":")
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_title("Even-channel phase shift")
    fig.tight_layout()
    fig.savefig(ASSETS / "phase_shift.png", dpi=140)
    plt.close(fig)


def sanity_checks():
    """Spot-check unitarity and the bound-state pole formula."""
    rng = np.random.default_rng(0)
    for _ in range(5):
        lam = rng.uniform(-3, 3)
        k = rng.uniform(0.1, 5.0)
        t, r = t_r(k, lam)
        assert np.isclose(np.abs(t) ** 2 + np.abs(r) ** 2, 1.0), \
            f"unitarity broken at lam={lam}, k={k}"
    for lam in [-2.0, -0.5, -3.7]:
        kappa = -lam / 2
        E_b = -kappa ** 2
        denom = 2j * (1j * kappa) - lam
        assert np.isclose(denom, 0.0), \
            f"bound-state pole misplaced for lam={lam}"
        assert np.isclose(E_b, -lam ** 2 / 4)
    print("sanity checks passed")


if __name__ == "__main__":
    sanity_checks()
    fig_transmission()
    fig_pole(lam=-2.0)
    fig_phase_shift()
    print(f"figures written to {ASSETS}")
