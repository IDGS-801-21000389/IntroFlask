from wtforms import Form, StringField
from wtforms import SearchField, IntegerField, PasswordField, FloatField, EmailField, validators

class UserForm(Form):
    matricula = IntegerField("Matricula: ", [
        validators.DataRequired(message="Llene este campo"),validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido")])
    
    nombre = StringField("Nombre: ", [
        validators.DataRequired(message="Llene este campo")])
    
    apaterno = StringField("Apellido Paterno: ", [
        validators.DataRequired(message="Llene este campo")])
    
    amaterno = StringField("Apellido Materno: ", [
        validators.DataRequired(message="Llene este campo")])
    
    correo = EmailField("Correo:", [
        validators.Email(message="Ingresa un correo valido")])