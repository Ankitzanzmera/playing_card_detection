from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source:str
    local_data_file:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    data_validation_status_file:Path
    data_validation_required_file:list
    unzip_dir:Path