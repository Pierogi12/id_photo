def setup():
    size(400,400)
    global id_photo
    id_photo = loadImage("zdjecie.jpg")
    global img
    img = loadImage("was.png")
    global photo
    photo = loadImage("glasses.png")
def draw():
    global id_photos
    global img
    image(id_photo, 0, 0, 400, 400)
    image(img, 155, 235, 90, 50)
    image(photo, 100, 170, 200, 50)

   
