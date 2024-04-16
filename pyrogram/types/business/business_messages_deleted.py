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
from typing import Dict, List

import pyrogram
from pyrogram import raw, utils, errors
from pyrogram import types
from ..object import Object


class BusinessMessagesDeleted(Object):
    """This object is received when messages are deleted from a connected business account.

    Parameters:
        business_connection_id (``str``):
            Unique identifier of the business connection

        chat (:obj:`~pyrogram.types.Chat`):
            Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.

        message_ids (Lis of ``int``):
            list of identifiers of deleted messages in the chat of the business account

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            business_connection_id: str,
            chat: "types.Chat",
            message_ids: List[int]
    ):
        super().__init__(client)

        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids

    @staticmethod
    def _parse(
            client,
            update: "raw.types.UpdateBotDeleteBusinessMessage",
            users: Dict[int, "raw.types.User"],
            chats: Dict[int, "raw.types.Chat"],
    ) -> "BusinessMessagesDeleted":
        peer_id = utils.get_peer_id(update.peer)
        message_ids = update.messages
        user_obj = users.get(peer_id, None)

        if not user_obj and peer_id < 0:
            raise errors.PeerIdInvalid(f"{peer_id} is not a valid peer id")

        elif not update.connection_id:
            raise errors.BusinessConnectionIdInvalid()

        else:
            chat = types.Chat._parse_user_chat(client, user_obj)
            return BusinessMessagesDeleted(
                business_connection_id=update.connection_id,
                chat=chat,
                message_ids=message_ids
            )
