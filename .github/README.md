# BYU MS Core Facility - Analysis Tools

Mass Spectrometry QC and analysis tools for Brigham Young University's Fritz B. Burns Cancer Research Center MS Core Facility.

## Overview

This repository contains workflows and tools for bottom-up proteomics analysis, focusing on:
- Quality control optimization for MS Core Facility operations
- Spike-in validation and fold change analysis
- Protein identification and quantification
- Data visualization for DIA-NN output

## Quick Start

### Prerequisites
- Python 3.10+ ([Download](https://www.python.org/downloads/))
- Node.js 18+ ([Download](https://nodejs.org/)) - only for web app

### Installation

**Automated Setup (Recommended):**
```powershell
.\scripts\setup_dev.ps1
```

**Manual Setup:**
```powershell
# 1. Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies (choose one):
pip install -r requirements.txt           # Production only
pip install -e ".[dev]"                   # With dev tools (Ruff, pytest)
pip install -e ".[dev,jupyter]"           # With Jupyter support

# 3. (Optional) Install web app frontend
cd programs/mspp_web/frontend
npm install
```

## Tools

### MSPP Data Plotter (Web App)
Modern web-based interface for proteomics data visualization.

**Features:**
- Drag-and-drop TSV file upload
- Protein ID bar charts
- E.coli vs Yeast fold change analysis
- Organisms vs HeLa spike-in validation
- Grouped analysis with regex pattern matching
- Dark mode UI

**Run:**
```powershell
python programs/mspp_web/launch_app.py
```

### MSPP Data Plotter (Desktop)
Tkinter-based desktop GUI with the same analysis capabilities.

**Run:**
```powershell
python programs/pyscripts/MSPP_data_plotter.py
```

### FASTA Filter GUI
Tool for filtering FASTA files by organism patterns.

**Run:**
```powershell
python programs/pyscripts/filter_fasta_gui.py
```

## Repository Structure

```
BYU-Core-MS-Lab/
├── programs/              # Analysis tools
│   ├── mspp_web/         # Web application (React + Flask)
│   └── pyscripts/        # Desktop GUI tools
├── tutorials/            # Workflow tutorials
├── literature/           # Reference literature
├── documentations/       # Technical documentation
├── scripts/              # Setup and utility scripts
├── requirements.txt      # Python dependencies
└── pyproject.toml        # Project metadata
```

## Typical Workflow

1. **Prepare Data:** Export protein groups from DIA-NN as TSV
2. **Upload Files:** Use web app or desktop GUI
3. **Analyze:**
   - Check protein ID counts by organism
   - Validate spike-in ratios (E.coli vs Yeast)
   - Compare organisms against HeLa median
4. **Export:** Save plots for reporting

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```powershell
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

## Documentation

- [FA Workflow Tutorial](tutorials/FA_Workflow_Tutorial.md)
- [Web App README](programs/mspp_web/README.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## Links

- **GitHub:** [MSCoreLab/BYU-Core-MS-Lab](https://github.com/MSCoreLab/BYU-Core-MS-Lab)
- **BYU MS Core Facility:** [Fritz B. Burns Cancer Research Center](https://lifesciences.byu.edu/burns-cancer-center)

## Recent Updates

- ✅ Web application with React + TypeScript frontend
- ✅ Performance optimizations (5-10x faster on cached data)
- ✅ Grouped fold change analysis with pattern matching
- ✅ Dark mode UI for all visualizations

See [CHANGELOG.md](CHANGELOG.md) for full history.

---

**Maintained by:** BYU Fritz B. Burns Cancer Research Center MS Core Facility
