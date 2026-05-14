TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();

Function: This object (nebulahpc_calib) is responsible for calibrating the NEBULA High Pressure Chamber (HPC) data. The HPC is mainly used as a veto detector for neutron detection in NEBULA, to distinguish neutrons from charged particles (such as electrons or protons produced by gamma-ray conversion).

- Input: Reads raw data from the HPC detector (e.g., TDC timing information) from TArtEventStore.
- Processing:
  - Applies time calibration parameters (managed by TArtSAMURAIParameters).
  - Converts raw TDC values to physical time.
  - Performs basic hit identification.
- Output: Calibrated TArtNEBULAHPC objects, each containing calibrated information for an HPC hit (such as time, detector ID, etc.), stored in a "NEBULAHPC" TClonesArray in TArtStoreManager.

---

TArtCalibNEBULA *nebulapla_calib = new TArtCalibNEBULA();

Function: This object (nebulapla_calib) is responsible for calibrating the NEBULA plastic scintillator (Pla) data, which is the main component of the NEBULA neutron detector.

- Input: Reads raw data from both ends of the plastic scintillator PMTs (TDC timing and QDC charge) from TArtEventStore.
- Processing:
  - Applies time and charge calibration parameters.
  - Calculates the average time, time difference (for position reconstruction), and average charge for each hit.
  - Calculates the hit position.
  - Converts calibrated time and charge to physical units (ns, MeVee).
- Output: Calibrated TArtNEBULAPla objects, each containing detailed calibration information for a hit (ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal, etc.), stored in a "NEBULAPla" TClonesArray in TArtStoreManager.

---

TArtRecoNeutron *reco_neutron = new TArtRecoNeutron();

Function: This object (reco_neutron) is responsible for reconstructing neutron events from the calibrated neutron detector data. This is a higher-level reconstruction step.

- Input:
  - Mainly relies on the collection of TArtNEBULAPla objects produced by TArtCalibNEBULA (plastic scintillator hit information).
  - May use the output of TArtCalibNEBULAHPC (TArtNEBULAHPC objects) as a charged particle veto signal to improve neutron identification purity.
  - May also require information from other detectors (such as beam detector timing as a TOF reference).
- Processing:
  - Clustering: Groups TArtNEBULAPla hits that are close in space and time into potential neutron clusters.
  - Particle identification (PID): Uses charge information (dE/dx) and time-of-flight (TOF) to distinguish neutrons from other particles.
  - Time-of-flight calculation: Calculates the neutron TOF from the target (or reference detector) to NEBULA.
  - Energy reconstruction: Calculates neutron kinetic energy based on TOF and flight path length.
  - Position reconstruction: Determines the neutron interaction position.
- Output: Reconstructed TArtNeutron objects (or similar classes), each containing the physical properties of a neutron (energy, time, position, angle, etc.), stored in a "Neutron" TClonesArray in TArtStoreManager.

## NEBULA Reconstruction Procedure (Sample Code Workflow)

- Initialization and Parameter Loading
  - Load necessary libraries and headers, set include paths.
  - Obtain and load the `TArtSAMURAIParameters` parameter file.
  - Open the RIDF data file.

- Reconstruction Class Initialization
  - Create objects for `TArtCalibNEBULAHPC`, `TArtCalibNEBULA`, and `TArtRecoNeutron`.

- Event Loop Processing
  - For each event (e.g., the first 10 events), perform the following:
    - Clear data from the previous event (`ClearData()`).
    - Call `ReconstructData()` to perform hit and neutron reconstruction.
    - Retrieve and output HPC hits, Pla hits, and neutron reconstruction results.
    - Clear raw event data in preparation for the next event.

- Output Content
  - Output the number of HPC hits and details for each event (ID, Layer, SubLayer, TRaw, TCal, etc.).
  - Output the number of Pla hits and details (ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal, etc.).
  - Output the number of reconstructed neutrons and their physical quantities (Time, MeVee, PosX, PosY, PosZ, etc.).

- Cleanup and Resource Release
  - After the event loop, release all allocated objects and resources.

> For the specific code implementation, see the example integrated in the latter part of this file.

```

#include <iostream>
void recoNebulaTrack(const char* ridffile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0073.ridf") {
    gSystem->Load("libXMLParser.so");
    gSystem->Load("libanacore.so");

    // It's good practice to set the include path if your custom classes are not in standard ROOT include paths
    // Adjust this path if your anaroot/users/tbt/src/include is different or if headers are elsewhere
    gSystem->AddIncludePath("-I/home/s057/exp/exp2505_s057/anaroot/users/tbt/src/include");
    gSystem->AddIncludePath("-I/home/s057/exp/exp2505_s057/anaroot/users/tbt/src/sources/Reconstruction/SAMURAI/include");


    TArtSAMURAIParameters *param = TArtSAMURAIParameters::Instance();
    if (!param) {
        std::cerr << "Error: Failed to get TArtSAMURAIParameters instance." << std::endl;
        return;
    }


    param->LoadParameter((char*)"/home/s057/exp/exp2505_s057/anaroot/users/tbt/db/NEBULA.2023_7_6.xml"); 

    TArtEventStore *estore = new TArtEventStore();
    if (!estore->Open(ridffile)) {
        std::cerr << "Error: Cannot open RIDF file: " << ridffile << std::endl;
        delete estore;
        return;
    }

    // Initialize reconstruction classes
    TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();
    TArtCalibNEBULA    *nebulapla_calib = new TArtCalibNEBULA(); // Corrected type
    TArtRecoNeutron    *reco_neutron    = new TArtRecoNeutron();

    TArtStoreManager *sman = TArtStoreManager::Instance();

    std::cout << "Starting event loop for NEBULA reconstruction..." << std::endl;
    int neve = 0;
    while (estore->GetNextEvent() && neve < 10) { // Process first 10 events
        std::cout << "========== Event " << neve + 1 << " ==========" << std::endl;

        // 1. Clear data from previous event
        nebulahpc_calib->ClearData();
        nebulapla_calib->ClearData(); 
        reco_neutron->ClearData();

        // 2. Reconstruct current event's data
        // LoadRawData is typically called internally by ReconstructData if fDataLoaded is false.
        // If your framework requires explicit LoadRawData, uncomment the lines below.
        // nebulahpc_calib->LoadRawData(); 
        // nebulapla_calib->LoadData(); // TArtCalibNEBULA uses LoadData()

        nebulahpc_calib->ReconstructData();
        nebulapla_calib->ReconstructData(); 
        reco_neutron->ReconstructData();

        // 3. Output reconstructed results

        // Output HPC hits
        int n_hpc_hits = nebulahpc_calib->GetNumNEBULAHPC();
        std::cout << "  NEBULA HPC Hits: " << n_hpc_hits << std::endl;
        for (int i = 0; i < n_hpc_hits; ++i) {
            TArtNEBULAHPC* hit = nebulahpc_calib->GetNEBULAHPC(i);
            if (hit) {
                std::cout << "    HPC Hit " << i
                          << ": ID=" << hit->GetID()
                          << ", Layer=" << hit->GetLayer()
                          << ", SubLayer=" << hit->GetSubLayer()
                          << ", TRaw=" << hit->GetTRaw()
                          << ", TCal=" << hit->GetTCal()
                          << std::endl;
            }
        }

        // Output Pla hits
        int n_pla_hits = nebulapla_calib->GetNumNEBULAPla();
        std::cout << "  NEBULA Pla Hits: " << n_pla_hits << std::endl;
        for (int i = 0; i < n_pla_hits; ++i) {
            TArtNEBULAPla* pla_hit = nebulapla_calib->GetNEBULAPla(i);
            if (pla_hit) {
                std::cout << "    Pla Hit " << i
                          << ": ID=" << pla_hit->GetID()
                          << ", Layer=" << pla_hit->GetLayer()
                          << ", SubLayer=" << pla_hit->GetSubLayer()
                          << ", QUAveCal=" << pla_hit->GetQAveCal()
                          << ", TAveCal=" << pla_hit->GetTAveCal()
                          << ", PosCal=" << pla_hit->GetPosCal()
                          << std::endl;
            }
        }

        // Output Neutron reconstruction results
        TClonesArray* neutron_array = reco_neutron->GetNeutronArray();
        int n_neutron = neutron_array ? neutron_array->GetEntriesFast() : 0;
        std::cout << "  Reconstructed Neutrons: " << n_neutron << std::endl;
        for (int i = 0; i < n_neutron; ++i) {
            TArtNeutron* neutron = (TArtNeutron*)neutron_array->At(i);
            if (neutron) {
                std::cout << "    Neutron " << i
                          << ": Time=" << neutron->GetTime()
                          << ", MeVee=" << neutron->GetMeVee()
                          << ", PosX=" << neutron->GetPos(0)
                          << ", PosY=" << neutron->GetPos(1)
                          << ", PosZ=" << neutron->GetPos(2)
                          << std::endl;
            }
        }

        estore->ClearData(); // Clear raw event data for the next event
        neve++;
    }

    std::cout << "Finished event loop. Processed " << neve << " events." << std::endl;

    // Clean up
    delete nebulahpc_calib;
    delete nebulapla_calib;
    delete reco_neutron;
    delete estore;
    // TArtStoreManager::Delete(); // If it's a singleton managed this way
    // TArtSAMURAIParameters::Delete(); // If it's a singleton managed this way
}
```

---

## Real TArtCalibNEBULA pipeline

### 1. Raw decode (`LoadData`, `TArtCalibNEBULA.cc:64-204`)

- Keeps only `device == SAMURAI` and detector ∈ `{NEBULA1Q, NEBULA1T, …, NEBULA4Q, NEBULA4T}`.
- HPC channels are skipped (line 121).
- TDC leading (`edge==0`) → `fTURaw / fTDRaw` + `TUMulti / TDMulti`++; trailing → `fTURaw_Trailing / fTDRaw_Trailing` (lines 159-173).
- QDC: U/D → `fQURaw / fQDRaw` (lines 187-202).

### 2. Calibration (`ReconstructData`, `TArtCalibNEBULA.cc:207-400`)

#### TRef subtraction

```
turaw_subtref = turaw - turaw_ref
tdraw_subtref = tdraw - tdraw_ref
```

#### Charge calibration

```
quped   = quraw - QUPed
qdped   = qdraw - QDPed
qucal   = quped * QUCal
qdcal   = qdped * QDCal
qaveped = sqrt(quped * qdped)
qavecal = QAveCal * sqrt(qucal * qdcal)
```

#### TDC linear calibration

```
tucal = turaw_subtref * TUCal + TUOff
tdcal = tdraw_subtref * TDCal + TDOff
```

#### Slewing (the key non-linearity)

If `TUSlwLog[0] != 0`, a **5-term log polynomial** is used (`TArtCalibNEBULA.cc:291-307`):

$$
t_u^\text{slw} = t_u^\text{cal} - \sum_{k=0}^{4} c_k \, [\log(q_u^\text{ped})]^{k+1}
$$

(the k=2 term is double-weighted). Otherwise the classic 1/√q form is applied:

$$
t_u^\text{slw} = t_u^\text{cal} - \frac{\text{TUSlw}}{\sqrt{q_u^\text{ped}}}
$$

#### Position reconstruction

```
dtcal = tdcal - tucal
dtslw = tdslw - tuslw
PosCal = dtcal * DTCal + DTOff
PosSlw = dtslw * DTCal + DTOff

pos[0] = DetPos[0] + posxoff
pos[1] = PosSlw    + DetPos[1] + posyoff
pos[2] = DetPos[2] + poszoff
```

The effective light velocity inside the bar is encoded in `DTCal` (mm per ns or per TDC-channel difference).

#### Charge attenuation correction

$$
q_\text{ave}^\text{cal} \leftarrow \frac{q_\text{ave}^\text{cal}}{1 + y^2 \cdot \text{QAveCalAtt}}
$$

#### TOF hypotheses

```
TTOFGamma   = taveslw - L / 29.979   // γ (c = 29.979 cm/ns)
TTOFNeutron = taveslw - L / 20.       // β ≈ 2/3
```

---

## `TArtNEBULAFilter` — 5 cut algorithms

| Cut | Lines | Algorithm |
|---|---|---|
| `IHitMin(ihitmin_n, ihitmin_v)` | 34-58 | Require ≥ ihitmin of `{TURaw, TDRaw, QURaw, QDRaw}` in `(0, 4096]` (separate NEUT/VETO thresholds) |
| `Threshold(thr_n, thr_v)` | 85-112 | `QAveCal` threshold (NEUT and VETO separately) |
| `TOF(tmin, tmax)` | 115-137 | `TAveSlw` window on NEUT only |
| `Veto(VetoNum)` | 140-196 | Scan `SubLayer==0` bars; find smallest-layer veto hit `VetoHitMin`; if it's layer 1 drop everything, else drop all NEUT with `Layer > VetoHitMin` |
| `HitMinPos / HitMinTime / HitMinPos2` | 200-406 | Keep one earliest-position or earliest-time NEUT per layer group |

> `SubLayer == 0` → VETO; `SubLayer ∈ {1, 2}` → NEUT sublayers.

---

## `TArtRecoNeutron` actual logic (`TArtRecoNeutron.cc:57-125`)

⚠️ **No clustering.** Each surviving `TArtNEBULAPla` produces exactly one `TArtNeutron`. Cluster logic must be added by the user.

```cpp
m = 939.565 MeV                  // neutron mass
time = pla->GetTAveSlwT0()
mevee = pla->GetQAveCal()
pos = pla->GetPos()              // (x,y,z) in lab

β_i = pos[i] / (time * 29.979 cm/ns)
γ   = 1 / sqrt(1 - β·β)
p_i = m * γ * β_i
E   = sqrt(m^2 + p·p) - m
θ   = atan( sqrt(p_x^2 + p_y·p_z) / p_z )
```

> Note: `sqrt(p_x^2 + p_y*p_z)` is the literal expression in source (`TArtRecoNeutron.cc:105`); this looks like a typo for `p_y^2`. Verify against your anaroot version before using θ.

---

## NEBULA parameter file (`db/NEBULA.csv`)

Full column header (`db/NEBULA.csv:1`):

```
ID, NAME, FPl, Layer, SubLayer, PosX, PosY, PosZ,
TUCal, TUOff, TUSlw, QUCal, QUPed,
TDCal, TDOff, TDSlw, QDCal, QDPed,
DTCal, DTOff, TAveOff,
tu_det, tu_geo, tu_ch, td_det, td_geo, td_ch,
qu_geo, qu_ch, qd_geo, qd_ch,
is_tref, is_hpc, id_hpc, Ignore
```

184 module rows. Deployment census:

| Layer | SubLayer | Type | Count | PosZ (mm) |
|---|---|---|---|---|
| 1 | 0 | VETO / reference | 13 | — |
| 2 | 0 | VETO / reference | 18 | — |
| 3 | 0 | VETO front wall | 14 | 11493.72 / 11508.72 (staggered) |
| 3 | 1 | **NEUT front SL1** | **30** | **13895.2** |
| 3 | 2 | **NEUT front SL2** | **30** | **14025.2** (+130) |
| 4 | 0 | VETO rear wall | 16 | 12339.72 / 12354.72 |
| 4 | 1 | **NEUT rear SL1** | **30** | **14741.2** |
| 4 | 2 | **NEUT rear SL2** | **30** | **14871.2** (+130) |
| 5 | 0 | bookkeeping | 3 | — |

**Total: 120 NEUT + ~61 VETO**. The Geant4 Dayone preset has 120+24 — the deployed array includes additional structural veto/reference bars.

X span -1901.8 → +1647.8 mm, pitch 122.4 mm (30 bars × 122.4 ≈ 3672 mm wide).

### Typical calibration values

- `TUCal, TDCal ≈ 0.0976` ns/ch (TDC LSB)
- `QUCal, QDCal ≈ 0.035–0.048` MeVee/ch
- `QUPed, QDPed ≈ 100–145` ch
- `DTCal = 1`, `DTOff ≈ -20…+30 mm`
- `TUSlw, TDSlw = 0` (classic slewing disabled in current CSV; the XML uses `<TUSlwLog>` polynomial coefficients instead)

### Magnet-centered frame

`db/NEBULA_Pos_FromMagCenter.csv` has the same module IDs but `PosZ ≈ 9784…10374 mm` (magnet center is ~4111 mm upstream of NEBULA front). Use this frame for RK tracing and TOF.

### HPC (anti-veto)

`db/NEBULAHPC.csv` columns: `NAME, FPl, Layer, SubLayer, PosX, PosY, PosZ, TCal, TOff, tdc_geo, tdc_ch`. **16 HPC paddles** at `Z = 9442.3 mm`, single TDC channel each (no Q, no TU/TD split). They sit in front of NEBULA to veto charged particles.

---

## References (`../refs/`)

- `Kondo_NIMA_967_163826_NEBULA_calibration.pdf` — Kondo et al., NIM A 967 (2020) 163826
- `NEBULA_workshop_Kondo.pdf` — light attenuation, time resolution, efficiency
- `Detector-NEBULA.pdf` — RIKEN SAMURAI NEBULA datasheet
- `Kondo_arXiv_2412.17887_QFS_review.pdf` — multi-neutron review (NEBULA-Plus)