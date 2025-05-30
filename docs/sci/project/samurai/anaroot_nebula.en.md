TArtCalibNEBULAHPC *nebulahpc_calib = new TArtCalibNEBULAHPC();

**Function**: This object (nebulahpc_calib) is responsible for calibrating the NEBULA High Pressure Chamber (HPC) data. The HPC is mainly used as a veto detector for neutron detection in NEBULA, to distinguish neutrons from charged particles (such as electrons or protons produced by gamma-ray conversion).

- **Input**: Reads raw data from the HPC detector (e.g., TDC timing information) from TArtEventStore.
- **Processing**:
  - Applies time calibration parameters (managed by TArtSAMURAIParameters).
  - Converts raw TDC values to physical time.
  - Performs basic hit identification.
- **Output**: Calibrated TArtNEBULAHPC objects, each containing calibrated information for an HPC hit (such as time, detector ID, etc.), stored in a "NEBULAHPC" TClonesArray in TArtStoreManager.

---

TArtCalibNEBULA *nebulapla_calib = new TArtCalibNEBULA();

**Function**: This object (nebulapla_calib) is responsible for calibrating the NEBULA plastic scintillator (Pla) data, which is the main component of the NEBULA neutron detector.

- **Input**: Reads raw data from both ends of the plastic scintillator PMTs (TDC timing and QDC charge) from TArtEventStore.
- **Processing**:
  - Applies time and charge calibration parameters.
  - Calculates the average time, time difference (for position reconstruction), and average charge for each hit.
  - Calculates the hit position.
  - Converts calibrated time and charge to physical units (ns, MeVee).
- **Output**: Calibrated TArtNEBULAPla objects, each containing detailed calibration information for a hit (ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal, etc.), stored in a "NEBULAPla" TClonesArray in TArtStoreManager.

---

TArtRecoNeutron *reco_neutron = new TArtRecoNeutron();

**Function**: This object (reco_neutron) is responsible for reconstructing neutron events from the calibrated neutron detector data. This is a higher-level reconstruction step.

- **Input**:
  - Mainly relies on the collection of TArtNEBULAPla objects produced by TArtCalibNEBULA (plastic scintillator hit information).
  - May use the output of TArtCalibNEBULAHPC (TArtNEBULAHPC objects) as a charged particle veto signal to improve neutron identification purity.
  - May also require information from other detectors (such as beam detector timing as a TOF reference).
- **Processing**:
  - Clustering: Groups TArtNEBULAPla hits that are close in space and time into potential neutron clusters.
  - Particle identification (PID): Uses charge information (dE/dx) and time-of-flight (TOF) to distinguish neutrons from other particles.
  - Time-of-flight calculation: Calculates the neutron TOF from the target (or reference detector) to NEBULA.
  - Energy reconstruction: Calculates neutron kinetic energy based on TOF and flight path length.
  - Position reconstruction: Determines the neutron interaction position.
- **Output**: Reconstructed TArtNeutron objects (or similar classes), each containing the physical properties of a neutron (energy, time, position, angle, etc.), stored in a "Neutron" TClonesArray in TArtStoreManager.

## NEBULA Reconstruction Procedure (Sample Code Workflow)

- **Initialization and Parameter Loading**
  - Load necessary libraries and headers, set include paths.
  - Obtain and load the `TArtSAMURAIParameters` parameter file.
  - Open the RIDF data file.

- **Reconstruction Class Initialization**
  - Create objects for `TArtCalibNEBULAHPC`, `TArtCalibNEBULA`, and `TArtRecoNeutron`.

- **Event Loop Processing**
  - For each event (e.g., the first 10 events), perform the following:
    - Clear data from the previous event (`ClearData()`).
    - Call `ReconstructData()` to perform hit and neutron reconstruction.
    - Retrieve and output HPC hits, Pla hits, and neutron reconstruction results.
    - Clear raw event data in preparation for the next event.

- **Output Content**
  - Output the number of HPC hits and details for each event (ID, Layer, SubLayer, TRaw, TCal, etc.).
  - Output the number of Pla hits and details (ID, Layer, SubLayer, QUAveCal, TAveCal, PosCal, etc.).
  - Output the number of reconstructed neutrons and their physical quantities (Time, MeVee, PosX, PosY, PosZ, etc.).

- **Cleanup and Resource Release**
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