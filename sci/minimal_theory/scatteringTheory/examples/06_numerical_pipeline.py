"""Unified s-wave numerical pipeline.

Two engines:
  1. numerov_swave(V_local, k)  — coordinate space, takes V(r), returns δ_0
  2. ls_swave(V_l_pp, E)         — momentum space, takes V_l(p,p'), returns T_l(k,k;E), then δ_0

Apply to: square well, delta shell (smoothed), Yukawa, Yamaguchi.
Compare numerical against analytic results from prior articles.

Convention: ℏ=1, 2m=1.  LS measure follows 05_separable_rank1.py.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ASSETS = Path(__file__).parent / "assets" / "06_numerical_pipeline"
ASSETS.mkdir(parents=True, exist_ok=True)


# ------------------ Engine 1: Numerov in coordinate space ------------------

def numerov_swave(V_local, k, r_max=40.0, N=20000):
    """Solve u'' + [k² - V(r)] u = 0 with u(0)=0; return δ_0(k) by 2-point match."""
    h = r_max / N
    r = np.linspace(0.0, r_max, N + 1)
    f = k * k - V_local(r)
    u = np.zeros(N + 1)
    u[1] = h
    h2 = h * h / 12
    for n in range(1, N):
        u[n + 1] = (2 * u[n] * (1 - 5 * h2 * f[n])
                    - u[n - 1] * (1 + h2 * f[n - 1])) / (1 + h2 * f[n + 1])
    n2 = N
    n1 = N - max(2, int(0.25 * np.pi / (k * h)))
    r1, r2 = r[n1], r[n2]
    u1, u2 = u[n1], u[n2]
    K = u1 * np.sin(k * r2) - u2 * np.sin(k * r1)
    L = u2 * np.cos(k * r1) - u1 * np.cos(k * r2)
    return np.arctan2(K, L)


# ------------------ Engine 2: momentum-space LS solver ------------------

def ls_swave(V_l_pp, E, N=128, qmax=30.0):
    """Solve s-wave LS in momentum space using Sloan / Kowalski subtraction.

    Convention:
        T(p,p';E) = V(p,p') + ∫ dq q²/(2π²) V(p,q) T(q,p';E) / (E - q² + i0)

    Augment the Gauss grid with k0 = √E as the last node; treat the singularity
    by principal-value subtraction plus the imaginary residue −iπk0/2.
    """
    if E <= 0:
        raise ValueError("on-shell solver requires E > 0")
    k0 = np.sqrt(E)
    x, w = np.polynomial.legendre.leggauss(N)
    q = 0.5 * qmax * (x + 1)
    wq = 0.5 * qmax * w
    pv_tail = -qmax + 0.5 * k0 * np.log((qmax + k0) / (qmax - k0))
    u_eff = np.zeros(N + 1, dtype=complex)
    u_eff[:N] = wq * q ** 2 / (E - q ** 2)
    u_eff[N] = pv_tail - 1j * np.pi * k0 / 2 - np.sum(u_eff[:N].real)
    u_eff /= 2 * np.pi ** 2
    q_aug = np.concatenate([q, [k0]])
    Vmat = V_l_pp(q_aug[:, None], q_aug[None, :])
    M = np.eye(N + 1, dtype=complex) - Vmat * u_eff[None, :]
    rhs = Vmat[:, N]
    T_aug = np.linalg.solve(M, rhs)
    return T_aug[N]


def delta_from_T(T_on, k):
    """δ_0 ∈ (0, π) via k cot δ.

    With LS measure 1/(2π²): T = -4π e^{iδ} sin δ / k, so
    k cot δ = -4π Re(1/T).  Use arctan2(k, kc) for stable Levinson branch.
    """
    kc = -4 * np.pi * (1.0 / T_on).real
    return np.arctan2(k, kc)


# ------------------ Potential providers ------------------

def square_well(r, V0=5.0, R=1.0):
    return -V0 * (r < R).astype(float)


def square_well_delta(k, V0=5.0, R=1.0):
    K = np.sqrt(k * k + V0)
    return np.arctan2(k * np.sin(K * R), K * np.cos(K * R)) - k * R


def delta_shell_smoothed(r, gamma=20.0, R=1.0, sigma=0.015):
    return (gamma / R) * np.exp(-(r - R) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))


def delta_shell_delta(k, gamma=20.0, R=1.0):
    num = -gamma * np.sin(k * R) ** 2
    den = k * R + gamma * np.sin(k * R) * np.cos(k * R)
    return np.arctan2(num, den)


def yukawa(r, V0=1.0, mu=1.0):
    rsafe = np.where(r > 1e-9, r, 1e-9)
    return -V0 * np.exp(-mu * rsafe) / (mu * rsafe)


def yukawa_born_delta(k, V0=1.0, mu=1.0):
    return V0 / (4 * k * mu) * np.log(1 + 4 * k * k / (mu * mu))


def yamaguchi_V(p, pp, lam=-30.0, beta=1.0):
    return lam / ((p * p + beta ** 2) * (pp * pp + beta ** 2))


def yamaguchi_delta(k, lam=-30.0, beta=1.0):
    kc = -4 * np.pi * (beta ** 2 + k ** 2) ** 2 / lam + (k ** 2 - beta ** 2) / (2 * beta)
    return np.arctan2(k, kc)


# ------------------ Plots ------------------

def fig_delta0_unified():
    k = np.linspace(0.10, 4.0, 70)
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))

    ax = axes[0, 0]
    d_an = np.unwrap([square_well_delta(ki, 5.0, 1.0) for ki in k])
    d_nm = np.unwrap([numerov_swave(lambda r: square_well(r, 5.0, 1.0), ki, r_max=20) for ki in k])
    ax.plot(k, d_an, "b-", lw=2, label="analytic")
    ax.plot(k, d_nm, "r--", lw=1.2, label="Numerov")
    ax.set_title("square well  $V_0=5,\\ R=1$")

    ax = axes[0, 1]
    d_an = np.unwrap([delta_shell_delta(ki, 20.0, 1.0) for ki in k])
    d_nm = np.unwrap([numerov_swave(
        lambda r: delta_shell_smoothed(r, 20.0, 1.0, 0.015), ki, r_max=8, N=40000) for ki in k])
    ax.plot(k, d_an, "b-", lw=2, label="analytic")
    ax.plot(k, d_nm, "r--", lw=1.2, label="Numerov (σ=0.015)")
    ax.set_title("delta shell  $\\gamma=20,\\ R=1$")

    ax = axes[1, 0]
    d_nm = [numerov_swave(lambda r: yukawa(r, 1.0, 1.0), ki, r_max=30) for ki in k]
    d_born = yukawa_born_delta(k, 1.0, 1.0)
    ax.plot(k, d_nm, "r-", lw=2, label="Numerov (exact)")
    ax.plot(k, d_born, "g--", lw=1.2, label="Born")
    ax.set_title("Yukawa  $V_0=1,\\ \\mu=1$")

    ax = axes[1, 1]
    d_an = yamaguchi_delta(k, -30.0, 1.0)
    d_ls = []
    for ki in k:
        T_on = ls_swave(lambda p, pp: yamaguchi_V(p, pp, -30.0, 1.0), ki ** 2, N=96)
        d_ls.append(delta_from_T(T_on, ki))
    d_ls = np.array(d_ls)
    # convention factor: separable LS gives δ that may need adjustment
    ax.plot(k, d_an, "b-", lw=2, label="analytic")
    ax.plot(k, d_ls, "r--", lw=1.2, label="LS solver")
    ax.set_title("Yamaguchi separable  $\\lambda=-30,\\ \\beta=1$")

    for ax in axes.flat:
        ax.set_xlabel("$k$")
        ax.set_ylabel(r"$\delta_0(k)$")
        ax.legend()
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(ASSETS / "delta0_unified.png", dpi=140)
    plt.close(fig)


def fig_convergence():
    k = 1.5
    Ns = [200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    err_sq, err_yk = [], []
    ref_sq = square_well_delta(k, 5.0, 1.0)
    ref_yk = numerov_swave(lambda r: yukawa(r, 1.0, 1.0), k, r_max=30, N=200000)
    for N in Ns:
        d_sq = numerov_swave(lambda r: square_well(r, 5.0, 1.0), k, r_max=20, N=N)
        d_yk = numerov_swave(lambda r: yukawa(r, 1.0, 1.0), k, r_max=30, N=N)
        err_sq.append(abs(d_sq - ref_sq))
        err_yk.append(abs(d_yk - ref_yk))
    fig, ax = plt.subplots(figsize=(7, 5))
    Na = np.array(Ns, float)
    ax.loglog(Ns, err_sq, "o-", label="square well (V discontinuous)")
    ax.loglog(Ns, err_yk, "s-", label="Yukawa (V smooth)")
    ax.loglog(Na, 5e2 / Na ** 2, "k:", alpha=0.5, label=r"$\propto 1/N^2$")
    ax.loglog(Na, 1e3 / Na ** 4, "k--", alpha=0.5, label=r"$\propto 1/N^4$")
    ax.set_xlabel("N (grid points)")
    ax.set_ylabel(r"$|\delta_0 - \delta_0^{\rm ref}|$")
    ax.set_title(f"Numerov convergence  ($k={k}$)")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(ASSETS / "convergence.png", dpi=140)
    plt.close(fig)


def fig_ls_engine():
    """Verify LS solver against Yamaguchi closed form."""
    k = np.linspace(0.10, 4.0, 80)
    d_an = yamaguchi_delta(k, -30.0, 1.0)
    d_ls = []
    for ki in k:
        T_on = ls_swave(lambda p, pp: yamaguchi_V(p, pp, -30.0, 1.0), ki ** 2, N=128)
        d_ls.append(delta_from_T(T_on, ki))
    d_ls = np.array(d_ls)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    axes[0].plot(k, d_an, "b-", lw=2, label="analytic")
    axes[0].plot(k, d_ls, "r--", lw=1.2, label="LS solver  N=128")
    axes[0].set_xlabel("$k$"); axes[0].set_ylabel(r"$\delta_0(k)$")
    axes[0].set_title("Yamaguchi separable")
    axes[0].legend(); axes[0].grid(alpha=0.3)
    axes[1].semilogy(k, np.abs(d_ls - d_an) + 1e-16, "k-")
    axes[1].set_xlabel("$k$"); axes[1].set_ylabel(r"$|\delta_0^{\rm LS} - \delta_0^{\rm an}|$")
    axes[1].set_title("LS solver residual")
    axes[1].grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(ASSETS / "ls_engine.png", dpi=140)
    plt.close(fig)


def sanity_checks():
    k = 1.5
    d_an = square_well_delta(k, 5.0, 1.0)
    d_nm = numerov_swave(lambda r: square_well(r, 5.0, 1.0), k, r_max=20, N=20000)
    assert abs(d_nm - d_an) < 1e-3, f"square well: an={d_an} nm={d_nm}"

    d_an = delta_shell_delta(k, 20.0, 1.0)
    d_nm = numerov_swave(
        lambda r: delta_shell_smoothed(r, 20.0, 1.0, 0.01), k, r_max=8, N=80000)
    assert abs(d_nm - d_an) < 0.05, f"delta shell: an={d_an} nm={d_nm}"

    d_an = yamaguchi_delta(k, -30.0, 1.0)
    T_on = ls_swave(lambda p, pp: yamaguchi_V(p, pp, -30.0, 1.0), k * k, N=128)
    d_ls = delta_from_T(T_on, k)
    assert abs(d_ls - d_an) < 1e-3, f"yamaguchi: an={d_an} ls={d_ls}"
    print("sanity checks passed")


if __name__ == "__main__":
    sanity_checks()
    fig_delta0_unified()
    fig_convergence()
    fig_ls_engine()
    print(f"figures written to {ASSETS}")
