from summarizer import summarize


text = "The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet. Sometimes an article modifies a noun that is also modified by an adjective. The usual word order is article + adjective + noun. If the article is indefinite, choose a or an based on the word that immediately follows it. Uncountable nouns include intangible things (e.g., information, air), liquids (e.g., milk, wine), and things that are too large or numerous to count (e.g., equipment, sand, wood). Because these things can’t be counted, you should never use a or an with them—remember, the indefinite article is only for singular nouns. Possessive pronouns can help identify whether you’re talking about specific or nonspecific items. As we’ve seen, articles also indicate specificity. But if you use both a possessive pronoun and an article at the same time, readers will become confused. Possessive pronouns are words like his, my, our, its, her, and their. "

no_of_sentence = 10

summary_text = summarize(text , no_of_sentence)

print(summary_text)