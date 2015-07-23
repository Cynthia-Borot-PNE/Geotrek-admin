# -*- coding: utf-8 -*-
from django import forms as django_forms
from django.db.models.fields.related import ForeignKey, ManyToManyField, FieldDoesNotExist
from django.utils.translation import ugettext_lazy as _

import floppyforms as forms
from mapentity.forms import MapEntityForm

from geotrek.authent.models import (default_structure, StructureRelated,
                                    StructureRelatedQuerySet)

from .mixins import NoDeleteMixin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import FormActions


class CommonForm(MapEntityForm):

    class Meta:
        fields = []

    def deep_remove(self, fieldslayout, name):
        if isinstance(fieldslayout, list):
            for field in fieldslayout:
                self.deep_remove(field, name)
        elif hasattr(fieldslayout, 'fields'):
            if name in fieldslayout.fields:
                fieldslayout.fields.remove(name)
            for field in fieldslayout.fields:
                self.deep_remove(field, name)

    def replace_orig_fields(self):
        model = self._meta.model
        codeperm = '%s.publish_%s' % (
            model._meta.app_label, model._meta.object_name.lower())
        if 'published' in self.fields and self.user and not self.user.has_perm(codeperm):
            del self.fields['published']
            self.deep_remove(self.fieldslayout, 'published')
        if 'review' in self.fields and self.instance and self.instance.any_published:
            del self.fields['review']
            self.deep_remove(self.fieldslayout, 'review')
        super(CommonForm, self).replace_orig_fields()

    def filter_related_field(self, name, field):
        if not isinstance(field, django_forms.models.ModelChoiceField):
            return
        try:
            modelfield = self.instance._meta.get_field(name)
        except FieldDoesNotExist:
            # be careful but custom form fields, not in model
            modelfield = None
        if not isinstance(modelfield, (ForeignKey, ManyToManyField)):
            return
        model = modelfield.related.parent_model
        # Filter structured choice fields according to user's structure
        if issubclass(model, StructureRelated):
            field.queryset = StructureRelatedQuerySet.queryset_for_user(
                field.queryset, self.user)
        if issubclass(model, NoDeleteMixin):
            field.queryset = field.queryset.filter(deleted=False)

    def __init__(self, *args, **kwargs):
        super(CommonForm, self).__init__(*args, **kwargs)

        # Check if structure is present, if so, use hidden input
        if 'structure' in self.fields:
            self.fields['structure'].widget = forms.HiddenInput()
            # On entity creation, use user's structure
            if not self.instance or not self.instance.pk:
                structure = default_structure()
                if self.user:
                    structure = self.user.profile.structure
                self.fields['structure'].initial = structure

        for name, field in self.fields.items():
            self.filter_related_field(name, field)


class ImportDatasetForm(django_forms.Form):
    parser = forms.TypedChoiceField(
        label=_('Parser'),
        widget=forms.RadioSelect,
        required=True,
    )

    def __init__(self, choices=None, *args, **kwargs):
        super(ImportDatasetForm, self).__init__(*args, **kwargs)

        self.fields['parser'].choices = choices

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    'parser',
                ),
                FormActions(
                    Submit('import-web', _("Import"), css_class='button white')
                ),
                css_class='file-attachment-form',
            )
        )


class ImportDatasetFormWithFile(ImportDatasetForm):
    zipfile = forms.FileField(
        label=_('File'),
        required=True,
        widget=forms.FileInput
    )

    def __init__(self, *args, **kwargs):
        super(ImportDatasetFormWithFile, self).__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Div(
                Div(
                    'parser',
                    'zipfile',
                ),
                FormActions(
                    Submit('upload-file', _("Upload"), css_class='button white')
                ),
                css_class='file-attachment-form',
            )
        )

    def clean_zipfile(self):
        if self.cleaned_data['zipfile'].content_type != "application/zip":
            raise django_forms.ValidationError(
                _("File must be of ZIP type."), code='invalid')
