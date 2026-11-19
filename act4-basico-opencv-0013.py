# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
nombre_ventana = 'Michael_Jackson.jpg'
print("-+-+-+- Meredith Aguirre NC = 0013 -+-+-+-")

# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================

print("\n1. LECTURA DE IMÁGENES 0013")  # Imprime el título de la sección en la consola.
nombre_ventana = 'Gpo 3H Michael Jackson Meredith Aguirre 0013' # Linea nueva
imgMichael_Jackson = cv2.imread('Michael_Jackson.jpg')
cv2.namedWindow(nombre_ventana) #Linea nueva
if imgMichael_Jackson is None:  # Verifica si la variable 'img' está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'Michael_Jackson.jpg'.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

    # ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN 0013")  # Imprime el título de la segunda sección.
height, width, channels = imgMichael_Jackson.shape  # Extrae el alto (filas), ancho (columnas) y canales de color de la matriz.
print(f"Dimensiones de la imagen: {width}x{height} píxeles")  # Muestra el ancho por el alto en consola.
print(f"Número de canales de color: {channels}")  # Muestra cuántos canales tiene (3 para BGR: Azul, Verde, Rojo).
print(f"Tipo de dato de la imagen: {imgMichael_Jackson.dtype}")  # Muestra el tipo de dato (uint8 = enteros de 0 a 255).
print(f"Total de datos/píxeles: {imgMichael_Jackson.size}")  # Muestra la cantidad total de valores numéricos en la matriz.

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL 0013")  # Imprime el título de la tercera sección.
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")  # Instrucción para el usuario.
# Mostrar imagen
cv2.imshow(nombre_ventana, imgMichael_Jackson)  # Linea nueva
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.
cv2.destroyAllWindows()
print("-+-+-+- Modificando los pixeles.. -+-+-+-")

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")  # Imprime el título de la cuarta sección.
pixel_img = imgMichael_Jackson.copy()  # Crea una copia exacta de la imagen original para no dañar la original.
y, x = 100, 150  # Define las coordenadas a analizar: fila (Y) = 100, columna (X) = 150.
pixel = pixel_img[y, x]  # Obtiene los 3 valores de color [Azul, Verde, Rojo] del píxel en esa posición.
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")  # Imprime los valores BGR del píxel en consola.
pixel_img[y, x] = [0, 0, 255]  # Cambia el color de ese único píxel a Rojo puro (0 Azul, 0 Verde, 255 Rojo).
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)  # Dibuja un círculo amarillo alrededor para poder verlo a simple vista.
cv2.imshow('Meredith Aguirre 0013', pixel_img)  # Muestra la imagen con el píxel alterado y señalado.
cv2.waitKey(0)  # Espera a que se presione una tecla para continuar.

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")  # Imprime el título de la quinta sección.
roi_img = imgMichael_Jackson.copy()  # Crea una nueva copia limpia de la imagen original.
roi = roi_img[50:200, 100:300]  # Recorta una sub-matriz desde la fila 50 a 200 y columna 100 a 300.
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)  # Dibuja un rectángulo verde marcando la zona recortada.
cv2.imshow('Imagen con ROI Meredith Aguirre 0013', roi_img)  # Muestra la imagen completa con el recuadro verde.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.imshow('ROI Extraida Meredith Aguirre 0013', roi)  # Muestra únicamente el pedazo recortado en una ventana aparte.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")  # Imprime el título de la sexta sección.
b, g, r = cv2.split(imgMichael_Jackson)  # Divide la imagen a color en 3 matrices independientes: Azul (b), Verde (g) y Rojo (r).
cv2.imshow('Canal Azul Meredith Aguirre 0013', b)  # Muestra la intensidad del canal azul en tonos de gris.
cv2.imshow('Canal Verde Meredith Aguirre 0013', g)  # Muestra la intensidad del canal verde en tonos de gris.
cv2.imshow('Canal Rojo Meredith Aguirre 0013', r)  # Muestra la intensidad del canal rojo en tonos de gris.
cv2.waitKey(0)  # Pausa el programa mientras observas las 3 ventanas en blanco y negro.
zeros = np.zeros_like(b)  # Crea una matriz llena de ceros (negro) del mismo tamaño que un canal.
blue_img = cv2.merge([b, zeros, zeros])  # Une el canal azul real con verde y rojo en cero (solo se ve azul).
green_img = cv2.merge([zeros, g, zeros])  # Une el canal verde real con azul y rojo en cero (solo se ve verde).
red_img = cv2.merge([zeros, zeros, r])  # Une el canal rojo real con azul y verde en cero (solo se ve rojo).
cv2.imshow('Canal Azul Meredith Aguirre 0013', blue_img)  # Muestra la imagen filtrada únicamente en color azul.
cv2.imshow('Canal Verde Meredith Aguirre 0013', green_img)  # Muestra la imagen filtrada únicamente en color verde.
cv2.imshow('Canal Rojo Meredith Aguirre 0013', red_img)  # Muestra la imagen filtrada únicamente en color rojo.
cv2.waitKey(0)  # Espera a que se presione una tecla para avanzar.

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")  # Imprime el título de la séptima sección.
resized_img = cv2.resize(imgMichael_Jackson, (400, 300))  # Cambia el tamaño exacto de la imagen a 400px de ancho por 300px de alto.
cv2.imshow('Meredith Aguirre 0013', resized_img)  # Muestra la imagen con sus nuevas dimensiones fijas.
cv2.waitKey(0)  # Espera a que se presione una tecla.
half_size = cv2.resize(imgMichael_Jackson, None, fx=0.5, fy=0.5)  # Reduce la imagen a la mitad (50% en ancho y 50% en alto).
double_size = cv2.resize(imgMichael_Jackson, None, fx=1.5, fy=1.5)  # Amplía la imagen un 50% extra (escala 1.5x).
cv2.imshow('Meredith Aguirre 0013', half_size)  # Muestra la versión reducida.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.imshow('Meredith Aguirre 0013', double_size)  # Muestra la versión ampliada.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")  # Imprime el título de la octava sección.
height, width = imgMichael_Jackson.shape[:2]  # Obtiene nuevamente el alto y ancho actual de la imagen original.
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)  # Calcula la matriz para girar 45° desde el centro.
rotated_img = cv2.warpAffine(imgMichael_Jackson, rotation_matrix, (width, height))  # Aplica la rotación matemática sobre la imagen.
cv2.imshow('Meredith Aguirre 0013', rotated_img)  # Muestra la imagen inclinada 45 grados.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")  # Imprime el título de la novena sección.
horizontal_flip = cv2.flip(imgMichael_Jackson, 1)  # Voltea la imagen horizontalmente (código 1 = efecto espejo).
cv2.imshow('Meredith Aguirre 0013', horizontal_flip)  # Muestra el volteo horizontal.
cv2.waitKey(0)  # Espera a que se presione una tecla.
vertical_flip = cv2.flip(imgMichael_Jackson, 0)  # Voltea la imagen verticalmente (código 0 = de cabeza).
cv2.imshow('Meredith Aguirre 0013', vertical_flip)  # Muestra el volteo vertical.
cv2.waitKey(0)  # Espera a que se presione una tecla
both_flip = cv2.flip(imgMichael_Jackson, -1)  # Voltea en ambos ejes al mismo tiempo (código -1 = horizontal + vertical).
cv2.imshow('Meredith Aguirre 0013', both_flip)  # Muestra el volteo combinado.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")  # Imprime el título de la décima sección.
result = cv2.imwrite('rotated_image.jpg', rotated_img)  # Guarda la imagen rotada en el disco duro como 'rotated_image.jpg'.
if result:  # Comprueba si el guardado devolvió True (verdadero).
    print("Imagen rotada guardada exitosamente como 'rotated_image.jpg'")  # Confirma que el archivo se creó.
else:  # Si ocurrió algún problema de permisos o ruta...
    print("Error: No se pudo guardar la imagen rotada.")  # Notifica el fallo en consola.
cv2.destroyAllWindows()  # Cierra todas las ventanas gráficas abiertas por OpenCV para liberar memoria RAM.
print("\n¡Todas las operaciones se completaron con éxito!")  # Mensaje final de cierre en la terminal.