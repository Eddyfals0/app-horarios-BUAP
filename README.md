# 🎓 Optimizador de Horarios BUAP

Una aplicación web moderna y fácil de usar para optimizar horarios universitarios de la BUAP. Genera automáticamente todas las combinaciones posibles de horarios sin conflictos, permitiendo calificar profesores y encontrar la mejor opción para tu semestre.

## ✨ Características Principales

- **📂 Carga Automática**: Acceso inmediato a un catálogo pre-cargado de carreras y especialidades.
- **⚡ Generación Inteligente**: Encuentra todas las combinaciones de horarios sin conflictos.
- **⭐ Sistema de Calificaciones**: Califica a tus profesores (Excelente, Bueno, Regular, Malo, Nulo).
- **📸 Exportación HD**: Descarga tu horario como una imagen de alta resolución que integra el calendario visual y la tabla de información de profesores.
- **📋 Copiado Rápido**: Exporta los detalles textuales (NRC, Materia, Maestro) directamente al portapapeles para compartir fácil.
- **📐 Tablas Dinámicas**: Las tablas visuales se ajustan inteligentemente al rango de horas real de tus clases (sin espacios vacíos innecesarios).
- **🎨 Interfaz Moderna**: Diseño responsive con modo oscuro incluido.
- **💾 Persistencia**: Tus preferencias y selecciones se recuerdan automáticamente.

## 🚀 Cómo Usar

### 1. Iniciar la Aplicación
1. Abre el archivo `index.html` en cualquier navegador moderno.
2. La aplicación cargará automáticamente el catálogo disponible desde `carreras.js`.

### 2. Seleccionar Materias
1. Selecciona tu **Carrera** de la lista.
2. Elige la **Especialidad o Periodo** correspondiente (archivo CSV).
3. Marca las casillas de las **materias** que deseas cursar este semestre.

### 3. Configurar Preferencias
1. **Califica a los profesores** según tu experiencia o recomendaciones.
2. (Opcional) Usa los filtros rápidos para eliminar clases muy temprano o muy tarde.
3. Haz clic en **"Generar Combinaciones"**.

### 4. Elegir y Exportar
1. Explora las opciones generadas, ordenadas por calificación o compacidad.
2. Haz clic en **"Ver Horario Visual"** para ver el detalle de la semana.
3. Usa las herramientas de exportación:
   - **📥 Descargar HD**: Crea una imagen PNG completa del horario y los profesores.
   - **📋 Copiar Texto**: Copia el resumen del horario al portapapeles.

## 🛠️ Gestión del Catálogo (Para Administradores)

Si necesitas actualizar los horarios disponibles en la aplicación:

### 1. Extracción de Datos
Usa el script `extractor_docx.py` para convertir los documentos de Word oficiales (Horarios) a formato CSV limpio.
*(Requiere configurar la ruta del archivo en el script)*.

### 2. Estructura de Directorios
Organiza los archivos CSV generados en una carpeta llamada `Carreras`, siguiendo esta estructura:
```
/Carreras
  /Ingeniería en Ciencias de la Computación
    primavera_2024.csv
  /Ingeniería Mecatrónica
    otoño_2024.csv
```

### 3. Generar `carreras.js`
Ejecuta el script de Python para consolidar todos los CSV en un único archivo que la web pueda leer:
```bash
python generate_catalog.py
```
Esto generará un nuevo archivo `carreras.js`. Simplemente recarga `index.html` para ver los cambios.

## 📊 Sistema de Calificaciones

| Calificación | Descripción | Color |
|--------------|-------------|-------|
| ⭐⭐⭐⭐⭐ | Excelente | Morado |
| ⭐⭐⭐⭐ | Bueno | Verde |
| ⭐⭐⭐ | Regular | Naranja |
| ⭐⭐ | Malo | Rojo |
| ⭐ | Nulo | Gris |

## 🌐 Compatibilidad

- **Navegadores**: Chrome, Firefox, Safari, Edge (versiones modernas)
- **Dispositivos**: Desktop, tablet, móvil
- **Sistemas**: Windows, macOS, Linux, Android, iOS

## 🤝 Contribuciones

¿Tienes ideas para mejorar la aplicación? ¡Las contribuciones son bienvenidas!

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**¡Optimiza tu horario universitario de manera inteligente y encuentra la mejor combinación de materias y profesores!** 🎓✨
