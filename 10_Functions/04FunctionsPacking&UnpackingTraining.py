#------------------------------------------------------
# Functions Packing and Unpacking Training
#--------------------------------
#   - *Args
#   - Unknown Number of Arguments
#   - Function Default Parameters
#   - Keyword Arguments
#   - Arbitrary Arguments (*kwargs)
#   - Keyword Arbitrary Arguments (**kwargs)
#------------------------------------------------------

Tuple = ("01", "02", "03")

MySkills = {
    'ROS2': "70%",
    'Matlab': "80%",
    'C/C++': "90%",
    'Assembly': "60%"
}

def personal_skills(name, *skills, **skills_with_progress):
    print(f"Hola, {name} \n Skills without progress is: ")
    for skill in skills:
        print(f"- {skill}")

    print("Skills without progress is: ")
    for skill_key, skill_value in skills_with_progress.items():
        print(f"- {skill_key} => {skill_value}")


personal_skills("JohnWick", "James", "Bond", Python="90%", GoTo="12$")

print("=============================================")

personal_skills("JohnWick", Tuple, Python="90%", GoTo="12$")

print("=============================================")

personal_skills("JohnWick", *Tuple, Python="90%", GoTo="12$")
print("=============================================")

personal_skills("JohnWick", *Tuple, MySkills, Python="90%", GoTo="12$")

print("=============================================")

personal_skills("JohnWick", *Tuple, **MySkills, Python="90%", GoTo="12$")