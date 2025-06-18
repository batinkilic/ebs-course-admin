import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    program = db.Column(db.String, nullable=False)
    code = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "program": self.program,
            "code": self.code,
            "name": self.name
        }

class CourseDetail(db.Model):
    __tablename__ = 'course_details'
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    program_outcome_mapping = db.Column(JSON)   # Ders Öğ. Çıkt.–Program Yeterliliği
    evaluation              = db.Column(JSON)   # Değerlendirme Sistemi
    workload                = db.Column(JSON)   # AKTS / İş Yükü Tablosu
    outcomes                = db.Column(JSON)   # Dersin Öğrenme Çıktıları
    weekly_plan             = db.Column(JSON)   # Haftalara Göre Konular
    instructors             = db.Column(db.Text) # Öğretim Elemanları

    def serialize(self):
        return {
            "course_id": self.course_id,
            "program_outcome_mapping": self.program_outcome_mapping,
            "evaluation": self.evaluation,
            "workload": self.workload,
            "outcomes": self.outcomes,
            "weekly_plan": self.weekly_plan,
            "instructors": self.instructors
        }
