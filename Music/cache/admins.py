from typing import Dict, List
from Music.config import admins

admins: Dict[int, List[int]] = {}

def set(chatId: int, admins_: List[int]):
    admins[chatId] = admins_

def get(chat_id: int) -> List[int]:
    if chat_id in admins:
        return admins[chat_id]
    return []