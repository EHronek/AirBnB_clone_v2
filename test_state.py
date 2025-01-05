from models.state import State
new_state = State(name="California")
new_state.save()
print(new_state.id)

