import random

# Danh sách các bình luận mở rộng
comments_list = [
    "Great book!", "Not my type.", "Loved it!", "Could be better.", "Amazing read!",
    "Boring at times.", "Highly recommend!", "Didn't enjoy it.", "A masterpiece!", "Very informative.",
    "Too long...", "A page-turner!", "Well written.", "Disappointing.", "Learned a lot.",
    "Too complex.", "Engaging story!", "Fantastic!", "Worth reading.", "Not for me.",
    "An absolute gem!", "Would read again!", "Confusing at times.", "A thrilling adventure!",
    "Best book I've read this year!", "Not what I expected.", "Overrated.", "Kept me hooked!",
    "Brilliant writing!", "Felt rushed.", "Slow start but great ending!", "Heartwarming story!",
    "Superb storytelling!", "Couldn't put it down!", "Not as good as I hoped.", "Very inspiring!",
    "A thought-provoking read.", "Waste of time.", "Highly enjoyable!", "So much depth!",
    "Wouldn't recommend.", "One of my favorites!", "Perfect for a rainy day.", "Simply magical!"
]

# Danh sách emoji ngẫu nhiên
emojis = ["😊", "😍", "😢", "😡", "😴", "👍", "👎", "🔥", "💖", "📖", "🤔", "😆", "😞", "✨"]

num_users = 100
num_books = 50
comments_per_user_range = (5, 15)  # Số lượng bình luận ngẫu nhiên mỗi người dùng

with open("comments.txt", "w", encoding="utf-8") as f:
    for user_id in range(1, num_users + 1):
        num_comments = random.randint(*comments_per_user_range)
        for _ in range(num_comments):
            book_id = random.randint(1, num_books)
            rating = random.randint(1, 5)  # Thêm đánh giá từ 1-5 sao
            comment = random.choice(comments_list)

            # 20% cơ hội thêm câu bổ sung
            if random.random() < 0.2:
                comment += " " + random.choice(comments_list).lower()

            # 30% cơ hội thêm emoji
            if random.random() < 0.3:
                comment += " " + random.choice(emojis)

            f.write(f"{user_id},{book_id},{rating},{comment}\n")

print("Generated comments.txt successfully!")
