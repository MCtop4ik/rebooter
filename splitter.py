def wrap_paragraphs(text):
    paragraphs = text.split('\n')
    wrapped_paragraphs = ['<p>{}</p>'.format(p) for p in paragraphs]
    wrapped_text = '\n'.join(wrapped_paragraphs)
    return wrapped_text


text = """
Once upon a time, in a charming garden, there was a little butterfly named Bella. Bella lived among colorful flowers and friendly insects. She fluttered from one blossom to another, enjoying the sweet nectar and warm sunshine.
Bella loves to explore her garden. She often visits her friends, the ladybugs and bees, who work busily among the flowers.
One day, while Bella was sipping nectar from a beautiful rose, she overheard a conversation among the garden creatures. They spoke of a legendary treasure hidden deep in the Enchanted Forest, guarded by mythical creatures.
Bella was listening intently to the tales, her eyes wide with curiosity. She wonders if she has the courage to embark on such a daring adventure.
Determined to uncover the treasure and filled with excitement, Bella took flight, gracefully soaring over the green canopy and into the Enchanted Forest.
As she ventured deeper into the forest, Bella encountered mischievous fairies, wise old owls, and majestic unicorns. Together, they faced numerous challenges and solved ancient riddles.
Bella will confront the fearsome dragon who guards the hidden treasure. With bravery and the help of her newfound friends, she will outsmart the dragon and unlock the secret to its lair.
Their journey, filled with magic and wonder, leads them to a clearing filled with shimmering light. There, they discover the treasure - a chest containing the power to bring joy and happiness to all who possess it.
Thrilled about their find, Bella and her friends return to the garden, carrying the treasure with them. With every flap of Bella's delicate wings, the garden blossoms radiate vibrant colors, and the air fills with laughter and cheer.
All the creatures in the garden now gather around Bella, grateful for her courage and friendship. They live in harmony, enjoying the beauty and happiness that Bella's treasure has brought.
And so, from that day on, the garden and its inhabitants thrive, forever grateful to Bella for her extraordinary adventure and the magical treasure she discovered.
"""
wrapped_text = wrap_paragraphs(text)
print(wrapped_text)
