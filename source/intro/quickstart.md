# Quick Start

This guide walks you through the basic workflow in MTDataPro.

## Step 1: Create a New Project

1. Launch MTDataPro
2. Click **File → New Project**
3. Enter a project name and select the save location
4. Click **Create**

## Step 2: Import Data

1. In the Project panel, right-click on **Sites**
2. Select **Import Data**
3. Choose your instrument type (Phoenix, Metronix, etc.)
4. Navigate to your data files and select them
5. Click **Open** to import

MTDataPro will automatically detect the sampling rate, time range, and channel configuration.

## Step 3: View Time Series

1. Double-click on an imported site in the Project panel
2. The Time Series tab will display raw data plots
3. Use the toolbar to zoom, pan, and adjust display settings
4. Right-click to access channel selection and plot options

## Step 4: Process Data

1. Select the time series you want to process
2. Click **Processing → New Process Schema**
3. Configure the processing steps:
   - Pre-filtering (e.g., remove DC offset)
   - Notch filtering (50/60 Hz)
   - FFT window selection
   - Robust processing options
4. Click **Run** to execute the processing

## Step 5: Review Results

Processed results are stored in the **Fourier Coefficients** section of each site.

## Step 6: Export Data

1. Select the data you want to export (site, group, or individual spectra)
2. Click **File → Export**
3. Choose the export format (EDI, J-format, ASCII, etc.)
4. Configure export options and click **Export**

## Next Steps

- Explore the [Tutorial](tutorial/overview/) for detailed processing workflows
- Learn about [Processing Pipelines](processing/overview/) for advanced configuration
- Review instrument-specific guides in [Modules](modules/overview/)
