## NEBULA Related Libraries

### 1. Parameter Management

#### TNEBULASimParameter
- **Files**: `TNEBULASimParameter.hh / .cc`
- **Function**: Stores all NEBULA parameters, including the number, type, and geometry of detectors, for use by simulation and data conversion modules.

#### NEBULASimParameterReader
- **Files**: `NEBULASimParameterReader.hh / .cc`
- **Function**: Reads NEBULA parameter files (e.g., `NEBULA_Dayone.csv`, `NEBULA_Detectors_Dayone.csv`) and loads parameters into the simulation environment, including detector count, position, and size.

#### Related Data Files
- **Files**: `NEBULA_Dayone.csv` / `NEBULA_Detectors_Dayone.csv`
- **Function**: These files contain specific parameters for the NEBULA array, such as the position, size, and ID of each detector, which are read by `NEBULASimParameterReader` during simulation.

### 2. Geometry Construction

#### NEBULAConstruction & NEBULAConstructionMessenger
- **Files**: `NEBULAConstruction.hh / .cc`
- **Function**: Defines the geometry of NEBULA neutron detectors, including array size, position, materials, etc. Responsible for building the NEBULA physical model in Geant4 simulation.
- **Files**: `NEBULAConstructionMessenger.hh / .cc`
- **Function**: Provides command interfaces, allowing users to dynamically set NEBULA parameters (such as array parameter files, detector parameter files) via macro files or command line.

### 3. Simulation Core

#### NEBULASD
- **Files**: `NEBULASD.hh / .cc`
- **Function**: Defines the sensitive detector for NEBULA, used to record energy deposition, position, time, and other information of particles in NEBULA detectors during simulation.

### 4. Data Handling

#### NEBULASimDataInitializer
- **Files**: `NEBULASimDataInitializer.hh / .cc`
- **Function**: Initializes NEBULA simulation data structures, allocates data storage space for each detector, and prepares for subsequent data acquisition and analysis.

#### NEBULASimDataConverter_TArtNEBULAPla
- **Files**: `NEBULASimDataConverter_TArtNEBULAPla.hh / .cc`
- **Function**: Converts raw data generated during simulation (such as energy deposition, detector response) into the data format required for experimental analysis (e.g., TArtNEBULAPla), and writes to ROOT files. Implements energy conversion, resolution processing, and other physical models.

## NEBULA Output in Geant4

### 1. Simulation Output Information
- **Energy Deposit**: Each NEBULA detector module records the energy deposited by particles (mainly neutrons) in the detector.
- **Detector Response**: Simulates the signal output of the detector in actual experiments (e.g., PMT response) based on energy deposit, detector resolution, and other physical models.
- **Position and Time Information**: Records the hit position and incident time of particles in the detector, used for subsequent TOF and spatial distribution analysis.
- **Particle Type and ID**: Distinguishes different particles (e.g., neutron, fake neutron, fake gamma) and their corresponding detector IDs for event selection and physics analysis.

### 2. Generated ROOT Files
- **Data Structure**: NEBULA simulation data is converted to ROOT files, usually containing one or more TTrees (e.g., `NEBULAPla`), each entry corresponding to an event or detector response.
- **Example Content**:
    - Under each event, the `NEBULAPla` branch stores response data (such as energy, position, time) for all hit NEBULA detector modules.
    - Other branches may contain global event information, initial particle parameters, etc.
- **Usage**:
    - **Experimental Data Comparison**: The structure of the simulated ROOT file matches the experimental data and can be directly used for comparative analysis.
    - **Physics Analysis**: ROOT scripts or analysis frameworks can be used for statistics, plotting, efficiency calculation, energy spectrum analysis, etc.
    - **Detector Performance Evaluation**: Analyze the response distribution, resolution, detection efficiency, etc., to support experiment design and data interpretation.
    - **Event Selection**: Select interesting physics events based on particle type, energy, position, etc.

### 3. Related Code Modules
- **`NEBULASimDataConverter_TArtNEBULAPla`**: Responsible for converting simulation data to `TArtNEBULAPla` format and writing to ROOT files.
- **`NEBULASD`**: Implements the sensitive detector, responsible for collecting particle hit information during simulation.
- **`NEBULASimParameterReader`**: Reads detector parameters and determines the output data structure and content.

## TArtNEBULAPla Data Structure

`TArtNEBULAPla` is a data structure class in the ANAROOT framework used to describe a single NEBULA detector module (Plastic Scintillator). Its main function is to store and manage the experimental or simulated response information of each NEBULA plastic bar for subsequent physics analysis and data processing.

### 1. Main Member Variables (Common Fields)
- **Detector ID**: Unique identifier for each NEBULA plastic bar, for positioning and distinction.
- **Energy**: Records the energy deposited by particles in the plastic bar (usually in MeV), used for spectrum analysis and event selection.
- **Time**: Records the time information when particles hit the plastic bar (e.g., TOF), used for time resolution and event reconstruction.
- **Position**: Spatial coordinates of the plastic bar in the array, for spatial distribution analysis and geometry reconstruction.
- **Particle Type (ParticleID)**: Records the type of particle hitting the plastic bar (e.g., neutron, gamma, heavy ion), for physics process distinction.
- **Resolution/Signal Processing Variables**: May include resolution, signal amplitude, PMT response, etc., in simulation or experiment.

### 2. TArtNEBULAPla.h
```cpp
#ifndef _TARTNEBULAPLA_H_
#define _TARTNEBULAPLA_H_

#include "TString.h"

#include <iostream>

#include "TArtDataObject.hh"

class TArtNEBULAPla : public TArtDataObject
{
public:
  TArtNEBULAPla()
    : TArtDataObject(),
      fLayer(-1), fSubLayer(-1), fHit(0),
      fQURaw(-1), fQDRaw(-1), fQUCal(-1), fQDCal(-1),
      fQAvePed(-1), fQAveCal(-1), fLogQPed(0), fLogQCal(0),
      fIvSqrtQUPed(-1), fIvSqrtQDPed(-1), fIvSqrtQAvePed(-1), 
      fTURaw(-1), fTDRaw(-1), fTURaw_Trailing(-1), fTDRaw_Trailing(-1), fTURaw_Width(-1), fTDRaw_Width(-1), 
      fTURawRef(-1), fTDRawRef(-1), fTURaw_SubTRef(-99999), fTDRaw_SubTRef(-99999), 
      fTUMulti(0), fTDMulti(0), 
      fTUCal(-1), fTDCal(-1), fTUCal_Width(-1), fTDCal_Width(-1), fTUSlw(-1), fTDSlw(-1),
      fDTRaw(-1), fDTCal(-1), fDTSlw(-1), fTAveRaw(-1), fTAveCal(-1), fTAveSlw(-1),
      fTUCalT0(-1), fTDCalT0(-1), fTUSlwT0(-1), fTDSlwT0(-1), fTAveCalT0(-1), fTAveSlwT0(-1),
      fTTOFGamma(-90000), fTTOFNeutron(-90000),
      fPosCal(0), fPosSlw(0), fFlightLength(-1), fFlightAngle(-1)
  {
    for(Int_t i=0; i<3; ++i) fDetPos[i] = -90000;
    for(Int_t i=0; i<3; ++i) fPos[i] = -90000;
  }
  virtual ~TArtNEBULAPla(){;}

  virtual void SetLayer(Int_t val){fLayer = val;}
  virtual void SetSubLayer(Int_t val){fSubLayer = val;}
  virtual void SetDetPos(const Double_t* val){for(Int_t i=0; i<3; ++i){fDetPos[i] = val[i];}}
  virtual void SetDetPos(Double_t val, Int_t i){fDetPos[i] = val;}
  virtual void SetHit(Int_t val){fHit = val;}

  virtual void SetQURaw(Int_t    val){fQURaw = val;}
  virtual void SetQDRaw(Int_t    val){fQDRaw = val;}
  virtual void SetQUPed(Double_t val){fQUPed = val;}
  virtual void SetQDPed(Double_t val){fQDPed = val;}
  virtual void SetQUCal(Double_t val){fQUCal = val;}
  virtual void SetQDCal(Double_t val){fQDCal = val;}
  virtual void SetQAvePed(Double_t val){fQAvePed = val;}
  virtual void SetQAveCal(Double_t val){fQAveCal = val;}
  virtual void SetLogQPed(Double_t val){fLogQPed = val;}
  virtual void SetLogQCal(Double_t val){fLogQCal = val;}
  virtual void SetIvSqrtQUPed(Double_t val){fIvSqrtQUPed = val;}
  virtual void SetIvSqrtQDPed(Double_t val){fIvSqrtQDPed = val;}
  virtual void SetIvSqrtQAvePed(Double_t val){fIvSqrtQAvePed = val;}

  virtual void SetTURaw(Int_t    val){fTURaw = val;}
  virtual void SetTDRaw(Int_t    val){fTDRaw = val;}
  virtual void SetTURaw_Trailing(Int_t    val){fTURaw_Trailing = val;}
  virtual void SetTDRaw_Trailing(Int_t    val){fTDRaw_Trailing = val;}
  virtual void SetTURaw_Width(Int_t    val){fTURaw_Width = val;}
  virtual void SetTDRaw_Width(Int_t    val){fTDRaw_Width = val;}
  virtual void SetTURawRef(Int_t val){fTURawRef = val;}
  virtual void SetTDRawRef(Int_t val){fTDRawRef = val;}
  virtual void SetTURaw_SubTRef(Int_t val){fTURaw_SubTRef = val;}
  virtual void SetTDRaw_SubTRef(Int_t val){fTDRaw_SubTRef = val;}
  virtual void SetTUMulti(Int_t val){fTUMulti = val;}  
  virtual void SetTDMulti(Int_t val){fTDMulti = val;}  
  virtual void SetTUCal(Double_t val){fTUCal = val;}
  virtual void SetTDCal(Double_t val){fTDCal = val;}
  virtual void SetTUCal_Width(Double_t val){fTUCal_Width = val;}
  virtual void SetTDCal_Width(Double_t val){fTDCal_Width = val;}
  virtual void SetTUSlw(Double_t val){fTUSlw = val;}
  virtual void SetTDSlw(Double_t val){fTDSlw = val;}
  virtual void SetDTRaw(Double_t val){fDTRaw = val;}
  virtual void SetDTCal(Double_t val){fDTCal = val;}
  virtual void SetDTSlw(Double_t val){fDTSlw = val;}
  virtual void SetTAveRaw(Double_t val){fTAveRaw = val;}
  virtual void SetTAveCal(Double_t val){fTAveCal = val;}
  virtual void SetTAveSlw(Double_t val){fTAveSlw = val;}
  virtual void SetTUCalT0(Double_t val){fTUCalT0 = val;}
  virtual void SetTDCalT0(Double_t val){fTDCalT0 = val;}
  virtual void SetTUSlwT0(Double_t val){fTUSlwT0 = val;}
  virtual void SetTDSlwT0(Double_t val){fTDSlwT0 = val;}
  virtual void SetTAveCalT0(Double_t val){fTAveCalT0 = val;}
  virtual void SetTAveSlwT0(Double_t val){fTAveSlwT0 = val;}
  virtual void SetTTOFGamma(Double_t val){fTTOFGamma = val;}
  virtual void SetTTOFNeutron(Double_t val){fTTOFNeutron = val;}

  virtual void SetPosCal(Double_t val){fPosCal = val;}
  virtual void SetPosSlw(Double_t val){fPosSlw = val;}
  virtual void SetPos(const Double_t* val){for(Int_t i=0; i<3; ++i) fPos[i] = val[i];}
  virtual void SetPos(Double_t val, Int_t i){fPos[i] = val;}
  virtual void SetFlightLength(Double_t val){fFlightLength = val;}
  virtual void SetFlightAngle(Double_t val){fFlightAngle = val;}

  virtual Int_t GetLayer() const {return fLayer;}
  virtual Int_t GetSubLayer() const {return fSubLayer;}
  virtual const Double_t* GetDetPos() const {return fDetPos;}
  virtual Double_t GetDetPos(Int_t i) const {return fDetPos[i];}
  virtual Int_t GetHit() const {return fHit;}

  virtual Int_t    GetQURaw() const {return fQURaw;}
  virtual Int_t    GetQDRaw() const {return fQDRaw;}
  virtual Double_t GetQUPed() const {return fQUPed;}
  virtual Double_t GetQDPed() const {return fQDPed;}
  virtual Double_t GetQUCal() const {return fQUCal;}
  virtual Double_t GetQDCal() const {return fQDCal;}
  virtual Double_t GetQAvePed() const {return fQAvePed;}
  virtual Double_t GetQAveCal() const {return fQAveCal;}
  virtual Double_t GetLogQPed() const {return fLogQPed;}
  virtual Double_t GetLogQCal() const {return fLogQCal;}
  virtual Double_t GetIvSqrtQUPed() const {return fIvSqrtQUPed;}
  virtual Double_t GetIvSqrtQDPed() const {return fIvSqrtQDPed;}
  virtual Double_t GetIvSqrtQAvePed() const {return fIvSqrtQAvePed;}

  virtual Int_t    GetTURaw() const {return fTURaw;}
  virtual Int_t    GetTDRaw() const {return fTDRaw;}
  virtual Int_t    GetTURaw_Trailing() const {return fTURaw_Trailing;}
  virtual Int_t    GetTDRaw_Trailing() const {return fTDRaw_Trailing;}
  virtual Int_t    GetTURaw_Width() const {return fTURaw_Width;}
  virtual Int_t    GetTDRaw_Width() const {return fTDRaw_Width;}
  virtual Int_t    GetTURawRef() const {return fTURawRef;}
  virtual Int_t    GetTDRawRef() const {return fTDRawRef;}
  virtual Int_t    GetTURaw_SubTRef() const {return fTURaw_SubTRef;}
  virtual Int_t    GetTDRaw_SubTRef() const {return fTDRaw_SubTRef;}
  virtual Int_t    GetTUMulti() const {return fTUMulti;}
  virtual Int_t    GetTDMulti() const {return fTDMulti;}
  virtual Double_t GetTUCal() const {return fTUCal;}
  virtual Double_t GetTDCal() const {return fTDCal;}
  virtual Double_t GetTUCal_Width() const {return fTUCal_Width;}
  virtual Double_t GetTDCal_Width() const {return fTDCal_Width;}
  virtual Double_t GetTUSlw() const {return fTUSlw;}
  virtual Double_t GetTDSlw() const {return fTDSlw;}
  virtual Double_t GetDTRaw() const {return fDTRaw;}
  virtual Double_t GetDTCal() const {return fDTCal;}
  virtual Double_t GetDTSlw() const {return fDTSlw;}
  virtual Double_t GetTAveRaw() const {return fTAveRaw;}
  virtual Double_t GetTAveCal() const {return fTAveCal;}
  virtual Double_t GetTAveSlw() const {return fTAveSlw;}
  virtual Double_t GetTUCalT0() const {return fTUCalT0;}
  virtual Double_t GetTDCalT0() const {return fTDCalT0;}
  virtual Double_t GetTUSlwT0() const {return fTUSlwT0;}
  virtual Double_t GetTDSlwT0() const {return fTDSlwT0;}
  virtual Double_t GetTAveCalT0() const {return fTAveCalT0;}
  virtual Double_t GetTAveSlwT0() const {return fTAveSlwT0;}
  virtual Double_t GetTTOFGamma() const {return fTTOFGamma;}
  virtual Double_t GetTTOFNeutron() const {return fTTOFNeutron;}

  virtual Double_t GetPosCal() const {return fPosCal;}
  virtual Double_t GetPosSlw() const {return fPosSlw;}
  virtual const Double_t* GetPos() const {return fPos;}
  virtual Double_t GetPos(Int_t i) const {return fPos[i];}
  virtual Double_t GetFlightLength() const {return fFlightLength;}
  virtual Double_t GetFlightAngle() const {return fFlightAngle;}

private:
  Int_t    fLayer;  
  Int_t    fSubLayer;  
  Double_t fDetPos[3];
  Int_t    fHit;

  Int_t    fQURaw;
  Int_t    fQDRaw;
  Double_t fQUPed;
  Double_t fQDPed;
  Double_t fQUCal;
  Double_t fQDCal;
  Double_t fQAvePed;
  Double_t fQAveCal;
  Double_t fLogQPed;
  Double_t fLogQCal;
  Double_t fIvSqrtQUPed;
  Double_t fIvSqrtQDPed;
  Double_t fIvSqrtQAvePed;

  Int_t    fTURaw;
  Int_t    fTDRaw;
  Int_t    fTURaw_Trailing;
  Int_t    fTDRaw_Trailing;
  Int_t    fTURaw_Width;
  Int_t    fTDRaw_Width;
  Int_t    fTURawRef;
  Int_t    fTDRawRef;
  Int_t    fTURaw_SubTRef;
  Int_t    fTDRaw_SubTRef;
  Int_t    fTUMulti;
  Int_t    fTDMulti;
  Double_t fTUCal;
  Double_t fTDCal;
  Double_t fTUCal_Width;
  Double_t fTDCal_Width;
  Double_t fTUSlw;
  Double_t fTDSlw;
  Double_t fDTRaw;
  Double_t fDTCal;
  Double_t fDTSlw;
  Double_t fTAveRaw;
  Double_t fTAveCal;
  Double_t fTAveSlw;
  Double_t fTUCalT0;
  Double_t fTDCalT0;
  Double_t fTUSlwT0;
  Double_t fTDSlwT0;
  Double_t fTAveCalT0;
  Double_t fTAveSlwT0;
  Double_t fTTOFGamma;
  Double_t fTTOFNeutron;

  Double_t fPosCal;
  Double_t fPosSlw;
  Double_t fPos[3];
  Double_t fFlightLength;
  Double_t fFlightAngle;

  ClassDef(TArtNEBULAPla,1);
};
#endif
```

### 3. Member Variable Details

#### a. Detector Structure
- `fLayer`: Layer number (e.g., which layer in the NEBULA array).
- `fSubLayer`: Sub-layer number (grouping within the same layer).
- `fDetPos[3]`: Detector spatial coordinates (X, Y, Z), for geometry positioning.

#### b. Signal and Energy
- `fQURaw` / `fQDRaw`: Raw signals (ADC) from upper/lower ends, not calibrated.
- `fQUCal` / `fQDCal`: Calibrated signals (energy) from upper/lower ends, usually in MeV.
- `fQAveCal`: Average of upper/lower signals, commonly used for energy reconstruction.
- `fLogQCal`: Logarithmic transformation of signals, for spectrum analysis or resolution processing.
- `fIvSqrtQUPed` etc.: Signal processing variables for resolution and noise analysis.

#### c. Time
- `fTURaw` / `fTDRaw`: Raw time signals (TDC) from upper/lower ends.
- `fTUCal` / `fTDCal`: Calibrated time signals (in ns).
- `fTAveCal`: Average time of upper/lower ends, commonly used for TOF calculation.
- `fTTOFGamma` / `fTTOFNeutron`: TOF for gamma/neutron, for particle identification.

#### d. Position and Flight Parameters
- `fPosCal` / `fPosSlw`: Calibrated and slow signal values of hit position.
- `fPos[3]`: Spatial coordinates (X, Y, Z) of the hit point.
- `fFlightLength`: Flight distance from reaction point to detector.
- `fFlightAngle`: Incident angle of the particle.

#### e. Multiple Hits and Reference Signals
- `fTUMulti` / `fTDMulti`: Multiple hit counts for upper/lower ends.
- `fTURawRef` / `fTDRawRef`: Reference time signals (e.g., trigger reference).
- `fTURaw_SubTRef` / `fTDRaw_SubTRef`: Difference with reference signals.

#### f. Others
- `fHit`: Whether hit (0/1), for event selection.
- Many other signal processing variables (e.g., trailing, width, slw) for detailed analysis of detector response characteristics.
fFlightLength：粒子从反应点到探测器的飞行距离。
fFlightAngle：粒子入射角度。
5. 多重击中与参考信号
fTUMulti / fTDMulti：上/下端多重击中计数。
fTURawRef / fTDRawRef：参考时间信号（如触发参考）。
fTURaw_SubTRef / fTDRaw_SubTRef：与参考信号的差值。
6. 其他
fHit：是否被击中（0/1），用于事件筛选。
还有大量信号处理相关变量（如 trailing、width、slw），用于详细分析探测器响应特性。

