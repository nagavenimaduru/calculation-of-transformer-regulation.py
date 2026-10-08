# DC Motor Torque Calculator

print("===== DC Motor Torque Calculator =====")

# Input values
power = float(input("Enter motor output power (W): "))
speed = float(input("Enter motor speed (RPM): "))

# Calculate angular speed
angular_speed = (2 * 3.14159 * speed) / 60

# Calculate torque
torque = power / angular_speed

print("\n===== Results =====")
print(f"Output Power : {power:.2f} W")
print(f"Speed        : {speed:.2f} RPM")
print(f"Angular Speed: {angular_speed:.2f} rad/s")
print(f"Torque       : {torque:.2f} N-m")
