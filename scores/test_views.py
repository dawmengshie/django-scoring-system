from django.http import HttpResponse


def test_view(request):
    """Simple test view to debug 500 error"""
    try:
        return HttpResponse("Test view working - no 500 error!")
    except Exception as e:
        return HttpResponse(f"Error in test view: {str(e)}", status=500)
