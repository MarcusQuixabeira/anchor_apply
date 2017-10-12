# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import re

# Create your models here.
class Avaliation(models.Model):
    upload = models.FileField(upload_to='uploads', null=False)
    result = models.TextField(null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.upload.name

    def process(self):
        data = []
        result = ""
        first_line = ""
        pattern = re.compile("(^[4-6]\d{15})$|(^[4-6]\d{3}-\d{4}-\d{4}-\d{4})")
        pattern2 = re.compile(r'(.)\1{3}')
        lines = self.upload.read().splitlines()

        for line in lines:
            if len(line) > 0:
                data.append(line)

        try:
            first_line = int(data[0])
        except Exception as e:
             self.result = 'The N (first line) value must be a number'
             return self.result

        if first_line != (len(data) -1):
            self.result = 'The N (first line) value diverges from the card numbers found'
            return self.result

        data.remove(data[0])

        if len(data) > 0:
            if first_line > 0 and first_line < 100:
                for line in data:
                    if pattern.match(line):
                        if "-" in line:
                            no_hifen_line = line.replace("-","")
                            if pattern2.search(no_hifen_line):
                                result += line + ' [Invalid] \n'
                            else:
                                result += line + ' [Valid] \n'
                        else:
                            if pattern2.search(line):
                                result += line + ' [Invalid] \n'
                            else:
                                result += line + ' [Valid] \n'
                    else:
                        result += line + ' [Invalid] \n'
            else:
                result = 'N can\'t be greater than 100'
        else:
            result = 'The file can\'t be blank'

        self.result = result

        return result
