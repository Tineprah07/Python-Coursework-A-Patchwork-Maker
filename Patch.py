from graphics import *

# Final Digit
def finalDigits(win, point, col1, col2, rad):
    circle = Circle(point, rad)
    circle.setOutline(col1)
    circle.setFill(col2)
    circle.draw(win)
    return circle

def finalMain(win, xMove, yMove, colors):
    x, y = 10, 10
    rad = 10
    patch = []
    col2 = [colors, "white"]
    col1 = [colors]

    for row in range(5):
        for col in range(5):
            circle = finalDigits(win, Point(x, y), col1[0], col2[row % 2], rad)
            patch.append(circle)
            x = x + 20
        x = 10
        y = y + 20
        
    border = Rectangle(Point(0, 0), Point(100, 100))
    border.draw(win)
    patch.append(border)

    for parts in patch:
        parts.move(xMove, yMove)

# Penultimate Digit
def penultimateDigit(win, p1, p2, p3, p4, p5, p6, col1, col2, counter):
    white = [7, 9, 17, 19]
    polygon = Polygon(p1, p2, p3, p4, p5, p6)
    polygon.setOutline(col1)
    if counter not in white:
        polygon.setFill(col2)
    polygon.draw(win)
    return polygon

def penultimateMain(win, xMove, yMove, colors):
    x, y = 0, 0
    patch = []
    col1 = [colors]
    counter = 0

    for row in range(5):
        for column in range(5):
            counter += 1
            
            col2 = colors
            polygon = penultimateDigit(win, Point(x, y), Point(x, y + 10), Point(x + 10, y + 20),
                                       Point(x + 20, y + 10), Point(x + 20, y), Point(x + 10, y + 10), col1[0], col2, counter)
            patch.append(polygon)
            x += 20
        x = 0
        y += 20
    
    border = Rectangle(Point(0, 0), Point(100,100))
    border.draw(win)
    patch.append(border)

    for parts in patch:
        parts.move(xMove, yMove)

# Antepenultimate Digit
def rectangle(win, xMove, yMove, colors):
    rectangle = Rectangle(Point(0, 0), Point(100, 100))
    rectangle.setFill(colors)
    rectangle.draw(win)
    rectangle.move(xMove, yMove)

def getPatchSize():
    while True:
        size = int(input("Enter patch size (5, 7, 9): "))
        if size in [5, 7, 9]:
            return size
        else:
            print("Invalid patch size. Please enter 5, 7, or 9.")

def getDistinctColors():
    colorNames = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    colors = []

    while len(colors) < 3:
        color = input(f"Enter color {len(colors) + 1} ({', '.join(colorNames)}): ").lower()

        if color in colorNames and color not in colors:
            colors.append(color)
        else:
            print("Invalid color. Please enter a distinct and valid color.")

    return colors
            
def colour(row, column, patchSize, colors):
    rowColour = (patchSize - 1) * 100
    colColour = (patchSize // 2) * 100

    if (row == 0 or row == rowColour or column == colColour):
        return colors[0]
    elif (rowColour > row > 0 and column < colColour):
        return colors[1]
    else:
        return colors[2]

def mode(win,width):
    okButton = Rectangle(Point(0, 0), Point(30, 30))
    okButton.setFill("black")
    okText = Text(Point(15, 15), "OK")
    okText.setTextColor("white")
    okText.setSize(8)
    okButton.draw(win)
    okText.draw(win)

    closeButton = Rectangle(Point(width - 30, 0), Point(width, 30))
    closeButton.setFill("black")
    closeText = Text(Point(width - 15, 15), "Close")
    closeText.setTextColor("white")
    closeText.setSize(8)
    closeButton.draw(win)
    closeText.draw(win)

    while True:
        clickPoint = win.getMouse()
        clickX = clickPoint.getX()
        clickY = clickPoint.getY()
        
        if width - 30 <= clickX <= width and 0 <= clickY <= 30:
            win.close()
            break
      
def main():
    patchSize = getPatchSize()
    colors = getDistinctColors()
    
    width = patchSize * 100
    height = patchSize * 100

    win = GraphWin("", width, height)
    win.setBackground("white")
    
    # Draw patch
    for column in range(0, height, 100):
        for row in range(0, width, 100):
            if row / 100 % 2 == 0 and column / 100 % 2 == 0 or row / 100 % 2 == 1 and column / 100 % 2 == 1:
                finalMain(win, row, column, colour(row, column, patchSize, colors))
            elif column != height / 2 - 50 and row != 0 and row != width - 100:
                penultimateMain(win, row, column, colour(row, column, patchSize, colors))
            else:
                rectangle(win, row, column, colour(row, column, patchSize, colors))
                
    mode(win,width)
                
main()
            


