def greeting(name, surname):
    """Function greets a person given full name as a string"""
    
    print(f"Hello {name.split()[0]} {surname.split()[1]}, How are you today?")

greeting("John Doe", "Jane Smith")