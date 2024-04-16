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

from .on_folder_peers import OnFolderPeers
from .on_read_messages_contents import OnReadMessagesContents
from .on_bot_menu_button import OnBotMenuButton
from .on_bot_inline_send import OnBotInlineSend
from .on_chat_participant_admin import OnChatParticipantAdmin
from .on_edited_message import OnEditedMessage
from .on_delete_scheduled_messages import OnDeleteScheduledMessages
from .on_bot_precheckout_query import OnBotPrecheckoutQuery
from .on_peer_wallpaper import OnPeerWallpaper
from .on_pts_changed import OnPtsChanged
from .on_story import OnStory
from .on_bot_callback_query import OnBotCallbackQuery
from .on_read_channel_discussion_outbox import OnReadChannelDiscussionOutbox
from .on_chat_participant_add import OnChatParticipantAdd
from .on_new_channel_message import OnNewChannelMessage
from .on_bot_commands import OnBotCommands
from .on_channel import OnChannel
from .on_encrypted_chat_typing import OnEncryptedChatTyping
from .on_user_typing import OnUserTyping
from .on_bot_stopped import OnBotStopped
from .on_bot_delete_business_message import OnBotDeleteBusinessMessage
from .on_dc_options import OnDcOptions
from .on_chosen_inline_result import OnChosenInlineResult
from .on_channel_web_page import OnChannelWebPage
from .on_bot_shipping_query import OnBotShippingQuery
from .on_new_sticker_set import OnNewStickerSet
from .on_user import OnUser
from .on_disconnect import OnDisconnect
from .on_chat_participants import OnChatParticipants
from .on_geo_live_viewed import OnGeoLiveViewed
from .on_raw_update import OnRawUpdate
from .on_new_encrypted_message import OnNewEncryptedMessage
from .on_read_featured_emoji_stickers import OnReadFeaturedEmojiStickers
from .on_delete_messages import OnDeleteMessages
from .on_phone_call_signaling_data import OnPhoneCallSignalingData
from .on_lang_pack_too_long import OnLangPackTooLong
from .on_channel_message_views import OnChannelMessageViews
from .on_faved_stickers import OnFavedStickers
from .on_message_id import OnMessageID
from .on_new_authorization import OnNewAuthorization
from .on_new_message import OnNewMessage
from .on_move_sticker_set_to_top import OnMoveStickerSetToTop
from .on_sticker_sets import OnStickerSets
from .on_bot_chat_invite_requester import OnBotChatInviteRequester
from .on_read_channel_discussion_inbox import OnReadChannelDiscussionInbox
from .on_sent_story_reaction import OnSentStoryReaction
from .on_message_poll_vote import OnMessagePollVote
from .on_chat_user_typing import OnChatUserTyping
from .on_bot_inline_query import OnBotInlineQuery
from .on_channel_user_typing import OnChannelUserTyping
from .on_sms_job import OnSmsJob
from .on_pinned_messages import OnPinnedMessages
from .on_short_sent_message import OnShortSentMessage
from .on_pinned_saved_dialogs import OnPinnedSavedDialogs
from .on_user_phone import OnUserPhone
from .on_channel_participant import OnChannelParticipant
from .on_peer_located import OnPeerLocated
from .on_pinned_dialogs import OnPinnedDialogs
from .on_privacy import OnPrivacy
from .on_business_message import OnBusinessMessage
from .on_phone_call import OnPhoneCall
from .on_peer_blocked import OnPeerBlocked
from .on_peer_history_ttl import OnPeerHistoryTTL
from .on_saved_reaction_tags import OnSavedReactionTags
from .on_group_call_participants import OnGroupCallParticipants
from .on_notify_settings import OnNotifySettings
from .on_bot_message_reactions import OnBotMessageReactions
from .on_quick_reply_message import OnQuickReplyMessage
from .on_read_stories import OnReadStories
from .on_read_featured_stickers import OnReadFeaturedStickers
from .on_channel_message_forwards import OnChannelMessageForwards
from .on_saved_ringtones import OnSavedRingtones
from .on_quick_replies import OnQuickReplies
from .on_user_emoji_status import OnUserEmojiStatus
from .on_channel_read_messages_contents import OnChannelReadMessagesContents
from .on_bot_chat_boost import OnBotChatBoost
from .on_channel_pinned_topics import OnChannelPinnedTopics
from .on_bot_new_business_message import OnBotNewBusinessMessage
from .on_attach_menu_bots import OnAttachMenuBots
from .on_transcribed_audio import OnTranscribedAudio
from .on_read_history_inbox import OnReadHistoryInbox
from .on_group_call import OnGroupCall
from .on_read_history_outbox import OnReadHistoryOutbox
from .on_read_channel_outbox import OnReadChannelOutbox
from .on_web_page import OnWebPage
from .on_business_connection import OnBusinessConnection
from .on_story_id import OnStoryID
from .on_combined import OnCombined
from .on_encryption import OnEncryption
from .on_message_reactions import OnMessageReactions
from .on_peer_settings import OnPeerSettings
from .on_dialog_filter_order import OnDialogFilterOrder
from .on_bot_message_reaction import OnBotMessageReaction
from .on_theme import OnTheme
from .on_pending_join_requests import OnPendingJoinRequests
from .on_saved_dialog_pinned import OnSavedDialogPinned
from .on_dialog_filter import OnDialogFilter
from .on_edit_channel_message import OnEditChannelMessage
from .on_delete_quick_reply_messages import OnDeleteQuickReplyMessages
from .on_chat_participant import OnChatParticipant
from .on_user_name import OnUserName
from .on_dialog_unread_mark import OnDialogUnreadMark
from .on_inline_bot_callback_query import OnInlineBotCallbackQuery
from .on_new_quick_reply import OnNewQuickReply
from .on_pinned_channel_messages import OnPinnedChannelMessages
from .on_bot_business_connect import OnBotBusinessConnect
from .on_saved_gifs import OnSavedGifs
from .on_recent_emoji_statuses import OnRecentEmojiStatuses
from .on_web_view_result_sent import OnWebViewResultSent
from .on_service_notification import OnServiceNotification
from .on_contacts_reset import OnContactsReset
from .on_bot_edit_business_message import OnBotEditBusinessMessage
from .on_chat import OnChat
from .on_group_call_connection import OnGroupCallConnection
from .on_short_chat_message import OnShortChatMessage
from .on_new_scheduled_message import OnNewScheduledMessage
from .on_poll import OnPoll
from .on_edited_business_message import OnEditedBusinessMessages
from .on_bot_webhookjson import OnBotWebhookJSON
from .on_encrypted_messages_read import OnEncryptedMessagesRead
from .on_auto_save_settings import OnAutoSaveSettings
from .on_message_reaction_count import OnMessageReactionCount
from .on_channel_too_long import OnChannelTooLong
from .on_inline_query import OnInlineQuery
from .on_user_status import OnUserStatus
from .on_deleted_business_messages import OnDeletedBusinessMessages
from .on_dialog_pinned import OnDialogPinned
from .on_dialog_filters import OnDialogFilters
from .on_sticker_sets_order import OnStickerSetsOrder
from .on_recent_stickers import OnRecentStickers
from .on_too_long import OnTooLong
from .on_login_token import OnLoginToken
from .on_message_poll import OnMessagePoll
from .on_chat_join_request import OnChatJoinRequest
from .on_message_extended_media import OnMessageExtendedMedia
from .on_chat_default_banned_rights import OnChatDefaultBannedRights
from .on_message_reaction import OnMessageReaction
from .on_chat_member_updated import OnChatMemberUpdated
from .on_short import OnShort
from .on_bot_webhookjson_query import OnBotWebhookJSONQuery
from .on_edit_message import OnEditMessage
from .on_channel_available_messages import OnChannelAvailableMessages
from .on_config import OnConfig
from .on_stories_stealth_mode import OnStoriesStealthMode
from .on_callback_query import OnCallbackQuery
from .on_lang_pack import OnLangPack
from .on_channel_view_forum_as_messages import OnChannelViewForumAsMessages
from .on_read_channel_inbox import OnReadChannelInbox
from .on_draft_message import OnDraftMessage
from .on_delete_channel_messages import OnDeleteChannelMessages
from .on_chat_participant_delete import OnChatParticipantDelete
from .on_recent_reactions import OnRecentReactions
from .on_delete_quick_reply import OnDeleteQuickReply
from .on_channel_pinned_topic import OnChannelPinnedTopic
from .on_short_message import OnShortMessage


class Decorators(
    OnFolderPeers,
    OnReadMessagesContents,
    OnBotMenuButton,
    OnBotInlineSend,
    OnChatParticipantAdmin,
    OnEditedMessage,
    OnDeleteScheduledMessages,
    OnBotPrecheckoutQuery,
    OnPeerWallpaper,
    OnPtsChanged,
    OnStory,
    OnBotCallbackQuery,
    OnReadChannelDiscussionOutbox,
    OnChatParticipantAdd,
    OnNewChannelMessage,
    OnBotCommands,
    OnChannel,
    OnEncryptedChatTyping,
    OnUserTyping,
    OnBotStopped,
    OnBotDeleteBusinessMessage,
    OnDcOptions,
    OnChosenInlineResult,
    OnChannelWebPage,
    OnBotShippingQuery,
    OnNewStickerSet,
    OnUser,
    OnDisconnect,
    OnChatParticipants,
    OnGeoLiveViewed,
    OnRawUpdate,
    OnNewEncryptedMessage,
    OnReadFeaturedEmojiStickers,
    OnDeleteMessages,
    OnPhoneCallSignalingData,
    OnLangPackTooLong,
    OnChannelMessageViews,
    OnFavedStickers,
    OnMessageID,
    OnNewAuthorization,
    OnNewMessage,
    OnMoveStickerSetToTop,
    OnStickerSets,
    OnBotChatInviteRequester,
    OnReadChannelDiscussionInbox,
    OnSentStoryReaction,
    OnMessagePollVote,
    OnChatUserTyping,
    OnBotInlineQuery,
    OnChannelUserTyping,
    OnSmsJob,
    OnPinnedMessages,
    OnShortSentMessage,
    OnPinnedSavedDialogs,
    OnUserPhone,
    OnChannelParticipant,
    OnPeerLocated,
    OnPinnedDialogs,
    OnPrivacy,
    OnBusinessMessage,
    OnPhoneCall,
    OnPeerBlocked,
    OnPeerHistoryTTL,
    OnSavedReactionTags,
    OnGroupCallParticipants,
    OnNotifySettings,
    OnBotMessageReactions,
    OnQuickReplyMessage,
    OnReadStories,
    OnReadFeaturedStickers,
    OnChannelMessageForwards,
    OnSavedRingtones,
    OnQuickReplies,
    OnUserEmojiStatus,
    OnChannelReadMessagesContents,
    OnBotChatBoost,
    OnChannelPinnedTopics,
    OnBotNewBusinessMessage,
    OnAttachMenuBots,
    OnTranscribedAudio,
    OnReadHistoryInbox,
    OnGroupCall,
    OnReadHistoryOutbox,
    OnReadChannelOutbox,
    OnWebPage,
    OnBusinessConnection,
    OnStoryID,
    OnCombined,
    OnEncryption,
    OnMessageReactions,
    OnPeerSettings,
    OnDialogFilterOrder,
    OnBotMessageReaction,
    OnTheme,
    OnPendingJoinRequests,
    OnSavedDialogPinned,
    OnDialogFilter,
    OnEditChannelMessage,
    OnDeleteQuickReplyMessages,
    OnChatParticipant,
    OnUserName,
    OnDialogUnreadMark,
    OnInlineBotCallbackQuery,
    OnNewQuickReply,
    OnPinnedChannelMessages,
    OnBotBusinessConnect,
    OnSavedGifs,
    OnRecentEmojiStatuses,
    OnWebViewResultSent,
    OnServiceNotification,
    OnContactsReset,
    OnBotEditBusinessMessage,
    OnChat,
    OnGroupCallConnection,
    OnShortChatMessage,
    OnNewScheduledMessage,
    OnPoll,
    OnEditedBusinessMessages,
    OnBotWebhookJSON,
    OnEncryptedMessagesRead,
    OnAutoSaveSettings,
    OnMessageReactionCount,
    OnChannelTooLong,
    OnInlineQuery,
    OnUserStatus,
    OnDeletedBusinessMessages,
    OnDialogPinned,
    OnDialogFilters,
    OnStickerSetsOrder,
    OnRecentStickers,
    OnTooLong,
    OnLoginToken,
    OnMessagePoll,
    OnChatJoinRequest,
    OnMessageExtendedMedia,
    OnChatDefaultBannedRights,
    OnMessageReaction,
    OnChatMemberUpdated,
    OnShort,
    OnBotWebhookJSONQuery,
    OnEditMessage,
    OnChannelAvailableMessages,
    OnConfig,
    OnStoriesStealthMode,
    OnCallbackQuery,
    OnLangPack,
    OnChannelViewForumAsMessages,
    OnReadChannelInbox,
    OnDraftMessage,
    OnDeleteChannelMessages,
    OnChatParticipantDelete,
    OnRecentReactions,
    OnDeleteQuickReply,
    OnChannelPinnedTopic,
    OnShortMessage,
):
    pass
