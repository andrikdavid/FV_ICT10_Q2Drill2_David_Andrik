from pyscript import document, display

# List of original Hogwarts students
students = {
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Draco Malfoy",
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley",
    "Fred Weasley",
    "George Weasley",
    "Cedric Diggory",
    "Cho Chang",
    "Seamus Finnigan",
    "Dean Thomas",
    "Parvati Patil",
    "Padma Patil",
    "Lavender Brown",
    "Pansy Parkinson",
    "Gregory Goyle",
    "Vincent Crabbe",
    "Colin Creevey",
    "Jacque Delmudez"
}

# Set for newly added students
new_students = set()

# Combines the original and new students
master_students = students | new_students

# Adds a new student to the list

def add(e):
    # Gets the inputted names
    first = document.getElementById("firstname").value.strip()
    last = document.getElementById("lastname").value.strip()

    # Combines the first and last names
    full_name = first + " " + last

    # Adds the new student
    new_students.add(full_name)

    # Combines both sets
    master_students = students | new_students

    # Counts the total members
    count = len(master_students)

    # Clears the previous results
    document.getElementById("result").innerHTML = ""
    document.getElementById("total").innerHTML = ""

    # Displays the updated list and total
    display(", ".join(master_students), target="result")
    display(f"There are {count} official students in Hogwarts School of Witchcraft! ✨", target="total")

    # Clears the input fields
    document.getElementById("firstname").value = ""
    document.getElementById("lastname").value = ""
