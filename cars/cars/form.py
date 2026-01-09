from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    
    model = forms.CharField(max_length=255)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    price = forms.FloatField(required=False)
    factory_year = forms.IntegerField(required=False)
    model_year = forms.IntegerField(required=False)
    plate = forms.CharField(max_length=10, required=False)
    image = forms.ImageField(required=False)

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            price=self.cleaned_data['price'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            image=self.cleaned_data['image']
        )
        car.save()
        return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price', 'Value must be greater than $ 0')
        return price

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1970 or factory_year > 2025:
            self.add_error('factory_year', 'Factory year must be between 1970 and 2025')
        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year < 1970 or model_year > 2025:
            self.add_error('model_year', 'Model year must be between 1970 and 2025')
        return model_year

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        if plate is None:
            return plate
        if plate < 0 or plate > 10:
            self.add_error('plate', 'Plate must be between 0 and 10')
        return plate

