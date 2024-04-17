import pyrogram
from pyrogram import utils
from pyrogram.handlers import *
from pyrogram.raw.types import *


class Parser:

    def __init__(self, client: "pyrogram.Client"):
        self.client = client

    async def parser(self, update, users, chats):

        if isinstance(update, (
                UpdateNewMessage, UpdateNewChannelMessage, UpdateNewScheduledMessage, UpdateEditMessage,
                UpdateEditChannelMessage, UpdateBotNewBusinessMessage, UpdateBotEditBusinessMessage)):
            return await pyrogram.types.Message._parse(
                self.client,
                update.message,
                users,
                chats,
                is_scheduled=isinstance(update, UpdateNewScheduledMessage),
                connection_id=getattr(update, "connection_id", None)
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


updates = {
    UpdateNewMessage: NewMessageHandler,
    UpdateMessageID: MessageIDHandler,
    UpdateDeleteMessages: DeleteMessagesHandler,
    UpdateUserTyping: UserTypingHandler,
    UpdateChatUserTyping: ChatUserTypingHandler,
    UpdateChatParticipants: ChatParticipantsHandler,
    UpdateUserStatus: UserStatusHandler,
    UpdateUserName: UserNameHandler,
    UpdateNewAuthorization: NewAuthorizationHandler,
    UpdateNewEncryptedMessage: NewEncryptedMessageHandler,
    UpdateEncryptedChatTyping: EncryptedChatTypingHandler,
    UpdateEncryption: EncryptionHandler,
    UpdateEncryptedMessagesRead: EncryptedMessagesReadHandler,
    UpdateChatParticipantAdd: ChatParticipantAddHandler,
    UpdateChatParticipantDelete: ChatParticipantDeleteHandler,
    UpdateDcOptions: DcOptionsHandler,
    UpdateNotifySettings: NotifySettingsHandler,
    UpdateServiceNotification: ServiceNotificationHandler,
    UpdatePrivacy: PrivacyHandler,
    UpdateUserPhone: UserPhoneHandler,
    UpdateReadHistoryInbox: ReadHistoryInboxHandler,
    UpdateReadHistoryOutbox: ReadHistoryOutboxHandler,
    UpdateWebPage: WebPageHandler,
    UpdateReadMessagesContents: ReadMessagesContentsHandler,
    UpdateChannelTooLong: ChannelTooLongHandler,
    UpdateChannel: ChannelHandler,
    UpdateNewChannelMessage: NewChannelMessageHandler,
    UpdateReadChannelInbox: ReadChannelInboxHandler,
    UpdateDeleteChannelMessages: DeleteChannelMessagesHandler,
    UpdateChannelMessageViews: ChannelMessageViewsHandler,
    UpdateChatParticipantAdmin: ChatParticipantAdminHandler,
    UpdateNewStickerSet: NewStickerSetHandler,
    UpdateStickerSetsOrder: StickerSetsOrderHandler,
    UpdateStickerSets: StickerSetsHandler,
    UpdateSavedGifs: SavedGifsHandler,
    UpdateBotInlineQuery: BotInlineQueryHandler,
    UpdateBotInlineSend: BotInlineSendHandler,
    UpdateEditChannelMessage: EditChannelMessageHandler,
    UpdateBotCallbackQuery: BotCallbackQueryHandler,
    UpdateEditMessage: EditMessageHandler,
    UpdateInlineBotCallbackQuery: InlineBotCallbackQueryHandler,
    UpdateReadChannelOutbox: ReadChannelOutboxHandler,
    UpdateDraftMessage: DraftMessageHandler,
    UpdateReadFeaturedStickers: ReadFeaturedStickersHandler,
    UpdateRecentStickers: RecentStickersHandler,
    UpdateConfig: ConfigHandler,
    UpdatePtsChanged: PtsChangedHandler,
    UpdateChannelWebPage: ChannelWebPageHandler,
    UpdateDialogPinned: DialogPinnedHandler,
    UpdatePinnedDialogs: PinnedDialogsHandler,
    UpdateBotWebhookJSON: BotWebhookJSONHandler,
    UpdateBotWebhookJSONQuery: BotWebhookJSONQueryHandler,
    UpdateBotShippingQuery: BotShippingQueryHandler,
    UpdateBotPrecheckoutQuery: BotPrecheckoutQueryHandler,
    UpdatePhoneCall: PhoneCallHandler,
    UpdateLangPackTooLong: LangPackTooLongHandler,
    UpdateLangPack: LangPackHandler,
    UpdateFavedStickers: FavedStickersHandler,
    UpdateChannelReadMessagesContents: ChannelReadMessagesContentsHandler,
    UpdateContactsReset: ContactsResetHandler,
    UpdateChannelAvailableMessages: ChannelAvailableMessagesHandler,
    UpdateDialogUnreadMark: DialogUnreadMarkHandler,
    UpdateMessagePoll: MessagePollHandler,
    UpdateChatDefaultBannedRights: ChatDefaultBannedRightsHandler,
    UpdateFolderPeers: FolderPeersHandler,
    UpdatePeerSettings: PeerSettingsHandler,
    UpdatePeerLocated: PeerLocatedHandler,
    UpdateNewScheduledMessage: NewScheduledMessageHandler,
    UpdateDeleteScheduledMessages: DeleteScheduledMessagesHandler,
    UpdateTheme: ThemeHandler,
    UpdateGeoLiveViewed: GeoLiveViewedHandler,
    UpdateLoginToken: LoginTokenHandler,
    UpdateMessagePollVote: MessagePollVoteHandler,
    UpdateDialogFilter: DialogFilterHandler,
    UpdateDialogFilterOrder: DialogFilterOrderHandler,
    UpdateDialogFilters: DialogFiltersHandler,
    UpdatePhoneCallSignalingData: PhoneCallSignalingDataHandler,
    UpdateChannelMessageForwards: ChannelMessageForwardsHandler,
    UpdateReadChannelDiscussionInbox: ReadChannelDiscussionInboxHandler,
    UpdateReadChannelDiscussionOutbox: ReadChannelDiscussionOutboxHandler,
    UpdatePeerBlocked: PeerBlockedHandler,
    UpdateChannelUserTyping: ChannelUserTypingHandler,
    UpdatePinnedMessages: PinnedMessagesHandler,
    UpdatePinnedChannelMessages: PinnedChannelMessagesHandler,
    UpdateChat: ChatHandler,
    UpdateGroupCallParticipants: GroupCallParticipantsHandler,
    UpdateGroupCall: GroupCallHandler,
    UpdatePeerHistoryTTL: PeerHistoryTTLHandler,
    UpdateChatParticipant: ChatParticipantHandler,
    UpdateChannelParticipant: ChannelParticipantHandler,
    UpdateBotStopped: BotStoppedHandler,
    UpdateGroupCallConnection: GroupCallConnectionHandler,
    UpdateBotCommands: BotCommandsHandler,
    UpdatePendingJoinRequests: PendingJoinRequestsHandler,
    UpdateBotChatInviteRequester: BotChatInviteRequesterHandler,
    UpdateMessageReactions: MessageReactionsHandler,
    UpdateAttachMenuBots: AttachMenuBotsHandler,
    UpdateWebViewResultSent: WebViewResultSentHandler,
    UpdateBotMenuButton: BotMenuButtonHandler,
    UpdateSavedRingtones: SavedRingtonesHandler,
    UpdateTranscribedAudio: TranscribedAudioHandler,
    UpdateReadFeaturedEmojiStickers: ReadFeaturedEmojiStickersHandler,
    UpdateUserEmojiStatus: UserEmojiStatusHandler,
    UpdateRecentEmojiStatuses: RecentEmojiStatusesHandler,
    UpdateRecentReactions: RecentReactionsHandler,
    UpdateMoveStickerSetToTop: MoveStickerSetToTopHandler,
    UpdateMessageExtendedMedia: MessageExtendedMediaHandler,
    UpdateChannelPinnedTopic: ChannelPinnedTopicHandler,
    UpdateChannelPinnedTopics: ChannelPinnedTopicsHandler,
    UpdateUser: UserHandler,
    UpdateAutoSaveSettings: AutoSaveSettingsHandler,
    UpdateStory: StoryHandler,
    UpdateReadStories: ReadStoriesHandler,
    UpdateStoryID: StoryIDHandler,
    UpdateStoriesStealthMode: StoriesStealthModeHandler,
    UpdateSentStoryReaction: SentStoryReactionHandler,
    UpdateBotChatBoost: BotChatBoostHandler,
    UpdateChannelViewForumAsMessages: ChannelViewForumAsMessagesHandler,
    UpdatePeerWallpaper: PeerWallpaperHandler,
    UpdateBotMessageReaction: BotMessageReactionHandler,
    UpdateBotMessageReactions: BotMessageReactionsHandler,
    UpdateSavedDialogPinned: SavedDialogPinnedHandler,
    UpdatePinnedSavedDialogs: PinnedSavedDialogsHandler,
    UpdateSavedReactionTags: SavedReactionTagsHandler,
    UpdateSmsJob: SmsJobHandler,
    UpdateQuickReplies: QuickRepliesHandler,
    UpdateNewQuickReply: NewQuickReplyHandler,
    UpdateDeleteQuickReply: DeleteQuickReplyHandler,
    UpdateQuickReplyMessage: QuickReplyMessageHandler,
    UpdateDeleteQuickReplyMessages: DeleteQuickReplyMessagesHandler,
    UpdateBotBusinessConnect: BotBusinessConnectHandler,
    UpdateBotNewBusinessMessage: BotNewBusinessMessageHandler,
    UpdateBotEditBusinessMessage: BotEditBusinessMessageHandler,
    UpdateBotDeleteBusinessMessage: BotDeleteBusinessMessageHandler,
    UpdatesTooLong: TooLongHandler,
    UpdateShortMessage: ShortMessageHandler,
    UpdateShortChatMessage: ShortChatMessageHandler,
    UpdateShort: ShortHandler,
    UpdatesCombined: CombinedHandler,
    UpdateShortSentMessage: ShortSentMessageHandler,
}
