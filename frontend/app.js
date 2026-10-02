const form = document.getElementById("roastForm");

const urlInput = document.getElementById("instagramUrl");

const button = document.getElementById("roastButton");

const loading = document.getElementById("loading");

const resultContainer = document.getElementById("resultContainer");

const result = document.getElementById("result");

const error = document.getElementById("error");


form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = urlInput.value.trim();

    if (!/^[a-zA-Z0-9._-]+$/.test(username)) {
        error.textContent =
            "Instagram username hanya boleh menggunakan huruf, angka, titik, underscore, dan strip.";

        error.classList.remove("hidden");
        return;
    }

    const instagramUrl = `https://www.instagram.com/${username}/`;

    if (!instagramUrl) {
        return;
    }

    // Reset UI
    error.classList.add("hidden");
    resultContainer.classList.add("hidden");

    loading.classList.remove("hidden");

    button.disabled = true;
    button.textContent = "🍴Sedang roasting...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/roast",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    instagram_url: instagramUrl
                })
            }
        );

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`
            );
        }

        const data = await response.json();

        result.innerHTML = marked.parse(data.result);

        resultContainer.classList.remove("hidden");

    } catch (err) {
        console.error(err);
        error.textContent ="Gagal terhubung ke backend. Pastikan FastAPI dan Ollama sedang berjalan.";
        error.classList.remove("hidden");

    } finally {

        loading.classList.add("hidden");

        button.disabled = false;

        button.textContent = "🍴 Roasting kembali";
    }
});