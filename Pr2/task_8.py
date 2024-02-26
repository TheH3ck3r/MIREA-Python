def task_8(words: list):
  s = ""
  for word in words:
    s = f"{word} {s}"
  return s.strip()

print(task_8(words=["language!", "programming", "Python", "the", "love", "I"]))