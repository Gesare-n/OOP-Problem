def calculate_score(participants):
    scoreboard = []
    for participant in participants:
        score = sum(food_count * points for food_count, points in zip(participant.values(), [5, 3, 2]))
        scoreboard.append({"name": participant["name"], "score": score})

    scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
    return scoreboard
