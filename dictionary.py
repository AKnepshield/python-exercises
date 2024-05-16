"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""

word_definitions = {
    "Eclipse": "A phenomenon where one celestial body obscures or partially blocks the light from another celestial body. In the context of astronomy, this commonly refers to solar and lunar eclipses, where the Sun, Earth, and Moon align in specific configurations.",
    "Obsidian": "A naturally occurring volcanic glass formed when molten lava rapidly cools. Obsidian typically has a dark color, ranging from black to dark brown, and exhibits conchoidal fracture patterns. It has been used historically for tools, weapons, and decorative objects.",
    "Nocturnal": "Relating to or occurring during the night. Nocturnal animals are active primarily during the night, while nocturnal activities refer to those that take place after dark.",
    "Abyss": "A deep, immeasurable space or void, often associated with the depths of the ocean or the universe. Figuratively, it can represent a profound or overwhelming sense of emptiness, darkness, or mystery.",
}
# print(word_definitions)
for key, value in word_definitions.items():
    print(f"The definition of {key} is {value}\n")

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for idiom, words in idioms.items():
    print(f"{idiom}: {' '.join(words)}")
