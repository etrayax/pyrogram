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

from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnEditChannelMessage:
    def on_edit_channel_message(
        self=None,
        filters=None,
        group: int = 0
    ) -> Callable:
        """Decorator for handling edit channel message.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using the
        :obj:`~pyrogram.handlers.EditChannelMessage`.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to allow only a subset of edit_channel_message to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.EditChannelMessageHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.EditChannelMessageHandler(func, self),
                        group if filters is None else filters
                    )
                )

            return func

        return decorator


