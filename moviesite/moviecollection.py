import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=AjYOMk-4NIU")

avatar = media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")

school_of_rock = media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")

ratatouille = media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")

midnight_in_paris= media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")

hunger_games = media.Movie("Toy Story", "A story about toys", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "http://www.youtube.com/watch?v=vwyZH85NQC4")


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)