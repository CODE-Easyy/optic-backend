from django.shortcuts import render

# Create your views here.
def ger_order(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        import time
        import webbrowser as wb
        # import pyautogui as pg

        wb.open('https://web.whatsapp.com/send?phone=+77761688760&text=' + text)
        time.sleep(30)
        # pg.press('enter')
        return render(request, 'orders/home.html')
    return render(request, 'orders/home.html')
