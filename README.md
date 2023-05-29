# Interfaces
Actividad de MidTerm - Autor: Fernando Cuellar Martinez A00827540\

El siguiente contenido de folders y archivos se encuentran dentro de un paquete llamado midterm, si usted desea copiar este a su entorno, favor de crear un catkinws para dentro de src, crear un paquete y poner todos los archivos dentro de ese paquete (midterm en mi caso para los archivos launch) dentro de un folder para tener organizacion, la carpeta de launch tambien debe ir en nivel jerárquico dentro del paquete mismo.
![route](https://github.com/fercuellar/Interfaces/assets/58601693/8dbd2062-30b5-492a-81dd-d5fb499c6a11)


# Links de videos
[Link de video Funcionamiento Paso 1 a 6](https://drive.google.com/file/d/1emYHH88Ft-TMoo0sp1uwgtTFQWfG-5P-/view?usp=share_link)\
[Link de video Funcionamiento Paso 7 a 8](https://drive.google.com/file/d/1lwl2GcAH6AmOw8Fl-fXwjXSztrc1P0Hp/view?usp=sharing)

# Puntos extras
[Link de Funcionamiento para arduino con Protobuf](https://drive.google.com/file/d/1giKIJEYNWWy6wwcf7OErQ0WSMvJpdxPN/view?usp=share_link)\
[Investigacion de CORS](https://github.com/fercuellar/Interfaces/blob/master/CORS/CORS-Extra%20Points.pdf)

# Diagrama DFD
![Interfaces](https://github.com/fercuellar/Interfaces/assets/58601693/359852f7-0fe3-494e-be3d-12df2e0dbe75)

# Que no se puede docuemntar en Doxygen 

Aunque la mayoría de estos se pueden documentar mediante este estándar, hay algunos los cuales no se es recomendable hacer, unos de estos son los archivos de tipo proto, ya que estos están diseñados para ser simples, legibles y descriptivos por estructuras de datos, además de que como estos se utilizan en diferentes entornos de desarrollo los comentarios pueden generar problemas de compatibilidad, otra razon es que la documentación de estos mensajes normalmente va por separado.

Otros archivos que no se deben de documentar o incluso tocar en absoluto son los generados por los mismos protos, sobre los grpc, ya que estos son instructivos para realizar acciones.


#    1. Capturar una imagen de la webcam por un ROS Node en Python (en Linux), detectar un objeto verde en la imagen, calcular las coordenadas X y Y del objeto (se puede utilizar un Aruco para el mismo fin).
#    2. Crear una librería de C++ (*.so en Linux, *.dll en Windows) que multiplique los valores de las coordenadas por 100.
#    3. Cargar la librería de C++ en el ROS Node para hacer la operación de multiplicación.
#    4. Publicar el resultado con su timestamp en un ROS Topic.
#    5. Crear un Wrapper de gRPC para convertir el ROS Topic de las coordenadas del objeto a un servicio RPC.
#    6. En C# crear un programa que tome las coordenadas del objeto desde el servicio RPC y las despliegue en la terminal. (De preferencia en Windows con Visual Studio, pero se puede utilizar Java o MonoDevelop en Linux).
#    7. Utilizar grpc-Gateway para que el Wrapper haga disponible el servicio como un REST-API
#    8. En Postman (o Flask en Python), adquirir las coordenadas de objeto desde el nuevo REST-API, y guardar el dato en un archivo JSON.
