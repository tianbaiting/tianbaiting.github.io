"""3D delta shell V(r)=(gamma/R)delta(r-R), s-wave. Units hbar=1, 2mu=1, E=k^2."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "03_delta_shell"
ASSETS.mkdir(parents=True, exist_ok=True)


def tan_delta0(k, gamma, R=1.0):
    s, c = np.sin(k * R), np.cos(k * R)
    return -gamma * s * s / (k * R + gamma * s * c)


def s_matrix(k, gamma, R=1.0):
    t = tan_delta0(k, gamma, R)
    return (1 + 1j * t) / (1 - 1j * t)


def cross_section(k, gamma, R=1.0):
    s, c = np.sin(k * R), np.cos(k * R)
    num = (gamma * s * s) ** 2
    den = (k * R + gamma * s * c) ** 2 + num
    return 4 * np.pi * num / den / (k * k)


def newton_pole(k0, gamma, R=1.0, tol=1e-12, itmax=80):
    """Zero of D(k)=kR+gamma sin cos + i gamma sin^2; pole of S_0 (Im k<0)."""
    k = complex(k0)
    for _ in range(itmax):
        s, c = np.sin(k * R), np.cos(k * R)
        f = k * R + gamma * s * c + 1j * gamma * s * s
        df = R + gamma * R * (c * c - s * s) + 2j * gamma * s * c * R
        dk = f / df
        k -= dk
        if abs(dk) < tol:
            break
    return k


def fig_phase_shift():
    k = np.linspace(0.05, 8.0, 2000)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for gamma in (5.0, 20.0, 50.0):
        d = np.unwrap(2 * np.arctan(tan_delta0(k, gamma))) / 2
        ax.plot(k, d, label=f"γ={gamma:g}")
    for n in (1, 2):
        ax.axvline(n * np.pi, color="gray", lw=0.4, ls=":")
    ax.set(xlabel="k  (R=1)", ylabel=r"$\delta_0(k)$",
           title="S-wave phase shift, repulsive shell")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "phase_shift.png", dpi=140); plt.close(fig)


def fig_cross_section():
    k = np.linspace(0.05, 8.0, 4000)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for gamma in (5.0, 20.0, 50.0):
        ax.plot(k, cross_section(k, gamma), label=f"γ={gamma:g}")
    ax.set(xlabel="k  (R=1)", ylabel=r"$\sigma_0=4\pi\sin^2\delta_0/k^2$",
           title="S-wave cross section, Breit-Wigner peaks", yscale="log")
    ax.legend(); ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(ASSETS / "cross_section.png", dpi=140); plt.close(fig)


def fig_pole_scan(gamma=20.0):
    kr = np.linspace(0.2, 7.5, 600); ki = np.linspace(-1.5, 0.3, 360)
    KR, KI = np.meshgrid(kr, ki)
    Z = np.log10(np.abs(s_matrix(KR + 1j * KI, gamma)) + 1e-6)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    pcm = ax.pcolormesh(KR, KI, np.clip(Z, -1, 4), shading="auto", cmap="magma")
    fig.colorbar(pcm, ax=ax, label=r"$\log_{10}|S_0(k)|$")
    poles = [newton_pole(n * np.pi - 0.05 - 0.2j / n, gamma) for n in (1, 2, 3)]
    for n, kp in enumerate(poles, 1):
        ax.plot(kp.real, kp.imag, "c*", ms=14)
        ax.annotate(f"n={n}", (kp.real, kp.imag), xytext=(6, 6),
                    textcoords="offset points", color="cyan")
    ax.axhline(0, color="w", lw=0.4)
    ax.set(xlabel="Re k", ylabel="Im k",
           title=rf"$|S_0(k)|$ on second sheet, γ={gamma:g}")
    fig.tight_layout(); fig.savefig(ASSETS / "pole_scan.png", dpi=140); plt.close(fig)
    return poles


def fig_width_vs_gamma():
    gammas = np.geomspace(3.0, 300.0, 30)
    widths = np.array([abs(4 * (kp := newton_pole(
        np.pi - 0.05 - 0.3j / np.sqrt(g), g)).real * kp.imag) for g in gammas])
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.loglog(gammas, widths, "o-", label=r"first resonance $\Gamma$")
    ax.loglog(gammas, 2 * np.pi / gammas, "k--", lw=0.8, label=r"$2\pi/\gamma$")
    ax.set(xlabel=r"$\gamma$", ylabel=r"$\Gamma$",
           title="First resonance width vs coupling")
    ax.legend(); ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "width_vs_gamma.png", dpi=140); plt.close(fig)


def sanity_checks():
    rng = np.random.default_rng(1)
    for _ in range(8):
        gamma, k = rng.uniform(-10, 50), rng.uniform(0.2, 5.0)
        assert np.isclose(abs(s_matrix(k, gamma)), 1.0, atol=1e-10)
    for k in (0.3, 1.7, 4.2):
        assert np.isclose(np.arctan(tan_delta0(k, 0.0)), 0.0)
    kp = newton_pole(np.pi - 0.05 - 0.05j, 20.0)
    assert abs(kp.real - np.pi) < 0.2 and -0.5 < kp.imag < 0.0, kp
    print(f"sanity checks passed; first pole (γ=20): k={kp:.4f}, "
          f"E_R={kp.real**2 - kp.imag**2:.4f}, Γ={abs(4*kp.real*kp.imag):.4f}")


if __name__ == "__main__":
    sanity_checks()
    fig_phase_shift(); fig_cross_section()
    poles = fig_pole_scan(gamma=20.0)
    for n, kp in enumerate(poles, 1):
        print(f"  n={n}: k={kp:.5f}  E_R={kp.real**2-kp.imag**2:.4f}  "
              f"Γ={abs(4*kp.real*kp.imag):.4f}")
    fig_width_vs_gamma()
    print(f"figures written to {ASSETS}")
