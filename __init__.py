import sys
from . import demucs

# This aliasing allows 'import demucs' to work after 'demucs_next' is touched
sys.modules["demucs"] = demucs