"""1D half-line well + barrier: V=-V0 on (0,a), V=+V1 on (a,a+b), 0 beyond.
Hard wall at x=0. Units hbar=1, 2m=1, E=k^2. Long-lived resonances by
barrier tunnelling (alpha-decay analogue)."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "well_barrier_1d"
ASSETS.mkdir(parents=True, exist_ok=True)
V0, V1, A, B = 20.0, 8.0, 1.0, 2.0

def log_deriv(E, b=None):
    """L = u'/u at x=a+b for the u(0)=0 solution. exp(kap*b) cancels in
    num/den, keeping the formula stable on the second sheet."""
    b = B if b is None else b
    E = np.asarray(E, dtype=complex)
    q, kap = np.sqrt(V0 + E), np.sqrt(V1 - E)
    s, c = np.sin(q * A), np.cos(q * A)
    em2 = np.exp(-2 * kap * b)
    Cp, Cm = 0.5 * (1 + em2), 0.5 * (1 - em2)
    return (kap * s * Cm + q * c * Cp) / (s * Cp + (q * c / kap) * Cm)

def S_matrix(E, b=None):
    b = B if b is None else b
    k = np.sqrt(np.asarray(E, dtype=complex)); L = log_deriv(E, b)
    return -np.exp(-2j * k * (A + b)) * (L - 1j * k) / (L + 1j * k)

def phase_shift(E):
    k = np.sqrt(np.asarray(E, dtype=float)); L = log_deriv(E).real
    return np.unwrap(2 * (np.arctan2(k, L) - k * (A + B))) / 2

def newton_pole(E0, b=None, tol=1e-13, itmax=300, max_step=0.05):
    b = B if b is None else b; E = complex(E0)
    for _ in range(itmax):
        f = log_deriv(E, b) - 1j * np.sqrt(E)
        h = 1e-7 * (1 + abs(E))
        df = (log_deriv(E + h, b) - 1j * np.sqrt(E + h) - f) / h
        if not np.isfinite(df) or df == 0:
            return E
        dE = f / df
        if abs(dE) > max_step: dE *= max_step / abs(dE)
        E -= dE
        if abs(dE) < tol: break
    return E

def seed_real(b):
    Es = np.linspace(0.01, V1 - 0.01, 4000)
    q, kap = np.sqrt(V0 + Es), np.sqrt(V1 - Es)
    em2 = np.exp(-2 * kap * b); Cp, Cm = 0.5 * (1 + em2), 0.5 * (1 - em2)
    nums = kap * np.sin(q * A) * Cm + q * np.cos(q * A) * Cp
    for i in range(len(Es) - 1):
        if nums[i] * nums[i + 1] < 0 and abs(nums[i] - nums[i + 1]) < 1.0:
            return 0.5 * (Es[i] + Es[i + 1]) - 0.001j
    return None

def gamma_wkb(E_R, b):  # bounce freq k_in/a (v=2 k_in) times e^{-2 kap b}
    return (np.sqrt(V0 + E_R) / A) * np.exp(-2 * b * np.sqrt(max(V1 - E_R, 0.0)))

def bw_fit(E_R0, half0):
    Ewide = np.linspace(E_R0 - 30 * half0, E_R0 + 30 * half0, 1001)
    bg = 0.5 * (phase_shift(Ewide)[:80].mean() + phase_shift(Ewide)[-80:].mean())
    E = np.linspace(E_R0 - 1.5 * half0, E_R0 + 1.5 * half0, 401)
    y = np.tan(phase_shift(E) - bg)
    keep = np.isfinite(y) & (np.abs(y) < 1e3)
    M = np.column_stack([np.ones(keep.sum()), y[keep]])
    sol, *_ = np.linalg.lstsq(M, E[keep], rcond=None)
    return float(sol[0]), float(sol[1])

def fig_potential(Ep):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot([0, 0, A, A, A + B, A + B, A + B + 1.5],
            [V1 + 5, -V0, -V0, V1, V1, 0, 0], lw=1.8)
    ax.fill_between([0, A], -V0, 0, alpha=0.15)
    ax.fill_between([A, A + B], 0, V1, color="C3", alpha=0.15)
    ax.axhline(Ep.real, xmin=0, xmax=A / (A + B + 1.5), color="k", lw=0.8, ls="--")
    ax.text(0.05, Ep.real + 0.4, f"$E_R={Ep.real:.3f}$", fontsize=10)
    ax.set(xlabel="x", ylabel="V(x)", title="Half-line well + barrier",
           xlim=(-0.2, A + B + 1.5), ylim=(-V0 - 2, V1 + 4)); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "potential.png", dpi=140); plt.close(fig)

def fig_transmission(Ep):
    E_R, half = Ep.real, -Ep.imag
    E = np.linspace(max(0.05, E_R - 50 * half), min(V1 - 0.05, E_R + 50 * half), 4000)
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(E, phase_shift(E), lw=1.2); ax.grid(alpha=0.3)
    ax.set(xlabel="E", ylabel=r"$\eta(E)$", title="S-wave phase shift across the resonance")
    Eloc = np.linspace(E_R - 8 * half, E_R + 8 * half, 400)
    eta_loc = phase_shift(Eloc); bg = 0.5 * (eta_loc[0] + eta_loc[-1])
    ins = ax.inset_axes([0.55, 0.15, 0.4, 0.55])
    ins.plot(Eloc, eta_loc, label="numerical")
    ins.plot(Eloc, bg + np.arctan((Eloc - E_R) / half), "k--", lw=0.9, label="BW")
    ins.set(title=fr"$E_R={E_R:.4f},\ \Gamma={2*half:.2e}$")
    ins.legend(fontsize=8); ins.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "transmission.png", dpi=140); plt.close(fig)

def fig_pole_plane(Ep):
    E_R, half = Ep.real, -Ep.imag
    er = np.linspace(E_R - 30 * half, E_R + 30 * half, 300)
    ei = np.linspace(-6 * half, 2 * half, 200)
    ER, EI = np.meshgrid(er, ei)
    Z = np.log10(np.abs(S_matrix(ER + 1j * EI)) + 1e-6)
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    pcm = ax.pcolormesh(ER, EI, np.clip(Z, -1, 4), shading="auto", cmap="magma")
    fig.colorbar(pcm, ax=ax, label=r"$\log_{10}|S(E)|$")
    ax.plot(Ep.real, Ep.imag, "c*", ms=14); ax.axhline(0, color="w", lw=0.4)
    ax.annotate(r"$E_R-i\Gamma/2$", (Ep.real, Ep.imag), xytext=(8, 8),
                textcoords="offset points", color="cyan")
    ax.set(xlabel="Re E", ylabel="Im E",
           title=rf"$|S(E)|$ 2nd sheet, $V_0={V0:g},V_1={V1:g},a={A:g},b={B:g}$")
    fig.tight_layout(); fig.savefig(ASSETS / "pole_E_plane.png", dpi=140); plt.close(fig)

def fig_width_vs_b():
    bs = np.linspace(1.2, 3.2, 11); widths, wkbs = [], []; seed = 5.29 - 0.05j
    for b in bs:
        Ep = newton_pole(seed, b=b, max_step=0.005)
        if not (0 < Ep.real < V1 and Ep.imag < 0): break
        widths.append(-2 * Ep.imag); wkbs.append(gamma_wkb(Ep.real, b))
        kap = np.sqrt(max(V1 - Ep.real, 0.0))
        seed = complex(Ep.real, Ep.imag * np.exp(-2 * kap * (bs[1] - bs[0])))
    bs = bs[: len(widths)]; widths = np.array(widths); wkbs = np.array(wkbs)
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    ax.semilogy(bs, widths, "o-", label=r"numerical $\Gamma$")
    ax.semilogy(bs, wkbs, "k--", label=r"$(k_{\rm in}/a)\,e^{-2b\sqrt{V_1-E_R}}$")
    ax.set(xlabel="b", ylabel=r"$\Gamma$", title="First resonance width vs barrier width")
    ax.legend(fontsize=9); ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "width_vs_b.png", dpi=140); plt.close(fig)
    return bs, widths, wkbs

def sanity_checks(Ep):
    rng = np.random.default_rng(2)
    for _ in range(6):
        E = rng.uniform(0.2, V1 - 0.2)
        assert abs(abs(S_matrix(E)) - 1.0) < 1e-9
    ER_p, half_p = Ep.real, -Ep.imag
    ER_b, half_b = bw_fit(ER_p, half_p)
    assert abs(ER_p - ER_b) < 1e-3, (ER_p, ER_b)
    assert abs(half_p - half_b) / half_p < 1e-2, (half_p, half_b)
    bs, widths, wkbs = fig_width_vs_b()
    ratio = widths[bs > 2.0] / wkbs[bs > 2.0]
    assert ((ratio > 0.5) & (ratio < 2.0)).all(), ratio
    print(f"sanity passed.\n  Newton: E_R={ER_p:.6f}, Γ={2*half_p:.4e}"
          f"\n  BW fit: E_R={ER_b:.6f}, Γ={2*half_b:.4e}\n"
          f"  Γ_num/Γ_WKB on b>2: {ratio}")

if __name__ == "__main__":
    Ep = newton_pole(seed_real(B))
    sanity_checks(Ep)
    fig_potential(Ep); fig_transmission(Ep); fig_pole_plane(Ep)
    print(f"  pole: E={Ep:.6f}\nfigures written to {ASSETS}")
