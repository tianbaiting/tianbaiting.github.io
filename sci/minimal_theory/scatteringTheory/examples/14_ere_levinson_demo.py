"""ERE & Levinson numerical demos. Units hbar=1, 2mu=1, E=k^2, R=1.
Demos: (1) Wigner delta_l ~ k^{2l+1} for square well; (2) ERE fit k cot(delta_0)
vs k^2 on well/Yukawa/Yamaguchi; (3) Levinson delta_0(0)-delta_0(inf)=n_0 pi;
(4) unitary limit a_0(V0) at K_0 R = pi/2.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ASSETS = Path(__file__).parent / "assets" / "14_ere_levinson_demo"
ASSETS.mkdir(parents=True, exist_ok=True)
R = 1.0


# ---- Square-well closed forms (cf. 02_square_well_3d, 13_jost_demo) ----
def F0_well(k, V0):
    K = np.sqrt(k * k + V0 + 0j)
    return np.exp(1j * k * R) * (np.cos(K * R) - 1j * (k / K) * np.sin(K * R))

def delta0_well(k, V0):
    """Closed-form principal-branch delta_0."""
    K = np.sqrt(k * k + V0)
    return -k * R + np.arctan(k / K * np.tan(K * R))

def well_n0(V0):
    return int(np.floor(np.sqrt(V0) * R / np.pi + 0.5))

def a0_well(V0):
    K0 = np.sqrt(V0)
    return R * (1.0 - np.tan(K0 * R) / (K0 * R))


# ---- Numerov engine for arbitrary l (cf. 04_yukawa, 06_numerical_pipeline) ----
def numerov_phase_l(V_func, k, l=0, r_max=40.0, N=20000):
    """Solve u'' + [k^2 - V - l(l+1)/r^2] u = 0; return delta_l (principal branch)."""
    h = r_max / N
    r = np.linspace(h, r_max, N)
    f = k * k - V_func(r) - l * (l + 1) / (r * r)
    u = np.zeros(N); u[0] = r[0] ** (l + 1)
    u[1] = r[1] ** (l + 1) * (1.0 + h * h * f[0] / 6.0)
    c = h * h / 12.0
    for n in range(1, N - 1):
        u[n + 1] = (2 * u[n] * (1 - 5 * c * f[n])
                    - u[n - 1] * (1 + c * f[n - 1])) / (1 + c * f[n + 1])
    i1, i2 = N - 200, N - 100
    # Riccati-Bessel by upward recurrence: S_l = kr j_l, C_l = -kr y_l
    S, C = np.sin(k * r), -np.cos(k * r)
    if l >= 1:
        S, S_prev = np.sin(k * r) / (k * r) - np.cos(k * r), S
        C, C_prev = -np.cos(k * r) / (k * r) - np.sin(k * r), C
        for L_ in range(1, l):
            S, S_prev = (2 * L_ + 1) / (k * r) * S - S_prev, S
            C, C_prev = (2 * L_ + 1) / (k * r) * C - C_prev, C
    A1, B1, A2, B2 = S[i1], C[i1], S[i2], C[i2]
    num = u[i1] * A2 - u[i2] * A1
    den = u[i2] * B1 - u[i1] * B2
    return np.arctan(num / den)


# ---- Potentials & Yamaguchi closed-form (cf. 05_separable_rank1) ----
def V_well(r, V0=5.0):
    return -V0 * (r < R).astype(float)

def V_yukawa(r, V0=1.0, mu=1.0):
    rs = np.where(r > 1e-9, r, 1e-9)
    return -V0 * np.exp(-mu * rs) / (mu * rs)

def kcot_yam(k, lam=-30.0, beta=1.0):
    return -4 * np.pi * (beta ** 2 + k ** 2) ** 2 / lam + (k ** 2 - beta ** 2) / (2 * beta)

def a_re_yam(lam=-30.0, beta=1.0):
    return (1.0 / (4 * np.pi * beta ** 4 / lam + beta / 2.0),
            1.0 / beta - 16 * np.pi * beta ** 2 / lam)


# ---- Demo 1: Wigner threshold ----
def fig_wigner_threshold():
    V0 = 2.0  # below V_c = (pi/2)^2 = 2.467, no bound state, delta_l(0)=0
    k_arr = np.geomspace(0.01, 1.0, 24)
    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    fits = {}
    for l, c in zip([0, 1, 2], ["C0", "C1", "C2"]):
        d = np.array([numerov_phase_l(lambda r: V_well(r, V0), k, l=l,
                                      r_max=30.0, N=15000) for k in k_arr])
        ax.loglog(k_arr, np.abs(d), c + "o-", ms=5, label=fr"$l={l}$ (Numerov)")
        fits[l], _ = np.polyfit(np.log(k_arr[:10]), np.log(np.abs(d[:10])), 1)
        ref = np.abs(d[0]) * (k_arr / k_arr[0]) ** (2 * l + 1)
        ax.loglog(k_arr, ref, c + "--", lw=0.9, alpha=0.7,
                  label=fr"slope $2l+1={2*l+1}$ ref")
    txt = "Numerov fit slopes:\n" + "\n".join(
        fr"$l={l}$: {fits[l]:.3f}  (theory {2*l+1})" for l in (0, 1, 2))
    ax.text(0.04, 0.96, txt, transform=ax.transAxes, va="top", fontsize=9,
            bbox=dict(boxstyle="round", fc="white", ec="0.6", alpha=0.85))
    ax.set(xlabel=r"$k$", ylabel=r"$|\delta_l(k)|$",
           title=r"Wigner threshold $\delta_l\propto k^{2l+1}$  "
                 r"(square well $V_0=2,\,R=1$, $n_0=0$)")
    ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=8, loc="lower right")
    fig.tight_layout(); fig.savefig(ASSETS / "wigner_threshold.png", dpi=140)
    plt.close(fig)


# ---- Demo 2: ERE fit on three potentials ----
def _ere_panel(ax, k, kcot, color, title, data_label, extra=None):
    s, b = np.polyfit(k * k, kcot, 1)
    ax.plot(k * k, kcot, color + "o", ms=4, label=data_label)
    ax.plot(k * k, s * k * k + b, color + "-",
            label=fr"fit $a_0={-1/b:.3f},\ r_0={2*s:.3f}$")
    if extra: extra(ax)
    ax.set(xlabel=r"$k^2$", ylabel=r"$k\cot\delta_0$", title=title)
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

def fig_ere_fit_three():
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.4))
    V0, k = 2.0, np.linspace(0.05, 0.8, 30)
    a_th = a0_well(V0)
    _ere_panel(axes[0], k, k / np.tan(delta0_well(k, V0)), "C0",
               fr"Square well $V_0={V0}$", "closed form",
               lambda ax: ax.axhline(-1.0 / a_th, color="k", ls=":", lw=0.8,
                                     label=fr"exact $a_0={a_th:.3f}$"))
    V0_y, mu, k = 0.5, 1.0, np.linspace(0.05, 0.4, 24)
    d = np.array([numerov_phase_l(lambda r: V_yukawa(r, V0_y, mu), ki,
                                  r_max=40, N=18000) for ki in k])
    _ere_panel(axes[1], k, k / np.tan(d), "C1",
               fr"Yukawa $V_0={V0_y},\,\mu={mu}$", "Numerov")
    lam, beta, k = -30.0, 1.0, np.linspace(0.05, 0.5, 30)
    a_th2, r_th2 = a_re_yam(lam, beta)
    _ere_panel(axes[2], k, kcot_yam(k, lam, beta), "C2",
               fr"Yamaguchi $\lambda={lam},\,\beta={beta}$", "closed form",
               lambda ax: ax.text(0.04, 0.04,
                fr"analytic: $a_0={a_th2:.3f},\ r_0={r_th2:.3f}$" "\n"
                r"(ERE truncates at $k^2$)",
                transform=ax.transAxes, fontsize=9, va="bottom",
                bbox=dict(boxstyle="round", fc="white", ec="0.6", alpha=0.85)))
    fig.suptitle(r"ERE fit: $k\cot\delta_0=-1/a_0+r_0 k^2/2+\ldots$", y=1.02)
    fig.tight_layout(); fig.savefig(ASSETS / "ere_fit_three_potentials.png", dpi=140)
    plt.close(fig)


# ---- Demo 3: Levinson validation ----
def fig_levinson_validation():
    V0_list = [1.0, 2.5, 5.0, 12.0, 25.0]
    k = np.geomspace(1e-4, 50.0, 6000)
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.6),
                             gridspec_kw={"width_ratios": [2, 1]})
    rows = []
    for V0, c in zip(V0_list, ["C0", "C1", "C2", "C3", "C4"]):
        d = -np.unwrap(np.angle(F0_well(k, V0)))
        d = d - np.round(d[-1] / np.pi) * np.pi
        n0 = well_n0(V0); diff = (d[0] - d[-1]) / np.pi
        axes[0].plot(k, d / np.pi, c, lw=1.2, label=fr"$V_0={V0}$, $n_0={n0}$")
        rows.append((V0, n0, diff))
    for n in range(3):
        axes[0].axhline(n, color="gray", lw=0.3, ls=":")
    axes[0].set(xlabel=r"$k$", ylabel=r"$\delta_0(k)/\pi$", xscale="log",
                title=r"Levinson: $\delta_0(0)-\delta_0(\infty)=n_0\pi$  (square well)")
    axes[0].grid(alpha=0.3, which="both"); axes[0].legend(fontsize=9, loc="upper right")
    axes[1].axis("off")
    txt = (r"$V_0$    $n_0$    $\delta_0(0)-\delta_0(\infty)$" + "\n" + "-" * 36 + "\n"
           + "".join(f"{V0:>5.1f}   {n0}    {diff:>+6.3f} π\n" for V0, n0, diff in rows)
           + "\n" + r"thresholds  $V_{0,c}^{(n)}=((2n-1)\pi/2)^2$:" + "\n"
           + r"  $V_{0,c}^{(1)}=2.467$" + "\n" + r"  $V_{0,c}^{(2)}=22.21$")
    axes[1].text(0.0, 0.98, txt, family="monospace", fontsize=10, va="top",
                 transform=axes[1].transAxes)
    fig.tight_layout(); fig.savefig(ASSETS / "levinson_validation.png", dpi=140)
    plt.close(fig)


# ---- Demo 4: Unitary limit ----
def fig_unitary_limit():
    Vc = (np.pi / 2) ** 2
    V0_arr = np.linspace(0.05, 6.0, 4000); a_arr = np.array([a0_well(V) for V in V0_arr])
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(V0_arr, np.where(np.abs(a_arr) < 30, a_arr, np.nan),
            "C0-", lw=1.4, label=r"$a_0=R[1-\tan(K_0 R)/(K_0 R)]$")
    ax.axvline(Vc, color="r", ls="--", lw=1, label=fr"$V_0^*=(\pi/2)^2={Vc:.3f}$")
    ax.axhline(0, color="k", lw=0.4)
    ax.set(xlabel=r"$V_0$ (with $R=1$)", ylabel=r"$a_0(V_0)$", ylim=(-25, 25),
           title=r"Unitary limit: $a_0\to\pm\infty$ at $K_0R=\pi/2$ (first bound state threshold)")
    ax.legend(loc="lower left"); ax.grid(alpha=0.3)
    axin = ax.inset_axes([0.58, 0.62, 0.38, 0.34])
    axin.plot(V0_arr, 1.0 / a_arr, "C2-", lw=1.0)
    axin.axvline(Vc, color="r", ls="--", lw=0.8); axin.axhline(0, color="k", lw=0.4)
    axin.set(xlim=(1.5, 4.0), ylim=(-1.5, 1.5), xlabel=r"$V_0$", ylabel=r"$1/a_0$")
    axin.grid(alpha=0.3); axin.set_title(r"$1/a_0=0$ at $V_0=V_0^*$", fontsize=9)
    fig.tight_layout(); fig.savefig(ASSETS / "unitary_limit.png", dpi=140); plt.close(fig)


# ---- sanity ----
def sanity_checks():
    V0 = 2.0; k_arr = np.geomspace(0.005, 0.05, 12)
    for l in (0, 1, 2):
        d = np.array([numerov_phase_l(lambda r: V_well(r, V0), k, l=l,
                                      r_max=30.0, N=15000) for k in k_arr])
        slope, _ = np.polyfit(np.log(k_arr), np.log(np.abs(d)), 1)
        assert abs(slope - (2 * l + 1)) < 0.05, f"Wigner l={l}: slope={slope:.3f}"
        print(f"(a) Wigner l={l}: slope={slope:.4f} (theory {2*l+1})")
    k = np.linspace(0.02, 0.4, 30)
    kcot = k / np.tan(delta0_well(k, V0))
    s, b = np.polyfit(k * k, kcot, 1)
    a_fit, a_th = -1.0 / b, a0_well(V0)
    assert abs(a_fit - a_th) < 1e-2
    print(f"(b) Square well V0=2: a_fit={a_fit:.5f}, a_exact={a_th:.5f}, "
          f"|diff|={abs(a_fit-a_th):.2e}")
    V0 = 25.0; k = np.geomspace(1e-4, 50.0, 6000)
    d = -np.unwrap(np.angle(F0_well(k, V0)))
    d = d - np.round(d[-1] / np.pi) * np.pi
    n0 = well_n0(V0); diff = (d[0] - d[-1]) / np.pi; rel = abs(diff - n0) / n0
    assert n0 == 2 and rel < 0.05
    print(f"(c) Levinson V0=25: n_0={n0}, delta(0)-delta(inf)={diff:.4f} pi "
          f"(rel err {rel:.2%})")
    print("sanity checks passed")


if __name__ == "__main__":
    sanity_checks()
    fig_wigner_threshold(); fig_ere_fit_three()
    fig_levinson_validation(); fig_unitary_limit()
    print(f"figures written to {ASSETS}")
