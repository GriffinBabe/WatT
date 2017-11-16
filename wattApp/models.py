from django.db import models

class User(models.Model):

    user_id=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    #age=models.IntegerField()

    def __str__(self):
        return self.user_id

class Plant(models.Model):
    
    owner=models.ForeignKey(User)
    name=models.CharField(max_length=20)
    humidityGoal=models.IntegerField()

    def __str__(self):
        return "Plant name: "+self.name+". Owned by: "+self.owner.user_id
        

class TMeasure(models.Model):

    value=models.IntegerField()
    plant=models.ForeignKey(Plant)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Temperature Value: "+str(self.value)+". From Plant: "+self.plant.name+"."
    

class HMeasure(models.Model):

    value=models.IntegerField()
    plant=models.ForeignKey(Plant)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Humidity Value: "+str(self.value)+". From Plant: "+self.plant.name+"."
    
    
