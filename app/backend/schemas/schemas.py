from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from app.backend.database.register import RegisterUser

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RegisterUser
        load_instance = True
        include_fk = True
        dump_only = ("id",)

    
    username = ma.auto_field(required=True, validate=validate.Length(min=3, max=50))
    email = ma.auto_field(required=True, validate=validate.Email())
    hashed_password = ma.auto_field(load_only=True, required=True)

class LoginSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))

class RegisterSchema(ma.Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))

class CompanySchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    website = fields.Url()

class JobSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    company = fields.Nested(CompanySchema, allow_none=True)
    area = fields.Str()
    country = fields.Str()
    location = fields.Str()
    description = fields.Str()
    keywords = fields.List(fields.Str())

user_schema = UserSchema()
users_schema = UserSchema(many=True)
login_schema = LoginSchema()
register_schema = RegisterSchema()
company_schema = CompanySchema()
job_schema = JobSchema()