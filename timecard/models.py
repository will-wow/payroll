from django.db import models


class Employee(models.Model):
    """An employee record"""
    emp_num = models.PositiveIntegerField(primary_key=True)
    emp_group = models.PositiveIntegerField(null=True)
    name_first = models.CharField(max_length=24, blank=True)
    name_last = models.CharField(max_length=24, blank=True)
    name_mi = models.CharField(max_length=1, blank=True)
    name_suffix = models.CharField(max_length=5, blank=True)
    first_day = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['employee_last', 'employee_first']

    def full_name(self, last_first, first, last, suffix, mi=''):
        """Return a full name from name parts"""
        if last_first:
            name = last + ', ' + first
            if mi:
                name = name + ' ' + mi + '.'
            if suffix:
                name = name + ' ' + suffix  # don't add dot to suffix (it could be III, etc.)
        else:
            name = first
            if mi:
                name = name + ' ' + mi + '.'
            name = name + " " + last
            if suffix:
                name = name + ' ' + suffix

        return name

    def __unicode__(self):
        return self.full_name(False, self.name_first, self.name_last, self.name_suffix)


class Holiday(models.Model):
    """A company holiday"""
    holiday_date = models.DateField(primary_key=True)
    holiday_name = models.CharField(max_length=24)


class Day(models.Model):
    """A workday for an employee"""
    employee = models.ForeignKey(Employee)
    work_date = models.DateField()
    hours = models.PositiveSmallIntegerField(null=True)
    minutes = models.PositiveSmallIntegerField(null=True)
    pto = models.DecimalField(null=True)
    no_lunch = models.BooleanField(default=False)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['employee', 'work_date']

    def __unicode__(self):
        return '{0} {1} - {2}:{3}'.format(self.employee,
                                          self.work_date,
                                          self.hours,
                                          self.minutes)
