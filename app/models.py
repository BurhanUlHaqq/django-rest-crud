from django.db import models

# Model representing an Author with 10 fields
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    biography = models.TextField(blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    awards = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # class Meta:
    #     ordering = ['id']  # Default ordering by id

# Model representing a Book with 12 fields, linked to an Author (One-to-Many)
class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    publish_date = models.DateField()
    number_of_pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    summary = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['id']  # Default ordering by id

# Model representing a User Profile with 3 fields
class Profile(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - Profile'

    class Meta:
        ordering = ['id']  # Default ordering by id


