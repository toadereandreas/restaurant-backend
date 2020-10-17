from django import forms


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.populate_data_with_instance_values()

    def populate_data_with_instance_values(self):
        """
        Since GraphQL can send incomplete data to an update form, we want to
        pre-populate data with existing values that are in the database.
        The values from db are populated on the initial property by model form.
        """
        for field, value in self.initial.items():
            self.data[field] = self.data.get(field, value)
