from django.contrib.auth.decorators import login_required
from edxmako.shortcuts import render_to_response
from student.views.dashboard import _student_dashboard


@login_required
def programs_dashboard(request):
    context = _student_dashboard(request)
    return render_to_response('tma_apps/programs_dashboard.html', context)