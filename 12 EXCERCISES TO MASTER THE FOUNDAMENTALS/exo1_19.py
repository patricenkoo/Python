class Movie:
    def __init__(self, new_title, new_year, new_budget, initial_gross):
         self.title = new_title
         self.year = new_year
         self.budget = new_budget
         self.gross = initial_gross
     
    def get_gross(self):
                return self.gross
    def set_gross(self, new_value):
        self.gross = new_value

    def get_net(self):
        the_net = self.gross - self.budget
        return the_net

new_movie = Movie("Titanic", 1997, 200000000, 659363944)
print(new_movie.title,new_movie.year, new_movie.budget, new_movie.gross)
