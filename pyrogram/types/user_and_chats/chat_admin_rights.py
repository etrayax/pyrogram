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
        can_change_info: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_delete_messages: bool = None,
        can_ban_users: bool = None,
        can_invite_users: bool = None,
        can_pin_messages: bool = None,
        can_add_admins: bool = None,
        can_anonymous: bool = None,
        can_manage_call: bool = None,
        can_other: bool = None,
        can_manage_topics: bool = None,
        can_post_stories: bool = None,
        can_edit_stories: bool = None,
        can_delete_stories: bool = None,
    ):
        super().__init__(None)

        self.change_info = can_change_info
        self.post_messages = can_post_messages
        self.edit_messages = can_edit_messages
        self.delete_messages = can_delete_messages
        self.ban_users = can_ban_users
        self.invite_users = can_invite_users
        self.pin_messages = can_pin_messages
        self.add_admins = can_add_admins
        self.anonymous = can_anonymous
        self.manage_call = can_manage_call
        self.other = can_other
        self.manage_topics = can_manage_topics
        self.post_stories = can_post_stories
        self.edit_stories = can_edit_stories
        self.delete_stories = can_delete_stories

    @staticmethod
    def _parse(permission: "raw.base.ChatAdminRights") -> "ChatAdminRights":
        if isinstance(permission, raw.types.ChatAdminRights):
            return ChatAdminRights(
                can_change_info=permission.change_info,
                can_post_messages=permission.post_messages,
                can_edit_messages=permission.edit_messages,
                can_delete_messages=permission.delete_messages,
                can_ban_users=permission.ban_users,
                can_invite_users=permission.invite_users,
                can_pin_messages=permission.pin_messages,
                can_add_admins=permission.add_admins,
                can_anonymous=permission.anonymous,
                can_manage_call=permission.manage_call,
                can_other=permission.other,
                can_manage_topics=permission.manage_topics,
                can_post_stories=permission.post_stories,
                can_edit_stories=permission.edit_stories,
                can_delete_stories=permission.delete_stories,
            )
