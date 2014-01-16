from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context, loader
from emailClient.models import *
from django.core import serializers
from  emailConnection import *
from composeForm import *
import json
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime
import time
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

# Create your views here.

def index(request):
	if request.user.is_authenticated():
		t = loader.get_template('tema1/inbox.tmpl.html')
		c = Context()
		return HttpResponse(t.render(c))
	else:
		return HttpResponseRedirect('/login/')

def emailFromFolder(request):
	imap_username = 'sirbunicolaecezar2@gmail.com'
	imap_password = 'mysecretpassword'
	if request.user.is_authenticated():
		# Do something for authenticated users.
		with MailBox(imap_username, imap_password) as mbox:
			msgs = mbox.get_msgs_headers('Inbox')
			msgs_json = {'emails':  []}
			email_items = []
			i = len(msgs)
			for msg in msgs:
				email_items.append({"id": "id1", "id_email": i, "subject": msg['subject'], "sender": msg['from'], "read": False, "date_recieved": msg['date']})
				i = i - 1
			msgs_json['emails'] = email_items
			return HttpResponse(json.dumps(msgs_json));
	else:
		return HttpResponse("Authentificate first!");

def details(request, emailId):
	return HttpResponse("Hello %s" % emailId);

def agendaTemplate(request):
	if request.user.is_authenticated():
		t = loader.get_template('tema1/contact-list.tmpl.html')
		c = Context({'utilizatori': email_users.objects.all(),'xx':4})
		#c = Context()
		return HttpResponse(t.render(c))
	else:
		t = loader.get_template('mustlogin.tmpl.html')
		c = Context()
		return HttpResponse(t.render(c))

def agendaJson(request):
	if request.user.is_authenticated():
		co = email_users.objects.all()
		c = serializers.serialize('json', co)
		return HttpResponse(c);
	else:
		t = loader.get_template('new/mustlogin.tmpl.html')
		c = Context()
		return HttpResponse(t.render(c))

def readMail(request):
	if request.user.is_authenticated():
		imap_username = 'sirbunicolaecezar2@gmail.com'
		imap_password = 'mysecretpassword'
		id_email = request.GET['id_email']
		with MailBox(imap_username, imap_password) as mbox:
			mail = mbox.fetch_message(id_email)
			for part in mail.walk():
				if part.get_content_type() == 'text/plain':
					body = part.get_payload()

			match = re.search(r'[\w\.-]+@[\w\.-]+', mail['from'])
			email = match.group(0)
			c = Context({"mail": mail, "body": body, "id_email": id_email, "email": email})
			t = loader.get_template('tema1/email.tmpl.html')
			return HttpResponse(t.render(c))
	else:
		return HttpResponse("Eroare")

def composeEmail(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = ComposeForm(request.POST)
			if form.is_valid():
				to = []
				to.append(form.cleaned_data['to'])
				subject = form.cleaned_data['subject']
				message = form.cleaned_data['message']
				send_mail(subject, message, 'sirbunicolaecezar2@gmail.com', to)
				t = loader.get_template('tema1/mailsent.tmpl.html')
				c = RequestContext(request, {'form': form})
				return HttpResponse(t.render(c))
		else:
			form = ComposeForm()
			t = loader.get_template('tema1/compose.tmpl.html')
			c = RequestContext(request, {'form': form})
			return HttpResponse(t.render(c))
	else:
		t = loader.get_template('new/mustlogin.tmpl.html')
		c = Context()
		return HttpResponse(t.render(c))

def replyPage(request):
	if request.user.is_authenticated():
		imap_username = 'sirbunicolaecezar2@gmail.com'
		imap_password = 'mysecretpassword'
		id_email = request.GET['id_email']
		with MailBox(imap_username, imap_password) as mbox:
			mail = mbox.fetch_message(id_email)
			for part in mail.walk():
				if part.get_content_type() == 'text/plain':
					body = part.get_payload()

			match = re.search(r'[\w\.-]+@[\w\.-]+', mail['from'])
			email = match.group(0)
			c = RequestContext(request, {"mail": mail, "body": body, "id_email": id_email, "email": email})
			t = loader.get_template('tema1/reply.tmpl.html')
			return HttpResponse(t.render(c))
	else:
		return HttpResponse("Eroare")


def authenticate_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/inbox/')
		else:
			return HttpResponse("Contul %s este inactiv" %user)
	else:
		return HttpResponse("User/Parola incorecta")

def loginView(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/email/')
	else:
		t = loader.get_template('tema1/index.tmpl.html')
		c = RequestContext(request)
		return HttpResponse(t.render(c))

def logoffView(request):
	logout(request)
	return HttpResponseRedirect('/login/')
