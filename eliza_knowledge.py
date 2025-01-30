"""
=========================================================
 ELIZA KNOWLEDGE BASE (Reflections & Rules)
=========================================================
This file stores the knowledge base for a specialized 
ELIZA chatbot focusing on:
 - PhD trauma
 - Living in Vienna
 - Political climate (far-right, elections)
 - Generic emotional states
 - Additional coverage for synonyms / different phrasings

Import this from your main script to keep code organized.
"""

import re

# Reflection dictionary: Map from user pronouns to "reflected" pronouns
REFLECTIONS = {
    r"\bI\b": "you",
    r"\bI'm\b": "you're",
    r"\bme\b": "you",
    r"\bmy\b": "your",
    r"\bmine\b": "yours",
    r"\bam\b": "are",
    r"\byou\b": "I",
    r"\byour\b": "my",
    r"\byours\b": "mine",
    r"\bwas\b": "were",
    r"\bwe\b": "you",
    r"\bWe\b": "you",
    r"\bus\b": "you",
    r"\bour\b": "your",
    r"\bmyself\b": "yourself",
    r"\bYourself\b": "myself"
}


# A large set of regex-based rules for matching user input.
# Many lines now include synonyms or alternative phrasings.
RULES = [

    # ----------------------------------------------------
    # Quick Negative / Short Replies
    # ----------------------------------------------------
    (r"^(no(pe)?|nah|not really)\.?$",
     ["Would you prefer to talk about something else?",
      "That's okay. Is there another topic you'd like to discuss?",
      "Are you feeling hesitant to continue, or do you just want a different subject?"]),

    (r"^(nothing|nothing\.)$",
     ["Sometimes feeling 'nothing' can be a defense. Could you share more about what's behind that?",
      "It sounds like you might be feeling empty or numb. Want to explore this further?",
      "Would it help to talk about why you feel there's nothing to say?"]),

    (r"(.*)\b(I'd rather not|I would rather not|I prefer not)\b(.*)",
     ["It's okay to set boundaries. Would you like to talk about something else?",
      "We can change the topic if you want. What else is on your mind?",
      "I understand your reluctance. Is there a different subject that feels safer to discuss?"]),

    (r"(.*)\bi don't want to talk about it\b(.*)",
     ["I respect that. Is there another issue or topic you're comfortable sharing?",
      "We can shift focus. What else is on your mind?",
      "That's okay. If you change your mind, I'm here to listen. Meanwhile, is there something else you'd like to address?"]),

    # This handles truly minimal or empty user input
    (r"^(\s*)$",
     ["Take your time. I’m here when you’re ready to talk.",
      "I notice you’re silent. Is there anything at all you’d like to share?",
      "It's okay to pause. Let me know when you want to continue."]),

    # ----------------------------------------------------
    # Hopelessness / Wanting to Leave
    # ----------------------------------------------------
    (r"(.*)\bno hope\b(.*)",
     ["It sounds like you're feeling hopeless. Can you tell me more about this feeling?",
      "Hopelessness can be overwhelming. What do you think contributes to it?",
      "Have you considered seeking professional support for these feelings of no hope?"]),

    (r"(.*)\bno future\b(.*)",
     ["When you say you see no future, do you mean in your PhD or in Vienna?",
      "It's hard to feel motivated without a sense of future. Could you elaborate on why you feel this way?",
      "Can you recall a time when you did see a future for yourself? What's changed?"]),

    (r"(.*)\bI want to leave\b(.*)",
     ["What makes you want to leave? Is it related to Vienna, your PhD, or something else?",
      "Leaving can be a big step. Have you thought about the consequences or potential new options?",
      "Is there anything that could make you stay or reconsider?"]),

    (r"(.*)\bcan't handle it anymore\b(.*)",
     ["What feels unmanageable right now?",
      "Sometimes when stress accumulates, it feels like too much. Could you break down what's overwhelming you?",
      "Have you reached out to anyone for help with these feelings?"]),

    # ----------------------------------------------------
    # Greetings / Generic
    # ----------------------------------------------------
    (r"^[Hh]ello|^[Hh]i|^[Hh]ey(.*)",
     ["Hello... Feel free to talk about your PhD struggles, Vienna life, or anything else.",
      "Hi there! How can I help you today regarding your PhD or living in Vienna?",
      "Hey! What's on your mind related to academia, politics, or personal well-being?"]),

    (r"(.*)\bhow are you\b(.*)",
     ["I'm just a program, but let's focus on you. How are you feeling?",
      "I'm doing fine in code form. How about you, especially regarding your PhD or Vienna life?"]),

    (r"(.*)\bwho are you\b(.*)",
     ["I’m a simple rule-based chatbot, here to discuss PhD stress, politics in Vienna, or anything else on your mind.",
      "I'm ELIZA, an old-school AI therapy simulation. Who are you and how can I help?"]),

    # ----------------------------------------------------
    # "I'm worried/concerned/anxious about" + synonyms
    # ----------------------------------------------------
    (
        r"(.*)\bI('?m| am)\s+(worried|concerned|anxious|uneasy)\s+about\b\s+(.*)",
        [
            "What specifically {3} you about {4}?",
            "Why do you think {4} is causing you to feel {3}?",
            "Could you share more details on why you're feeling {3} about {4}?"
        ]
    ),

    # ----------------------------------------------------
    # PhD / Academic Stress
    # ----------------------------------------------------
    (r"(.*)\b(PhD|doctoral|dissertation|thesis)\b(.*)",
     ["Tell me more about your {2} journey, especially if there's any trauma involved.",
      "What aspects of your {2} are causing you the most stress?",
      "How does Vienna or current politics affect your {2} progress?"]),

    (r"(.*)\bmy advisor\b(.*)",
     ["Advisors can be challenging. What are the biggest issues with your advisor?",
      "How does your advisor's feedback (or lack thereof) affect your well-being?",
      "Do you think your advisor is aware of your struggles?"]),

    (r"(.*)\bgraduat(e|ion|ing)\b(.*)",
     ["Are you excited or anxious about graduating?",
      "How do you see your life changing after graduation?",
      "Has the political climate in Austria influenced your post-graduation plans?"]),

    (r"(.*)\bimposter syndrome\b(.*)",
     ["Imposter syndrome is common among PhD students. What makes you feel like an imposter?",
      "Could external factors—like your environment in Vienna or academic pressure—be fueling these doubts?",
      "When do these feelings of imposter syndrome intensify for you?"]),

    (r"(.*)\bburnout\b(.*)",
     ["Burnout can happen when stress becomes overwhelming. What do you think led to your burnout?",
      "Have you considered taking breaks or seeking professional help for burnout?",
      "Does the academic culture or political climate in Vienna contribute to your burnout?"]),

    (r"(.*)\b(funding|scholarship)\b(.*)",
     ["Funding can be a huge source of stress. Are you worried about losing or not getting funding?",
      "Have you looked into grants or scholarships specific to Vienna or the EU?",
      "Does uncertainty about funding affect your motivation or mental health?"]),

    (r"(.*)\bpublication(s)?\b(.*)",
     ["Publishing can be stressful. Are you under pressure to publish soon?",
      "What challenges are you facing with your publication process?",
      "Does your advisor or department support you in publishing?"]),

    # ----------------------------------------------------
    # Vienna / Location
    # ----------------------------------------------------
    (r"(.*)\bliving in (Vienna|Wien)\b(.*)",
     ["Vienna can be beautiful but also isolating. How do you feel about living here?",
      "Do you feel the politics or culture in Vienna adds to your stress?",
      "Have you found a supportive community in Vienna for academic pursuits?"]),

    (r"(.*)\bVienna\b(.*)",
     ["What draws you to Vienna or keeps you here?",
      "Is Vienna inspiring or stressful for your research?",
      "Does the local political climate affect your daily life?"]),

    (r"(.*)\blanguage barrier\b(.*)",
     ["Language barriers can be tough in Vienna if you don't speak German. How does that impact you?",
      "Have you considered taking language courses or seeking bilingual communities?",
      "Has the language barrier affected your PhD progress or social life?"]),

    (r"(.*)\bFreud\b(.*)",
     ["Freud is indeed historically associated with Vienna. Are you interested in psychoanalysis?",
      "Freud’s theories are complex. Do you feel they relate to your current emotional state?",
      "Is your interest in Freud connected to your PhD research or personal curiosity?"]),

    (r"(.*)\bexpat\b(.*)",
     ["Being an expat in Vienna can add cultural stress. How are you adapting?",
      "Have you found a community of fellow expats or international students?",
      "What do you find most challenging about living here as an expat?"]),

    # ----------------------------------------------------
    # Politics / Far-Right / Elections
    # ----------------------------------------------------
    (r"(.*)\b(far[\s-]?right|right[-\s]?wing|election|politics)\b(.*)",
     ["Recent political shifts can be unsettling. How do you feel about it?",
      "Many students worry about far-right policies. Has this impacted you?",
      "Do you think the political environment intersects with your PhD or personal well-being?"]),

    (r"(.*)\b(Austria|Austrian politics)\b(.*)",
     ["Austrian politics can be complex. What concerns you most at the moment?",
      "Have you experienced any direct effects from political changes in Austria?",
      "Does the current political climate influence your research or daily life?"]),

    (r"(.*)\belection results\b(.*)",
     ["Election results can stir strong emotions. How do you feel about the outcome?",
      "Do you worry about policy changes affecting international students or academia?",
      "Are you following the political discussions in Vienna about the election results?"]),

    # ----------------------------------------------------
    # Trauma / Emotional States
    # ----------------------------------------------------
    # Expand trauma to include "traumatic"
    (r"(.*)\b(trauma|traumatic)\b(.*)",
     ["Trauma can be tough. Would you share what's triggering these feelings?",
      "Have you found any coping mechanisms for your traumatic experiences?",
      "Is this trauma tied to academia, politics, or personal issues?"]),

    # Expand stress to include synonyms: stress, stressed, pressure, pressured
    (r"(.*)\b(stress|stressed|pressure|pressured)\b(.*)",
     ["What's the main source of this {2}?",
      "Have you sought professional help for feeling {2}?",
      "Do your surroundings or political climate add to your sense of {2}?"]),

    # Expand fear to synonyms: fear, afraid, scared, terrified
    (r"(.*)\b(fear|afraid|scared|terrified)\b(.*)",
     ["What are you {2} of specifically?",
      "Does uncertainty about your PhD or political upheaval drive this {2}?",
      "How does this {2} affect your daily activities?"]),

    # Expand depressed to synonyms: depression, depressed, downcast
    (r"(.*)\b(depression|depressed|downcast)\b(.*)",
     ["I'm sorry you're feeling {2}. How long has this been going on?",
      "{2} can be worsened by isolation or politics. Can you tell me more?",
      "Have you considered talking to a mental health professional in Vienna about feeling {2}?"]),

    # Combine lonely synonyms if desired, but "lonely" is fairly direct
    (r"(.*)\blonely\b(.*)",
     ["Loneliness is often felt by PhD students. Have you joined any groups or clubs?",
      "What do you think would help reduce your loneliness?",
      "Is the feeling of loneliness tied to living in Vienna or your academic path?"]),

    # Expand hate to synonyms? (angry is separate, so let's keep "hate" direct.)
    (r"(.*)\bhate\b (.*)",
     ["Hate can be intense. Why do you hate {2}?",
      "Does this hate impact your work or well-being?",
      "Tell me more about your feelings toward {2}."]),

    (r"(.*)\bpanic attacks?\b(.*)",
     ["Panic attacks can be scary. Have you explored any grounding or relaxation techniques?",
      "When do these panic attacks usually occur?",
      "Is there something in your environment that triggers these attacks?"]),

    (r"(.*)\binsomnia\b(.*)",
     ["Difficulty sleeping can worsen stress and anxiety. When did your insomnia start?",
      "Have you tried adjusting your schedule or seeking medical advice?",
      "Do you think your PhD workload or the political climate in Vienna contributes to insomnia?"]),

    # Synonyms for sadness: sad, down, blue, despondent
    (r"(.*)\b(sad|down|blue|despondent)\b(.*)",
     ["I'm sorry you're feeling {2}. Can you describe what's making you feel this way?",
      "Did something specific trigger you feeling {2}?",
      "What helps you cope when you feel {2}?"]),

    (r"(.*)\bhomesick\b(.*)",
     ["Feeling homesick is common for international students. What do you miss the most?",
      "Have you been able to maintain a connection with home while in Vienna?",
      "Does homesickness affect your motivation or studies?"]),

    # "I am feeling" can remain as is
    (r"(.*)\bI am feeling\b (.*)",
     ["Why do you feel {2}?",
      "Has anything triggered you feeling {2} recently?",
      "Do you see a connection to your PhD or events in Vienna?"]),

    (r"(.*)\bI feel\b (.*)",
     ["Why do you feel {2}?",
      "Does the local situation or your PhD progress affect your feeling of {2}?",
      "Have these feelings changed over time?"]),

    # "I am worried about" is partially replaced by the new synonyms rule above
    (r"(.*)\bI am worried about\b (.*)",
     ["What specifically worries you about {2}?",
      "Why do you think {2} is causing anxiety?",
      "Could you share more details on your worries about {2}?"]),

    # "I can't" plus synonyms "cannot"
    (r"(.*)\bI can('?t|not)\b (.*)",
     ["Why do you believe you can't {3}?",
      "What's preventing you from {3}?",
      "Could the political climate or academic pressure be contributing to this inability?"]),

    # Expand angry synonyms: angry, mad, furious, irate
    (r"(.*)\b(angry|mad|furious|irate)\b(.*)",
     ["What makes you {2}?",
      "Do you feel your {2} is tied to your PhD, politics, or personal circumstances?",
      "How do you usually handle being {2}?"]),

    (r"(.*)\bnostalgic\b(.*)",
     ["What are you nostalgic for?",
      "Has living in Vienna triggered memories of your past?",
      "Is there something you're missing from home or another time in your life?"]),

    (r"(.*)\bhelp\b(.*)",
     ["How do you feel you need help?",
      "Have you sought professional, academic, or personal help from friends or counselors?",
      "Sometimes expressing your needs is the first step. Can you elaborate on your needs?"]),

    (r"(.*)\b(relationship|breakup)\b(.*)",
     ["Relationships during a PhD can be stressful. Can you share more about what's going on?",
      "Has living in Vienna affected your relationship?",
      "Do you feel your PhD or political environment complicates your love life or relationships?"]),

    (r"(.*)\bfamily\b(.*)",
     ["Family can be a source of both comfort and pressure. How is your family situation?",
      "Do you get support from your family regarding your PhD or life in Vienna?",
      "Has the political situation impacted your family's view of your stay in Vienna?"]),

    (r"(.*)\bfriends\b(.*)",
     ["Friends can help relieve stress. Do you feel you have enough social support in Vienna?",
      "Have your friendships changed since starting the PhD?",
      "Do you find it challenging to maintain friendships under academic or political stress?"]),

    # ----------------------------------------------------
    # Labs, Conferences, Collaborations
    # ----------------------------------------------------
    (r"(.*)\blab mates?\b(.*)",
     ["How is your relationship with your lab mates?",
      "Do you feel supported by your lab mates, or is there tension?",
      "Sometimes lab dynamics can affect mental health. Want to share more?"]),

    (r"(.*)\bconference(s)?\b(.*)",
     ["Are you preparing for a conference, or did you recently attend one?",
      "Conferences can be stressful. Are you anxious about presenting your research?",
      "How does travel or funding for conferences work in your case?"]),

    (r"(.*)\bcollaboration(s)?\b(.*)",
     ["Collaboration can be rewarding but also stressful. What's your experience?",
      "Do you collaborate across different countries or within Vienna?",
      "Any challenges in forming or maintaining collaborative research projects?"]),

    # ----------------------------------------------------
    # Catch-all fallback
    # ----------------------------------------------------
    (r"(.*)",
     ["I'm here to listen. Could you tell me more?",
      "Could you elaborate on that?",
      "Let's go deeper. How does that affect you?",
      "Please, continue. I'm listening.",
      "I see. Is there more you'd like to share?"])
]

