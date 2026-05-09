"""Two-channel s-wave Feshbach resonance: matrix Numerov on coupled radial eqs.

Open channel V11=0; closed channel V22=-V2 theta(R-r) shifted up by threshold
gap dE; coupling V12=g theta(R-r). Below threshold (E<dE) channel 2 is closed
(k2 imaginary, u2 -> 0 at infinity). Units hbar=1, 2m=1.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "09_feshbach_two_channel"
ASSETS.mkdir(parents=True, exist_ok=True)
V2, R, DE = 8.0, 1.0, 5.0


def closed_bound_state():
    """Solve K cot(KR) = -kappa for the g=0 closed-channel s-wave bound state."""
    def f(Eb):
        kap, K = np.sqrt(DE - Eb), np.sqrt(V2 - (DE - Eb))
        return K / np.tan(K * R) + kap
    Es = np.linspace(0.01, DE - 0.01, 4000)
    a, b = Es[np.where(np.diff(np.sign(f(Es))))[0][0] + np.array([0, 1])]
    for _ in range(80):
        m = 0.5 * (a + b)
        b, a = (m, a) if f(a) * f(m) < 0 else (b, m)
    Eb = 0.5 * (a + b)
    K, kap = np.sqrt(V2 - (DE - Eb)), np.sqrt(DE - Eb)
    norm2 = (R / 2 - np.sin(2 * K * R) / (4 * K)) + np.sin(K * R) ** 2 / (2 * kap)
    return Eb, K, kap, 1.0 / np.sqrt(norm2)


def integrate(E, g, rmax=8.0, N=1600):
    """Matrix Numerov for u'' = F u, F = V - diag(k1^2, k2^2). Returns r and
    U[N+1, channel, indep-solution] with U[0]=0 and U[1]=h*I."""
    h = rmax / N; r = np.linspace(0, rmax, N + 1)
    F_in = np.array([[-E, g], [g, -V2 - (E - DE)]])
    F_out = np.array([[-E, 0.0], [0.0, -(E - DE)]])
    h2, I2 = h * h, np.eye(2)
    M_curr_in = np.linalg.solve(I2 - h2 / 12 * F_in, 2 * (I2 + 5 * h2 / 12 * F_in))
    M_curr_out = np.linalg.solve(I2 - h2 / 12 * F_out, 2 * (I2 + 5 * h2 / 12 * F_out))
    is_in = r <= R
    U = np.zeros((N + 1, 2, 2)); U[1] = h * I2
    for n in range(1, N):
        if is_in[n] == is_in[n + 1] == is_in[n - 1]:
            M_c = M_curr_in if is_in[n] else M_curr_out
            U[n + 1] = M_c @ U[n] - U[n - 1]
        else:
            F_n = F_in if is_in[n + 1] else F_out
            F_c = F_in if is_in[n] else F_out
            F_p = F_in if is_in[n - 1] else F_out
            rhs = 2 * (I2 + 5 * h2 / 12 * F_c) @ U[n] - (I2 - h2 / 12 * F_p) @ U[n - 1]
            U[n + 1] = np.linalg.solve(I2 - h2 / 12 * F_n, rhs)
    return r, U


def phase_shift(E, g, rmax=8.0, N=1600):
    """Open-channel phase shift; impose u_2(rmax) ~ exp(-|k2| r) on the 2-D
    solution space, then read tan(delta1) = Cc/Cs from u_1 in the asymptotic region."""
    r, U = integrate(E, g, rmax, N)
    k1, k2abs, h = np.sqrt(E), np.sqrt(DE - E), r[1] - r[0]
    coeff = (U[-1, 1, :] - U[-2, 1, :]) / h + k2abs * U[-1, 1, :]   # length-2
    alpha = np.array([-coeff[1], coeff[0]])
    if np.linalg.norm(alpha) < 1e-14: return 0.0
    alpha /= np.linalg.norm(alpha)
    u1 = U[:, 0, :] @ alpha
    i1, i2 = int(0.7 * N), int(0.9 * N); r1, r2 = r[i1], r[i2]; v1, v2 = u1[i1], u1[i2]
    s1, c1, s2, c2 = np.sin(k1 * r1), np.cos(k1 * r1), np.sin(k1 * r2), np.cos(k1 * r2)
    det = s1 * c2 - s2 * c1
    return np.arctan2((s1 * v2 - s2 * v1) / det, (v1 * c2 - v2 * c1) / det)


def g_eff_squared(E, g):
    """Friedrichs effective coupling |g_eff(E)|^2 for V12=g, energy-normalized
    free open-channel state u_E^(0)(r) = sin(k1 r)/sqrt(pi k1)."""
    Eb, K, kap, A = closed_bound_state(); k1 = np.sqrt(E)
    if abs(K - k1) < 1e-10:
        I1 = R / 2 - np.sin(2 * K * R) / (4 * K)
    else:
        I1 = 0.5 * (np.sin((K - k1) * R) / (K - k1) - np.sin((K + k1) * R) / (K + k1))
    return (g * A * I1) ** 2 / (np.pi * k1)


def extract_width(g, Eb_guess):
    """Resonance position and width: at E_R the phase derivative peaks; Gamma=2/d."""
    Es = np.linspace(max(0.05, Eb_guess - 0.6), min(DE - 0.05, Eb_guess + 0.6), 401)
    dd = np.gradient(np.unwrap(np.array([phase_shift(E, g) for E in Es])), Es)
    i = int(np.argmax(dd))
    return Es[i], 2.0 / dd[i]


def _save(fig, name):
    fig.tight_layout(); fig.savefig(ASSETS / name, dpi=140); plt.close(fig)


def make_figures():
    Eb, *_ = closed_bound_state()
    # fig 1: model
    rs = np.linspace(0, 2.0, 400); fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(rs, 0 * rs, "C0", lw=2, label=r"$V_{11}=0$ (open)")
    ax.plot(rs, np.where(rs <= R, DE - V2, DE), "C1", lw=2,
            label=rf"$V_{{22}}+\Delta E$, $V_2={V2}$")
    ax.axhline(DE, color="C1", lw=0.6, ls=":"); ax.axhline(0, color="k", lw=0.4)
    ax.axhline(Eb, color="r", lw=1.0, ls="--", label=rf"$E_b^{{(2)}}={Eb:.3f}$")
    ax.set(xlabel="r", ylabel="energy", title="Two-channel potentials (+dE offset on closed)")
    ax.legend(); ax.grid(alpha=0.3); _save(fig, "model.png")
    # fig 2&3: phase shift and cross section
    Es = np.linspace(0.05, DE - 0.05, 220)
    f_p, a_p = plt.subplots(figsize=(7, 4.5)); f_x, a_x = plt.subplots(figsize=(7, 4.5))
    for g, c in zip([0.3, 0.7, 1.5], ["C0", "C1", "C2"]):
        d = np.unwrap(np.array([phase_shift(E, g) for E in Es]))
        a_p.plot(Es, d / np.pi, c, label=rf"$g={g}$")
        a_x.plot(Es, 4 * np.pi * np.sin(d) ** 2 / Es, c, label=rf"$g={g}$")
    a_p.axvline(Eb, color="r", lw=0.6, ls=":", label=rf"$E_b^{{(2)}}={Eb:.3f}$")
    a_p.set(xlabel="E", ylabel=r"$\delta_1(E)/\pi$",
            title=r"Open-channel phase shift; resonance at $E_R\approx E_b^{(2)}$")
    a_x.set(xlabel="E", ylabel=r"$\sigma_1(E)$", yscale="log",
            title=r"Cross section $\sigma_1=4\pi\sin^2\delta_1/k_1^2$")
    for f, a, n in [(f_p, a_p, "phase_shift_E"), (f_x, a_x, "cross_section")]:
        a.legend(); a.grid(alpha=0.3, which="both"); _save(f, n + ".png")
    # fig 4: width vs g^2
    gs = np.array([0.15, 0.2, 0.3, 0.45, 0.6, 0.85])
    Gnum = np.array([extract_width(g, Eb)[1] for g in gs])
    Gpred = np.array([2 * np.pi * g_eff_squared(Eb, g) for g in gs])
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.loglog(gs ** 2, Gnum, "C0o-", label=r"numerical $\Gamma(g)$")
    ax.loglog(gs ** 2, Gpred, "C1--", label=r"Friedrichs $2\pi|g_{\rm eff}(E_b)|^2$")
    ax.set(xlabel=r"$g^2$", ylabel=r"$\Gamma$",
           title=r"Width $\Gamma$ vs coupling $g^2$ (weak coupling: slope 1)")
    ax.legend(); ax.grid(alpha=0.3, which="both"); _save(fig, "gamma_vs_g2.png")


def sanity_checks():
    Eb, *_ = closed_bound_state()
    for E in [0.5, 1.5, 3.0, 4.5]:
        d = phase_shift(E, 0.0); d_mod = (d + np.pi / 2) % np.pi - np.pi / 2
        assert abs(d_mod) < 1e-8, f"g=0 -> delta1=0 mod pi failed: {d} at E={E}"
    g = 0.3; _, Gnum = extract_width(g, Eb); Gpred = 2 * np.pi * g_eff_squared(Eb, g)
    rel = abs(Gnum - Gpred) / Gpred
    assert rel < 5e-2, f"weak-coupling Gamma mismatch rel={rel:.3e}"
    E_R, _ = extract_width(0.2, Eb)
    assert abs(E_R - Eb) < 0.1, f"E_R={E_R} should approach Eb={Eb}"
    print(f"sanity checks passed. Eb={Eb:.4f}, weak-g rel.err={rel:.3e}")


if __name__ == "__main__":
    sanity_checks(); make_figures(); print(f"figures written to {ASSETS}")
