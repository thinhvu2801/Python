def a5_1_encrypt(data, key_x, key_y, key_z):
    # Initialize the A5/1 registers
    register_x = key_x
    register_y = key_y
    register_z = key_z

    # Generate the keystream
    keystream = []
    for _ in range(len(data)):
        # Calculate the majority bit
        majority_bit = (register_x[8] & register_y[10]) ^ (register_x[8] & register_z[10]) ^ (register_y[10] & register_z[10])

        # Shift the registers
        if register_x[8] == majority_bit:
            register_x = [register_x[18] ^ register_x[17] ^ register_x[16] ^ register_x[13]] + register_x[:-1]
        if register_y[10] == majority_bit:
            register_y = [register_y[21] ^ register_y[20]] + register_y[:-1]
        if register_z[10] == majority_bit:
            register_z = [register_z[22] ^ register_z[21] ^ register_z[20] ^ register_z[7]] + register_z[:-1]

        # Generate the keystream bit
        keystream_bit = register_x[18] ^ register_y[21] ^ register_z[22]

        # Append the keystream bit to the keystream
        keystream.append(keystream_bit)

    # Encrypt the data using the keystream
    encrypted_data = bytes([data[i] ^ keystream[i] for i in range(len(data))])
    return encrypted_data

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def get_key_from_input():
    key_x = list(map(int, input("Nhập khóa key_x (dãy 0 và 1, 23 số): "))) #key_x = [10101010101010101010101]

    key_y = list(map(int, input("Nhập khóa key_y (dãy 0 và 1, 22 số): "))) #key_y = [1100110011001100110011]

    key_z = list(map(int, input("Nhập khóa key_z (dãy 0 và 1, 23 số): "))) #key_z = [11100110011001100110011]

    return key_x, key_y, key_z

# Đường dẫn tới tệp tin input.txt và output.txt
input_file_path = 'input.txt'
output_file_path = 'output2.txt'

# Nhập các số khóa từ bàn phím
key_x, key_y, key_z = get_key_from_input()

# Đọc dữ liệu từ tệp tin input.txt
data = read_file(input_file_path)

# Mã hóa dữ liệu
encrypted_data = a5_1_encrypt(data, key_x, key_y, key_z)

# Ghi kết quả vào tệp tin output2.txt
write_file(output_file_path, encrypted_data)