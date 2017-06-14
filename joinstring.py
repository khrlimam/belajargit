kontens = ["ini", "adalah", "konten", "percobaan"]
join_konten = ""
for konten in kontens:
    join_konten = "{} {}".format(join_konten, konten)
join_konten = join_konten[1:]
print join_konten
