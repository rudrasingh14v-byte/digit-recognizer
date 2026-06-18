import pygame 
from PIL import Image
from tensorflow import keras
import numpy as np

print("Loading model...")
model = keras.models.load_model("digit_recognizer_model.keras")
print("Model loaded successfully! Draw a digit, press P to predict, press C to clear")

WIDTH,HEIGHT = 280, 280

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draw a digit   |   P = Predict   |   C = Clear")


BLACK = (0,0,0)
WHITE = (255,255,255)

screen.fill(BLACK)

def predict_digit(): 
    raw_pixels = pygame.surfarray.array3d(screen) #stored in shape of the form (width,height,3)- 3 is indicative of the RGB values which pygame uses to store image data i.e pixels 
    raw_pixels = np.transpose(raw_pixels, (1,0,2))#converting it in form (heigt,width,3), which is equivalent to (rows,columns,3)

    img = Image.fromarray(raw_pixels).convert('L') # using pillow, converting raw image from pygame to an Image object using PIL, and converting rgb values into grayscale by using 'L', which sets the luminance as brightness values in terms of black, white and gray, i.e grayscale
    img = img.resize((28,28), Image.LANCZOS)

    img_array = np.array(img)/255.0

    img_array = img_array.reshape(1,28,28)

    predictions = model.predict(img_array, verbose = 0)
    predicted_digit = np.argmax(predictions)
    confidence = np.max(predictions)*100
    print(f"Prediction: {predicted_digit}  (confidence: {confidence:.1f}%)")

is_running = True
is_drawing = False

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_drawing = True
        
        elif event.type == pygame.MOUSEMOTION:
            if is_drawing:
                x_cursor, y_cursor = event.pos
                pygame.draw.circle(screen,WHITE,(x_cursor,y_cursor),8)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                screen.fill(BLACK)
                print("Canvas cleared!")
            elif event.key == pygame.K_p:
                predict_digit()
    pygame.display.flip()
pygame.quit()