"""VoxCPM: A speech recognition and processing toolkit based on CPM architecture."""

__version__ = "1.5.0"
__author__ = "VoxCPM Contributors"
__license__ = "Apache 2.0"

from voxcpm.model import VoxCPM
from voxcpm.processor import AudioProcessor

__all__ = ["VoxCPM", "AudioProcessor"]
