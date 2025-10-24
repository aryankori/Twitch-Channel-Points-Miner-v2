# -*- coding: utf-8 -*-
import logging
import os
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings
from TwitchChannelPointsMiner.classes.Settings import Priority, Events
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, FilterCondition, DelayMode, OutcomeKeys, Condition
from TwitchChannelPointsMiner.classes.entities.Streamer import StreamerSettings

# Get Twitch username from environment variable
twitch_username = os.environ.get('TWITCH_USERNAME', 'your-username-here')

twitch_miner = TwitchChannelPointsMiner(
    username=twitch_username,
    claim_drops_startup=True,
    priority=[Priority.STREAK, Priority.DROPS, Priority.ORDER],
    logger_settings=LoggerSettings(
        save=True,
        console_level=logging.INFO,
        emoji=False,  # Important for server
        less=False,
        colored=False
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,
        follow_raid=True,
        claim_drops=True,
        watch_streak=True
    )
)

# Enable analytics web server for Render
twitch_miner.analytics(host='0.0.0.0', port=10000, refresh=5, days_ago=7)

# Mine followers automatically
twitch_miner.mine(followers=True)
