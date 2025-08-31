# PDC Drift Chamber Simulation Plan

## References and Tutorials

### 1. Drift Chamber Principles
- [Drift Chamber tutorial (Chinese)](https://yznkxjs.xml-journal.net/cn/article/pdf/preview/10.7538/yzk.1981.15.01.0116.pdf)
- [Drift Chamber Tutorial (ICFA 2005)](https://indico.cern.ch/event/426015/contributions/1047606/attachments/906077/1278746/DriftChamber_ICFA2005.pdf)
- [Drift Chamber Principles (IOP)](https://iopscience.iop.org/article/10.1088/1742-6596/18/1/010/pdf)

### 2. Geant4 Simulation
- [Geant4 Simulation Tutorial (Munich 2018)](https://indico.cern.ch/event/709670/contributions/3027829/attachments/1670306/2679293/Munich.pdf)

### 3. PDC Detector Technical Documents
- [PDC detailed parameters and design](https://www.nishina.riken.jp/ribf/SAMURAI/image/Detector-PDC.pdf)
- [PDC CAD screenshots](https://indico2.riken.jp/event/2752/contributions/11231/attachments/7528/8801/04_EMIS2012_KobayashiT.pdf)

## PDC Specifications

### 1. Design and Purpose

The PDC detector (Proton Drift Chamber) measures momenta of protons near projectile rapidity and is placed downstream of the SAMURAI magnet. To reduce the number of readout planes, PDC uses cathode readout for position information while the anode planes use Walenta-type drift chamber wires. An 8 mm drift distance reduces the number of anode wires. To handle multi-particle events, the cathode strips are arranged in three orientations: 0°, +45°, and -45°.

Note: PDC uses cathode readout. When ionization electrons drift toward the anode wires and cause avalanches, induced charges appear on nearby cathode strips. Reading these induced charges provides particle positions.

### 2. Main Parameters

- Effective area: 1700 mm × 800 mm
- Anode wires: gold-tungsten/ rhenium alloy, 30 μm diameter, 16 mm spacing, 8 mm drift length
- Cathode wires: gold-aluminum alloy, 80 μm diameter, 3 mm spacing
- Anode-cathode gap: 8 mm
- Cathode strip width: 12 mm (every 4 cathode wires are grouped into one strip)
- HV scheme: positive high voltage on anode wires, slightly negative potential on field wires
- Layer configuration: Cathode (U) - Anode (V) - Cathode (X) - Anode (U) - Cathode (V)
- Operating gas: Ar + 25% i-C4H10 or Ar + 50% C2H6

![PDC structure diagram](assets/PDC.zh/image.png)
*PDC structure diagram*

![PDC chamber structure](assets/PDC.zh/image-1.png)
*PDC chamber structure. The X, U, V layers use wires (or strips) at different orientations to determine 2D hit positions. For example, X-layer wires are typically perpendicular to the X-axis to measure the X coordinate precisely.*

Anode wire (readout wire) illustration:
![alt text](assets/PDC.zh/image-2.png)

Code: https://github.com/tianbaiting/Dpol_smsimulator/blob/main/sim_deuteron/forunderstanding/plot_pdc_wires.py

### 3. Readout Scheme and Development

- Initial scheme (tested): To reduce readout channels, a charge-division readout was tested where cathode strips were chained through resistors and every 8 strips were read out by one charge-sensitive preamplifier. A prototype chamber (600 mm × 480 mm) achieved ~1 mm (rms) position resolution with X-rays but could not correctly handle two-proton events.
- New scheme (in development): To address multi-particle events and improve resolution, a new readout circuit is being developed. Each cathode signal connects directly to a preamplifier, shaper, and sample-and-hold circuit, digitized on a front-end board (FEB). Position resolution is expected to improve by about 5×, requiring ~810 readout channels.

---

## Simulation Plan Overview

You need to build the PDC detector geometry yourself. Geant4 can simulate ionization processes in gas accurately. Our simplified approach:

1. Use Geant4 to simulate particles traversing the drift-chamber gas.
2. In a Geant4 user action (SteppingAction), record all ionization hits (energy deposits) with positions.
3. For each wire, build a Sensitive Detector region; use the nearest-wire distance as a proxy for drift time and the total deposited energy as amplitude.
4. This method simplifies "firing" to "ionization occurred nearby," ignoring electron drift time, diffusion, and avalanche gain.

## Limitations

- Ignores electron drift: Real ionization electrons drift along field lines and may avalanche in high-field regions. This method cannot simulate that process.
- Cannot model signal shapes and timing: Without drift times, precise timing and waveform information are not available.
- Cannot model gain: Geant4 does not simulate avalanches, so signal gain per “hit” is not available.

---

## 1. Physical Model Summary

- Build PDC geometry and gas materials in Geant4.
- Particles (e.g., protons) ionize the gas and energy depositions are recorded.
- In SteppingAction, check if an ionization step is near an anode wire; use the nearest distance as drift time and deposited energy as signal amplitude.
- Ignore electron drift, avalanche gain, and signal shaping — simulate only spatial distribution and energy response.

## 2. Geometry and Materials Construction

- Define the gas mixture, e.g., 75% Ar + 25% i-C4H10 at 1 atm.
- Build the chamber box using G4Box or G4Trap to represent the gas volume.
- Construct the wire array using G4Cylinder or G4Tubs for anode wires and place them at actual positions.

## 3. Sensitive Detector Setup

- Set the gas volume as a Sensitive Detector (SD) and record energy deposition and position for each step in the SD.

## 4. SteppingAction Implementation

- In UserSteppingAction, check whether the step is in the gas volume and handle recording accordingly.

## 5. Data Output

- For each event, output all “fired” signals (store in a TTree/TClonesArray), including energy, position, nearest-wire index, drift distance, etc.

## Specific Code Implementation

Data flow diagram:

```mermaid
graph TD
    subgraph "Input & Simulation"
        A[Input file<br/>dbreakb01.root] --> B{Geant4 simulation};
        C[BeamSimTree] --> D[beam data];
    end

    subgraph "PDC Tracker Processing"
        E(FragmentSD) --> F[FragSimData];
    end

    subgraph "Neutron Detector Processing"
        I(NEBULASD) --> J[NEBULAPla data];
        J --> K[Neutron analysis];
    end

    subgraph "Other"
            G{Needed by tracking algorithms} --> H[Output branches<br/>target_*, PDC1*, PDC2*];
    end
    B --> E & I;
```

/home/tbt/workspace/dpol/smsimulator5.5/sim_deuteron/src/DeutDetectorConstruction.cc
```cpp
// Lines 232-234: place PDC1 in the world
G4ThreeVector pdc1_pos_lab{fPDC1Pos}; 
pdc1_pos_lab.rotateY(pdc_angle);  // coordinate transform
G4Transform3D pdc1_trans{pdc1_rm, pdc1_pos_lab};
new G4PVPlacement{pdc1_trans, pdc_log, "PDC1", expHall_log, false, 0};

// Lines 236-240: save to simulation parameters
frag_prm->fPDC1Position.SetXYZ(
    fPDC1Pos.x()/mm, 
    fPDC1Pos.y()/mm, 
    fPDC1Pos.z()/mm
);
```
Translate first, then rotate

PDC has 3 independent sensitive layers:

U layer: /PDC_U - tilted wire direction  
X layer: /PDC_X - vertical wire direction  
V layer: /PDC_V - tilted wire direction

// In DeutDetectorConstruction.cc setup
fPDCSD_U = new FragmentSD("/PDC_U");  // U-layer sensitive detector
fPDCSD_X = new FragmentSD("/PDC_X");  // X-layer sensitive detector  
fPDCSD_V = new FragmentSD("/PDC_V");  // V-layer sensitive detector

// Bind to corresponding logical volumes
fPDCConstruction->fLayerU->SetSensitiveDetector(fPDCSD_U);
fPDCConstruction->fLayerX->SetSensitiveDetector(fPDCSD_X);
fPDCConstruction->fLayerV->SetSensitiveDetector(fPDCSD_V);

FragmentSD working principle
Core method is ProcessHits():

```cpp
G4bool FragmentSD::ProcessHits(G4Step* aStep, G4TouchableHistory*)
{
    // 1. Get the data manager
    SimDataManager *sman = SimDataManager::GetSimDataManager();
    TClonesArray *SimDataArray = sman->FindSimDataArray("FragSimData");
    
    // 2. Extract step information
    G4StepPoint* preStepPoint = aStep->GetPreStepPoint();
    G4StepPoint* postStepPoint = aStep->GetPostStepPoint();
    
    // 3. Selection: only record primary particle and charged particles
    if(parentid == 0 && aStep->GetTrack()->GetDefinition()->GetPDGCharge() != 0.)
    {
        // 4. Create a TSimData object and fill fields
        TSimData* data = new TSimData();
        data->fTrackID = trackid;
        data->fDetectorName = detectorName;  // "U", "X", "V"
        data->fPrePosition = prePosition;
        data->fPostPosition = postPosition;
        data->fPreMomentum = preMomentum;
        // ... more physical quantities
    }
}
```
