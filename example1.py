from taipy import Gui


name = "Lorenzo Drumond"
variable = 100
data = {"Rating": [1, 4, 3, 1, 4, 5, 2, 4, 2],
        "Salary": [100, 450, 340, 120, 290, 600, 250, 430, 220]}

page = """
# First Taipy Web Application

Hello: <|{name}|>

Variable value: <|{variable}|>

Change Value:

<|{variable}|slider|>

Data Chart: <|{data}|chart|mode=markers|x=Rating|y=Salary|type=scatter|>

DataFrame: <|{data}|table|>
"""

Gui(page=page).run()
