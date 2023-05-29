# Interfaces
Actividad de MidTerm - Autor: Fernando Cuellar Martinez A00827540\

El siguiente contenido de folders y archivos se encuentran dentro de un paquete llamado midterm, si usted desea copiar este a su entorno, favor de crear un catkinws para dentro de src, crear un paquete y poner todos los archivos dentro de ese paquete (midterm en mi caso para los archivos launch), la carpeta de launch tambien debe ir en nivel jerárquico dentro de src

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
