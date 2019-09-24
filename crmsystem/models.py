
from mongoengine import Document, EmbeddedDocument, fields


class Project(EmbeddedDocument):
    ProjectId = fields.StringField(max_length=10, required=True, null=False)
    Name = fields.StringField(max_length=100, required=True)
    StartDate = fields.DateField()
    EndDate = fields.DateField()

class Skills(EmbeddedDocument):
    Technology = fields.StringField(max_length=250, required=True)
    Experience = fields.StringField(max_length=250)
    Level = fields.StringField(max_length=50)


class Employee(Document):
    EmployeeId = fields.StringField(max_length= 10, required=True, null=False)
    EmployeeName = fields.StringField(max_length=50, required=True)
    EmpWorkLocation = fields.StringField(max_length=100, required=True)
    EmpProject = fields.EmbeddedDocumentListField(Project)
    EmpSkills = fields.EmbeddedDocumentListField(Skills)