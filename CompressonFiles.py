import zlib
import base64
import os

def compress_file(input_file, output_file):
    """Compress a file using zlib and encode it with Base64."""
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)
            base64_data = base64.b64encode(compressed_data)

        with open(output_file, 'wb') as f_out:
            f_out.write(base64_data)

        print(f"File '{input_file}' compressed and encoded successfully to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file(input_file, output_file):
    """Decode a Base64 file and decompress it using zlib."""
    try:
        with open(input_file, 'rb') as f_in:
            base64_data = f_in.read()
            compressed_data = base64.b64decode(base64_data)
            data = zlib.decompress(compressed_data)

        with open(output_file, 'wb') as f_out:
            f_out.write(data)

        print(f"File '{input_file}' decoded and decompressed successfully to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except zlib.error:
        print(f"Error: File '{input_file}' is not a valid compressed file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "example.txt"
    compressed_file = "example_compressed.b64"
    decompressed_file = "example_decompressed.txt"

    # Compress and encode the file
    compress_file(input_file, compressed_file)

    # Decode and decompress the file
    decompress_file(compressed_file, decompressed_file)