---
title: Detailed Explanation of RIKEN RIDF File Structure: Data Block (Block) Description
---

# Detailed Explanation of RIKEN RIDF File Structure: Data Block (Block) Description

RIKEN's RIDF (RIBF Data Format) file is a **binary file**, and its basic unit is the **data block (Block)**. The entire file consists of a series of such data blocks arranged sequentially. Each data block describes specific information, such as raw detector data, event information, scaler data, comments, or status information.

The nested structure of [block[segment[data point]]]:

[Event [[Event Header], [Data Segment 1 [[Segment Header 1], [Data Point Set 1]]], [Data Segment 2 [[Segment Header 2], [Data Point Set 2]]], ...]]

---

## General Block Structure

Each data block begins with one or more **Header Word(s)**, which define the attributes and type of the data block. The most critical is the first header word, typically 32 bits (4 bytes) in size, structured as follows:

1.  **First Header Word (32 bits)**:
    * **`Revision` (2 bits)**: The version number of the block format. Typically `0b00` (decimal 0), representing version 1.
    * **`Layer` (2 bits)**: Defines the depth of the data block in the hierarchical structure. For example, a top-level block might be Layer 0, and its sub-blocks might be Layer 1, and so on.
    * **`Class ID` (6 bits)**: **This is the key field that distinguishes the type of data block.** Different `Class ID` values represent different types of data blocks, such as event data, raw data segments, comments, etc. We will detail some common `Class ID` values below.
    * **`Block Size` (22 bits)**: Defines the **total size of the entire data block**, measured in **short words (2 bytes each)**. This size includes the header word(s) and all subsequent data. This field allows the reading program to determine how much data to read to fully retrieve the current block and locate the starting position of the next block.

2.  **Address Word (32 bits) (usually immediately following the first header word)**:
    * This 32-bit word is typically used to identify the source of the data. For data blocks generated by front-end electronics modules (e.g., VME modules), this address word is often the **Event Fragment ID**, or it may represent the IP address or other identifier of the front-end computer that generated the data.

**Thus, a typical data block usually contains at least 8 bytes of header information (the first header word + address word).** The subsequent content is entirely determined by the `Class ID`.

---

## Data Block Content Determined by `Class ID`

The `Class ID` tells us what kind of data is contained in the block. Below are some common and important `Class ID` values in RIDF and their corresponding data block meanings:

* **`Class ID = 0`: Event Fragment**
    * **Purpose**: Represents a data packet about an "event" sent from an independent data source (e.g., a data acquisition card, a front-end computer, or a subsystem).
    * **Typical Content**:
        * Standard header word(s) and address word (the address word is usually the unique ID of this fragment).
        * May contain a fragment-specific header, such as a timestamp or trigger information.
        * **Core Content**: Usually contains one or more **Segment Blocks (`Class ID = 4`)**, which hold raw data from different detectors or electronics modules.

* **`Class ID = 1`: Event Assembly**
    * **Purpose**: Combines data from different sources (i.e., multiple event fragments, `Class ID = 0`) that belong to the same physical event. This is the result of the event building process.
    * **Typical Content**:
        * Standard header word(s) and address word.
        * May contain a global event header, such as a global event number or global timestamp.
        * Contains multiple previously described **Event Fragment Blocks (Event Fragment)**.

* **`Class ID = 4`: Segment**
    * **Purpose**: **This is the most basic unit containing actual raw detector data and is very important!**
    * **Typical Content**:
        * Standard header word(s) and address word (the address word may have specific meanings at this level or be inherited from the parent block).
        * **Segment Header**: A header specific to this data segment, typically containing:
            * **`Segment ID`**: An integer uniquely identifying the source of this data segment (e.g., which detector, which module). The `Segment ID` itself is often structurally defined, including device, focal plane, detector type, and module number information.
            * Data type indicator: Specifies the exact format of the subsequent data (e.g., ADC data, TDC data, pattern words, etc.).
            * Channel count or data word count, etc.
        * **Data Payload**: The actual raw data values (e.g., ADC conversion results, TDC time measurements, etc.).

* **`Class ID = 5`: Comment Block**
    * **Purpose**: Used to embed textual comments in the data file, such as run numbers, experimental conditions, operator notes, etc.
    * **Typical Content**:
        * Standard header word(s) and address word.
        * A field specifying the length of the comment.
        * Actual ASCII or UTF-8 text string.

* **`Class ID = 11, 12, 13`: Scaler Block**
    * **Purpose**: Stores values of various scalers (e.g., beam intensity counts, trigger rate counts, etc.).
    * `Class ID = 11`: Non-cleared scaler (24 bits)
    * `Class ID = 12`: Cleared scaler (24 bits)
    * `Class ID = 13`: Non-cleared scaler (32 bits)
    * **Typical Content**:
        * Standard header word(s) and address word.
        * Usually contains a field indicating the number of scaler channels.
        * A series of scaler values.

* **`Class ID = 16`: Timestamp Block**
    * **Purpose**: Records timestamp information, often used for event synchronization, dead time calculation, etc.
    * **Typical Content**:
        * Standard header word(s) and address word.
        * One or more high-precision timestamp values.

* **`Class ID = 21`: Status Block**
    * **Purpose**: Records the status information of the DAQ system or experiment.
    * **Typical Content**:
        * Standard header word(s) and address word.
        * **`Status ID`**: Further subdivides the status type.
            * `Status ID = 11`: Run start status, typically containing **XML-formatted text** describing various configurations and parameters at the start of the run.
            * `Status ID = 12`: Run end status, also containing **XML-formatted text** recording information at the end of the run.
        * Status data itself (e.g., XML text content).

---

## Hierarchical Nature

It is important to understand the hierarchical structure of RIDF. A high-level data block (e.g., `Class ID = 1` Event Assembly Block) can contain multiple lower-level data blocks (e.g., multiple `Class ID = 0` Event Fragment Blocks), and an Event Fragment Block can contain multiple `Class ID = 4` Segment Blocks. The `Block Size` field ensures that decoding software can correctly skip or enter these nested blocks.

This structure makes the data both organized and highly flexible, capable of meeting the needs of RIKEN's complex nuclear physics experiments. Software for decoding RIDF files (e.g., ANAROOT) parses these data blocks one by one, identifies their `Class ID`, and extracts valid data based on the definitions of different block types.



You can use this macros to convert RIDF to human readble data.
```
#include <fstream> // Add file stream header
#include <iostream> // Add to use std::cerr

void convertRIDFtoReadable(const char* ridfFile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0013.ridf") {
    // Load necessary libraries
    gSystem->Load("libanacore.so");

    // Open RIDF file
    TArtEventStore *estore = new TArtEventStore();
    if (!estore->Open(ridfFile)) {
        std::cerr << "Error: Failed to open RIDF file: " << ridfFile << std::endl;
        return;
    }

    TArtRawEventObject *rawevent = estore->GetRawEventObject();

    // Open output file
    std::ofstream outFile("readable.txt");
    if (!outFile.is_open()) {
        std::cerr << "Error: Failed to open output file: readable.txt" << std::endl;
        return;
    }

    int neve = 0; // Event counter
    while (estore->GetNextEvent() && neve < 10) { // Only process the first 10 blocks
        outFile << "==================== Event " << neve + 1 << " ====================" << std::endl;

        // Iterate over all segments in the current event
        for (int i = 0; i < rawevent->GetNumSeg(); i++) {
            TArtRawSegmentObject *seg = rawevent->GetSegment(i);
            outFile << "Segment " << i + 1 << ":" << std::endl;
            outFile << "  Device: " << seg->GetDevice() << std::endl;
            outFile << "  FP: " << seg->GetFP() << std::endl;
            outFile << "  Detector: " << seg->GetDetector() << std::endl;
            outFile << "  Module: " << seg->GetModule() << std::endl;
            outFile << "  NumData: " << seg->GetNumData() << std::endl;

            // Iterate over all data points in the segment
            for (int j = 0; j < seg->GetNumData(); j++) {
                TArtRawDataObject *d = seg->GetData(j);
                int geo = d->GetGeo();
                int ch = d->GetCh();
                int val = d->GetVal();
                int cat = d->GetCategoryID();
                int det = d->GetDetectorID();
                int id = d->GetDatatypeID();

                outFile << "    Data " << j + 1 << ":" << std::endl;
                outFile << "      Geo: " << geo << std::endl;
                outFile << "      Channel: " << ch << std::endl;
                outFile << "      Value: " << val << std::endl;
                outFile << "      Category ID: " << cat << std::endl;
                outFile << "      Detector ID: " << det << std::endl;
                outFile << "      Datatype ID: " << id << std::endl;
            }
        }

        estore->ClearData(); // Clear current event data
        neve++;
    }

    outFile << "Conversion completed. Processed " << neve << " blocks." << std::endl;

    // Close output file
    outFile.close();

    std::cout << "Conversion completed. Results saved to readable.txt" << std::endl;
}
```

source:

https://www-nh.scphys.kyoto-u.ac.jp/~yano/ws/en/docs/documents/daq/dataformat/ridf/

https://ribf.riken.jp/RIBFDAQ/index.php?plugin=attach&refer=DAQ%2FManual%2FDataformat&openfile=dataformat_101112e.pdf