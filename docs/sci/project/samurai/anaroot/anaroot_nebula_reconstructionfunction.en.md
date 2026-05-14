# TArtCalibNEBULA::ReconstructData — Full Walk-through

This code implements the `TArtCalibNEBULA::ReconstructData()` method, which reconstructs and calibrates physical quantities for each NEBULA plastic-scintillator (Pla) module.

## Overall flow

1. If raw data are not yet loaded (`fDataLoaded` is `false`) call `LoadData()`.
2. Three position offsets (`posxoff`, `posyoff`, `poszoff`) are declared. Currently all set to 0 — placeholders for future bar-level alignment.
3. Loop over all NEBULA Pla modules (`GetNumNEBULAPla()` / `GetNEBULAPla(i)`).
4. For each module:
   - Look up its parameter object (`para`) by ID. If missing → skip.
   - If the module is a `Tref` (timing reference) channel → skip.
   - Retrieve reference times `tref_u`, `tref_d` for both PMT ends.
   - Compute raw widths (leading − trailing), TRef-subtracted times, raw charges, etc.
   - Optional global T0 calibration (`fT0Array`).
   - Mark hit type via `hit` bitmask of finite QU/QD/TU/TD signals.
   - Subtract pedestals, apply linear calibration, optional log transform, compute averages and ratios.
   - Apply slewing correction (5-term log-polynomial form if `TUSlwLog[0]!=0`, otherwise classic `TUSlw/sqrt(quped)`).
   - Reconstruct position from time difference `dt = tdslw − tuslw` and the geometric parameters in `para`.
   - Correct for light attenuation in charge using reconstructed Y.
   - Compute flight length / angle and TOF for gamma and neutron hypotheses.
5. Write all results back to the `TArtNEBULAPla` object via `Set...` methods and mark the module as reconstructed.
6. After the loop, set `fReconstructed = true`.

This pipeline turns raw PMT signals into the physics-grade quantities (energy in MeVee, calibrated time, 3D hit position, TOF) used by downstream NEBULA analysis.

## Key formulas

### Time calibration & slewing

```
turaw_subtref = turaw - turaw_ref
tucal         = turaw_subtref * TUCal + TUOff
tuslw         = tucal - sum_{k=0..4} c_k * log(quped)^(k+1)   # if log-poly
              = tucal - TUSlw / sqrt(quped)                    # otherwise
```

Same form for the lower PMT. The slewing correction is the leading non-linearity in time reconstruction.

### Charge calibration

```
quped   = quraw - QUPed
qucal   = quped * QUCal
qaveped = sqrt(quped * qdped)
qavecal = QAveCal * sqrt(qucal * qdcal)
```

### Position reconstruction

```
dtcal = tdcal - tucal
dtslw = tdslw - tuslw
PosCal = dtcal * DTCal + DTOff
PosSlw = dtslw * DTCal + DTOff

pos[0] = DetPos[0] + posxoff
pos[1] = PosSlw    + DetPos[1] + posyoff
pos[2] = DetPos[2] + poszoff
```

The effective light velocity inside the BC-408 bar is encoded in `DTCal` (mm per ns or per TDC channel difference, depending on units).

### Attenuation correction on charge

```
qavecal /= 1 + posY^2 * QAveCalAtt
```

This removes the position-dependent attenuation along the bar so that the final `QAveCal` is a position-independent estimate of deposited light (proportional to MeVee).

### TOF hypotheses

```
TTOFGamma   = taveslw - L / 29.979   # photons (c = 29.979 cm/ns)
TTOFNeutron = taveslw - L / 20.       # β ≈ 2/3 neutron prior
```

## Source

```cpp
void TArtCalibNEBULA::ReconstructData()
{
  if(!fDataLoaded) LoadData();
  // Common offsets — placeholders for future per-bar alignment.
  Double_t posxoff = 0;
  Double_t posyoff = 0;
  Double_t poszoff = 0;
  for(Int_t i=0;i<GetNumNEBULAPla();++i){
    TArtNEBULAPla* pla = GetNEBULAPla(i);
    Int_t id = pla->GetID();
    const TArtNEBULAPlaPara* para = FindNEBULAPlaPara(id);
    if(!para){
      TArtCore::Info(__FILE__,"cannot find para %d", id);
      continue;
    }
    if (para->IsTref()) continue;

    // TRef subtraction
    TArtRIDFMap map_u = para->GetMapTU();
    TArtRIDFMap map_d = para->GetMapTD();
    Double_t turaw_ref = GetTRef(map_u);
    Double_t tdraw_ref = GetTRef(map_d);

    Double_t turaw = pla->GetTURaw();
    Double_t tdraw = pla->GetTDRaw();
    Double_t turaw_subtref = turaw - turaw_ref;
    Double_t tdraw_subtref = tdraw - tdraw_ref;
    Double_t turaw_width   = pla->GetTURaw_Trailing() - pla->GetTURaw();
    Double_t tdraw_width   = pla->GetTDRaw_Trailing() - pla->GetTDRaw();
    Double_t quraw = pla->GetQURaw();
    Double_t qdraw = pla->GetQDRaw();

    double t0 = TArtMath::InvalidNum();
    if(fT0Array){
      if(0 == fT0Array->GetEntries()){
        TArtCore::Error(__FILE__,"CalibSAMURAIT0 seems not to be reconstructed; cannot reconstruct CalibSAMURAITZero.");
      }else{
        t0 = ((TArtTZero*)fT0Array->At(0))->GetTZeroSlw();
      }
    }

    // Hit type bitmask
    Int_t hit = 0;
    if(TMath::Finite(quraw)) hit += 1;
    if(TMath::Finite(qdraw)) hit += 2;
    if(TMath::Finite(turaw)) hit += 4;
    if(TMath::Finite(tdraw)) hit += 8;

    // Charge: pedestal subtraction, calibration, averages
    Double_t quped   = quraw - para->GetQUPed();
    Double_t qdped   = qdraw - para->GetQDPed();
    Double_t qucal   = quped * para->GetQUCal();
    Double_t qdcal   = qdped * para->GetQDCal();
    Double_t qaveped = sqrt(quped * qdped);
    Double_t qavecal = para->GetQAveCal() * sqrt(qucal * qdcal);
    // ... (linear TDC calibration, slewing, position reconstruction,
    //      attenuation correction, TOF, etc.)
  }
  fReconstructed = true;
}
```

## See also

- `anaroot_nebula.md` — complete reconstruction pipeline including `LoadData`, `TArtRecoNeutron`, `TArtNEBULAFilter`.
- `../smsimulator/nebula_simlulator.md` — corresponding Geant4 detector model used to validate this reconstruction.
