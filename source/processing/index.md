# Processing Overview

MTDataPro provides a flexible, modular processing system based on **Processing Schemas**.

## Processing Pipeline

```
Raw Time Series
      ↓
  Pre-processing
  (DC removal, despike)
      ↓
  Band-pass Filter
      ↓
  Notch Filter
  (50/60 Hz removal)
      ↓
  FFT & Windowing
      ↓
  Remote Reference
  (optional)
      ↓
  Transfer Function
  Estimation
      ↓
  Robust Processing
      ↓
  Fourier Coefficients
      ↓
  Export (EDI, etc.)
```

## Processing Schema

A Processing Schema defines a complete, reusable processing pipeline. Schemas can be:

- **Saved and loaded** for consistent processing across projects
- **Shared** between team members
- **Modified** with different parameter sets
- **Applied** to individual sites or batch processed

## Key Parameters

### FFT Window

- **Length**: Number of samples per window
- **Overlap**: Percentage of overlap between windows (typically 50%)
- **Window Type**: Hanning, Hamming, Blackman, Kaiser-Bessel, etc.

### Robust Processing

- **Iterative Reweighting**: Reduces influence of outliers
- **Threshold**: Cutoff for outlier detection
- **Max Iterations**: Convergence limit

### Remote Reference

- Requires synchronized magnetic field channels
- Uses robust remote reference algorithm
- Significantly improves processing quality in noisy environments
