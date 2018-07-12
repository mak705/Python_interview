formatter  = '%r %r %r %r'
print formatter % (1, 2, 3, 4)
print formatter % ("one","two", "three", 4)
print formatter % (formatter,"formatter", formatter, "formatter")
fr = 'hi'
print formatter % (fr,"fr","fr",fr)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "Helllo\'s",
    "whatzup" 
)

