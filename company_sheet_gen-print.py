import random
import win32print

class Employee:
    def __init__(self, role):
        self.role = role
        self.stats = ["BODY", "DODGE", "FIGHT", "FIRST AID", "GUILE", "REPAIR", "RESEARCH", "SEARCH", "SNEAK", "HACK"]
        self.points_dict = {stat: 0 for stat in self.stats}
        self.career_stats = ["COMBAT", "MEDICINE", "HACK", "ENGINEER", "SCIENCE", "TECH"]
        self.career_dict = {stat: 0 for stat in self.career_stats}
        self.health = 0
        self.aware = 0
        self.job = ""
        self.team_stress = ""
        self.loadout = []
        self.item = ""

    def assign_points(self):
        if self.role == "soldier":
            self.points_dict["BODY"] += 1
            self.points_dict["FIGHT"] += 1
            self.points_dict["SNEAK"] += 1
            self.career_dict["COMBAT"] += 1
        elif self.role == "scientist":
            self.points_dict["RESEARCH"] += 1
            self.points_dict["SEARCH"] += 1
            self.points_dict["SNEAK"] += 1
            self.career_dict["SCIENCE"] += 1
        elif self.role == "medic":
            self.points_dict["BODY"] += 1
            self.points_dict["DODGE"] += 1
            self.points_dict["FIRST AID"] += 1
            self.career_dict["MEDICINE"] += 1
        elif self.role == "engineer":
            self.points_dict["DODGE"] += 1
            self.points_dict["REPAIR"] += 1
            self.points_dict["SEARCH"] += 1
            self.career_dict["ENGINEER"] += 1
        elif self.role == "technician":
            self.points_dict["HACK"] += 1
            self.points_dict["REPAIR"] += 1
            self.points_dict["RESEARCH"] += 1
            self.career_dict["TECH"] += 1

        # Assign remaining points randomly to other stats
        remaining_points = 2
        while remaining_points > 0:
            stat_to_increase = random.choice(self.stats)
            if self.points_dict[stat_to_increase] < 1:
                self.points_dict[stat_to_increase] += 1
                remaining_points -= 1

    def assign_attributes(self):
        if self.role == "soldier":
            self.health = 5
            self.aware = 2
            self.job = "Engage with threats to protect ARC team and survivors\nUtilize tactics to minimize team casualties"
            self.team_stress = "Other employees take stress when the Soldier fails Fight or Combat rolls"
            self.loadout = ["Knife", "Handgun", "Body Armor"]
            self.item = random.choice(["Ring", "Shell", "Scarf", "Patch", "Employee Handbook", "Old Cigar", "Combat Medal", "Glass Bead", "Dented Flask", "Partially Burnt Photo"])
            self.loadout.append(self.item)  # Add item to loadout
        elif self.role == "scientist":
            self.health = 3
            self.aware = 1
            self.job = "Recover Company Research data, specimens or prototypes"
            self.team_stress = "Other employees take stress when the Scientist fails Research or Science rolls"
            self.loadout = ["Field Research Kit", "Flashlight"]
            self.item = random.choice(["Microscope Slide", "Beat-up Notebook", "Fountain Pen", "Antique Snake Oil Vial", "Laminated Scientific Method Card", "Patch 'Control Group'", "Folded Textbook Page", "Half of a Locket", "Brass Pocket Ruler", "Two Snake Vertebrae"])
            self.loadout.append(self.item)  # Add item to loadout
        elif self.role == "medic":
            self.health = 4
            self.aware = 2
            self.job = "Ensure the physical well-being of the team and any survivors"
            self.team_stress = "Other employees take stress when the Medic fails First Aid or Medicine rolls"
            self.loadout = ["Field Kit", "Painkillers", "Scalpel"]
            self.item = random.choice(["Petoskey Stone", "Caduceus Necklace", "Old mp3 Player", "Patch 'Good For Health'", "Embroidered Handkerchief", "Aviator Sunglasses", "Sewing Kit", "Sour Candies", "Casino Chip", "Harmonica"])
            self.loadout.append(self.item)  # Add item to loadout
        elif self.role == "engineer":
            self.health = 4
            self.aware = 1
            self.job = "Protect and/or repair Company assets.\nUtilize infrastructure to accomplish goals"
            self.team_stress = "Other employees take stress when the Engineer fails Repair or Engineer rolls"
            self.loadout = ["Compact Toolkit", "Digital Schematics"]
            self.item = random.choice(["Lucky Screwdriver", "Welding Goggles", "Worn Work Gloves", "Patch 'BunkerBuster'", "Magnifying Glass w/Light", "Carpenter Pencil", "Engraved Lighter", "Large Bolt", "Fidget Spinner", "Turkey Jerky"])
            self.loadout.append(self.item)  # Add item to loadout
        elif self.role == "technician":
            self.health = 3
            self.aware = 1
            self.job = "Bypass digital security protocols.\nUtilize digital assets to accomplish goals"
            self.team_stress = "Other employees take stress when the Technician fails Hack or Tech rolls"
            self.loadout = ["Electronic Toolkit", "Personal Digital Device"]
            self.item = random.choice(["USB drive with pet code", "Patch 'ICE Breaker'", "Handheld game device", "Patch 'F Key'", "Dented Pocket Watch", "Consumer Candy Bar", "Tinted Glasses", "Digital Timer", "Ten Sided Die", "Flavored Gum"])
            self.loadout.append(self.item)  # Add item to loadout

def generate_fake_name():
    # Lists of syllables to create a name
    prefixes = ["al", "be", "ca", "de", "el", "fi", "ga", "hi", "jo", "ki", "le", "ma", "no", "op", "pa", "qu", "ra", "si", "tu", "va", "we", "xi", "yo", "za"]
    middles = ["ab", "ba", "ce", "de", "el", "fo", "ga", "ho", "in", "jo", "ke", "le", "mo", "na", "op", "po", "qu", "ri", "sa", "ta", "ur", "vi", "we", "xi", "yo", "za"]
    suffixes = ["al", "be", "cy", "do", "el", "fa", "ga", "ho", "ic", "jo", "ka", "la", "mo", "ny", "op", "py", "qu", "ra", "si", "to", "va", "we", "xi", "yo", "za"]
    
    # Randomly select syllables
    first_name = random.choice(prefixes) + random.choice(middles)
    last_name = random.choice(middles) + random.choice(suffixes)
    
    # Capitalize the first letter of each name
    fake_name = first_name.capitalize() + " " + last_name.capitalize()
    return fake_name

def pick_random_role():
    roles = ["soldier", "scientist", "medic", "engineer", "technician"]
    return random.choice(roles)

def display_pips(pips):
    return (( "☒ " * pips) + ( "☐ " * (3-pips)))

if __name__ == "__main__":
    role = pick_random_role()
    
    employee = Employee(role)
    employee.assign_points()
    employee.assign_attributes()
    fake_name = generate_fake_name()
    
#  open the printer?
    printer_name = win32print.GetDefaultPrinter()
    with open(printer_name, "w",encoding='utf-8') as printer:
    
        printer.write(f"NAME: {fake_name}")
        printer.write(f"CAREER: {employee.role.capitalize()}")
        printer.write(f"\nHEALTH   STRESS   DRIVE")
        printer.write(f"=====  =====  =====")
        printer.write(f"| {employee.health} |  |   |  |   |")
        printer.write(f"=====  =====  =====")
        printer.write(f"AWARE: {display_pips(employee.aware)}")
        printer.write("SKILLS")
        for stat, points in employee.points_dict.items():
            printer.write(f"{stat}: " + display_pips(points))

        printer.write("CAREER")
        for stat, points in employee.career_dict.items():
            printer.write(f"{stat}: " + display_pips(points))

        printer.write(f"╔═══════════════════════╗")
        printer.write(f"Job: {employee.job}")
        printer.write(f"╠═══════════════════════╣")
        printer.write(f"Team Stress: {employee.team_stress}")
        printer.write(f"╠═══════════════════════╣")
        tmp_loadout = "Loadout:", ", ".join(employee.loadout)
        printer.write(f"{tmp_loadout}")
        printer.write(f"╚═══════════════════════╝")
