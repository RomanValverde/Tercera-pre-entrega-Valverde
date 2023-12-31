from django.urls import path, include
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('inicio/', inicio, name="Inicio"),
    path('curso/', curso, name="Curso"),
    path('profesor/', profesor, name="Profesores"),
    path('estudiante/', estudiante, name="Estudiantes"),
    path('entregable/', entregable, name='Entregables'),    
    path('setEstudiante/',setEstudiantes, name="setEstudiante"),
    path('getEstudiante/',getEstudiantes, name="getEstudiante"),
    path('buscarEstudiante/',buscarEstudiantes, name="buscarEstudiante"),
    #path('editarEstudiante/',editarEstudiante, name="editarEstudiante"),
    path('getCurso/',getCursos, name="getCurso"),
    path('buscarCurso/',buscarCursos, name="buscarCurso"),
    path('setProfesor/',setProfesor, name="setProfesor"),
    path('setCurso/',setCurso, name="setCurso"),
    path('setEntregable/',setEntregable, name="setEntregable"),
    path('login/', myLogin, name='login'),
]
