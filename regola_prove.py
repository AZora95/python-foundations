casi = [
    (None, 2, "da_completare"),
    (0, 2, "ordinaria"),
    (99999, 2, "ordinaria"),
    (100000, 2, "da_rivedere"),
    (4500, 1, "da_rivedere"),
]

for importo_centesimi, documenti, attesa in casi:
    if importo_centesimi is None:
        categoria = "da_completare"
    elif importo_centesimi >= 100000 or documenti < 2:
        categoria = "da_rivedere"
    else:
        categoria = "ordinaria"
    assert categoria == attesa, f"{importo_centesimi}, {documenti}: attesa {attesa}, ottenuta {categoria}"

print("Tutte le prove passano.")
