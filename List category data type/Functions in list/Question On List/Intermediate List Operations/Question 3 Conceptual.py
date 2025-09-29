from jsonschema.benchmarks.const_vs_enum import value

words_list = [
    ["Python", "is", "a", "popular", "programming", "language", "known", "for", "its", "simplicity"],
    ["and", "versatility.", "It", "is", "widely", "used", "in", "web", "development,", "data"],
    ["science,", "artificial", "intelligence,", "machine", "learning,", "automation,", "and", "software", "development."],
    ["Its", "clean", "syntax", "makes", "it", "easy", "for", "beginners", "to", "learn"],
    ["and", "attractive", "for", "experienced", "developers", "as", "well.", "Python", "has", "a"],
    ["huge", "ecosystem", "of", "libraries", "and", "frameworks", "that", "help", "solve", "complex"],
    ["problems", "efficiently.", "For", "example,", "NumPy", "and", "Pandas", "are", "used", "for"],
    ["data", "analysis,", "while", "TensorFlow", "and", "PyTorch", "are", "popular", "for", "AI"],
    ["and", "deep", "learning.", "Frameworks", "like", "Django", "and", "Flask", "make", "web"],
    ["application", "development", "faster", "and", "more", "secure.", "This", "is", "why", "Python"]
]

for i , innerlist in enumerate(words_list):
    if 'For'  in innerlist :
        print(words_list[i].index('For'))
        break
