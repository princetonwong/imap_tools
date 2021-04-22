import datetime
    
DATA = dict(
    subject='Re: Saying Hello',
    from_='mary@example.net',
    to=('jdoe@machine.example',),
    cc=(),
    bcc=(),
    reply_to=('smith@home.example',),
    date=datetime.datetime(1997, 11, 21, 10, 1, 10, tzinfo=datetime.timezone(datetime.timedelta(-1, 64800))),
    date_str='Fri, 21 Nov 1997 10:01:10 -0600',
    text='This is a reply to your hello.\r\n',
    html='',
    headers={'from': ('Mary Smith <mary@example.net>',), 'to': ('John Doe <jdoe@machine.example>',), 'reply-to': ('"Mary Smith: Personal Account" <smith@home.example>',), 'subject': ('Re: Saying Hello',), 'date': ('Fri, 21 Nov 1997 10:01:10 -0600',), 'message-id': ('<3456@example.net>',), 'in-reply-to': ('<1234@local.machine.example>',), 'references': ('<1234@local.machine.example>',)},
    attachments=[],
    from_values={'email': 'mary@example.net', 'name': 'Mary Smith', 'full': 'Mary Smith <mary@example.net>'},
    to_values=({'email': 'jdoe@machine.example', 'name': 'John Doe', 'full': 'John Doe <jdoe@machine.example>'},),
    cc_values=(),
    bcc_values=(),
    reply_to_values=({'email': 'smith@home.example', 'name': 'Mary Smith: Personal Account', 'full': 'Mary Smith: Personal Account <smith@home.example>'},),
)