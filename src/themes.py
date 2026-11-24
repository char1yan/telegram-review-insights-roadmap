"""Transparent keyword taxonomy for tagging app reviews with product themes.

A review can belong to several themes. Patterns are matched on lower-cased text.
Keeping rules in one place makes them easy to audit, extend and explain to stakeholders.
"""
import re

import pandas as pd

THEMES = {
    "Voice & video calls": r"\b(?:call|calls|calling|voice chat|video chat)\b",
    "Notifications": r"notif",
    "Crashes & bugs": r"\b(?:crash\w*|bugs?|buggy|freez\w*|hangs?|hanging|stuck|glitch\w*|force clos\w*|not working|doesn'?t work|stopped working|error)\b",
    "Speed & performance": r"\b(?:slow\w*|lag|lags|laggy|lagging)\b",
    "Connection & sync": r"\b(?:connecting|connection|connect|network|servers?|offline|sync\w*)\b",
    "Login & verification": r"\b(?:login|log ?in|sign ?in|sign ?up|register\w*|verification|verify|activation|code|otp)\b",
    "Stickers & emoji": r"\b(?:stickers?|emojis?|emoticons?|smiley\w*|smilies)\b",
    "Offensive sticker pack (incident)": r"\b(?:buddha\w*|buddhis\w*|insult\w*)\b",
    "Privacy & security": r"\b(?:secret|privacy|private|encrypt\w*|secur\w*|hack\w*)\b",
    "Media & file sharing": r"\b(?:photos?|pictures?|images?|videos?|gifs?|files?|music|audio|upload\w*|download\w*|media)\b",
    "Storage & data usage": r"\b(?:storage|cache|memory|space|data usage)\b",
    "Message controls": r"\b(?:delete\w*|unsend|edit|editing|forward\w*|schedul\w*)\b",
    "Language & localisation": r"\b(?:languages?|translat\w*|hindi|urdu|arabic|persian|farsi|kannada|tamil|bengali|locali[sz]\w*)\b",
    "UI & themes": r"\b(?:themes?|night mode|dark mode|design|interface|ui|fonts?|layout)\b",
    "Groups, channels & bots": r"\b(?:groups?|channels?|bots?|admins?|supergroups?)\b",
    "Battery": r"\bbatter(?:y|ies)\b",
}

REQUEST = (r"(?:please add|pls add|plz add|add (?:a |an |the )?(?:option|feature|ability)|need (?:a |an )?(?:option|feature)"
           r"|would be (?:nice|great|better|good)|i wish|wish (?:there|you|it)|feature request|please (?:make|give|bring|allow|enable)"
           r"|should (?:add|have)|hope you (?:add|will)|waiting for|when will)")

AVAILABILITY = r"(?:where|can'?t find|cannot find|not (?:available|showing|show|appear\w*|there|visible)|no (?:call|voice)|when will|my (?:country|region)|region|asia|india|iran)"


def tag_themes(text: pd.Series) -> pd.DataFrame:
    low = text.str.lower().fillna("")
    return pd.DataFrame({name: low.str.contains(pat, regex=True) for name, pat in THEMES.items()}, index=text.index)


def is_request(text: pd.Series) -> pd.Series:
    return text.str.lower().fillna("").str.contains(REQUEST, regex=True)


def is_availability_issue(text: pd.Series) -> pd.Series:
    return text.str.lower().fillna("").str.contains(AVAILABILITY, regex=True)
