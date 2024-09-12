from pathlib import Path

_PACKAGEDIR = Path(__file__).parent.absolute()
_MODEL_PATH = str(_PACKAGEDIR / "models" / "kidney_model.pt")