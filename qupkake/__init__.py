"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os
import logging

logger = logging.getLogger(__name__)

# Lê a variável de ambiente XTBPATH,
# ou usa esse caminho como padrão se XTBPATH não estiver definida:
XTB_LOCATION = os.environ.get(
    "XTBPATH", 
    "/usr/insilicall/ionizationpro/QupKake/xtb-6.4.1/bin/xtb"
)

logger.info(f"Checking xTB executable at: {XTB_LOCATION}")

if not os.path.exists(XTB_LOCATION):
    raise RuntimeError(
        f'xTB executable not found at: "{XTB_LOCATION}". '
        f"Please ensure the path is correct or set the XTBPATH environment variable."
    )
elif not os.access(XTB_LOCATION, os.X_OK):
    raise RuntimeError(
        f'xTB executable found at: "{XTB_LOCATION}" but is not executable. '
        f"Run `chmod +x {XTB_LOCATION}` or check permissions."
    )

logger.info("xTB executable found and verified.")
