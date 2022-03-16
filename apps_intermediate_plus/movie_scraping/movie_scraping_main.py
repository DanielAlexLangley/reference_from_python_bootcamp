
# 100 Movies that You Must Watch
# # Objective:

# Scrape the top 100 movies of all time from a website.
# Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1).
# The result should look something like this:

# 1) The Godfather
# 2) The Empire Strikes Back
# 3) The Dark Knight
# 4) The Shawshank Redemption

# The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles -
# from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists).

from bs4 import BeautifulSoup

# Make soup:
with open("100_best_movies.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

# Make list from 1 to 100:
list_movies = [_.getText() for _ in soup.find_all(name="h3")]
list_movies.reverse()

# Make movies.txt and add each item in the list to the file:
with open("movies.txt", mode="w") as file:
    for _ in list_movies:
        file.write(f"{_}\n")
