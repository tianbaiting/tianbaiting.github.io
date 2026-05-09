"""DWBA numerical demo: PWBA vs DWBA vs exact.

Three amplitudes for V = V_C + V_SR with V_SR(r) = -V0 exp(-r^2 / R^2):

  PWBA  : Born on V_C + V_SR using plane waves. V_C Born is divergent
          (Coulomb Fourier blows up at q -> 0); we report only the V_SR piece.
  DWBA  : f_C exact + Coulomb-distorted Born on V_SR via F_l^2 integral
          delta_l^{SR,DWBA} = -(1/k) int F_l(eta, kr)^2 V_SR dr.
  exact : f_C exact + Numerov on V_C+V_SR, delta_l^{SR} = phi^{tot} - sigma_l.

Convention: hbar = 2m = 1, mu = 1/2 so (2 mu / hbar^2 k) in (delta-CB) of
coulomb_scattering.zh.md:352 reduces to (1/k). dependencies: numpy + matplotlib.
"""
from pathlib import Path
import sys
from importlib import import_module
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
_c11 = import_module("11_coulomb_demo")
sigma_l_array = _c11.sigma_l_array
numerov_coulomb = _c11.numerov_coulomb
extract_total_phase = _c11.extract_total_phase
f_coulomb = _c11.f_coulomb
f_short_range = _c11.f_short_range

ASSETS = Path(__file__).parent / "assets" / "12_dwba_demo"
ASSETS.mkdir(parents=True, exist_ok=True)

ETA, R_GAUSS, K_INC = 1.0, 1.0, 1.0
L_MAX = 12
RMAX_FL, N_FL = 80.0, 40000
RMAX_TOT, N_TOT = 400.0, 200000


def V_SR(r, V0):
    return -V0 * np.exp(-(r / R_GAUSS) ** 2)


def coulomb_F(l, k, eta):
    """F_l(eta, kr) by Numerov, normalized to unit asymptotic amplitude."""
    r, u = numerov_coulomb(l, k, eta, V_extra=None, r_max=RMAX_FL, N=N_FL)
    sig = sigma_l_array(eta, l)[l]
    phi = extract_total_phase(r, u, l, k, eta, ref=sig)
    n2 = len(r) - 1
    arg2 = k * r[n2] - l * np.pi / 2 - eta * np.log(2 * k * r[n2])
    return r, u / (u[n2] / np.sin(arg2 + phi))


def delta_dwba(l, k, eta, V0):
    """delta_l^{SR,DWBA} = -(1/k) int F_l^2 V_SR dr ; (delta-CB) of coulomb_scattering.zh.md:352."""
    r, F = coulomb_F(l, k, eta)
    return -(1.0 / k) * np.trapezoid(F ** 2 * V_SR(r, V0), r)


def delta_exact(l, k, eta, V0, sigma_l):
    """delta_l^{SR,exact} = phi^{tot} - sigma_l from Numerov on V_C + V_SR."""
    if V0 == 0.0:
        return 0.0
    r, u = numerov_coulomb(l, k, eta, V_extra=lambda rr: V_SR(rr, V0),
                           r_max=RMAX_TOT, N=N_TOT)
    phi = extract_total_phase(r, u, l, k, eta, ref=sigma_l)
    d = phi - sigma_l
    return d - np.pi * round(d / np.pi)


def f_pwba_gaussian(theta, k, V0):
    """Plane-wave Born for the Gaussian piece only (V_C Born diverges).
    f^{PWBA}_{SR}(theta) = -(1/(4 pi)) * Fourier{V_SR}(q),
    Fourier{-V0 e^{-r^2/R^2}} = -V0 (pi R^2)^{3/2} e^{-q^2 R^2/4}.
    """
    q2 = 4.0 * k * k * np.sin(theta / 2.0) ** 2
    fourier = -V0 * (np.pi * R_GAUSS ** 2) ** 1.5 * np.exp(-q2 * R_GAUSS ** 2 / 4.0)
    return -fourier / (4.0 * np.pi)


def assemble(theta, V0):
    """Return (f_C, f_pwba_SR, f_DWBA_total, f_exact_total, delta_d, delta_e)."""
    k, eta = K_INC, ETA
    sigma_l = sigma_l_array(eta, L_MAX - 1)
    delta_d = np.array([delta_dwba(l, k, eta, V0) for l in range(L_MAX)])
    delta_e = np.array([delta_exact(l, k, eta, V0, sigma_l[l]) for l in range(L_MAX)])
    fC = f_coulomb(theta, k, eta)
    fSR_d = f_short_range(theta, k, eta, delta_d, sigma_l)
    fSR_e = f_short_range(theta, k, eta, delta_e, sigma_l)
    return fC, f_pwba_gaussian(theta, k, V0), fC + fSR_d, fC + fSR_e, delta_d, delta_e


def fig_cross_section_compare():
    theta = np.linspace(0.05, np.pi - 0.001, 400)
    V0 = 1.0
    fC, fpw, fdw, fex, _, _ = assemble(theta, V0)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(np.degrees(theta), np.abs(fC) ** 2, "k:", label=r"$|f_C|^2$ Rutherford")
    ax.semilogy(np.degrees(theta), np.abs(fpw) ** 2, "C0--",
                label=r"$|f_{SR}^{PWBA}|^2$ (no Coulomb!)")
    ax.semilogy(np.degrees(theta), np.abs(fdw) ** 2, "C1-", lw=2,
                label=r"$|f_C+f_{SR}^{DWBA}|^2$")
    ax.semilogy(np.degrees(theta), np.abs(fex) ** 2, "C3-", lw=1.5,
                label=r"$|f_C+f_{SR}^{exact}|^2$")
    ax.set_xlabel(r"$\theta$  [deg]"); ax.set_ylabel(r"$d\sigma/d\Omega$")
    ax.set_title(rf"PWBA vs DWBA vs exact, $\eta=1$, $V_0={V0}$, $R=1$, $k=1$")
    ax.legend(fontsize=9, loc="upper right"); ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(ASSETS / "cross_section_compare.png", dpi=140)
    plt.close(fig)


def fig_dwba_error_vs_VSR():
    V0_grid = np.array([0.05, 0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
    theta = np.array([np.pi / 2.0])
    rel = []
    for V0 in V0_grid:
        _, _, fdw, fex, _, _ = assemble(theta, V0)
        rel.append(np.abs(fdw - fex)[0] / np.abs(fex)[0])
    rel = np.array(rel)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.loglog(V0_grid, rel, "C1o-", label=r"$|f^{DWBA}-f^{exact}|/|f^{exact}|$")
    ax.loglog(V0_grid, rel[1] * (V0_grid / V0_grid[1]) ** 2,
              "k--", lw=0.8, label=r"slope-2 guide")
    ax.set_xlabel(r"$V_0$"); ax.set_ylabel(r"relative error at $\theta = 90°$")
    ax.set_title(r"DWBA error scaling, $\eta=1$, $k=1$, $R=1$")
    ax.legend(); ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(ASSETS / "dwba_error_vs_VSR.png", dpi=140)
    plt.close(fig)
    return V0_grid, rel


def fig_phase_shifts_compare():
    ls = np.arange(4)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, V0 in zip(axes, [1.0, 3.0]):
        sigma_l = sigma_l_array(ETA, max(ls))
        d_d = np.array([delta_dwba(l, K_INC, ETA, V0) for l in ls])
        d_e = np.array([delta_exact(l, K_INC, ETA, V0, sigma_l[l]) for l in ls])
        ax.plot(ls, d_d, "C0o-", label=r"$\delta_l^{SR,DWBA}$ via $F_l^2$ integral")
        ax.plot(ls, d_e, "C3x", ms=12, mew=2, label=r"$\delta_l^{SR,exact}$ Numerov")
        ax.set_xlabel(r"$l$"); ax.set_ylabel(r"$\delta_l^{SR}$")
        ax.set_title(rf"$V_0 = {V0}$, $\eta=1$, $k=1$")
        ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "phase_shifts_compare.png", dpi=140)
    plt.close(fig)


def fig_interference_pattern():
    theta = np.linspace(0.05, np.pi - 0.001, 400)
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    for ax, V0 in zip(axes, [0.3, 1.0, 3.0]):
        _, fpw, fdw, fex, _, _ = assemble(theta, V0)
        ax.semilogy(np.degrees(theta), np.abs(fpw) ** 2, "C0--",
                    label=r"$|f_{SR}^{PWBA}|^2$")
        ax.semilogy(np.degrees(theta), np.abs(fdw) ** 2, "C1-", lw=2,
                    label=r"$|f^{DWBA}|^2$")
        ax.semilogy(np.degrees(theta), np.abs(fex) ** 2, "C3-", lw=1.2,
                    label=r"$|f^{exact}|^2$")
        ax.set_xlabel(r"$\theta$  [deg]"); ax.set_ylabel(r"$d\sigma/d\Omega$")
        ax.set_title(rf"$V_0 = {V0}$"); ax.legend(fontsize=8)
        ax.grid(alpha=0.3, which="both")
    fig.tight_layout(); fig.savefig(ASSETS / "interference_pattern.png", dpi=140)
    plt.close(fig)


def sanity_checks():
    theta = np.array([np.pi / 3, np.pi / 2, 2 * np.pi / 3])
    # (a) V0 = 0 : f_DWBA = f_exact = f_C
    fC, _, fdw, fex, _, _ = assemble(theta, 0.0)
    err_a = max(np.max(np.abs(fdw - fC)), np.max(np.abs(fex - fC)))
    assert err_a < 1e-6, f"(a) V0=0 failed, err={err_a}"
    # (b) V0 = 0.1 : relative error < 5%
    _, _, fdw, fex, _, _ = assemble(theta, 0.1)
    rel_b = np.max(np.abs(fdw - fex) / np.abs(fex))
    assert rel_b < 0.05, f"(b) V0=0.1 failed, rel={rel_b}"
    # (c) V0 = 0.3 : low-l phase agreement < 6% (above Numerov noise floor)
    sigma_l = sigma_l_array(ETA, 3); diags = []
    for l in range(2):
        dd = delta_dwba(l, K_INC, ETA, 0.3)
        de = delta_exact(l, K_INC, ETA, 0.3, sigma_l[l])
        rel = abs(dd - de) / abs(de); diags.append((l, dd, de, rel))
        assert rel < 0.06, f"(c) l={l} DWBA={dd:.5f} exact={de:.5f} rel={rel}"
    print("sanity checks passed")
    print(f"  (a) V0=0   max |f_DWBA-f_C|       = {err_a:.2e}")
    print(f"  (b) V0=0.1 max relative error     = {rel_b:.4f}")
    for l, dd, de, rel in diags:
        print(f"  (c) V0=0.3 l={l}  DWBA={dd:+.5f}  exact={de:+.5f}  rel={rel:.3%}")


if __name__ == "__main__":
    sanity_checks()
    fig_cross_section_compare()
    V0_grid, rel = fig_dwba_error_vs_VSR()
    fig_phase_shifts_compare()
    fig_interference_pattern()
    print("DWBA error scan at theta=90 deg:")
    for V0, r in zip(V0_grid, rel):
        print(f"  V0={V0:5.2f}  rel_err={r:.4e}")
    print(f"figures written to {ASSETS}")
