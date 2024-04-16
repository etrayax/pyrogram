
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

from .handler import Handler


class PinnedChannelMessagesHandler(Handler):
    """The PinnedChannelMessages handler class. Used to handle pinned_channel_messages.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_pinned_channel_messages` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new PinnedChannelMessages update arrives. It takes *(client, pinned_channel_messages)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of pinned_channel_messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the pinned_channel_messages handler.

        pinned_channel_messages (:obj:`~pyrogram.types.PinnedChannelMessages`):
            The received pinned channel messages.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)

