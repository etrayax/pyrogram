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

import asyncio
import inspect
import logging
from collections import OrderedDict

import pyrogram
from pyrogram import utils
from pyrogram.handlers import *

from pyrogram.raw.types import (
    UpdateNewMessage,
    UpdateNewChannelMessage,
    UpdateNewScheduledMessage,
    UpdateEditMessage,
    UpdateEditChannelMessage,
    UpdateDeleteMessages,
    UpdateDeleteChannelMessages,
    UpdateBotCallbackQuery,
    UpdateInlineBotCallbackQuery,
    UpdateUserStatus,
    UpdateBotInlineQuery,
    UpdateMessagePoll,
    UpdateBotInlineSend,
    UpdateChatParticipant,
    UpdateChannelParticipant,
    UpdateBotChatInviteRequester,
    UpdateBotMessageReaction,
    UpdateMessageReactions,
    UpdateBotPrecheckoutQuery,
    UpdateBotBusinessConnect,
    UpdateBotNewBusinessMessage,
    UpdateBotEditBusinessMessage,
    UpdateBotDeleteBusinessMessage
)

from typing import Callable

log = logging.getLogger(__name__)


class Handler:
    def __init__(self, parser, handler):
        self.parser = parser
        self.handler = handler

    async def __call__(self, client, update, users, chats, **kwargs):
        return (
            await self.parser(client, update, users, chats, **kwargs),
            self.handler
        )


class Dispatcher:

    def __init__(self, client: "pyrogram.Client"):
        self.client = client
        self.loop = asyncio.get_event_loop()

        self.handler_worker_tasks = []
        self.locks_list = []

        self.updates_queue = asyncio.Queue()
        self.groups = OrderedDict()

        self.update_parsers = {
            UpdateNewMessage: NewMessageHandler,
            UpdateNewChannelMessage: NewChannelMessageHandler,
            UpdateNewScheduledMessage: NewScheduledMessageHandler,
            UpdateEditMessage: EditMessageHandler,
            UpdateEditChannelMessage: EditChannelMessageHandler,
            UpdateBotNewBusinessMessage: BotNewBusinessMessageHandler,
            UpdateBotEditBusinessMessage: BotEditBusinessMessageHandler,
            UpdateDeleteMessages: DeleteMessagesHandler,
            UpdateDeleteChannelMessages: DeleteChannelMessagesHandler,
            UpdateBotCallbackQuery: BotCallbackQueryHandler,
            UpdateInlineBotCallbackQuery: InlineBotCallbackQueryHandler,
            UpdateUserStatus: UserStatusHandler,
            UpdateBotInlineQuery: BotInlineQueryHandler,
            UpdateMessagePoll: MessagePollHandler,
            UpdateBotInlineSend: BotInlineSendHandler,
            UpdateChatParticipant: ChatParticipantHandler,
            UpdateChannelParticipant: ChannelParticipantHandler,
            UpdateBotChatInviteRequester: BotChatInviteRequesterHandler,
            UpdateBotMessageReaction: BotMessageReactionHandler,
            UpdateMessageReactions: MessageReactionsHandler,
            UpdateBotBusinessConnect: BotBusinessConnectHandler,
            UpdateBotDeleteBusinessMessage: BotDeleteBusinessMessageHandler

        }

        self.update_parsers = {key: value for key, value in self.update_parsers.items()}

    async def parser(self, update, users, chats):

        if isinstance(update, (
                UpdateNewMessage, UpdateNewChannelMessage, UpdateNewScheduledMessage, UpdateEditMessage,
                UpdateEditChannelMessage, UpdateBotNewBusinessMessage, UpdateBotEditBusinessMessage)):
            return await pyrogram.types.Message._parse(
                self.client,
                update,
                users,
                chats,
                is_scheduled=isinstance(update, UpdateNewScheduledMessage),
            )

        if isinstance(update, (UpdateDeleteMessages, UpdateDeleteChannelMessages)):
            return utils.parse_deleted_messages(self.client, update)

        if isinstance(update, (UpdateBotCallbackQuery, UpdateInlineBotCallbackQuery)):
            return await pyrogram.types.CallbackQuery._parse(self.client, update, users)

        if isinstance(update, UpdateUserStatus):
            return pyrogram.types.User._parse_user_status(self.client, update)

        if isinstance(update, UpdateBotInlineQuery):
            return pyrogram.types.InlineQuery._parse(self.client, update, users),

        if isinstance(update, UpdateMessagePoll):
            return pyrogram.types.Poll._parse_update(self.client, update)

        if isinstance(update, UpdateBotInlineSend):
            return pyrogram.types.ChosenInlineResult._parse(self.client, update, users)

        if isinstance(update, (UpdateChatParticipant, UpdateChannelParticipant)):
            return pyrogram.types.ChatMemberUpdated._parse(self.client, update, users, chats)

        if isinstance(update, UpdateBotChatInviteRequester):
            return pyrogram.types.ChatJoinRequest._parse(self.client, update, users, chats)

        if isinstance(update, UpdateBotMessageReaction):
            return pyrogram.types.MessageReactionUpdated._parse(self.client, update, users, chats)

        if isinstance(update, UpdateMessageReactions):
            return pyrogram.types.MessageReactionCountUpdated._parse(self.client, update, users, chats)

        if isinstance(update, UpdateBotBusinessConnect):
            return pyrogram.types.BusinessConnection._parse(self.client, update, users, chats)

        if isinstance(update, UpdateBotDeleteBusinessMessage):
            return pyrogram.types.BusinessMessagesDeleted._parse(self.client, update, users, chats)

    async def start(self):
        if not self.client.no_updates:
            for i in range(self.client.workers):
                self.locks_list.append(asyncio.Lock())

                self.handler_worker_tasks.append(
                    self.loop.create_task(self.handler_worker(self.locks_list[-1]))
                )

            log.info("Started %s HandlerTasks", self.client.workers)

    async def stop(self):
        if not self.client.no_updates:
            for i in range(self.client.workers):
                self.updates_queue.put_nowait(None)

            for i in self.handler_worker_tasks:
                await i

            self.handler_worker_tasks.clear()
            self.groups.clear()

            log.info("Stopped %s HandlerTasks", self.client.workers)

    def add_handler(self, handler, group: int):
        async def fn():
            for lock in self.locks_list:
                await lock.acquire()

            try:
                if group not in self.groups:
                    self.groups[group] = []
                    self.groups = OrderedDict(sorted(self.groups.items()))

                self.groups[group].append(handler)
            finally:
                for lock in self.locks_list:
                    lock.release()

        self.loop.create_task(fn())

    def remove_handler(self, handler, group: int):
        async def fn():
            for lock in self.locks_list:
                await lock.acquire()

            try:
                if group not in self.groups:
                    raise ValueError(f"Group {group} does not exist. Handler was not removed.")

                self.groups[group].remove(handler)
            finally:
                for lock in self.locks_list:
                    lock.release()

        self.loop.create_task(fn())

    async def handler_worker(self, lock):
        while True:
            packet = await self.updates_queue.get()

            if packet is None:
                break

            try:
                update, users, chats = packet
                get_handler = self.update_parsers.get(type(update), None)

                parsed_update, handler_type = (
                    await self.parser(update, users, chats)
                    if get_handler is not None
                    else (None, type(None)),
                    get_handler
                )

                async with lock:
                    for group in self.groups.values():
                        for handler in group:
                            args = None

                            if isinstance(handler, handler_type):
                                try:
                                    if await handler.check(self.client, parsed_update):
                                        args = (parsed_update,)
                                except Exception as e:
                                    log.exception(e)
                                    continue

                            elif isinstance(handler, RawUpdateHandler):
                                args = (update, users, chats)

                            if args is None:
                                continue

                            try:
                                if inspect.iscoroutinefunction(handler.callback):
                                    await handler.callback(self.client, *args)
                                else:
                                    await self.loop.run_in_executor(
                                        self.client.executor,
                                        handler.callback,
                                        self.client,
                                        *args
                                    )
                            except pyrogram.StopPropagation:
                                raise
                            except pyrogram.ContinuePropagation:
                                continue
                            except Exception as e:
                                log.exception(e)

                            break
            except pyrogram.StopPropagation:
                pass
            except Exception as e:
                log.exception(e)
