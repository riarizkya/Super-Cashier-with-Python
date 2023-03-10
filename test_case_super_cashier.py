# -*- coding: utf-8 -*-
"""Test Case - Super Cashier.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TRG74mgYoAP1OUx8EZTsZEF1A1RlRC8o

# TEST CASES

In this file, we will test whether the code runs well or not using the test cases provided.
"""

# importing the module and give it a shorter name 

import super_cashier as sc

trnsct_123 = sc.Transactions()

"""# TEST 1: Adding Items

In this test case, the customer wants to make a transaction by adding some items alongside the quantity of the items and the prices:



*   Nama item: Ayam Goreng, Qty: 2, Harga: 20000
*   Nama item: Pasta Gigi, Qty: 3, Harga: 15000
"""

trnsct_123.tambah_barang('Ayam Goreng', 2, 20000)
trnsct_123.tambah_barang('Pasta Gigi', 3, 15000)

"""# TEST 2: Deleting an Item

The customer wants to delete the item 'Pasta Gigi' from the list.
"""

trnsct_123.hapus_barang('Pasta Gigi')

"""# TEST 3: Resetting the Transaction

The customer wants to delete (reset) the entire transaction.
"""

trnsct_123.reset_transaksi()

"""# TEST 4: Showing Total Price (After Discount) & Qty """

trnsct_123.tambah_barang('Ayam Goreng', 10, 15000)
trnsct_123.tambah_barang('Pasta Gigi', 10, 25000)
trnsct_123.menampilkan_daftar_barang()
