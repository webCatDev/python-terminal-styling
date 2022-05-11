import random

class Colors:
    def __init__(self):
        self.end = "\u001b[0m"
      
        self.color_map = {
            "red": self.create_code_list(196),
            "light-red": self.create_code_list(1),
            "dark-red": self.create_code_list(124),
            "purple": self.create_code_list(5),
            "light-purple": self.create_code_list(201),
            "dark-purple": self.create_code_list(53),
            "blue": self.create_code_list(75),
            "light-blue": self.create_code_list(4),
            "dark-blue": self.create_code_list(20),
            "green": self.create_code_list(46),
            "light-green": self.create_code_list(10),
            "dark-green": self.create_code_list(2),
            "orange": self.create_code_list(130),
            "light-orange": self.create_code_list(208),
            "dark-orange": self.create_code_list(202),
            "yellow": self.create_code_list(228),
            "light-yellow": self.create_code_list(227),
            "dark-yellow": self.create_code_list(220),
            "grey": self.create_code_list(243),
            "light-grey": self.create_code_list(246),
            "dark-grey": self.create_code_list(236),
            "black": self.create_code_list(0),
            "white": self.create_code_list(231)
        }

        self.all_color_combinations = []

       
        for i in range(0,256):
          for j in range(0,256):
            self.all_color_combinations.append(f"{self.get_background_code(i)}{self.get_foreground_code(j)}")
  

    def get_random_style(self):   
      random_color_index = random.randrange(0, len(self.all_color_combinations))
      print(self.all_color_combinations[random_color_index] + f"id:  {random_color_index} " + self.end)
      return random_color_index

    def print_random_styles(self,count = 10):
        for i in range(count):
          self.get_random_style()

       
        
        
    def get_background_code(self,color_code):
        return f"\u001b[48;5;{color_code}m"

    def get_foreground_code(self,color_code):
        return f"\u001b[38;5;{color_code}m"

    def create_code_list(self, color_code):
        return [
            self.get_foreground_code(color_code),
            self.get_background_code(color_code)
        ]

    def see_all_colors(self):
        for i in range(0, 256):
            print(self.get_foreground_code(i), i) 
  
    def see_all_combinations(self):
      for i in range(len(self.all_color_combinations)):
        print(f"{self.all_color_combinations[i]}id: {i}")

    def printf(self,
               string,
               bg_index=None,
               c_index=None,
               bold=False,
               underline=False):
        bold = "\u001b[1m" if bold is True else ""
        underline = "\u001b[4m" if underline is True else ""

        if c_index is None:
            c_code = ""

        if type(c_index) is int:
            c_code = self.get_foreground_code(c_index)

        if type(c_index) is str:
            c_code = self.color_map[c_index][0]

        if bg_index is None:
            bg_code = ""

        if type(bg_index) is int:
            bg_code = self.get_background_code(bg_index)

        if type(bg_index) is str:
            bg_code = self.color_map[bg_index][1]

        print(bg_code + bold + underline + c_code + " " + string + " " + self.end)

    def print_by_id(self,
               string,
               id,
               bold=False,
               underline=False):
        bold = "\u001b[1m" if bold is True else ""
        underline = "\u001b[4m" if underline is True else ""                 
        
        print(self.all_color_combinations[id] + bold + underline +  " " + string + " " + self.end)


colors = Colors()

printf = colors.printf
print_by_id = colors.print_by_id
get_random_style = colors.get_random_style
print_random_styles = colors.print_random_styles
see_all_colors = colors.see_all_colors
see_all_combinations = colors.see_all_combinations

def printLineBreaks(count=0):
    print("\n" * count)
