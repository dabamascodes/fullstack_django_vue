from rest_framework import serializers
from .models import *

'''
Este código crea un **serializer** para el modelo `Categoria` usando **Django REST Framework**. Vamos a desglosarlo:

1. **`serializers.ModelSerializer`**:
   - Es una clase base que facilita la serialización y deserialización de modelos Django automáticamente.
   - En este caso, se usa para convertir instancias del modelo `Categoria` en datos JSON (y viceversa).

2. **Clase `Meta`**:
   - Especifica detalles sobre cómo el serializer debe comportarse.
   - Aquí se definen:
     - **`model = Categoria`**: El modelo que el serializer usa.
     - **`fields = ("id", "nombre", "slug")`**: Los campos específicos del modelo `Categoria` que se incluirán en la serialización.

3. **`fields`**:
   - Incluye una lista de los campos que quieres exponer en la API. En este caso:
     - `id`: Probablemente un identificador único (como un campo `AutoField`).
     - `nombre`: Podría ser un campo `CharField` que almacena el nombre de la categoría.
     - `slug`: Usado comúnmente para URLs amigables, como un identificador basado en texto.

### Resultado
Con este serializer, puedes usarlo en tus vistas para manejar datos de `Categoria` fácilmente. Por ejemplo:

- **Convertir un objeto `Categoria` en JSON**:
  ```python
  categoria = Categoria.objects.first()
  serializer = CategoriaSerializer(categoria)
  print(serializer.data)  # {'id': 1, 'nombre': 'Ejemplo', 'slug': 'ejemplo'}
  ```

- **Validar y guardar datos desde JSON**:
  ```python
  data = {'nombre': 'Nueva Categoria', 'slug': 'nueva-categoria'}
  serializer = CategoriaSerializer(data=data)
  if serializer.is_valid():
      serializer.save()
  ```


'''




class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ("id", "nombre", "slug")
        # fields = '__all__'
        # fields = ('__all__')