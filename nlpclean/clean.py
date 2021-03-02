

def remove_html_tags(text):
    pass

def remove_trash_words(text):
    pass

# https://github.com/google-research/electra/blob/master/model/tokenization.py
# def _run_strip_accents(self, text):
#     """Strips accents from a piece of text."""
#     text = unicodedata.normalize("NFD", text)
#     output = []
#     for char in text:
#       cat = unicodedata.category(char)
#       if cat == "Mn":
#         continue
#       output.append(char)
#     return "".join(output)
# def _clean_text(self, text):
#     """Performs invalid character removal and whitespace cleanup on text."""
#     output = []
#     for char in text:
#       cp = ord(char)
#       if cp == 0 or cp == 0xfffd or _is_control(char):
#         continue
#       if _is_whitespace(char):
#         output.append(" ")
#       else:
#         output.append(char)
#     return "".join(output)


# def _is_control(char):
#   """Checks whether `chars` is a control character."""
#   # These are technically control characters but we count them as whitespace
#   # characters.
#   if char == "\t" or char == "\n" or char == "\r":
#     return False
#   cat = unicodedata.category(char)
#   if cat.startswith("C"):
#     return True
#   return False

# TODO https://github.com/NeelShah18/emot/blob/master/emot/emo_unicode.py