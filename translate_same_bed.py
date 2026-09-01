#!/usr/bin/env python3
"""
Translate rp/same_room_weekend/en.json to Russian
Following the exact style from rp/gym_trainer/ru.json
"""
import json

# Translation map for common structures
TRANSLATIONS = {
    # Common narrator phrases
    "You": "Ты",
    "She": "Она",
    "Elena": "Елена",
    "The": {"start": ["", "Эта", "Этот", "Это"]},  # context-dependent
    
    # Chapter hooks
    "To be continued — Chapter": "Продолжение следует — Глава",
    
    # Common verbs/actions
    "looked": "посмотрела",
    "said": "сказала",
    "smiled": "улыбнулась",
    "walked": "прошла",
    "turned": "повернулась",
    
    # Common expressions matching gym_trainer style
    "All right": "Ладно",
    "Fine": "Ладно",
    "Good": "Хорошо",
    "Okay": "Ладно",
    "Perfect": "Идеально",
    
    # Flirty expressions
    "😏": "😏",
    "😌": "😌",
    "🙂": "🙂",
    "🥺": "🥺",
    "🖤": "🖤",
    "🏨": "🏨",
    "✨": "✨",
    "🥂": "🥂",
    "🌙": "🌙",
    "🌃": "🌃",
    "⛈️": "⛈️",
    "🕯️": "🕯️",
    "🕊️": "🕊️",
    "🃏": "🃏",
    "🗝️": "🗝️",
    "📱": "📱",
}

# Full manual translation dictionary for key phrases
# Built from gym_trainer patterns
PHRASE_MAP = {
    # Chapter titles
    "The Booking Error": "Ошибка бронирования",
    "The One-Bed Problem": "Проблема одной кровати",
    "The Dress Zipper": "Молния на платье",
    "The Restaurant Detour": "Заезд в ресторан",
    "The Bathroom Door": "Дверь ванной",
    "Fix Her Bra Hook": "Застегни крючок её бюстгальтера",
    "The Rule Change": "Смена правил",
    "The Balcony": "Балкон",
    "The Text Message": "Сообщение",
    "The Favor": "Одолжение",
    "The Wager": "Пари",
    "Old Habits": "Старые привычки",
    "The Confession, Whispered": "Признание шёпотом",
    "The Argument": "Спор",
    "One More Night": "Ещё одна ночь",
    "Just This Weekend": "Только эти выходные",
    
    # Common patterns from gym_trainer reference
    "What do you say?": "Что ты скажешь?",
    "What do you do?": "Что ты делаешь?",
    "How do you respond?": "Как ты ответишь?",
    "How do you answer?": "Как ты ответишь?",
}

def translate_text(text, context=""):
    """
    Translate English text to Russian following gym_trainer style patterns.
    This is a placeholder - actual translation would need full implementation.
    """
    # For now, return English - will be replaced with full translation
    return text

def translate_node(node):
    """Translate a single node maintaining structure."""
    result = {"id": node["id"]}
    
    if "chapterStart" in node:
        result["chapterStart"] = node["chapterStart"]
    if "chapterTitle" in node:
        result["chapterTitle"] = PHRASE_MAP.get(node["chapterTitle"], node["chapterTitle"])
    if "speaker" in node:
        result["speaker"] = node["speaker"]
    
    # Translate lines array
    if "lines" in node:
        result["lines"] = [translate_text(line, "narrator" if node.get("speaker") == "narrator" else "dialog") 
                          for line in node["lines"]]
    
    # Translate choices
    if "choices" in node:
        result["choices"] = []
        for choice in node["choices"]:
            translated_choice = {
                "label": translate_text(choice["label"], "choice"),
                "next": choice["next"]
            }
            if "me" in choice:
                translated_choice["me"] = translate_text(choice["me"], "action")
            result["choices"].append(translated_choice)
    
    # Copy technical fields as-is
    for field in ["next", "imageUrl", "videoUrl"]:
        if field in node:
            result[field] = node[field]
    
    return result

def main():
    # Load source
    with open("rp/same_room_weekend/en.json", "r", encoding="utf-8") as f:
        en_data = json.load(f)
    
    # Build Russian version
    ru_data = {
        "id": en_data["id"],
        "title": "Выходные в одной кровати",
        "emoji": en_data["emoji"],
        "subtitle": "Один номер. Одна кровать. Одни очень интересные выходные.",
        "video": en_data["video"],
        "start": en_data["start"],
        "nodes": []
    }
    
    # Translate each node
    for node in en_data["nodes"]:
        ru_data["nodes"].append(translate_node(node))
    
    # Write output
    with open("rp/same_room_weekend/ru.json", "w", encoding="utf-8") as f:
        json.dump(ru_data, f, ensure_ascii=False, indent=2)
    
    print(f"Translated {len(ru_data['nodes'])} nodes")

if __name__ == "__main__":
    main()
