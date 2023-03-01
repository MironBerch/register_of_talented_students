import os
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse

from students.services import get_student_contest_by_id, get_student_by_id
from users.mixins import SuperUserRequiredMixin
from students.forms import StudentsImportForm
from students.input import import_students


class ImportStudentsView(
    SuperUserRequiredMixin,
    TemplateResponseMixin,
    View,
):

    template_name = 'students/import_student.html'
    form_class = StudentsImportForm

    def get(self, request):
        return self.render_to_response(
            context = {
                'form': self.form_class(),
            },
        )
    
    def post(self, request):
        form = StudentsImportForm(request.POST or None, files=request.FILES or None)

        if form.is_valid():
            students = form.save()
            filename = students.file.open('r')
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '/media/' + str(filename)
            import_students(filepath)
            return redirect('list')
        
        return self.render_to_response(
            context = {
                'form': self.form_class(),
            },
        )
    

class StudentDetailView(
    LoginRequiredMixin,
    TemplateResponseMixin,
    View,
):
    
    template_name = 'students/detail_student.html'

    def get(self, request, id):
        return self.render_to_response(
            context = {
                'contests': get_student_contest_by_id(id=id),
                'student': get_student_by_id(id=id)
            },
        )


def download_students_import_example(request):
    """Download example excel file"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'students_import_example.xlsx'
    filepath = BASE_DIR + '/media/' + filename
    file = open(filepath, 'rb')
    response = FileResponse(file)
    return response