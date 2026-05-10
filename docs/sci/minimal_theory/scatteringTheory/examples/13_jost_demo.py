"""Jost function numerical demos. Units hbar=1, 2mu=1, E=k^2, l=0, R=1.

Demo 1: square well   F0+(k) = e^{ikR}[cos(KR) - i(k/K)sin(KR)], K=sqrt(k^2+V0)
Demo 2: Yamaguchi     F0+(k) = 1 - lambda * I(k^2),  I = -1/[8 pi beta (beta-ik)^2]
Demo 3: delta-shell   D(k) = kR + gamma sin(kR) e^{ikR}  (Jost-equivalent, same zeros)
Demo 4: Levinson      delta_0(0) - delta_0(inf) = n_0 pi  (square well)
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ASSETS = Path(__file__).parent / "assets" / "13_jost_demo"
ASSETS.mkdir(parents=True, exist_ok=True)
R = 1.0


# ---------- Demo 1: square well ----------
def F0_well(k, V0):
    K = np.sqrt(k * k + V0 + 0j)
    return np.exp(1j * k * R) * (np.cos(K * R) - 1j * (k / K) * np.sin(K * R))


def well_kappas(V0):
    """+i-axis zeros: solve cos(KR) + (kappa/K) sin(KR) = 0, K=sqrt(V0-kappa^2)."""
    K0 = np.sqrt(V0)
    kap = np.linspace(1e-6, K0 - 1e-6, 8000)
    Ks = np.sqrt(V0 - kap ** 2)
    g = np.cos(Ks * R) + (kap / Ks) * np.sin(Ks * R)
    idx = np.where(np.diff(np.sign(g)) != 0)[0]
    out = []
    for i in idx:
        a, b = kap[i], kap[i + 1]
        for _ in range(80):
            m = 0.5 * (a + b)
            Km = np.sqrt(V0 - m ** 2)
            gm = np.cos(Km * R) + (m / Km) * np.sin(Km * R)
            if np.sign(gm) == np.sign(g[i]):
                a = m
            else:
                b = m
        out.append(0.5 * (a + b))
    return np.array(out)


def fig_square_well_F0():
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    k_real = np.linspace(0.01, 6.0, 800)
    kr = np.linspace(-3.5, 3.5, 240)
    ki = np.linspace(-2.0, 2.5, 220)
    KR, KI = np.meshgrid(kr, ki)
    for j, V0 in enumerate([1.0, 5.0, 12.0]):
        F = F0_well(k_real, V0)
        ax = axes[0, j]
        ax.plot(k_real, np.abs(F), "C0", label=r"$|F_0^+(k)|$")
        ax2 = ax.twinx()
        ax2.plot(k_real, -np.unwrap(np.angle(F)), "C3", lw=1)
        ax.set(xlabel="k", title=rf"$V_0={V0:g}$, $R={R:g}$")
        ax.set_ylabel(r"$|F_0^+(k)|$", color="C0")
        ax2.set_ylabel(r"$\delta_0(k)=-\arg F_0^+$", color="C3")
        ax.grid(alpha=0.3)

        Z = F0_well(KR + 1j * KI, V0)
        axb = axes[1, j]
        pcm = axb.pcolormesh(KR, KI, np.log10(np.abs(Z) + 1e-3),
                             shading="auto", cmap="viridis", vmin=-2, vmax=2)
        fig.colorbar(pcm, ax=axb, label=r"$\log_{10}|F_0^+|$")
        kappas = well_kappas(V0)
        for kap in kappas:
            axb.plot(0, kap, "r*", ms=14, mec="white", mew=0.6)
        axb.axhline(0, color="w", lw=0.4); axb.axvline(0, color="w", lw=0.4)
        axb.set(xlabel="Re k", ylabel="Im k",
                title=rf"complex-$k$, $n_0={len(kappas)}$ bound state(s)")
    fig.suptitle(r"Square-well Jost function $F_0^+(k)=e^{ikR}[\cos(KR)-i(k/K)\sin(KR)]$",
                 y=1.00)
    fig.tight_layout(); fig.savefig(ASSETS / "square_well_jost_F0.png", dpi=140)
    plt.close(fig)


# ---------- Demo 2: Yamaguchi separable ----------
def F0_yam(k, lam, beta):
    return 1.0 + lam / (8 * np.pi * beta * (beta - 1j * k) ** 2)


def yam_kappa(lam, beta):
    rhs = -lam / (8 * np.pi * beta)
    return np.sqrt(rhs) - beta if rhs > 0 and np.sqrt(rhs) > beta else None


def fig_yamaguchi_zero():
    beta = 1.0
    lams = np.linspace(-60.0, -5.0, 60)
    kaps = np.array([yam_kappa(l, beta) or np.nan for l in lams])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    ax = axes[0]
    m = np.isfinite(kaps)
    sc = ax.scatter(lams[m], kaps[m], c=lams[m], cmap="plasma", s=30)
    fig.colorbar(sc, ax=ax, label=r"$\lambda$")
    lam_c = -8 * np.pi * beta ** 3
    ax.axvline(lam_c, color="k", ls=":", lw=1, label=rf"$\lambda_c=-8\pi\beta^3={lam_c:.2f}$")
    ax.set(xlabel=r"$\lambda$", ylabel=r"$\kappa=\mathrm{Im}\, k_{\rm zero}$",
           title=r"Yamaguchi: bound-state $\kappa$ vs $\lambda$, $\beta=1$")
    ax.grid(alpha=0.3); ax.legend()

    ax2 = axes[1]
    lam_show = -30.0
    kr = np.linspace(-2.0, 2.0, 200); ki = np.linspace(-1.0, 1.5, 200)
    KR, KI = np.meshgrid(kr, ki)
    Z = F0_yam(KR + 1j * KI, lam_show, beta)
    pcm = ax2.pcolormesh(KR, KI, np.log10(np.abs(Z) + 1e-3),
                         shading="auto", cmap="viridis", vmin=-2, vmax=2)
    fig.colorbar(pcm, ax=ax2, label=r"$\log_{10}|F_0^+|$")
    kap = yam_kappa(lam_show, beta)
    ax2.plot(0, kap, "r*", ms=18, mec="white", mew=0.7,
             label=fr"zero at $i\kappa$, $\kappa={kap:.4f}$")
    ax2.axhline(0, color="w", lw=0.4); ax2.axvline(0, color="w", lw=0.4)
    ax2.set(xlabel="Re k", ylabel="Im k",
            title=rf"$|F_0^+(k)|$ at $\lambda={lam_show}$, $\beta={beta}$")
    ax2.legend()
    fig.tight_layout(); fig.savefig(ASSETS / "yamaguchi_jost_zero.png", dpi=140)
    plt.close(fig)


# ---------- Demo 3: delta-shell ----------
def D_shell(k, gamma):
    return k * R + gamma * np.sin(k * R) * np.exp(1j * k * R)


def newton_shell(k0, gamma, tol=1e-12, itmax=80):
    k = complex(k0)
    for _ in range(itmax):
        s, c = np.sin(k * R), np.cos(k * R)
        e = np.exp(1j * k * R)
        f = k * R + gamma * s * e
        df = R + gamma * R * (c + 1j * s) * e
        dk = f / df; k -= dk
        if abs(dk) < tol:
            break
    return k


def fig_delta_shell_zeros():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    ax = axes[0]
    gamma = 20.0
    kr = np.linspace(0.05, 8.0, 320); ki = np.linspace(-1.6, 0.6, 220)
    KR, KI = np.meshgrid(kr, ki)
    Z = D_shell(KR + 1j * KI, gamma)
    pcm = ax.pcolormesh(KR, KI, np.log10(np.abs(Z) + 1e-3),
                        shading="auto", cmap="magma", vmin=-1, vmax=2)
    fig.colorbar(pcm, ax=ax, label=r"$\log_{10}|F_0^+|$")
    poles = [newton_shell(n * np.pi - 0.05 - 0.2j / n, gamma) for n in (1, 2, 3)]
    for n, kp in enumerate(poles, 1):
        ax.plot(kp.real, kp.imag, "c*", ms=14)
        ax.annotate(f"n={n}", (kp.real, kp.imag), xytext=(6, 6),
                    textcoords="offset points", color="cyan")
    ax.axhline(0, color="w", lw=0.4)
    ax.set(xlabel="Re k", ylabel="Im k",
           title=rf"Repulsive shell $\gamma=+{gamma:g}$: zeros in lower half (resonances)")

    ax2 = axes[1]
    gammas = np.linspace(-30.0, 50.0, 60)
    zeros = []
    for g in gammas:
        if g < -1.5:
            seed = 0.5j  # attractive: bound state on +i axis
        else:
            seed = np.pi - 0.05 - 0.3j / np.sqrt(abs(g) + 0.5)
        zeros.append(newton_shell(seed, g))
    zeros = np.array(zeros)
    sc = ax2.scatter(zeros.real, zeros.imag, c=gammas, cmap="coolwarm", s=40, zorder=3)
    fig.colorbar(sc, ax=ax2, label=r"$\gamma$")
    ax2.axhline(0, color="k", lw=0.4); ax2.axvline(0, color="k", lw=0.4)
    ax2.set(xlabel="Re k", ylabel="Im k",
            title=r"$n=1$ zero trajectory, $\gamma:-30\to 50$",
            xlim=(-0.5, 4.5), ylim=(-1.2, 1.5))
    ax2.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(ASSETS / "delta_shell_zeros.png", dpi=140)
    plt.close(fig)


# ---------- Demo 4: Levinson ----------
def fig_levinson_check():
    k = np.linspace(1e-3, 200.0, 40000)
    fig, ax = plt.subplots(figsize=(8.5, 5))
    for V0 in [1.0, 8.0, 25.0, 60.0]:
        d = -np.unwrap(np.angle(F0_well(k, V0)))
        d = d - np.round(d[-1] / np.pi) * np.pi  # anchor delta(inf)=0
        n_b = len(well_kappas(V0))
        diff = (d[0] - d[-1]) / np.pi
        ax.plot(k, d / np.pi,
                label=rf"$V_0={V0:g}$, $n_0={n_b}$, $\delta_0(0)-\delta_0(\infty)={diff:.2f}\pi$")
        ax.axhline(n_b, color="gray", lw=0.3, ls=":")
    ax.set(xlabel="k", ylabel=r"$\delta_0(k)/\pi$", xscale="log",
           title=r"Levinson: $\delta_0(0)-\delta_0(\infty)=n_0\pi$  (square well, $R=1$)")
    ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=9)
    fig.tight_layout(); fig.savefig(ASSETS / "levinson_check.png", dpi=140)
    plt.close(fig)


# ---------- sanity ----------
def sanity_checks():
    # (a) square-well V0=5: bound-state kappa
    V0 = 5.0
    kap = well_kappas(V0)[0]
    assert abs(F0_well(1j * kap, V0)) < 1e-6
    Vc = (np.pi / 2) ** 2  # critical V0 for 1st bound state, K0 R = pi/2
    kap_near = well_kappas(Vc + 0.05)[0]
    assert kap_near < 0.2, kap_near
    print(f"(a) V0={V0}: kappa={kap:.6f}, Eb={-kap**2:.4f}; "
          f"Vc={Vc:.4f}, kappa(Vc+0.05)={kap_near:.4f}")

    # (b) Yamaguchi: F0+(i kappa)=0 matches the closed-form kappa_b
    lam, beta = -30.0, 1.0
    kap_y = yam_kappa(lam, beta)
    kap_ref = np.sqrt(-lam / (8 * np.pi * beta)) - beta  # cf. 05_separable_rank1
    assert abs(kap_y - kap_ref) < 1e-12
    assert abs(F0_yam(1j * kap_y, lam, beta)) < 1e-12
    print(f"(b) Yamaguchi lam={lam},beta={beta}: kappa={kap_y:.6f} (ref {kap_ref:.6f})")

    # (c) Levinson V0=25 (n_0=2)
    V0 = 25.0
    n_b = len(well_kappas(V0))
    k = np.linspace(1e-3, 200.0, 40000)
    d = -np.unwrap(np.angle(F0_well(k, V0)))
    d = d - np.round(d[-1] / np.pi) * np.pi
    diff = (d[0] - d[-1]) / np.pi
    print(f"(c) V0=25 Levinson: n_b={n_b}, delta(0)-delta(inf) = {diff:.4f} pi")
    assert n_b == 2 and abs(diff - n_b) < 0.1
    print("sanity checks passed")


if __name__ == "__main__":
    sanity_checks()
    fig_square_well_F0()
    fig_yamaguchi_zero()
    fig_delta_shell_zeros()
    fig_levinson_check()
    print(f"figures written to {ASSETS}")
