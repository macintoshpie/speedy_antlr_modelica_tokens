from modelica.print_tokens import print_tokens

print(" === USING C++ IMPLEMENTATION ===")
print_tokens('DCMotor.mo', use_cpp=True)
print("\n\n\n\n === USING PYTHON IMPLEMENTATION ===")
print_tokens('DCMotor.mo', use_cpp=False)
