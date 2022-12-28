def Authentication(request):
    if request.session.has_key('user_email'):
        user_email = request.session['user_email']
        user_id = request.session['user_id']
        user_name = request.session['user_name']
        context={
            "user_email":user_email,
            "user_name":user_name,
            "user_id":user_id
        }
        return(context)
    else:
        context={
            "user_email":None,
            "user_name":None,
            "user_id":None
        }
        return(context)