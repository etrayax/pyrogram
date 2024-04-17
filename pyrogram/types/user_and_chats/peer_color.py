#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from typing import Optional

import pyrogram
from pyrogram import raw
from pyrogram import utils
from ..object import Object


class PeerColor(Object):
    """There's nothing here.

    Parameters:
        color (``int``):
            ...

        background_emoji_id (``int``):
            ...
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        color: int,
        background_emoji_id: int,
    ):
        super().__init__(client)

        self.color = color
        self.background_emoji_id = background_emoji_id

    @staticmethod
    def _parse(client, peer_color: "raw.types.PeerColor") -> Optional["PeerColor"]:
        if isinstance(peer_color, raw.types.PeerColor):
            return PeerColor(
                client=client,
                color=peer_color.color,
                background_emoji_id=peer_color.background_emoji_id,
            )

        return None

    def write(self):
        return raw.types.PeerColor(
            color=self.color,
            background_emoji_id=self.background_emoji_id
        )
