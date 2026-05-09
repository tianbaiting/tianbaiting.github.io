"""Coulomb scattering numerical demo.

Three demos:
  1. Coulomb phase shifts sigma_l(eta) = arg Gamma(l+1+i eta), analytic
     (Weierstrass series + recurrence) vs Numerov integration of the radial
     Coulomb equation matched to F_l(eta, kr) asymptotics.
  2. Pure Coulomb (Rutherford) differential cross section.
  3. Coulomb + short-range Gaussian, showing the Coulomb-nuclear interference
     in d sigma / d Omega.

Convention: hbar = 2m = 1, so E = k^2.  Sommerfeld parameter eta is taken as
an input (we do not unwind the units).

Dependencies: numpy + matplotlib only (scipy intentionally not used).
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "11_coulomb_demo"
ASSETS.mkdir(parents=True, exist_ok=True)

EULER_GAMMA = 0.5772156649015329


# ------------------ analytic sigma_l via Weierstrass + recurrence ------------

def sigma_0(eta, N=4000):
    """sigma_0(eta) = arg Gamma(1 + i eta) by Weierstrass series.

    arg Gamma(1 + i eta) = -gamma eta + sum_{n=1..inf} [eta/n - arctan(eta/n)]
    Each term ~ eta^3 / (3 n^3); N=4000 buys ~10 digits for |eta| <= 5.
    """
    n = np.arange(1, N + 1)
    return -EULER_GAMMA * eta + np.sum(eta / n - np.arctan(eta / n))


def sigma_l_array(eta, l_max):
    """[sigma_0, sigma_1, ..., sigma_lmax] using sigma_{l+1}=sigma_l+arctan(eta/(l+1))."""
    out = np.empty(l_max + 1)
    out[0] = sigma_0(eta)
    for l in range(l_max):
        out[l + 1] = out[l] + np.arctan(eta / (l + 1))
    return out


# ------------------ Numerov for radial Coulomb (+ optional short range) -----

def numerov_coulomb(l, k, eta, V_extra=None, r_max=80.0, N=40000):
    """Integrate u'' + [k^2 - 2 k eta / r - l(l+1)/r^2 - V_extra(r)] u = 0.

    Boundary: u(0)=0, u(h)=h^{l+1}.  Returns (r, u).
    V_extra is the (real) extra short-range potential term (in 2m=1 units).
    """
    h = r_max / N
    r = np.linspace(0.0, r_max, N + 1)
    rs = np.where(r > 0, r, 1.0)
    centrifugal = l * (l + 1) / rs ** 2
    coulomb = 2.0 * k * eta / rs
    f = k * k - coulomb - centrifugal
    if V_extra is not None:
        f = f - V_extra(rs)
    f[0] = 0.0  # not used; u[0]=0 anyway
    u = np.zeros(N + 1)
    u[1] = h ** (l + 1)
    h2 = h * h / 12.0
    for n in range(1, N):
        num = 2 * u[n] * (1 - 5 * h2 * f[n]) - u[n - 1] * (1 + h2 * f[n - 1])
        u[n + 1] = num / (1 + h2 * f[n + 1])
    return r, u


def _phase_at(r, u, l, k, eta, n1, n2, ref):
    """Match at indices n1<n2 to leading asymptotic; pick branch closest to ref."""
    r1, r2 = r[n1], r[n2]
    u1, u2 = u[n1], u[n2]
    arg1 = k * r1 - l * np.pi / 2 - eta * np.log(2 * k * r1)
    arg2 = k * r2 - l * np.pi / 2 - eta * np.log(2 * k * r2)
    K = u1 * np.sin(arg2) - u2 * np.sin(arg1)
    L = u2 * np.cos(arg1) - u1 * np.cos(arg2)
    phi = np.arctan2(K, L)
    if ref is not None:
        phi -= np.pi * round((phi - ref) / np.pi)
    return phi


def extract_total_phase(r, u, l, k, eta, ref=None):
    """Total accumulated phase phi from u(r) ~ A sin(kr - l pi/2 - eta ln(2 k r) + phi).

    Leading asymptotic match has a residual bias ~ O(1/(k r)) from sub-leading
    terms in the Coulomb asymptotic series.  We sample three matching radii on
    the integrated grid and Richardson-extrapolate phi(1/r) -> intercept.
    For pure Coulomb the result is sigma_l; for Coulomb + short range it is
    sigma_l + delta_l^SR.
    """
    N = len(r) - 1
    h = r[1] - r[0]
    step_back = max(4, int(0.25 * np.pi / (k * h)))
    fracs = [0.5, 0.75, 1.0]
    rs = []
    phis = []
    for fac in fracs:
        n2 = int(N * fac)
        n1 = n2 - step_back
        phi = _phase_at(r, u, l, k, eta, n1, n2, ref)
        rs.append(r[n2])
        phis.append(phi)
    rs = np.array(rs)
    phis = np.array(phis)
    # linear fit phi vs 1/r, take intercept
    p = np.polyfit(1.0 / rs, phis, 1)
    return p[1]


# ------------------ Rutherford & Coulomb amplitude -------------------------

def f_coulomb(theta, k, eta):
    """Closed form f_C(theta), eq (fC) in coulomb_scattering.zh.md:190."""
    s2 = np.sin(theta / 2.0) ** 2
    sig0 = sigma_0(eta)
    mag = -eta / (2.0 * k * s2)
    phase = np.exp(1j * (-eta * np.log(s2) + 2.0 * sig0))
    return mag * phase


def rutherford(theta, k, eta):
    return eta ** 2 / (4.0 * k ** 2 * np.sin(theta / 2.0) ** 4)


# ------------------ short-range partial-wave amplitude --------------------

def f_short_range(theta, k, eta, delta_sr, sigma_l):
    """f_{SR}(theta) = (1/2ik) sum (2l+1) e^{2i sigma_l} (e^{2i delta_l^SR} - 1) P_l(cos t)."""
    cos_t = np.cos(theta)
    L = len(delta_sr)
    # Legendre by recurrence
    P = np.zeros((L, len(theta)))
    P[0] = 1.0
    if L >= 2:
        P[1] = cos_t
    for l in range(1, L - 1):
        P[l + 1] = ((2 * l + 1) * cos_t * P[l] - l * P[l - 1]) / (l + 1)
    out = np.zeros(len(theta), dtype=complex)
    for l in range(L):
        amp = np.exp(2j * sigma_l[l]) * (np.exp(2j * delta_sr[l]) - 1.0)
        out += (2 * l + 1) * amp * P[l]
    return out / (2j * k)


# ============== DEMO 1: phase shifts =====================================

def fig_phase_shifts():
    etas = [0.5, 1.0, 2.0]
    l_max = 4
    k = 1.0
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
    for ax, eta in zip(axes, etas):
        ana = sigma_l_array(eta, l_max)
        num = []
        for l in range(l_max + 1):
            r, u = numerov_coulomb(l, k, eta, r_max=400.0, N=200000)
            phi = extract_total_phase(r, u, l, k, eta, ref=ana[l])
            num.append(phi)
        num = np.array(num)
        ls = np.arange(l_max + 1)
        ax.plot(ls, ana, "bo-", label=r"analytic $\arg\Gamma(l+1+i\eta)$")
        ax.plot(ls, num, "rx", ms=10, mew=2, label="Numerov match")
        ax.set_xlabel("$l$")
        ax.set_ylabel(r"$\sigma_l(\eta)$")
        ax.set_title(rf"$\eta = {eta}$,  $k=1$")
        ax.legend()
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(ASSETS / "coulomb_phase_shifts.png", dpi=140)
    plt.close(fig)


# ============== DEMO 1b: radial wavefunctions for eta=0,0.5,1.0 ============

def fig_wavefunction():
    k = 1.0
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.0))
    for ax, l in zip(axes, [0, 1, 2]):
        for eta, color in zip([0.0, 0.5, 1.0], ["C0", "C1", "C2"]):
            r, u = numerov_coulomb(l, k, eta, r_max=30.0, N=20000)
            # normalize to unit asymptotic amplitude using the last few points
            sig = sigma_l_array(eta, l)[l] if eta != 0.0 else 0.0
            phi = extract_total_phase(r, u, l, k, eta, ref=sig)
            n2 = len(r) - 1
            arg2 = k * r[n2] - l * np.pi / 2
            if eta != 0.0:
                arg2 = arg2 - eta * np.log(2 * k * r[n2])
            A = u[n2] / np.sin(arg2 + phi)
            ax.plot(r[1:], (u[1:] / A), color=color,
                    label=rf"$\eta={eta}$")
        ax.set_xlabel("$r$")
        ax.set_ylabel(rf"$F_{l}(\eta, kr)$  (normalized)")
        ax.set_title(rf"$l = {l}$, $k = 1$")
        ax.legend()
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(ASSETS / "coulomb_wavefunction.png", dpi=140)
    plt.close(fig)


# ============== DEMO 2: Rutherford ==========================================

def fig_rutherford():
    theta = np.linspace(0.05, np.pi - 0.001, 800)
    k = 1.0
    fig, ax = plt.subplots(figsize=(7, 5))
    for eta, color in zip([0.5, 1.0, 2.0], ["C0", "C1", "C2"]):
        ax.semilogy(np.degrees(theta), rutherford(theta, k, eta),
                    color=color, label=rf"$\eta={eta}$")
    ax.axvline(0, color="k", lw=0.5, ls=":")
    ax.set_xlabel(r"$\theta$  [deg]")
    ax.set_ylabel(r"$d\sigma_C/d\Omega$")
    ax.set_title("Rutherford  $\\eta^2 / [4 k^2 \\sin^4(\\theta/2)]$,  $k=1$")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(ASSETS / "rutherford_cross_section.png", dpi=140)
    plt.close(fig)


# ============== DEMO 3: Coulomb + short-range ===============================

def short_range_potential(r, V0=4.0, R=1.0):
    return -V0 * np.exp(-(r / R) ** 2)


def fig_coulomb_plus_short_range():
    k = 1.0
    eta = 1.0
    L = 12  # partial-wave cutoff
    sigma_l = sigma_l_array(eta, L - 1)

    # solve for total phase for each l with the full V = V_C + V_SR
    delta_sr = np.zeros(L)
    for l in range(L):
        r, u = numerov_coulomb(l, k, eta,
                               V_extra=lambda rr: short_range_potential(rr, 4.0, 1.0),
                               r_max=200.0, N=80000)
        phi_tot = extract_total_phase(r, u, l, k, eta, ref=sigma_l[l])
        d = phi_tot - sigma_l[l]
        # bring delta_sr into a canonical branch: nearest to zero modulo pi
        d -= np.pi * round(d / np.pi)
        delta_sr[l] = d

    theta = np.linspace(0.05, np.pi - 0.001, 600)
    fC = f_coulomb(theta, k, eta)
    fSR = f_short_range(theta, k, eta, delta_sr, sigma_l)
    fT = fC + fSR
    interference = 2 * np.real(np.conj(fC) * fSR)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(np.degrees(theta), np.abs(fC) ** 2,
                "C0--", label=r"$|f_C|^2$ (Rutherford)")
    ax.semilogy(np.degrees(theta), np.abs(fSR) ** 2,
                "C1:", label=r"$|f_{SR}|^2$ (short range only)")
    ax.semilogy(np.degrees(theta), np.abs(fT) ** 2,
                "C2-", lw=2, label=r"$|f_C + f_{SR}|^2$ (full)")
    pos = interference >= 0
    neg = ~pos
    ax.semilogy(np.degrees(theta[pos]), interference[pos],
                "C3-", lw=1, alpha=0.7,
                label=r"$+2\,\mathrm{Re}(f_C^* f_{SR})$")
    ax.semilogy(np.degrees(theta[neg]), -interference[neg],
                "C3--", lw=1, alpha=0.7,
                label=r"$-2\,\mathrm{Re}(f_C^* f_{SR})$ (i.e. negative)")
    ax.set_xlabel(r"$\theta$  [deg]")
    ax.set_ylabel(r"$d\sigma/d\Omega$")
    ax.set_title(rf"Coulomb + Gaussian short range,  $\eta={eta}$, $V_0=4$, $R=1$, $k=1$")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(ASSETS / "coulomb_plus_short_range.png", dpi=140)
    plt.close(fig)
    return delta_sr


# ============== sanity checks ==============================================

def sanity_checks():
    # (a) numerical sigma_l matches arg Gamma(l+1+i eta) at eta=1, l=0..4 to 1e-3
    eta = 1.0
    k = 1.0
    ana = sigma_l_array(eta, 4)
    for l in range(5):
        r, u = numerov_coulomb(l, k, eta, r_max=400.0, N=200000)
        phi = extract_total_phase(r, u, l, k, eta, ref=ana[l])
        assert abs(phi - ana[l]) < 1e-3, (
            f"sigma_l mismatch at l={l}: ana={ana[l]:.6f}  num={phi:.6f}")

    # (b) eta -> 0 gives sigma_l -> 0
    s = sigma_l_array(1e-3, 4)
    assert np.max(np.abs(s)) < 1e-2, f"sigma_l(eta=1e-3) too big: {s}"

    # (c) Rutherford at theta=pi matches eta^2/(4k^2)
    eta = 1.5
    k = 0.7
    val = rutherford(np.pi, k, eta)
    expect = eta ** 2 / (4 * k ** 2)
    assert abs(val - expect) < 1e-6, f"Rutherford backward: {val} vs {expect}"

    print("sanity checks passed")
    print(f"  sigma_0(eta=1)  analytic  = {sigma_0(1.0):.6f}")
    print(f"  sigma_0(eta=1)  reference = -0.301640  (arg Gamma(1+i))")


if __name__ == "__main__":
    sanity_checks()
    fig_phase_shifts()
    fig_wavefunction()
    fig_rutherford()
    delta_sr = fig_coulomb_plus_short_range()
    print("Coulomb-distorted short-range phase shifts (eta=1, V0=4, R=1, k=1):")
    for l, d in enumerate(delta_sr):
        print(f"  l={l}:  delta_l^SR = {d:+.4f}")
    print(f"figures written to {ASSETS}")
