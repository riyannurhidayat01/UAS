// Function to show selected section
function showSection(sectionId) {
    document.querySelectorAll("section").forEach(section => {
        section.classList.remove("active");
    });
    document.getElementById(sectionId).classList.add("active");
}

// Function to submit order form
function submitOrder() {
    const name = document.getElementById("name").value;
    const item = document.getElementById("item").value;

    if (name && item) {
        alert(`Terima kasih, ${name}! Pesanan Anda untuk ${item} telah berhasil diproses.`);
    } else {
        alert("Harap lengkapi formulir pemesanan.");
    }
}
