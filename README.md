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


## 1. Capturar una imagen de la webcam por un ROS Node en Python (en Linux), detectar un objeto verde en la imagen, calcular las coordenadas X y Y del objeto (se puede utilizar un Aruco para el mismo fin).

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/2a02603a-9f9b-478b-ba64-9a8510292b52)
![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/97e677d4-56bd-41f9-9191-d57ef78a1c80)

## 2. Crear una librería de C++ (*.so en Linux, *.dll en Windows) que multiplique los valores de las coordenadas por 100.

![image](https://github.com/fercuellar/Interfaces/assets/58601693/6981c666-f6c4-4c48-94ad-86af220e7ed5)

## 3. Cargar la librería de C++ en el ROS Node para hacer la operación de multiplicación.

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/a43e4069-831c-48df-bf08-1036d55418a1)

## 4. Publicar el resultado con su timestamp en un ROS Topic.

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/e379c2fd-edd7-4575-9d0f-fc22e6f8f1cf)

## 5. Crear un Wrapper de gRPC para convertir el ROS Topic de las coordenadas del objeto a un servicio RPC.

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/609c032e-ffe8-42ef-b160-598bb5d5f44b)

## 6. En C# crear un programa que tome las coordenadas del objeto desde el servicio RPC y las despliegue en la terminal. (De preferencia en Windows con Visual Studio, pero se puede utilizar Java o MonoDevelop en Linux).

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/785545a7-a9ff-40ec-8ba3-856b0ed8b02e)
![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/8e8c5a56-1e1e-4462-82c0-b6dd8e0b0297)
![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/d10deb10-31d2-44b4-962c-bcd40db33f30)

## 7. Utilizar grpc-Gateway para que el Wrapper haga disponible el servicio como un REST-API.

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/fbf7df35-6dd1-41bd-b7f3-fa6816607442)

## 8. En Postman (o Flask en Python), adquirir las coordenadas de objeto desde el nuevo REST-API, y guardar el dato en un archivo JSON.

![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/53d59385-d758-4891-a9d6-a9d4a550e579)
![Captura de imagen](https://github.com/fercuellar/Interfaces/assets/58601693/e440fdf6-fe77-4759-a50b-1c55d2672829)


