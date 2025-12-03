function startLoading() {
    document.getElementById("loading").style.display = "flex";
}

function copyURL() {
    navigator.clipboard.writeText(document.getElementById("urlInput").value);
}

function clearURL() {
    document.getElementById("urlInput").value = "";
}

function toggleMode() {
    document.body.classList.toggle("dark");
}

function removeWM() {
    alert("AI Watermark Remover aktif (versi simulasi).");
}

/* Download history */
window.onload = function () {
    let url = document.getElementById("urlInput")?.value;
    if (url) {
        let history = JSON.parse(localStorage.getItem("history") || "[]");
        history.push(url);
        localStorage.setItem("history", JSON.stringify(history));
    }

    let h = JSON.parse(localStorage.getItem("history") || "[]");
    let container = document.getElementById("history");

    if (container)
        container.innerHTML = h.map(x => `<p>${x}</p>`).join("");
};