# Crimp Force Curves Dataset - Analysis

This repository provides the **code and structure used to validate** the [Crimp Force Curves Dataset](https://doi.org/10.7910/DVN/WBDKN6).  

## 🔗 Dataset Download

You can download the dataset from Harvard Dataverse at:

👉 **[https://doi.org/10.7910/DVN/WBDKN6](https://doi.org/10.7910/DVN/WBDKN6)**

After downloading, **place the dataset file (`.pkl`) directly in the root folder of this repository**, alongside the Python scripts (e.g. `validation.py`, `preprocessing.py`).

Expected folder structure:

```
Crimp_force_curves_dataset/
├── crimp_force_curves_dataset.pkl
├── metadata.json
├── preprocessing.py
├── validation.py
├── images.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```
## Prerequisites

- **Operating System**: Windows (tested on Windows 11)  
- **Python**: 3.11  

## Setup & Installation (Windows)

1. **Clone the repository**
   ```bash
   git clone https://github.com/BJhof/cfc-analysis.git
   cd cfc-analysis

2. **Create and activate environment**
   ```bash
    python -m venv venv
    .\venv\Scripts\activate

3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
