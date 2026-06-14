class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def set_width(self, width):
        self._width = width
    def set_height(self, height):
        self._height = height
    def get_area(self):
        return self._width * self._height
    def get_perimeter(self):
        return 2 * (self._width + self._height)
    def get_diagonal(self):
        return ((self._width ** 2) + (self._height ** 2)) ** 0.5
    def get_picture(self):
        picture = ''
        if self._height > 50 or self._width > 50:
            return 'Too big for picture.'
        else:
            for l in range(self._height):
                line = self._width * '*'  
                picture += f"{line}\n"
        return picture
    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle) or isinstance(shape, Square):
            w_number = self._width // shape._width 
            h_number = self._height // shape._height
            if w_number < 1 or h_number < 1:
                result = 0
            else:
                result = w_number * h_number
        return result
        
            
    
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

class Square(Rectangle):
    def __init__(self, side):
        self._width = side
        self._height = side
        self._side = side
    def set_width(self, width):
        self._side = width
        self._width = width
        self._height = width
    def set_height(self, height):
        self._side = height
        self._width = height
        self._height = height 
    def set_side(self, side):
        self._side = side
        self._width = side
        self._height = side
    
    def __str__(self):
        return f"Square(side={self._side})"
        
rectangle_1 = Rectangle (10,15)
print(rectangle_1.get_picture())