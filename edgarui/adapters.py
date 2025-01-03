from allauth.account.adapter import DefaultAccountAdapter


class NoSignupAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # Always return False to disable signup
        return False
