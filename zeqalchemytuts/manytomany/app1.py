from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

db_url = "sqlite:///manytomany/database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

#This enables us to use class as the blueprint for our table
Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column('doctor_id', Integer, ForeignKey('doctors.id'))
    patient_id = Column('patient_id', Integer, ForeignKey('patients.id'))
    appointment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    #Having the relatonship defined in the associative table
    #allows for query on the instance of the Doctor and Patient classes
    #Access to info on both tables is only possible thru the associtive table
    #using appointments class as a reference point to collect information
    #rather than accessing info directly on the individual classes

    doctor = relationship("Doctor", backref="appointments")
    patient = relationship("Patient", backref="appointments")

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    specialty = Column(String)
    
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(DateTime)


Base.metadata.create_all(engine)

dr_smith = Doctor(name='Dr. Smith', specialty='Cardiology')
john_doe = Patient(name='John Doe', dob=datetime(1990, 1, 1))
appointment = Appointment(doctor=dr_smith, patient=john_doe, notes='Routine check-up')
session.add_all([dr_smith, john_doe])
session.commit()

# Find all appointments for either doctor or patient
appointments_for_dr_smith = session.query(Appointment).filter(Appointment.doctor.has(name='Dr. Smith')).all()
print("Dr. Smith's appointments")
print(appointments_for_dr_smith)

appointments_for_john_doe = session.query(Appointment).filter(Appointment.patient.has(name='John Doe')).all()
print("John Doe's appointments")
print(appointments_for_john_doe)

