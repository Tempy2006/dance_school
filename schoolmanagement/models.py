from django.db import models


class School(models.Model):
    name = models.CharField("nome", max_length=100)
    street = models.CharField("indirizzo", max_length=150)
    city = models.CharField("città", max_length=80)
    province = models.CharField("provincia", max_length=2)
    zip = models.CharField("CAP", max_length=5)
    country = models.CharField("paese", max_length=80, default="Italia")
    website = models.URLField("sito web")
    phone = models.CharField("telefono", max_length=30)
    email = models.EmailField()
    vat = models.CharField("partita IVA", max_length=11)

    class Meta:
        ordering = ["name"]
        verbose_name = "sede"
        verbose_name_plural = "sedi"

    def __str__(self):
        return self.name
