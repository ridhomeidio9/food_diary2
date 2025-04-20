import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analisis Nutrisi Makanan", page_icon="🍽️")

# Judul
st.title("🍽️ Analisis Nutrisi Makanan")
st.write("Pilih makanan dan masukkan berat (gram/ml) untuk melihat informasi gizinya.")

# Database nutrisi per 100g / ml / porsi standar
nutrisi_makanan = {
    "Nasi Putih": {"Kalori": 130, "Karbohidrat": 28, "Protein": 2.7, "Gula": 0.1},
    "Ayam Goreng": {"Kalori": 239, "Karbohidrat": 0, "Protein": 27, "Gula": 0},
    "Tahu Goreng": {"Kalori": 271, "Karbohidrat": 9.2, "Protein": 14, "Gula": 0.6},
    "Tempe Goreng": {"Kalori": 200, "Karbohidrat": 7.7, "Protein": 18, "Gula": 0},
    "Telur Rebus": {"Kalori": 155, "Karbohidrat": 1.1, "Protein": 13, "Gula": 1.1},
    "Apel": {"Kalori": 52, "Karbohidrat": 14, "Protein": 0.3, "Gula": 10},
    "Pisang": {"Kalori": 89, "Karbohidrat": 23, "Protein": 1.1, "Gula": 12},
    "Susu Full Cream": {"Kalori": 61, "Karbohidrat": 4.8, "Protein": 3.2, "Gula": 5.1},
    "Roti Tawar": {"Kalori": 265, "Karbohidrat": 49, "Protein": 9, "Gula": 5},
    "Mie Instan Rebus": {"Kalori": 370, "Karbohidrat": 50, "Protein": 8, "Gula": 2},
    "Kentang Rebus": {"Kalori": 87, "Karbohidrat": 20, "Protein": 1.9, "Gula": 0.9},
    "Wortel": {"Kalori": 41, "Karbohidrat": 10, "Protein": 0.9, "Gula": 4.7},
    "Bayam": {"Kalori": 23, "Karbohidrat": 3.6, "Protein": 2.9, "Gula": 0.4},
    "Sop Ayam": {"Kalori": 74, "Karbohidrat": 6, "Protein": 7, "Gula": 1},
    "Bakso Sapi": {"Kalori": 260, "Karbohidrat": 16, "Protein": 13, "Gula": 2.2},
    "Sate Ayam + Lontong": {"Kalori": 250, "Karbohidrat": 20, "Protein": 14, "Gula": 3},
    "Rendang Sapi": {"Kalori": 193, "Karbohidrat": 5.3, "Protein": 16.5, "Gula": 2},
    "Sambal Goreng Kentang": {"Kalori": 150, "Karbohidrat": 18, "Protein": 2, "Gula": 3},
    "Gado-Gado": {"Kalori": 140, "Karbohidrat": 10, "Protein": 7, "Gula": 4},
    "Es Teh Manis": {"Kalori": 70, "Karbohidrat": 17, "Protein": 0, "Gula": 16},
    "Jus Jeruk": {"Kalori": 45, "Karbohidrat": 10, "Protein": 0.7, "Gula": 8.4}
}

# Pilih makanan
makanan_dipilih = st.selectbox("Pilih Makanan", list(nutrisi_makanan.keys()))

# Input berat
berat = st.number_input("Masukkan berat makanan (gram/ml)", min_value=1, max_value=1000, value=100)

# Analisis dan hasil
if makanan_dipilih and berat:
    st.subheader(f"📊 Informasi Gizi: {makanan_dipilih} ({berat}g)")

    data = nutrisi_makanan[makanan_dipilih]
    kalori = data["Kalori"] * berat / 100
    karbo = data["Karbohidrat"] * berat / 100
    protein = data["Protein"] * berat / 100
    gula = data["Gula"] * berat / 100

    # Tampilkan metrik
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Kalori (kkal)", f"{kalori:.2f}")
        st.metric("Karbohidrat (g)", f"{karbo:.2f}")
    with col2:
        st.metric("Protein (g)", f"{protein:.2f}")
        st.metric("Gula (g)", f"{gula:.2f}")

    # Pie chart
    st.subheader("🍥 Komposisi Gizi")
    fig, ax = plt.subplots()
    labels = ['Karbohidrat', 'Protein', 'Gula']
    sizes = [karbo, protein, gula]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Dibuat oleh Mahasiswa Jurusan Pangan | Streamlit Nutrisi App 2025")
