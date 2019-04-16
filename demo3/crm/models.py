from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Roles(models.Model):
    rolename = models.CharField(max_length=20)

    def __str__(self):
        return self.rolename

class Modules(models.Model):
    modulename = models.CharField(max_length=20)

    def __str__(self):
        return self.modulename

class UserRoles(models.Model):
    userid = models.ForeignKey('Users',on_delete=models.CASCADE)
    roleid = models.ForeignKey('Roles',on_delete=models.CASCADE)


class RoleModules(models.Model):
    roleid = models.ForeignKey('Roles',on_delete=models.CASCADE)
    moduleid = models.ForeignKey('Modules',on_delete=models.CASCADE)

