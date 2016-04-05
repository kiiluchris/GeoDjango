from django import forms


class UserForm(forms.ModelForm):
	class Meta:
		model = social_data.user
		fields = [
			"extra_data",
		]