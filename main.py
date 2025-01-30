#!/usr/bin/env python3
"""
=========================================================
 MAIN ELIZA CHATBOT (PhD Trauma / Vienna Edition)
=========================================================

Usage:
------
python phd_vienna_eliza.py

Description:
------------
A specialized ELIZA chatbot focusing on:
 - PhD-related stress or trauma
 - Living in Vienna
 - Political climate (far-right elections)
 
It imports REFLECTIONS and RULES from eliza_knowledge.py,
keeping the knowledge base separate.

Features:
---------
 - Short greeting message emphasizing PhD trauma & Vienna context
 - Detect repeated user messages (same input) and respond differently
 - Classic ELIZA pattern matching & reflection

Type 'quit', 'exit', or 'bye' to end the chat.
"""

import re
import random
from eliza_knowledge import REFLECTIONS, RULES


def reflect(fragment: str) -> str:
    """
    Applies reflection mappings to transform user statements.
    """
    if fragment is None:
        return ""
    for pattern, replacement in REFLECTIONS.items():
        fragment = re.sub(pattern, replacement, fragment, flags=re.IGNORECASE)
    return fragment


def generate_response(user_input: str) -> str:
    """
    Searches RULES in order. If a pattern matches, picks a random
    response and substitutes capturing groups after reflection.
    """
    for (pattern, responses) in RULES:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response_template = random.choice(responses)
            result = response_template
            for i in range(1, len(match.groups()) + 1):
                group_text = match.group(i)
                if group_text is None:
                    group_text = ""
                group_text = reflect(group_text)
                placeholder = f"{{{i}}}"
                result = result.replace(placeholder, group_text)
            return result

    # Shouldn't reach here due to the catch-all rule
    return "I'm not sure I understand. Could you elaborate?"


def trauma_vienna_eliza_chat():
    """
    Main conversation loop, with repeated input detection.
    """
    print("ELIZA (PhD / Vienna Edition):")
    print("Hello! Let's talk about your PhD, life in Vienna, or anything on your mind.\n")

    last_input = None
    repeat_count = 0

    while True:
        user_input = input("YOU: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nELIZA: Thank you for sharing. All the best for your PhD and life in Vienna. Take care!")
            break

        # Check if user repeats the same message
        if user_input == last_input and user_input != "":
            repeat_count += 1
        else:
            repeat_count = 0

        last_input = user_input

        # If repeated multiple times, respond differently
        if repeat_count >= 1:  # repeating the same exact input consecutively
            # Choose some special response or vary them
            special_responses = [
                "You've said that already. Is there a reason you're repeating yourself?",
                "We seem to be going in circles. Is something bothering you?",
                "You're repeating the same phrase. Could we explore why you feel the need to repeat this?"
            ]
            response = random.choice(special_responses)
        else:
            response = generate_response(user_input)

        print(f"ELIZA: {response}")


if __name__ == "__main__":
    trauma_vienna_eliza_chat()

