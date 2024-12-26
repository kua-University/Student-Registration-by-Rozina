from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Result(models.Model):
    """Model to store student results."""

    board = models.CharField(max_length=255)
    roll = models.IntegerField(
        validators=[
            MinValueValidator(1),  # Roll number should be at least 1
            MaxValueValidator(9999)  # Roll number should be at most 9999
        ]
    )
    gpa = models.IntegerField(
        validators=[
            MinValueValidator(0),   # GPA should be at least 0
            MaxValueValidator(4)    # GPA should be at most 4 (assuming a 4.0 scale)
        ]
    )

    def __str__(self):
        """Return the roll number as a string representation of the model."""
        return str(self.roll)

    class Meta:
        ordering = ['roll']  # Order by roll number
