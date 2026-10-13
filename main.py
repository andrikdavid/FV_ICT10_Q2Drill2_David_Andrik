from pyscript import document, display

# List of Hogwarts students
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

new_students = set()

def add(e):
    # Get the names from the input boxes
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()
    
    # Only add if the user actually typed something
    if first_name and last_name:
        fullname = f"{first_name} {last_name}"
        new_students.add(fullname)
    
    # Combine the original set with the new student set
    final_students = students | new_students

    # Clear previous output container content and display the updated list
    output_div = document.getElementById("output1")
    output_div.innerHTML = ""

    display(final_students, target='output1')