from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if not self.check_if_user_exists(username):
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for user in self.users_collection:
            if user.username == username:
                self.movies_collection.append(movie)
                user.movies_owned.append(movie)
                return f"{username} successfully added {movie.title} movie."


    def edit_movie(self, username, movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, val in kwargs.items():
            setattr(movie, key, val)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        if not movie in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not movie.owner.username == username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for user in self.users_collection:
            if user.username == username:
                self.movies_collection.remove(movie)
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
                movie.likes += 1
                user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    movie.likes -= 1
                    user.movies_liked.remove(movie)
                    return f"{username} disliked {movie.title} movie."
                raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        if self.movies_collection:
            sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
            result = ''
            for m in sorted_movies:
                result += m.details() + '\n'
            return result.strip()
        return "No movies found."

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join(x.username for x in self.users_collection)}\n"
        if not self.movies_collection:
            result += "All movies: No movies.\n"
        else:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}\n"
        return result.strip()
