from django.db import models

class Dueño(models.Model):
    id_dueño = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    id_dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre


class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    num_colegiado = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    id_veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    motivo = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Consulta {self.id_consulta} - {self.id_mascota.nombre}"


class Vacuna(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    fecha_aplicacion = models.DateField()
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
