# WiSense AI

WiSense AI is a research-learning prototype with two separate modes:

- **Demo Mode** shows simulated patterns for learning and is always labeled **SIMULATED DATA**.
- **Real Data (UT-HAR)** reads a public Wi-Fi CSI dataset recorded by other researchers. It does not collect signals.

The model page runs a simple scikit-learn baseline on the provided train/validation/test split. Scores are measured on that provided split only.

The UT-HAR page uses animated stick-figure illustrations for a selected recording's class and, after training, the model's predicted class. These illustrations are not a camera view or a real person. Optional recorded-sample graphs and playback are kept in collapsed sections. Model evaluation also shows confusion-matrix heatmaps, feature importance, and per-class precision/recall.

## Run on macOS with VS Code

1. Open the project folder in VS Code.
2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
4. Install the project requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. Select the `.venv` interpreter in VS Code: press **Cmd+Shift+P**, choose **Python: Select Interpreter**, then select the interpreter inside `.venv`.
6. Start the dashboard:
   ```bash
   streamlit run app.py
   ```

## UT-HAR dataset

Download the processed UT-HAR files from the SenseFi benchmark repository:

1. Open the [SenseFi benchmark README](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark).
2. Follow **Download Processed Data** and choose **UT_HAR**.
3. Place the dataset so the project contains:
   ```text
   data/raw/benchmark/UT_HAR/
   ├── data/
   │   ├── X_train.csv
   │   ├── X_val.csv
   │   └── X_test.csv
   └── label/
       ├── y_train.csv
       ├── y_val.csv
       └── y_test.csv
   ```

These `.csv`-named files contain NumPy arrays and are loaded with NumPy, not pandas. The large training array is loaded only when a page action requests it. Extracted features are cached in `data/processed/ut_har_features.npz`; the repository ignores that directory.

UT-HAR is attributed to Yousefi et al. (2017) and distributed in the SenseFi benchmark (Yang et al., *Patterns*, 2023). See the [SenseFi repository](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) and its MIT license.

## CSV upload format

The optional CSV Upload page expects a header row with `timestamp` and `amplitude` columns. A `label` column is optional. This upload is independent of UT-HAR.

## Limitations

- Demo Mode uses simulated data only; it is not real sensing and does not produce validated predictions.
- UT-HAR recordings were collected by other researchers, not by this project, and the dashboard does not collect Wi-Fi signals.
- Class-name order is assumed from the SenseFi README; it has not been independently verified.
- It is unknown whether recordings from the same session appear in both train and test splits. Scores may be optimistic and must be described as **measured on the provided split only**.
- Performance may vary across rooms, people, and days. The baseline is a learning example, not a validated activity detector.
- Real CSI collection requires CSI-capable hardware/tools such as ESP32 with esp-csi, Intel 5300, or Atheros CSI tools; ordinary college access points do not expose CSI to applications.
# ClearPath
