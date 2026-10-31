
# ==========================================
# PROYEK 1B - STRUKTUR DATA TREE
# SISTEM SILSILAH ORGANISASI UIN SUSKA RIAU
# ==========================================


class Node:
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.children = []


class Tree:
    def __init__(self, root):
        self.root = root

    # Operasi penyisipan data
    def insert_node(self, id_pegawai, nama, jabatan, id_atasan):
        atasan = self.search_node(id_atasan, "id")

        if atasan is not None:
            node_baru = Node(id_pegawai, nama, jabatan)
            atasan.children.append(node_baru)
            print(f"Data {nama} berhasil ditambahkan.")
        else:
            print("Atasan tidak ditemukan.")

    # Operasi pencarian data
    def search_node(self, keyword, berdasarkan="nama"):
        return self._search(self.root, keyword, berdasarkan)

    def _search(self, node, keyword, berdasarkan):
        if berdasarkan == "id" and node.id_pegawai == keyword:
            return node
        elif berdasarkan == "nama" and node.nama.lower() == keyword.lower():
            return node
        elif berdasarkan == "jabatan" and node.jabatan.lower() == keyword.lower():
            return node

        for child in node.children:
            hasil = self._search(child, keyword, berdasarkan)
            if hasil is not None:
                return hasil

        return None

    # Preorder Traversal
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root

        print(f"{node.nama} ({node.jabatan})")

        for child in node.children:
            self.preorder_traversal(child)

    # Inorder Traversal
    # General Tree menggunakan aturan:
    # anak pertama - node - anak berikutnya
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if len(node.children) > 0:
            self.inorder_traversal(node.children[0])

        print(f"{node.nama} ({node.jabatan})")

        for child in node.children[1:]:
            self.inorder_traversal(child)

    # Postorder Traversal
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        for child in node.children:
            self.postorder_traversal(child)

        print(f"{node.nama} ({node.jabatan})")


# 3. MEMBUAT DATA AWAL ORGANISASI

rektor = Node("P001", "Ahmad", "Rektor")

organisasi = Tree(rektor)

# Menambahkan dekan
organisasi.insert_node("P002", "Budi", "Dekan FST", "P001")
organisasi.insert_node("P003", "Citra", "Dekan FEB", "P001")

# Menambahkan ketua program studi
organisasi.insert_node("P004", "Dedi", "Ketua Prodi TI", "P002")
organisasi.insert_node("P005", "Eka", "Ketua Prodi SI", "P002")
organisasi.insert_node("P006", "Harto", "Ketua Prodi AK", "P003")

# Menambahkan dosen
organisasi.insert_node("P007", "Gina", "Dosen TI", "P004")
organisasi.insert_node("P008", "Hadi", "Dosen SI", "P005")
organisasi.insert_node("P009", "Intan", "Dosen AK", "P006")


# 4. MENAMPILKAN HASIL TRAVERSAL

print("\n===== PREORDER TRAVERSAL =====")
organisasi.preorder_traversal()

print("\n===== INORDER TRAVERSAL =====")
organisasi.inorder_traversal()

print("\n===== POSTORDER TRAVERSAL =====")
organisasi.postorder_traversal()


# 5. CONTOH PENCARIAN DATA

print("\n===== PENCARIAN PEGAWAI =====")
hasil = organisasi.search_node("Gina", "nama")

if hasil:
    print("Data ditemukan!")
    print("ID       :", hasil.id_pegawai)
    print("Nama     :", hasil.nama)
    print("Jabatan  :", hasil.jabatan)
else:
    print("Data tidak ditemukan.")


# 6. CONTOH PENAMBAHAN DATA BARU

print("\n===== PENAMBAHAN PEGAWAI BARU =====")
organisasi.insert_node(
    "P010", "Joko", "Dosen Baru", "P004"
)

print("\n===== PREORDER SETELAH PENAMBAHAN =====")
organisasi.preorder_traversal()
