"""
Bloom filter Pokedex.

Using Murmer and FNV non-cryptographic hash functions

"""
import pyhash

bit_vector = [0] * 20

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output fo FNV hash functions for Pikachu and Charmander
fnv_pika = fnv('Pikachu') % 20
murmur_char = murmur('Charmander') % 20

fnv_char = fnv('Charmander') % 20
murmur_pika = murmur('Pikachu') % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

fnv_bulb = fnv('Bulbasaur') % 20
murmur_bulb = murmur('Bulbasaur') % 20


