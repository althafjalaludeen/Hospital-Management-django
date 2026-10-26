from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class PatientView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        patient_name = form_data.get('patient_name')
        age = form_data.get('age')
        gender = form_data.get('gender')
        phone = form_data.get('phone')
        disease = form_data.get('disease')
        print(request_body)
        data = {
            'message': 'Patient API is working fine',
            'Patient_Name': patient_name,
            'Age': age,
            'Gender': gender,
            'Phone': phone,
            'Disease': disease
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class DoctorView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        doctor_name = form_data.get('doctor_name')
        department = form_data.get('department')
        experience = form_data.get('experience')
        consultation_fee = form_data.get('consultation_fee')
        print(request_body)
        data = {
            'message': 'Doctor API is working fine',
            'Doctor_Name': doctor_name,
            'Department': department,
            'Experience': experience,
            'Consultation_Fee': consultation_fee
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class AppointmentView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        patient_name = form_data.get('patient_name')
        doctor_name = form_data.get('doctor_name')
        appointment_date = form_data.get('appointment_date')
        appointment_time = form_data.get('appointment_time')
        print(request_body)
        data = {
            'message': 'Appointment API is working fine',
            'Patient_Name': patient_name,
            'Doctor_Name': doctor_name,
            'Appointment_Date': appointment_date,
            'Appointment_Time': appointment_time
        }
        return JsonResponse(data)
