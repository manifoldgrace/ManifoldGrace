"""Offline starting point. No model calls or upstream code are executed."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    runpy.run_path(str(here.parents[1] / "tools" / "record_observation.py"),
                   init_globals={"PROJECT_DIR": here}, run_name="__main__")
