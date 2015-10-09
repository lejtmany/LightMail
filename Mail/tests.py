from django.test import TestCase
import Mail.views
from Mail.models import Email, Contact
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template import defaultfilters
# from selenium.webdriver.chrome.webdriver import WebDriver
# from django.test import LiveServerTestCase


def create_email(sender='sender@gmail.com', receiver='receiver@gmail.com', date=timezone.now(), subject='Empty',
                 content='Empty', is_deleted=False, is_read=False):
    return Email.objects.create(sender=sender, receiver=receiver, date=date, subject=subject,
                                content=content, is_deleted=is_deleted, is_read=is_read)

def create_contact(first_name='John', last_name='Doe', dob=timezone.now(), email='jdoe@gmail.com'):
    return Contact.objects.create(first_name=first_name, last_name=last_name, dob=dob, email=email)


def assert_queryset_objects_equal(self, context_queryset, other_queryset, ordered=False):
    return self.assertQuerysetEqual(context_queryset, map(repr, other_queryset), ordered=ordered)


# Create your tests here.
class InboxTests(TestCase):
    def test_inbox_doesnt_contain_mail_sent_by_owner(self):
        create_email(sender=Mail.views.my_email, receiver='otherguy@gmail.com')
        email_not_from_self = create_email()
        response = self.client.get(reverse('mail:inbox'))
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'], [email_not_from_self, ])

    def test_inbox_doesnt_contain_deleted_mail(self):
        create_email(is_deleted=True)
        email_not_deleted = create_email(is_deleted=False)
        response = self.client.get(reverse('mail:inbox'))
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'], [email_not_deleted, ])

    def test_inbox_with_search_params(self):
        create_email()
        target_sender = create_email(sender='tArget@gmail.com')
        target_content = create_email(content='TArGEThsbdfkjdnfksd')
        target_subject = create_email(subject='subjectTargETsubject')
        response = self.client.get(reverse('mail:inbox') + '?searchParams=TaRGet')
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'],
                                      [target_sender, target_content, target_subject, ])


class EmailDetailTests(TestCase):

    def test_email_detail_populates(self):
        now = timezone.now()
        sender = 'sender@gmail.com'
        receiver = 'receiver@gmail.com'
        content = 'hello world'
        create_email(sender=sender, receiver=receiver, date=now, content=content)
        response = self.client.get(reverse('mail:email_detail', args=[1]))
        self.assertContains(response, sender,
                            status_code=200)
        self.assertContains(response, content,
                            status_code=200)
        self.assertContains(response, defaultfilters.date(now),
                            status_code=200)

class ComposeEmailTests(TestCase):

    def test_compose_email_populates_receiver(self):
        receiver = 'receiver@gmail.com'
        create_email(receiver=receiver)
        response = self.client.get(reverse('mail:compose_email') + '?compose_to=' + receiver)
        self.assertContains(response, receiver,
                            status_code=200)

class SentEmailListTests(TestCase):

    def test_sent_emails_list_only_contains_sent_emails(self):
        bad_message = 'Stranger!'
        create_email(sender=Mail.views.my_email)
        create_email(sender=Mail.views.my_email)
        create_email(sender='other_person@gmail.com', content=bad_message)
        response = self.client.get(reverse('mail:sent_emails'))
        self.assertNotContains(response, bad_message,
                            status_code=200)

class ContactListTests(TestCase):

    def test_search_for_contact(self):
        fname_match = create_contact(first_name='MArv')
        lname_match =create_contact(last_name='MaRv')
        email_match =create_contact(email='MarV@gmail.com')
        no_match = create_contact()
        response = self.client.get(reverse('mail:contacts')+ '?searchParams=MARV')
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['contacts'], [fname_match, lname_match,email_match])