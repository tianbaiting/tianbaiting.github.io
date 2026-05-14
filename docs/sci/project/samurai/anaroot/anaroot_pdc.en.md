---
title: ANAROOT Libraries for PDC Analysis
tag: 
    - anaroot
---

# C++ Libraries for PDC Reconstruction and Calibration

## TArtCalibPDCHit
- Location: anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCHit.hh, TArtCalibPDCHit.cc  
- Function: Performs hit-level calibration and reconstruction for PDC raw data (such as TDC, QDC), generating a TArtDCHit object for each wire.
- Typical usage:
```cpp
TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
pdchitcalib->ReconstructData();
TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
```

## TArtCalibPDCTrack
- Location: anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCTrack.hh, TArtCalibPDCTrack.cc  
- Function: Based on the output of TArtCalibPDCHit, reconstructs tracks from all hits and outputs TArtDCTrack objects.
- Typical usage:
```cpp
TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();
pdctrackcalib->ReconstructData();
TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");
```

## TArtDCHit and TArtDCTrack
- TArtDCHit: Stores information for a single PDC wire hit (position, TDC, QDC, etc.).
- TArtDCTrack: Stores a reconstructed PDC track (position, angle, chi2, etc.).

# PDC Parameter Database

## SAMURAIPDC.xml
- Location: SAMURAIPDC.xml  
- Function: Stores parameters for each PDC wire (geo, ch, wireid, position, etc.), used for lookup and calibration during reconstruction.

# Macros and Scripts

## recoPDCTrack.C
- Location: users/tbt/tbt_try/recoPDCTrack.C  
- Function: Typical macro for PDC reconstruction. Workflow: load parameters → open RIDF → PDC hit reconstruction → PDC track reconstruction → output track parameters.
- Usage: Batch processing of data files, outputting PDC track parameters for each event.

## RIDF2Tree.C
- Location: users/tbt/tbt_try/RIDF2Tree.C  
- Function: Decodes RIDF raw data and saves as ROOT TTree format for further analysis. Can include PDC data branches.

## RecoSAMURAI.C, RecoTrack_wSks.C
- Location: Macros/SAMURAI/Analysis/RecoSAMURAI.C, Macros/SAMURAI/RKtrace/RecoTrack_wSks.C  
- Function: Used for fragment momentum and track reconstruction in the SAMURAI spectrometer. By default uses FDC/BDC, but can be modified to use PDC tracks for extrapolation and momentum reconstruction.

## OnlineMonitor.cc
- Location: OnlineMonitor.cc  
- Function: Online monitoring macro, supports online reconstruction and visualization of PDC data (set fUsePDC=true).

# Other Notes

## SAMURAIPDC.xml Parameter File
- Note: All PDC channels (geo/ch) actually used must be defined in this file, otherwise reconstruction will fail.


- ID: Unique identifier for the wire (usually the same as wireid).
- NAME: Name of the wire, e.g. `PDC_0_0` means layer 0, wire 0.
- FPL: Focal plane number, e.g. 13 means F13.
- layer: Layer number (e.g. 0, 1, 2, etc.).
- id_plane: Plane ID (e.g. 81, 82, 83, etc.).
- anodedir: Anode wire direction (U/X/V), indicates the measurement direction of the layer.
- wireid: Wire number within the layer.
- wirepos: Physical position of the wire in this layer (usually in mm).
- wirez: Z position of the wire (usually in mm).
- tzero_offset: Time zero offset (usually 0).
- det: Detector ID (e.g. 37).
- geo: Electronics geometry number (e.g. 0, 1, 2, etc.).
- ch: Electronics channel number, used for data decoding.

# Summary and Recommendations

| Name                  | Type      | Main Function / Usage                                 |
|-----------------------|-----------|------------------------------------------------------|
| TArtCalibPDCHit       | Class     | PDC hit-level reconstruction (raw signal → hit)      |
| TArtCalibPDCTrack     | Class     | PDC track reconstruction (hit → track)               |
| TArtDCHit/TArtDCTrack | Class     | Store single hit / track information                 |
| SAMURAIPDC.xml        | ParamFile | Parameter database for each PDC wire                 |
| transPDCData.C        | Macro     | Convert PDC raw data to readable text                |
| RIDF2Tree.C           | Macro     | Convert RIDF to ROOT TTree, including PDC branches   |
| RecoSAMURAI.C         | Macro     | Fragment momentum/track reconstruction (PDC track)   |
| RecoTrack_wSks.C      | Macro     | Runge-Kutta tracking (PDC track)                     |
| OnlineMonitor.s024    | Macro     | Online monitoring, supports PDC data reconstruction  |

## How to Choose and Use

- Only PDC reconstruction: Use TArtCalibPDCHit, TArtCalibPDCTrack.
- Full-chain physics analysis: In macros like RecoSAMURAI.C or RecoTrack_wSks.C, replace FDC/BDC with PDC track for extrapolation to the target and momentum reconstruction.
- Online monitoring: Use OnlineMonitor.s024 and set fUsePDC=true.

---

## Data Flow and Algorithm for PDC Track Reconstruction

### Data Flow Overview
- Input: All PDC hits (TArtDCHit), each with spatial position (x/y/z), drift time, etc.
- Processing: In `TArtCalibPDCTrack::ReconstructData()`, hits are first classified (by layer/direction), then geometric methods (e.g., weighted centroid, line fitting) are used to reconstruct track parameters.
- Output: Reconstructed track parameters (position, angle, chi2, etc.) are written to TArtDCTrack objects via `SetAngle`, `SetPosition`, etc.

### Real algorithm: 4-parameter MIGRAD fit (`TArtCalibPDCTrack.cc:9-336`)

`TArtCalibPDCTrack` is **not** a weighted-centroid fitter. The earlier description above is a simplification — the actual code uses `TMinuit/MIGRAD` to minimise a χ² over four track parameters.

**1. Hard-coded layer geometry** (`TArtCalibPDCTrack.cc:36-43`):

```
PDC1 = U, X, V
PDC2 = U, X, V
nlayer_y = 0     // no dedicated Y plane
```

**2. Fit parameters and bounds** (`TArtCalibPDCTrack.cc:122-133`):

| Parameter | Meaning | Range |
|---|---|---|
| `x0`   | x intercept at z=0 | ±1000 mm |
| `y0`   | y intercept at z=0 | ± 800 mm |
| `k_xz` | dx/dz | ±100 |
| `k_yz` | dy/dz | ±100 |

`TMinuit::mnexcm("MIGRAD", ...)` does the χ² minimisation.

**3. χ² evaluation** (`Chi2Calculation`, `TArtCalibPDCTrack.cc:224-336`):

For each plane the valid hits (`TDC>0 && TrailTDC>0`) are reduced to a **TOT-weighted wire centroid**:

$$
w_i = |\,\text{TDC}_i - \text{TrailTDC}_i\,|,\qquad
\bar{x}_\text{layer} = \frac{\sum_i w_i\,x_i}{\sum_i w_i}
$$

The model prediction is projected onto the wire direction:
- U plane: `U_pred = (x + y)/√2`
- V plane: `V_pred = (x − y)/√2`
- X plane: `x` directly

Residual² is accumulated to form the χ².

**4. Write `TArtDCTrack`** (`TArtCalibPDCTrack.cc:151-158`):

```cpp
trk->SetPosition(x0, 0);
trk->SetPosition(y0, 1);
trk->SetAngle(atan(k_xz), 0);
trk->SetAngle(atan(k_yz), 1);
trk->SetNDF(2);
trk->SetNumHitLayer(nhit_total);
trk->SetChi2(chi2_sum);
```

**5. No χ²/ndf cut in the current build**: the `if (chi2 < 10000)` filter is commented out (lines 148, 162-168), so the output contains poor-quality tracks. Downstream code must add its own `Chi2/NDF` cut.

### Accessor pattern

```cpp
TArtDCTrack* trk = (TArtDCTrack*)pdc_trk_array->At(i);
double x  = trk->GetPosition(0);   // x0 at z=0
double y  = trk->GetPosition(1);   // y0 at z=0
double ax = trk->GetAngle(0);      // atan(dx/dz)
double ay = trk->GetAngle(1);      // atan(dy/dz)
double chi2 = trk->GetChi2();
int    nhit = trk->GetNumHitLayer();
```

### SAMURAIPDC.xml / SAMURAIPDC_fit.csv schema

CSV header (`SAMURAIPDC_fit.csv:1`):

```
ID, NAME, FPL, layer, id_plane, anodedir, wireid, wirepos, wirez, tzero_offset, det, geo, ch
```

≈ 816 wires total, all on `FPL=13`, `det=37`.

| layer | anodedir | id_plane | wirez (mm) | first wirepos | geo start | Notes |
|---|---|---|---|---|---|---|
| 0 | U | 81 | 40 | -822 | 0 | PDC1 plane 1 |
| 1 | X | 82 | 24 | -822 | 2 | PDC1 plane 2 |
| 2 | V | 83 | 8 | +822 (desc.) | 4 | PDC1 plane 3 |
| 3 | U | 84 | -576 | -822 | 8 | PDC2 plane 1 |
| 4 | X | 85 | -592 | -822 | 10 | PDC2 plane 2 |
| 5 | V | 86 | -608 | +822 (desc.) | 13 | PDC2 plane 3 |

- 136 wires per plane, **pitch 12 mm**, `wirepos ∈ [-822, +822] mm`.
- **PDC1 vs PDC2 separated by ≈ 616 mm in z** (PDC1 mean z ≈ 24 mm, PDC2 mean z ≈ -592 mm).
- V layer's `wireid` is reversed wrt `wirepos`.

Example row:

```
1,PDC_0_0,13,0,81,U,0,-822,40,0,37,0,0
```

> All `(geo, ch)` actually used in the run must be present in `SAMURAIPDC.xml`, otherwise the `TArtRIDFMap` lookup fails and hit reconstruction throws.

### PDC track to target

⚠️ The main anaroot pipeline (`Macros/SAMURAI/RKtrace/RecoTrack_wSks.C`, `TArtRecoFragment`) uses **FDC1+FDC2**, not PDC, for SKS-based Runge-Kutta back-tracing to the target.

PDC-to-target lives in two parallel places:

1. **User scripts** under `anaroot/tbt_try/` (`recoPDCdataTosamurai.C`, etc.)
2. **Simulator-side RK + NN** in `smsimulator5.5/libs/analysis_pdc_reco/` (see [smsimulator PDC reco](../smsimulator/PDC.md), driven by `bin/reconstruct_target_momentum`)

Both must read the same `SAMURAIPDC.xml` to stay consistent.

---

## Notes on Momentum

PDC is a multi-wire drift chamber and can only measure the spatial trajectory (x, y, a, b) of a particle. It cannot determine momentum alone. Momentum reconstruction requires magnetic field information and the spectrometer's transfer matrix (or field tracking algorithms), usually involving tracks at multiple positions (e.g., FDC1, FDC2, BDC, PDC) and magnetic field parameters.

---

## Example: Detector Distribution Macro

```cpp
#include <sys/stat.h>
#include <string>
#include <set>
#include <vector>
#include <iostream>
void recoPDCTrack(const char* ridffile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0074.ridf") {

  gSystem->Load("libXMLParser.so"); // 先加载XML解析库
    gSystem->Load("libanacore.so");
    // 加载PDC参数
    TArtSAMURAIParameters *samuraiparameters = TArtSAMURAIParameters::Instance();
    samuraiparameters->LoadParameter("../db/SAMURAIPDC.xml");

    // Open RIDF file
    TArtEventStore *estore = new TArtEventStore();
    estore->Open(ridffile);

    // Initialize PDC hit and track reconstruction
    TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
    TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();

    TArtStoreManager *sman = TArtStoreManager::Instance();
    TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
    TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");

    // get input file name
    std::string inputFileName = std::string(ridffile);
    size_t pos = inputFileName.find_last_of('/');
    std::string fileName = (pos != std::string::npos) ? inputFileName.substr(pos + 1) : inputFileName;

    // 创建输出ROOT文件和TTree
    const char* outputDir = "./output";
    std::string outroot = std::string(outputDir) + "/" + fileName + "_pdc.root";
    std::string outpng = std::string(outputDir) + "/" + fileName + "_pdc_track_xy.png";

    TFile *fout = new TFile(outroot.c_str(), "RECREATE");
    TTree *tree = new TTree("pdctree", "PDC Track Tree");
    int event, trackid, ndf, nhit;
    double x, y, ax, ay, chi2;
    tree->Branch("event", &event, "event/I");
    tree->Branch("trackid", &trackid, "trackid/I");
    tree->Branch("x", &x, "x/D");
    tree->Branch("y", &y, "y/D");
    tree->Branch("ax", &ax, "ax/D");
    tree->Branch("ay", &ay, "ay/D");
    tree->Branch("chi2", &chi2, "chi2/D");
    tree->Branch("ndf", &ndf, "ndf/I");
    tree->Branch("nhit", &nhit, "nhit/I");

    int neve = 0;
    while (estore->GetNextEvent() && neve < 1000) {
        pdchitcalib->ClearData();
        pdctrackcalib->ClearData();
        pdchitcalib->ReconstructData();
        pdctrackcalib->ReconstructData();

        int ntrk = pdc_trk_array->GetEntries();
        for (int i = 0; i < ntrk; ++i) {
            TArtDCTrack *trk = (TArtDCTrack*)pdc_trk_array->At(i);
            x = trk->GetPosition(0);
            y = trk->GetPosition(1);
            ax = trk->GetAngle(0);
            ay = trk->GetAngle(1);
            chi2 = trk->GetChi2();
            ndf = trk->GetNDF();
            nhit = trk->GetNumHitLayer();
            event = neve;
            trackid = i;
            tree->Fill();
            std::cout << "Event: " << neve << ", Track ID: " << i 
                      << ", X: " << x << ", Y: " << y 
                      << ", Ax: " << ax << ", Ay: " << ay 
                      << ", Chi2: " << chi2 
                      << ", NDF: " << ndf 
                      << ", NHits: " << nhit 
                      << std::endl;
        }
        neve++;
    }
    tree->Write();

    TCanvas *c1 = new TCanvas("c1", "PDC Track X-Y", 800, 600);
    tree->Draw("y:x>>hxy", "", "COLZ");
    c1->SaveAs(outpng.c_str());
    delete c1;
    std::cout << "Output ROOT file: " << outroot << std::endl;
    std::cout << "Output PNG file: " << outpng << std::endl;
    
    fout->Close();
    delete pdchitcalib;
    delete pdctrackcalib;
    delete estore;
}

```




