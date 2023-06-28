from django.db import models
from django.urls import reverse


from django.core.validators import MinValueValidator, MaxValueValidator


class ComputerBrands(models.Model):
    brand_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.brand_name


class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=100)
    price_min = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(20000.00)])
    price_max = models.DecimalField(max_digits=10, decimal_places=2,  validators=[MaxValueValidator(100000.00)])
    ram = models.IntegerField(validators=[MinValueValidator(1)])
    brand = models.ForeignKey(ComputerBrands, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.brand.brand_name} - {self.generation}'


class Computer(models.Model):
    computer_code = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit_rate = models.IntegerField(validators=[MinValueValidator(0)])
    total_price = models.IntegerField(validators=[MinValueValidator(0)])
    computer = models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_rate
        super().save(*args, **kwargs)

    def __str__(self):
        # return f'{self.computer_code} - {self.computer.generation}'
        return f'{self.computer.generation}'
    
    def get_absolute_url(self):
        return reverse('home')
