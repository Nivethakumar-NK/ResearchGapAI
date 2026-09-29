from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent

# Data Directories
DATA_DIR = BASE_DIR / "data"

PDF_DIR = DATA_DIR / "pdfs"
EXTRACTED_DIR = DATA_DIR / "extracted"
METADATA_DIR = DATA_DIR / "metadata"
LOG_DIR = DATA_DIR / "logs"

# Create directories if they don't exist
for folder in [PDF_DIR, EXTRACTED_DIR, METADATA_DIR, LOG_DIR]:
    folder.mkdir(parents=True, exist_ok=True)