from django.shortcuts import render, redirect
from .models import Dueño, Mascota, Veterinario, Consulta, Vacuna
from datetime import datetime

def inicio_Veterinaria(request):
    return render(request, 'inicio.html')

def agregar_dueño(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        email = request.POST['email']
        fecha_registro = request.POST['fecha_registro']
        dueño = Dueño(nombre=nombre, telefono=telefono, direccion=direccion, email=email, fecha_registro=fecha_registro)
        dueño.save()
        return redirect('ver_dueños')
    return render(request, 'dueño/agregar_dueño.html')

def ver_dueños(request):
    dueños = Dueño.objects.all()
    return render(request, 'dueño/ver_dueños.html', {'dueños': dueños})

def actualizar_dueño(request, id_dueño):
    dueño = Dueño.objects.get(id_dueño=id_dueño)
    return render(request, 'dueño/actualizar_dueño.html', {'dueño': dueño})

def realizar_actualizacion_dueño(request, id_dueño):
    dueño = Dueño.objects.get(id_dueño=id_dueño)
    if request.method == 'POST':
        dueño.nombre = request.POST['nombre']
        dueño.telefono = request.POST['telefono']
        dueño.direccion = request.POST['direccion']
        dueño.email = request.POST['email']
        dueño.fecha_registro = request.POST['fecha_registro']
        dueño.save()
        return redirect('ver_dueños')
    return render(request, 'dueño/actualizar_dueño.html', {'dueño': dueño})

def borrar_dueño(request, id_dueño):
    dueño = Dueño.objects.get(id_dueño=id_dueño)
    if request.method == 'POST':
        dueño.delete()
        return redirect('ver_dueños')
    return render(request, 'dueño/borrar_dueño.html', {'dueño': dueño})

def agregar_mascota(request):
    dueños = Dueño.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        especie = request.POST['especie']
        raza = request.POST['raza']
        sexo = request.POST['sexo']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        id_dueño = request.POST['id_dueño']
        dueño = Dueño.objects.get(id_dueño=id_dueño)
        peso = request.POST['peso']
        
        mascota = Mascota(nombre=nombre, especie=especie, raza=raza, sexo=sexo, fecha_nacimiento=fecha_nacimiento, id_dueño=dueño, peso=peso)
        mascota.save()
        return redirect('ver_mascotas')
    return render(request, 'mascota/agregar_mascota.html', {'dueños': dueños})

def ver_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascota/ver_mascotas.html', {'mascotas': mascotas})

def actualizar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id_mascota=id_mascota)
    dueños = Dueño.objects.all()
    return render(request, 'mascota/actualizar_mascota.html', {'mascota': mascota, 'dueños': dueños})

def realizar_actualizacion_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id_mascota=id_mascota)
    if request.method == 'POST':
        mascota.nombre = request.POST['nombre']
        mascota.especie = request.POST['especie']
        mascota.raza = request.POST['raza']
        mascota.sexo = request.POST['sexo']
        mascota.fecha_nacimiento = request.POST['fecha_nacimiento']
        id_dueño = request.POST['id_dueño']
        dueño = Dueño.objects.get(id_dueño=id_dueño)
        mascota.id_dueño = dueño
        mascota.peso = request.POST['peso']
        
        mascota.save()
        return redirect('ver_mascotas')
    dueños = Dueño.objects.all()
    return render(request, 'mascota/actualizar_mascota.html', {'mascota': mascota, 'dueños': dueños})

def borrar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id_mascota=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')
    return render(request, 'mascota/borrar_mascota.html', {'mascota': mascota})

def agregar_veterinario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        email = request.POST['email']
        num_colegiado = request.POST['num_colegiado']
        turno = request.POST['turno']
        veterinario = Veterinario(nombre=nombre, especialidad=especialidad, telefono=telefono, email=email, num_colegiado=num_colegiado, turno=turno)
        veterinario.save()
        return redirect('ver_veterinarios')
    return render(request, 'veterinario/agregar_veterinario.html')

def ver_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'veterinario/ver_veterinarios.html', {'veterinarios': veterinarios})

def actualizar_veterinario(request, id_veterinario):
    veterinario = Veterinario.objects.get(id_veterinario=id_veterinario)
    return render(request, 'veterinario/actualizar_veterinario.html', {'veterinario': veterinario})

def realizar_actualizacion_veterinario(request, id_veterinario):
    veterinario = Veterinario.objects.get(id_veterinario=id_veterinario)
    if request.method == 'POST':
        veterinario.nombre = request.POST['nombre']
        veterinario.especialidad = request.POST['especialidad']
        veterinario.telefono = request.POST['telefono']
        veterinario.email = request.POST['email']
        veterinario.num_colegiado = request.POST['num_colegiado']
        veterinario.turno = request.POST['turno']
        veterinario.save()
        return redirect('ver_veterinarios')
    return render(request, 'veterinario/actualizar_veterinario.html', {'veterinario': veterinario})

def borrar_veterinario(request, id_veterinario):
    veterinario = Veterinario.objects.get(id_veterinario=id_veterinario)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('ver_veterinarios')
    return render(request, 'veterinario/borrar_veterinario.html', {'veterinario': veterinario})

def agregar_consulta(request):
    mascotas = Mascota.objects.all()
    veterinarios = Veterinario.objects.all()
    if request.method == 'POST':
        id_mascota = request.POST['id_mascota']
        mascota = Mascota.objects.get(id_mascota=id_mascota)
        id_veterinario = request.POST['id_veterinario']
        veterinario = Veterinario.objects.get(id_veterinario=id_veterinario)
        fecha_consulta = request.POST['fecha_consulta']
        motivo = request.POST['motivo']
        diagnostico = request.POST['diagnostico']
        tratamiento = request.POST['tratamiento']
        costo = request.POST['costo']
        consulta = Consulta(id_mascota=mascota, id_veterinario=veterinario, fecha_consulta=fecha_consulta, motivo=motivo, diagnostico=diagnostico, tratamiento=tratamiento, costo=costo)
        consulta.save()
        return redirect('ver_consultas')
    return render(request, 'consulta/agregar_consulta.html', {'mascotas': mascotas, 'veterinarios': veterinarios})

def ver_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/ver_consultas.html', {'consultas': consultas})

def actualizar_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id_consulta=id_consulta)
    mascotas = Mascota.objects.all()
    veterinarios = Veterinario.objects.all()
    return render(request, 'consulta/actualizar_consulta.html', {'consulta': consulta, 'mascotas': mascotas, 'veterinarios': veterinarios})

def realizar_actualizacion_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id_consulta=id_consulta)
    if request.method == 'POST':
        id_mascota = request.POST['id_mascota']
        mascota = Mascota.objects.get(id_mascota=id_mascota)
        consulta.id_mascota = mascota
        id_veterinario = request.POST['id_veterinario']
        veterinario = Veterinario.objects.get(id_veterinario=id_veterinario)
        consulta.id_veterinario = veterinario
        consulta.fecha_consulta = request.POST['fecha_consulta']
        consulta.motivo = request.POST['motivo']
        consulta.diagnostico = request.POST['diagnostico']
        consulta.tratamiento = request.POST['tratamiento']
        consulta.costo = request.POST['costo']
        consulta.save()
        return redirect('ver_consultas')
    mascotas = Mascota.objects.all()
    veterinarios = Veterinario.objects.all()
    return render(request, 'consulta/actualizar_consulta.html', {'consulta': consulta, 'mascotas': mascotas, 'veterinarios': veterinarios})

def borrar_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id_consulta=id_consulta)
    if request.method == 'POST':
        consulta.delete()
        return redirect('ver_consultas')
    return render(request, 'consulta/borrar_consulta.html', {'consulta': consulta})

def agregar_vacuna(request):
    mascotas = Mascota.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        fecha_aplicacion = request.POST['fecha_aplicacion']
        id_mascota = request.POST['id_mascota']
        mascota = Mascota.objects.get(id_mascota=id_mascota)
        vacuna = Vacuna(nombre=nombre, tipo=tipo, fecha_aplicacion=fecha_aplicacion, id_mascota=mascota)
        vacuna.save()
        return redirect('ver_vacunas')
    return render(request, 'vacuna/agregar_vacuna.html', {'mascotas': mascotas})

def ver_vacunas(request):
    vacunas = Vacuna.objects.all()
    return render(request, 'vacuna/ver_vacunas.html', {'vacunas': vacunas})

def actualizar_vacuna(request, id_vacuna):
    vacuna = Vacuna.objects.get(id_vacuna=id_vacuna)
    mascotas = Mascota.objects.all()
    return render(request, 'vacuna/actualizar_vacuna.html', {'vacuna': vacuna, 'mascotas': mascotas})

def realizar_actualizacion_vacuna(request, id_vacuna):
    vacuna = Vacuna.objects.get(id_vacuna=id_vacuna)
    if request.method == 'POST':
        vacuna.nombre = request.POST['nombre']
        vacuna.tipo = request.POST['tipo']
        vacuna.fecha_aplicacion = request.POST['fecha_aplicacion']
        id_mascota = request.POST['id_mascota']
        mascota = Mascota.objects.get(id_mascota=id_mascota)
        vacuna.id_mascota = mascota
        vacuna.save()
        return redirect('ver_vacunas')
    mascotas = Mascota.objects.all()
    return render(request, 'vacuna/actualizar_vacuna.html', {'vacuna': vacuna, 'mascotas': mascotas})

def borrar_vacuna(request, id_vacuna):
    vacuna = Vacuna.objects.get(id_vacuna=id_vacuna)
    if request.method == 'POST':
        vacuna.delete()
        return redirect('ver_vacunas')
    return render(request, 'vacuna/borrar_vacuna.html', {'vacuna': vacuna})
