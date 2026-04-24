---
title: Deuteron polarization measurement and polarization-axis determination
tag:
    - polarization
    - polarimeter
    - isovector
    - spin precession
---

This page organizes the derivations and monitoring scheme of deuteron polarization measurement and polarized scattering as presented in the isovector reorientation paper (*Simulation studies of the isovector reorientation effect of deuteron scattering on heavy target*), and adds two further sections on top: (1) spin precession of the beam when passing through magnetic elements; (2) placing polarimeters at different beam-line positions to determine the polarization axis.

## 1. Experimental background

The paper aims to measure the reorientation effect induced by the isovector potential when a 190 MeV/u polarized deuteron beam scatters on heavy targets ($^{112}$Sn, $^{124}$Sn, $^{208}$Pb) and breaks up, at the SAMURAI spectrometer of RIKEN Nishina Center. The effect requires the tensor polarization of the deuteron beam to be known and stable, so a dedicated polarimeter is placed upstream of the target to monitor the tensor polarization on-line via $p(\vec{d},d)p$ elastic scattering.

The reason for using a polarized beam is that, without polarization, the azimuthal anisotropy of the neutron–proton angular distribution after breakup averages out under the random orientation of the spin, and the IVR effect becomes unobservable.

## 2. Definition of tensor polarization

The deuteron is a spin-1 nucleus. Its polarization state is characterized by the spin density operator $\hat{\rho}$. For a spin-1 system, $\hat{\rho}$ is a $3\times 3$ Hermitian matrix that simultaneously carries vector and tensor polarization information.

In the Cartesian basis (see Ohlsen 1972), the density matrix can be expanded as

$$
\hat{\rho} = \frac{1}{3}\left\{ I + \frac{3}{2}\sum_i p_i \mathscr{P}_i + \frac{2}{3}\sum_{i\neq j} p_{ij}\mathscr{P}_{ij} + \frac{1}{3}\sum_i p_{ii}\mathscr{P}_{ii} \right\}
$$

where $\mathscr{P}_i = S_i$ is the vector polarization operator, $\mathscr{P}_{ij} = 3 S_i S_j - 2I$ is the tensor polarization operator, and $p_i$ and $p_{ij}$ are the corresponding polarization components. Because

$$
\mathscr{P}_{xx} + \mathscr{P}_{yy} + \mathscr{P}_{zz} = 0,
$$

the three diagonal tensor components are not independent; in experiments one typically takes $p_{z'z'}$ or $p_{y'y'}$ as the monitored observable.

Experiments use the beam frame $S'$: the $z'$ axis is along the incident direction $\vec{k}_\text{in}$, and the $y'$ axis points upward. The ideal tensor-polarized states are $p_{z'z'}=1$ (longitudinal polarization) or $p_{y'y'}=1$ (vertical polarization).

## 3. Polarized differential scattering cross section

The final-state density matrix is related to the initial one via $\hat{\rho}_f = M\hat{\rho}_i M^\dagger$. Define the analyzing powers

$$
A_i = \frac{\operatorname{Tr}(M\mathscr{P}_i M^\dagger)}{\operatorname{Tr}(MM^\dagger)}, \qquad A_{ij} = \frac{\operatorname{Tr}(M\mathscr{P}_{ij} M^\dagger)}{\operatorname{Tr}(MM^\dagger)}.
$$

The differential cross section for a polarized beam is then

$$
\sigma = \sigma_0(\theta)\left\{ 1 + \frac{3}{2}\sum_i p_i A_i + \frac{1}{3}\sum_{ij} p_{ij} A_{ij} \right\}
$$

with $\sigma_0(\theta) = \tfrac{1}{3}\operatorname{Tr}(MM^\dagger)$ the unpolarized differential cross section.

Using parity conservation (requiring $N_x + N_z$ to be even) and the coordinate transformation between the beam frame $S'$ and the scattering frame $S$, this reduces to the Ohlsen form:

$$
\begin{aligned}
\frac{\sigma(\theta,\phi)}{\sigma_0(\theta)} = 1 &+ \frac{3}{2}(p_{x'}\sin\phi + p_{y'}\cos\phi) A_y(\theta) \\
&+ \frac{2}{3}(p_{x'z'}\cos\phi - p_{y'z'}\sin\phi) A_{xz}(\theta) \\
&+ \frac{1}{6}\big[(p_{x'x'}-p_{y'y'})\cos 2\phi - 2 p_{x'y'}\sin 2\phi\big]\big[A_{xx}(\theta)-A_{yy}(\theta)\big] \\
&+ \frac{1}{2}p_{z'z'} A_{zz}(\theta).
\end{aligned}
$$

## 4. LRUD four-detector scheme

Place four detectors at the same polar angle $\theta$ and azimuthal angles $\phi = 0^\circ,90^\circ,180^\circ,270^\circ$, labeled L, U, R, D respectively. Substituting into the formula above gives

$$
\begin{aligned}
\sigma_L &= \sigma_0\Big\{1 + \tfrac{3}{2}p_{y'}A_y + \tfrac{2}{3}p_{x'z'}A_{xz} + \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_R &= \sigma_0\Big\{1 - \tfrac{3}{2}p_{y'}A_y - \tfrac{2}{3}p_{x'z'}A_{xz} + \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_U &= \sigma_0\Big\{1 - \tfrac{3}{2}p_{x'}A_y + \tfrac{2}{3}p_{y'z'}A_{xz} - \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}, \\
\sigma_D &= \sigma_0\Big\{1 + \tfrac{3}{2}p_{x'}A_y - \tfrac{2}{3}p_{y'z'}A_{xz} - \tfrac{1}{6}(p_{x'x'}-p_{y'y'})(A_{xx}-A_{yy}) + \tfrac{1}{2}p_{z'z'}A_{zz}\Big\}.
\end{aligned}
$$

### 4.1 Monitoring $p_{y'y'}$ (existing method)

Following Bieber 2001, define the left-right-up-down count asymmetry

$$
R_{LRUD} = \frac{N_L + N_R - N_U - N_D}{N_L + N_R + N_U + N_D} = \frac{p_{y'y'}(A_{xx}-A_{yy})}{2 p_{y'y'} A_{zz} - 4},
$$

which inverts to

$$
p_{y'y'} = \frac{R_{LRUD}}{\tfrac{1}{2}A_{zz} R_{LRUD} - \tfrac{1}{4}(A_{xx}-A_{yy})}.
$$

### 4.2 Monitoring $p_{z'z'}$ (proposed in this work)

The four-detector average cross section

$$
\bar{\sigma} = \frac{\sigma_L + \sigma_R + \sigma_U + \sigma_D}{4} = \sigma_0\left(1 + \tfrac{1}{2}p_{z'z'} A_{zz}\right),
$$

gives $p_{z'z'}$ directly from $\bar{\sigma}$ if $A_{zz}$ is known. To cancel systematic factors from beam intensity and target thickness, one takes the ratio of $\bar{\sigma}$ at two polar angles $\theta_1$ and $\theta_2$: the common normalization drops out and only the $\sigma_0$ and $A_{zz}$ combinations at the two angles remain.

## 5. Polarimeter design and simulation results

Detector scheme: $p(\vec{d},d)p$ elastic scattering with a CH$_2$ target of thickness $1000\,\text{mg/cm}^2$, beam current $1.6\times 10^{-3}$ pnA (i.e. $10^7$ pps). The two recoil-proton angles are $\theta_1 = 55.9^\circ$ and $\theta_2 = 11.3^\circ$, both 600 mm from the target, with roughly $20\times 20\,\text{mm}^2$ acceptance. A $50\times 40\,\text{mm}^2$ deuteron detector is placed at $\theta = 20.87^\circ$, 500 mm from the target.

Analyzing powers are taken from the public $d$–$p$ elastic scattering data of Sekiguchi et al.

GEANT4 simulation results:

- The four azimuthal detectors at $\theta_1$ accumulate $\sim 10^5$ events in 30 min;
- The two-angle count ratio vs $p_{zz}$ (Fig. Ratio_vs_pzz) and $R_{LRUD}$ vs $p_{y'y'}$ (Fig. R\_LRUD\_vs\_pyy) both show that the statistical error is far smaller than the $\sim 10\%$ tensor-polarization resolution required;
- Thus this polarimeter can monitor $p_{z'z'}$ and $p_{y'y'}$ to a relative precision of $\sim 10\%$.

## 6. Spin precession in magnetic fields

A polarimeter reading only gives the polarization components "at that location." To connect it with the beam source (polarized ion source and Wien filter) and the target, one must track the spin precession through the accelerator and transport line.

### 6.1 The deuteron g-factor

The deuteron g-factor is $g_d \approx 0.8574$. Define the anomalous magnetic moment factor

$$
G = \frac{g - 2}{2}.
$$

For the deuteron, $G_d \approx -0.1430$.

### 6.2 Thomas–BMT precession

In a pure magnetic field, the relativistic Thomas–BMT equation governs the spin precession about the magnetic field. For a particle bent in a vertical magnetic field, the extra spin rotation relative to the momentum direction is

$$
\theta_\text{spin} - \theta_\text{bend} = G\gamma\, \theta_\text{bend},
$$

so the spin tune (extra turns of spin relative to momentum per revolution) is $G\gamma$.

For 190 MeV/u deuterons, $\gamma = 1 + T/(m_u c^2) = 1.204$, giving

$$
G\gamma \approx -0.172.
$$

Every horizontal dipole (geometric bending angle $\theta_B$) rotates the in-plane polarization direction by an additional $G\gamma\,\theta_B$ relative to the momentum. The difference between longitudinal $p_{z'z'}$ and vertical $p_{y'y'}$ is:

- Vertical polarization ($y'$) is parallel to the field and is not rotated by Thomas–BMT to leading order, only preserved;
- Longitudinal polarization ($z'$) lies in the horizontal plane and rotates by $G\gamma\,\theta_B$ relative to the momentum, so any horizontal dipole between the ion source and the target alters "the polarization-axis direction seen at the polarimeter."

### 6.3 Wien filter

The RIKEN scheme places a Wien filter (crossed electric and magnetic fields) at the front end of the accelerator. Inside the Wien filter the particle trajectory is not deflected, but the spin can be rotated to any desired direction. This allows the source to prepare the polarization axis along any target direction (any of $x$, $y$, $z$ or any combination). The Wien filter setting must be validated against downstream polarimeter readings to guarantee that the axis at the target matches the design.

### 6.4 Spin preservation through single-turn cyclotron extraction

The single-turn extraction of the three cyclotrons (AVF, RRC, SRC) ensures that the polarization amplitude is not reduced by the cancellation of multi-turn contributions, so the extracted polarization still retains $\sim 80\%$ of its theoretical value.

## 7. Determining the polarization axis with polarimeters at multiple positions

If a polarimeter is placed at only one point of the beam line, the L/R/U/D counts give certain combinations of the $p_{i'j'}$ components at that point (see §4), but the 3D direction of the polarization axis $\hat{S}$ cannot be fully determined. The reason is that at a single point the degrees of freedom are limited: for example $R_{LRUD}$ alone cannot simultaneously resolve $(\beta,\phi)$.

### 7.1 Cross section for an arbitrary polarization axis

Parameterize the axis by spherical angles $(\beta,\phi)$. For a pure tensor polarization $P_{zz}$ (Ohlsen rotation rule, see `spherical_operator.md` on this site), the beam-frame components are

$$
\begin{aligned}
p_{xx} &= \tfrac{1}{2}(3\sin^2\beta\sin^2\phi - 1)P_{zz}, \\
p_{yy} &= \tfrac{1}{2}(3\sin^2\beta\cos^2\phi - 1)P_{zz}, \\
p_{zz} &= \tfrac{1}{2}(3\cos^2\beta - 1)P_{zz}, \\
p_{xy} &= -\tfrac{3}{2}\sin^2\beta\sin\phi\cos\phi\, P_{zz}, \\
p_{yz} &= \sin\beta\cos\beta\cos\phi\, P_{zz}, \\
p_{xz} &= -\sin\beta\cos\beta\sin\phi\, P_{zz}.
\end{aligned}
$$

The corresponding LRUD asymmetries become

$$
\begin{aligned}
\frac{2(L-R)}{L+R+U+D} &= \frac{\tfrac{3}{2}P_z\sin\beta A_y}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}, \\
\frac{2(U-D)}{L+R+U+D} &= \frac{P_{zz}\sin\beta\cos\beta A_{xz}}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}, \\
\frac{(L+R) - (U+D)}{L+R+U+D} &= \frac{-\tfrac{1}{4}P_{zz}\sin^2\beta(A_{xx}-A_{yy})}{1 + \tfrac{1}{2}P_{zz}(3\cos^2\beta - 1)A_{zz}}.
\end{aligned}
$$

These three observables are functions of $(P_z,P_{zz},\beta,\phi)$, but the $\sin\beta$/$\cos\beta$ branches and the $\phi \leftrightarrow \phi + \pi$ symmetry prevent single-point LRUD from uniquely inverting the 3D direction of $\hat{S}$.

### 7.2 Multi-position polarimeter scheme

Place a polarimeter before and after a magnetic element along the beam line (denoted $P_1$ and $P_2$), with the beam in between passing through a known field $B$ and a known geometric bending angle $\theta_B$. By §6.2 the in-plane polarization-axis rotates by $\Delta\phi_s = G\gamma\,\theta_B$ relative to the momentum between the two points.

If the polarization-axis spherical angles at $P_1$ are $(\beta,\phi_1)$, then in the $P_2$ beam frame they are

$$
(\beta,\phi_2) = (\beta,\phi_1 + G\gamma\,\theta_B).
$$

(The vertical component $\cos\beta$ is not affected by a horizontal dipole, so $\beta$ is invariant at leading order.)

The six independent asymmetries from the two polarimeters (three per device) form an over-determined system for the four unknowns $(P_z, P_{zz}, \beta, \phi_1)$. A least-squares or $\chi^2$ fit simultaneously resolves

1. the vector polarization magnitude $P_z$;
2. the tensor polarization magnitude $P_{zz}$;
3. the polar angle $\beta$ of the polarization axis;
4. the azimuthal angle $\phi_1$ (and hence $\phi_2$).

### 7.3 Why an intermediate magnetic field is essential

If the two polarimeters are separated by only drift space, the spin direction does not change between them; the two readings are equivalent and carry no additional information. A known precession $\Delta\phi_s$ is required to lift the degeneracy between the $(\beta,\phi)$ components. This is the physical essence of "using spin precession + multi-position polarimeters to determine the polarization axis."

Three common choices of intermediate magnet in practice:

- A dipole already present in the beam line: $\theta_B$ is geometrically known and $G\gamma\,\theta_B$ is directly available;
- A dedicated spin rotator (Wien filter, solenoid): $\Delta\phi_s$ can be scanned programmatically for calibration;
- An upstream solenoid: rotates the axis from $z'$ to $y'$ or any combination, and combined with the two polarimeters enables systematic calibration.

### 7.4 Practical layout suggestions

A minimal configuration for the IVR experiment could be:

1. Install a polarimeter before and after a dipole along the RRC→SRC bypass beam line (or reuse existing dPol / BigDpol hardware);
2. Configure the polarimeter with the LRUD + two-angle ($\theta_1,\theta_2$) combination proposed in the paper, monitoring both $p_{y'y'}$ and $p_{z'z'}$;
3. Fit $(P_z,P_{zz},\beta,\phi)$ using the six asymmetries from both polarimeters, and feed the result back to the source-end Wien filter for closed-loop control;
4. Use the target-upstream polarimeter for the final values; the IVR analysis uses the measured $p_{z'z'}$ / $p_{y'y'}$ at the target as ground truth.

This preserves the sensitivity of the "single-point LRUD + two-angle" scheme demonstrated in the paper, and additionally promotes the polarization-axis direction into an observable, so that the experiment can verify in real time that the Wien filter operates at the intended setting.

## 8. Combined vector and tensor polarization

Section 7 assumed the beam carries only tensor polarization ($P_{zz}$, with $P_z = 0$). A real RIKEN polarized ion source produces superpositions of RF-transition states and generally carries both vector polarization $P_z$ and tensor polarization $P_{zz}$. Together with the axis $(\beta,\phi)$ this gives **four unknowns** $(P_z, P_{zz}, \beta, \phi)$.

### 8.1 Full polarization components

The vector polarization along $(\beta,\phi)$ in the beam frame is

$$
\begin{aligned}
p_{x'} &= -P_z \sin\beta\sin\phi, \\
p_{y'} &= \phantom{-}P_z \sin\beta\cos\phi, \\
p_{z'} &= \phantom{-}P_z \cos\beta.
\end{aligned}
$$

The tensor components (already given in §7.1) are restated as

$$
\begin{aligned}
p_{x'x'}-p_{y'y'} &= -\tfrac{3}{2}\sin^2\beta\cos 2\phi\, P_{zz}, \\
p_{z'z'} &= \tfrac{1}{2}(3\cos^2\beta - 1)P_{zz}, \\
p_{y'z'} &= \sin\beta\cos\beta\cos\phi\, P_{zz}, \\
p_{x'z'} &= -\sin\beta\cos\beta\sin\phi\, P_{zz}.
\end{aligned}
$$

### 8.2 Four independent observables

Substituting these components into the Ohlsen formula of §4, a single polarimeter at polar angle $\theta$ provides three asymmetries:

$$
\begin{aligned}
\mathcal{A}_{LR} &\equiv \frac{2(\sigma_L - \sigma_R)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{\tfrac{3}{2}P_z \sin\beta\cos\phi\, A_y - \tfrac{2}{3}P_{zz}\sin\beta\cos\beta\sin\phi\, A_{xz}}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}, \\[4pt]
\mathcal{A}_{UD} &\equiv \frac{2(\sigma_U - \sigma_D)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{\tfrac{3}{2}P_z \sin\beta\sin\phi\, A_y + \tfrac{2}{3}P_{zz}\sin\beta\cos\beta\cos\phi\, A_{xz}}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}, \\[4pt]
\mathcal{A}_{LR-UD} &\equiv \frac{(\sigma_L+\sigma_R)-(\sigma_U+\sigma_D)}{\sigma_L+\sigma_R+\sigma_U+\sigma_D}
= \frac{-\tfrac{1}{4}\sin^2\beta\cos 2\phi\, P_{zz}(A_{xx}-A_{yy})}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}}.
\end{aligned}
$$

Together with the two-angle average cross-section ratio of §4.2,

$$
\mathcal{R}_{12} \equiv \frac{\bar{\sigma}(\theta_1)}{\bar{\sigma}(\theta_2)} = \frac{\sigma_0(\theta_1)}{\sigma_0(\theta_2)}\cdot\frac{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}(\theta_1)}{1 + \tfrac{1}{4}(3\cos^2\beta - 1)P_{zz} A_{zz}(\theta_2)},
$$

a single polarimeter thus provides **four independent observables** $\{\mathcal{A}_{LR},\mathcal{A}_{UD},\mathcal{A}_{LR-UD},\mathcal{R}_{12}\}$, matching the number of unknowns. However, these equations retain multiple degeneracies in $(\beta,\phi)$:

- $\phi \leftrightarrow \phi + \pi$: both $(\mathcal{A}_{LR},\mathcal{A}_{UD})$ flip sign while $\mathcal{A}_{LR-UD}$ and $\mathcal{R}_{12}$ are unchanged; equivalent to flipping $P_z \to -P_z$, and therefore indistinguishable.
- $\beta \leftrightarrow \pi - \beta$: $\cos\beta \to -\cos\beta$, yet $\mathcal{R}_{12}$ and $\mathcal{A}_{LR-UD}$ are unchanged.
- Whenever $\beta$ or $\sin\beta$ is small, certain terms are suppressed and the sensitivity to the corresponding component drops sharply.

So a single-point polarimeter, though equation-count-sufficient, is numerically unstable to invert.

### 8.3 Lifting the degeneracy with two polarimeters

Install a known horizontal dipole (bending angle $\theta_B$) between the two polarimeters. By §6.2, the vertical component $p_{y'}$ is preserved and the in-plane components rotate by $\Delta\phi_s = G\gamma\,\theta_B$. In terms of $(\beta,\phi)$, $\beta$ is unchanged and $\phi$ maps to

$$
\phi_2 = \phi_1 + \Delta\phi_s.
$$

(Strictly speaking, the "azimuthal angle" refers to the orientation around $y'$ in the horizontal plane; this section follows the Ohlsen notation of §7.1. For a purely vertical polarization $\beta=\pi/2,\phi=0$, the dipole does not change the observables, and one must rely on the spin-flip method described below.)

The two polarimeters together provide **eight observables**:

$$
\big\{\mathcal{A}_{LR}^{(1)},\mathcal{A}_{UD}^{(1)},\mathcal{A}_{LR-UD}^{(1)},\mathcal{R}_{12}^{(1)};\ \mathcal{A}_{LR}^{(2)},\mathcal{A}_{UD}^{(2)},\mathcal{A}_{LR-UD}^{(2)},\mathcal{R}_{12}^{(2)}\big\}.
$$

The formulas for polarimeter $(2)$ share the same structure as $(1)$, with $\phi_1$ replaced by $\phi_1 + \Delta\phi_s$. Minimize the eight-equation $\chi^2$

$$
\chi^2(P_z, P_{zz}, \beta, \phi_1) = \sum_{k=1}^{2}\sum_{X\in\{LR,UD,LR-UD,12\}}\frac{\big[\mathcal{A}_X^{(k),\text{meas}} - \mathcal{A}_X^{(k),\text{model}}(P_z,P_{zz},\beta,\phi_k)\big]^2}{\delta_X^{(k)\,2}}
$$

simultaneously for $(P_z, P_{zz}, \beta, \phi_1)$, which uniquely resolves the four unknowns and leaves four degrees of freedom for self-consistency checks (goodness-of-fit and systematic-bias diagnostics).

### 8.4 Complementarity with the spin-flip technique

Switching the RF transitions at the ion source produces distinct source states, e.g.

| Source state | $P_z$ | $P_{zz}$ |
|---|---|---|
| Pure $m=+1$ | $+1$ | $+1$ |
| Pure $m=0$ | $\phantom{+}0$ | $-2$ |
| Pure $m=-1$ | $-1$ | $+1$ |

Swapping $m=\pm 1$ flips $P_z$ while keeping $P_{zz}$ fixed, so

- $(N^{(+)}-N^{(-)})$ retains only terms linear in $P_z$ → directly yields the **vector asymmetry**;
- $(N^{(+)}+N^{(-)})/2 - N^{\text{unpol}}$ retains only terms linear in $P_{zz}$ → directly yields the **tensor asymmetry**.

The two techniques are complementary:

- **Spin flip** purifies observables at the source, but requires controllable and stable fast source-state switching;
- **Two polarimeters** exploit the existing magnetic precession along the transport line to determine polarization magnitudes and axis simultaneously, without switching the source, but require at least one dipole of known geometry.

In practice we recommend combining both: use spin flip to separate the linear responses in $\{P_z, P_{zz}\}$, and use the eight observables from the two polarimeters to fit $\beta$ and $\phi$, pushing the closed-loop Wien-filter adjustment to a polarization-axis precision on the order of a few degrees.

### 8.5 Fitting procedure

1. Offline calibration: measure $\sigma_0(\theta_1),\sigma_0(\theta_2)$ in a known source state (e.g. unpolarized or pure $m=0$), fix the geometry and efficiency factors of both polarimeters; take $A_y(\theta),A_{xz}(\theta),A_{zz}(\theta),(A_{xx}-A_{yy})(\theta)$ from the $d$–$p$ database (Sekiguchi et al.).
2. Online data: for each source state record counts at both polarimeters and compute the eight observables with their statistical uncertainties.
3. Global $\chi^2$ fit for $(P_z, P_{zz}, \beta, \phi_1)$; $\Delta\phi_s$ is fixed (or treated as a nuisance parameter).
4. Cross-check fit stability on independent spin-flipped data sets.
5. Feed the measured $(\beta,\phi)$ back to the Wien filter for closed-loop polarization-axis stabilization.

## 9. Cross-reference to related pages

- `spherical_operator.md`: operator matrices for Cartesian / spherical tensors, tensor components under the $U$ transformation, and the polarization-axis decomposition $(\beta,\phi)$;
- `my_polarimeter.en.md`: bunch spacing and polarimeter time-resolution requirements;
- `other_polarmeter.en.md`: comparison of polarimeter schemes at RIKEN (dPol, BigDpol, KuJyaku), JINR (DSS), COSY (EDDA, JePo), and others;
- `stastic.zh.md`: statistical uncertainty of $R_{LRUD}$ and $\bar{\sigma}_{\theta_1}/\bar{\sigma}_{\theta_2}$ from the multinomial distribution / error propagation.
