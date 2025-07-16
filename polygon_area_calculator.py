class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        output_str = ""
        for row in range(self.height):
            output_str += "*" * self.width + "\n"
        
        return output_str
    
    def get_amount_inside(self, other):
        if self.width > other.width and self.height > other.height:
            return (self.height // other.height) * (self.width // other.width)
        return 0
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_width(self, side_length):
        self.set_side(side_length)
    
    def set_height(self, side_length):
        self.set_side(side_length)
    
    def set_side(self, side_length):
        super().set_width(side_length)
        super().set_height(side_length)
    
    def __repr__(self):
        return f"Square(side={self.width})"

r = Rectangle(15, 10)
s = Square(5)
print(r.get_amount_inside(s))
