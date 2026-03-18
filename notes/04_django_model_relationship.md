# Django Model Relationships
In Django, models are Python classes that represent database tables. To connect models (i.e. database tables), Django provides three main types of relationships:
- One to One
- One to Many
- Many to Many
  

## One-to-Many (ForeignKey)
- One model has many instances of another model. Suppose first model is parent model and second model is child model
- A child model has a foreign key field to the parent model
- Relation builds with `ForeignKey` property
- Example: One author can write many books.

```py
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# driver code
author = Author.objects.create(name="Jane Austen")
book1 = Book.objects.create(title="Pride and Prejudice", author=author)
book2 = Book.objects.create(title="Prejudice and Pride", author=author)

book1.author  # return the Author instance
author.books.all()  # returns a queryset of all related Book instances
```


## Many-to-Many (ManyToManyField)
- A model can relate to many instances of another model and vice versa.
- Relation builds with `ManyToManyField` property
- Example: A student can enroll in multiple courses, and each course can have multiple students.
- Django creates an intermediate (junction) table behind the scenes.

### Without through (Auto-managed) attribute
When we run `makemigrations` and `migrate`, Django will create three tables in database:
- **appname_student -** for the `Student` model
- **appname_course -** for the `Course` model
- **appname_course_students -** an auto-generated junction table to manage the `Many-To-Many Relationship`.

The third table (e.g., course_students) has -
- id (optional unless specified)
- course_id (foreign key to Course)
- student_id (foreign key to Student)

### How Django manages it
- When we call `.add()`, `.remove()`, `.clear()` on the relationship, Django updates the junction table accordingly.
- No need to manually manage this table unless we need additional fields on the relationship.

```py
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

# Driver code
# Create students
student1 = Student.objects.create(name="Alice")
student2 = Student.objects.create(name="Bob")

# Create courses
course1 = Course.objects.create(name="Mathematics")
course2 = Course.objects.create(name="Physics")

# Add students to courses
course1.students.add(student1, student2) # Add Alice and Bob to course1
course2.students.add(student1)           # Add only Alice to Physics

# Alternatively
student1.courses.add(course1, course2)
student2.courses.add(course1)

# Accessing data
course1.students.all()  # List of students in Mathematics
student1.courses.all()  # List of courses Alice is enrolled in
student2.courses.all()  # List of courses Bob is enrolled in
```

### With through (Custom intermediate model)
- We need to specify a junction model for `Many-To-Many Relationship`, if we need to add some custom fields.
  
```py
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Enrollment', related_name='courses')

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField() # extra field we need to add
```

### How to Access
- From Course: `course.students.all()` (all students in the course).
- From Student: `student.courses.all()` (all courses the student is enrolled in).
- From Student: `student.enrollments.all()` (all Enrollment instances for the student).
- From Enrollment: `enrollment.course` or `enrollment.student`


## 3. One-to-One (OneToOneField)
- Each instance of a model is related to one and only one instance of another model.
- Example: A user can have only one profile.
- Often used to extend built-in models (like the Django User model).

```py
cfrom django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()

# driver code
profile.user    #returns the related User instance
user.profile    #returns the related Profile instance
```