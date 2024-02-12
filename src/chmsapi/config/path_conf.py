import os

from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent.parent.parent

# Log file path
LogPath = os.path.join(BasePath, 'src', 'chmsapi', 'logs')
