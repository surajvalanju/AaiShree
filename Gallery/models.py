from django.db import models


class Gallery(models.Model):
    ImageName = models.CharField(max_length=250)
    DisplayName = models.CharField(max_length=350)
    ImageUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.DisplayName  #use + to add more


class ImgInfo(models.Model):
    image = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    Discription = models.CharField(max_length=5000)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.Discription  #use + to add more


class OurProjects(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=600)

    def __str__(self):
        return self.name


class OurProjectImages(models.Model):
    ourProject = models.ForeignKey(OurProjects, on_delete=models.CASCADE)
    ImageUrl = models.FileField()
    ProjectName = models.CharField(max_length=600)

    def __str__(self):
        return self.ProjectName

