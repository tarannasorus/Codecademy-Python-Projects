train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9


f100_in_celsius = f_to_c(82)
print(f100_in_celsius)

def c_to_f(c_temp):
 return c_temp * (9/5) + 32

c0_in_fahrenheit = c_to_f(27)
print(c0_in_fahrenheit)

def get_force(train_mass, train_acceleration):
  return train_mass * train_acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force")
c = 3*10**8
def get_energy(mass, c):
  return mass * (c*c)
bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  return train_force * train_distance
train_work = train_force * train_distance
print(train_work)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")