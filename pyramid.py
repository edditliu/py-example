def pyramid():
    global x
    for x in range(1,40):
        y= 39 - x
        print(2*y * " "+ x * "🐱"+(x - 1) * "🐶")
    for x in range(1,40):
        y= 39 - x
        print(2*x*" "+y * "🐍"+(y-1)*"🐭" )
pyramid()
print(x)

