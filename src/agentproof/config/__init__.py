"""Typed configuration loading."""

from agentproof.config.loader import (
    ConfigError,
    ConfigProvenance,
    LoadedConfig,
    ResearchStudy,
    load_config,
    load_research_study,
)
from agentproof.config.models import ConfigKind

__all__ = [
    "ConfigError",
    "ConfigKind",
    "ConfigProvenance",
    "LoadedConfig",
    "ResearchStudy",
    "load_config",
    "load_research_study",
]
