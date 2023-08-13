"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight

ceiling_entity = "light.study_ceiling_group"
lamps_entity = "light.study_lamps_group"
switch_name = "Study Switch"


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = StudyLight()
    add_entities([ent])


class StudyLight(NewLight):
    """Study Light."""

    def __init__(self) -> None:
        """Initialize Study Light."""
        super(StudyLight, self).__init__(
            "Study", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities[lamps_entity] = None
        self.entities[ceiling_entity] = None
        self.entities_below_threshold = [lamps_entity]
        self.entities_above_threshold = [ceiling_entity]
        self.switch = switch_name
