import optuna
import time

print("# Start Server")
server = optuna.server.start_nb()
time.sleep(1)

print("# Create Client")
client = optuna.client.Client()

print("# Create Study(1)")
study = client.create_study()
print("# => ", study)

print("# Create Study(2)")
study = client.create_study()
print("# => ", study)
client.close_study(study)

print("# Create Study(3)")
study = client.create_study()
print("# => ", study)

print("# Start Trial")
trial = client.start_trial(study)
print("=> ", trial)
