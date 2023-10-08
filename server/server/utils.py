from django.db import models





class CustomAutoIncrementSaleField(models.CharField):
    def pre_save(self, model_instance, add):
        if add and getattr(model_instance, self.attname) is None:
            # Get the maximum value of the field in the database
            max_value = model_instance.__class__.objects.aggregate(models.Max(self.attname)).get(self.attname + '__max')

            # Increment the value by 1
            next_value = int((max_value or 0)[3:]) + 1

            # Set the field value with the custom format
            setattr(model_instance, self.attname, 'BDS-Sale-{:03d}'.format(next_value))

        return super().pre_save(model_instance, add)
    
class CustomAutoIncrementHireField(models.CharField):
    # def to_internal_value(self, data):
    #     # Write your auto-increment logic here
    #     # Retrieve the latest maBDS value from the database
    #     latest_maBDS = HomeHire.objects.order_by('maBDS').last()
    #     if latest_maBDS:
    #         last_number = int(latest_maBDS.maBDS)
    #         new_number = last_number + 1
    #     else:
    #         new_number = 1
    #     # Format the new maBDS value with leading zeros
    #     new_maBDS = str(new_number).zfill(6)
    #     return new_maBDS


    def pre_save(self, model_instance, add):
        if add and getattr(model_instance, self.attname) is None:
            # Get the maximum value of the field in the database
            max_value = model_instance.__class__.objects.aggregate(models.Max(self.attname)).get(self.attname + '__max')

            # Increment the value by 1
            next_value = int((max_value or 0)[3:]) + 1

            # Set the field value with the custom format
            setattr(model_instance, self.attname, 'BDS-Hire-{:03d}'.format(next_value))
    
        return super().pre_save(model_instance, add)
    
   