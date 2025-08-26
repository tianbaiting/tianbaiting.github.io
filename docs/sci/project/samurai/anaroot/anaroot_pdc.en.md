---
title: ANAROOT Libraries for PDC Analysis
tag: 
    - anaroot
---

# C++ Libraries for PDC Reconstruction and Calibration

## TArtCalibPDCHit
- **Location:** anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCHit.hh, TArtCalibPDCHit.cc  
- **Function:** Performs hit-level calibration and reconstruction for PDC raw data (such as TDC, QDC), generating a TArtDCHit object for each wire.
- **Typical usage:**
```cpp
TArtCalibPDCHit *pdchitcalib = new TArtCalibPDCHit();
pdchitcalib->ReconstructData();
TClonesArray *pdc_hit_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCHit");
```

## TArtCalibPDCTrack
- **Location:** anaroot/sources/Reconstruction/SAMURAI/include/TArtCalibPDCTrack.hh, TArtCalibPDCTrack.cc  
- **Function:** Based on the output of TArtCalibPDCHit, reconstructs tracks from all hits and outputs TArtDCTrack objects.
- **Typical usage:**
```cpp
TArtCalibPDCTrack *pdctrackcalib = new TArtCalibPDCTrack();
pdctrackcalib->ReconstructData();
TClonesArray *pdc_trk_array = (TClonesArray *)sman->FindDataContainer("SAMURAIPDCTrack");
```

## TArtDCHit and TArtDCTrack
- **TArtDCHit:** Stores information for a single PDC wire hit (position, TDC, QDC, etc.).
- **TArtDCTrack:** Stores a reconstructed PDC track (position, angle, chi2, etc.).

# PDC Parameter Database

## SAMURAIPDC.xml
- **Location:** SAMURAIPDC.xml  
- **Function:** Stores parameters for each PDC wire (geo, ch, wireid, position, etc.), used for lookup and calibration during reconstruction.

# Macros and Scripts

## recoPDCTrack.C
- **Location:** users/tbt/tbt_try/recoPDCTrack.C  
- **Function:** Typical macro for PDC reconstruction. Workflow: load parameters → open RIDF → PDC hit reconstruction → PDC track reconstruction → output track parameters.
- **Usage:** Batch processing of data files, outputting PDC track parameters for each event.

## RIDF2Tree.C
- **Location:** users/tbt/tbt_try/RIDF2Tree.C  
- **Function:** Decodes RIDF raw data and saves as ROOT TTree format for further analysis. Can include PDC data branches.

## RecoSAMURAI.C, RecoTrack_wSks.C
- **Location:** Macros/SAMURAI/Analysis/RecoSAMURAI.C, Macros/SAMURAI/RKtrace/RecoTrack_wSks.C  
- **Function:** Used for fragment momentum and track reconstruction in the SAMURAI spectrometer. By default uses FDC/BDC, but can be modified to use PDC tracks for extrapolation and momentum reconstruction.

## OnlineMonitor.cc
- **Location:** OnlineMonitor.cc  
- **Function:** Online monitoring macro, supports online reconstruction and visualization of PDC data (set fUsePDC=true).

# Other Notes

## SAMURAIPDC.xml Parameter File
- **Note:** All PDC channels (geo/ch) actually used must be defined in this file, otherwise reconstruction will fail.


- **ID**: Unique identifier for the wire (usually the same as wireid).
- **NAME**: Name of the wire, e.g. `PDC_0_0` means layer 0, wire 0.
- **FPL**: Focal plane number, e.g. 13 means F13.
- **layer**: Layer number (e.g. 0, 1, 2, etc.).
- **id_plane**: Plane ID (e.g. 81, 82, 83, etc.).
- **anodedir**: Anode wire direction (U/X/V), indicates the measurement direction of the layer.
- **wireid**: Wire number within the layer.
- **wirepos**: Physical position of the wire in this layer (usually in mm).
- **wirez**: Z position of the wire (usually in mm).
- **tzero_offset**: Time zero offset (usually 0).
- **det**: Detector ID (e.g. 37).
- **geo**: Electronics geometry number (e.g. 0, 1, 2, etc.).
- **ch**: Electronics channel number, used for data decoding.

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

- **Only PDC reconstruction:** Use TArtCalibPDCHit, TArtCalibPDCTrack.
- **Full-chain physics analysis:** In macros like RecoSAMURAI.C or RecoTrack_wSks.C, replace FDC/BDC with PDC track for extrapolation to the target and momentum reconstruction.
- **Online monitoring:** Use OnlineMonitor.s024 and set fUsePDC=true.

---

## Data Flow and Algorithm for PDC Track Reconstruction

### Data Flow Overview
- **Input:** All PDC hits (TArtDCHit), each with spatial position (x/y/z), drift time, etc.
- **Processing:** In `TArtCalibPDCTrack::ReconstructData()`, hits are first classified (by layer/direction), then geometric methods (e.g., weighted centroid, line fitting) are used to reconstruct track parameters.
- **Output:** Reconstructed track parameters (position, angle, chi2, etc.) are written to TArtDCTrack objects via `SetAngle`, `SetPosition`, etc.

### Typical Implementation (Weighted Centroid Example)

1. **Hit Classification**  
   Classify all hits by wire direction (u/x/v/y), store in separate buffers.

2. **Calculate Weighted Centroid for Each Direction**  
   For each layer, calculate the weighted average position (weight is usually drift time difference or signal strength).

3. **Line Fitting to Obtain Angles**  
   Fit a straight line to the centroid points to get the slope (angle):  
   - X direction: a = (x2 - x1)/(z2 - z1)
   - Y direction: b = (y2 - y1)/(z2 - z1)  
   Or use least squares fitting with multiple points.

4. **Write to TArtDCTrack**  
   Use `SetAngle(a, 0)` and `SetAngle(b, 1)` to store the fitted angles in TArtDCTrack's ca[0] and ca[1].

5. **Access Later**  
   Use `GetAngle(0)` and `GetAngle(1)` to retrieve the X and Y angles.

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




