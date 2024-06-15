from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='media/course_logo')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курсы на веб_сайт'
        verbose_name_plural = 'Курсы на веб_сайт'


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_time = models.CharField(max_length=77)
    course_day = models.CharField(max_length=23)
    course_duration = models.CharField(max_length=123)
    is_teens = models.BooleanField()
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, "Идет набор!"),
            (2, 'Набор зактрыт!'),
            (3, "Скоро набор!")
        ),
        default=3
    )
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курс'

    def __str__(self):
        return str(self.course)


