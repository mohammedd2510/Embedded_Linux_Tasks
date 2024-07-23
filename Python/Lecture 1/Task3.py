# Import the 'os' module to access operating system-related functionality, including environment variables.
import os

# Print a separator for clarity.
print('*----------------------------------*')

# Print all environment variables.
print(os.environ)
# Print a separator for clarity.
print('*----------------------------------*')

# Access and print the 'HOME' environment variable.
print(os.environ['HOME'])

# Print a separator for clarity.
print('*----------------------------------*')

# Access and print the 'PATH' environment variable.
print(os.environ['PATH'])

# Print a separator for clarity.
print('*----------------------------------*')