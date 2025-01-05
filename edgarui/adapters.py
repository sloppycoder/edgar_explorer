from allauth.account.adapter import DefaultAccountAdapter


class NoSignupAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):  # pyright: ignore
        # Always return False to disable signup
        return False
