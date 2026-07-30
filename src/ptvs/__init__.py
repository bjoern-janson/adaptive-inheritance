"""
PTVS - Predictive Trajectory Validation System

Layer 1 of the Adaptive Inheritance architecture.

PTVS provides:
- trajectory admissibility monitoring
- empirical friction detection
- Latent Branch Ratio (LBR) telemetry

Core role:

Reality
   ↓
Empirical Shift E*
   ↓
PTVS Telemetry
   ↓
LBR_t signal
   ↓
MRAT routing
"""

from .telemetry import PTVSAnalyzer, TrajectoryRecord

__all__ = [
    "PTVSAnalyzer",
    "TrajectoryRecord",
]
