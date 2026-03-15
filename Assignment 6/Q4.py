def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency, key=lambda word: frequency[word], reverse=True)
    top_5 = sorted_words[:5]

    total_words = len(words)
    top_5_count = 0
    for word in top_5:
        top_5_count += frequency[word]

    proportion = (top_5_count / total_words) * 100

    print("Top 5:")
    for word in top_5:
        print(f"  {word}: {frequency[word]}")
    print("Total words:", total_words)
    print("Proportion:", top_5_count, "/", total_words, "=", proportion)