# -*- coding: utf-8 -*-
"""Praktik Data Science.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kur14jZasnlqWa_XL1jNAztFIW44XWc6

# **Import Library**
"""

# Memanggil Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# **Data Wrangling**

## **Gathering Data**
"""

#Memuat Tabel Customer

customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()

#Memuat Tabel Ordes

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
orders_df.head()

#Memuat Tabel Product

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()

#Memuat Tabel Sales

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()

"""## **Assessing Data**

### **Data Customer**
"""

#Info Customer

customers_df.info()

#Melihat Missing Value

customers_df.isna().sum()

#Memeriksa Data Duplikasi

print("Jumlah Duplikasi :", customers_df.duplicated().sum())

#Pemeriksaan Menggunakan Describe()

customers_df.describe()

"""### **Data Order**"""

#info Order


orders_df.info()

#Memeriksa Data Duplikasi
print("Jumlah Duplikasi :", orders_df.duplicated().sum())

#Pemeriksaan Menggunakan Describe()
orders_df.describe()

"""### **Data Product**"""

#Info Product
product_df.info()

#Memeriksa Data Duplikasi
print("Jumlah Duplikasi :", product_df.duplicated().sum())

#Pemeriksaan Menggunakan Describe()
product_df.describe()

"""### **Data Sales**"""

#info Sales
sales_df.info()

#Memeriksa Missing Value
sales_df.isna().sum()

#Memeriksa Data Duplikasi
print("Jumlah Duplikasi :", sales_df.duplicated().sum())

#Pemeriksaan Menggunakan Describe()
sales_df.describe()

"""## **Cleaning Data**

### **Membersihkan Data Customer**

**Menghilangkan DUplikasi**
"""

#Menghilangkan dupliated data
customers_df.drop_duplicates(inplace=True)

#Memeriksa Duplikasi
print("Jumlah Duplikasi :", customers_df.duplicated().sum())

"""**Menangani Missing Value**"""

#Melihat data yang mengandung Missing Value dengan Filtering
customers_df[customers_df.gender.isna()]

#Mengatasi Missing Value dengan Imputation,
#kolom gender kategori jadi mengisi dengan nilai yang dominan
customers_df.gender.value_counts()

#Mengisi Missing Value
customers_df.fillna(value="Prefer not to say", inplace=True)

#Mengecek dan Memastikan Mising Value
customers_df.isna().sum()

"""**Menangani Inaccurate Value**"""

#melihat data baris data yang mengandung inaccurate value
customers_df[customers_df.age == customers_df.age.max()]

#Mengganti nilai inaccurate dengan replace
customers_df.age.replace(customers_df.age.max(), 70, inplace=True)

#Mengecek Hasil
customers_df[customers_df.age == customers_df.age.max()]

#Mengganti nilai inaccurate dengan replace
customers_df.age.replace(customers_df.age.max(), 40, inplace=True)

#memastikan kembali tidak terdapat inaccurate value
customers_df.describe()

"""### **Membersihkan Data orders**"""

import datetime
#Mengganti tipe data pada kolom order_date & delivery_date dari object menjadi datetime
datetime_columns = ["order_date", "delivery_date"]

for column in datetime_columns:
  orders_df[column] = pd.to_datetime(orders_df[column])

#Mengecek hasilnya dengan info
orders_df.info()

"""### **Membersihkan Data Product**"""

#Menghapus data duplikasi
product_df.drop_duplicates(inplace=True)

#Memastikan hasil Drop
print("Jumlah Duplikasi :", product_df.duplicated().sum())

"""### **Membersihkan Data Sales**"""

#Mengetahui Informasi Missing Value
sales_df[sales_df.total_price.isna()]

#Berdasarkan tampilan data tersebut, kita menemukan bahwa nilai total_price merupakan hasil perkalian antara price_per_unit dan quantity
sales_df["total_price"] = sales_df["price_per_unit"] * sales_df["quantity"]

#Mengecek jumlah missing value pada sales_df
sales_df.isna().sum()

"""# **Exploratory Data Analysis**

## **Eksplorasi Data Customer**
"""

#Penggunaan Describe dengan Include = 'all'
customers_df.describe(include="all")

#Pivot Tabel Melihat pelanggan berdasarkan jenis kelamin (gender) dengan method groupby() yang diikuti dengan method agg()
customers_df.groupby(by="gender").agg({
    "customer_id" : "nunique",
    "age" : ["max", "min", "mean", "std"]
})

"""Persebaran jumlah pelanggan berdasarkan kota (city) dan negara bagian (state) dengan method groupby() dan mengurutkannya nilainya menggunakan method sort_values() secara descending"""

customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)

customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=False)

"""## **Eksplorasi Data Order**

Menghitung selisih antar delivery_date dan order_date serta menyimpannya sebagai delivery_time. Dengan menggunakan method **Apply()**. Operasi yang akan kita lakukan ialah menghitung jumlah detik dari delivery_time menggunakan method **total_seconds()**
"""

delivery_time = orders_df["delivery_date"] - orders_df["order_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time/86400)
orders_df.head()

#Rangkuman Parameter Statistik
orders_df.describe(include="all")

"""**Eksplorasi Data orders_df dan customers_df** pada data orders_df terdapat kolom yang berisi informasi terkait customer id pelanggan yang pernah melakukan order. Informasi ini bisa kita gunakan untuk mengidentifikasi pelanggan yang belum pernah melakukan order. Untuk melakukan hal ini, kita bisa membuat sebuah kolom baru bernama “status” pada data customers_df. Kolom tersebut memiliki nilai “Active” untuk pelanggan yang pernah melakukan order setidaknya sekali dan sebaliknya bernilai “Non Active”"""

#Membuat Kolom Baru
customer_id_in_orders_df = orders_df.customer_id.tolist()
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customer_id_in_orders_df else "Non Active")
customers_df.sample(5)

#Mengetahui jumlah pelanggan yang berstatus “Active” dan “Non Active”
customers_df.groupby(by="status").customer_id.count()

"""Untuk memperoleh lebih banyak informasi terkait kedua data tersebut, kita perlu menggabungkan keduanya melalui **proses join atau merge**."""

#Merge orders_df dan customers_df
orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
orders_customers_df.head()

"""Pivot table untuk memperoleh informasi terkait jumlah order berdasarkan kota"""

orders_customers_df.groupby(by="city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)

#Jumlah order berdasarkan state
orders_customers_df.groupby(by="state").order_id.nunique().sort_values(ascending=False)

#Jumlah order berdasarkan gender
orders_customers_df.groupby(by="gender").order_id.nunique().sort_values(ascending=False)

#Jumlah order berdasarkan kelompok usia
orders_customers_df["age_group"] = orders_customers_df.age.apply(lambda x: "Youth" if x <= 24 else ("Seniors" if x > 64 else "Adults"))
orders_customers_df.groupby(by="age_group").order_id.nunique().sort_values(ascending=False)

"""## **Eksplorasi Data product_df dan sales_df**"""

#Menggunakan method Describe sebagai permulaan
product_df.describe(include="all")
sales_df.describe(include="all")

#Mengecek harga termahal dan terendah
product_df.sort_values(by="price", ascending=False)

"""Menggunakan pivot table untuk mencari informasi terkait produk berdasarkan tipe dan nama produknya."""

product_df.groupby(by="product_type").agg({
    "product_id": "nunique",
    "quantity": "sum",
    "price":  ["min", "max"]
})

product_df.groupby(by="product_name").agg({
    "product_id": "nunique",
    "quantity": "sum",
    "price": ["min", "max"]
})

"""Sebagai calon praktisi data yang Andal, tentunya Anda penasaran dengan produk yang paling laris. Nah, untuk menjawab pertanyaan ini, kita perlu menyatukan (merge) tabel product_df dan sales_df"""

#Merge tabel product_df dan sales_df
sales_product_df = pd.merge(
    left=sales_df,
    right=product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
sales_product_df.head()

#Pivot tabel berdasarkan product type
sales_product_df.groupby(by="product_type").agg({
    "sales_id": "nunique",
    "quantity_x": "sum",
    "total_price": "sum"
})

#Pivot Table untuk informasi penjualan berdasarkan nama produk
sales_product_df.groupby(by="product_name"). agg({
    "sales_id" : "nunique",
    "quantity_x" : "sum",
    "total_price" : "sum"
}).sort_values(by="total_price", ascending=False)

"""Melihat pola pembelian berdasarkan demografi pelanggan. Oleh karena itu, kita perlu membuat sebuah DataFrame baru bernama all_df untuk menampung semua informasi dari keempat tabel yang kita miliki"""

#Informasi keempat tabel menjadi 1
all_df = pd.merge(
    left=sales_product_df,
    right=orders_customers_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
all_df.head()

#preferensi pembelian berdasarkan state pelanggan dan tipe produk
all_df.groupby(by=["state", "product_type"]).agg({
    "quantity_x": "sum",
    "total_price": "sum"
})

#untuk mengetahui selera tipe produk pelanggan berdasarkan gender
all_df.groupby(by=["gender", "product_type"]).agg({
    "quantity_x": "sum",
    "total_price": "sum"
})

#untuk mengetahui selera tipe produk pelanggan berdasarkan kelompok usia
all_df.groupby(by=["age_group", "product_type"]).agg({
    "quantity_x": "sum",
    "total_price": "sum"
})

all_df.groupby(by="state").agg({
    "order_id": "nunique",
    "total_price": "sum"
}).sort_values(by="total_price", ascending=False)

"""# **Visualisasi Data**

## **Bagaimana Performa Penjualan dan Revenue Perusahaan dalam Beberapa Bulan Terakhir?**

Method bernama **resample()**. Method ini memungkinkan kita untuk mengubah frekuensi atau melakukan resampling terhadap DataFrame yang memiliki komponen time series. Untuk menggunakan method ini, kita harus mendefinisikan parameter **rule** (mengatur target konversi) dan **on** (nama kolom bertipe datetime yang akan diubah frekuensinya)

Melakukan resample data order_date menjadi bulanan serta melakukan agregasi terhadap data tersebut untuk memperoleh informasi terkait jumlah order dan total revenue yang diperoleh tiap bulan
"""

monthly_orders_df = all_df.resample(rule='M', on='order_date').agg({
    "order_id": "nunique",
    "total_price": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)
monthly_orders_df.head()

"""Menggunakan bentuk line chart untuk memvisualkan informasi terkait jumlah order dan total revenue yang diperoleh tiap bulan."""

monthly_orders_df = all_df.resample(rule='M', on='order_date').agg({
    "order_id": "nunique",
    "total_price": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime('%B') #mengubah format order date menjadi nama bulan

monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(monthly_orders_df["order_date"], monthly_orders_df["order_count"], marker='o', linewidth=2, color="blue")
plt.title("Number of Orders per Month (2021)", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

"""Berdasarkan visualisasi di atas, dapat melihat bahwa jumlah order terbanyak terjadi pada bulan Maret. Selain itu, kita juga dapat melihat adanya penurunan jumlah order yang cukup signifikan pada bulan Februari, April, Mei, dan Oktober.

Tentunya penurunan tersebut akan berdampak pada total revenue yang diperoleh perusahaan. Untuk memvalidasi hal ini, membuat line chart
"""

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_orders_df["order_date"],
    monthly_orders_df["revenue"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
plt.title("Total Revenue per Month (2021)", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

"""## **Produk Apa yang Paling Banyak dan Paling Sedikit Terjual?**

Membuat sebuah DataFrame baru guna menampung informasi terkait jumlah penjualan tiap produk
"""

sum_order_items_df = all_df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()
sum_order_items_df.head(15)

"""Membuat dua buah visualisasi data dalam satu gambar visual. Untuk melakukan ini, gunakanlah function **subplot()**. Dengan menggunakan object berupa **fig** dan **ax**.  **ax[0]** merupakan object untuk kanvas pertama (bagian kanan) dan **ax[1]** merupakan object untuk kanvas kedua (bagian kiri)."""

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(26, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

plt.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)
plt.show()

"""## **Bagaimana Demografi Pelanggan yang Kita Miliki?**

Untuk menjawab hal ini, bisa membuat DataFrame baru untuk menampung informasi terkait jumlah pelanggan untuk demografi tertentu seperti gender, state, dll

### **Berdasarkan gender**
"""

bygender_df = all_df.groupby(by="gender").customer_id.nunique().reset_index()
bygender_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

plt.figure(figsize=(10, 5))

sns.barplot(
    y="customer_count",
    x="gender",
    data=bygender_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)
plt.title("Number of Customer by Gender", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

"""### **Berdasarkan age**"""

byage_df = all_df.groupby(by="age_group").customer_id.nunique().reset_index()
byage_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
byage_df
byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])
plt.figure(figsize=(10, 5))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    y="customer_count",
    x="age_group",
    data=byage_df.sort_values(by="age_group", ascending=False),
    palette=colors_
)
plt.title("Number of Customer by Age", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

"""### **Berdasarkan states**"""

bystate_df = all_df.groupby(by="state").customer_id.nunique().reset_index()
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
bystate_df
plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count",
    y="state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
plt.title("Number of Customer by States", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()

"""Untuk menjawab tiga pertanyaan analisis terakhir, kita bisa menggunakan teknik analisis lanjutan yang bernama RFM analysis. Sederhananya, RFM analysis merupakan salah satu metode yang umum digunakan untuk melakukan segmentasi pelanggan (mengelompokkan pelanggan ke dalam beberapa kategori) berdasarkan tiga parameter, yaitu recency, frequency, dan monetary.

* Recency: parameter yang digunakan untuk melihat kapan terakhir seorang pelanggan melakukan transaksi
* Frequency: parameter ini digunakan untuk mengidentifikasi seberapa sering seorang pelanggan melakukan transaksi
* Monetary: parameter terakhir ini digunakan untuk mengidentifikasi seberapa besar revenue yang berasal dari pelanggan tersebut
"""

rfm_df = all_df.groupby(by="customer_id", as_index=False).agg({
    "order_date": "max", # mengambil tanggal order terakhir
    "order_id": "nunique", # menghitung jumlah order
    "total_price": "sum" # menghitung jumlah revenue yang dihasilkan
})
rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]

# menghitung kapan terakhir pelanggan melakukan transaksi (hari)
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
recent_date = orders_df["order_date"].dt.date.max()
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
rfm_df.head()

"""Mengidentifikasi best customer berdasarkan parameter frequency, monetary, dan recancy"""

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis ='x', labelsize=15)

sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)

sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)
plt.show()

"""**Mengurutkan customer berdasarkan recency, frequency, & monetary score**"""

rfm_df['r_rank'] = rfm_df['recency'].rank(ascending=False)
rfm_df['f_rank'] = rfm_df['frequency'].rank(ascending=True)
rfm_df['m_rank'] = rfm_df['monetary'].rank(ascending=True)

rfm_df.head()

# normalizing the rank of the customers
rfm_df['r_rank_norm'] = (rfm_df['r_rank']/rfm_df['r_rank'].max())*100
rfm_df['f_rank_norm'] = (rfm_df['f_rank']/rfm_df['f_rank'].max())*100
rfm_df['m_rank_norm'] = (rfm_df['m_rank']/rfm_df['m_rank'].max())*100

rfm_df.drop(columns=['r_rank', 'f_rank', 'm_rank'], inplace=True)

rfm_df.head()

rfm_df['RFM_score'] = 0.15*rfm_df['r_rank_norm']+0.28 * \
    rfm_df['f_rank_norm']+0.57*rfm_df['m_rank_norm']
rfm_df['RFM_score'] *= 0.05
rfm_df = rfm_df.round(2)
rfm_df[['customer_id', 'RFM_score']].head(7)

"""**Segmentasi customer berdasarkan RFM_score**"""

rfm_df["customer_segment"] = np.where(
    rfm_df['RFM_score'] > 4.5, "Top customers", (np.where(
        rfm_df['RFM_score'] > 4, "High value customer",(np.where(
            rfm_df['RFM_score'] > 3, "Medium value customer", np.where(
                rfm_df['RFM_score'] > 1.6, 'Low value customers', 'lost customers'))))))

rfm_df[['customer_id', 'RFM_score', 'customer_segment']].head(20)

customer_segment_df = rfm_df.groupby(by="customer_segment", as_index=False).customer_id.nunique()
customer_segment_df

customer_segment_df['customer_segment'] = pd.Categorical(customer_segment_df['customer_segment'], [
    "lost customers", "Low value customers", "Medium value customer",
    "High value customer", "Top customers"
])

plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="customer_id",
    y="customer_segment",
    data=customer_segment_df.sort_values(by="customer_segment", ascending=False),
    palette=colors_
)
plt.title("Number of Customer for Each Segment", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()

#Menyimpan Berkas
all_df.to_csv("all_data.csv", index=False)