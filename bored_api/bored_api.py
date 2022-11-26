from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional, Any

from aiohttp import ClientSession


class BoredException(Exception):
    """Base exception for the API."""

class ActivityType(Enum):
    EDUCATION = "education"
    RECREATIONAL = "recreational"
    SOCIAL = "social"
    DIY = "diy"
    CHARITY = "charity"
    COOKING = "cooking"
    RELAXATION = "relaxation"
    MUSIC = "music"
    BUSYWORK = "busywork"


@dataclass
class BoredActivity:
    activity: str
    accessibility: float
    type: ActivityType
    participants: int
    price: float
    key: int
    link: str


class BoredClient:
    BASE_URL = "http://www.boredapi.com/api/activity/?"

    async def _get_request(self, url: str) -> dict[str, Any]:
        """
        Makes a GET request to bored api
        :param url: The url.
        :return: dict[str,Any]
        """
        async with ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def get(
        self,
        *,
        key: Optional[int] = None,
        type: Optional[Union[ActivityType, str]] = None,
        participants: Optional[int] = None,
        price: Optional[float] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        accessibility: Optional[float] = None,
        min_accessibility: Optional[float] = None,
        max_accessibility: Optional[float] = None,
    ) -> BoredActivity:
        """
        Gets a event with given parameters or random event if parameters not given.

        :param key: A unique numeric id. [1000000, 9999999]
        :param type: Type of the activity.
        :param participants: The number of people that this activity could involve [0, n].
        :param price: A factor describing the cost of the event with zero being free [0, 1].
        :param min_price: The minimal price for activity. Start from 0.
        :param max_price: The maximum price for activity. Up to 1.
        :param accessibility: A factor describing how possible an event is to do with zero being the most accessible.
        :param min_accessibility: The minimal accessibility. Start from 0.
        :param max_accessibility: The maximum accessibility. Up to 1.

        :return: activity with given parameters
        :rtype: BoredActivity
        """
        payload = {}
        if key is not None:
            payload["key"] = key
        if type is not None:
            payload["type"] = type.value if isinstance(type, ActivityType) else type
        if participants is not None:
            payload["participants"] = participants
        if price is not None:
            payload["price"] = price
        if min_price is not None:
            payload["min_price"] = min_price
        if max_price is not None:
            payload["max_price"] = max_price
        if accessibility is not None:
            payload["accessibility"] = accessibility
        if min_accessibility is not None:
            payload["min_accessibility"] = min_accessibility
        if max_accessibility is not None:
            payload["max_accessibility"] = max_accessibility

        data = await self._get_request(
            self.BASE_URL
            + "&".join(
                f"{key.replace('_', '')}={value}" for key, value in payload.items()
            )
        )
        if "error" in data:
            raise BoredException(data["error"])

        if "type" in data:
            data["type"] = ActivityType[data["type"].upper()]
        if "key" in data:
            data["key"] = int(data["key"])

        return BoredActivity(**data)

    async def get_random(self) -> BoredActivity:
        """
        Find a random activity. Similar as `BoredClient().get()`.

        :return: BoredActivity
        """
        return await self.get()

    async def get_by_key(self, key: int) -> BoredActivity:
        """
        Find an activity by its key.
        :param key: A unique numeric id. Key can be in range [1000000, 9999999]

        :return: BoredActivity
        """
        return await self.get(key=key)

    async def get_by_type(self, type: Union[ActivityType, str]) -> BoredActivity:
        """
        Find a random activity with a given type.
        :param type: Type of the activity

        :return: BoredActivity
        """
        return await self.get(
            type=type.value if isinstance(type, ActivityType) else type
        )

    async def get_by_participants(self, participants: int) -> BoredActivity:
        """
        Find a random activity with a given number of participants.
        :param participants: The number of people that this activity could involve [0, n].

        :return: BoredActivity
        """
        return await self.get(participants=participants)

    async def get_by_price(self, price: float) -> BoredActivity:
        """
        Find an activity with a specified price.
        :param price: A factor describing the cost of the event with zero being free [0, 1].

        :return: BoredActivity
        """
        return await self.get(price=price)

    async def get_by_min_max_price(
        self, min_price: float, max_price: float
    ) -> BoredActivity:
        """
        Find an event with a specified price in an inclusively constrained range.
        :param min_price: The minimal price for activity. Start from 0.
        :param max_price: The maximum price for activity. Up to 1.

        :return: BoredActivity
        """
        return await self.get(min_price=min_price, max_price=max_price)

    async def get_by_accessibility(self, accessibility: float) -> BoredActivity:
        """
        Find a price in an inclusively constrained range.
        :param accessibility: A factor describing how possible an event is to do with zero being the most accessible.

        :return: BoredActivity
        """
        return await self.get(accessibility=accessibility)

    async def get_by_min_max_accessibility(
        self, min_accessibility: float, max_accessibility: float
    ) -> BoredActivity:
        """
        Find an event with a specified accessibility in an inclusively constrained range.
        :param min_accessibility: The minimal accessibility. Start from 0.
        :param max_accessibility: The maximum accessibility. Up to 1.

        :return: BoredActivity
        """
        return await self.get(
            min_accessibility=min_accessibility, max_accessibility=max_accessibility
        )
