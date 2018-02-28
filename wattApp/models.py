from django.db import models

class User(models.Model):

    user_id=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    sID=models.IntegerField()

    def __str__(self):
        return self.user_id

class Plant(models.Model):
    
    owner=models.ForeignKey(User)
    name=models.CharField(max_length=20)
    humidityGoal=models.IntegerField()
    sID = models.IntegerField()

    def __str__(self):
        return "Plant name: "+self.name+". Owned by: "+self.owner.user_id
        

class User_Measure(models.Model):

    temperature=models.IntegerField()
    humidity=models.IntegerField()
    user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Room Temperature Value: "+str(self.temperature)\
               +" & Humidity value: "+str(self.humidity)
    

class Plant_Measure(models.Model):

    humidity=models.IntegerField()
    plant=models.ForeignKey(Plant)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Humidity Value: "+str(self.humidity)+". From Plant: "+self.plant.name+"."

