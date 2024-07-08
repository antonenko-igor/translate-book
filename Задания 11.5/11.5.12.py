chord_steps = {
    "major": [4, 7],
    "minor": [3, 7],
    "dominant seventh": [4, 7, 10],
    "augmented fifth": [4, 8],
    "minor seventh": [3, 7, 10],
    "minor fifth": [4, 6],
    "major seventh": [4, 7, 11],
    "major sixth": [4, 7, 9],
    "diminished seventh": [3, 6, 10],
    "minor sixth": [3, 7, 9]
}

musical_keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

key = input("Введите музыкальный ключ: ")
chord_type = input("Введите тип аккорда: ")

if key not in musical_keys:
    print("Неверный ключ")
elif chord_type.lower() not in chord_steps:
    print("Неверный тип аккорда")
else:
    root_index = musical_keys.index(key)
    notes = [musical_keys[root_index]]
    steps = chord_steps[chord_type.lower()]
    for step in steps:
        notes.append(musical_keys[(root_index + step) % 12])
    print(f"Ноты для  {key} {chord_type} аккорда следующие {', '.join(notes)}") 