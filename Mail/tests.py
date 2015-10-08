from django.test import TestCase
import Mail.views
from Mail.models import Email
from django.core.urlresolvers import reverse
from django.utils import timezone

def create_email(sender, receiver, date = timezone.now(), subject = 'Empty', content = 'Empty', is_deleted = False, is_read = False):
    return Email.objects.create(sender=sender, receiver=receiver, date=date, subject=subject,
                                content=content, is_deleted=is_deleted, is_read=is_read)

def assert_queryset_objects_equal(self,context_queryset, other_queryset, ordered=False):
    return self.assertQuerysetEqual(context_queryset, map(repr, other_queryset), ordered=ordered)


# Create your tests here.
class InboxTests(TestCase):

    def test_inbox_doesnt_contain_mail_sent_by_owner(self):
        create_email(sender=Mail.views.my_email, receiver='otherguy@gmail.com')
        email_not_from_self = create_email(sender='someone@gmail.com', receiver='otherguy@gmail.com')
        response = self.client.get(reverse('mail:inbox'))
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'], [email_not_from_self,])

    def test_inbox_doesnt_contain_deleted_mail(self):
        create_email(sender='someguy@gmail.com', receiver='otherguy@gmail.com', is_deleted=True)
        email_not_deleted = create_email(sender='someone@gmail.com', receiver='otherguy@gmail.com', is_deleted=False)
        response = self.client.get(reverse('mail:inbox'))
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'], [email_not_deleted,])

    def test_inbox_with_search_params(self):
        create_email(sender='someguy@gmail.com', receiver='otherguy@gmail.com')
        target_sender = create_email(sender='tArget@gmail.com', receiver='otherguy@gmail.com')
        target_content = create_email(sender='someguy@gmail.com', receiver='otherguy@gmail.com', content='TArGEThsbdfkjdnfksd')
        target_subject = create_email(sender='someguy@gmail.com', receiver='somereceiver@gmail.com' ,subject='subjectTargETsubject')
        response = self.client.get(reverse('mail:inbox') + '?searchParams=TaRGet')
        self.assertEqual(response.status_code, 200)
        assert_queryset_objects_equal(self, response.context['emails'], [target_sender, target_content, target_subject,])


# class EmailDetailTests(TestCase):
