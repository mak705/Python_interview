import re
class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w)(\1{2,})')
        self.repl = r'\1'
    def replace(self, word):
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replace(repl_word)
        else:
            return repl_word
replacer = RepeatReplacer()
replacer.replace('llddddoop')
