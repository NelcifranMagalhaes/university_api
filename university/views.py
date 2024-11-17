from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        estudent = {
            'id':'1',
            'nome':'midoryia'
        }
        return JsonResponse(estudent)
