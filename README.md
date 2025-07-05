# 🎓 Optimizador de Horarios BUAP

Una aplicación web moderna y fácil de usar para optimizar horarios universitarios de la BUAP. Genera automáticamente todas las combinaciones posibles de horarios sin conflictos, permitiendo calificar profesores y encontrar la mejor opción para tu semestre.

## ✨ Características Principales

- **🎯 Análisis Automático**: Pega directamente los datos de los cursos desde Word o PDF
- **⚡ Generación Inteligente**: Encuentra todas las combinaciones de horarios sin conflictos
- **⭐ Sistema de Calificaciones**: Califica a tus profesores (Excelente, Bueno, Regular, Malo, Nulo)
- **🎨 Interfaz Moderna**: Diseño responsive con modo oscuro incluido
- **📊 Visualización Avanzada**: Tablas de horarios con colores por materia
- **🔍 Filtros Inteligentes**: Filtra por horarios específicos
- **📋 Exportación**: Copia horarios completos al portapapeles
- **💾 Persistencia**: Los datos se guardan automáticamente

## 🚀 Cómo Usar

### 1. Preparar los Datos
1. Convierte tu PDF de horarios a un archivo de Word
2. Copia únicamente las líneas de las materias que te interesan
3. Asegúrate de que cada línea tenga el formato correcto

### 2. Formato Requerido
Cada línea debe seguir este formato:
```
NRC CLAVE MATERIA SECCION DIA HORARIO PROFESOR SALON
```

**Ejemplo:**
```
25665 CCOS 250 Circuitos Logicos OO1 L 1000-1059 TRINIDAD - GARCIA GREGORIO 1CCO4/101
98765 FIS 101 Física Cuántica Aplicada OO1 L 0800-0900 EINSTEIN - ALBERT LAB01
20016 FGUS 007 Lengua Extranjera IV 101 M 0900-1059 CHAVEZ - HEREDIA CLAUDIA 1CCO1/002
```

**Donde:**
- `NRC`: Código del curso (5 dígitos)
- `CLAVE`: Clave de la materia (ej: CCOS 250)
- `MATERIA`: Nombre completo de la materia
- `SECCION`: Sección del curso (ej: OO1, 101)
- `DIA`: Día de la semana (L=Lunes, M=Miércoles, A=Martes, J=Jueves, V=Viernes)
- `HORARIO`: Horario en formato 24h (ej: 1000-1059)
- `PROFESOR`: Nombre completo del profesor
- `SALON`: Salón o laboratorio

### 3. Proceso de Optimización

#### Paso 1: Ingresar Datos
- Pega el texto en el área correspondiente
- Haz clic en "Analizar y Configurar Materias"

#### Paso 2: Configurar Materias
- **Califica a los profesores** usando el sistema de estrellas
- **Elimina opciones** que no te interesen
- **Usa filtros rápidos** para descartar horarios específicos
- Haz clic en "Generar Combinaciones"

#### Paso 3: Explorar Resultados
- **Ordena por**: Mejor combinación, calificación de maestros, o horario más compacto
- **Visualiza horarios** en formato de tabla semanal
- **Exporta horarios** completos al portapapeles
- **Descarta combinaciones** que no te gusten

## 🎨 Características de la Interfaz

### Modo Oscuro
La aplicación incluye un modo oscuro automático que se adapta a las preferencias de tu sistema.

### Diseño Responsive
- **Desktop**: Vista completa con tablas detalladas
- **Tablet**: Diseño adaptado para pantallas medianas
- **Móvil**: Interfaz optimizada para dispositivos móviles

### Colores por Materia
Cada materia tiene un color único para facilitar la identificación en las tablas de horarios.

## 📊 Sistema de Calificaciones

| Calificación | Descripción | Color |
|--------------|-------------|-------|
| ⭐⭐⭐⭐⭐ | Excelente | Morado |
| ⭐⭐⭐⭐ | Bueno | Verde |
| ⭐⭐⭐ | Regular | Naranja |
| ⭐⭐ | Malo | Rojo |
| ⭐ | Nulo | Gris |

## 🔧 Filtros Disponibles

### Filtro por Horario
- **Clases que terminen después de las X**: Elimina clases que terminan tarde
- **Clases que empiecen antes de las X**: Elimina clases muy tempranas
- **Clases durante la hora X**: Elimina clases en horarios específicos

### Ordenamiento de Resultados
- **Mejor Combinación**: Balance entre calificación de maestros y compactitud
- **Calificación de Maestros**: Prioriza profesores mejor calificados
- **Horario más Compacto**: Minimiza las horas libres entre clases

## 💾 Almacenamiento

Los datos se guardan automáticamente en el navegador usando localStorage, por lo que:
- No se pierden al cerrar la pestaña
- Se mantienen entre sesiones
- Son privados (solo en tu navegador)

## 🌐 Compatibilidad

- **Navegadores**: Chrome, Firefox, Safari, Edge (versiones modernas)
- **Dispositivos**: Desktop, tablet, móvil
- **Sistemas**: Windows, macOS, Linux, Android, iOS

## 🚀 Instalación

No requiere instalación. Simplemente:

1. Descarga el archivo `index.html`
2. Ábrelo en cualquier navegador web moderno
3. ¡Listo para usar!

## 📝 Ejemplo de Uso Completo

1. **Copia datos** de tu PDF de horarios
2. **Pega en la aplicación** y analiza
3. **Califica profesores** según tu experiencia
4. **Elimina opciones** no deseadas
5. **Genera combinaciones**
6. **Explora resultados** y elige el mejor horario
7. **Exporta** tu horario final

## 🤝 Contribuciones

¿Tienes ideas para mejorar la aplicación? ¡Las contribuciones son bienvenidas!

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:
1. Verifica que el formato del texto sea correcto
2. Asegúrate de usar un navegador moderno
3. Revisa que los datos no tengan caracteres especiales extraños

---

**¡Optimiza tu horario universitario de manera inteligente y encuentra la mejor combinación de materias y profesores!** 🎓✨
