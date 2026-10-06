from django.db import models


class Department(models.Model):
    name = models.CharField("Назва кафедри", max_length=100)
    head = models.CharField("Завідувач кафедри", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"


class Specialty(models.Model):
    name = models.CharField("Назва спеціальності", max_length=100)
    code = models.CharField("Код спеціальності", max_length=20)
    description = models.TextField("Опис спеціальності")
    coordinator_name = models.CharField("Ім'я координатора набору", max_length=100)
    coordinator_contact = models.CharField("Контакт координатора", max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="specialties",
        verbose_name="Випускова кафедра",
    )
    disciplines = models.TextField(
        verbose_name="Список дисциплін",
        help_text="Вкажіть дисципліни через кому або кожну з нового рядка",
    )

    def __str__(self):
        return f"{self.code} {self.name}"

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


class Teacher(models.Model):
    full_name = models.CharField("ПІБ викладача", max_length=100)
    position = models.CharField("Посада", max_length=100)
    academic_degree = models.CharField("Науковий ступінь", max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра",
    )

    def __str__(self):
        return f"{self.full_name} ({self.position})"

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class HomePageInfo(models.Model):
    faculty_name = models.CharField(
        max_length=100,
        default="Факультет природничих наук (ФПрН)",
        verbose_name="Назва факультету",
    )
    description = models.TextField("Опис факультету")
    general_info = models.TextField("Основна інформація")
    contacts = models.TextField("Контакти")

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name = "Інформація головної сторінки"
        verbose_name_plural = "Інформація головної сторінки"


class ExchangeProgram(models.Model):
    university = models.CharField("Університет", max_length=255)
    languages = models.CharField("Мови навчання", max_length=255)
    places = models.CharField("Кількість місць", max_length=50)
    deadline = models.DateField("Дедлайн подачі")
    description = models.TextField("Опис")
    country = models.CharField("Країна", max_length=100, default="", blank=True)

    def __str__(self):
        return self.university

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"
