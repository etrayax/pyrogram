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

from pyrogram import raw
from ..object import Object


class ChatAdminRights(Object):
    """...

    Parameters:
        ...
    """

    def __init__(
        self,
        *,
        change_info: bool = None,
        post_messages: bool = None,
        edit_messages: bool = None,
        delete_messages: bool = None,
        ban_users: bool = None,
        invite_users: bool = None,
        pin_messages: bool = None,
        add_admins: bool = None,
        anonymous: bool = None,
        manage_call: bool = None,
        other: bool = None,
        manage_topics: bool = None,
        post_stories: bool = None,
        edit_stories: bool = None,
        delete_stories: bool = None,
    ):
        super().__init__(None)

        self.change_info = change_info
        self.post_messages = post_messages
        self.edit_messages = edit_messages
        self.delete_messages = delete_messages
        self.ban_users = ban_users
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.add_admins = add_admins
        self.anonymous = anonymous
        self.manage_call = manage_call
        self.other = other
        self.manage_topics = manage_topics
        self.post_stories = post_stories
        self.edit_stories = edit_stories
        self.delete_stories = delete_stories

    @staticmethod
    def _parse(permission: "raw.base.ChatAdminRights") -> "ChatAdminRights":
        if isinstance(permission, raw.types.ChatAdminRights):
            return ChatAdminRights(
                change_info=permission.change_info,
                post_messages=permission.post_messages,
                edit_messages=permission.edit_messages,
                delete_messages=permission.delete_messages,
                ban_users=permission.ban_users,
                invite_users=permission.invite_users,
                pin_messages=permission.pin_messages,
                add_admins=permission.add_admins,
                anonymous=permission.anonymous,
                manage_call=permission.manage_call,
                other=permission.other,
                manage_topics=permission.manage_topics,
                post_stories=permission.post_stories,
                edit_stories=permission.edit_stories,
                delete_stories=permission.delete_stories,
            )
